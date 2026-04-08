# OMEN X v1.0 - Scalping Bot para Binance Futures

## 🚀 Descripción

OMEN X es un agente autónomo de trading que opera en modo **scalping** (1-15 min timeframe) usando estrategias de análisis técnico en **Binance Futures Testnet**.

**Fase actual:** TESTNET 7 DÍAS (sin dinero real)

---

## 📋 Requisitos

- Python 3.11+
- API Keys de Binance Testnet
- Telegram Bot (opcional, para alertas)

---

## 🛠️ Instalación

```bash
cd agents/OMEN-X/bot-trading
chmod +x setup.sh
./setup.sh
```

---

## ⚙️ Configuración

1. **Obtener API Keys de Testnet:**
   - Ve a https://testnet.binance.vision/
   - Regístrate/Login
   - Genera API Key y Secret

2. **Configurar variables de entorno:**
```bash
cp .env.example .env
nano .env
# Añade tus keys
```

3. **Ajustar parámetros en `config.py`:**
```python
CAPITAL_INICIAL = 1000  # Tu capital en EUR
SYMBOLS = ["BTC/USDT:USDT", "ETH/USDT:USDT", "SOL/USDT:USDT"]
RIESGO_POR_TRADE = 0.015  # 1.5% por operación
```

---

## ▶️ Ejecutar

```bash
source venv/bin/activate
python bot.py
```

---

## 📊 Estrategia Implementada

### EMA Scalping + RSI

| Indicador | Configuración |
|-----------|---------------|
| EMA Rápida | 9 períodos |
| EMA Lenta | 21 períodos |
| RSI | 14 períodos (30/70) |
| Volumen | >1.5x media móvil |

### Señales de Entrada

**LONG:**
- EMA rápida > EMA lenta (tendencia alcista)
- RSI < 30 (sobreventa)
- Volumen > 1.5x media
- Precio cruza por encima de EMA rápida

**SHORT:**
- EMA rápida < EMA lenta (tendencia bajista)
- RSI > 70 (sobrecompra)
- Volumen > 1.5x media
- Precio cruza por debajo de EMA rápida

### Gestión de Riesgo

- **Riesgo por trade:** 1.5% del capital
- **Stop Loss:** 1.5x ATR
- **Take Profit:** Ratio 2:1
- **Máximo drawdown diario:** -5% (pausa automática)
- **Máximo trades diarios:** 10

---

## 📁 Estructura del Proyecto

```
bot-trading/
├── config.py           # Configuración global
├── bot.py              # Orquestador principal
├── core/
│   └── exchange.py     # Conexión CCXT
├── strategies/
│   └── ema_scalping.py # Estrategia EMA+RSI
├── risk/
│   └── manager.py      # Gestor de riesgo
├── data/               # Histórico de trades
├── logs/               # Logs de ejecución
└── requirements.txt    # Dependencias
```

---

## 🔔 Alertas Telegram

El bot envía notificaciones a Telegram cuando:

- ✅ Orden ejecutada (entrada LONG/SHORT)
- ⚠️ Pérdida > €20 en posición
- ⛔ Límite de drawdown alcanzado
- 📈 Reporte horario de P&L

---

## ⚠️ Disclaimer

Este bot es para **propósitos educativos/testnet**. trading implica riesgo sustancial de pérdida. No operar con dinero que no puedas permitirte perder.

---

## 📈 Roadmap

| Fase | Estado | Descripción |
|------|--------|-------------|
| v1.0 | ✅ Testnet | EMA Scalping básico |
| v1.1 | 🔜 | Añadir más indicadores (MACD, BB) |
| v1.2 | 🔜 | Optimización con backtesting |
| v2.0 | 🔜 | Modo REAL con capital pequeño |
| v3.0 | 🔜 | Múltiples estrategias |

---

*OMEN X v1.0 - Hybrid Labs L2*
