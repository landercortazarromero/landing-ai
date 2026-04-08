"""
OMEN X - Estrategia MACD Scalping
Complemento a EMA para confirmación de momentum
"""

import pandas as pd
try:
    import talib
    HAS_TALIB = True
except ImportError:
    import ta
    HAS_TALIB = False
from typing import Dict, Tuple, Optional

class MACDScalpingStrategy:
    """
    Estrategia basada en MACD + Volumen
    Para confirmación de momentum en scalping
    """
    
    def __init__(self, config: Dict):
        self.fast = config.get("macd_fast", 12)
        self.slow = config.get("macd_slow", 26)
        self.signal = config.get("macd_signal", 9)
        self.rsi_period = config.get("rsi_periodo", 14)
        self.stoch_k = config.get("stoch_k", 14)
        self.stoch_d = config.get("stoch_d", 3)
    
    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcula MACD, RSI, Estocástico"""
        
        # MACD
        df["macd"], df["macd_signal"], df["macd_hist"] = talib.MACD(
            df["close"],
            fastperiod=self.fast,
            slowperiod=self.slow,
            signalperiod=self.signal
        )
        
        # RSI
        df["rsi"] = talib.RSI(df["close"], timeperiod=self.rsi_period)
        
        # Estocástico
        df["stoch_k"], df["stoch_d"] = talib.STOCH(
            df["high"], df["low"], df["close"],
            fastk_period=self.stoch_k,
            slowk_period=self.stoch_d
        )
        
        # ATR
        df["atr"] = talib.ATR(df["high"], df["low"], df["close"], timeperiod=14)
        
        # Volumen
        df["volume_sma"] = df["volume"].rolling(20).mean()
        
        return df
    
    def generate_signal(self, df: pd.DataFrame) -> Tuple[str, Optional[Dict]]:
        """
        Genera señal basada en MACD crossover + estocástico
        """
        if len(df) < 50:
            return "HOLD", None
        
        df = self.calculate_indicators(df)
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        # === LONG CONDITIONS ===
        # MACD cruza arriba de señal
        macd_bullish = prev["macd"] < prev["macd_signal"] and last["macd"] > last["macd_signal"]
        # Histograma positivo
        histogram_positive = last["macd_hist"] > 0
        # Estocástico en sobreventa
        stoch_oversold = last["stoch_k"] < 30 and last["stoch_d"] < 30
        # Volumen confirmado
        volume_confirm = last["volume"] > last["volume_sma"] * 1.3
        
        if macd_bullish and histogram_positive and stoch_oversold and volume_confirm:
            sl = last["close"] - (last["atr"] * 1.5)
            tp = last["close"] + (last["atr"] * 3.0)
            
            return "LONG", {
                "price": last["close"],
                "stop_loss": sl,
                "take_profit": tp,
                "macd": last["macd"],
                "macd_signal": last["macd_signal"],
                "rsi": last["rsi"],
                "stoch_k": last["stoch_k"],
                "volume_ratio": last["volume"] / last["volume_sma"]
            }
        
        # === SHORT CONDITIONS ===
        # MACD cruza debajo de señal
        macd_bearish = prev["macd"] > prev["macd_signal"] and last["macd"] < last["macd_signal"]
        # Histograma negativo
        histogram_negative = last["macd_hist"] < 0
        # Estocástico en sobrecompra
        stoch_overbought = last["stoch_k"] > 70 and last["stoch_d"] > 70
        
        if macd_bearish and histogram_negative and stoch_overbought and volume_confirm:
            sl = last["close"] + (last["atr"] * 1.5)
            tp = last["close"] - (last["atr"] * 3.0)
            
            return "SHORT", {
                "price": last["close"],
                "stop_loss": sl,
                "take_profit": tp,
                "macd": last["macd"],
                "macd_signal": last["macd_signal"],
                "rsi": last["rsi"],
                "stoch_k": last["stoch_k"],
                "volume_ratio": last["volume"] / last["volume_sma"]
            }
        
        return "HOLD", None
