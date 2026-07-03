# 12 - RESTful API — Tutte le Sessioni


---

## Sessione 1: Test RESTful API Gruppi


Test RESTful API  •  ITS Competenze Informatiche/Digitali
Nome: ______________________________   Data: ___________
Questo fascicolo contiene 8 domande di tre tipologie:
🔍  Correggere Errori – individua e correggi gli errori presenti
🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B
✅  Vero o Falso – indica V o F e motiva brevemente la risposta
Domanda 1   [Correggere Errori]   Argomento: JSON
Il seguente oggetto JSON contiene 3 errori. Individuali e correggi.
'nome': 'Mario Rossi',
"attivo": True,
"tags": ["admin", "editor",],
Correzioni e spiegazioni:
Domanda 2   [Abbinamento]   Argomento: Verbi HTTP
Abbina ogni verbo HTTP alla sua descrizione corretta.
Risposte:  1__   2__   3__   4__   5__   6__
Domanda 3   [Vero o Falso]   Argomento: Principi REST
Per ognuna delle seguenti affermazioni indica se è VERA o FALSA e motiva brevemente.
Domanda 4   [Correggere Errori]   Argomento: Endpoint REST
I seguenti endpoint violano le convenzioni REST. Correggi ognuno e spiega perché.
POST /getUser/123
GET  /deleteProduct/456
GET  /api/v1/user         (per ottenere tutti gli utenti)
POST /api/v1/orders/create
Correzioni e spiegazioni:
Domanda 5   [Abbinamento]   Argomento: Codici di Stato HTTP
Abbina ogni codice di stato HTTP alla situazione corrispondente.
Risposte:  1__   2__   3__   4__   5__   6__
Domanda 6   [Vero o Falso]   Argomento: JSON
Indica VERO o FALSO e motiva la risposta.
Domanda 7   [Correggere Errori]   Argomento: Request/Response HTTP
La seguente request HTTP contiene errori. Individua e correggi.
SEND /api/v1/users HTTP/1.1
Host: api.example.com
content-Type: application/xml
"nome": "Luigi",
"email": "luigi@example.com"
Correzioni e spiegazioni:
Domanda 8   [Abbinamento]   Argomento: Architettura REST
Abbina ogni concetto REST alla sua definizione.
Risposte:  1__   2__   3__   4__   5__   6__
Test RESTful API  •  ITS Competenze Informatiche/Digitali
Nome: ______________________________   Data: ___________
Questo fascicolo contiene 8 domande di tre tipologie:
🔍  Correggere Errori – individua e correggi gli errori presenti
🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B
✅  Vero o Falso – indica V o F e motiva brevemente la risposta
Domanda 1   [Abbinamento]   Argomento: Verbi HTTP
Abbina ogni scenario all'operazione HTTP più appropriata.
Risposte:  1__   2__   3__   4__   5__   6__
Domanda 2   [Correggere Errori]   Argomento: JSON
Il seguente JSON ha 3 errori. Trovali e correggi.
"nome": 'Biblioteca Centrale',
{ "titolo": "1984", "anno": 1949, },
{ "titolo": "Il Signore degli Anelli", "pagine": null }
"aperta": false
Correzioni e spiegazioni:
Domanda 3   [Vero o Falso]   Argomento: Architettura REST
Indica VERO o FALSO con motivazione.
Domanda 4   [Abbinamento]   Argomento: Codici di Stato HTTP
Abbina il codice di stato HTTP alla sua famiglia e significato.
Risposte:  1__   2__   3__   4__   5__   6__
Domanda 5   [Correggere Errori]   Argomento: Request/Response HTTP
Questa response HTTP ha 3 errori. Correggili.
content-type: text/json
"messaggio": "Utente creato con successo"
Correzioni e spiegazioni:
Domanda 6   [Vero o Falso]   Argomento: Verbi HTTP
Indica VERO o FALSO con motivazione.
Domanda 7   [Correggere Errori]   Argomento: Endpoint REST
Correggi questi endpoint in modo che rispettino le convenzioni REST.
GET  /api/v1/getAllBooks
POST /api/v1/book/add
DEL  /api/v1/books/55
GET  /api/v1/book/10/getReviews
Correzioni e spiegazioni:
Domanda 8   [Abbinamento]   Argomento: OpenAPI/Swagger
Abbina ogni termine dell'ecosistema OpenAPI/Swagger alla sua funzione.
Risposte:  1__   2__   3__   4__   5__   6__
Test RESTful API  •  ITS Competenze Informatiche/Digitali
Nome: ______________________________   Data: ___________

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 2: Guida Essenziale alle API RESTful


<head><title>404 Not Found</title></head>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

---

## Sessione 3: index


<head><title>404 Not Found</title></head>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->

---

## Sessione 4: ISTRUZIONI MUSICLAB


# 🎵 MusicLab — Esercitazione REST API con Node.js, Express e SQLite
## Obiettivo
Costruire un'API RESTful per gestire una collezione musicale, con un frontend HTML (fornito) che consenta di interagire con essa tramite interfaccia grafica.
Al termine dell'esercitazione avrai un server Node.js con Express che espone endpoint REST, un database SQLite con dati reali, e una pagina HTML funzionante per visualizzare e modificare brani e playlist semplicemente inserendo http://localhost:3000 nella barra degli inidirizzi del browser.
## Prerequisiti
- Node.js installato (v18 o superiore)
- Un editor di codice (VS Code consigliato)
- Postman per testare gli endpoint (opzionale ma consigliato)
## Struttura del progetto
├── server.js          ← entry point del server
├── db.js          ← configurazione e inizializzazione del database
└── musiclab.db    ← file contenente il database
└── index.html     ← file unico contenente la grafica e le logiche di Frontend
│   ├── songs.js       ← endpoint per i brani
│   └── playlists.js   ← endpoint per le playlist (bonus)
├── package.json
├── package-lock.json
## Setup iniziale
### 1. Crea la cartella
Crea una cartella chiamata musiclab; poi da VSC entraci dentro tramite il comando File -> Open Folder
### 2. Inizializza il progetto
Apri il Terminale di VSC e assicurati che sia del tipo Git Bash (NON powershell!) e inizializza il progetto tramite il comando
Ricorda di specificare il file "server.js" come entry point (voce "main" del file package.js) e il type a "module" (non "common").
### 3. Installa le dipendenze e crea lo script di avvio
npm install express sqlite3 nodemon
Terminato il comando, vai nel file package.json appena creato, togli qualsiasi cosa ci sia nell'oggetto "scripts" e al suo interno metti il comando di avvio, in modo che risulti come segue:
"start": "nodemon server.js"
### 4. Crea la struttura di base dell'applicazione evvia il server
Definisci una costante "app" che rappresenti l'applicazione e le altre costanti necessarie (porta, basePath, ...), definisci il comando di avvio del server ( app.listen() ) e avvialo per verificare che tutto parta regolarmente:
## Schema del database
### Tabella `songs`
| Colonna  | Tipo    | Note             |
|----------|---------|------------------|
| id       | INTEGER | PK, autoincrement |
| title    | TEXT    | NOT NULL         |
| artist   | TEXT    | NOT NULL         |
| album    | TEXT    | nullable         |
| genre    | TEXT    | nullable         |
| year     | INTEGER | nullable         |
### Tabella `playlists` *(bonus)*
| Colonna     | Tipo    | Note             |
|-------------|---------|------------------|
| id          | INTEGER | PK, autoincrement |
| name        | TEXT    | NOT NULL         |
| description | TEXT    | nullable         |
### Tabella `playlist_songs` *(bonus)*
| Colonna     | Tipo    | Note                   |
|-------------|---------|------------------------|
| playlist_id | INTEGER | NOT NULL               |
| song_id     | INTEGER | NOT NULL               |
| PK composta su (playlist_id, song_id)  -> Vedi script sotto
CREATE TABLE IF NOT EXISTS playlist_songs (
playlist_id INTEGER NOT NULL,
song_id     INTEGER NOT NULL,
PRIMARY KEY (playlist_id, song_id)
## Parte base — CRUD sui brani (~2 ore)
### Endpoint da implementare
| Metodo   | Path              | Descrizione                              |
|----------|-------------------|------------------------------------------|
| `GET`    | `/songs`          | Recupera tutti i brani                   |
| `GET`    | `/songs?title=..` | Filtra per titolo (query param)          |
| `GET`    | `/songs?artist=..`| Filtra per artista (query param)         |
| `GET`    | `/songs/:id`      | Recupera un brano specifico              |
| `POST`   | `/songs`          | Aggiunge un nuovo brano                  |
| `PUT`    | `/songs/:id`      | Modifica un brano (sostituzione completa)|
| `DELETE` | `/songs/:id`      | Rimuove un brano                         |
### Indicazioni
**`GET /songs`**
- Se non ci sono query params, restituisci tutti i brani
- Se è presente `?title=rock`, filtra i brani il cui titolo contiene quella stringa (usa `LIKE` in SQL, case-insensitive)
- Se è presente `?artist=beatles`, filtra per artista
- I due filtri si possono combinare: `?artist=beatles&title=hey`
- Risposta: array JSON di brani, status 200
**`GET /songs/:id`**
- Se il brano esiste, restituiscilo come oggetto JSON, status 200
- Se non esiste, restituisci `{ error: "Brano non trovato" }`, status 404
**`POST /songs`**
- Il body JSON deve contenere almeno `title` e `artist`
- Se mancano, restituisci `{ error: "title e artist sono obbligatori" }`, status 400
- Dopo l'inserimento, restituisci il brano appena creato con il suo `id`, status 201

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 5: Lezione 1


UNITA’ FORMATIVA
Competenze informatiche/digitali
chiacchiere tra
Docente: Fabio Abbà
Per comprendere la ragione di fondo di questo corso è
utile fare un parallelo con ciò che facciamo tutti i giorni per
interagire: parlare.
Perchè ci sia una buona comunicazione occorrono alcuni
- chi fa una richiesta (client)
- chi ascolta (server)
- un canale di trasmissione della voce/richiesta
- una lingua comune (SOAP, REST, GraphQl, ecc.)
Distinzione tra
Client e Server
Questo assicura che ci possa essere uno scambio
efficace di informazioni tra due elementi.
Nel caso dei servizi web, è ormai prassi consolidata che
ci sia una netta distinzione di ruoli tra client, che richiede
e visualizza i dati, e server, che recupera ed invia i dati
Questo ha anche il vantaggio di disaccoppiare le
tecnologie utilizzate (p.es. è possibile modificare l'intera
architettura di persistenza dati lato server in maniera
completamente invisibile, o trasparente, per il client) e
quindi permettere la comunicazione tra sistemi e
linguaggi diversi.
Timeline delle origini
Protocollo HTTP
Nascita del Web
ARPANET, sviluppata negli anni '60,
era la prima rete di computer,
collegando istituzioni militari e
università, ponendo le basi per la
comunicazione digitale moderna.
Il protocollo TCP/IP, adottato nel
1983, ha sostituito NCP, permettendo
la comunicazione tra diversi sistemi
operativi e migliorando l'affidabilità
del trasferimento dati.
Il protocollo HTTP è stato introdotto
negli anni '90, consentendo la
trasmissione di contenuti web. Ha
trasformato il modo in cui gli utenti
interagiscono con le informazioni
Con la creazione di HTML e URL,
Tim Berners-Lee ha dato vita al
World Wide Web, rivoluzionando
l'accesso alle informazioni e
cambiando il panorama digitale per
Hyper Text Markup Language, creato da Tim BernersLee, è un linguaggio di markup essenziale che definisce
la struttura delle pagine web. Permette di posizionare e
formattare contenuti visibili nei browser per l'utente
Esempio del primo HTTP, basata su due soli
oggetti: request e response.
Ma con l'evoluzione del web, è nata l'esigenza di fornire
all'utente dei contenuti dinamici, ossia che si adattassero
alle sue azioni o che potessero modificare il contesto
applicativo: risultati di ricerca, form di contatto, pagine
personalizzate.
Si giunge dapprima ad un'interattività lato server: Common
Gateway Interface permetteva al server web di eseguire
programmi esterni per generare HTML al volo.
Come funzionava:
- Browser richiede /cgi-bin/hello.cgi
- Server esegue lo script Perl
- Script genera HTML e lo stampa su stdout
- Server invia l'output al browser
Esempio CGI in Perl:
Lato client: JavaScript e PHP
Discorso analogo con le Java Server Pages (.jsp) su cui qualcuno di vuoi probabilmente avrà ancora
la (s)fortuna di lavorare...
Ma tutto questo era piuttosto grossolano e macchinoso, specie per le connessioni dell'epoca (le
vecchie 56k dial up a pagamento... nel migliore dei casi).
Ben presto si scelse di far girare il
codice per l'interattività lato client,
direttamente nel browser per ridurre i
tempi di risposta.
Così nel 1995 nacque PHP, da Java si
staccò Javascript, nell'HTML si
cominciarono a vedere tag <script> per
inserire logiche applicative nelle pagine

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 6: Lezione 2


UNITA’ FORMATIVA
Competenze informatiche/digitali
Quando il web parla chiaro
In questa lezione, analizzeremo e metteremo alla prova il più
diffuso formato di rappresentazione degli oggetti scambiati
SOAP (Simple Object Access Protocol) è un protocollo
più vecchio e rigido, basato interamente su XML.
Definisce un formato di messaggio molto strutturato
con envelope, header e body.
Include funzionalità enterprise come WS-Security per
sicurezza avanzata, WS-ReliableMessaging per
garantire la consegna, e WSDL per descrivere
formalmente il servizio.
È verboso e complesso, ma ancora utilizzato in
contesti enterprise legacy, bancari e governativi dove
questi standard sono richiesti.
Esempio di chiamata SOAP
GraphQL rappresenta un cambio di paradigma: invece di
endpoint multipli che restituiscono strutture fisse,
espone un singolo endpoint dove il client specifica
esattamente quali dati necessita attraverso un
linguaggio di query. Ad esempio, posso richiedere solo
nome ed email di un utente, evitando di ricevere 20
campi inutili. Risolve i problemi di over-fetching e underfetching di REST, ma introduce complessità nel caching
e richiede più lavoro di setup iniziale.
Esempio di chiamata GraphQL
JSON è il formato di scambio dati più utilizzato nelle
API RESTful moderne.
È leggero, human-readable e nativamente supportato
La sintassi è semplice, e usa una struttura chiavevalore separati da ":" e da "," con tipi di dato limitati ma
• String: "nome" : "Mario"
• Number: "età" : 30
• Boolean: "attivo" : true
• Null: "telefono" : null
• Array: "tags" : ["fiction", "thriller"]
• Object: "indirizzo" : {"città": "Roma", "cap": "00100"}
Vediamo che JSON supporta nativamente array
e oggetti, mentre XML richiede una struttura più
Oggetto Json: collezione non ordinata di coppie
Array: lista ordinata di valori.
• Chiavi sempre tra doppi apici: "nome"
• Niente virgola dopo ultimo elemento: [1, 2, 3]
• Solo doppi apici per stringhe: "testo"
• Nomenclatura case-sensitive
JSON è lo standard per le API REST per la sua semplicità e
Non è l'unico formato di rappresentazione delle risorse: si
trovano comunemente anche XML o HTML.
Vantaggi e Svantaggi di JSON
Vantaggi di JSON
Svantaggi di JSON
• Leggero (meno verboso di XML)
• Facile da leggere e scrivere
• Supporto nativo in JavaScript
• Parsing veloce
• Supportato da tutti i linguaggi moderni
• No date native (si usano stringhe ISO 8601)
• No tipi complessi (tutto è stringa, numero o
Esercizio: oggetto libro
Costruiamo ora la rappresentazione JSON di un array di oggetti "libro" che abbiano le
seguenti proprietà:
• titolo: string
• genere: string
• autore: string
• editore: string
• numeroPagine: number
PRO: organizzare i libri secondo il genere (suggerimento: ci sarà un oggetto contenitore per i
generi, e ogni genere sarà un oggetto che conterrà un array di libri).
Usiamo un validatore JSON online per controllare il risultato: https://jsonlint.com/
Esercizio: libreria
Ora usiamo l’array appena creato all’interno di un
oggetto “libreria” così composto:
• indirizzo: string
• catalogoLibri: libro[ ]
PRO: l’indirizzo diventa un oggetto con I campi via, citta,
Controlliamo sempre il risultato sul validatore JSON
https://jsonlint.com/
Panoramica Request e Response
Vediamo dunque come si compongono i due oggetti cardine del protocollo HTTP e di tutta la
comunicazione REST: request e response.
1) il client web (browser, p.es. Chrome) invia al server web (p.es. Apache) una richiesta (REQUEST), ad

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 7: Lezione 3


UNITA’ FORMATIVA
Competenze informatiche/digitali
Docente: Fabio Abbà
Per API (Application Programming Interface) si intende un insieme di regole e convenzioni che permette a
due software di comunicare tra loro: è la lingua comune che entrambi parlano e capiscono, il «menu» del
ristorante che ci dice cosa c’è a disposizione.
Conoscendo la struttura delle API a disposizione, il client invia una richiesta che potrà essere compresa
dal server, senza bisogno di conoscerne il suo funzionamento interno.
Facciamo l’esempio dell’API di un servizio meteo: essa sarà costituita
dall’insieme di endpoint (URI) correlati che espongono le risorse fornite da un
• https://weather.api.com/current
• https://weather.api.com/forecast?days=3
• https://weather.api.com/air-quality
Pianificazione di
Per creare un'API è utile delinearne
preventivamente la struttura, ricordando che
l'architettura REST prevede che gli endpoit da
chiamare rispecchino le risorse (oggetti) a
disposizione e facciano uso dei verbi HTTP.
Qualche convenzione di nomenclatura sarà di
Convenzioni di Nomenclatura
Chiarezza e coerenza negli endpoint
Per cominciare, è importante che si seguano delle convenzioni uniformi in tutto l'applicativo;
questo rende l'esperienza più prevedibile ed intuitiva per l'utente ma anche per lo sviluppatore
che deve metterci mano (specialmente se non è stato lui a scrivere quel codice!).
Per esempio: se abbiamo /users/{id}/orders per gli ordini di un utente, dovremmo seguire lo
stesso pattern per altre relazioni, come /users/{id}/addresses o /products/{id}/reviews
Convenzioni di Nomenclatura
Oppure, evitare di usare nomi diversi per lo stesso campo (created_at e creation_date), oppure
case diversi (created_at e createdAt).
Voi mi direte: basta un po' di buon senso!
E io vi dico che ne sono provviste molte meno persone di quelle che pensate. Ma sorvoliamo...
Per le collezioni di dati si usa il plurale (es. /products, /users); per identificare la singola risorsa si
usa comunemente il suo id usato come path variable (es. /products/123, /users/456).
Convenzioni di Nomenclatura
In questo modo si rende chiaro che si agisce andando a cercare un dettaglio all'interno della
Beninteso: la struttura può annidarsi ulteriormente, ad es.
/users/456/orders/112233 → sto andando a cercare tra gli ordini dell'utente 456 quello con
il numero 112233.
La gerarchia del path di solito rispecchia la relazione tra le risorse.
Convenzioni di Nomenclatura
Altrettanto importante ai fini della chiarezza è l'uso dei verbi HTTP:
• GET /products -> ritorna la lista di utenti
• GET /products/123 -> ritorna un prodotto specifico
• POST /products -> aggiunge un nuovo prodotto (non è specificato l'id, solitamente è
aggiunto dal db)
• PUT /products/123 -> aggiorna il prodotto con id 123
• DELETE /products/123 -> elimina il prodotto con id 123
Convenzioni di Nomenclatura
Naturalmente le chiamate GET possono prevedere dei query params (?nomeParametro=valore)
per raffinare la ricerca (comunemente filtraggio, ordinamento o paginazione).
• GET /users?role=admin
• GET /products?page=2&limit=20
• GET /products?sort=field&order=asc
Infine, non è una cattiva idea usare una strategia di versionamento.
Se non abbiamo fatto un lavoro osceno destinato ad estinguersi da sè, prima o poi dovremo
aggiornare qualcosa nel nostro applicativo.
Finchè si aggiungono cose, di solito non si creano grandi problemi. Ma nel caso in cui ci fossero
eliminazioni di endpoint, campi o comunque modifiche sostanziali alle nostre API, bisognerà
prevedere un meccanismo per creare una finestra di tempo che consenta agli utenti di
aggiornare i loro sistemi.
(E, detto tra noi, non è male anche per avere un backup nel caso in cui la nuova versione fosse il
lavoro osceno di cui sopra...)
L'approccio più popolare e diffuso è
includere la versione nell'URL:
/v1/users, /v2/users, /v3/users
La versione è tipicamente subito dopo il
dominio, prima delle risorse.
facile da implementare e capire.
immediatamente visibile, e
Quindi, mettiamo insieme:
• nomenclatura uniforme
• gerarchia nel path
• uso verbi HTTP
• versionamento
Usiamo tutto questo per definire l’API “Catalogo”
dell'applicazione "libreria" che vogliamo creare.
Create le API relative alla gestione dei clienti
e degli ordini ad essi correlati.
Per comodità, assumiamo che i clienti siano

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 8: Lezione 4


UNITA’ FORMATIVA
Competenze informatiche/digitali
OpenAPI Solutions
Understanding API Standards
OpenAPI (precedentemente Swagger Specification) è uno standard industriale per descrivere API
REST in formato machine-readable (tipicamente JSON o YAML).
Definisce un formato strutturato che descrive tutti gli endpoint della nostra API, i parametri che
accettano, gli schemi dei dati in input e output, i codici di stato HTTP possibili, i metodi di
autenticazione, esempi, descrizioni testuali.
SWAGGER È L'ECOSISTEMA DI STRUMENTI
CHE IMPLEMENTA QUESTA SPECIFICA,
COMPRENDENDO EDITOR, GENERATORI DI
CODICE E INTERFACCE INTERATTIVE.
Swagger Editor è uno strumento online che
permette di scrivere e modificare specifiche
OpenAPI in modo (quasi) intuitivo.
Swagger UI fornisce un'interfaccia web
interattiva per visualizzare e testare le API.
SWAGGER CODEGEN
Swagger Codegen è un generatore automatico
di client e server che produce codice sorgente
in vari linguaggi. Accelera lo sviluppo e
garantisce coerenza tra implementazione e
documentazione API.
Vantaggi della documentazione
STANDARDIZZAZIONE
TESTING INTEGRATO
L'uso di OpenAPI garantisce
un formato universalmente
riconosciuto, facilitando la
comunicazione e
l'integrazione tra team
diversi e sistemi.
Grazie a strumenti come
Swagger, è possibile ridurre
errori manuali e mantenere
la sincronizzazione tra codice
e documentazione,
generando automaticamente
il codice necessario.
La documentazione
OpenAPI consente di
testare direttamente gli
endpoint dall'interfaccia,
rendendo il processo di
verifica più semplice e
immediato per gli
Tools aggiuntivi
Vediamo subito in pratica quanto detto.
Per documentare le API della nostra applicazione
avremo bisogno di un tool aggiuntivo che ci
semplifichino il lavoro:
• swagger-ui-express: genererà l’interfaccia a
partire da un file di configurazione (JSON in questo
caso, ma più comunemente YAML)
https://medium.com/@im_AnkitTiwari/swaggerizingyour-node-js-rest-api-a-step-by-step-guide267255bf8bbe
Cominciamo ad installare quanto serve:
E creiamo (se non l'abbiamo già fatto) una directory
"doc“ (o swagger) dove inserire il file che servirà a
generare l’interfaccia.
Questo è un esempio in
Questo è un esempio in
E' possibile dare il file .yml in
pasto a dei servizi che sulla
base di questo contenuto
creeranno automaticamente
la struttura documentata
delle API che esponiamo.
Molto però dipende dal tipo
di architettura usata.
Per quanto ci riguarda, noi useremo il file JSON
per generare l'interfaccia Swagger.
Aggiungiamo il codice necessario:
Interfaccia Swagger
Ora, se avviamo l'applicazione e andiamo sulla pagina "/api-docs", avremo a disposizione un'interfaccia che ci
mostra gli endpoint disponibili e ci permette di testarli.
Oltre all'interfaccia intuitiva, c'è un altro grande vantaggio in
questo approccio: una volta definita la struttura delle API nel file
swagger.yml (e sperando che non cambi nel frattempo!), esso
fungerà da riferimento per gli sviluppi sia lato frontend che lato

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 9: Lezione 5


UNITA’ FORMATIVA
Competenze informatiche/digitali
Sicurezza nelle
Docente: Fabio ABBA’
della sicurezza
L'argomento di oggi è della massima importanza nello
sviluppo di applicazioni web moderne.
Immaginate di costruire una casa con muri solidi e una
porta blindata, ma di lasciare la chiave sotto lo zerbino:
questa è un'applicazione che non applica standard di
sicurezza, cioè è facilmente violabile. Le vulnerabilità
possono portare a furti di dati, danni reputazionali e
perdite finanziarie.
Immaginiamo di essere in un bar affollato. Se parlo
con il mio amico a voce alta, tutti possono sentire la
nostra conversazione. Questo è HTTP: i dati
viaggiano in chiaro sulla rete, chiunque può
intercettarli e leggerli.
Ora immaginiamo di parlare in una lingua segreta
che solo io e il mio amico conosciamo. Anche se
qualcuno ascolta, non capisce nulla.
Questo è HTTPS: i dati sono crittografati.
HTTPS e i suoi vantaggi
HTTPS è la versione sicura del protocollo HTTP. Aggiunge un livello di crittografia chiamato TLS (Transport
Layer Security), il successore di SSL.
La crittografia assicura che i dati
scambiati tra client e server siano
cifrati. Se un malintenzionato
intercettasse la comunicazione
(attacco "Man-in-the-Middle"),
vedrebbe solo dati incomprensibili.
L'integrità garantisce che i dati
non vengano alterati durante il
trasferimento. Se un attaccante
tentasse di modificare i dati, il
sistema rileverebbe l'anomalia e
respingerebbe la
L'autenticazione verifica che le
comunicazioni avvengano con il
server corretto. Utilizzando
certificati digitali, si assicura che
gli utenti si connettano solo a
fonti affidabili.
Autenticazione e
Un altro pilastro della sicurezza delle applicazioni
web è la combinazione di autenticazione (chi sei?) e
autorizzazione (cosa puoi fare?).
La strategia più comune e adatta alle API REST
stateless è quella basata sui JSON Web Tokens
Un JSON WebToken è una stringa che contiene
(codificate) le informazioni che riguardano l'utente
(idenificativo, ruolo/permessi), specifiche del token
(emissione e scadenza), ed altre info customizzabili
a seconda del contesto applicativo.
Tali informazioni sono firmate lato server secondo la
specifica JSON Web Signature(JWS), quindi il
server è in grado di riconoscere se sono state
generate da lui o meno.
Autenticazione JWT
Fondamenti del processo di autenticazione
L'utente invia le sue credenziali
(es. email e password) a un
endpoint come “/auth/login”.
Il server verifica le credenziali;
se sono valide, il server crea un
JWT, ossia una stringa
codificata che contiene
informazioni sull'utente (es. ID,
ruolo) e una firma digitale.
Il server invia il token JWT al
client, permettendo così
all'utente di accedere a risorse
Autenticazione JWT
Gestione delle richieste sicure
Richieste Autenticate
Risposta al Client
Il client deve includere il token JWT
nell'header Authorization per tutte le
richieste a endpoint protetti,
garantendo che solo gli utenti

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 10: JWT e autenticazione


Una delle esigenze più comuni del WEB è quella di restringere l’accessibilità di una o
più pagine di un applicazione web ai soli utenti autenticati o addirittura ad una
ristretta cerchia di utenti (ad es. agli utenti admin). Questa esigenza si presenta
anche nel mondo delle API. Nella prima parte di questo articolo spiegherò il principio
su cui si basa JWT mentre nella seconda parte scriveremo una semplice
implementazione di autenticazione Spring su JWT.
AUTENTICAZIONE STATELESS
Un servizio REST dovrebbe essere per definizione stateless: ovvero le interazioni tra
client e server devono essere senza stato, rispettando la comunicazione stateless
nativa del protocollo HTTP. La gestione dello stato (se necessaria) avviene sul client,
ottimizzando le prestazioni del server che non deve curare lo stato. L’approccio
stateless di un architettura RESTful rende quindi inappropriato l’utilizzo dei cookie di
sessione per il meccanismo di autenticazione.
La soluzione di autenticazione Stateless piu’ semplice è l’autenticazione BASIC: ad
ogni chiamata del client viene passato un token in un header http contenente le
credenziali in modo che il server ad ogni chiamata possa autenticare il client. In
questo modo mantengo stateless il mio backend RESTful ma ottengo un overhead
dovuto al fatto che il server debba autenticare ad ogni richiesta il client. Questa
soluzione non è quindi adatta a sistemi di produzione: immaginiamo di dover rieseguire ad ogni richiesta le query di autenticazione sul nostro db su un sistema con
migliaia di utenti online nel singolo istante! Una soluzione completamente
Stateless, scalabile e con nessuno overhead è quella oggetto di questo articolo:
JWT (JSON WEB TOKEN)
Prima di analizzare il meccanismo di autenticazione su JWT cerchiamo innanzitutto
di capire cos’ è un JSON WEB TOKEN: abbreviato più comunemente con l acronimo
di JWT. JWT è uno standard che viene usato per “regolare” le richieste tra due parti.
JSON Web Token è un security token (una stringa) che agisce come un container
per le claims degli user. I claims sono informazioni di un utente: chi è l’utente loggato
(e altre info di contorno: ad es mail, nome, cognome), scadenza di un token (quindi
scadenza dell’autenticazione dell’utente), privilegi dell’utente (è un admin o un
normale utente) ed altre info customizzabili a seconda del contesto applicativo . Tali
informazioni sono firmate lato server secondo la specifica JSON Web Signature
(JWS), quindi il server è in grado di riconoscere se sono state generate da lui o
meno. Riportiamo un esempio di token JWT:
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImF1ZGllbmNlIjoid2ViIiwicm9sZXMiOlsiUk9MRV
9BRE1JTiIsIlJPTEVfVVNFUiJdLCJpc0VuYWJsZWQiOnRydWUsImV4cCI6MTUxMjk3NTQ1MCwiaWF0IjoxN
TEyOTY4MjUwMjMwfQ.J49qG_yi0yMZP4K2PWddTNR7QyUloAR7qj_3QtLL_6A
Come si evince dall’esempio identifichiamo 3 parti in un token JWT
- Header : Se decodifichiamo la prima parte del token scopriamo che si riferisce ad
un json che contiene le due voci “typ” e “alg”. Il primo ha come valore sempre
“JWT”, mentre il nodo “alg” contiene il nome dell’algoritmo usato per il token.
Nell’immagine sopra è stato usato l’algoritmo “HMAC-SHA256”.
- Payload : La seconda parte del token è il corpo vero e proprio che contiene dei
dati “variabili” in base al contesto in formato json e codificati in base64. Nel nostro
esempio il payload decodificato è
"sub": "admin",
"isEnabled": true,
"exp": 1512975450,
"iat": 1512968250230
JWT propone dei campi “standard” da utilizzare nel payload (es: sub, audience, exp
e iat) ma il programmatore può inserire proprietà aggiuntive (vedi isEnabled e roles
da me definiti e non contemplati nei clams standard). Andando ad analizzare il json
del body possiamo interpretare dal token le seguenti info:
● utente admin (claim sub)
● ha come target il web (claim aud)
● ruoli utente ROLE_ADMIN, ROLE_USER (claim roles)
● utente abilitato (claim isEnabled)
info relative al momento in cui è stato creato il token (iat) e sulla data di
scadenza (exp): momento in cui tale token non sarà più ritenuto valido dal
- Signature: La terza parte di un token è la firma che non è altro che il risultato di
una funzione hash 256 che prende in input la codifica base64 dell’header
concatenandola con un punto alla codifica base64 del payload, il tutto codificato
con la nostra “chiave segreta” che solo il server conosce.
Con questa piccola introduzione sui JSON WEB TOKEN capiamo subito che questi
token possono esser un ottimo modo per trasportare all’interno di ogni richiesta
HTTP info legate all’autenticazione di un utente in modo totalmente sicuro: il server
grazie al campo signature è in grado di capire che tali info sono state generate da lui
grazie alla firma e che quindi garantiscono che tale richiesta è da considerarsi
relativa ad un utente autentificato.
FLUSSO LOGICO DI AUTENTICAZIONE JWT
Ora che abbiamo introdotto i JSON WEB TOKEN descriverò come possono essere
utilizzati per implementare il meccanismo di autenticazione in un backend RESTful. Il
meccanismo di autenticazione JWT può essere riassunto in questo schema.
1. Il client, utilizzando l’endpoint di login, invia le proprie credenziali al server per
2. Il server verifica se le credenziali postate sono corrette. In caso positivo
costruisce un token jwt utilizzando la chiave segreta e inserendo nel payload
del token le informazioni utente e le data di creazione e scadenza del token;
Tale token verrà firmato e autentificato con la sua chiave privata ( importante
solo il server deve conoscere la chiave privata )
3. tale token viene inviato nella risposta all’interno di un header http ( nella
implementazione che proporremo sotto utilizzeremo l header http X-auth)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 11: JWT vs HttpOnly cookie


JWT vs HttpOnly cookie
1. JWT in header
Scenario tipico:
● Login con POST /login → il server genera un JWT (spesso firmato con HS256)
Il client (SPA/JS) salva il token in:
○ localStorage oppure
○ sessionStorage
● Ad ogni richiesta → header:
Authorization: Bearer <jwt>
Problema principale
Se il sito ha anche solo una vulnerabilità XSS, uno script malevolo può fare:
localStorage.getItem("token") // oppure sessionStorage
e rubarsi il JWT.
A quel punto il token è usabile ovunque, da chiunque lo possieda.
● JWT molto lunghi
● scadenza troppo ampia
troppe informazioni dentro il payload
● nessun meccanismo di rotazione / revoca
Risultato: se il token viene rubato, l’attaccante è loggato “per sempre” finché il token non
2. Cosa cambia con HttpOnly cookie
L’idea moderna è:
1. Il server, dopo il login, NON ti dà il JWT da salvare nel JS.
Invece, risponde con un Set-Cookie:
Set-Cookie: access_token=<jwt-o-id-sessione>;
SameSite=Strict;
○ salva il cookie
lo rimanda automaticamente in ogni richiesta verso quel dominio.
Tu dal frontend non fai più:
Authorization: Bearer ...
ma semplicemente chiami le API (fetch/axios) e il browser allega i cookie.
Perché è più sicuro?
Flag HttpOnly → il cookie NON è leggibile da JavaScript:
document.cookie // non mostra il cookie HttpOnly
Quindi, anche se hai XSS, l’attaccante non può rubare il token semplicemente
leggendolo dal client.
● Flag Secure → il cookie viaggia solo su HTTPS (non in chiaro).
● Flag SameSite:
○ Strict o Lax riducono i rischi di CSRF, cioè richieste da altri siti che usano
3. Ma allora JWT sono “insicuri”?
Non è che JWT siano insicuri in sé.
Problemi comuni:
1. Uso improprio:
○ Token lunghissimi, con un sacco di dati sensibili.
○ Nessuna rotazione.
○ Nessuna revoca server-side (“se ho un JWT valido posso bypassare tutto”).
2. Storage insicuro nel frontend:
○ localStorage + XSS = furto del token.
3. Assenza di controlli extra:
○ niente IP binding, niente device binding, niente controllo su user-agent.
Spesso oggi si consiglia di:
● usare JWT come access token a breve durata
tenerli nel backend o in cookie HttpOnly, non nel JS leggibile.
4. Flusso moderno tipico (semplificato) per le tue
5. Confronto didattico: Header JWT vs HttpOnly cookie
Puoi sintetizzare così ai ragazzi:
JWT in header + localStorage
JWT/Session in HttpOnly Cookie
Lettura JS ✅ sì (localStorage)
❌ no (HttpOnly)
alto (token rubabile)
più basso (token non leggibile da
Rischio CSRF basso (token in header
più alto se SameSite è None
client controlla header
browser gestisce i cookie da solo
Messaggio importante da passare:
Non è che “JWT sono il male” e “cookie sono il bene”.
Il tema è dove tieni il token e come gestisci XSS/CSRF.
1. Implementre Http CLient Only
npm install cookie-parser
3. Modifica di server.js per usare i cookie
In server.js, aggiungi cookie-parser e (se usi una SPA) abilita CORS con credenziali.
server.js aggiornato (versione semplificata)
// agganciamo le librerie che abbiamo installato con node
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');
const cors = require('cors');
const cookieParser = require('cookie-parser'); // <--- NEW
// dichiariamo su che porta risponderà il server web

*[Contenuto troncato — vedi file originale per dettagli completi]*


---
*Totale: 11 sessioni generate il 02/07/2026*