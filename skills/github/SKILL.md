---
name: github
description: GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, API queries. Optimizado para workflow rápido y eficiencia máxima. Usa cuando: (1) checking PR status or CI, (2) creating/commenting on issues, (3) listing/filtering PRs or issues, (4) viewing run logs. NOT for: complex web UI interactions.
---

# GITHUB — Elite GitHub Operations

## Quick Commands

### Issues
```bash
gh issue list --state open --limit 10
gh issue view 123
gh issue create --title " Título" --body "Descripción"
gh issue close 123
```

### PRs
```bash
gh pr list --state open
gh pr view 456
gh pr create --title "Título" --body "Descripción"
gh pr merge 456 --squash
gh pr checkout 456
```

### CI/CD
```bash
gh run list --limit 5
gh run view 789
gh run watch 789  # Watch in real-time
```

### Repo
```bash
gh repo clone owner/repo
gh repo view
gh repo list --limit 10
```

## Workflows Optimizados

### Crear PR con descripción
```bash
gh pr create --title "[TIPO] descripción" --body "## Qué\n- cambio\n## Por qué\n- razón\n## Testing\n- verificado"
```

### Code Review rápido
```bash
gh pr view 123 --comments
gh pr review 123 --approve --comment "LGTM"
```

### Buscar issues con label
```bash
gh issue list --label bug --state open --limit 20
```

## API Queries (para scripts)
```bash
gh api repos/owner/repo/releases/latest
gh api repos/owner/repo/issues --jq '.[] | {title, state}'
```

## Auto-completion
Añadir a ~/.zshrc:
```bash
eval "$(gh completion -s zsh)"
```