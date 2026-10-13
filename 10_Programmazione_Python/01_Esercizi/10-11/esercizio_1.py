"""
Autore: Edoardo Querio Gianetto
Data: 12/10/2026

Titolo: Primo esercizio sulle classi (OOP)
Creare una classe Insegnante con nome, eta' e stipendio privato.
Analisi: input = dati di due insegnanti; output = nome, eta' e stipendio.
Suddivisione: costruzione degli oggetti, lettura e modifica degli attributi.
"""

##
## Classi:
##

class Insegnante:
    """Rappresenta un insegnante con nome, eta' e stipendio privato."""

    def __init__(self, nome: str, eta: int, stipendio: float) -> None:
        """
        Metodo: __init__
            Inizializza i dati dell'insegnante.
        Parametri formali:
            nome (str): nome dell'insegnante.
            eta (int): eta' in anni.
            stipendio (float): stipendio dell'insegnante.
        Valore di ritorno:
            None.
        """
        self.nome = nome  # Nome pubblico dell'insegnante.
        self.eta = eta  # Eta' pubblica dell'insegnante.
        self.__stipendio = stipendio  # Stipendio privato dell'insegnante.

    def get_nome(self) -> str:
        """Restituisce il nome (str); non richiede parametri aggiuntivi."""
        return self.nome

    def set_nome(self, nome: str) -> None:
        """Imposta nome (str), nuovo nome dell'insegnante; restituisce None."""
        self.nome = nome

    def get_eta(self) -> int:
        """Restituisce l'eta' (int); non richiede parametri aggiuntivi."""
        return self.eta

    def set_eta(self, eta: int) -> None:
        """Imposta eta (int), nuova eta' dell'insegnante; restituisce None."""
        self.eta = eta

    def get_stipendio(self) -> float:
        """Restituisce lo stipendio (float); non richiede altri parametri."""
        return self.__stipendio

    def set_stipendio(self, stipendio: float) -> None:
        """Imposta stipendio (float), nuovo stipendio; restituisce None."""
        self.__stipendio = stipendio

    def __str__(self) -> str:
        """Restituisce nome ed eta' come str; non richiede altri parametri."""
        return f"Nome: {self.nome}, eta': {self.eta}"


"""
Programma principale
Crea due insegnanti, modifica i dati del secondo e stampa i risultati.
"""
if __name__ == "__main__":
    # Sezione di input dati
    nome1 = "Mario Rossi"  # Nome del primo insegnante.
    nome2 = "Anna Bianchi"  # Nome del secondo insegnante.

    # Inizializzazioni variabili
    insegnante1 = Insegnante(nome1, 45, 1800.0)  # Primo oggetto.
    insegnante2 = Insegnante(nome2, 38, 1700.0)  # Secondo oggetto.

    # Elaborazione
    insegnante2.set_nome("Anna Verdi")
    insegnante2.set_eta(39)
    insegnante2.set_stipendio(1750.0)

    # Sezione di output
    print("Primo insegnante:", insegnante1)
    print("Stipendio:", insegnante1.get_stipendio())
    print("Secondo insegnante:", insegnante2)
    print("Nome:", insegnante2.get_nome())
    print("Eta':", insegnante2.get_eta())
    print("Stipendio:", insegnante2.get_stipendio())
