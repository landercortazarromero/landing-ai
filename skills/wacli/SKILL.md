---
name: wacli
description: Send WhatsApp messages to other people or search/sync WhatsApp history via the wacli CLI. INSTALLED via brew. Usar SOLO cuando Lander pida contactar a alguien específico.
---

# WACLI — WhatsApp CLI (INSTALLED ✅)

## Estado
✅ Instalado: `/opt/homebrew/bin/wacli` v0.2.0

## Comandos

### Enviar mensaje
```bash
wacli send text --to "+34600000000" --message "Hola, mensaje desde CLI"
```

### Buscar chats
```bash
wacli chats list --limit 20
wacli chats list --query "nombre"
```

### Buscar mensajes
```bash
wacli messages search "texto" --limit 20
```

### Sync historial
```bash
wacli sync --follow
```

## Seguridad
- Confirmar siempre recipient + mensaje antes de enviar
- No usar para chats normales (OpenClaw los maneja)

## Auth (solo primera vez)
```bash
wacli auth  # QR login
```