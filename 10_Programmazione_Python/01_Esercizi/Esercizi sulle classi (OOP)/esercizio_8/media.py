"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Ottavo esercizio - Classi dei media della biblioteca
Analisi: input = dati di libri e DVD; output = informazioni e tempi di fruizione.
Suddivisione: Media gestisce i dati comuni; Libro e DVD aggiungono i propri dati.
"""


class Media:
    """Elemento del catalogo con titolo, autore e anno."""

    def __init__(self, titolo: str, autore: str, anno: int) -> None:
        """Riceve titolo, autore e anno; inizializza gli attributi (None)."""
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def get_info(self) -> str:
        """Senza parametri aggiuntivi; restituisce le informazioni base (str)."""
        return f'"{self.titolo}" di {self.autore} ({self.anno})'

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce le informazioni del media (str)."""
        return self.get_info()


class Libro(Media):
    """Media con un numero di pagine."""

    def __init__(self, titolo: str, autore: str, anno: int, numero_pagine: int) -> None:
        """Riceve i dati base e il numero di pagine; inizializza il libro (None)."""
        super().__init__(titolo, autore, anno)
        self.numero_pagine = numero_pagine

    def get_info(self) -> str:
        """Senza parametri aggiuntivi; restituisce dati e numero di pagine (str)."""
        return f"Libro: {super().get_info()} - {self.numero_pagine} pagine"

    def tempo_lettura(self) -> int:
        """Senza parametri aggiuntivi; restituisce i minuti di lettura (int)."""
        return self.numero_pagine * 2


class DVD(Media):
    """Media con una durata espressa in minuti."""

    def __init__(self, titolo: str, autore: str, anno: int, durata_minuti: int) -> None:
        """Riceve i dati base e la durata in minuti; inizializza il DVD (None)."""
        super().__init__(titolo, autore, anno)
        self.durata_minuti = durata_minuti

    def get_info(self) -> str:
        """Senza parametri aggiuntivi; restituisce dati e durata del DVD (str)."""
        return f"DVD: {super().get_info()} - {self.durata_minuti} minuti"

    def tempo_visione(self) -> str:
        """Senza parametri aggiuntivi; restituisce la durata in ore:minuti (str)."""
        ore = self.durata_minuti // 60  # Ore complete della durata.
        minuti = self.durata_minuti % 60  # Minuti rimanenti.
        return f"{ore}:{minuti:02d}"
