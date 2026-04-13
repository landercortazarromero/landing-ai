---
name: imsg
description: iMessage/SMS CLI for listing chats, history, and sending messages via Messages.app. INSTALLED via brew. Activar cuando Lander pida enviar iMessage o buscar conversaciones.
---

# IMSG — iMessage CLI (INSTALLED ✅)

## Estado
✅ Instalado: `/opt/homebrew/bin/imsg`

## Comandos

### Enviar mensaje
```bash
imsg send "+34600000000" "Mensaje de texto"
imsg send "contacto@email.com" "Mensaje"
```

### Listar chats
```bash
imsg chats list
imsg chats list --limit 20
```

### Buscar historial
```bash
imsg history "texto a buscar"
imsg history "texto" --limit 50
```

### Info contacto
```bash
imsg contact info "+34600000000"
```

## Notas
- Usa la app Messages de macOS
- Necesita Mac con Messages configurado
- No funciona para chats de grupo