"""
OMEN X - Estrategia EMA Scalping + RSI
Entradas rápidas en dirección de la tendencia
"""

import pandas as pd
import numpy as np
from typing import Dict, Optional, Tuple
try:
    import talib
    HAS_TALIB = True
except ImportError:
    import ta
    HAS_TALIB = False

class EMAScalpingStrategy:
    """
    Estrategia de scalping basada en:
    - EMA 9/21 (tendencia)
    - RSI 14 (sobrecompra/sobreventa)
    - Volumen (confirmación)
    """
    
    def __init__(self, config: Dict):
        self.ema_fast = config.get("ema_rapida", 9)
        self.ema_slow = config.get("ema_lenta", 21)
        self.rsi_period = config.get("rsi_periodo", 14)
        self.rsi_overbought = config.get("rsi_sobrecompra", 70)
        self.rsi_oversold = config.get("rsi_sobreventa", 30)
        self.volume_threshold = config.get("volumen_minimo", 1.5)
    
    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcula todos los indicadores"""
        # EMAs
        if HAS_TALIB:
            df["ema_fast"] = talib.EMA(df["close"], timeperiod=self.ema_fast)
            df["ema_slow"] = talib.EMA(df["close"], timeperiod=self.ema_slow)
            df["rsi"] = talib.RSI(df["close"], timeperiod=self.rsi_period)
        else:
            from ta.trend import EMAIndicator, RSIIndicator
            df["ema_fast"] = EMAIndicator(df["close"], window=self.ema_fast).ema_indicator()
            df["ema_slow"] = EMAIndicator(df["close"], window=self.ema_slow).ema_indicator()
            df["rsi"] = RSIIndicator(df["close"], window=self.rsi_period).rsi()
        
        # Volumen medio
        df["volume_sma"] = df["volume"].rolling(window=20).mean()
        
        # ATR para stops
        if HAS_TALIB:
            df["atr"] = talib.ATR(df["high"], df["low"], df["close"], timeperiod=14)
        else:
            from ta.volatility import ATRIndicator
            df["atr"] = ATRIndicator(df["high"], df["low"], df["close"], window=14).atr()
        
        return df
    
    def generate_signal(self, df: pd.DataFrame) -> Tuple[str, Optional[Dict]]:
        """
        Genera señal de trading
        
        Returns:
            (señal, metadata) 
            señal: "LONG", "SHORT", o "HOLD"
        """
        if len(df) < 50:
            return "HOLD", None
        
        df = self.calculate_indicators(df)
        
        # Última vela
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        # Condiciones de tendencia
        trend_up = last["ema_fast"] > last["ema_slow"]
        trend_down = last["ema_fast"] < last["ema_slow"]
        
        # Condiciones de volumen
        volume_ok = last["volume"] > (last["volume_sma"] * self.volume_threshold)
        
        # Señal LONG
        if trend_up and last["rsi"] < self.rsi_oversold and volume_ok:
            # Cruce de precio con EMA rápida
            if prev["close"] < prev["ema_fast"] and last["close"] > last["ema_fast"]:
                sl = last["close"] - (last["atr"] * 1.5)
                tp = last["close"] + (last["atr"] * 3.0)  # 2:1 R/R
                
                return "LONG", {
                    "price": last["close"],
                    "stop_loss": sl,
                    "take_profit": tp,
                    "rsi": last["rsi"],
                    "ema_fast": last["ema_fast"],
                    "ema_slow": last["ema_slow"],
                    "volume_ratio": last["volume"] / last["volume_sma"]
                }
        
        # Señal SHORT
        if trend_down and last["rsi"] > self.rsi_overbought and volume_ok:
            if prev["close"] > prev["ema_fast"] and last["close"] < last["ema_fast"]:
                sl = last["close"] + (last["atr"] * 1.5)
                tp = last["close"] - (last["atr"] * 3.0)
                
                return "SHORT", {
                    "price": last["close"],
                    "stop_loss": sl,
                    "take_profit": tp,
                    "rsi": last["rsi"],
                    "ema_fast": last["ema_fast"],
                    "ema_slow": last["ema_slow"],
                    "volume_ratio": last["volume"] / last["volume_sma"]
                }
        
        return "HOLD", None
    
    def get_position_size(self, capital: float, riesgo: float, 
                          entry: float, stop_loss: float) -> float:
        """Calcula tamaño de posición basado en riesgo"""
        risk_amount = capital * riesgo
        stop_distance = abs(entry - stop_loss)
        
        if stop_distance == 0:
            return 0
        
        position_size = risk_amount / stop_distance
        return round(position_size, 6)
