"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Quarto esercizio sui files
Copiare il contenuto di un file di testo in un altro file.
Analisi: input = nome sorgente e destinazione; output = copia del testo.
Suddivisione: lettura del contenuto e scrittura nel file di destinazione.
"""

##
## Funzioni:
##

def copia_file(sorgente: str, destinazione: str) -> None:
    """
    Funzione: copia_file
        Legge il testo e lo scrive nel file di destinazione.
    Parametri formali:
        sorgente (str): nome del file da leggere.
        destinazione (str): nome del file in cui scrivere.
    Valore di ritorno:
        None.
    """
    with open(sorgente, "r", encoding="utf-8") as file:
        contenuto = file.read()  # Testo da copiare.
    with open(destinazione, "w", encoding="utf-8") as file:
        file.write(contenuto)


"""
Programma principale
Richiede i due nomi e copia il testo.
"""
if __name__ == "__main__":
    # Sezione di input dati
    sorgente = input("Nome o percorso del file da copiare: ")
    destinazione = input("Nome o percorso del file di destinazione: ")

    # Elaborazione
    copia_file(sorgente, destinazione)

    # Sezione di output
    print("Copia completata.")
