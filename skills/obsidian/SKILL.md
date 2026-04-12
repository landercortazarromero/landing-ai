---
name: obsidian
description: Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli. Optimizado para gestión de conocimiento personal.
---

# OBSIDIAN — Elite Knowledge Management

## Vault Location
`~/.obsidian/vaults/`

## Comandos principales
```bash
obsidian list
obsidian search "query"
obsidian note create "Título"
obsidian note read "path/to/note.md"
```

## Vaults Disponibles
Verificar con `obsidian list`

## Automatización

### Crear nota rápida
```bash
obsidian note create "Nota del día: YYYY-MM-DD"
```

### Buscar en notas
```bash
obsidian search "palabra clave"
```

### Listar notas recientes
```bash
obsidian list --recent 10
```

## Estructura recomendada
```
vault/
├── 00-Inbox/
│   └── notes.md
├── 01-Projects/
│   └── project-name.md
├── 02-Areas/
│   └── area-name.md
├── 03-Resources/
│   └── topic-notes.md
└── Z-Templates/
    └── template.md
```

## Integración con Sistema de Memoria

### Daily Notes
Crear nota diaria:
```bash
obsidian note create "$(date '+%Y-%m-%d')" --folder "Daily Notes"
```

### Buscar en memoria
```bash
obsidian search "YYYY-MM-DD"
```