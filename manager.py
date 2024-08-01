import subprocess
import time

# Ścieżka do skryptu uruchamiającego komendę
run_script = 'run_command.py'
# Ścieżka do pliku wykonywalnego, który ma być uruchamiany
executable_path = 'target\\release\\voter.exe'
# Maksymalna liczba równocześnie uruchomionych procesów
max_processes = 2
# Lista przechowująca referencje do uruchomionych procesów
processes = []

def start_process(script, executable):
    # Uruchamianie nowego procesu
    return subprocess.Popen(['python', script, executable])

while True:
    # Uruchamianie nowych procesów, jeśli jest mniej niż maksymalna liczba
    while len(processes) < max_processes:
        process = start_process(run_script, executable_path)
        processes.append(process)
        print(f"Uruchomiono proces, ID: {process.pid}")

    # Zatrzymywanie procesów po pewnym czasie
    time.sleep(20)  # Czas działania procesów (ON)
    for process in processes:
        print(f"Zatrzymywanie procesu, ID: {process.pid}")
        process.terminate()
        try:
            process.wait(timeout=5)
            print(f"Proces zatrzymany, ID: {process.pid}")
        except subprocess.TimeoutExpired:
            process.kill()
            print(f"Proces został siłowo zatrzymany, ID: {process.pid}")

    # Usuwanie zakończonych procesów z listy
    processes.clear()

    # Czekanie przed ponownym uruchomieniem procesów (OFF)
    time.sleep(5)
