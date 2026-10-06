"""
Autore: Edoardo Querio Gianetto
Data: 05/10/2026

Titolo: Quinto esercizio sui dizionari
Creare un dizionario delle occorrenze dei caratteri di una stringa.
Analisi: input = stringa; output = dizionario {carattere: occorrenze}.
Si contano anche gli spazi, distinguendo le maiuscole dalle minuscole.
"""

##
## Funzioni:
##

def conta_occorrenze(stringa: str) -> dict:
    """
    Funzione: conta_occorrenze
        Conta quante volte compare ogni carattere nella stringa.
    Parametri formali:
        stringa (str): testo da esaminare.
    Valore di ritorno:
        dict: caratteri e frequenze; vuoto per una stringa vuota.
    """
    occorrenze = {}  # Conteggi dei caratteri gia' incontrati.
    for carattere in stringa:
        if carattere in occorrenze:
            occorrenze[carattere] += 1
        else:
            occorrenze[carattere] = 1
    return occorrenze


"""
Programma principale
Legge una stringa e stampa le occorrenze dei suoi caratteri.
"""
if __name__ == "__main__":
    # Sezione di input dati
    stringa = input("Inserisci una stringa: ")  # Testo da analizzare.

    # Inizializzazioni variabili
    risultato = {}  # Dizionario delle occorrenze.

    # Elaborazione
    risultato = conta_occorrenze(stringa)

    # Sezione di output
    print("Dizionario:", risultato)
