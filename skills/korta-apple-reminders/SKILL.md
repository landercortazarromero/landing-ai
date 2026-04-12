---
name: apple-reminders
description: Manage Apple Reminders via the `remindctl` CLI on macOS (list, add, edit, complete, delete). Supports lists, date filters, and JSON/plain output. Optimizado para gestión rápida de tareas.
---

# APPLE-REMINDERS — Elite Task Management

## Quick Commands

### List Tasks
```bash
remindctl list
remindctl list --list "Inbox"
remindctl list --today
remindctl list --upcoming
remindctl list --json
```

### Add Task
```bash
remindctl add "Tarea importante" --list "Inbox"
remindctl add "Reunión" --due "2026-04-15" --list "Trabajo"
remindctl add "Proyecto" --due "tomorrow" --time "14:00"
```

### Complete/Delete
```bash
remindctl complete "Tarea importante"
remindctl delete "Tarea antigua"
```

### Lists
```bash
remindctl lists
remindctl list --list "Personal"
remindctl list --list "Trabajo"
```

## Workflow Optimizado

### Daily Review
```bash
remindctl list --today --json | jq '.[] | .title'
```

### Add from Terminal
```bash
remindctl add "{{TASK}}" --due "{{DATE}}" --list "{{LIST}}"
```

### Batch Complete
```bash
remindctl list --completed --json | jq '.[] | .title'
```

## Notes
- Requires macOS and Reminders app
- `remindctl` debe estar instalado