"""
Autore: Edoardo Querio Gianetto
Data: 30/09/2026

Titolo: Quarto esercizio sulle tuple
Scrivere un programma per contare gli elementi in una lista finch?
non si incontra un elemento di tipo tupla.
Suggerimento: si usi la funzione isinstance().
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
list = [1, 2, 3, (4, 5), 6, 7]

# Inizializzazioni variabili
def controlloLista(list):

    if list:
        count = 0
        for elemento in list:
            if isinstance(elemento, tuple):
                break
            count += 1
    return count

# Elaborazione


# Eventuali sotto processi di elaborazione
# Sezione di output
print ("Lista originale:", list)
print ("Numero di elementi prima della tupla:", controlloLista(list))
