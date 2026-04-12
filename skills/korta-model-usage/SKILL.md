---
name: model-usage
description: Use CodexBar CLI local cost usage to summarize per-model usage for Codex or Claude, including the current (most recent) model or a full model breakdown. Trigger when asked for model-level usage/cost data from codexbar.
---

# MODEL-USAGE — Elite Cost Analytics

## Quick Commands

### Current Usage
```bash
codexbar cost
codexbar cost --current
```

### Full Breakdown
```bash
codexbar cost --all
codexbar cost --json
```

### By Model
```bash
codexbar cost --model claude-sonnet
codexbar cost --model gpt-4
codexbar cost --model ollama/minimax-m2.7:cloud
```

### Time Range
```bash
codexbar cost --today
codexbar cost --week
codexbar cost --month
```

## Parse Output
```bash
codexbar cost --json | jq '.total'
codexbar cost --json | jq '.models[].cost'
```

## Tips
- Útil para tracking de gasto en APIs
- Identificar modelos más caros
- Optimizar uso de modelos cheaper