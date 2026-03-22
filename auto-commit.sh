#!/bin/bash
# Auto-commit script for ELITE JSR web
# Run this after every change

cd ~/.openclaw/workspace

# Check if there are changes
if git diff --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Add all changes
git add -A

# Commit with timestamp
git commit -m "ELITE JSR update: $(date '+%Y-%m-%d %H:%M')"

echo "✅ Changes saved at $(date)"
