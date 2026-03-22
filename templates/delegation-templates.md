# Delegation Templates

## Quick Delegation Patterns

### Code Task
```
Task: [description]
Output: [file path]
Requirements: [specifics]
Verify: [checkpoints]
```

### Research Task
```
Topic: [subject]
Depth: [brief/detailed]
Output: [summary/report]
Sources: [preferred]
```

### Document Creation
```
Topic: [subject]
Format: [markdown/pdf/etc]
Sections: [outline]
Tone: [formal/casual]
```

### Analysis Task
```
Data: [source]
Analysis: [type]
Output: [format]
Visualizations: [yes/no]
```

## Agent Selection Guide

| Task Type | Primary Agent | Backup | Notes |
|-----------|--------------|--------|-------|
| Code | Codex | Claude | Use --full-auto |
| Review | Claude | Codex | Use --print mode |
| Research | Web + KORTA | Pi | Verify sources |
| Writing | Claude | KORTA | Specify tone |
| Analysis | Pi | KORTA | Check data quality |

## Escalation Triggers

- Agent fails 3x → Switch agent
- Task > 30 min → Notify Lander
- Unclear requirements → Ask before proceeding
- Security concern → Stop + Alert