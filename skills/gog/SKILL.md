---
name: gog
description: Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs. INSTALLED via npm. Optimizado para gestión de email y calendario.
---

# GOG — Google Workspace CLI (INSTALLED ✅)

## Estado
✅ Instalado: `/Users/landercortazarromero/.npm-global/bin/gog`

## Setup
```bash
gog auth  # Autenticar con Google
gog auth --reauth  # Re-autenticar
```

## Gmail

### Ver mensajes
```bash
gog gmail list --limit 10
gog gmail list --unread
gog gmail list --search "from:lander"
```

### Enviar email
```bash
gog gmail send --to "email@example.com" --subject "Asunto" --body "Contenido"
```

### Gestionar
```bash
gog gmail archive ID
gog gmail trash ID
```

## Calendar

### Ver eventos
```bash
gog calendar list --today
gog calendar list --upcoming
gog calendar list --date 2026-04-15
```

### Crear evento
```bash
gog calendar create "Reunión" --start "2026-04-15 10:00" --end "2026-04-15 11:00"
```

## Drive

```bash
gog drive list
gog drive upload file.pdf
```

## Notes
- Requiere auth con cuenta Google
- Scopes limitados a lo necesario
- Ideal para gestión de email desde terminal