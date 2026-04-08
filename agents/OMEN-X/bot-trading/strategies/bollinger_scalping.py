"""
OMEN X - Estrategia Bollinger Bands Scalping
Para mercados en rango o con rotura de volatilidad
"""

import pandas as pd
try:
    import talib
    HAS_TALIB = True
except ImportError:
    import ta
    HAS_TALIB = False
import numpy as np
from typing import Dict, Tuple, Optional

class BollingerScalpingStrategy:
    """
    Estrategia basada en Bollinger Bands + RSI
    Busca roturas de rango y squeezes de volatilidad
    """
    
    def __init__(self, config: Dict):
        self.bb_period = config.get("bb_period", 20)
        self.bb_std = config.get("bb_std", 2)
        self.rsi_period = config.get("rsi_periodo", 14)
        self.atr_period = config.get("atr_period", 14)
    
    def calculate_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcula BB, RSI, ATR"""
        
        # Bollinger Bands
        df["bb_upper"], df["bb_middle"], df["bb_lower"] = talib.BBANDS(
            df["close"],
            timeperiod=self.bb_period,
            nbdevup=self.bb_std,
            nbdevdn=self.bb_std
        )
        
        # BandWidth (indicador de squeeze)
        df["bb_width"] = (df["bb_upper"] - df["bb_lower"]) / df["bb_middle"]
        df["bb_width_sma"] = df["bb_width"].rolling(20).mean()
        
        # RSI
        df["rsi"] = talib.RSI(df["close"], timeperiod=self.rsi_period)
        
        # ATR
        df["atr"] = talib.ATR(df["high"], df["low"], df["close"], timeperiod=self.atr_period)
        
        # Volumen
        df["volume_sma"] = df["volume"].rolling(20).mean()
        
        # Detectar squeeze (bandas estrechas)
        df["squeeze"] = df["bb_width"] < df["bb_width_sma"] * 0.8
        
        return df
    
    def generate_signal(self, df: pd.DataFrame) -> Tuple[str, Optional[Dict]]:
        """
        Genera señales de:
        1. Squeeze breakout (rotura tras compresión)
        2. Mean reversion (precio toca banda exterior)
        """
        if len(df) < 50:
            return "HOLD", None
        
        df = self.calculate_indicators(df)
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        price = last["close"]
        
        # === SQUEEZE BREAKOUT LONG ===
        # Squeeze previo y precio rompe arriba
        squeeze_prev = prev["squeeze"]
        breakout_up = price > last["bb_upper"]
        rsi_ok = 40 < last["rsi"] < 60  # No sobrecomprado
        
        if squeeze_prev and breakout_up and rsi_ok:
            sl = last["bb_lower"]
            tp = price + (last["atr"] * 2.5)
            
            return "LONG", {
                "type": "squeeze_breakout",
                "price": price,
                "stop_loss": sl,
                "take_profit": tp,
                "bb_width": last["bb_width"],
                "rsi": last["rsi"]
            }
        
        # === MEAN REVERSION LONG ===
        # Precio toca banda inferior + RSI sobrevendido
        touch_lower = price <= last["bb_lower"] * 1.01
        rsi_oversold = last["rsi"] < 35
        
        if touch_lower and rsi_oversold:
            sl = last["bb_lower"] - (last["atr"] * 0.5)
            tp = last["bb_middle"]  # Volver a la media
            
            return "LONG", {
                "type": "mean_reversion",
                "price": price,
                "stop_loss": sl,
                "take_profit": tp,
                "bb_lower": last["bb_lower"],
                "rsi": last["rsi"]
            }
        
        # === SQUEEZE BREAKOUT SHORT ===
        squeeze_prev = prev["squeeze"]
        breakout_down = price < last["bb_lower"]
        rsi_ok_short = 40 < last["rsi"] < 60
        
        if squeeze_prev and breakout_down and rsi_ok_short:
            sl = last["bb_upper"]
            tp = price - (last["atr"] * 2.5)
            
            return "SHORT", {
                "type": "squeeze_breakout",
                "price": price,
                "stop_loss": sl,
                "take_profit": tp,
                "bb_width": last["bb_width"],
                "rsi": last["rsi"]
            }
        
        # === MEAN REVERSION SHORT ===
        touch_upper = price >= last["bb_upper"] * 0.99
        rsi_overbought = last["rsi"] > 65
        
        if touch_upper and rsi_overbought:
            sl = last["bb_upper"] + (last["atr"] * 0.5)
            tp = last["bb_middle"]
            
            return "SHORT", {
                "type": "mean_reversion",
                "price": price,
                "stop_loss": sl,
                "take_profit": tp,
                "bb_upper": last["bb_upper"],
                "rsi": last["rsi"]
            }
        
        return "HOLD", None
