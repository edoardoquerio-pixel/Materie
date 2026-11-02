"""
Autore: Edoardo Querio Gianetto
Data: 26/10/2026

Titolo: Quarto esercizio sul modulo OS
Eliminare i file il cui nome contiene una sequenza di caratteri.
Analisi: input = percorso e sequenza; output = eliminazione dei file trovati.
Si esaminano solo i file direttamente presenti nel percorso indicato.
"""

import os

##
## Funzioni:
##

def elimina_file(percorso: str, sequenza: str) -> None:
    """
    Funzione: elimina_file
        Elimina i file che contengono la sequenza nel nome.
    Parametri formali:
        percorso (str): directory da esaminare.
        sequenza (str): caratteri da cercare nel nome dei file.
    Valore di ritorno:
        None: stampa il nome di ogni file eliminato.
    """
    for nome in os.listdir(percorso):
        percorso_file = os.path.join(percorso, nome)
        if os.path.isfile(percorso_file) and sequenza in nome:
            os.remove(percorso_file)
            print("File eliminato:", nome)


"""
Programma principale
Richiede il percorso e una sequenza non vuota, poi elimina i file corrispondenti.
"""
if __name__ == "__main__":
    # Sezione di input dati
    percorso = input("Inserisci il percorso: ")
    sequenza = input("Inserisci la sequenza da cercare nei nomi: ")
    while sequenza == "":
        sequenza = input("Inserisci una sequenza non vuota: ")

    # Elaborazione e output
    elimina_file(percorso, sequenza)
