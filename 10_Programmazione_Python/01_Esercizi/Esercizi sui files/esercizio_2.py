"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Secondo esercizio sui files
Creare una classe che legga un testo e salvi la parola piu' lunga in output.txt.
Analisi: input = nome del file; output = parola piu' lunga su output.txt.
Suddivisione: lettura, ricerca della parola e scrittura del risultato.
Si separano le parole con split e si toglie la punteggiatura ai loro estremi.
In caso di parita' si conserva la prima parola incontrata.
"""


class AnalizzatoreParole:
    """Legge un file di testo e cerca la parola piu' lunga."""

    def __init__(self, nome_file: str) -> None:
        """Riceve il nome del file (str); inizializza il testo (None)."""
        self.nome_file = nome_file
        self.testo = ""  # Contenuto del file.

    def leggi_file(self) -> None:
        """Senza parametri aggiuntivi; legge il testo e restituisce None."""
        with open(self.nome_file, "r", encoding="utf-8") as file:
            self.testo = file.read()

    def parola_piu_lunga(self) -> str:
        """Senza parametri aggiuntivi; restituisce la parola o una stringa vuota."""
        risultato = ""  # Parola piu' lunga incontrata.
        for parola in self.testo.split():
            parola = parola.strip(".,;:!?\"'()-")
            if len(parola) > len(risultato):
                risultato = parola
        return risultato

    def salva_parola(self) -> None:
        """Senza parametri aggiuntivi; salva la parola in output.txt (None)."""
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(self.parola_piu_lunga())


"""
Programma principale
Prova la classe e salva la parola piu' lunga del testo.
"""
if __name__ == "__main__":
    # Sezione di input dati
    nome_file = input("Nome o percorso del file di testo: ")

    # Inizializzazioni variabili
    analizzatore = AnalizzatoreParole(nome_file)

    # Elaborazione
    analizzatore.leggi_file()
    analizzatore.salva_parola()

    # Sezione di output
    print("Parola salvata in output.txt:", analizzatore.parola_piu_lunga())
