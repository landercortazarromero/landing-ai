# MISTAKES LEARNED — Errores y Soluciones

**Last Updated:** 2026-03-26

## 2026-03-26

### Error: Modelo incorrecto instalado
**Situación:** Se instaló minimax-m2.5 en lugar de minimax-m2.7
**Impacto:** Configuración incompleta, requería corrección
**Solución:** Verificar versión exacta antes de instalar. Siempre confirmar: `ollama list | grep modelo`
**Prevención:** Script de verificación post-instalación

### Error: Cron job duplicado
**Situación:** openclaw-backup.sh aparecía 2 veces en crontab
**Impacto:** Backup redundante, recursos desperdiciados
**Solución:** `crontab -l | sort | uniq | crontab -`
**Prevención:** Script de validación de cron jobs

### Error: Memory gap — active-tasks.md no existía
**Situación:** No había tracking de proyectos en curso
**Impacto:** Pérdida de contexto entre sesiones
**Solución:** Crear active-tasks.md con estructura priorizada
**Prevención:** Crear automáticamente si no existe al inicio

---

## 2026-03-24

### Error: Deploy web requería autenticación manual
**Situación:** Netlify requería intervención del usuario para subir archivos
**Impacto:** No 100% autónomo
**Solución:** Configurar deploy vía CLI con token o usar Netlify Drop
**Prevención:** Implementar webhook auto-deploy para futuros cambios

---

## Patrones Detectados

**Patrón:** Configuración incompleta antes de declarar "listo"
**Impacto:** Re-trabajo, correcciones posteriores
**Solución:** Checklist de verificación obligatoria

**Patrón:** Skills instaladas pero no documentadas en MEMORY.md
**Impacto:** Desconocimiento de capacidades disponibles
**Solución:** Actualizar MEMORY.md inmediatamente después de instalar skill

---

*Sistema Anti-Frágil — Documentar para No Repetir*
