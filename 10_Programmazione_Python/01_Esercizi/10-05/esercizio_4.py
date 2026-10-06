"""
Autore: Edoardo Querio Gianetto
Data: 05/10/2026

Titolo: Quarto esercizio sui dizionari
Rimuovere i duplicati da un dizionario.
Analisi: input = dizionario; output = nuovo dizionario senza valori ripetuti.
Le chiavi sono gia' uniche: si interpretano i duplicati come valori uguali,
mantenendo la prima chiave associata a ciascun valore.
"""

##
## Funzioni:
##

def rimuovi_duplicati(dizionario: dict) -> dict:
    """
    Funzione: rimuovi_duplicati
        Copia solo il primo elemento con ciascun valore distinto.
    Parametri formali:
        dizionario (dict): dizionario da esaminare.
    Valore di ritorno:
        dict: nuovo dizionario senza valori duplicati.
    """
    risultato = {}  # Dizionario dei valori gia' incontrati.
    for chiave in dizionario:
        valore = dizionario[chiave]  # Valore corrente da verificare.
        if valore not in risultato.values():
            risultato[chiave] = valore
    return risultato


"""
Programma principale
Rimuove i valori ripetuti e stampa il dizionario ottenuto.
"""
if __name__ == "__main__":
    # Sezione di input dati
    dizionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}  # Dati iniziali.

    # Inizializzazioni variabili
    risultato = {}  # Dizionario senza duplicati.

    # Elaborazione
    risultato = rimuovi_duplicati(dizionario)

    # Sezione di output
    print("Dizionario originale:", dizionario)
    print("Dizionario senza duplicati:", risultato)
