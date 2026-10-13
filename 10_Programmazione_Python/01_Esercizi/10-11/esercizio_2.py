"""
Autore: Edoardo Querio Gianetto
Data: 12/10/2026

Titolo: Secondo esercizio sulle classi (OOP)
Creare una classe Rettangolo con base, altezza, area, perimetro e contiene.
Analisi: input = dimensioni di due rettangoli; output = area, perimetro
e risultato del confronto tra le dimensioni.
Suddivisione: gestione delle dimensioni, calcoli e confronto dei rettangoli.
Si confrontano base con base e altezza con altezza, senza rotazioni.
Le dimensioni devono essere non negative; il confronto e' strettamente maggiore.
"""

##
## Classi:
##

class Rettangolo:
    """Rappresenta un rettangolo mediante base e altezza."""

    def __init__(self, base: float, altezza: float) -> None:
        """
        Metodo: __init__
            Inizializza le dimensioni tramite i setter.
        Parametri formali:
            base (float): lunghezza della base, non negativa.
            altezza (float): lunghezza dell'altezza, non negativa.
        Valore di ritorno:
            None. Solleva ValueError per dimensioni negative.
        """
        self.set_base(base)
        self.set_altezza(altezza)

    def get_base(self) -> float:
        """Restituisce la base (float); non richiede parametri aggiuntivi."""
        return self.base

    def set_base(self, base: float) -> None:
        """Imposta base (float); restituisce None, ValueError se negativa."""
        if base < 0:
            raise ValueError("La base non puo' essere negativa.")
        self.base = base  # Lunghezza della base.

    def get_altezza(self) -> float:
        """Restituisce l'altezza (float); non richiede altri parametri."""
        return self.altezza

    def set_altezza(self, altezza: float) -> None:
        """Imposta altezza (float); restituisce None, ValueError se negativa."""
        if altezza < 0:
            raise ValueError("L'altezza non puo' essere negativa.")
        self.altezza = altezza  # Lunghezza dell'altezza.

    def area(self) -> float:
        """Restituisce base per altezza (float); non richiede altri parametri."""
        return self.base * self.altezza

    def perimetro(self) -> float:
        """Restituisce il perimetro (float); non richiede altri parametri."""
        return 2 * (self.base + self.altezza)

    def contiene(self, rettangolo: "Rettangolo") -> bool:
        """
        Metodo: contiene
            Confronta le dimensioni dei due rettangoli.
        Parametri formali:
            rettangolo (Rettangolo): oggetto da confrontare con self.
        Valore di ritorno:
            bool: True se entrambe le dimensioni di self sono maggiori,
            False altrimenti, anche in caso di dimensioni uguali.
        """
        return self.base > rettangolo.get_base() and self.altezza > rettangolo.get_altezza()


"""
Programma principale
Crea due rettangoli, modifica il secondo e confronta le dimensioni.
"""
if __name__ == "__main__":
    # Sezione di input dati
    base = 10.0  # Base del primo rettangolo.
    altezza = 8.0  # Altezza del primo rettangolo.

    # Inizializzazioni variabili
    rettangolo1 = Rettangolo(base, altezza)  # Rettangolo maggiore.
    rettangolo2 = Rettangolo(3.0, 2.0)  # Rettangolo da confrontare.

    # Elaborazione
    rettangolo2.set_base(5.0)
    rettangolo2.set_altezza(4.0)

    # Sezione di output
    print("Primo rettangolo:", rettangolo1.get_base(), "x", rettangolo1.get_altezza())
    print("Area:", rettangolo1.area())
    print("Perimetro:", rettangolo1.perimetro())
    print("Secondo rettangolo:", rettangolo2.get_base(), "x", rettangolo2.get_altezza())
    print("Area:", rettangolo2.area())
    print("Perimetro:", rettangolo2.perimetro())
    print("Il primo contiene il secondo:", rettangolo1.contiene(rettangolo2))
    print("Il secondo contiene il primo:", rettangolo2.contiene(rettangolo1))
