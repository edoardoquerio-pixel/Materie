"""
Autore: Edoardo Querio Gianetto
Data: 26/10/2026

Titolo: Terzo esercizio sul modulo OS
Eseguire un comando del sistema operativo usando il modulo os.
Analisi: input = comando; output = risultato del comando sul terminale.
"""

import os

##
## Funzioni:
##

def esegui_comando(comando: str) -> None:
    """
    Funzione: esegui_comando
        Esegue il comando usando il sistema operativo.
    Parametri formali:
        comando (str): comando da eseguire.
    Valore di ritorno:
        None.
    """
    os.system(comando)


"""
Programma principale
Richiede un comando e lo esegue.
"""
if __name__ == "__main__":
    # Sezione di input dati
    comando = input("Inserisci un comando (es. dir): ")

    # Elaborazione e output
    esegui_comando(comando)
