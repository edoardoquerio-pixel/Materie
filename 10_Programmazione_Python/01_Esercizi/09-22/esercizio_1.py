"""
Autore: Edoardo Querio Gianetto
Data: 22/09/2026

Titolo: Primo esercizio sulle stringhe
Scrivere un programma per rimuovere l'n-esimo carattere da una stringa
non vuota. Progettare una funzione che accetti la stringa e la posizione
del carattere e restituisca la stringa modificata.
"""

##
## Funzioni: fun()


##

# Schema di documentazione delle funzioni da completare:
# Funzione:
#     Descrizione:
#     Parametri formali:
#     Valore di ritorno:

"""
Programma principale
Descrizione sintetica delle funzionalità: da completare.
"""

# Sezione di input dati


# Elaborazione
def rimuovi_carattere(parola, n):
    """
    Rimuove il carattere all'indice n della stringa parola.

    Parametri formali:
        parola (str): stringa non vuota.
        n (int): indice a partire da zero.
    Valore di ritorno:
        str: stringa modificata o messaggio di errore per dati non validi.
        Se n coincide con la lunghezza, restituisce la stringa invariata.
    """
    if len(parola) >= n and n >= 0 and parola:
        return parola[:n] + parola[n+1:]
    else:
        return "Errore nell'insermento dati, verifica i parametri."

# Inizializzazioni variabili
parola = "ciao"
n = 1 # Indice dell'elemento.

    
rimuovi_carattere(parola,n)

# Eventuali sotto processi di elaborazione
# Sezione di output
print(rimuovi_carattere(parola,n))