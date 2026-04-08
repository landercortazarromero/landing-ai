"""
OMEN X - Dashboard Data Server
Serve status data for web dashboard
"""

from flask import Flask, jsonify, render_template
import threading
import time
from datetime import datetime
from typing import Dict, List

app = Flask(__name__)

# Global state (simple for now)
BOT_STATE = {
    "status": "STOPPED",
    "mode": "TESTNET",
    "started_at": None,
    "capital": 1000,
    "daily_pnl": 0,
    "total_pnl": 0,
    "trades_today": 0,
    "total_trades": 0,
    "win_rate": 0,
    "drawdown": 0,
    "positions": [],
    "recent_trades": [],
    "signals": []
}

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/status")
def status():
    return jsonify(BOT_STATE)

@app.route("/api/trades")
def trades():
    return jsonify(BOT_STATE["recent_trades"])

@app.route("/api/signals")
def signals():
    return jsonify(BOT_STATE["signals"][-20:])  # Last 20

class DashboardServer:
    """Wrapper para ejecutar Flask en thread separado"""
    
    def __init__(self, port: int = 5000):
        self.port = port
        self.thread = None
        self.running = False
    
    def update_state(self, new_state: Dict):
        """Actualiza el estado global del dashboard"""
        BOT_STATE.update(new_state)
    
    def add_trade(self, trade: Dict):
        """Añade trade al histórico"""
        BOT_STATE["recent_trades"].append({
            **trade,
            "timestamp": datetime.now().isoformat()
        })
        # Keep last 50
        BOT_STATE["recent_trades"] = BOT_STATE["recent_trades"][-50:]
    
    def add_signal(self, signal: Dict):
        """Añade señal detectada"""
        BOT_STATE["signals"].append({
            **signal,
            "timestamp": datetime.now().isoformat()
        })
        BOT_STATE["signals"] = BOT_STATE["signals"][-20:]
    
    def start(self):
        """Inicia servidor en thread"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()
            print(f"🌐 Dashboard disponible en http://localhost:{self.port}")
    
    def _run(self):
        app.run(host="0.0.0.0", port=self.port, debug=False)


# HTML Dashboard Template (inline for simplicity)
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OMEN X - Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'JetBrains Mono', monospace; 
            background: #0a0a0f; 
            color: #00ff88;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            padding: 20px 40px;
            border-bottom: 2px solid #00ff88;
        }
        .header h1 { font-size: 28px; }
        .header span { opacity: 0.7; font-size: 14px; }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px 40px;
        }
        .stat-card {
            background: #1a1a2e;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }
        .stat-card .value { font-size: 32px; font-weight: bold; }
        .stat-card .label { opacity: 0.6; font-size: 12px; margin-top: 5px; }
        .positive { color: #00ff88; }
        .negative { color: #ff4757; }
        
        .sections {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            padding: 0 40px 40px;
        }
        .section {
            background: #1a1a2e;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 20px;
        }
        .section h2 { 
            font-size: 16px; 
            margin-bottom: 15px; 
            border-bottom: 1px solid #333;
            padding-bottom: 10px;
        }
        
        .trade {
            display: flex;
            justify-content: space-between;
            padding: 10px;
            border-bottom: 1px solid #222;
        }
        .trade:last-child { border-bottom: none; }
        .trade .symbol { font-weight: bold; }
        .trade .pnl { font-size: 14px; }
        .long { color: #00ff88; }
        .short { color: #ff4757; }
        
        .signal {
            padding: 8px;
            margin: 5px 0;
            border-radius: 6px;
            font-size: 13px;
        }
        .signal.long { background: rgba(0,255,136,0.1); border-left: 3px solid #00ff88; }
        .signal.short { background: rgba(255,71,87,0.1); border-left: 3px solid #ff4757; }
        .signal.hold { background: rgba(255,255,255,0.05); border-left: 3px solid #666; }
        
        .status-badge {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }
        .status-badge.running { background: #00ff88; color: #000; }
        .status-badge.stopped { background: #ff4757; color: #fff; }
        
        .refresh {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #00ff88;
            color: #000;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-family: inherit;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎯 OMEN X <span>Trading Bot</span></h1>
        <p>Status: <span id="status" class="status-badge stopped">STOPPED</span></p>
    </div>
    
    <div class="stats">
        <div class="stat-card">
            <div class="value" id="capital">1000.00</div>
            <div class="label">CAPITAL (€)</div>
        </div>
        <div class="stat-card">
            <div class="value" id="pnl">0.00</div>
            <div class="label">P&L DIARIO (€)</div>
        </div>
        <div class="stat-card">
            <div class="value" id="total-pnl">0.00</div>
            <div class="label">P&L TOTAL (€)</div>
        </div>
        <div class="stat-card">
            <div class="value" id="trades">0</div>
            <div class="label">TRADES HOY</div>
        </div>
        <div class="stat-card">
            <div class="value" id="winrate">0%</div>
            <div class="label">WIN RATE</div>
        </div>
        <div class="stat-card">
            <div class="value" id="drawdown">0%</div>
            <div class="label">DRAWDOWN</div>
        </div>
    </div>
    
    <div class="sections">
        <div class="section">
            <h2>📊 RECIENTES TRADES</h2>
            <div id="trades-list">
                <p style="opacity:0.5;text-align:center;padding:20px;">Sin trades aún</p>
            </div>
        </div>
        <div class="section">
            <h2>📡 SEÑALES DETECTADAS</h2>
            <div id="signals-list">
                <p style="opacity:0.5;text-align:center;padding:20px;">Esperando señales...</p>
            </div>
        </div>
    </div>
    
    <button class="refresh" onclick="fetchData()">🔄 REFRESH</button>
    
    <script>
        async function fetchData() {
            try {
                const res = await fetch('/api/status');
                const data = await res.json();
                
                document.getElementById('capital').textContent = data.capital.toFixed(2);
                document.getElementById('pnl').textContent = data.daily_pnl.toFixed(2);
                document.getElementById('pnl').className = data.daily_pnl >= 0 ? 'positive' : 'negative';
                document.getElementById('total-pnl').textContent = data.total_pnl.toFixed(2);
                document.getElementById('total-pnl').className = data.total_pnl >= 0 ? 'positive' : 'negative';
                document.getElementId('trades').textContent = data.trades_today;
                document.getElementById('winrate').textContent = (data.win_rate * 100).toFixed(1) + '%';
                document.getElementById('drawdown').textContent = data.drawdown.toFixed(2) + '%';
                
                const statusEl = document.getElementById('status');
                statusEl.textContent = data.status;
                statusEl.className = 'status-badge ' + (data.status === 'RUNNING' ? 'running' : 'stopped');
                
            } catch(e) { console.error(e); }
        }
        
        async function fetchSignals() {
            try {
                const res = await fetch('/api/signals');
                const signals = await res.json();
                const container = document.getElementById('signals-list');
                
                if (signals.length === 0) {
                    container.innerHTML = '<p style="opacity:0.5;text-align:center;">Esperando señales...</p>';
                    return;
                }
                
                container.innerHTML = signals.slice(-10).reverse().map(s => 
                    `<div class="signal ${s.signal.toLowerCase()}">
                        <strong>${s.symbol}</strong> — ${s.signal} @ ${s.price?.toFixed(2) || 'N/A'}
                        <br><small>${new Date(s.timestamp).toLocaleTimeString()}</small>
                    </div>`
                ).join('');
                
            } catch(e) { console.error(e); }
        }
        
        // Refresh cada 5 segundos
        setInterval(fetchData, 5000);
        setInterval(fetchSignals, 5000);
        fetchData();
        fetchSignals();
    </script>
</body>
</html>
"""

# Save dashboard template
import os
template_dir = os.path.join(os.path.dirname(__file__), "templates")
os.makedirs(template_dir, exist_ok=True)
with open(os.path.join(template_dir, "dashboard.html"), "w") as f:
    f.write(DASHBOARD_HTML)
