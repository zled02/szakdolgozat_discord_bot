#!/bin/bash

# A figyelt folyamat neve
process_name="bot.py"

# Ellenőrzi, hogy a folyamat fut-e
is_process_running() {
    pgrep -f "$process_name" > /dev/null
}

# Indítja a folyamatot
start_process() {
    echo "Indítás: $process_name"
    nohup python3 $process_name > /dev/null 2>&1 &
}

# Fő ciklus
trap 'stop_bot' SIGINT  # Leállítás a Ctrl+C esetén

stop_bot() {
    if is_process_running; then
        echo "Leállítás: $process_name"
        pkill -f "$process_name"
    fi
    exit 0
}

while true; do
    if ! is_process_running; then
        start_process
    fi
    sleep 30
done
