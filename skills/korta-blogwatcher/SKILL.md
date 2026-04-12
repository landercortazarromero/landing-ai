---
name: blogwatcher
description: Monitor blogs and RSS/Atom feeds for updates using the blogwatcher CLI. Optimizado para tracking de contenido.
---

# BLOGWATCHER — Elite Feed Monitoring

## Quick Commands

### Add Feed
```bash
blogwatcher add https://example.com/feed
blogwatcher add https://example.com/rss.xml --name "Blog Name"
```

### List Feeds
```bash
blogwatcher list
blogwatcher list --json
```

### Check Updates
```bash
blogwatcher check
blogwatcher check --all
blogwatcher check --feed "Blog Name"
```

### Remove Feed
```bash
blogwatcher remove "Blog Name"
blogwatcher remove --all
```

## Config
```bash
blogwatcher config --set interval 60  # minutos
blogwatcher config --set output json
```

## Usage
Perfecto para tracking de:
- Blogs de competidores
- News feeds
- Updates de productos
- Contenido de industria