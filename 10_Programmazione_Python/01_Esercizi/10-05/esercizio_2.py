"""
Autore: Edoardo Querio Gianetto
Data: 05/10/2026

Titolo: Secondo esercizio sui dizionari
Generare e stampare un dizionario nella forma {x: x*x}, da 1 a n.
Analisi: input = intero n; output = dizionario dei quadrati.
"""

##
## Funzioni:
##

def genera_quadrati(n: int) -> dict:
    """
    Funzione: genera_quadrati
        Associa ogni numero da 1 a n al suo quadrato.
    Parametri formali:
        n (int): limite superiore dell'intervallo.
    Valore di ritorno:
        dict: numeri e quadrati; vuoto se n e' minore o uguale a zero.
    """
    quadrati = {}  # Dizionario dei numeri e dei rispettivi quadrati.
    for numero in range(1, n + 1):
        quadrati[numero] = numero * numero
    return quadrati


"""
Programma principale
Legge un intero e stampa il dizionario dei quadrati.
"""
if __name__ == "__main__":
    # Sezione di input dati
    n = int(input("Inserisci un numero intero n: "))  # Limite superiore.

    # Inizializzazioni variabili
    risultato = {}  # Dizionario dei quadrati.

    # Elaborazione
    risultato = genera_quadrati(n)

    # Sezione di output
    print("Dizionario:", risultato)
