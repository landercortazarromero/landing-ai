# ERRORES SOLUCIONADOS — Registro

**Protocolo:** Detectar → Solucionar → Documentar → Prevenir  
**Last Updated:** 2026-03-27

---

## [2026-03-27] — GitHub Token Fine-Grained no funciona para push
**Problema:** Tokens `github_pat_*` (Fine-Grained) no tienen permiso de escritura en repos. Error 403 al hacer push.
**Solución:** Usar Classic token (`ghp_*`) con scope `repo` completo.
**Prevención:** Documentado. Token Classic generado y funcionando.
**Status:** ✅ SOLUCIONADO — Deploy automático activo

## [2026-03-27] — GitHub Pages activación via API
**Problema:** Activación manual requerida en Settings > Pages
**Solución:** Usar GitHub API directamente para activar Pages
**Comando:** `curl -X POST -H "Authorization: token TOKEN" https://api.github.com/repos/USER/REPO/pages`
**Prevención:** Guardar token con scope `repo` + `workflow` para operaciones API
**Status:** ✅ SOLUCIONADO — Pages activado via API automáticamente

---

*Lista actualizada*