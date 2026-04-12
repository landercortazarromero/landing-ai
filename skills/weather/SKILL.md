---
name: weather
description: Get current weather and forecasts via wttr.in or Open-Meteo. Optimizado para respuestas rápidas y precisas. Use when: user asks about weather, temperature, or forecasts for any location.
---

# WEATHER — Elite Weather Intelligence

## Quick Query
```
wttr.in/Madrid
wttr.in/Bilbao?lang=es
wttr.in/Barcelona?format=j1
```

## Formatos

### Sin formato (default)
```bash
curl wttr.in/Madrid
```

### Formato JSON
```bash
curl wttr.in/Madrid?format=j1
```

### Próximos 3 días
```bash
curl wttr.in/Madrid?format=3
```

## Locations específicas

### Con emoji
```bash
curl wttr.in/~Eiffel%20Tower
```

### Lat/Lon
```bash
curl wttr.in/:55.75,37.62
```

## Open-Meteo (más preciso)
```bash
curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"
```

## Output parsing con jq
```bash
curl wttr.in/Madrid?format=j1 | jq '.current_condition[0].temp_C'
curl wttr.in/Madrid?format=j1 | jq '.weather[0].hourly[4].chanceofrain'
```

## Casos de Uso

### Tiempo actual
```bash
curl wttr.in/Madrid
```

### Forecast 3 días
```bash
curl wttr.in/Madrid?format=3
```

### Amanecer/atardecer
```bash
curl wttr.in/Madrid?format=j1 | jq '.weather[0].astronomy[0]'
```

## Notas
- wttr.in usa datos de NOAA
- Open-Meteo es más preciso para Europa
- Ambos gratis, sin API key