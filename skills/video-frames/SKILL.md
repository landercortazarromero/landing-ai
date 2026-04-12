---
name: video-frames
description: Extract frames or short clips from videos using ffmpeg. Optimizado para producción de contenido rápido.
---

# VIDEO-FRAMES — Elite Video Extraction

## Quick Commands

### Extract Single Frame
```bash
video-frames extract video.mp4 --timestamp 00:01:30
video-frames extract video.mp4 --time 90
video-frames extract video.mp4 --frame 150
```

### Extract Multiple Frames
```bash
video-frames extract video.mp4 --every 5s --output frames/
video-frames extract video.mp4 --interval 10 --count 20
```

### Create Clip
```bash
video-frames clip video.mp4 --start 00:01:00 --end 00:01:30 --output clip.mp4
video-frames clip video.mp4 --duration 30s --start 00:01:00
```

### Thumbnails Strip
```bash
video-frames thumbnails video.mp4 --count 10 --output strip.jpg
```

## FFmpeg Direct Commands

### Best Quality Frame
```bash
ffmpeg -i video.mp4 -ss 00:01:30 -vframes 1 frame.jpg
```

### Extract Scene Changes
```bash
ffmpeg -i video.mp4 -vf "select='eq(pix_fabs difference\,0)',change" -vsync vfr frames/%03d.jpg
```

### Timelapse
```bash
ffmpeg -i video.mp4 -filter:v "setpts=0.5*PTS" -r 30 timelapse.mp4
```

## Tips
- Usar `-ss` antes de `-i` para seek rápido
- `-q:v 2` para calidad alta en JPEG
- Para Instagram/TikTok: 9:16 crop con `crop=iw:ih*9/16`