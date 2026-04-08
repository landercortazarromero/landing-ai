"""
OMEN X v1.0 - Configuración
Scalping Bot para Binance Futures (Testnet)
"""

# MODO OPERACIÓN
MODO = "TESTNET"  # "TESTNET" o "REAL"

# EXCHANGE CONFIG
EXCHANGE_CONFIG = {
    "name": "binance",
    "testnet": {
        "apiKey": "",  # Se carga de env vars
        "secret": "",  # Se carga de env vars
        "sandbox": True,
    },
    "real": {
        "apiKey": "",  # Se carga de env vars
        "secret": "",  # Se carga de env vars
        "sandbox": False,
    }
}

# CAPITAL Y RIESGO
CAPITAL_INICIAL = 1000  # EUR
RIESGO_POR_TRADE = 0.015  # 1.5% del capital por trade
MAX_DRAWDOWN_DIARIO = 0.05  # -5% = pausa automática
MAX_POSICIONES_SIMULTANEAS = 3

# PARES A OPERAR (Futures USDT-M)
SYMBOLS = ["BTC/USDT:USDT", "ETH/USDT:USDT", "SOL/USDT:USDT"]
TIMEFRAMES = ["1m", "5m", "15m"]  # Multi-timeframe

# ESTRATEGIA: EMA SCALPING + RSI
ESTRATEGIA_CONFIG = {
    "ema_rapida": 9,
    "ema_lenta": 21,
    "rsi_periodo": 14,
    "rsi_sobrecompra": 70,
    "rsi_sobreventa": 30,
    "volumen_minimo": 1.5,  # Multiplicador sobre media
}

# GESTIÓN DE ÓRDENES
ORDER_CONFIG = {
    "tipo": "limit",  # limit/market
    "sl_porcentaje": 1.5,  # % desde entrada
    "tp_ratio": 2.0,  # 2:1 risk/reward
    "trailing_stop": True,
    "trailing_activacion": 1.0,  # % de ganancia para activar
}

# NOTIFICACIONES
TELEGRAM_CONFIG = {
    "enabled": True,
    "bot_token": "",  # Se carga de env vars
    "chat_id": "",    # Se carga de env vars
}

# LOGGING
LOG_LEVEL = "INFO"
LOG_FILE = "logs/omen_x.log"
DB_PATH = "data/trades.db"
