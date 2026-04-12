---
name: notion
description: Notion API for creating and managing pages, databases, and blocks. Optimizado para gestión de contenido y workflow.
---

# NOTION — Elite Notion Integration

## Quick Actions

### Pages
```bash
notion page create --title "Nueva página"
notion page list --limit 10
notion page read "PAGE_ID"
notion page update "PAGE_ID" --title "Título nuevo"
notion page delete "PAGE_ID"
```

### Databases
```bash
notion database list
notion database create --parent "PARENT_ID" --title "DB Name"
notion database query "DATABASE_ID"
```

### Blocks
```bash
notion block add "PAGE_ID" --type paragraph --content "Texto"
notion block children "PAGE_ID"
notion block update "BLOCK_ID" --content "Texto actualizado"
```

## Workflow

### Crear página desde CLI
```bash
notion page create --title "{{TITLE}}" --parent "{{PARENT_ID}}"
```

### Añadir bloque
```bash
notion block add "{{PAGE_ID}}" --type heading --content "{{CONTENT}}"
```

### Query database
```bash
notion database query "{{DB_ID}}" --filter "property:Status,select:Active"
```

## Tips
- Necesitas API key de Notion
- Guarda el token en variable de entorno: `NOTION_TOKEN`
- Page IDs son UUIDs largos