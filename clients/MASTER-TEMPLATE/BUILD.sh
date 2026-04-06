#!/bin/bash
# BUILD.sh - Genera web de piloto desde plantilla maestra
# Uso: ./BUILD.sh

set -e

echo "🎯 Generando web del piloto..."

# Ir al directorio del proyecto
cd "$(dirname "$0")"

# Verificar que existe web/index.html
if [ ! -f "web/index.html" ]; then
    echo "❌ Error: No existe web/index.html"
    exit 1
fi

# Cargar datos del piloto
source DATOS-PILOTO.md 2>/dev/null || true

echo "✅ Plantilla lista para procesar"
echo ""
echo "📋 Datos cargados:"
echo "   - Nombre: $NOMBRE $APELLIDO #$DORSAL"
echo "   - Categoría: $CATEGORIA"
echo "   - Equipo: $EQUIPO"
echo ""
echo "⚠️  Para generar la web necesitas ejecutar el script de Python"
echo "   python3 build-web.py"
