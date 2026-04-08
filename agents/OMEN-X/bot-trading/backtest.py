"""
OMEN X - Backtesting Engine
Analiza rendimiento de estrategias con datos históricos
"""

import ccxt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import json
import os

class Backtester:
    """
    Backtester para OMEN X strategies
    Usa datos históricos reales de Binance
    """
    
    def __init__(self, initial_capital: float = 1000):
        self.initial_capital = initial_capital
        self.capital = initial_capital
        self.exchange = ccxt.binance({"enableRateLimit": True})
        
        # Results storage
        self.trades = []
        self.equity_curve = []
        self.metrics = {}
    
    def fetch_historical_data(self, symbol: str, timeframe: str = "5m", 
                             days: int = 180) -> pd.DataFrame:
        """
        Descarga datos históricos
        180 días = ~51,000 velas en 5m
        """
        print(f"📥 Descargando datos {symbol} {timeframe} ({days} días)...")
        
        since = self.exchange.milliseconds() - (days * 24 * 60 * 60 * 1000)
        
        all_ohlcv = []
        while since < self.exchange.milliseconds():
            try:
                ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=1000)
                if not ohlcv:
                    break
                all_ohlcv.extend(ohlcv)
                since = ohlcv[-1][0] + 1
                print(f"   {len(all_ohlcv)} velas descargadas...", end="\r")
            except Exception as e:
                print(f"\n⚠️ Error: {e}, esperando 2s...")
                import time; time.sleep(2)
        
        print(f"\n✅ Total: {len(all_ohlcv)} velas")
        
        df = pd.DataFrame(all_ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        
        return df
    
    def run_strategy_backtest(self, df: pd.DataFrame, strategy_func, 
                             strategy_name: str = "EMA") -> Dict:
        """
        Ejecuta backtest de una estrategia
        strategy_func(df) -> (signal, params)
        """
        print(f"\n🔄 Ejecutando backtest: {strategy_name}")
        
        self.capital = self.initial_capital
        self.trades = []
        self.equity_curve = []
        
        # Simular trading
        position = None
        entry_price = 0
        position_size = 0
        
        # Importar estrategias
        from strategies.ema_scalping import EMAScalpingStrategy
        from strategies.macd_scalping import MACDScalpingStrategy
        from strategies.bollinger_scalping import BollingerScalpingStrategy
        
        strategies = {
            "EMA": EMAScalpingStrategy({"ema_rapida": 9, "ema_lenta": 21, "rsi_periodo": 14}),
            "MACD": MACDScalpingStrategy({"macd_fast": 12, "macd_slow": 26, "macd_signal": 9, "rsi_periodo": 14}),
            "BOL": BollingerScalpingStrategy({"bb_period": 20, "bb_std": 2, "rsi_periodo": 14})
        }
        
        strategy = strategies.get(strategy_name, strategies["EMA"])
        
        # Parámetros de riesgo
        RISK_PER_TRADE = 0.015  # 1.5%
        ATR_MULTIPLIER = 1.5
        RR_RATIO = 2.0
        
        # Iterar por cada vela (excepto últimas 50 para lookahead)
        total_bars = len(df) - 50
        
        for i in range(50, total_bars):
            current_df = df.iloc[:i+1].copy()
            
            # Obtener señal
            signal, params = strategy.generate_signal(current_df)
            
            # Solo operar si no hay posición
            if position is None and signal != "HOLD":
                # Calcular tamaño
                entry_price = params["price"]
                stop_loss = params["stop_loss"]
                risk_amount = self.capital * RISK_PER_TRADE
                stop_distance = abs(entry_price - stop_loss)
                
                if stop_distance > 0:
                    position_size = risk_amount / stop_distance
                    
                    # Comisiones (0.04% taker en Binance futures)
                    commission = entry_price * position_size * 0.0004
                    
                    position = {
                        "side": signal,
                        "entry": entry_price,
                        "size": position_size,
                        "sl": stop_loss,
                        "tp": params["take_profit"],
                        "commission": commission,
                        "entry_bar": i
                    }
            
            # Check si hay posición
            elif position is not None:
                current_price = df.iloc[i]["close"]
                
                # Stop Loss
                if position["side"] == "LONG" and current_price <= position["sl"]:
                    pnl = (current_price - position["entry"]) * position["size"] - position["commission"]
                    self._close_trade(position, current_price, pnl, "SL", i)
                    position = None
                
                elif position["side"] == "SHORT" and current_price >= position["sl"]:
                    pnl = (position["entry"] - current_price) * position["size"] - position["commission"]
                    self._close_trade(position, current_price, pnl, "SL", i)
                    position = None
                
                # Take Profit
                elif position["side"] == "LONG" and current_price >= position["tp"]:
                    pnl = (current_price - position["entry"]) * position["size"] - position["commission"]
                    self._close_trade(position, current_price, pnl, "TP", i)
                    position = None
                
                elif position["side"] == "SHORT" and current_price <= position["tp"]:
                    pnl = (position["entry"] - current_price) * position["size"] - position["commission"]
                    self._close_trade(position, current_price, pnl, "TP", i)
                    position = None
            
            # Registrar equity
            self.equity_curve.append({
                "timestamp": df.index[i],
                "equity": self.capital
            })
        
        # Cerrar posición final si existe
        if position is not None:
            final_price = df.iloc[-1]["close"]
            pnl = (final_price - position["entry"]) * position["size"] - position["commission"] if position["side"] == "LONG" else (position["entry"] - final_price) * position["size"] - position["commission"]
            self.capital += pnl
            self.trades.append({**position, "exit": final_price, "pnl": pnl, "exit_reason": "EOD", "exit_bar": len(df)})
        
        return self._calculate_metrics()
    
    def _close_trade(self, position, exit_price, pnl, reason, bar_index):
        self.capital += pnl
        self.trades.append({
            "side": position["side"],
            "entry": position["entry"],
            "exit": exit_price,
            "size": position["size"],
            "pnl": pnl,
            "commission": position["commission"],
            "entry_bar": position["entry_bar"],
            "exit_bar": bar_index,
            "exit_reason": reason
        })
    
    def _calculate_metrics(self) -> Dict:
        """Calcula métricas de rendimiento"""
        if not self.trades:
            return {"error": "No trades executed"}
        
        wins = [t for t in self.trades if t["pnl"] > 0]
        losses = [t for t in self.trades if t["pnl"] <= 0]
        
        total_pnl = sum(t["pnl"] for t in self.trades)
        win_rate = len(wins) / len(self.trades) * 100
        
        # Max drawdown
        equity = self.initial_capital
        peak = equity
        max_dd = 0
        for t in self.equity_curve:
            equity = t["equity"]
            if equity > peak:
                peak = equity
            dd = (peak - equity) / peak * 100
            if dd > max_dd:
                max_dd = dd
        
        # Trade duration media
        durations = [t["exit_bar"] - t["entry_bar"] for t in self.trades]
        
        # Profit factor
        gross_profit = sum(t["pnl"] for t in wins)
        gross_loss = abs(sum(t["pnl"] for t in losses))
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        
        # Best/worst
        pnls = [t["pnl"] for t in self.trades]
        
        metrics = {
            "total_trades": len(self.trades),
            "wins": len(wins),
            "losses": len(losses),
            "win_rate": win_rate,
            "total_pnl": total_pnl,
            "total_pnl_pct": (total_pnl / self.initial_capital) * 100,
            "profit_factor": profit_factor,
            "max_drawdown": max_dd,
            "avg_trade_pnl": np.mean(pnls),
            "best_trade": max(pnls),
            "worst_trade": min(pnls),
            "avg_duration_bars": np.mean(durations),
            "sharpe_ratio": self._calculate_sharpe(),
        }
        
        return metrics
    
    def _calculate_sharpe(self) -> float:
        """Calcula Sharpe Ratio simplificado"""
        if len(self.equity_curve) < 100:
            return 0
        
        returns = []
        for i in range(1, len(self.equity_curve)):
            ret = (self.equity_curve[i]["equity"] - self.equity_curve[i-1]["equity"]) / self.equity_curve[i-1]["equity"]
            returns.append(ret)
        
        if not returns:
            return 0
        
        avg_return = np.mean(returns)
        std_return = np.std(returns)
        
        if std_return == 0:
            return 0
        
        return (avg_return / std_return) * np.sqrt(252 * 288)  # Annualized (5min bars)
    
    def generate_report(self, metrics: Dict, strategy_name: str) -> str:
        """Genera informe de backtest"""
        
        status = "🟢 POSITIVO" if metrics.get("total_pnl", 0) > 0 else "🔴 NEGATIVO"
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║           OMEN X BACKTEST REPORT - {strategy_name}                  
╚══════════════════════════════════════════════════════════════╝

📊 RESULTADO: {status}
   P&L Total: {metrics.get('total_pnl', 0):+.2f}€ ({metrics.get('total_pnl_pct', 0):+.2f}%)
   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 MÉTRICAS DE TRADING:

   Trades Totales:    {metrics.get('total_trades', 0)}
   Wins:              {metrics.get('wins', 0)}
   Losses:            {metrics.get('losses', 0)}
   Win Rate:          {metrics.get('win_rate', 0):.1f}%
   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 GESTIÓN DE RIESGO:

   Profit Factor:      {metrics.get('profit_factor', 0):.2f}
   Max Drawdown:       {metrics.get('max_drawdown', 0):.2f}%
   Mejor Trade:        {metrics.get('best_trade', 0):+.2f}€
   Peor Trade:        {metrics.get('worst_trade', 0):.2f}€
   Media Trade:       {metrics.get('avg_trade_pnl', 0):+.2f}€
   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📉 ANÁLISIS DE CARTERA:

   Capital Inicial:   {self.initial_capital:.2f}€
   Capital Final:     {self.initial_capital + metrics.get('total_pnl', 0):.2f}€
   Sharpe Ratio:      {metrics.get('sharpe_ratio', 0):.2f}
   Duración Media:    {metrics.get('avg_duration_bars', 0):.1f} velas (5min)
   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏰ PERÍODO DE ANÁLISIS: 180 días (≈ 6 meses)

═══════════════════════════════════════════════════════════════
"""
        return report
    
    def save_results(self, metrics: Dict, strategy_name: str):
        """Guarda resultados en JSON"""
        results_dir = os.path.join(os.path.dirname(__file__), "backtest_results")
        os.makedirs(results_dir, exist_ok=True)
        
        filename = f"{results_dir}/{strategy_name.lower()}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, "w") as f:
            json.dump({
                "strategy": strategy_name,
                "period": "180 days",
                "initial_capital": self.initial_capital,
                "metrics": metrics,
                "trades": self.trades
            }, f, indent=2, default=str)
        
        print(f"💾 Resultados guardados: {filename}")


def run_full_backtest():
    """Ejecuta backtest completo con las 3 estrategias"""
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║     OMEN X - BACKTEST HISTÓRICO 180 DÍAS                   ║
║     Estrategias: EMA + MACD + Bollinger                    ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    bt = Backtester(initial_capital=1000)
    
    # Descargar datos BTC 5m
    df = bt.fetch_historical_data("BTC/USDT:USDT", "5m", days=180)
    
    results = {}
    
    # Backtest EMA
    print("\n" + "="*60)
    metrics_ema = bt.run_strategy_backtest(df, None, "EMA")
    results["EMA"] = metrics_ema
    print(bt.generate_report(metrics_ema, "EMA Scalping"))
    
    # Backtest MACD
    print("\n" + "="*60)
    metrics_macd = bt.run_strategy_backtest(df, None, "MACD")
    results["MACD"] = metrics_macd
    print(bt.generate_report(metrics_macd, "MACD Scalping"))
    
    # Backtest Bollinger
    print("\n" + "="*60)
    metrics_bol = bt.run_strategy_backtest(df, None, "BOLL")
    results["BOLL"] = metrics_bol
    print(bt.generate_report(metrics_bol, "Bollinger Scalping"))
    
    # Comparativa
    print("""
╔══════════════════════════════════════════════════════════════╗
║              COMPARATIVA DE ESTRATEGIAS                     ║
╚══════════════════════════════════════════════════════════════╝

Estrategia    │  Trades  │  Win%  │  P&L €   │  P&L %   │  PF
──────────────┼──────────┼────────┼──────────┼──────────┼───────""")
    
    for name, m in results.items():
        print(f"{name:13} │ {m.get('total_trades', 0):8} │ {m.get('win_rate', 0):5.1f}% │ {m.get('total_pnl', 0):+8.2f} │ {m.get('total_pnl_pct', 0):+7.2f}% │ {m.get('profit_factor', 0):.2f}")
    
    # Guardar todos los resultados
    bt.save_results(results, "ALL_STRATEGIES")
    
    return results


if __name__ == "__main__":
    results = run_full_backtest()
