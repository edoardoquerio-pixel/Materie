"""
Autore: Edoardo Querio Gianetto
Data: 14/10/2026

Titolo: Quarto esercizio - Ereditarieta' di Persona
Analisi: input = nome, indirizzo, eta' e dati di scuola o azienda.
Output = descrizione delle persone e valori letti dopo una modifica.
Suddivisione: Persona gestisce i dati comuni; Studente e Lavoratore
aggiungono i propri attributi, riutilizzando il costruttore della classe base.
"""


class Persona:
    """Persona con nome, indirizzo ed eta'."""

    def __init__(self, nome: str, indirizzo: str, eta: int) -> None:
        """Riceve nome, indirizzo ed eta'; inizializza gli attributi (None)."""
        self.nome = nome
        self.indirizzo = indirizzo
        self.eta = eta

    def get_nome(self) -> str:
        """Senza parametri aggiuntivi; restituisce il nome (str)."""
        return self.nome

    def set_nome(self, nome: str) -> None:
        """Riceve il nuovo nome (str); lo aggiorna e restituisce None."""
        self.nome = nome

    def get_indirizzo(self) -> str:
        """Senza parametri aggiuntivi; restituisce l'indirizzo (str)."""
        return self.indirizzo

    def set_indirizzo(self, indirizzo: str) -> None:
        """Riceve il nuovo indirizzo (str); lo aggiorna e restituisce None."""
        self.indirizzo = indirizzo

    def get_eta(self) -> int:
        """Senza parametri aggiuntivi; restituisce l'eta' (int)."""
        return self.eta

    def set_eta(self, eta: int) -> None:
        """Riceve la nuova eta' (int); la aggiorna e restituisce None."""
        self.eta = eta

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce i dati comuni (str)."""
        return f"Nome: {self.nome}, indirizzo: {self.indirizzo}, eta': {self.eta}"


class Studente(Persona):
    """Persona che frequenta una scuola e possiede una media voti."""

    def __init__(self, nome: str, indirizzo: str, eta: int,
                 scuola: str, media_voti: float) -> None:
        """Riceve i dati personali, scuola e media; inizializza lo studente (None)."""
        super().__init__(nome, indirizzo, eta)
        self.scuola = scuola
        self.media_voti = media_voti

    def get_scuola(self) -> str:
        """Senza parametri aggiuntivi; restituisce la scuola (str)."""
        return self.scuola

    def set_scuola(self, scuola: str) -> None:
        """Riceve la scuola (str); la aggiorna e restituisce None."""
        self.scuola = scuola

    def get_media_voti(self) -> float:
        """Senza parametri aggiuntivi; restituisce la media voti (float)."""
        return self.media_voti

    def set_media_voti(self, media_voti: float) -> None:
        """Riceve la media voti (float); la aggiorna e restituisce None."""
        self.media_voti = media_voti

    def __str__(self) -> str:
        """Restituisce i dati personali, la scuola e la media voti (str)."""
        return f"{super().__str__()}, scuola: {self.scuola}, media voti: {self.media_voti}"


class Lavoratore(Persona):
    """Persona che lavora per un'azienda e riceve uno stipendio."""

    def __init__(self, nome: str, indirizzo: str, eta: int,
                 azienda: str, stipendio: float) -> None:
        """Riceve i dati personali, azienda e stipendio; inizializza l'oggetto (None)."""
        super().__init__(nome, indirizzo, eta)
        self.azienda = azienda
        self.stipendio = stipendio

    def get_azienda(self) -> str:
        """Senza parametri aggiuntivi; restituisce l'azienda (str)."""
        return self.azienda

    def set_azienda(self, azienda: str) -> None:
        """Riceve l'azienda (str); la aggiorna e restituisce None."""
        self.azienda = azienda

    def get_stipendio(self) -> float:
        """Senza parametri aggiuntivi; restituisce lo stipendio (float)."""
        return self.stipendio

    def set_stipendio(self, stipendio: float) -> None:
        """Riceve lo stipendio (float); lo aggiorna e restituisce None."""
        self.stipendio = stipendio

    def __str__(self) -> str:
        """Restituisce i dati personali, l'azienda e lo stipendio (str)."""
        return f"{super().__str__()}, azienda: {self.azienda}, stipendio: {self.stipendio}"


if __name__ == "__main__":
    # Input di esempio e inizializzazione: un oggetto per ciascuna classe.
    persona = Persona("Anna", "Via Roma 1", 40)
    studente = Studente("Luca", "Via Po 2", 20, "ITS ICT", 8.0)
    lavoratore = Lavoratore("Sara", "Via Milano 3", 30, "Informatica SRL", 1800.0)

    # Output prima delle modifiche: prova dei metodi __str__.
    print(persona)
    print(studente)
    print(lavoratore)

    # Elaborazione: prova dei setter, anche di quelli ereditati.
    persona.set_indirizzo("Via Torino 4")
    studente.set_eta(21)
    studente.set_media_voti(8.5)
    lavoratore.set_stipendio(2000.0)

    # Output: prova dei getter.
    print("\nNuovo indirizzo:", persona.get_indirizzo())
    print("Eta' studente:", studente.get_eta())
    print("Media voti:", studente.get_media_voti())
    print("Stipendio:", lavoratore.get_stipendio())
