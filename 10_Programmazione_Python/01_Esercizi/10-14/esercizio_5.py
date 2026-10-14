"""
Autore: Edoardo Querio Gianetto
Data: 14/10/2026

Titolo: Quinto esercizio - AritmeticaDue e AritmeticaTre
Analisi: input = due o tre operandi e un altro oggetto per il confronto.
Output = differenza, prodotto, confronto tra prodotti e somma di tre operandi.
Suddivisione: un metodo per operazione; AritmeticaTre eredita da AritmeticaDue.
La differenza di tre operandi e' operando1 - operando2 - operando3.
Il confronto restituisce False anche quando i prodotti sono uguali.
"""


class AritmeticaDue:
    """Esegue operazioni con due operandi."""

    def __init__(self, operando1: float = 0, operando2: float = 0) -> None:
        """Riceve due numeri, predefiniti a zero; inizializza gli attributi (None)."""
        self.operando1 = operando1
        self.operando2 = operando2

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce i due operandi (str)."""
        return f"Operando 1: {self.operando1}, operando 2: {self.operando2}"

    def differenza(self) -> float:
        """Senza parametri aggiuntivi; restituisce operando1 - operando2 (float)."""
        return self.operando1 - self.operando2

    def prodotto(self) -> float:
        """Senza parametri aggiuntivi; restituisce il prodotto degli operandi (float)."""
        return self.operando1 * self.operando2

    def confronto(self, altro: "AritmeticaDue") -> bool:
        """Riceve un AritmeticaDue; restituisce True se il proprio prodotto e' maggiore."""
        return self.prodotto() > altro.prodotto()


class AritmeticaTre(AritmeticaDue):
    """Estende le operazioni a tre operandi."""

    def __init__(self, operando1: float = 0, operando2: float = 0,
                 operando3: float = 0) -> None:
        """Riceve tre numeri, predefiniti a zero; inizializza gli attributi (None)."""
        super().__init__(operando1, operando2)
        self.operando3 = operando3

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce tutti e tre gli operandi (str)."""
        return f"{super().__str__()}, operando 3: {self.operando3}"

    def differenza(self) -> float:
        """Senza parametri aggiuntivi; sottrae il secondo e il terzo al primo (float)."""
        return super().differenza() - self.operando3

    def prodotto(self) -> float:
        """Senza parametri aggiuntivi; restituisce il prodotto dei tre operandi (float)."""
        return super().prodotto() * self.operando3

    def confronto(self, altro: AritmeticaDue) -> bool:
        """Riceve un oggetto aritmetico; confronta i prodotti restituendo un bool."""
        return self.prodotto() > altro.prodotto()

    def somma(self) -> float:
        """Senza parametri aggiuntivi; restituisce la somma dei tre operandi (float)."""
        return self.operando1 + self.operando2 + self.operando3


if __name__ == "__main__":
    # Input di esempio e inizializzazione degli oggetti da confrontare.
    primo = AritmeticaDue(10, 3)  # Prodotto 30.
    secondo = AritmeticaDue(4, 5)  # Prodotto 20.
    terzo = AritmeticaTre(10, 3, 2)  # Prodotto 60.
    quarto = AritmeticaTre(4, 5, 3)  # Prodotto 60: caso di uguaglianza.
    predefinito = AritmeticaDue()  # Prova dei valori predefiniti.
    tre_predefiniti = AritmeticaTre()  # Tre operandi uguali a zero.

    # Elaborazione e output: prova di tutti i metodi delle due classi.
    print(primo)
    print("Differenza:", primo.differenza())
    print("Prodotto:", primo.prodotto())
    print("Prodotto maggiore del secondo:", primo.confronto(secondo))
    print("Confronto inverso:", secondo.confronto(primo))
    print("\n", terzo, sep="")
    print("Differenza:", terzo.differenza())
    print("Prodotto:", terzo.prodotto())
    print("Somma:", terzo.somma())
    print("Prodotto maggiore del quarto (prodotti uguali):", terzo.confronto(quarto))
    print("\nValori predefiniti:", predefinito)
    print("Prodotto con zero:", predefinito.prodotto())
    print("Tre valori predefiniti:", tre_predefiniti)
    print("Somma con zero:", tre_predefiniti.somma())
