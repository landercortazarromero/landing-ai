#!/bin/bash
# =============================================================================
# TITAN-OS PILOT WEB GENERATOR v1.0
# Anti-Data-Mixing Protocol - L7 God Mode
# =============================================================================
# Usage: ./pilot-generator.sh [NOMBRE] [APELLIDO] [DORSAL] [EMAIL] [COLOR]
# Example: ./pilot-generator.sh Andoni Sanchez 11 piloto@email.com "#ff0055"
# =============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  TITAN-OS PILOT WEB GENERATOR v1.0${NC}"
echo -e "${BLUE}  Anti-Data-Mixing Protocol${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Args
NOMBRE="${1:-}"
APELLIDO="${2:-}"
DORSAL="${3:-}"
EMAIL="${4:-}"
COLOR="${5:-#00ff88}"

# Validation
if [ -z "$NOMBRE" ] || [ -z "$APELLIDO" ] || [ -z "$DORSAL" ]; then
    echo -e "${RED}❌ ERROR: Missing required arguments${NC}"
    echo -e "${YELLOW}Usage: $0 [NOMBRE] [APELLIDO] [DORSAL] [EMAIL] [COLOR]${NC}"
    echo -e "${YELLOW}Example: $0 Andoni Sanchez 11 piloto@email.com \"#ff0055\"${NC}"
    exit 1
fi

# Sanitize inputs (lowercase for IDs, proper for display)
ID_LOWER=$(echo "$NOMBRE-$APELLIDO-$DORSAL" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
DISPLAY_NAME=$(echo "$NOMBRE" | tr '[:lower:]' '[:upper:]')
DISPLAY_APELLIDO=$(echo "$APELLIDO" | tr '[:lower:]' '[:upper:]')

echo -e "${GREEN}✅ Datos recibidos:${NC}"
echo "   Nombre: $DISPLAY_NAME $DISPLAY_APELLIDO"
echo "   Dorsal: $DORSAL"
echo "   Email: ${EMAIL:-N/A}"
echo "   Color: $COLOR"
echo "   ID: $ID_LOWER"
echo ""

# Create client structure
CLIENT_DIR="$HOME/.openclaw/workspace/clients/$ID_LOWER"
TEMPLATE_DIR="$HOME/.openclaw/workspace/clients/MASTER-TEMPLATE/web"
SCRIPT_DIR="$HOME/.openclaw/workspace/scripts"

echo -e "${YELLOW}📁 Creando estructura...${NC}"
mkdir -p "$CLIENT_DIR/assets" "$CLIENT_DIR/web/images"

# Copy template (clean start)
echo -e "${YELLOW}📋 Copiando template base...${NC}"
cp -r "$TEMPLATE_DIR/images/"* "$CLIENT_DIR/web/images/" 2>/dev/null || true
cp "$TEMPLATE_DIR/index.html" "$CLIENT_DIR/web/template.html"

# Generate from template with placeholders
echo -e "${YELLOW}🔧 Generando web con datos del piloto...${NC}"

sed -e "s/{{NOMBRE}}/$DISPLAY_NAME/g" \
    -e "s/{{APELLIDO}}/$DISPLAY_APELLIDO/g" \
    -e "s/{{NOMBRE_LOWER}}/$(echo $NOMBRE | tr '[:upper:]' '[:lower:]')/g" \
    -e "s/{{APELLIDO_LOWER}}/$(echo $APELLIDO | tr '[:upper:]' '[:lower:]')/g" \
    -e "s/{{DORSAL}}/$DORSAL/g" \
    -e "s/{{EMAIL}}/${EMAIL:-N\/A}/g" \
    -e "s/{{COLOR_NEON}}/$COLOR/g" \
    -e "s/{{ID_LOWER}}/$ID_LOWER/g" \
    "$CLIENT_DIR/web/template.html" > "$CLIENT_DIR/web/index.html"

# Remove template source (anti-mixing)
rm "$CLIENT_DIR/web/template.html"

# Add vercel.json
cat > "$CLIENT_DIR/web/vercel.json" << 'EOF'
{
  "version": 2,
  "routes": [
    { "src": "/(.*)", "dest": "/$1" }
  ]
}
EOF

echo -e "${YELLOW}🔍 Verificando Anti-Data-Mixing...${NC}"

# Check for data mixing
MIXING_CHECK=$(grep -iE "ian|iñaki|traba" "$CLIENT_DIR/web/index.html" || true)
if [ -n "$MIXING_CHECK" ]; then
    echo -e "${RED}❌ DATA MIXING DETECTED!${NC}"
    echo "   Found: $MIXING_CHECK"
    echo -e "${RED}   Abortando...${NC}"
    exit 1
fi

# Count placeholders remaining
REMAINING=$(grep -c "{{" "$CLIENT_DIR/web/index.html" || echo "0")
if [ "$REMAINING" -gt 0 ]; then
    echo -e "${YELLOW}⚠️  WARNING: $REMAINING placeholders sin reemplazar${NC}"
fi

echo -e "${GREEN}✅ VERIFICACIÓN PASSED${NC}"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ WEB GENERADA CORRECTAMENTE${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "📂 Ubicación: $CLIENT_DIR/web/"
echo "🌐 URL: https://$ID_LOWER.vercel.app (después de deploy)"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "   1. cd $CLIENT_DIR/web"
echo "   2. ./verify.sh && vercel --yes --prod"
echo "   3. Compartir URL"
echo ""
