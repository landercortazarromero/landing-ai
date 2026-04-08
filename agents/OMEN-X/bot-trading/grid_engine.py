"""
OMEN X v3.0 - Grid Trading Engine
Estrategia de grid dinámico para 50% mensual ROI
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class GridStatus(Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    CLOSED = "closed"

@dataclass
class GridLevel:
    """Nivel individual del grid"""
    price: float
    side: str  # "buy" or "sell"
    amount: float
    executed: bool = False
    order_id: Optional[str] = None

@dataclass  
class GridConfig:
    """Configuración del grid"""
    symbol: str
    upper_price: float
    lower_price: float
    grid_levels: int = 20
    total_investment: float = 1000.0
    
    @property
    def grid_spacing(self) -> float:
        """Espaciado entre niveles"""
        return (self.upper_price - self.lower_price) / self.grid_levels

class GridTradingEngine:
    """
    Motor de Grid Trading Dinámico
    
    Características:
    - Grid levels auto-calculados
    - Reinversión automática de profits
    - Detección de tendencia (pausa en breakout)
    - Ajuste dinámico de spacing
    """
    
    def __init__(self, config: GridConfig):
        self.config = config
        self.status = GridStatus.PAUSED
        self.levels: List[GridLevel] = []
        self.active_orders: Dict[str, GridLevel] = {}
        self.profit_accumulated = 0.0
        self.trade_count = 0
        
        self._initialize_grid()
    
    def _initialize_grid(self):
        """Crea los niveles del grid"""
        spacing = self.config.grid_spacing
        investment_per_level = self.config.total_investment / self.config.grid_levels
        
        for i in range(self.config.grid_levels + 1):
            price = self.config.lower_price + (i * spacing)
            
            # Alternamos buy/sell
            side = "buy" if i % 2 == 0 else "sell"
            
            level = GridLevel(
                price=price,
                side=side,
                amount=investment_per_level / price
            )
            self.levels.append(level)
        
        logger.info(f"✅ Grid inicializado: {len(self.levels)} niveles")
        logger.info(f"   Rango: {self.config.lower_price:.2f} - {self.config.upper_price:.2f}")
        logger.info(f"   Spacing: {spacing:.4f} ({spacing/self.config.lower_price*100:.2f}%)")
    
    def check_price(self, current_price: float) -> List[Dict]:
        """
        Verifica si el precio tocó algún nivel del grid
        Retorna lista de señales a ejecutar
        """
        if self.status != GridStatus.ACTIVE:
            return []
        
        signals = []
        
        for level in self.levels:
            if level.executed:
                continue
            
            # Check si precio cruzó el nivel
            if level.side == "buy" and current_price <= level.price:
                signals.append({
                    "action": "buy",
                    "price": level.price,
                    "amount": level.amount,
                    "level_idx": self.levels.index(level)
                })
                level.executed = True
                
            elif level.side == "sell" and current_price >= level.price:
                signals.append({
                    "action": "sell", 
                    "price": level.price,
                    "amount": level.amount,
                    "level_idx": self.levels.index(level)
                })
                level.executed = True
        
        return signals
    
    def calculate_profit(self, buy_price: float, sell_price: float, amount: float) -> float:
        """Calcula profit de un ciclo buy-sell"""
        profit = (sell_price - buy_price) * amount
        # Restar comisiones (0.04% taker en Binance futures)
        fees = (buy_price + sell_price) * amount * 0.0004
        return profit - fees
    
    def detect_breakout(self, prices: List[float]) -> Optional[str]:
        """
        Detecta si hay breakout del rango del grid
        Retorna 'up', 'down', o None
        """
        if len(prices) < 20:
            return None
        
        df = pd.DataFrame({"close": prices})
        
        # EMA 20 para detectar tendencia
        df["ema20"] = df["close"].ewm(span=20).mean()
        df["ema50"] = df["close"].ewm(span=50).mean()
        
        last = df.iloc[-1]
        
        # Breakout alcista
        if last["close"] > self.config.upper_price * 1.02 and last["ema20"] > last["ema50"]:
            return "up"
        
        # Breakout bajista
        if last["close"] < self.config.lower_price * 0.98 and last["ema20"] < last["ema50"]:
            return "down"
        
        return None
    
    def reinitialize_on_breakout(self, breakout_direction: str, new_prices: Tuple[float, float]):
        """Reinicializa grid después de breakout"""
        new_upper, new_lower = new_prices
        
        logger.warning(f"🔄 Breakout detectado: {breakout_direction}")
        logger.warning(f"   Nuevo rango: {new_lower:.2f} - {new_upper:.2f}")
        
        # Cerrar posiciones actuales
        self.status = GridStatus.PAUSED
        
        # Reinicializar con nuevo rango
        self.config.upper_price = new_upper
        self.config.lower_price = new_lower
        self.levels = []
        self._initialize_grid()
        
        # Compounding: añadir profit acumulado
        if self.profit_accumulated > 0:
            reinvestment = self.profit_accumulated * 0.5  # 50% reinversión
            self.config.total_investment += reinvestment
            self.profit_accumulated *= 0.5  # Guardar 50%
            logger.info(f"💰 Reinversión: +{reinvestment:.2f}€")
    
    def get_stats(self) -> Dict:
        """Estadísticas del grid"""
        executed = sum(1 for l in self.levels if l.executed)
        pending = len(self.levels) - executed
        
        return {
            "status": self.status.value,
            "levels_total": len(self.levels),
            "levels_executed": executed,
            "levels_pending": pending,
            "profit_accumulated": self.profit_accumulated,
            "trade_count": self.trade_count,
            "current_investment": self.config.total_investment
        }
    
    def start(self):
        """Activa el grid"""
        self.status = GridStatus.ACTIVE
        logger.info("🚀 Grid ACTIVADO")
    
    def pause(self):
        """Pausa el grid"""
        self.status = GridStatus.PAUSED
        logger.info("⏸️  Grid PAUSADO")
    
    def close(self):
        """Cierra todas las posiciones"""
        self.status = GridStatus.CLOSED
        logger.info("🛑 Grid CERRADO")


class GridBacktester:
    """
    Backtester para Grid Trading
    Simula rendimiento histórico
    """
    
    def __init__(self, engine: GridTradingEngine):
        self.engine = engine
        self.trades = []
        self.equity_curve = []
    
    def run(self, price_data: List[float]) -> Dict:
        """
        Ejecuta backtest con datos históricos
        
        Args:
            price_data: Lista de precios (cada 5 minutos)
        
        Returns:
            Dict con métricas de rendimiento
        """
        self.engine.start()
        
        for i, price in enumerate(price_data):
            # Check niveles
            signals = self.engine.check_price(price)
            
            for signal in signals:
                self._execute_signal(signal, price)
            
            # Check breakout cada 100 velas
            if i > 0 and i % 100 == 0:
                breakout = self.engine.detect_breakout(price_data[max(0, i-50):i])
                if breakout:
                    # Simular reinicialización
                    new_range = self._calculate_new_range(price, breakout)
                    self.engine.reinitialize_on_breakout(breakout, new_range)
                    self.engine.start()
            
            # Registrar equity
            self.equity_curve.append({
                "timestamp": i,
                "price": price,
                "equity": self._calculate_equity(price)
            })
        
        return self._calculate_metrics()
    
    def _execute_signal(self, signal: Dict, current_price: float):
        """Simula ejecución de orden"""
        self.trades.append({
            **signal,
            "executed_price": current_price,
            "timestamp": len(self.trades)
        })
        self.engine.trade_count += 1
    
    def _calculate_new_range(self, current_price: float, direction: str) -> Tuple[float, float]:
        """Calcula nuevo rango tras breakout"""
        volatility = current_price * 0.10  # 10% volatilidad
        
        if direction == "up":
            return (current_price + volatility, current_price)
        else:
            return (current_price, current_price - volatility)
    
    def _calculate_equity(self, current_price: float) -> float:
        """Calcula equity actual"""
        # Simplificación: asumimos mitad en USDT, mitad en crypto
        crypto_value = self.engine.config.total_investment * 0.5 / current_price * current_price
        usdt_value = self.engine.config.total_investment * 0.5
        return crypto_value + usdt_value + self.engine.profit_accumulated
    
    def _calculate_metrics(self) -> Dict:
        """Métricas finales"""
        if not self.equity_curve:
            return {}
        
        initial = self.equity_curve[0]["equity"]
        final = self.equity_curve[-1]["equity"]
        
        total_return = (final - initial) / initial * 100
        
        # Max drawdown
        peak = initial
        max_dd = 0
        for point in self.equity_curve:
            if point["equity"] > peak:
                peak = point["equity"]
            dd = (peak - point["equity"]) / peak * 100
            if dd > max_dd:
                max_dd = dd
        
        return {
            "initial_capital": initial,
            "final_equity": final,
            "total_return_pct": total_return,
            "max_drawdown_pct": max_dd,
            "total_trades": len(self.trades),
            "trades_per_day": len(self.trades) / (len(self.equity_curve) / 288),  # 288 velas/día
            "profit_factor": final / initial if initial > 0 else 0
        }


if __name__ == "__main__":
    # Test básico
    config = GridConfig(
        symbol="BTC/USDT:USDT",
        upper_price=110000,
        lower_price=85000,
        grid_levels=20,
        total_investment=1000
    )
    
    engine = GridTradingEngine(config)
    print(engine.get_stats())
