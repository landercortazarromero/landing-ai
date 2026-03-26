# VPS MIGRATION PLAN — L7+ God Mode Cloud

**Priority:** HIGH  
**ETA:** 2-3 hours  
**Cost:** ~$5-10/month

---

## CURRENT STATE
- **Host:** MacBook Air local
- **Uptime:** Dependiente del Mac
- **Access:** Solo cuando Mac está encendido
- **Backup:** Local + Git

## TARGET STATE
- **Host:** VPS (DigitalOcean/AWS/Linode)
- **Uptime:** 99.9% (24/7/365)
- **Access:** Desde cualquier dispositivo
- **Backup:** Cloud + Snapshots

---

## MIGRATION STEPS

### Phase 1: VPS Setup (30 min)
1. Crear cuenta en DigitalOcean/AWS
2. Crear droplet Ubuntu 22.04 LTS
3. Configurar SSH keys
4. Instalar Node.js, npm, Git

### Phase 2: OpenClaw Install (20 min)
1. Instalar OpenClaw global: `npm i -g openclaw`
2. Copiar configuración: `~/.openclaw/`
3. Instalar modelos Ollama
4. Configurar Telegram bot

### Phase 3: Data Migration (15 min)
1. Sync workspace: `rsync -avz workspace/ vps:~/workspace/`
2. Copiar agents: `rsync -avz agents/ vps:~/.openclaw/agents/`
3. Copiar config: `rsync openclaw.json vps:~/.openclaw/`

### Phase 4: DNS + SSL (15 min)
1. Configurar dominio (opcional)
2. Instalar SSL con Let's Encrypt
3. Configurar reverse proxy (nginx)

### Phase 5: Validation (10 min)
1. Test conexión Telegram
2. Test modelo minimax-m2.7
3. Test skills
4. Test agents

---

## POST-MIGRATION
- Actualizar MEMORY.md con nueva infra
- Configurar monitoreo externo (UptimeRobot)
- Documentar acceso SSH

---

*Plan de migración cloud — Máxima disponibilidad*
