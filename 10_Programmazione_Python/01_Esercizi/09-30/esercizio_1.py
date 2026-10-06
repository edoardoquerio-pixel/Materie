"""
Autore: Edoardo Querio Gianetto
Data: 30/09/2026

Titolo: Primo esercizio sulle tuple
Scrivere un programma per rimuovere l'n-esimo elemento da una tupla non vuota.
"""

##
## Funzioni:

# Funzione:
#     Descrizione:
#     Parametri formali:
#     Valore di ritorno:

"""
Programma principale
Descrizione sintetica delle funzionalit?: da completare.
"""

# Sezione di input dati


# Inizializzazioni variabili
tuple = (1, 2, 3, 4, 5)
n = 2

# Elaborazione
def rimuovi_elemento(tuple, n):
    """
    Rimuove da una tupla l'elemento all'indice indicato.

    Parametri formali:
        tuple (tuple): tupla da elaborare.
        n (int): indice a partire da zero.
    Valore di ritorno:
        tuple: tupla senza l'elemento scelto. Per un indice non valido,
        stampa un errore e restituisce la tupla originale.
    """
    if 0 <= n < len(tuple):
        return tuple[:n] + tuple[n+1:]
    else:
        print("Indice non valido.")
        return tuple

tupla_rimossa = rimuovi_elemento(tuple, n)

# Eventuali sotto processi di elaborazione
# Sezione di output

print("Tupla originale:", tuple)
print("Tupla con l'elemento rimosso:", tupla_rimossa)