#!/bin/bash
# OpenClaw Skills Verification Script
# L7 God Mode Protocol

echo "🔍 Verificando skills de OpenClaw..."
echo "===================================="

# Check if openclaw is available
if ! command -v openclaw &> /dev/null; then
    echo "❌ ERROR: openclaw command not found"
    exit 1
fi

# Get skills list
SKILLS_OUTPUT=$(openclaw skills list 2>/dev/null)

# Count ready skills
READY_COUNT=$(echo "$SKILLS_OUTPUT" | grep -c "✓ ready")
TOTAL_COUNT=$(echo "$SKILLS_OUTPUT" | grep -c "│ ✓\|│ ✗")

echo "✅ Skills listas: $READY_COUNT"
echo "📊 Total skills: $TOTAL_COUNT"

# Check critical skills
echo ""
echo "🔍 Verificando skills críticas:"
echo "--------------------------------"

CRITICAL_SKILLS=("clawhub" "coding-agent" "github" "gh-issues" "skill-creator" "healthcheck" "weather")

for skill in "${CRITICAL_SKILLS[@]}"; do
    if echo "$SKILLS_OUTPUT" | grep -q "│ ✓ ready.*│ $skill │"; then
        echo "✅ $skill"
    else
        echo "⚠️  $skill - No disponible (instalar con: clawhub install $skill)"
    fi
done

echo ""
echo "===================================="
echo "Verificación completada"
