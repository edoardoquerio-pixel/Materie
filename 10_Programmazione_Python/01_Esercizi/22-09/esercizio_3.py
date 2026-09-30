"""
Autore: Edoardo Querio Gianetto
Data: 22/09/2026

Titolo: Primo esercizio sulle liste
Scrivere un programma python che rimuova gli elementi duplicati da una lista.
Esempio:
listaIN = [2, -4, 5, 6, 5, 5, 2]
listaOUT = [2, -4, 5, 6]
"""

##
## Funzioni:

# Funzione: rimuovi_duplicati
#     Descrizione: rimuove i duplicati mantenendo l'ordine degli elementi.
#     Parametri formali: lista, la lista da elaborare.
#     Valore di ritorno: una nuova lista senza duplicati.
def rimuovi_duplicati(lista):
    listaOUT = [] # Lista degli elementi senza duplicati.
    for elemento in lista:
        if elemento not in listaOUT:
            listaOUT.append(elemento)
    return listaOUT

"""
Programma principale
Rimuove gli elementi duplicati da una lista e stampa la lista ottenuta.
"""

# Sezione di input dati

# Inizializzazioni variabili
listaIN = [2, -4, 5, 6, 5, 5, 2] # Lista originale con duplicati.

# Elaborazione
listaOUT = rimuovi_duplicati(listaIN)

# Eventuali sotto processi di elaborazione
# Sezione di output
print(listaOUT)
