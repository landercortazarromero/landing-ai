# ERRORS & SOLUTIONS

**Last Updated:** 2026-04-05

---

## 🚨 ERROR: Modelo dando respuestas falsas

**Fecha:** 2026-04-05  
**Gravedad:** CRÍTICO  
**Descripción:** El modelo (minimax-m2.7:cloud) dio respuestas incorrectas al inicio de sesión, diciendo "No tengo acceso a los archivos fuente" cuando SÍ tenía acceso.

**Archivos afectados:** Ninguno (solo fue respuesta incorrecta)

**Causa raíz:** El modelo no hizo verificación de archivos antes de responder. Asumió que no tenía acceso sin verificar.

**Solución aplicada:**
- Siempre ejecutar `exec` con `ls` o `find` para verificar existencia de archivos ANTES de responder
- Nunca asumir que no existe algo sin verificar primero
- Si hay duda, verificar con múltiples comandos

**Prevención:**
- Protocolo: "Verificar primero, responder después"
- Antes de cualquier afirmación sobre archivos/sistema, usar exec para confirmar
- NO confiar en suposiciones del modelo

---

## 📝 LEARNING

- **Accuracy > Speed:** Verificar antes de responder
- **Text > Memory:** Consultar archivos reales, no asumir
- **Self-Correction:** Si detecto que di información incorrecta, corregir inmediatamente

---
