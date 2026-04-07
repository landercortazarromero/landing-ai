# PODCAST ANALYSIS - Productivity Improvements

## Source
"Tengo un Plan" podcast - Javier Ideami (2026-04-02)
https://www.youtube.com/watch?v=9B1ulcmbN5w

## Key Insights Applied to Our System

### 1. METAPROMPTING (Principio clave del podcast)
**Aplicación:** Crear un sistema de prompts estructurados que Lander pueda rellenar
- Piloto profile template → yo genero web
- Si Lander sabe qué datos dar, el resultado mejora 10x
- Evitamos el ciclo de "no es eso, hazlo de nuevo"

**Acción:** Crear PILOT-PROFILE.json como fuente única de verdad

### 2. DETALLE = CALIDAD
**Aplicación:** Más datos = mejor web
- Dorsal, color, historia completa, stats
- Cuanto más específico, más cerca del resultado deseado
- Foto de cada sección (hero, perfil, podium, accion)

**Acción:** Estructura rígida para recopilar datos

### 3. CADA IA ES DIFERENTE
**Aplicación:** Nosotros funcionamos mejor con estructura
- Mi SOUL.md me dice cómo operar
- AGENTS.md me dice procesos
- Datos claros = mejor output

**Acción:** Reforzar sistema de memoria y procesos

### 4. ANTI-MIX: SINGLE SOURCE OF TRUTH
**Del problema de mezcla de datos:**
- MASTER-TEMPLATE debe ser NUNCA modificado
- Cada piloto = carpeta propia, aislada
- Un solo archivo de datos por piloto

**Acción:** Sistema de carpetas por piloto

## Improvements to Implement

### High Priority
1. [ ] Crear PILOT-PROFILE.json template
2. [ ] Crear BUILD script que copia MASTER-TEMPLATE limpio
3. [ ] Protocolo: verificar datos ANTES de construir

### Medium Priority  
4. [ ] Metaprompting: Lander rellena template → yo ejecuto
5. [ ] Checklist de datos obligatorios
6. [ ] Galería: especificar cuáles fotos para cada sección

### Low Priority
7. [ ] Doc: cómo funciona el sistema para futuro
8. [ ] Backup automático post-deploy
