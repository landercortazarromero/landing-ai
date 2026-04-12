---
name: things-mac
description: Manage Things 3 via the `things` CLI on macOS (add/update projects+todos via URL scheme; read/search/list from the local Things database). Use when a user asks to add a task to Things, list inbox/today/upcoming, search tasks, or inspect projects/areas/tags.
---

# THINGS-MAC — Elite Things 3 Management

## Quick Commands

### Add Task
```bash
things add "{{TASK_NAME}}" --list "Inbox"
things add "{{TASK}}" --project "{{PROJECT}}" --due "today"
things add "{{TASK}}" --area "{{AREA}}" --tags "urgent,work"
```

### Projects
```bash
things projects list
things projects show "{{PROJECT}}"
things projects create "{{NAME}}"
```

### Areas
```bash
things areas list
things areas show "{{AREA}}"
```

### Tags
```bash
things tags list
things tags show "{{TAG}}"
```

### Search & List
```bash
things list --today
things list --upcoming
things list --inbox
things list --someday
things search "{{QUERY}}"
```

### Complete & Delete
```bash
things complete "{{TASK_ID}}"
things delete "{{TASK_ID}}"
```

## Workflows

### Morning Review
```bash
things list --today
things list --upcoming
```

### Quick Add
```bash
things add "{{TASK}}" --due "tomorrow" --list "Inbox"
```

### Project Setup
```bash
things projects create "{{PROJECT_NAME}}"
things add "{{TASK}}" --project "{{PROJECT}}" --due "friday"
```

## Notes
- Requires Things 3 app on macOS
- `things` CLI usa URL scheme
- Los IDs son UUIDs