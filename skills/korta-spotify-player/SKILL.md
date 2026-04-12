---
name: spotify-player
description: Terminal Spotify playback/search via spogo (preferred) or spotify_player. Optimizado para control rápido sin UI.
---

# SPOTIFY-PLAYER — Elite Terminal Control

## Preferred: spogo

### Playback
```bash
spogo play
spogo pause
spogo next
spogo previous
spogo shuffle
spogo repeat
```

### Volume
```bash
spogo volume 80
spogo volume +10
spogo volume -10
spogo mute
```

### Search & Play
```bash
spogo search "song name"
spogo play artist "artist name"
spogo play album "album name"
spogo play playlist "playlist name"
```

### Queue
```bash
spogo queue add "song"
spogo queue list
spogo queue clear
spogo queue shuffle
```

### Status
```bash
spogo status
spogo current
spogo devices
```

## Fallback: spotify_player CLI
```bash
spotify_player pull
spotify_player push
spotify_player toggle
spotify_player next
spotify_player previous
```

## Tips
- spogo es más rápido y con menos dependencias
- Requiere Spotify premium para control remoto
- Verificar que spogo está instalado: `which spogo`