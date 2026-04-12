---
name: node-connect
description: Diagnose OpenClaw node connection and pairing failures for Android, iOS, and macOS companion apps. Use when QR/setup code/manual connect fails, local Wi-Fi works but VPS/tailnet does not, or errors mention pairing required, unauthorized, bootstrap token invalid or expired.
---

# NODE-CONNECT — Elite Node Diagnostics

## Quick Diagnosis
```bash
# Ver estado del gateway
openclaw gateway status

# Ver nodes conectados
openclaw nodes list

# Diagnosticar problema específico
openclaw diagnose
```

## Common Issues

### QR Code / Setup Code Fail
1. Verificar que companion app soporta versión actual
2. Asegurar que están en la misma red
3. Regenerar setup code: `openclaw pairing regenerate`
4. Ver logs: `openclaw logs --recent 50`

### Bootstrap Token Expired
```bash
# Regenerar token
openclaw pairing regenerate-token
# Re-pair desde app
```

### Tailscale / Remote URL Issues
```bash
# Verificar gateway config
openclaw config get gateway.bind
openclaw config get gateway.remote.url

# Test conexión
openclaw diagnose --test-connection
```

## Logs
```bash
openclaw logs --recent 100
openclaw logs --level error
openclaw logs --since "1 hour ago"
```

## Reset
```bash
openclaw gateway restart
openclaw reset pairing
```