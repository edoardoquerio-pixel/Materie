"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Settimo esercizio - Operatori e collezioni eterogenee
Analisi: input = numeri complessi, vettori 2D e uno scalare, definiti nel codice.
Output = rappresentazione, somme, prodotti e moduli degli oggetti.
Suddivisione: ogni classe implementa gli operatori e il proprio modulo;
una funzione stampa le operazioni su due oggetti dello stesso tipo.
La forma algebrica scelta e' a + ib, come indicato nella consegna.
"""

from math import sqrt


class NumeroComplesso:
    """Numero con parte reale e parte immaginaria."""

    def __init__(self, parte_reale: float, parte_immaginaria: float) -> None:
        """Riceve parte reale e immaginaria; inizializza gli attributi (None)."""
        self.parte_reale = parte_reale
        self.parte_immaginaria = parte_immaginaria

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce la forma algebrica (str)."""
        if self.parte_immaginaria < 0:
            return f"{self.parte_reale} - i{abs(self.parte_immaginaria)}"
        return f"{self.parte_reale} + i{self.parte_immaginaria}"

    def __add__(self, altro: "NumeroComplesso") -> "NumeroComplesso":
        """Riceve un NumeroComplesso; restituisce un nuovo oggetto con la somma."""
        return NumeroComplesso(self.parte_reale + altro.parte_reale,
                               self.parte_immaginaria + altro.parte_immaginaria)

    def __mul__(self, altro: "NumeroComplesso") -> "NumeroComplesso":
        """Riceve un NumeroComplesso; restituisce un nuovo oggetto con il prodotto."""
        reale = self.parte_reale * altro.parte_reale - self.parte_immaginaria * altro.parte_immaginaria
        immaginaria = self.parte_reale * altro.parte_immaginaria + self.parte_immaginaria * altro.parte_reale
        return NumeroComplesso(reale, immaginaria)

    def modulo(self) -> float:
        """Senza parametri aggiuntivi; restituisce sqrt(a*a + b*b) (float)."""
        return sqrt(self.parte_reale ** 2 + self.parte_immaginaria ** 2)


class Vettore2D:
    """Vettore nel piano con coordinate x e y."""

    def __init__(self, x: float, y: float) -> None:
        """Riceve le coordinate x e y; inizializza gli attributi (None)."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce la coppia (x, y) come str."""
        return f"({self.x}, {self.y})"

    def __add__(self, altro: "Vettore2D") -> "Vettore2D":
        """Riceve un Vettore2D; restituisce un nuovo vettore con la somma."""
        return Vettore2D(self.x + altro.x, self.y + altro.y)

    def __mul__(self, scalare: float) -> "Vettore2D":
        """Riceve uno scalare numerico; restituisce un nuovo vettore moltiplicato."""
        return Vettore2D(self.x * scalare, self.y * scalare)

    def modulo(self) -> float:
        """Senza parametri aggiuntivi; restituisce la lunghezza (float)."""
        return sqrt(self.x ** 2 + self.y ** 2)


##
## Funzioni:
##

def stampa_operazioni(obj1, obj2) -> None:
    """
    Funzione: stampa_operazioni
        Stampa due oggetti, la loro somma e i rispettivi moduli.
    Parametri formali:
        obj1, obj2 (NumeroComplesso o Vettore2D): oggetti dello stesso tipo.
    Valore di ritorno:
        None: i risultati vengono stampati a video.
    """
    print("Primo oggetto:", obj1, "modulo:", obj1.modulo())
    print("Secondo oggetto:", obj2, "modulo:", obj2.modulo())
    print("Somma:", obj1 + obj2)


"""
Programma principale
Prova gli operatori sui due tipi e il modulo in una collezione mista.
"""
if __name__ == "__main__":
    # Input di esempio e inizializzazione degli oggetti.
    complesso1 = NumeroComplesso(3, 4)
    complesso2 = NumeroComplesso(1, -2)
    vettore1 = Vettore2D(5, 12)
    vettore2 = Vettore2D(3, 4)
    scalare = 2  # Fattore per moltiplicare il primo vettore.
    elementi = [complesso1, vettore1, complesso2, vettore2]

    # Elaborazione e output: prova delle somme, dei moduli e dei prodotti.
    print("Numeri complessi:")
    stampa_operazioni(complesso1, complesso2)
    print("Prodotto:", complesso1 * complesso2)
    print("\nVettori:")
    stampa_operazioni(vettore1, vettore2)
    print("Prodotto per", scalare, ":", vettore1 * scalare)

    # Collezione eterogenea: ogni oggetto risponde allo stesso metodo.
    print("\nCollezione mista:")
    for elemento in elementi:
        print("Elemento:", elemento, "modulo:", elemento.modulo())
