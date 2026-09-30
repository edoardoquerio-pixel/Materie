"""
Autore: Edoardo Querio Gianetto
Data: 22/09/2026

Titolo: Terzo esercizio sulle liste
Scrivere un programma per trovare il secondo numero più piccolo in una lista.
"""

##
## Funzioni:

# Funzione: secondo_minimo
#     Descrizione: trova il secondo valore minimo distinto senza modificare la lista.
#     Parametri formali: lista, una lista di numeri.
#     Valore di ritorno: il numero trovato, oppure None se i valori distinti sono meno di due.
def secondo_minimo(lista):
    if not lista:
        return None

    minimo = lista[0] # Valore più piccolo incontrato.
    for numero in lista:
        if numero < minimo:
            minimo = numero

    secondo = None # Secondo minimo, inizialmente non ancora trovato.
    for numero in lista:
        if numero > minimo:
            if secondo is None or numero < secondo:
                secondo = numero
    return secondo

"""
Programma principale
Determina e stampa il secondo minimo distinto della lista.
"""

   # Sezione di input dati

# Inizializzazioni variabili
lista = [2, -4, 5, 6, 5, 5, 2] # Numeri da esaminare.

   # Elaborazione
risultato = secondo_minimo(lista) # Secondo minimo o None.

   # Eventuali sotto processi di elaborazione
# Sezione di output
if risultato is None:
    print("Non esiste un secondo minimo: servono almeno due valori distinti.")
else:
    print("Il secondo numero più piccolo è:", risultato)
