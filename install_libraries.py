import subprocess
import sys

# Lista delle librerie da installare
required_libraries = [
    'selenium',
    'webdriver-manager'
]

# Funzione per installare una libreria
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Installa tutte le librerie richieste
for library in required_libraries:
    install(library)

print("Tutte le librerie sono state installate correttamente.")
