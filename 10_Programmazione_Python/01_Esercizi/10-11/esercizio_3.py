"""
Autore: Edoardo Querio Gianetto
Data: 12/10/2026

Titolo: Terzo esercizio sulle classi (OOP)
Creare una classe Calcolo per fattoriale, somma e tabelline di numeri interi.
Analisi: input = numero intero; output = fattoriale, somma da 1 a n,
tabellina del numero e tabelline da 1 a 9.
Suddivisione: un metodo per ogni calcolo; allTablesMult richiama tableMult.
Per fattoriale e somma si accettano interi non negativi.
"""

##
## Classi:
##

class Calcolo:
    """Raccoglie operazioni su numeri interi."""

    def __init__(self) -> None:
        """Costruttore senza parametri aggiuntivi o attributi; restituisce None."""
        pass

    def Factorial(self, numero: int) -> int:
        """
        Metodo: Factorial
            Calcola il fattoriale mediante moltiplicazioni successive.
        Parametri formali:
            numero (int): intero non negativo.
        Valore di ritorno:
            int: fattoriale; 1 se numero e' zero.
            Solleva ValueError per numeri negativi.
        """
        if numero < 0:
            raise ValueError("Il fattoriale richiede un intero non negativo.")
        risultato = 1  # Prodotto dei numeri da 1 a numero.
        for valore in range(1, numero + 1):
            risultato *= valore
        return risultato

    def Sum(self, numero: int) -> int:
        """
        Metodo: Sum
            Somma gli interi da 1 fino al numero indicato.
        Parametri formali:
            numero (int): intero non negativo.
        Valore di ritorno:
            int: somma dei primi numero interi; 0 se numero e' zero.
            Solleva ValueError per numeri negativi.
        """
        if numero < 0:
            raise ValueError("La somma richiede un intero non negativo.")
        risultato = 0  # Somma dei valori gia' elaborati.
        for valore in range(1, numero + 1):
            risultato += valore
        return risultato

    def tableMult(self, numero: int) -> None:
        """
        Metodo: tableMult
            Visualizza la tabellina con moltiplicatori da 1 a 10.
        Parametri formali:
            numero (int): numero di cui stampare la tabellina.
        Valore di ritorno:
            None: i prodotti sono stampati a video.
        """
        for moltiplicatore in range(1, 11):
            print(numero, "x", moltiplicatore, "=", numero * moltiplicatore)

    def allTablesMult(self) -> None:
        """
        Metodo: allTablesMult
            Visualizza le tabelline dei numeri da 1 a 9.
        Parametri formali:
            Nessun parametro aggiuntivo.
        Valore di ritorno:
            None: richiama tableMult per stampare ogni tabellina.
        """
        for numero in range(1, 10):
            print("\nTabellina del", numero)
            self.tableMult(numero)


"""
Programma principale
Legge un intero non negativo e prova tutti i metodi della classe Calcolo.
"""
if __name__ == "__main__":
    # Sezione di input dati
    numero = int(input("Inserisci un intero non negativo: "))  # Numero da elaborare.
    while numero < 0:
        numero = int(input("Numero non valido. Inserisci un intero non negativo: "))

    # Inizializzazioni variabili
    calcolo = Calcolo()  # Oggetto per eseguire le operazioni.
    fattoriale = 1  # Risultato del fattoriale.
    somma = 0  # Risultato della somma.

    # Elaborazione
    fattoriale = calcolo.Factorial(numero)
    somma = calcolo.Sum(numero)

    # Sezione di output
    print("Fattoriale:", fattoriale)
    print("Somma dei primi", numero, "interi:", somma)
    print("\nTabellina del", numero)
    calcolo.tableMult(numero)
    print("\nTutte le tabelline da 1 a 9:")
    calcolo.allTablesMult()
