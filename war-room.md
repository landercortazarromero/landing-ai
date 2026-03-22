# War Room Coordination System

**Created:** 2026-03-22
**For:** KORTA (Asistente Personal L7)
**Owner:** Lander

---

## 🎯 Purpose

Centro de comando unificado para orquestación de tareas, monitoreo de agentes y gestión de crisis.

---

## 📋 Dashboard Components

### 1. Active Tasks Monitor
```
┌─────────────────────────────────────────┐
│ ACTIVE TASKS          Status: 🟢 LIVE   │
├─────────────────────────────────────────┤
│ ID    | Task           | Agent  | Time │
│------|------------------|--------|------│
│ T001  | Doc creation   | KORTA  | 2m   │
│ T002  | Skill install  | Auto   | 5m   │
└─────────────────────────────────────────┘
```

### 2. Sub-Agent Status
```
┌─────────────────────────────────────────┐
│ SUB-AGENTS              3 Active        │
├─────────────────────────────────────────┤
│ Agent    | Task        | Status | Load  │
│---------|-------------|--------|-------│
│ Codex-1  | Coding      | 🟢     | 45%   │
│ Claude   | Review      | 🟡     | 80%   │
│ Pi       | Analysis    | 🟢     | 30%   │
└─────────────────────────────────────────┘
```

### 3. Alert Feed
```
┌─────────────────────────────────────────┐
│ ALERTS                    Last 24h    │
├─────────────────────────────────────────┤
│ 🟡 WARN  | High latency   | 17:30     │
│ 🟢 INFO  | Task complete  | 17:25     │
│ 🔴 CRIT  | Agent failed   | 17:15     │
└─────────────────────────────────────────┘
```

---

## 🚨 Alert Levels

### 🔴 CRITICAL (Immediate Action)
- Agent failure
- Security breach
- Data loss risk
- **Response:** < 1 min, notify Lander

### 🟡 WARNING (Monitor Closely)
- High latency (> 30s)
- Resource exhaustion
- Skill unavailable
- **Response:** < 5 min, auto-remediate

### 🟢 INFO (Log Only)
- Task completion
- Normal operations
- **Response:** Log, no action

---

## ⚡ Crisis Protocols

### Protocol A: Agent Failure
1. Detect failure via heartbeat
2. Kill hung processes
3. Respawn agent with same task
4. Notify COO
5. Escalate to Lander if 3 failures

### Protocol B: System Overload
1. Monitor queue depth
2. Pause non-critical tasks
3. Scale to cloud models
4. Notify CFO of cost impact
5. Queue tasks for later

### Protocol C: Security Alert
1. Isolate affected component
2. Log incident details
3. Notify Lander immediately
4. Preserve evidence
5. Await instructions

---

## 📊 Priority Matrix

| Priority | Response Time | Escalation |
|----------|--------------|------------|
| P0 - Critical | < 1 min | Lander + CEO |
| P1 - High | < 5 min | COO |
| P2 - Normal | < 30 min | Auto |
| P3 - Low | < 4 hours | Queue |

---

## 🔄 Auto-Actions

### Every 5 Minutes
- Check agent health
- Update task status
- Rotate logs

### Every 30 Minutes
- Generate status report
- Check resource usage
- Review queue depth

### Every 24 Hours
- Generate daily summary
- Archive old logs
- Update metrics

---

## 🎮 Manual Commands

```bash
# Check all systems
openclaw status

# List active agents
process action:list

# Kill stuck agent
process action:kill sessionId:XXX

# Force heartbeat
openclaw system event --text "Manual check" --mode now
```

---

## 📈 Success Metrics

- **Uptime:** > 99.5%
- **Response Time:** < 10s avg
- **False Alerts:** < 5%
- **Recovery Time:** < 2 min

---

*Next Review: 2026-03-29*