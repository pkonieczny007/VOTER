import subprocess
import time
import sys

def run_command(executable_path):
    print("Uruchamianie komendy...")
    process = subprocess.Popen(executable_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        for line in process.stdout:
            print(f"Output: {line.strip()}")
        for line in process.stderr:
            print(f"Error: {line.strip()}")
    except Exception as e:
        print(f"Wystąpił błąd podczas czytania wyjścia: {e}")
    
    # Czekanie 10 sekund
    time.sleep(10)

    # Zatrzymywanie komendy
    process.terminate()
    try:
        process.wait(timeout=5)
        print("Komenda zatrzymana.")
    except subprocess.TimeoutExpired:
        process.kill()
        print("Komenda została siłowo zatrzymana.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        executable_path = sys.argv[1]
        run_command(executable_path)
    else:
        print("Proszę podać ścieżkę do pliku wykonywalnego jako argument.")
