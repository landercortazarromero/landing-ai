---
name: summarize
description: Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube). Optimizado para extracción rápida de información.
---

# SUMMARIZE — Elite Content Summarization

## Quick Commands

### URLs / Web
```bash
summarize https://example.com/article
summarize https://example.com/article --format markdown
summarize https://example.com/article --length short|medium|long
```

### PDFs
```bash
summarize document.pdf
summarize document.pdf --pages 1-5
summarize document.pdf --format text
```

### Images
```bash
summarize image.jpg
summarize screenshot.png --describe
```

### YouTube
```bash
summarize https://youtube.com/watch?v=VIDEO_ID
summarize https://youtube.com/watch?v=VIDEO_ID --timestamps
```

### Audio
```bash
summarize audio.mp3
summarize podcast.wav --format text
```

## Format Options
```bash
--format markdown|json|text
--length 1-5  # párrafos/resúmenes
--language es|en
```

## Tips
- Perfecto para research rápido
- YouTube: resume vídeos largos en segundos
- PDFs: extrae texto sin leer entero
- Imágenes: describe visual content