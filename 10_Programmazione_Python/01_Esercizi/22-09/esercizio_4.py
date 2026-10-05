"""
Autore: Edoardo Querio Gianetto
Data: 22/09/2026

Titolo: Secondo esercizio sulle liste
Scrivere un programma che date due liste stampi "OK" se hanno almeno
un membro comune, altrimenti stampi "KO".
"""

##
## Funzioni:

# Funzione: hanno_elemento_comune
#     Descrizione: verifica se le liste hanno almeno un elemento in comune.
#     Parametri formali: lista1 e lista2, le due liste da confrontare.
#     Valore di ritorno: bool, True se esiste un elemento comune, False altrimenti.
def hanno_elemento_comune(lista1, lista2):
    """
    Verifica se due liste hanno almeno un elemento in comune.

    Parametri formali:
        lista1 (list): prima lista.
        lista2 (list): seconda lista.
    Valore di ritorno:
        bool: True se esiste un elemento comune, False altrimenti.
    """
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False

"""
Programma principale
Confronta due liste e stampa l'esito della ricerca.
"""

   # Sezione di input dati

# Inizializzazioni variabili
lista1 = [1, 5, 8] # Prima lista da confrontare.
lista2 = [3, 1, 10] # Seconda lista da confrontare.

   # Elaborazione
in_comune = hanno_elemento_comune(lista1, lista2) # Esito della ricerca.

   # Eventuali sotto processi di elaborazione
# Sezione di output
if in_comune:
    print("OK")
else:
    print("KO")
