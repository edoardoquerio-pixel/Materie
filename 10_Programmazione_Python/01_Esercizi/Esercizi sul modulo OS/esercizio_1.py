"""
Autore: Edoardo Querio Gianetto
Data: 26/10/2026

Titolo: Primo esercizio sul modulo OS
Elencare tutte le directory presenti in un percorso.
Analisi: input = percorso; output = nomi delle directory presenti.
Si esamina solo il contenuto diretto del percorso indicato.
"""

import os

##
## Funzioni:
##

def elenca_directory(percorso: str) -> None:
    """
    Funzione: elenca_directory
        Stampa i nomi delle directory presenti nel percorso.
    Parametri formali:
        percorso (str): directory da esaminare.
    Valore di ritorno:
        None.
    """
    for nome in os.listdir(percorso):
        percorso_elemento = os.path.join(percorso, nome)  # Percorso completo.
        if os.path.isdir(percorso_elemento):
            print(nome)


"""
Programma principale
Richiede un percorso e ne elenca le directory.
"""
if __name__ == "__main__":
    # Sezione di input dati
    percorso = input("Inserisci il percorso: ")

    # Elaborazione e output
    elenca_directory(percorso)
