Descrizione della consegna: 

Realizzare le seguenti classi:

1) Persona è una classe astratta con

proprietà: Nome, Cognome, Stipendio
metodi: Tredicesima
2) Venditore che eredita da Persona con

proprietà: Settore che descrive il tipo di settore vendite a cui fa capo: Auto o Moto
metodi: Tredicesima che restituisce il 91% in più dello stipendio, Clone
3) Meccanico eredita da Persona con

proprietà: Tipologia che descrive il tipo di settore a cui fa capo: Carrozzeria o Meccanica
metodi: Tredicesima che restituisce il 93% in più dello stipendio, Equals
4) ResponsabileVenditori eredita da Venditore con

metodi:  Tredicesima che restituisce il doppio dello stipendio più un bonus del 15% della tariffa giornaliera di ogni venditore di cui è responsabile
5) CapoOfficina eredita da Meccanico con

metodi: Tredicesima che ridefinisce il metodo e restituisce il doppio dello stipendio più il 5% dell’importo di ogni ordine da gestire
6) Prodotto che contiene come

proprietà: Codice, Denominazione, Descrizione, Prezzo, Giacenza
7) Ordine (classe che impedisce l’ereditarietà) che contiene come

proprietà: Codice di tipo alfanumerico a lunghezza 8 caratteri fissi, univoco e generato automaticamente alla creazione dell'ordine (es. AB23F4TD, D23H4G6F, ecc... non può iniziare con un numero, caratteri maiuscoli), la Data, ElencoProdotti ovvero la lista di prodotti assegnati all'ordine, Venditore di tipo Venditore
metodi: NumeroPezzi che restituisce la quantità totale di prodotti ordinati, Totale ovvero il costo complessivo, Stampa che è un metodo per stampare l’elenco dettagliato dell’ordine su file txt denominato con codice dell'ordine (es. AB23F4TD.txt), che deve essere salvato nella cartella file presente all'interno del progetto a pari livello del main, dove sono presenti tutti i dati dell'ordine e per ogni prodotto su singola riga è presente il codice prodotto, nome del prodotto, quantità ordinata, prezzo unitario e subtotale. Alla fine di questo elenco è presente il totale dell'ordine.
Creare un Presentation Layer per scegliere una tra le seguenti opzioni:
Visualizzare i dati del responsabile dei venditori
Visualizzare i dati del capo officina
Stampare un ordine tramite codice
Termina il programma
Si consiglia di utilizzare l'AI di proprio gradimento per generare i dati di testing con cui popolare le liste

Strumenti

Linguaggio di programmazione: C#

Ambiente di Sviluppo: Visual Studio 2026 Community

Consegna

Per effettuare la consegna dell'esercitazione1 si chiede di:

generare un file pdf con intestazione con i dati dello/a studente/ssa: cognome, nome, corso, modulo e data e con all'interno tutte le classi create e presenti nel progetto 
effettuare il zip della cartella dell'intero progetto (comprensivo di file .sln), denominato come Studente_Esercitazione1.zip, dove Studente è il cognome dello studente. Nel caso ci fossero studenti con lo stesso cognome allora aggiungere anche l'iniziale del Nome.
Inviare i due file in piattaforma fad

Metodologia della valutazione: Voto 30/30



Griglia di valutazione
Descrittore	Punti
Classi	9
Collezione di dati	9
Interfaccia testuale	6
Funzionalità	6
Totale	30