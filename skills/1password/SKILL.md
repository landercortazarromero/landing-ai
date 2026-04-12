---
name: 1password
description: Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in (single or multi-account), or reading/injecting/running secrets via op. Optimizado para gestión de secrets.
---

# 1PASSWORD — Elite Secret Management

## Quick Commands

### Auth
```bash
op signin
op signin --account my.1password.com
op signin --using --secrets-dir ~/.config/op
```

### Items
```bash
op item list
op item get "Item Name"
op item get "Item Name" --fields password
op item create --title "Nuevo item" --vault "Personal"
op item edit "Item Name" --password "newpass"
```

### Password Generator
```bash
op generate password --length 24
op generate password --symbols --length 32
op generate passphrase --words 4
```

### Secrets Injection
```bash
eval "$(op env)"
op run --env-file .env -- echo $MY_SECRET
op inject -f .env.template > .env
```

## Workflows

### Get password rápido
```bash
op item get "Netflix" --field password | pbcopy
```

### Deploy con secrets
```bash
op run --env-file .env.enc -- your-deploy-script.sh
```

### Auto-fill
```bash
op autofill "https://login.example.com"
```

## Tips
- Usa `--vault` flag para especificar vault
- `op signin` solo una vez por sesión
- Para CI/CD: usa `op signin --using` con bootstrap token