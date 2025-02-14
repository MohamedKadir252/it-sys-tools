# Script: Surveillance des ressources système (Python)

import psutil

def system_monitor():
    print("🔍 Surveillance des ressources système")
    print(f"🖥 CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"💾 RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"🖴 Disk Usage: {psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
    system_monitor()