"""
Autore: Edoardo Querio Gianetto
Data: 26/10/2026

Titolo: Secondo esercizio sul modulo OS
Contare i file con una determinata estensione sotto un percorso.
Analisi: input = percorso ed estensione; output = numero di file trovati.
Si contano i file nel percorso e nelle sue sottodirectory immediate,
fermandosi al primo livello di profondita', come indicato nella consegna.
"""

import os

##
## Funzioni:
##

def conta_file(percorso: str, estensione: str) -> int:
    """
    Funzione: conta_file
        Conta i file con l'estensione richiesta fino al primo livello.
    Parametri formali:
        percorso (str): directory iniziale.
        estensione (str): estensione da cercare, compreso il punto.
    Valore di ritorno:
        int: numero di file trovati.
    """
    contatore = 0  # Numero di file con l'estensione richiesta.
    for nome in os.listdir(percorso):
        elemento = os.path.join(percorso, nome)
        if os.path.isfile(elemento):
            if os.path.splitext(nome)[1] == estensione:
                contatore += 1
        elif os.path.isdir(elemento):
            for nome_file in os.listdir(elemento):
                percorso_file = os.path.join(elemento, nome_file)
                if os.path.isfile(percorso_file):
                    if os.path.splitext(nome_file)[1] == estensione:
                        contatore += 1
    return contatore


"""
Programma principale
Richiede percorso ed estensione e stampa il conteggio.
"""
if __name__ == "__main__":
    # Sezione di input dati
    percorso = input("Inserisci il percorso: ")
    estensione = input("Inserisci l'estensione con il punto (es. .txt): ")

    # Elaborazione
    totale = conta_file(percorso, estensione)

    # Sezione di output
    print("File trovati:", totale)
