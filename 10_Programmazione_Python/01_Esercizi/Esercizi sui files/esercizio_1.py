"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Primo esercizio sui files
Salvare una stringa su stringa.txt e verificare il salvataggio rileggendola.
Analisi: input = stringa; output = testo riletto e risultato del confronto.
"""

##
## Funzioni:
##

def salva_stringa(stringa: str) -> None:
    """Riceve una stringa; la salva in stringa.txt e restituisce None."""
    with open("stringa.txt", "w", encoding="utf-8") as file:
        file.write(stringa)


def leggi_stringa() -> str:
    """Senza parametri; restituisce il contenuto di stringa.txt (str)."""
    with open("stringa.txt", "r", encoding="utf-8") as file:
        stringa = file.read()
    return stringa


"""
Programma principale
Salva il testo e verifica che il contenuto riletto sia uguale all'originale.
I file vengono aperti nella cartella da cui si esegue il programma.
"""
if __name__ == "__main__":
    # Sezione di input dati
    stringa = input("Inserisci una stringa: ")

    # Elaborazione
    salva_stringa(stringa)
    contenuto = leggi_stringa()  # Stringa riletta dal file.

    # Sezione di output
    print("Testo riletto:", contenuto)
    print("Salvataggio verificato:", contenuto == stringa)
