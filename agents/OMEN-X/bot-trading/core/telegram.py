"""
OMEN X - Telegram Alerts
Configuración y gestión de notificaciones
"""

import telegram
import os
from datetime import datetime
from typing import Optional

class TelegramAlerts:
    """
    Gestor de alertas Telegram para OMEN X
    """
    
    def __init__(self, bot_token: str = None, chat_id: str = None):
        self.token = bot_token or os.getenv("TELEGRAM_BOT_TOKEN", "")
        self.chat_id = chat_id or os.getenv("TELEGRAM_CHAT_ID", "")
        self.enabled = bool(self.token and self.chat_id)
        self.bot = None
        
        if self.enabled:
            try:
                self.bot = telegram.Bot(token=self.token)
            except Exception as e:
                print(f"⚠️  Telegram init error: {e}")
                self.enabled = False
    
    def send(self, message: str, parse_mode: str = "Markdown") -> bool:
        """Envía mensaje si está habilitado"""
        if not self.enabled or not self.bot:
            return False
        
        try:
            self.bot.send_message(
                chat_id=self.chat_id,
                text=f"📊 *OMEN X*\n{message}",
                parse_mode=parse_mode
            )
            return True
        except Exception as e:
            print(f"⚠️  Telegram send error: {e}")
            return False
    
    # === ALERTAS PREDEFINIDAS ===
    
    def alert_start(self):
        """Alerta de inicio del bot"""
        self.send(
            f"🚀 *INICIADO*\n"
            f"🕐 {datetime.now().strftime('%H:%M:%S')}\n"
            f"📈 Modo: TESTNET 7 DÍAS"
        )
    
    def alert_trade(self, signal: str, symbol: str, price: float, 
                    sl: float, tp: float, size: float):
        """Alerta de orden ejecutada"""
        emoji = "🟢" if signal == "LONG" else "🔴"
        self.send(
            f"{emoji} *{signal}* {symbol}\n"
            f"💰 Precio: `{price:.6f}`\n"
            f"🛡️ SL: `{sl:.6f}`\n"
            f"🎯 TP: `{tp:.6f}`\n"
            f"📦 Tamaño: {size}"
        )
    
    def alert_pnl(self, symbol: str, pnl: float, pct: float):
        """Alerta de P&L de posición"""
        emoji = "💚" if pnl >= 0 else "❤️"
        self.send(
            f"{emoji} *P&L Update*\n"
            f"{symbol}: {pnl:+.2f}€ ({pct:+.2f}%)"
        )
    
    def alert_stop_hit(self, symbol: str, pnl: float):
        """Alerta de SL o TP activado"""
        emoji = "🛑" if pnl < 0 else "🎯"
        self.send(
            f"{emoji} *CERRADO* {symbol}\n"
            f"P&L: {pnl:+.2f}€"
        )
    
    def alert_warning(self, message: str):
        """Alerta de advertencia"""
        self.send(f"⚠️ *AVISO*\n{message}")
    
    def alert_error(self, message: str):
        """Alerta de error"""
        self.send(f"❌ *ERROR*\n{message}")
    
    def alert_drawdown_limit(self, daily_pnl: float):
        """Alerta de límite de drawdown"""
        self.send(
            f"⛔ *LÍMITE DRAWDOWN*\n"
            f"P&L Diario: {daily_pnl:.2f}€\n"
            f"🔒 Trading pausado hasta mañana"
        )
    
    def alert_hourly(self, stats: dict):
        """Reporte horario"""
        self.send(
            f"📈 *REPORTE {datetime.now().strftime('%H:00')}+\n"
            f"Trades hoy: {stats.get('trades', 0)}\n"
            f"P&L Diario: {stats.get('pnl', 0):+.2f}€\n"
            f"Drawdown: {stats.get('drawdown', 0):.2f}%\n"
            f"Capital: {stats.get('capital', 0):.2f}€"
        )
    
    def alert_testnet_end(self, results: dict):
        """Reporte final de testnet"""
        self.send(
            f"🏁 *TESTNET FINALIZADO*\n"
            f"Trades totales: {results.get('total_trades', 0)}\n"
            f"Wins: {results.get('wins', 0)}\n"
            f"Losses: {results.get('losses', 0)}\n"
            f"Win Rate: {results.get('winrate', 0):.1f}%\n"
            f"P&L Total: {results.get('pnl', 0):+.2f}€\n"
            f"Mejor trade: {results.get('best_trade', 0):+.2f}€\n"
            f"Peor trade: {results.get('worst_trade', 0):.2f}€"
        )
