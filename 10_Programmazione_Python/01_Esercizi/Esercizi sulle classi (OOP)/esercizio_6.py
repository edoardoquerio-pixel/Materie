"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Sesto esercizio - Polimorfismo con oggetti veicolo
Analisi: input = dati di veicoli impostati nel codice.
Output = descrizione, messaggio di accensione e spegnimento di ogni veicolo.
Suddivisione: Veicolo gestisce i dati comuni; Auto, Moto e Bicicletta
ridefiniscono i metodi. Una funzione gestisce tutti i veicoli nello stesso modo.
"""


class Veicolo:
    """Veicolo con marca e modello."""

    def __init__(self, marca: str, modello: str) -> None:
        """Riceve marca e modello (str); inizializza gli attributi (None)."""
        self.marca = marca
        self.modello = modello

    def accendi(self) -> str:
        """Senza parametri aggiuntivi; restituisce il messaggio di avvio (str)."""
        return "Il veicolo si avvia"

    def spegni(self) -> str:
        """Senza parametri aggiuntivi; restituisce il messaggio di arresto (str)."""
        return "Il veicolo si spegne"

    def __str__(self) -> str:
        """Senza parametri aggiuntivi; restituisce marca e modello (str)."""
        return f"{self.marca} {self.modello}"


class Auto(Veicolo):
    """Veicolo con un numero di porte."""

    def __init__(self, marca: str, modello: str, numero_porte: int) -> None:
        """Riceve marca, modello e numero di porte; inizializza l'auto (None)."""
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    def accendi(self) -> str:
        """Senza parametri aggiuntivi; restituisce l'avvio dell'auto (str)."""
        return "L'auto si avvia con la chiave"

    def spegni(self) -> str:
        """Senza parametri aggiuntivi; restituisce lo spegnimento dell'auto (str)."""
        return "L'auto si spegne girando la chiave"


class Moto(Veicolo):
    """Veicolo con una cilindrata."""

    def __init__(self, marca: str, modello: str, cilindrata: int) -> None:
        """Riceve marca, modello e cilindrata; inizializza la moto (None)."""
        super().__init__(marca, modello)
        self.cilindrata = cilindrata

    def accendi(self) -> str:
        """Senza parametri aggiuntivi; restituisce l'avvio della moto (str)."""
        return "La moto si avvia premendo il pulsante"

    def spegni(self) -> str:
        """Senza parametri aggiuntivi; restituisce lo spegnimento della moto (str)."""
        return "La moto si spegne con l'interruttore"


class Bicicletta(Veicolo):
    """Veicolo caratterizzato dal tipo di bicicletta."""

    def __init__(self, marca: str, modello: str, tipo: str) -> None:
        """Riceve marca, modello e tipo (str); inizializza la bicicletta (None)."""
        super().__init__(marca, modello)
        self.tipo = tipo

    def accendi(self) -> str:
        """Senza parametri aggiuntivi; restituisce il messaggio di avvio (str)."""
        return "La bicicletta è sempre pronta!"

    def spegni(self) -> str:
        """Senza parametri aggiuntivi; restituisce il messaggio di arresto (str)."""
        return "La bicicletta non si spegne mai"


##
## Funzioni:
##

def gestisci_veicolo(veicolo: Veicolo) -> None:
    """
    Funzione: gestisci_veicolo
        Stampa i dati e richiama i metodi specifici del veicolo ricevuto.
    Parametri formali:
        veicolo (Veicolo): oggetto della classe base o di una classe derivata.
    Valore di ritorno:
        None: stampa le informazioni e i messaggi dei metodi.
    """
    print(f"{type(veicolo).__name__}: {veicolo}")
    print(veicolo.accendi())
    print(veicolo.spegni())


"""
Programma principale
Crea un oggetto per ciascuna classe e li gestisce attraverso una lista.
"""
if __name__ == "__main__":
    # Input di esempio e inizializzazione degli oggetti.
    veicolo = Veicolo("Generica", "Base")  # Prova della classe base.
    auto = Auto("Fiat", "Panda", 5)
    moto = Moto("Honda", "CBR", 600)
    bicicletta = Bicicletta("Bianchi", "Mountain Bike", "mountain bike")
    veicoli = [veicolo, auto, moto, bicicletta]  # Collezione di veicoli diversi.

    # Elaborazione e output: stessa chiamata, comportamenti diversi.
    for elemento in veicoli:
        gestisci_veicolo(elemento)
        print("---")
