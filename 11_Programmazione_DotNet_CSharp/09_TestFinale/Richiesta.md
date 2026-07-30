Si consideri il backup del database: BikeStores.

Utilizzare Microsoft Visual Studio 2026 per creare una soluzione vuota denominata: BikeStoresProject

BikeStores.Data
Aggiungere alla soluzione BikeStoresProject un nuovo progetto di librerie di classi denominato: BikeStores.Data. Aggiungere le librerie necessarie per Microsoft Entity Framework Core. Effettuare l'accesso al database come utente di Windows e generare lo scaffolding delle classi object model nella cartella Models.


BikeStores.Frontend

Aggiungere alla soluzione BikeStoresProject un nuovo progetto App Web ASP.NET Core MVC, con autenticazione Nessuna, https e  non usare istruzioni di primo livello e denominato BikeStores.Frontend. 

L'applicazione ha contenuti solo in Inglese 

Nel footer inserire i propri dati, dopo il copyright: Realizzato da Querio Gianetto Edoardo, Corso: Claude Specialist. 

Includere nelle dipendenze il progetto BikeStores.Data che ha solo dati, si utilizzerà entry framework per parlare con il db questo db sarà incluso con gli altri progetti che andiamo a creare e che saranno almeno 3. 

Registrare il servizio BikeStoresContext. 

Dalla barra di navigazione è possibile visualizzare l'elenco dei prodotti alla voce Products in ordine alfabetico crescente. Visualizzare in elenco solo i seguenti dati: nome del prodotto, marca, categoria, il prezzo. Per ogni elemento visualizzato predisporre la visualizzazione in dettaglio con tutti gli elementi precedenti e in aggiunta l'anno di produzione e quantità disponibile . Non sono ammesse le operazioni CRUD.
Ovvero deve esserci solo elenco e dettaglio.

Creare il servizio per visualizzare l'elenco dei negozi. Di ogni negozio nella lista sono visibili solo pochi dati (nome, telefono, email, città e stato). Il dettaglio fornisce l'elenco dettagliato del negozio. 

Per ogni negozio è necessario avere l'elenco dei dipendenti che ci lavorano visibile a forma di griglia nel dettaglio del negozio. Di questi dipendenti sono reperibili solo i seguenti dati: nome, cognome, email, telefono. Inoltre per ogni dipendente è disponibile il dettaglio con tutti i dati, cliccando sul link Details.

Creare il servizio per visualizzare l'elenco dei prodotti di una certa marca o nome o categoria. Il servizio deve utilizzare la vista Index del controller Products.


BikeStores.Backend
Aggiungere alla soluzione BikeStoresProject un nuovo progetto App Web ASP.NET Core MVC, con autenticazione Individuale, https e  non usare istruzioni di primo livello e denominato BikeStores.Backend.

La porta di comunicazione del protocollo https è 5001

Generare nel database BikeStores le tabelle per effettuare l'autenticazione sull'applicativo.

Creare i seguenti account: admin@bikes.shop con password: @Bike-2026

Creare i seguenti ruoli: Administrators, Employees, Customers.

Associare i ruoli agli utenti, come segue: admin@bikes.shop => Administrators, tutti i dipendenti a Employees, tutti i clienti a Customers.

Per effettuare l'acceso utilizzare utilizzare email e come password: @Bike-2026 (uguale per tutti gli utenti)

Dopo autenticazione si accede ad una DashBoard dove sono presenti diverse funzionalità.

Nel caso di un amministratore sarà possibile visualizzare la gestione degli ordini, l'elenco dei clienti, la gestione del catalogo (marche, categorie, prodotti, magazzino), la gestione dei negozi, la gestione dei dipendenti. Per gli amministratori sono consentite le operazioni CRUD.

Nel caso di un impiegato sarà possibile visualizzare gli ordini da lui gestiti, i clienti. Per gli impiegati sono consentite le operazioni CRUD solo per la gestione degli ordini e dei clienti.

Nel caso di un cliente sarà possibile visualizzare i propri ordini, il proprio profilo (Dettaglio). Sono ammesse le operazioni CRUD (tranne l'eliminazione) per le modifiche dei propri dati.

In merito alla gestione degli ordini è richiesta una funzionalità di ricerca, mediante menu a tendina, con la possibilità di visualizzare solo gli ordini appartenenti ad uno stato specifico (es. Pending, Processing, ecc...). Inoltre la visualizzazione degli ordini deve essere visualizzata per Data ordine decrescente. Si consideri altresì nel dettaglio degli ordini anche l'elenco dei prodotti dell'ordine. Per ogni riga sono richiesti i seguenti campi: ProductName, Quantity, ListPrice, Discount, TotalPrice, DiscountTotal, SubTotal. In coda a questo elenco il totale dell'ordine

In merito alla visualizzazione del magazzino, l'amministratore può cercare i prodotti esauriti oppure quelli in scorta (prodotti che hanno quantità compresa tra 1 e 9) 