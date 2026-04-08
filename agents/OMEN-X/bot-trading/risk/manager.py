"""
OMEN X - Gestor de Riesgo
Controla exposición, stops, y límites de pérdida
"""

import time
from typing import Dict, Optional
from datetime import datetime

class RiskManager:
    """
    Gestor de riesgo para OMEN X
    Implementa reglas duras de protección de capital
    """
    
    def __init__(self, config: Dict, exchange):
        self.config = config
        self.exchange = exchange
        self.capital = config.get("CAPITAL_INICIAL", 1000)
        self.riesgo_por_trade = config.get("RIESGO_POR_TRADE", 0.015)
        self.max_drawdown = config.get("MAX_DRAWDOWN_DIARIO", 0.05)
        self.max_positions = config.get("MAX_POSICIONES_SIMULTANEAS", 3)
        
        # Tracking
        self.daily_pnl = 0
        self.trades_today = 0
        self.last_reset = datetime.now().date()
    
    def reset_daily(self):
        """Resetea contadores diarios"""
        today = datetime.now().date()
        if today > self.last_reset:
            self.daily_pnl = 0
            self.trades_today = 0
            self.last_reset = today
    
    def can_trade(self) -> Tuple[bool, str]:
        """Verifica si se puede operar"""
        self.reset_daily()
        
        # Check drawdown diario
        if self.daily_pnl < -(self.capital * self.max_drawdown):
            return False, f"⛔ Drawdown límite alcanzado: {self.daily_pnl:.2f}€"
        
        # Check límite de trades diarios
        if self.trades_today >= 10:
            return False, f"⛔ Límite de trades diarios: {self.trades_today}"
        
        # Check capital mínimo
        balance = self.exchange.get_balance()
        if balance < self.capital * 0.5:
            return False, f"⛔ Capital bajo mínimo: {balance:.2f}€"
        
        return True, "✅ OK"
    
    def calculate_position_size(self, entry: float, stop_loss: float) -> float:
        """Tamaño de posición basado en riesgo por trade"""
        risk_amount = self.capital * self.riesgo_por_trade
        stop_distance = abs(entry - stop_loss)
        
        if stop_distance == 0:
            return 0
        
        size = risk_amount / stop_distance
        return round(size, 6)
    
    def update_trade(self, pnl: float = 0):
        """Actualiza tracking después de cada trade"""
        self.daily_pnl += pnl
        self.trades_today += 1
    
    def get_status(self) -> Dict:
        """Estado actual del risk manager"""
        return {
            "capital": self.capital,
            "daily_pnl": self.daily_pnl,
            "trades_today": self.trades_today,
            "drawdown_actual": self.daily_pnl / self.capital * 100,
            "can_trade": self.can_trade()[0]
        }
