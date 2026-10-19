"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Terzo esercizio sui files
Creare una classe che restituisca la parola piu' frequente in un file di testo.
Analisi: input = nome del file; output = parola piu' frequente.
Suddivisione: lettura, conteggio con dizionario e ricerca del massimo.
Si ignorano le maiuscole e si toglie la punteggiatura agli estremi delle parole.
In caso di parita' si conserva la prima parola incontrata.
Testo di prova disponibile: divina_commedia.txt (Project Gutenberg).
"""


class FrequenzeTesto:
    """Legge un testo e conta le occorrenze delle parole."""

    def __init__(self, nome_file: str) -> None:
        """Riceve il nome del file (str); inizializza il dizionario (None)."""
        self.nome_file = nome_file
        self.frequenze = {}  # Occorrenze di ogni parola.

    def leggi_file(self) -> None:
        """Senza parametri aggiuntivi; legge e conta le parole (None)."""
        with open(self.nome_file, "r", encoding="utf-8") as file:
            testo = file.read()
        self.frequenze = {}
        for parola in testo.lower().split():
            parola = parola.strip(".,;:!?\"'()-")
            if parola != "":
                if parola in self.frequenze:
                    self.frequenze[parola] += 1
                else:
                    self.frequenze[parola] = 1

    def parola_piu_frequente(self) -> str:
        """Senza parametri aggiuntivi; restituisce la parola o una stringa vuota."""
        risultato = ""  # Parola con il conteggio maggiore.
        massimo = 0  # Frequenza massima incontrata.
        for parola in self.frequenze:
            if self.frequenze[parola] > massimo:
                massimo = self.frequenze[parola]
                risultato = parola
        return risultato


"""
Programma principale
Prova il conteggio delle parole di un file, ad esempio divina_commedia.txt.
"""
if __name__ == "__main__":
    # Sezione di input dati
    nome_file = input("Nome o percorso del file di testo: ")

    # Inizializzazioni variabili
    analizzatore = FrequenzeTesto(nome_file)

    # Elaborazione
    analizzatore.leggi_file()
    parola = analizzatore.parola_piu_frequente()

    # Sezione di output
    print("Parola piu' frequente:", parola)
