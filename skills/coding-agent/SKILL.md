---
name: coding-agent
description: Delegate coding tasks to Codex, Claude Code, or Pi agents via background process. Optimizado para máxima eficiencia. Use when: (1) building/creating new features or apps, (2) reviewing PRs (spawn in temp dir), (3) refactoring large codebases, (4) iterative coding that needs file exploration. NOT for: simple one-liner fixes (just edit), reading code (use read tool).
---

# CODING-AGENT — Elite Code Delegation

## Agents Disponibles

| Agente | Comando | Mejor para |
|--------|---------|------------|
| **Claude Code** | `--print --permission-mode bypassPermissions` | Frontend, scripts |
| **Codex** | `pty:true` | General coding |
| **Pi/OpenCode** | `pty:true` | Exploración |

## Spawning Rápido

### Nuevo proyecto
```bash
openclaw sessions spawn --runtime subagent --model claude-sonnet --task "Build a [DESCRIPCIÓN] with [TECNOLOGÍA]" --mode run
```

### PR Review
```bash
openclaw sessions spawn --runtime subagent --task "Review PR at [URL] - check for bugs, security issues, and code quality" --mode run --cwd /tmp/pr-review
```

### Refactoring
```bash
openclaw sessions spawn --runtime subagent --task "Refactor [ARCHIVO/CARPETA] - improve [QUÉ MEJORAR]" --mode run
```

## Configuración Recomendada

### Claude Code (preferido para frontend)
```bash
--model anthropic/claude-sonnet-4-20250514
--timeout 300
```

### Codex (general)
```bash
--runtime acp
--pty true
--timeout 600
```

## Casos de Uso

### NUEVO PROYECTO
1. Definir specs (qué, cómo, stack)
2. Spawn agent con task completa
3. Agent crea boilerplate + implementa
4. Review + deploy

### PR REVIEW
1. Clone repo en /tmp
2. Spawn agent con task "Review PR #XXX"
3. Agent analiza y reporta issues
4. Aplicar fixes sugeridos

### LARGE REFACTOR
1. Identificar archivos a refactorizar
2. Spawn agent con contexto completo
3. Agent hace cambios incrementalmente
4. Validar que tests pasan

## ⚠️ NO USAR para:
- Fijes simples (usa `edit` directo)
- Leer código (usa `read` tool)
- ACP harness threads (usa `sessions_spawn` con `runtime:"acp"`)
- Work en ~/clawd workspace

## Optimización
Mantener --timeout largo para proyectos grandes. Usar --light-context cuando hay mucho contexto previo.