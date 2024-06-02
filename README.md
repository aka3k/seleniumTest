# Selenium Web Scraping Script

Questo repository contiene uno script Python che utilizza Selenium WebDriver per automatizzare la ricerca su Google, aprire il primo risultato della ricerca e estrarre il titolo della pagina e il primo paragrafo. 

## Prerequisiti

Prima di eseguire lo script, assicurati di avere installato Python e `pip` nel tuo sistema. Inoltre, assicurati di avere Google Chrome installato, poiché lo script utilizza il driver di Chrome per l'automazione del browser.

## Installazione delle dipendenze

Per installare le librerie necessarie, esegui il seguente script Python:

```python
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
