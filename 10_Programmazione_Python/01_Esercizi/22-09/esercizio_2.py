"""
Autore: Edoardo Querio Gianetto
Data: 22/09/2026

Titolo: Primo esercizio sulle stringhe
Scrivere un programma che dica se una stringa è palindroma.
Esempio:
str="ABBA" PALINDROMA
str="PIPPO" NON PALINDROMA
"""

##
## Funzioni:
def palindromo(stringa):
    """
    Verifica se una stringa si legge allo stesso modo nei due versi.

    Parametri formali:
        stringa (str): testo da verificare, distinguendo maiuscole e minuscole.
    Valore di ritorno:
        str: messaggio che indica se la stringa risulta palindroma.
    """
    if stringa == stringa[::-1]:
        return ("la stringa è palindroma")
    else:
        return ("la stringa non è palindroma")
# Sezione di input dati
stringa = "abba"

# Elaborazione

# Inizializzazioni variabili

# Eventuali sotto processi di elaborazione
# Sezione di output
print(palindromo(stringa))