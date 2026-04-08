# MEMORY.md - Long-Term Memory

**Last Updated:** 2026-04-05

## Skills Available
- **Core:** 52 total, 21 activos (40%)
- **Instalados recientemente:** things-mac, obsidian, model-usage, summarize, blogwatcher, xurl
- **Uso intensivo:** coding-agent, github, skill-creator, notion

## Projects Active
- L7 God Mode Activation (COMPLETADO)
- Sistema de memoria anti-frágil (OPERATIVO)
- **C-Level Team Architecture (OPERATIVO - 8/8 Agents)**
  - ✅ TITAN-OS (Orchestrator)
  - ✅ JORGE CARRASCO (Autoconocimiento)
  - ✅ OMEN X (Mentor Trading)
  - ✅ CANVAS (Chief Design Officer)
  - ✅ BRAND (Chief Brand Officer)
  - ✅ PIXEL (Senior Frontend Dev)
  - ✅ NEXUS (Infrastructure)
  - ✅ SCRIBE (Memory & Documentation)
- War Room Coordination (COMPLETADO)
- Opportunity Discovery Engine (COMPLETADO)
- **Web ELITE JSR - AGENCIA DE PILOTOS ÉLITE (ONLINE - 2026-03-24)**
- **OMEN X Trading Bot (TESTNET - 2026-04-08)**
  - Location: `agents/OMEN-X/bot-trading/`
  - Capital: €1,000 virtual (testnet)
  - Exchange: Binance Futures Testnet
  - Estrategia: Portfolio con 3 estrategias (EMA + MACD + Bollinger)
  - Risk: 1.5% por trade, -5% drawdown max diario
  - Dashboard web + Telegram alerts
  - Duración testnet: 7 días
  - URL: https://euphonious-pixie-e28440.netlify.app
  - Hosting: Netlify (gratis, permanente)
  - Ubicación local: `~/.openclaw/workspace/web-agencia/`
  - Archivo principal: `index.html` (550 líneas)
  - Diseño: Negro + azul neón (futurista)
  - Pilotos: 5 (Ian, Lander, Andoni, Aitzol, Iñaki)
  - Dossiers completos: Ian (#62), Lander (#59), Iñaki (#28)
  - Dossiers pendientes: Andoni (#11), Aitzol (#41)
  - Secciones: Header, Hero, Stats, Pilotos, Modales, Patrocinios, Contacto, Footer
  - **Estructura cliente:** `/clients/ELITE-JSR/` creada

## Important Decisions
- **2026-03-22:** Activado L7 God Mode por Lander
- **Modelo default:** ollama/minimax-m2.7:cloud
**Sistema:** Hybrid Labs L2 ACTIVADO (2026-03-27)
**Status:** 8/8 agents v10.0 operativos, 15 crons activos
**L7 Score:** 4.9/5.0 → 5.0/5.0
- **Filosofía:** NUNCA decir no puedo, SIEMPRE encontrar la manera

## CRITICAL ISSUE: Data Mixing (2026-04-07) — **RESUELTO 2026-04-08** ✅
**Problema:** Cada nuevo piloto hereda datos del piloto anterior
**Causa raíz:** MASTER-TEMPLATE no tiene 100% placeholders
**Solución implementada:** 
- ✅ Nuevo TEMPLATE-MASTER.html con 100% placeholders ({{NOMBRE}}, {{APELLIDO}}, etc.)
- ✅ Script `pilot-generator.sh` v2.0 con Anti-Data-Mixing Protocol
- ✅ Verificación automática: grep por nombres previos (ian|iñaki|traba|lander)
- ✅ Procedimiento documentado paso a paso

**Procedimiento para nuevos pilotos:**
```bash
# Uso del generador
~/.openclaw/workspace/scripts/pilot-generator.sh \
  -n ANDONI -a SANCHEZ -d 11 -c "#ff0055" \
  -e "piloto@email.com" -i "andoni11"

# Añadir fotos y deploy
cd ~/.openclaw/workspace/clients/andoni-sanchez-11/web
# Copiar fotos a images/
vercel --yes --prod
```

**Template seguro:** `/clients/MASTER-TEMPLATE/web/TEMPLATE-MASTER.html`
**Script:** `/scripts/pilot-generator.sh`

## Updates Recientes
- **2026-04-08:** Data Mixing RESUELTO — TEMPLATE-MASTER v2.0 + pilot-generator.sh
  - Placeholders 100% en TEMPLATE-MASTER.html
  - Script generador con verificación anti-mixing
  - Procedimiento documentado y probado

## Lessons Learned
- No responder sin verificar archivos primero
- Sub-agentes pueden time-out en tareas largas → inline es más seguro para tareas críticas
- Vercel vs Netlify: Lander prefiere Vercel para nuevos deployments
- MASTER-TEMPLATE debe tener 100% placeholders para evitar data mixing entre pilotos
- Tareas críticas hacer inline, no delegar a sub-agentes (evita timeouts)

## Configuration
- **Timezone:** Europe/Madrid
- **User:** Lander
- **Identity:** KORTA, Asistente Personal L7
- **Emoji:** 🎯
- **OpenClaw:** 2026.4.2
- **Skills:** 23/52 ready
