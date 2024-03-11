import psutil
import subprocess
import time

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False

def start_process(process_name):
    try:
        subprocess.Popen(['python3', process_name])
        print(f"{process_name} indítva!")
    except Exception as e:
        print(f"Hiba történt a folyamat indítása közben: {e}")

def main():
    process_name = "main.py"
    interval_minutes = 5

    while True:
        if not is_process_running(process_name):
            start_process(process_name)

        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    main()
