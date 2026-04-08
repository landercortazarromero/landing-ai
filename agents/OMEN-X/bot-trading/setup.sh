#!/bin/bash
# =============================================================================
# OMEN X - Setup & Installation
# =============================================================================

set -e

echo "🚀 OMEN X Setup"

# 1. Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependencias
echo "📥 Instalando dependencias..."
pip install --upgrade pip
pip install ccxt pandas numpy python-telegram-bot schedule python-dotenv

# 3. Instalar TA-Lib (requiere compilación)
echo "📥 Instalando TA-Lib (esto puede tardar)..."
pip install ta-lib || pip install ta

# 4. Crear estructura de carpetas
echo "📁 Creando estructura..."
mkdir -p logs data

# 5. Crear archivo .env ejemplo
echo "📝 Creando .env.example..."
cat > .env.example << 'EOF'
# Binance Testnet
BINANCE_TESTNET_API_KEY=tu_api_key_testnet
BINANCE_TESTNET_SECRET=tu_secret_testnet

# Binance Real (para después)
BINANCE_API_KEY=tu_api_key_real
BINANCE_SECRET=tu_secret_real

# Telegram (para alertas)
TELEGRAM_BOT_TOKEN=tu_bot_token
TELEGRAM_CHAT_ID=tu_chat_id
EOF

echo ""
echo "✅ OMEN X instalado"
echo ""
echo "SIGUIENTE PASO:"
echo "1. Copia .env.example a .env"
echo "2. Añade tus API keys de Binance Testnet"
echo "3. Obtén API keys en: https://testnet.binance.vision/"
echo ""
echo "Para activar el bot:"
echo "   source venv/bin/activate"
echo "   python bot.py"
