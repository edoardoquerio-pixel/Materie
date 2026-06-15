Genera dati di test in C# per un progetto con le seguenti classi:

- Venditore (Nome, Cognome, Stipendio double, Settore: Auto/Moto)
- Meccanico (Nome, Cognome, Stipendio double, Tipologia: Carrozzeria/Meccanica)
- ResponsabileVenditori : Venditore (con lista di Venditori seguiti)
- CapoOfficina : Meccanico (con lista di Ordini gestiti)
- Prodotto (Codice string, Denominazione, Descrizione, Prezzo double, Giacenza int)
- Ordine (Data, lista di Prodotto, Venditore associato)

Mi servono:
1. 4 venditori (2 Auto, 2 Moto) con stipendi realistici
2. 1 responsabile venditori che li gestisce tutti
3. 2 meccanici (1 Carrozzeria, 1 Meccanica) 
4. 1 capo officina che gestisce tutti gli ordini
5. 8 prodotti di ricambio auto/moto con codici P001-P008, prezzi e giacenze realistici
6. 3 ordini con date di giugno 2026, ognuno con 5-6 prodotti (anche ripetuti per simularne quantità multiple) e un venditore associato
