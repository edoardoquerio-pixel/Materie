"""
Autore: Edoardo Querio Gianetto
Data: 30/09/2026

Titolo: Terzo esercizio sulle tuple
Scrivere un programma per sostituire l'ultimo valore delle liste in una tupla
con un valore richiesto in input.
Esempio:
valore = 100
TuplaIN = ([10, 20, 40], 'a', [40, 50, 60], 23, [70, 80, 90])
TuplaOUT = ([10, 20, 100], 'a', [40, 50, 100], 23, [70, 80, 100])
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
TUPLE = ([10, 20, 40], 'a', [40, 50, 60], 23, [70, 80, 90])
valore = 100


# Inizializzazioni variabili
print ("Tupla originale:", TUPLE)

# Elaborazione
def sostituisci_ultimo_valore(tupla, valore):
    """
    Sostituisce l'ultimo elemento di ogni lista contenuta nella tupla.

    Parametri formali:
        tupla (tuple): tupla con liste non vuote ed eventuali altri valori.
        valore: nuovo valore da assegnare all'ultimo elemento delle liste.
    Valore di ritorno:
        tuple: tupla con le liste aggiornate e gli altri elementi invariati.
        Le liste vengono modificate anche nella tupla originale.
    Errori:
        IndexError: se una delle liste risulta vuota.
    """
    tupla_modificata = []
    for elemento in tupla:
        if isinstance(elemento, list):
            elemento[-1] = valore
        tupla_modificata.append(elemento)
    return tuple(tupla_modificata)

tupla_modificata = sostituisci_ultimo_valore(TUPLE, valore)

# Eventuali sotto processi di elaborazione
# Sezione di output


print("Valore da sostituire:", valore)
print("Tupla con l'ultimo valore sostituito:", tupla_modificata)