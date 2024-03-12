
# A leállítandó folyamat neve
process_name="bot.py"

# Ellenőrzi, hogy a folyamat fut-e
is_process_running() {
    pgrep -f "$process_name" > /dev/null
}

# Leállítja a folyamatot
stop_process() {
    pkill -f "$process_name"
}

# Ellenőrzi, hogy a folyamat fut, és leállítja
if is_process_running; then
    stop_process
    echo "$process_name leállítva."
else
    echo "$process_name nem fut."
fi
