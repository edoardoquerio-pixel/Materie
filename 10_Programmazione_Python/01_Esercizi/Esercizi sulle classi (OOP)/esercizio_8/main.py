"""
Autore: Edoardo Querio Gianetto
Data: 19/10/2026

Titolo: Ottavo esercizio - Sistema modulare per gestione biblioteca
Analisi: input = libri e DVD definiti nel codice, titolo e autore da cercare.
Output = catalogo, statistiche, ricerca per autore e risultato delle rimozioni.
Suddivisione: media.py definisce i media; biblioteca.py gestisce la collezione;
main.py importa le classi e prova tutti i metodi senza input da tastiera.
"""

from media import Media, Libro, DVD
from biblioteca import Biblioteca


"""
Programma principale
Popola una biblioteca e verifica le operazioni sul catalogo.
"""
if __name__ == "__main__":
    # Input di esempio e inizializzazione degli oggetti.
    biblioteca = Biblioteca()  # Catalogo inizialmente vuoto.
    libro1 = Libro("1984", "George Orwell", 1949, 328)
    dvd = DVD("Inception", "Christopher Nolan", 2010, 148)
    libro2 = Libro("Il Nome della Rosa", "Umberto Eco", 1980, 512)
    media_base = Media("Materiale di esempio", "Autore di esempio", 2026)

    # Elaborazione: inserimento dei media e prova della classe base.
    print("Informazioni del media base:", media_base.get_info())
    print("Rappresentazione del media base:", media_base)
    biblioteca.aggiungi_media(libro1)
    biblioteca.aggiungi_media(dvd)
    biblioteca.aggiungi_media(libro2)

    # Sezione di output: catalogo e statistiche.
    print("\n=== CATALOGO BIBLIOTECA ===")
    biblioteca.stampa_catalogo()
    statistiche = biblioteca.get_statistiche()  # Conteggi dei media presenti.
    print("\n=== STATISTICHE ===")
    print("Libri:", statistiche["libri"])
    print("DVD:", statistiche["dvd"])
    print("Totale media:", statistiche["totale"])

    # Ricerca parziale per autore, come nell'esempio della consegna.
    print('\n=== RICERCA PER AUTORE "Orwell" ===')
    risultati = biblioteca.cerca_per_autore("Orwell")
    for elemento in risultati:
        print(elemento)

    # Prova di ricerca senza risultati e rimozione di titoli presenti o assenti.
    print("Ricerca autore assente:", biblioteca.cerca_per_autore("Autore assente"))
    print("\nRimozione di Inception:", biblioteca.rimuovi_media("Inception"))
    print("Rimozione di titolo assente:", biblioteca.rimuovi_media("Titolo assente"))
    print("\n=== CATALOGO DOPO LA RIMOZIONE ===")
    biblioteca.stampa_catalogo()
    print("Statistiche aggiornate:", biblioteca.get_statistiche())
