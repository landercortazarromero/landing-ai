# 🌊 ELITE JSR - PLANTILLA MAESTRA

Plantilla para crear webs de pilotos de Jet Ski profesionales.

---

## 📋 PROCESO

### 1. Recibir formulario del piloto
Pide al piloto que llene `FORMULARIO-PILOTO.md` y envíe las fotos.

### 2. Crear proyecto
```bash
cd ~/.openclaw/workspace/clients
mkdir NUEVO-PILOTO
cd NUEVO-PILOTO/web
# Copiar todo de MASTER-TEMPLATE/web/
```

### 3. Actualizar datos
Edita `index.html` sustituyendo:

| Campo | Buscar | Reemplazar por |
|-------|--------|----------------|
| Nombre | LANDER | NOMBRE |
| Apellidos | CORTÁZAR | APELLIDOS |
| Dorsal | 59 | NÚMERO |
| Email | cortazar59web@gmail.com | email@piloto.com |
| Instagram | @cortazar_59 | @usuario |
| WhatsApp | 34686087467 | +34600000000 |
| Frase Hero | "Toda victoria..." | "FRASE" |

### 4. Añadir fotos
```
web/assets/images/
├── hero.jpg      (fondo Hero)
├── profile.jpg   (foto Perfil)
├── moto.jpg      (foto Moto)
├── podiums/      (fotos Podiums)
└── galeria/      (fotos Galería)
```

### 5. Desplegar
```bash
cd web
vercel --prod
```

---

## 📁 ESTRUCTURA

```
MASTER-TEMPLATE/
├── index.html           # Plantilla base
├── FORMULARIO-PILOTO.md # Formulario datos
├── clone-pilot.py       # Script automatización
└── README.md           # Este archivo
```

---

## 🎨 PERSONALIZACIÓN

### Colores (en index.html línea ~25)
```css
--neon: #e5ff00;        /* Color principal neón */
--neon-dark: #b8cc00;   /* Oscuro */
--neon-light: #f0ff66; /* Claro */
```

### Cambiar a otro color neón:
- Azul: `#00d4ff`
- Verde: `#00ff88`
- Rosa: `#ff00ff`
- Rojo: `#ff3366`

---

## 📞 DATOS DE CONTACTO

- **Email:** EliteJSR@elite-jsr.com
- **WhatsApp:** +34 686 08 74 67
- **Web:** elite-jsr.vercel.app
