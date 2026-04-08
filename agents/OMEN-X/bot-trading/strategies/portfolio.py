"""
OMEN X - Portfolio de Estrategias
Permite combinar múltiples estrategias con voting system
"""

from strategies.ema_scalping import EMAScalpingStrategy
from strategies.macd_scalping import MACDScalpingStrategy
from strategies.bollinger_scalping import BollingerScalpingStrategy
from typing import Dict, Tuple, List
import pandas as pd

class StrategyPortfolio:
    """
    Combina 3 estrategias con sistema de votación:
    - EMA Scalping (tendencia)
    - MACD Scalping (momentum)
    - Bollinger Scalping (rango/volatility)
    
    Solo opera si 2/3 estrategias coinciden
    """
    
    def __init__(self, config: Dict):
        self.ema = EMAScalpingStrategy(config)
        self.macd = MACDScalpingStrategy(config)
        self.bollinger = BollingerScalpingStrategy(config)
        
        # Pesos (ajustables)
        self.weights = {
            "ema": 1.0,
            "macd": 1.2,  # MACD tiene más peso por ser más fiable
            "bollinger": 0.8
        }
        
        # Mínimo同意 para operar
        self.min_votes = 2
    
    def analyze_all(self, df: pd.DataFrame) -> Dict:
        """Ejecuta todas las estrategias y devuelve resultados"""
        
        ema_signal, ema_params = self.ema.generate_signal(df)
        macd_signal, macd_params = self.macd.generate_signal(df)
        bollinger_signal, bollinger_params = self.bollinger.generate_signal(df)
        
        return {
            "ema": {"signal": ema_signal, "params": ema_params},
            "macd": {"signal": macd_signal, "params": macd_params},
            "bollinger": {"signal": bollinger_signal, "params": bollinger_params}
        }
    
    def vote(self, results: Dict) -> Tuple[str, Dict]:
        """
        Sistema de votación ponderado
        
        Returns:
            (signal, combined_params)
        """
        votes_long = 0
        votes_short = 0
        long_weight = 0
        short_weight = 0
        
        best_params = None
        
        for strategy, result in results.items():
            signal = result["signal"]
            weight = self.weights[strategy]
            
            if signal == "LONG":
                votes_long += 1 * weight
                long_weight += weight
                if not best_params or result["params"]:
                    best_params = result["params"]
            
            elif signal == "SHORT":
                votes_short += 1 * weight
                short_weight += weight
                if not best_params or result["params"]:
                    best_params = result["params"]
        
        # Decisión por mayoría ponderada
        if votes_long >= self.min_votes and votes_long > votes_short:
            return "LONG", best_params
        
        if votes_short >= self.min_votes and votes_short > votes_long:
            return "SHORT", best_params
        
        return "HOLD", None
    
    def generate_signal(self, df: pd.DataFrame) -> Tuple[str, Dict]:
        """
        Genera señal final basada en consenso de estrategias
        """
        if len(df) < 50:
            return "HOLD", None
        
        results = self.analyze_all(df)
        final_signal, params = self.vote(results)
        
        # Añadir info de consenso
        if params:
            params["consensus"] = {
                strategy: results[strategy]["signal"] 
                for strategy in results
            }
        
        return final_signal, params
    
    def get_strategy_status(self, results: Dict) -> str:
        """Resumen del estado de cada estrategia"""
        status = []
        for name, result in results.items():
            emoji = "✅" if result["signal"] != "HOLD" else "⚪"
            status.append(f"{emoji} {name.upper()}: {result['signal']}")
        return " | ".join(status)
