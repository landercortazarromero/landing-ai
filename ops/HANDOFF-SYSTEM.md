# HANDOFF SYSTEM — Coordinación Multi-Agente

**Last Updated:** 2026-03-26  
**Status:** ✅ Operativo

---

## PROTOCOLO DE HANDOFF

Cuando una tarea requiere múltiples agents, se ejecuta este protocolo:

### 1. IDENTIFICAR AGENTES REQUERIDOS
```
TITAN-OS (Orchestrator) → Siempre activo
CANVAS (Diseño) → Si requiere UI/UX
BRAND (Marca) → Si requiere identidad
PIXEL (Código) → Si requiere desarrollo
NEXUS (Infra) → Si requiere deploy/DevOps
SCRIBE (Docs) → Si requiere documentación
```

### 2. SECUENCIA DE HANDOFF

**Ejemplo: Nueva Landing Page**
```
1. TITAN-OS recibe request
2. TITAN-OS → BRAND (definir messaging)
3. BRAND → CANVAS (crear diseño)
4. CANVAS → PIXEL (implementar código)
5. PIXEL → NEXUS (deploy a producción)
6. NEXUS → SCRIBE (documentar)
7. SCRIBE → TITAN-OS (reportar completado)
```

### 3. FORMATO DE HANDOFF

Cada handoff incluye:
- Contexto completo del proyecto
- Assets entregados por agent anterior
- Criterios de aceptación
- Deadline
- Próximo agente en pipeline

### 4. ESTADOS DE HANDOFF

- 🟡 **PENDING** — Esperando agente anterior
- 🟢 **IN PROGRESS** — Agent actual trabajando
- 🔵 **REVIEW** — Esperando aprobación
- ✅ **COMPLETED** — Handoff finalizado
- 🔴 **BLOCKED** — Bloqueado, necesita intervención

---

## TEMPLATES DE HANDOFF

### Template: Diseño → Código
```
HANDOFF: CANVAS → PIXEL
Proyecto: [Nombre]
Assets entregados:
- Mockup: [ruta]
- Design system: [ruta]
- Especificaciones: [ruta]
Stack recomendado: [HTML/CSS/JS/React/etc]
Deadline: [Fecha]
```

### Template: Código → Deploy
```
HANDOFF: PIXEL → NEXUS
Proyecto: [Nombre]
Repositorio: [ruta]
Rama: [main/develop]
Entorno destino: [staging/producción]
Variables de entorno requeridas: [lista]
```

---

## AUTOMATIZACIÓN

Los handoffs se registran automáticamente en:
`/clients/[CLIENT]/HANDOFF-LOG.md`

Cada entrada incluye timestamp, agente origen, agente destino, y estado.

---

*Sistema de coordinación multi-agente — L7+ God Mode*
