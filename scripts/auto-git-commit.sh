#!/bin/bash
# Auto-git-commit script for KORTA
# Runs every hour to commit and push changes

cd ~/.openclaw/workspace

# Check if there are changes
if [[ -n $(git status --porcelain) ]]; then
    git add -A
    git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M') - Session updates"
    echo "✅ Committed at $(date)"
else
    echo "ℹ️ No changes to commit at $(date)"
fi

# Try to push if remote exists
if git remote get-url origin &>/dev/null; then
    git push
    echo "✅ Pushed at $(date)"
else
    echo "ℹ️ No remote configured, skipping push"
fi