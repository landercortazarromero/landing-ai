# 🌊 PLANTILLA COMPLETA - WEB DE PILOTO

**Versión:** 1.0  
**Fecha:** 2026-04-06  
**Referencia base:** cortazar59.com  
**Estado:** ✅ Plantilla oficial de Hybrid Labs

---

## 📋 SECCIÓN 1: INICIO (HERO)

### 1.1 Datos del Piloto
| Campo | Variable | Ejemplo |
|-------|----------|---------|
| NOMBRE | `{{NOMBRE}}` | IAN |
| APELLIDOS | `{{APELLIDOS}}` | TRABA ARCE |
| DORSAL | `{{DORSAL}}` | 62 |

### 1.2 Badge/Categoría
| Campo | Variable | Ejemplo |
|-------|----------|---------|
| CATEGORÍA | `{{CATEGORIA}}` | Runabout GP3 |
| EQUIPO | `{{EQUIPO}}` | Basque Riders |

### 1.3 Frase Hero
| Campo | Variable |
|-------|----------|
| FRASE | `{{FRASE_HERO}}` |

### 1.4 Botones Hero
| Botón | Texto | URL |
|-------|-------|-----|
| 1 | Ver Palmarés | #palmares |
| 2 | Contactar | #contacto |

### 1.5 Imagen Hero
| Campo | Archivo | Descripción |
|-------|---------|-------------|
| hero.jpg | `{{HERO_IMAGE}}` | Foto acción en moto, horizontal |

---

## 📊 SECCIÓN 2: STATS BAR
| Stat | Variable | Label |
|------|----------|-------|
| TÍTULOS | `{{STAT_TITULOS}}` | Títulos |
| AÑOS EXP. | `{{STAT_ANOS}}` | Años de Experiencia |
| CARRERAS NAC. | `{{STAT_NAC}}` | carreras nacionales |
| CARRERAS EUR. | `{{STAT_EUR}}` | carreras europeas |
| CARRERAS MUND. | `{{STAT_MUND}}` | carreras mundiales |

---

## 👤 SECCIÓN 3: SOBRE MÍ

### 3.1 Foto de Perfil
| Campo | Archivo | Descripción |
|-------|---------|-------------|
| profile.jpg | `{{PROFILE_IMAGE}}` | Foto mirando a cámara |

### 3.2 Historia - 5 Secciones
| # | Título | Variable | Contenido |
|---|--------|----------|-----------|
| 1 | EL ORIGEN | `{{HISTORIA_1}}` | La historia de cómo empezó |
| 2 | EL RETO | `{{HISTORIA_2}}` | El desafío que enfrentó |
| 3 | EL APOYO | `{{HISTORIA_3}}` | Quién le ayudó |
| 4 | LA SUPERACIÓN | `{{HISTORIA_4}}` | Cómo superó obstáculos |
| 5 | MI PROMESA | `{{HISTORIA_5}}` | Compromiso con patrocinadores |

### 3.3 Info Personal
| Campo | Variable |
|-------|----------|
| Nacionalidad | `{{NACIONALIDAD}}` |
| Fecha nacimiento | `{{FECHA_NAC}}` |
| Categoría | `{{CATEGORIA}}` |
| Equipo | `{{EQUIPO}}` |

---

## 🏆 SECCIÓN 4: PALMARÉS

**Formato Timeline:**
```
AÑO:
├── Título del logro
│ └── Competición
```

**Ejemplo:**
```
2025:
├── Campeón España Offshore GP2
│ └── Campeonato de España
├── Campeón Europeo
│ └── Europeo Offshore
```

**Variables dinámicas:**
| Variable | Descripción |
|----------|-------------|
| `{{PALMARES_YEAR_1}}` | Año |
| `{{PALMARES_TITLE_1}}` | Título del logro |
| `{{PALMARES_COMPETICION_1}}` | Competición |

---

## 📸 SECCIÓN 5: PODIUMS
| # | Archivo | Variable pie |
|---|---------|-------------|
| 1 | podium1.jpg | `{{PODIUM_1}}` |
| 2 | podium2.jpg | `{{PODIUM_2}}` |
| 3 | podium3.jpg | `{{PODIUM_3}}` |
| 4 | podium4.jpg | `{{PODIUM_4}}` |
| 5 | podium5.jpg | `{{PODIUM_5}}` |
| 6 | podium6.jpg | `{{PODIUM_6}}` |
| 7 | podium7.jpg | `{{PODIUM_7}}` |
| 8 | podium8.jpg | `{{PODIUM_8}}` |
| 9 | podium9.jpg | `{{PODIUM_9}}` |
| 10 | podium10.jpg | `{{PODIUM_10}}` |

---

## 🖼️ SECCIÓN 6: GALERÍA
| # | Archivo | Variable |
|---|---------|----------|
| 1 | galeria1.jpg | `{{GALERIA_1}}` |
| 2 | galeria2.jpg | `{{GALERIA_2}}` |
| 3 | galeria3.jpg | `{{GALERIA_3}}` |
| 4 | galeria4.jpg | `{{GALERIA_4}}` |
| 5 | galeria5.jpg | `{{GALERIA_5}}` |
| 6 | galeria6.jpg | `{{GALERIA_6}}` |
| 7 | galeria7.jpg | `{{GALERIA_7}}` |
| 8 | galeria8.jpg | `{{GALERIA_8}}` |
| 9 | galeria9.jpg | `{{GALERIA_9}}` |
| 10 | galeria10.jpg | `{{GALERIA_10}}` |
| 11 | galeria11.jpg | `{{GALERIA_11}}` |

---

## 📧 SECCIÓN 7: CONTACTO
| Campo | Variable |
|-------|----------|
| Email | `{{EMAIL}}` |
| Instagram | `{{INSTAGRAM}}` |
| WhatsApp | `{{WHATSAPP}}` |
| Ubicación | `{{UBICACION}}` |

---

## 🎨 DISEÑO - CONSTANTES

### Colores
| Variable | Valor | Uso |
|----------|-------|-----|
| --neon | #e5ff00 | Color principal (amarillo flúor) |
| --black | #000000 | Fondo |
| --dark | #0a0a0a | Secciones alternas |
| --light | #ffffff | Texto principal |

### Fuentes
| Tipo | Fuente |
|------|--------|
| Títulos | Orbitron (900 weight) |
| Cuerpo | Rajdhani (400-700) |

### Animaciones
- slideUp: Entrada de elementos
- neonPulse: Efecto neón en número dorsal
- float: Badge flotante
- fadeIn: Fade in general

---

## 📁 ESTRUCTURA DE ARCHIVOS

```
clients/{{CLIENT_ID}}/web/
├── index.html          # Web completa
├── netlify.toml        # Config deploy
├── assets/
│   └── images/
│       ├── hero/       # hero.jpg
│       ├── perfil/     # profile.jpg
│       ├── podiums/    # podium1-10.jpg
│       └── galeria/    # galeria1-11.jpg
└── ESTADO.md          # Estado del proyecto
```

---

## 🚀 DEPLOY

**Netlify:** `netlify deploy --prod`  
**Vercel:** `vercel --prod`

---

*Plantilla oficial Hybrid Labs L2*
