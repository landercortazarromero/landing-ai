# 🌐 PLANTILLA MAESTRA — Web de Piloto Jetski

**Estado:** LISTA PARA RELLENAR  
**Basada en:** Cortazar59 optimizada  
**Fecha:** 2026-04-06

---

## 📋 INSTRUCCIONES DE USO

1. Copiar esta carpeta y renombrar a `[NOMBRE]-[DORSAL]`
2. Rellenar TODOS los campos en DATOS-PILOTO.md
3. Copiar fotos a `web/images/`
4. Ejecutar `./BUILD.sh`
5. Web lista en Vercel

---

## 📁 ESTRUCTURA DE CARPETAS

```
PILOTO-XX/
├── web/
│   ├── index.html          ← No editar manualmente
│   └── images/
│       ├── hero.jpg         ← 1 foto (fondo hero)
│       ├── profile.jpg      ← 1 foto (perfil sobre mí)
│       ├── podium1.jpg      ← hasta 9 fotos
│       ├── podium2.jpg      ← ...
│       ├── galeria1.jpg     ← hasta 10 fotos
│       ├── galeria2.jpg     ← ...
│       └── ... más fotos
├── DATOS-PILOTO.md         ← RELLENAR AQUÍ
└── BUILD.sh               ← No editar
```

---

## 🔧 CAMPOS A RELLENAR

### SECCIÓN 1: DATOS BÁSICOS
```markdown
NOMBRE_COMPLETO:      [IAN TRABA ARCE]
NOMBRE:               [IAN]
APELLIDO:             [TRABA]
DORSAL:               [62]
FECHA_NACIMIENTO:     [11/02/2005]
NACIONALIDAD:         [Española]
CIUDAD:               [Bilbao]
CATEGORIA:            [GP3]
EQUIPO:               [Basque Riders]
```

### SECCIÓN 2: HERO (página inicio)
```markdown
FRASE_HERO:           ["Esto no es un deporte, es mi estilo de vida"]
```

### SECCIÓN 3: STATS (estadísticas)
```markdown
STAT_TITULOS_NUM:     [4]
STAT_ANOS_NUM:        [5]
STAT_PODIUMS_NUM:     [18]
STAT_CARRERAS_NUM:    [20+]
STAT_MEDALLAS_NUM:    [10+]
```

### SECCIÓN 4: HISTORIA (5 bloques)
```markdown
ORIGEN_TITULO:        [ej: "EL ORIGEN"]
ORIGEN_TEXTO:         [Empece en 2020 cuando me animo mi padre a comenzar en este deporte , Lo llevo viviendo desde pequeño con mi padre que siempre ha tenido motos de agua, y fue el quien me animo.]

PROBLEMA_TITULO:      [ej: "EL PROBLEMA"]
PROBLEMA_TEXTO:       [La lesion en la que sigo aunque ya estoy en la recta final, han sido meses complicados en los que te desmoralizas, pero siempre hay que tirar para adelante]

APOYO_TITULO:         [ej: "EL APOYO"]
APOYO_TEXTO:          [Mi padre siempre el que mas me anima y mas me ayuda en ese sentido para que no me venga abajo nunca]

SUPERACION_TITULO:    [ej: "LA SUPERACIÓN"]
SUPERACION_TEXTO:     [Estoy en ello, pero se que volvere mas fuerte y entrenare mucho para estar al máximo nivel]

PROMESA_TITULO:       [ej: "MI PROMESA"]
PROMESA_TEXTO:       [Porque veo que se me da bien y me gusta, es lo que me hace feliz]
```

### SECCIÓN 5: PALMARÉS (tantos años como quieras)
```markdown
# Formato: ANYO_X: [año]
#           TITULO_X_Y: [título de ese año]

ANYO_1:               [2025]
TITULO_1_1:           [🏆 Campeón del Mundo]
TITULO_1_3:           [🥇 Campeón España RALLYJET Y OFFSHORE]
TITULO_1_4:           [🥇 Campeón Euskadi]

ANYO_2:               [2024]
TITULO_2_1:           [🥇 Campeón España]
TITULO_2_2:           [🥇 Campeón Euskadi]

ANYO_3:               [2023]
TITULO_3_1:           [🥇 Campeón España]
TITULO_3_2:           [🥇 Campeón Europeo]
```

### SECCIÓN 6: FOTOS (no cambiar nombres de archivos)
```markdown
# Cubrir las que tengas, dejar vacías las que no
FOTO_HERO:            [hero.jpg]
FOTO_PROFILE:         [profile.jpg]
FOTOS_PODIUMS:        [podium1.jpg, podium2.jpg, ... hasta 9]
FOTOS_GALERIA:        [galeria1.jpg, galeria2.jpg, ... hasta 10]
```

### SECCIÓN 7: CONTACTO
```markdown
EMAIL:                [trabaian62@gmail.com]
INSTAGRAM:           [@iantraba_62]
TELEFONO_WHATSAPP:   [34647325346]
MENSAJE_WHATSAPP:    [hola Ian , vi tu pagina deportiva y quiero apoyarte. Cuantame como puedo unirme al equipo.]
```

### SECCIÓN 8: COLORES (opcional)
```markdown
COLOR_NEON:          [azul]
COLOR_NEON_DARK:     [texto negro]
COLOR_NEON_LIGHT:    [fondo blanco donde no haya foto]
```

---

## ✅ CHECKLIST FINAL

- [ ] Todos los campos de DATOS-PILOTO.md rellenados
- [ ] Fotos copiadas a web/images/
- [ ] Archivo BUILD.sh ejecutado
- [ ] Web probada localmente
- [ ] Deploy en Vercel completado
- [ ] URL compartida al cliente

---

## 📝 NOTAS TÉCNICAS

- Máximo 9 fotos de podiums
- Máximo 10 fotos de galería
- Palmarés: años ilimitados, 1-4 títulos por año
- Colores: si no se especifican, usa azul neón (#00d4ff)
- WhatsApp: el número debe tener formato 34XXXXXXXXX
