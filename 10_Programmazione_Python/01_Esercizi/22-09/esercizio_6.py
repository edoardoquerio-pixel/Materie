"""
Autore: Edoardo Querio Gianetto
Data: 22/09/2026

Titolo: Quarto esercizio sulle liste
Dividere una lista in due parti, data la lunghezza della prima parte.
"""

##
## Funzioni:

# Funzione: dividi_lista
#     Descrizione: divide la lista senza modificare quella originale.
#     Parametri formali: lista, la lista originale; lunghezza, un numero intero.
#     Valore di ritorno: una lista contenente le due parti.
#     Errori: ValueError se la lunghezza non è un intero valido.
def dividi_lista(lista, lunghezza):
    if type(lunghezza) is not int or lunghezza < 0 or lunghezza > len(lista):
        return None

    prima_parte = lista[:lunghezza] # Elementi prima del punto di divisione.
    seconda_parte = lista[lunghezza:] # Elementi rimanenti.
    return [prima_parte, seconda_parte]

"""
Programma principale
Divide la lista e stampa separatamente le due parti.
"""

   # Sezione di input dati

# Inizializzazioni variabili
lista = [1, 1, 2, 3, 4, 4, 5, 1] # Lista originale.
lunghezza = 3 # Numero di elementi della prima parte.

   # Elaborazione
parti = dividi_lista(lista, lunghezza)

# Eventuali sotto processi di elaborazione
# Sezione di output
if parti is None:
    print("Errore nell'inserimento dati, verifica la lunghezza.")
else:
    print("Prima parte:", parti[0])
    print("Seconda parte:", parti[1])
