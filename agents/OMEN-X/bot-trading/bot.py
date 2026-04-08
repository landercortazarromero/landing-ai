"""
OMEN X v2.0 - Trading Bot Principal con Portfolio de Estrategias
Ejecuta consenso de 3 estrategias en Binance Testnet
"""

import time
import schedule
import os
import pandas as pd
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Módulos propios
from core.exchange import ExchangeConnector
from core.telegram import TelegramAlerts
from core.dashboard import DashboardServer
from strategies.portfolio import StrategyPortfolio
from risk.manager import RiskManager
from config import *

# Logging
import logging
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class OMENXBot:
    """OMEN X - Agente Autónomo de Trading con Portfolio de Estrategias"""
    
    def __init__(self):
        self.config = {
            "CAPITAL_INICIAL": CAPITAL_INICIAL,
            "RIESGO_POR_TRADE": RIESGO_POR_TRADE,
            "MAX_DRAWDOWN_DIARIO": MAX_DRAWDOWN_DIARIO,
            "MAX_POSICIONES_SIMULTANEAS": MAX_POSICIONES_SIMULTANEAS,
            **ESTRATEGIA_CONFIG
        }
        
        # Inicializar módulos
        self.exchange = ExchangeConnector(MODO)
        self.strategy = StrategyPortfolio(self.config)  # Portfolio de 3 estrategias
        self.risk = RiskManager(self.config, self.exchange)
        self.telegram = TelegramAlerts()
        self.dashboard = DashboardServer()
        
        # Estado
        self.positions = []
        self.is_running = False
        self.stats = {
            "total_trades": 0,
            "wins": 0,
            "losses": 0,
            "best_trade": 0,
            "worst_trade": 0
        }
        
        logger.info("🚀 OMEN X v2.0 inicializado (Portfolio Mode)")
    
    def scan_markets(self):
        """Escanea todos los símbolos buscando señales"""
        results = []
        
        for symbol in SYMBOLS:
            try:
                # Obtener datos de múltiplos timeframes
                dfs = {}
                for tf in TIMEFRAMES:
                    data = self.exchange.fetch_ohlcv(symbol, tf, limit=100)
                    dfs[tf] = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
                
                # Usar 5m como timeframe principal
                df = dfs["5m"]
                
                # Generar señal con Portfolio
                signal, params = self.strategy.generate_signal(df)
                
                if signal != "HOLD":
                    results.append({
                        "symbol": symbol,
                        "signal": signal,
                        "params": params
                    })
                    logger.info(f"📡 {symbol}: {signal} — Consensus: {params.get('consensus', {})}")
                    
            except Exception as e:
                logger.error(f"Error escaneando {symbol}: {e}")
        
        return results
    
    def execute_trade(self, signal: Dict):
        """Ejecuta una operación"""
        symbol = signal["symbol"]
        side = signal["signal"].lower()
        params = signal["params"]
        
        # Verificar riesgo
        can_trade, reason = self.risk.can_trade()
        if not can_trade:
            logger.warning(f"No se puede tradear: {reason}")
            return None
        
        # Calcular tamaño
        position_size = self.risk.calculate_position_size(
            params["price"],
            params["stop_loss"]
        )
        
        if position_size < 0.001:
            logger.warning(f"Posición muy pequeña: {position_size}")
            return None
        
        # Crear orden
        order = self.exchange.create_order(
            symbol=symbol,
            side=side,
            amount=position_size,
            price=params["price"]
        )
        
        if order:
            logger.info(f"✅ Orden ejecutada: {side} {symbol}")
            
            # Notificar
            self.telegram.alert_trade(
                signal=signal["signal"],
                symbol=symbol,
                price=params["price"],
                sl=params["stop_loss"],
                tp=params["take_profit"],
                size=position_size
            )
            
            # Update dashboard
            self.dashboard.add_trade({
                "symbol": symbol,
                "signal": signal["signal"],
                "price": params["price"],
                "pnl": 0
            })
        
        return order
    
    def check_positions(self):
        """Monitoriza posiciones abiertas"""
        open_positions = self.exchange.fetch_positions()
        
        for pos in open_positions:
            symbol = pos["symbol"]
            pnl = float(pos.get("unrealizedPnL", 0))
            
            # Update dashboard
            self.dashboard.add_signal({
                "symbol": symbol,
                "signal": "MONITOR",
                "price": pnl
            })
            
            # Alertar si hay pérdidas grandes
            if pnl < -20:
                self.telegram.alert_pnl(symbol, pnl, (pnl/self.risk.capital)*100)
            
            # Check SL/TP
            # (En producción añadir lógica de trailing stop)
    
    def run_cycle(self):
        """Un ciclo completo de análisis y ejecución"""
        if not self.is_running:
            return
            
        logger.info(f"🔄 Ciclo OMEN X - {datetime.now().strftime('%H:%M:%S')}")
        
        # 1. Verificar riesgo
        can_trade, reason = self.risk.can_trade()
        if not can_trade:
            logger.info(f"Oportunidades pausadas: {reason}")
            if "Drawdown" in reason:
                self.telegram.alert_drawdown_limit(self.risk.daily_pnl)
            return
        
        # 2. Escanear mercados
        signals = self.scan_markets()
        
        if not signals:
            logger.info("Sin señales detectadas")
            return
        
        # 3. Ejecutar señales
        for signal in signals[:self.risk.max_positions]:
            self.execute_trade(signal)
        
        # 4. Check posiciones
        self.check_positions()
        
        # 5. Update dashboard
        self.dashboard.update_state({
            "status": "RUNNING" if self.is_running else "STOPPED",
            "capital": self.risk.capital,
            "daily_pnl": self.risk.daily_pnl,
            "trades_today": self.risk.trades_today,
            **self.stats
        })
    
    def hourly_report(self):
        """Reporte hourly"""
        if self.is_running:
            self.telegram.alert_hourly({
                "trades": self.risk.trades_today,
                "pnl": self.risk.daily_pnl,
                "drawdown": (self.risk.daily_pnl / self.risk.capital) * 100,
                "capital": self.risk.capital
            })
    
    def run_testnet(self):
        """Ejecuta en modo testnet 7 días"""
        logger.info("🧪 INICIANDO TESTNET 7 DÍAS")
        self.is_running = True
        
        # Iniciar dashboard
        self.dashboard.start()
        
        # Notificar inicio
        self.telegram.alert_start()
        
        # Schedule jobs
        schedule.every(2).minutes.do(self.run_cycle)  # Cada 2 min para no saturar
        schedule.every(15).minutes.do(self.check_positions)
        schedule.every().hour.do(self.hourly_report)
        
        # 7 días = 168 horas
        end_time = time.time() + (7 * 24 * 60 * 60)
        
        while self.is_running and time.time() < end_time:
            schedule.run_pending()
            time.sleep(1)
        
        # Testnet terminado
        self.testnet_summary()
    
    def testnet_summary(self):
        """Resumen final de testnet"""
        results = {
            "total_trades": self.stats["total_trades"],
            "wins": self.stats["wins"],
            "losses": self.stats["losses"],
            "winrate": (self.stats["wins"] / max(1, self.stats["total_trades"])) * 100,
            "pnl": self.risk.daily_pnl,
            "best_trade": self.stats["best_trade"],
            "worst_trade": self.stats["worst_trade"]
        }
        
        logger.info("🏁 TESTNET FINALIZADO")
        logger.info(f"   Trades: {results['total_trades']}")
        logger.info(f"   Wins: {results['wins']} / Losses: {results['losses']}")
        logger.info(f"   Win Rate: {results['winrate']:.1f}%")
        logger.info(f"   P&L: {results['pnl']:.2f}€")
        
        self.telegram.alert_testnet_end(results)
        
        # Preguntar si continuar en REAL
        logger.info("📢 ¿Continuar en modo REAL? Configura BINANCE_API_KEY y cambia MODO='REAL'")
    
    def stop(self):
        """Detiene el bot"""
        self.is_running = False
        logger.info("🛑 OMEN X DETENIDO")
        self.telegram.send("🛑 OMEN X DETENIDO MANUALMENTE")


if __name__ == "__main__":
    bot = OMENXBot()
    
    try:
        bot.run_testnet()
    except KeyboardInterrupt:
        bot.stop()
