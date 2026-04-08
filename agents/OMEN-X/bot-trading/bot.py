"""
OMEN X v1.0 - Trading Bot Principal
Ejecuta estrategia de scalping en Binance Testnet
"""

import time
import schedule
import telegram
import os
import pandas as pd
from datetime import datetime
from pathlib import Path

# Módulos propios
from core.exchange import ExchangeConnector
from strategies.ema_scalping import EMAScalpingStrategy
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
    """OMEN X - Agente Autónomo de Trading"""
    
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
        self.strategy = EMAScalpingStrategy(self.config)
        self.risk = RiskManager(self.config, self.exchange)
        
        # Telegram
        self.telegram = None
        if TELEGRAM_CONFIG["enabled"]:
            self._init_telegram()
        
        # Estado
        self.positions = []
        self.is_running = False
        
        logger.info("🚀 OMEN X v1.0 inicializado")
    
    def _init_telegram(self):
        """Inicializa bot de Telegram para alertas"""
        try:
            self.telegram = telegram.Bot(
                token=os.getenv("TELEGRAM_BOT_TOKEN", ""),
                chat_id=os.getenv("TELEGRAM_CHAT_ID", "")
            )
            self.send_alert("🚀 OMEN X ONLINE - Testnet 7 días")
        except Exception as e:
            logger.warning(f"Telegram no disponible: {e}")
    
    def send_alert(self, message: str):
        """Envía alerta a Telegram"""
        if self.telegram:
            try:
                self.telegram.send_message(
                    text=f"📊 OMEN X\n{message}",
                    parse_mode="Markdown"
                )
            except Exception as e:
                logger.error(f"Error enviando Telegram: {e}")
    
    def scan_markets(self):
        """Escanea todos los símbolos buscando señales"""
        results = []
        
        for symbol in SYMBOLS:
            try:
                # Obtener datos
                df = pd.DataFrame(
                    self.exchange.fetch_ohlcv(symbol, "5m", limit=100)
                )
                df.columns = ["timestamp", "open", "high", "low", "close", "volume"]
                
                # Generar señal
                signal, params = self.strategy.generate_signal(df)
                
                if signal != "HOLD":
                    results.append({
                        "symbol": symbol,
                        "signal": signal,
                        "params": params
                    })
                    
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
            self.send_alert(
                f"✅ *{side.upper()}* {symbol}\n"
                f"Precio: {params['price']}\n"
                f"SL: {params['stop_loss']}\n"
                f"TP: {params['take_profit']}\n"
                f"Cantidad: {position_size}"
            )
        
        return order
    
    def check_positions(self):
        """Monitoriza posiciones abiertas"""
        open_positions = self.exchange.fetch_positions()
        
        for pos in open_positions:
            symbol = pos["symbol"]
            pnl = float(pos.get("unrealizedPnL", 0))
            
            # Actualizar riesgo
            self.risk.update_trade(pnl)
            
            # Alertar si hay pérdidas grandes
            if pnl < -20:
                self.send_alert(f"⚠️ Pérdida en {symbol}: {pnl}€")
    
    def run_cycle(self):
        """Un ciclo completo de análisis y ejecución"""
        logger.info(f"🔄 Ciclo OMEN X - {datetime.now().strftime('%H:%M:%S')}")
        
        # 1. Verificar riesgo
        can_trade, reason = self.risk.can_trade()
        if not can_trade:
            logger.info(f"Oportunidades pausadas: {reason}")
            return
        
        # 2. Escanear mercados
        signals = self.scan_markets()
        
        if not signals:
            logger.info("Sin señales detectedas")
            return
        
        # 3. Ejecutar señales
        for signal in signals[:self.risk.max_positions]:
            self.execute_trade(signal)
        
        # 4. Check posiciones
        self.check_positions()
    
    def run_testnet(self):
        """Ejecuta en modo testnet 7 días"""
        logger.info("🧪 INICIANDO TESTNET 7 DÍAS")
        self.send_alert("🧪 TESTNET INICIADO - 7 días")
        
        # Horarios de trading (volátiles = mejor para scalping)
        schedule.every(1).minutes.do(self.run_cycle)
        schedule.every(15).minutes.do(self.check_positions)
        
        # Resumen cada hora
        schedule.every().hour.do(self.hourly_report)
        
        while self.is_running:
            schedule.run_pending()
            time.sleep(1)
    
    def hourly_report(self):
        """Reporte hourly"""
        status = self.risk.get_status()
        self.send_alert(
            f"📈 *Reporte Horario*\n"
            f"P&L Diario: {status['daily_pnl']:.2f}€\n"
            f"Trades: {status['trades_today']}\n"
            f"Drawdown: {status['drawdown_actual']:.2f}%"
        )
    
    def stop(self):
        """Detiene el bot"""
        self.is_running = False
        logger.info("🛑 OMEN X DETENIDO")
        self.send_alert("🛑 OMEN X DETENIDO")


if __name__ == "__main__":
    bot = OMENXBot()
    
    try:
        bot.run_testnet()
    except KeyboardInterrupt:
        bot.stop()
