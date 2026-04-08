"""
OMEN X - Conexión Exchange
Maneja la conexión con Binance Futures (Testnet/Real)
"""

import ccxt
import os
from typing import Dict, Optional

class ExchangeConnector:
    """Conector unificado para Binance Futures"""
    
    def __init__(self, modo: str = "TESTNET"):
        self.modo = modo.upper()
        self.exchange = None
        self._conectar()
    
    def _conectar(self):
        """Establece conexión con el exchange"""
        
        if self.modo == "TESTNET":
            api_key = os.getenv("BINANCE_TESTNET_API_KEY", "")
            api_secret = os.getenv("BINANCE_TESTNET_SECRET", "")
            sandbox = True
        else:
            api_key = os.getenv("BINANCE_API_KEY", "")
            api_secret = os.getenv("BINANCE_SECRET", "")
            sandbox = False
        
        self.exchange = ccxt.binance({
            "apiKey": api_key,
            "secret": api_secret,
            "enableRateLimit": True,
            "options": {
                "defaultType": "future",
                "sandbox": sandbox,
            }
        })
        
        # Verificar conexión
        try:
            self.exchange.load_markets()
            print(f"✅ OMEN X conectado a Binance Futures ({self.modo})")
        except Exception as e:
            print(f"❌ Error conectando: {e}")
            raise
    
    def get_balance(self, symbol: str = "USDT") -> float:
        """Obtiene balance disponible"""
        balance = self.exchange.fetch_balance()
        return balance["free"].get(symbol, 0)
    
    def fetch_ohlcv(self, symbol: str, timeframe: str = "5m", limit: int = 100):
        """Obtiene datos históricos de velas"""
        return self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    
    def fetch_ticker(self, symbol: str) -> Dict:
        """Obtiene precio actual y volumen"""
        return self.exchange.fetch_ticker(symbol)
    
    def create_order(self, symbol: str, side: str, amount: float, 
                     price: Optional[float] = None, params: Dict = None):
        """Crea orden de mercado o límite"""
        order_type = "limit" if price else "market"
        
        try:
            order = self.exchange.create_order(
                symbol=symbol,
                type=order_type,
                side=side,
                amount=amount,
                price=price,
                params=params or {}
            )
            return order
        except Exception as e:
            print(f"❌ Error creando orden: {e}")
            return None
    
    def set_leverage(self, symbol: str, leverage: int = 1):
        """Establece apalancamiento para el par"""
        try:
            self.exchange.set_leverage(leverage, symbol)
        except Exception as e:
            print(f"⚠️  No se pudo establecer leverage: {e}")
    
    def fetch_positions(self, symbol: Optional[str] = None):
        """Obtiene posiciones abiertas"""
        try:
            positions = self.exchange.fetch_positions([symbol] if symbol else None)
            return [p for p in positions if float(p.get("contracts", 0)) != 0]
        except Exception as e:
            print(f"❌ Error fetching positions: {e}")
            return []
