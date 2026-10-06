"""
Autore: Edoardo Querio Gianetto
Data: 05/10/2026

Titolo: Primo esercizio sui dizionari
Unire un numero indefinito di dizionari mediante una funzione.
Analisi: input = dizionari; output = un nuovo dizionario con tutti gli elementi.
In caso di chiavi uguali, viene mantenuto il valore dell'ultimo dizionario.
"""

##
## Funzioni:
##

def concatena_dizionari(*dizionari: dict) -> dict:
    """
    Funzione: concatena_dizionari
        Copia gli elementi dei dizionari in un nuovo dizionario.
    Parametri formali:
        dizionari (tuple): numero variabile di dizionari da unire.
    Valore di ritorno:
        dict: dizionario risultante; vuoto se non si passano parametri.
    """
    risultato = {}  # Dizionario che raccoglie tutti gli elementi.
    for dizionario in dizionari:
        for chiave in dizionario:
            risultato[chiave] = dizionario[chiave]
    return risultato


"""
Programma principale
Unisce tre dizionari e stampa il risultato.
"""
if __name__ == "__main__":
    # Sezione di input dati
    diz1 = {'v1': 1, 'v2': 2, 'v3': 3}  # Primo dizionario.
    diz2 = {'v4': 4, 'v5': 5, 'v6': 6}  # Secondo dizionario.
    diz3 = {'v7': 7, 'v8': 8}  # Terzo dizionario.

    # Inizializzazioni variabili
    risultato = {}  # Dizionario risultante dalla concatenazione.

    # Elaborazione
    risultato = concatena_dizionari(diz1, diz2, diz3)

    # Sezione di output
    print("Dizionario concatenato:", risultato)
