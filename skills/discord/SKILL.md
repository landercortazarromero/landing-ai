---
name: discord
description: Discord ops via the message tool (channel=discord). Activar cuando Lander pida enviar mensajes, crear canales, o gestionar Discord.
---

# DISCORD — Elite Discord Operations

## Setup (requiere configurar primero)
```bash
# Verificar que discord tool está activo
# El tool usa OpenClaw message tool con channel=discord
```

## Quick Actions

### Send Message
```bash
# Usar message tool con channel=discord
/message channel=discord to="#general" text="Hello"
```

### Send DM
```bash
/message channel=discord to="@username" text="DM message"
```

### Create Channel
(requiere bot permissions)

## Notes
- Necesita OpenClaw configured con cuenta Discord
- `channel=discord` en message tool
- Ver docs: https://docs.openclaw.ai/discord