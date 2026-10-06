"""
Autore: Edoardo Querio Gianetto
Data: 05/10/2026

Titolo: Terzo esercizio sui dizionari
Ottenere il valore massimo e minimo in un dizionario.
Analisi: input = dizionario con valori numerici; output = massimo e minimo.
"""

##
## Funzioni:
##

def trova_massimo_minimo(dizionario: dict) -> tuple:
    """
    Funzione: trova_massimo_minimo
        Confronta i valori del dizionario per trovare i due estremi.
    Parametri formali:
        dizionario (dict): dizionario con valori numerici confrontabili.
    Valore di ritorno:
        tuple: (massimo, minimo); (None, None) se il dizionario e' vuoto.
    """
    massimo = None  # Maggiore valore incontrato.
    minimo = None  # Minore valore incontrato.
    for chiave in dizionario:
        valore = dizionario[chiave]  # Valore corrente da confrontare.
        if massimo is None or valore > massimo:
            massimo = valore
        if minimo is None or valore < minimo:
            minimo = valore
    return massimo, minimo


"""
Programma principale
Calcola e stampa massimo e minimo dei valori di un dizionario.
"""
if __name__ == "__main__":
    # Sezione di input dati
    dizionario = {'a': 12, 'b': -3, 'c': 25, 'd': 7}  # Dati da esaminare.

    # Inizializzazioni variabili
    massimo = None  # Valore massimo del dizionario.
    minimo = None  # Valore minimo del dizionario.

    # Elaborazione
    massimo, minimo = trova_massimo_minimo(dizionario)

    # Sezione di output
    print("Dizionario:", dizionario)
    if massimo is None:
        print("Il dizionario e' vuoto: massimo e minimo non esistono.")
    else:
        print("Massimo:", massimo)
        print("Minimo:", minimo)
