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
trap 'kill -TERM $PID' SIGINT  # Leállítás a Ctrl+C esetén

while true; do
    if ! is_process_running; then
        start_process
    fi

    # Eltároljuk a folyamat PID-ját
    PID=$(pgrep -o -f "$process_name")

    # Várunk, amíg a folyamat befejeződik vagy 30 másodperc eltelik
    timeout 30s wait $PID
done
