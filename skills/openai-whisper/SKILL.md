---
name: openai-whisper
description: Local speech-to-text with the Whisper CLI (no API key needed). Perfect for transcribir audio para contenido GRILLO. INSTALLED via pip.
---

# WHISPER — Transcription CLI (INSTALLED ✅)

## Estado
✅ Instalado: `/Users/landercortazarromero/Library/Python/3.9/bin/whisper`
⚠️ Añadir al PATH: `export PATH="$HOME/Library/Python/3.9/bin:$PATH"`

## Comandos

### Transcribir audio
```bash
whisper audio.mp3 --model base
whisper grabacion.wav --language es --model medium
```

### Modelos disponibles
| Modelo | Velocidad | Precisión |
|--------|-----------|-----------|
| tiny | Muy rápido | Baja |
| base | Rápido | Media |
| small | Medio | Buena |
| medium | Lento | Alta |
| large | Muy lento | Máxima |

### Opciones
```bash
whisper audio.mp3 --model base --language es
whisper audio.mp3 --model small --output txt
whisper audio.mp3 --output_dir ./transcripts
```

## Uso para GRILLO
- Transcribir reels/podcasts
- Extraer texto de vídeos para carruseles
- Documentar contenido de comunidad

## Notes
- Sin API key (offline)
- Modelos descargados a ~/.cache/whisper/
- Requiere Mac con Apple Silicon o Intel