---
name: tmux
description: Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output. Optimizado para automatización de CLIs interactivos.
---

# TMUX — Elite Terminal Multiplexer Control

## Session Management
```bash
tmux new-session -s name
tmux attach -t name
tmux kill-session -t name
tmux list-sessions
```

## Sending Keys
```bash
tmux send-keys -t name "command" C-m
tmux send-keys -t name "ls -la" Enter
tmux send-keys -t name C-c  # Ctrl+C
tmux send-keys -t name C-d  # Ctrl+D
```

## Capture Output
```bash
tmux capture-pane -t name -p
tmux capture-pane -t name -p -S -50  #últimas 50 líneas
tmux capture-pane -t name -p > output.txt
```

## Panes
```bash
tmux split-window -h      # split horizontal
tmux split-window -v       # split vertical
tmux select-pane -t name.0 # seleccionar pane
```

## Workflow Automation
```bash
# Automate interactive CLI (e.g., htop)
tmux new-session -d -s mycli 'htop'
sleep 2
tmux send-keys -t mycli 'q' C-m
tmux capture-pane -t mycli -p
tmux kill-session -t mycli
```

## Tips
- `-t` = target session/pane
- `C-m` = Enter key
- `C-c` = Ctrl+C (interrupt)
- Background sessions con `-d`