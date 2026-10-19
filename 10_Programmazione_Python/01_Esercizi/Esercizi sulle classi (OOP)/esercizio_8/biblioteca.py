"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Ottavo esercizio - Gestione del catalogo della biblioteca
Analisi: input = media, titolo da rimuovere o autore da cercare.
Output = catalogo, risultati di ricerca e conteggio di libri e DVD.
Suddivisione: un metodo per ogni operazione sulla lista dei media.
La ricerca per autore e' parziale e non distingue maiuscole e minuscole.
La rimozione elimina il primo media con titolo uguale, ignorando le maiuscole.
"""

from media import Media, Libro, DVD


class Biblioteca:
    """Gestisce una lista di media."""

    def __init__(self) -> None:
        """Senza parametri aggiuntivi; inizializza una lista vuota (None)."""
        self.media = []  # Elementi presenti nel catalogo.

    def aggiungi_media(self, media: Media) -> None:
        """Riceve un Media o una sua derivata; lo aggiunge e restituisce None."""
        self.media.append(media)

    def rimuovi_media(self, titolo: str) -> bool:
        """Riceve un titolo (str); restituisce True se rimosso, False se assente."""
        for elemento in self.media:
            if elemento.titolo.lower() == titolo.lower():
                self.media.remove(elemento)
                return True
        return False

    def cerca_per_autore(self, autore: str) -> list:
        """Riceve un autore (str); restituisce la lista dei media corrispondenti."""
        risultati = []  # Media il cui autore contiene il testo cercato.
        for elemento in self.media:
            if autore.lower() in elemento.autore.lower():
                risultati.append(elemento)
        return risultati

    def stampa_catalogo(self) -> None:
        """Senza parametri aggiuntivi; stampa media e tempi, restituisce None."""
        if not self.media:
            print("Il catalogo e' vuoto.")
        for elemento in self.media:
            print(elemento)
            if isinstance(elemento, Libro):
                minuti = elemento.tempo_lettura()  # Tempo totale di lettura.
                print("Tempo di lettura stimato:", minuti, "minuti",
                      f"({minuti // 60} ore e {minuti % 60} minuti)")
            elif isinstance(elemento, DVD):
                print("Tempo di visione:", elemento.tempo_visione(), "(ore:minuti)")
            print("---")

    def get_statistiche(self) -> dict:
        """Senza parametri aggiuntivi; restituisce un dict con conteggi e totale."""
        libri = 0  # Numero di libri nel catalogo.
        dvd = 0  # Numero di DVD nel catalogo.
        for elemento in self.media:
            if isinstance(elemento, Libro):
                libri += 1
            elif isinstance(elemento, DVD):
                dvd += 1
        return {"libri": libri, "dvd": dvd, "totale": len(self.media)}
