---
name: gh-issues
description: Fetch GitHub issues, spawn sub-agents to implement fixes and open PRs, then monitor and address PR review comments. Optimizado para eficiencia máxima. Usage: /gh-issues [owner/repo] [--label bug] [--limit 5] [--milestone v1.0] [--assignee @me] [--fork user/repo] [--watch] [--interval 5] [--reviews-only] [--cron] [--dry-run]
---

# GH-ISSUES — Elite Issue Management

## Quick Start
```bash
/gh-issues owner/repo --limit 10
/gh-issues owner/repo --label bug
/gh-issues owner/repo --assignee @me
```

## Flags Disponibles
| Flag | Uso |
|------|-----|
| `--label` | Filtrar por label (bug, feature, etc.) |
| `--limit` | Número de issues (default: 5) |
| `--milestone` | Filtrar por milestone |
| `--assignee` | Filtrar por asignado |
| `--fork` | Hacer fork antes de trabajar |
| `--watch` | Monitorear nuevos issues |
| `--interval` | Intervalo de check (minutos) |
| `--reviews-only` | Solo issues con reviews |
| `--dry-run` | Solo mostrar, no ejecutar |
| `--cron` | Activar cron job |

## Workflow
1. Fetch issues según filtros
2. Spawn sub-agent por cada issue
3. Sub-agent implementa fix
4. Abre PR automáticamente
5. Monitor review comments
6. Address feedback si hay

## Projectos Activos en MEMORY.md
Ver MEMORY.md para projectos activos y sus repos.