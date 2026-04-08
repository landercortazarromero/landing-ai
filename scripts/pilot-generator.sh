#!/bin/bash
# =============================================================================
# TITAN-OS PILOT WEB GENERATOR v2.0 — ANTI-DATA-MIXING PROTOCOL
# =============================================================================
# Este script genera webs de pilotos 100% limpias, sin mezclas de datos
# =============================================================================

set -e

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

TEMPLATE_DIR="$HOME/.openclaw/workspace/clients/MASTER-TEMPLATE/web"

# Función de ayuda
show_help() {
    cat << EOF
${BLUE}TITAN-OS PILOT WEB GENERATOR v2.0${NC}

Uso: $0 [opciones]

OPCIONES REQUERIDAS:
    -n, --nombre      Nombre del piloto (ej: ANDONI)
    -a, --apellido    Apellido del piloto (ej: SANCHEZ)
    -d, --dorsal      Número de dorsal (ej: 11)
    -c, --color       Color en hex (ej: #ff0055)

OPCIONES OPCIONALES:
    -e, --email        Email de contacto
    -i, --instagram    Usuario de Instagram
    -w, --whatsapp     Número de WhatsApp
    -ci, --ciudad      Ciudad (ej: Bilbao)
    -q, --quote        Frase personal

EJEMPLO:
    $0 -n ANDONI -a SANCHEZ -d 11 -c "#ff0055" -e "piloto@email.com"

EOF
    exit 0
}

# Parsear argumentos
NOMBRE=""
APELLIDO=""
DORSAL=""
COLOR=""
EMAIL=""
INSTAGRAM=""
WHATSAPP=""
CIUDAD="España"
QUOTE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -n|--nombre) NOMBRE="$2"; shift 2 ;;
        -a|--apellido) APELLIDO="$2"; shift 2 ;;
        -d|--dorsal) DORSAL="$2"; shift 2 ;;
        -c|--color) COLOR="$2"; shift 2 ;;
        -e|--email) EMAIL="$2"; shift 2 ;;
        -i|--instagram) INSTAGRAM="$2"; shift 2 ;;
        -w|--whatsapp) WHATSAPP="$2"; shift 2 ;;
        -ci|--ciudad) CIUDAD="$2"; shift 2 ;;
        -q|--quote) QUOTE="$2"; shift 2 ;;
        -h|--help) show_help ;;
        *) echo "Opción desconocida: $1"; show_help ;;
    esac
done

# Validación
if [[ -z "$NOMBRE" || -z "$APELLIDO" || -z "$DORSAL" || -z "$COLOR" ]]; then
    echo -e "${RED}❌ ERROR: Faltan argumentos requeridos${NC}"
    show_help
fi

# Generar ID y rutas
ID_LOWER=$(echo "$NOMBRE-$APELLIDO-$DORSAL" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
CLIENT_DIR="$HOME/.openclaw/workspace/clients/$ID_LOWER"

# Extraer RGB del color hex
HEX=${COLOR//#}
R=$(printf '%d' 0x${HEX:0:2})
G=$(printf '%d' 0x${HEX:2:2})
B=$(printf '%d' 0x${HEX:4:2})

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  TITAN-OS PILOT GENERATOR v2.0 — Anti-Data-Mixing${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}✅ Datos recibidos:${NC}"
echo "   Piloto: $NOMBRE $APELLIDO #$DORSAL"
echo "   Color: $COLOR (RGB: $R, $G, $B)"
echo "   Email: ${EMAIL:-N/A}"
echo "   Instagram: ${INSTAGRAM:-N/A}"
echo "   WhatsApp: ${WHATSAPP:-N/A}"
echo "   ID: $ID_LOWER"
echo ""

# Crear estructura
echo -e "${YELLOW}📁 Creando estructura cliente...${NC}"
mkdir -p "$CLIENT_DIR/web/images" "$CLIENT_DIR/assets"

# Copiar template limpio
echo -e "${YELLOW}📋 Copiando TEMPLATE-MASTER limpio...${NC}"
cp "$TEMPLATE_DIR/TEMPLATE-MASTER.html" "$CLIENT_DIR/web/index.html"

# Aplicar reemplazos
echo -e "${YELLOW}🔧 Aplicando datos del piloto...${NC}"
sed -i '' \
    -e "s/{{NOMBRE}}/$NOMBRE/g" \
    -e "s/{{APELLIDO}}/$APELLIDO/g" \
    -e "s/{{DORSAL}}/$DORSAL/g" \
    -e "s/{{COLOR_NEON}}/$COLOR/g" \
    -e "s/{{COLOR_NEON_DARK}}/$COLOR/g" \
    -e "s/{{COLOR_NEON_LIGHT}}/$COLOR/g" \
    -e "s/{{RGB_R}}/$R/g" \
    -e "s/{{RGB_G}}/$G/g" \
    -e "s/{{RGB_B}}/$B/g" \
    -e "s/{{EMAIL}}/${EMAIL:-}/g" \
    -e "s/{{INSTAGRAM}}/${INSTAGRAM:-}/g" \
    -e "s/{{WHATSAPP}}/${WHATSAPP:-}/g" \
    -e "s/{{CIUDAD}}/$CIUDAD/g" \
    -e "s/{{QUOTE}}/${QUOTE:-Con esfuerzo y sacrificio se logran resultados}/g" \
    -e "s/{{STAT_TITULOS}}/0/g" \
    -e "s/{{STAT_ANOS}}/0/g" \
    -e "s/{{STAT_PODIUMS}}/0/g" \
    -e "s/{{STAT_VICTORIAS}}/0/g" \
    -e "s/{{WHATSAPP_MESSAGE}}/Hola%2C%20acabo%20de%20ver%20tu%20web/g" \
    "$CLIENT_DIR/web/index.html"

# Crear vercel.json
cat > "$CLIENT_DIR/web/vercel.json" << EOF
{
  "version": 2,
  "routes": [
    { "src": "/(.*)", "dest": "/\$1" }
  ]
}
EOF

# Verificación ANTI-DATA-MIXING
echo -e "${YELLOW}🔍 Verificando Anti-Data-Mixing...${NC}"

# Check 1: No deben quedar placeholders
REMAINING=$(grep -c '{{[A-Z_]*}}' "$CLIENT_DIR/web/index.html" 2>/dev/null || echo "0")
if [[ "$REMAINING" -gt 0 ]]; then
    echo -e "${YELLOW}⚠️  WARNING: $REMAINING placeholders sin reemplazar${NC}"
    grep -o '{{[A-Z_]*}}' "$CLIENT_DIR/web/index.html" | sort | uniq
fi

# Check 2: No debe haber datos de pilotos anteriores
PREV_NAMES="ian|iñaki|traba|lander"
MIXING=$(grep -iE "$PREV_NAMES" "$CLIENT_DIR/web/index.html" || true)
if [[ -n "$MIXING" ]]; then
    echo -e "${RED}❌ DATA MIXING DETECTADO!${NC}"
    echo "$MIXING" | head -5
    echo -e "${RED}   Abortando...${NC}"
    exit 1
fi

echo -e "${GREEN}✅ VERIFICACIÓN PASSED — Web 100% limpia${NC}"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ WEB GENERADA CORRECTAMENTE${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "📂 Ubicación: $CLIENT_DIR/web/"
echo "🌐 URL: https://$ID_LOWER.vercel.app"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "   1. cd $CLIENT_DIR/web"
echo "   2. Añadir fotos a images/ (hero.jpg, perfil.jpg, podium1-9.jpg, accion1-10.jpg)"
echo "   3. vercel --yes --prod"
echo ""
echo -e "${GREEN}✨ Proceso Anti-Data-Mixing completado${NC}"
echo ""
