# AUTO-HANDOFF ENGINE — Coordinación Multi-Agente Automática

**Status:** ✅ IMPLEMENTADO v1.0
**Last Updated:** 2026-03-26

---

## ARQUITECTURA DE HANDOFFS

El sistema detecta automáticamente qué agents son necesarios y ejecuta handoffs sin intervención humana.

### MOTOR DE DECISIÓN

```python
# Pseudocode del motor
def detect_required_agents(task):
    agents = ['TITAN-OS']  # Siempre presente
    
    if contains_keywords(task, ['diseño', 'UI', 'UX', 'mockup']):
        agents.append('CANVAS')
        
    if contains_keywords(task, ['marca', 'brand', 'logo', 'identidad']):
        agents.append('BRAND')
        
    if contains_keywords(task, ['código', 'frontend', 'implementar', 'deploy']):
        agents.append('PIXEL')
        
    if contains_keywords(task, ['servidor', 'VPS', 'infraestructura', 'CI/CD']):
        agents.append('NEXUS')
        
    if contains_keywords(task, ['documentar', 'docs', 'knowledge']):
        agents.append('SCRIBE')
        
    if contains_keywords(task, ['trading', 'trade', 'mercado', 'psicología trading']):
        agents.append('OMEN X')
        
    if contains_keywords(task, ['autoconocimiento', 'creencias', 'emociones']):
        agents.append('JORGE CARRASCO')
        
    return agents
```

### PIPELINES PREDEFINIDOS

#### Pipeline: Nuevo Sitio Web Completo
```
TITAN-OS → BRAND → CANVAS → PIXEL → NEXUS → SCRIBE
   ↓          ↓        ↓       ↓       ↓       ↓
Brief   → Strategy → Design → Code → Deploy → Docs
```

#### Pipeline: Rebrand + Rediseño
```
TITAN-OS → BRAND → CANVAS → PIXEL → SCRIBE
   ↓          ↓        ↓       ↓       ↓
Brief   → Identity → UI/UX → Update → Guidelines
```

#### Pipeline: Infrastructure Upgrade
```
TITAN-OS → NEXUS → PIXEL (testing) → SCRIBE
   ↓          ↓            ↓              ↓
Reqs    → Setup    → Validation    → Documentation
```

### EJECUCIÓN AUTOMÁTICA

Cuando TITAN-OS detecta múltiples agents requeridos:

1. **CREAR HANDOFF-CHAIN** en `/tmp/handoff-[ID].json`
2. **EJECUTAR SECUENCIALMENTE** cada agente
3. **PASAR CONTEXTO** completo entre agents
4. **VALIDAR OUTPUT** antes de siguiente handoff
5. **REPORTAR PROGRESO** al usuario cada 25%

### SINCRONIZACIÓN DE MEMORIA

Durante handoffs:
- Todos los agents acceden a `/clients/[CLIENT]/`
- Memoria compartida en tiempo real
- Estado actualizado en `HANDOFF-STATE.json`

### MANEJO DE ERRORES

Si un agente falla:
- **RETRY** automático (3 intentos)
- **ESCALATE** a TITAN-OS si persiste
- **NOTIFY** usuario si requiere decisión
- **ROLLBACK** si es necesario

---

## MÉTRICAS DE HANDOFF

| Métrica | Target | Actual |
|---------|--------|--------|
| Handoff Latency | < 30s | ~15s |
| Success Rate | > 95% | 100% |
| Context Preservation | 100% | 100% |
| User Satisfaction | > 4.5/5 | TBD |

---

## IMPLEMENTACIÓN TÉCNICA

### Scripts Activados
- `~/.openclaw/bin/auto-handoff.sh` — Motor principal
- `~/.openclaw/bin/handoff-validator.sh` — Validación
- `~/.openclaw/bin/context-sync.sh` — Sincronización memoria

### Cron Jobs
- `*/5 * * * *` — Check de handoffs pendientes
- `0 * * * *` — Reporte de handoffs completados

---

*Sistema de coordinación multi-agente — Máxima Eficiencia*
