# API RESTful — Quaderno di Appunti

> **Materia:** 12_RESTful_API
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [1 - Introduzione a REST](#1---introduzione-a-rest)
2. [2 - JSON request e response](#2---json-request-e-response)
3. [3 - Progettare unAPI REST](#3---progettare-unapi-rest)
4. [4 - Swagger OpenAPI - Sempl](#4---swagger-openapi---sempl)
5. [5 - HTTPS JWT auth](#5---https-jwt-auth)
6. [Guida Essenziale alle API RESTful](#guida-essenziale-alle-api-restful)
7. [index](#index)
8. [ISTRUZIONI MUSICLAB](#istruzioni-musiclab)
9. [JWT e autenticazione](#jwt-e-autenticazione)
10. [JWT vs HttpOnly cookie](#jwt-vs-httponly-cookie)
11. [script libri](#script-libri)
12. [Test RESTful API Gruppi](#test-restful-api-gruppi)

---

# 1 - Introduzione a REST

**File:** `1 - Introduzione a REST.pdf`
**Tipo:** `.pdf`
**Dimensione:** 2414.8 KB
**Ultima modifica:** 02/07/2026 09:12

---

DOCENTE Fabio ABBA’
UNITA’ FORMATIVA Competenze informatiche/digitali
ARGOMENTO RESTful API


Docente: Fabio Abbà
Quattro 
chiacchiere tra 
macchine


Comunicazione 
e interazione
Per comprendere la ragione di fondo di questo corso è 
utile fare un parallelo con ciò che facciamo tutti i giorni per 
interagire: parlare.
Perchè ci sia una buona comunicazione occorrono alcuni 
elementi:
 - chi fa una richiesta (client)
 - chi ascolta (server)
 - un canale di trasmissione della voce/richiesta 
(web/http)
 - una lingua comune (SOAP , REST , GraphQl, ecc.)

Distinzione tra 
Client e Server
Questo assicura che ci possa essere uno scambio 
efficace di informazioni tra due elementi.
Nel caso dei servizi web, è ormai prassi consolidata che 
ci sia una netta distinzione di ruoli tra client, che richiede 
e visualizza i dati, e server, che recupera ed invia i dati 
richiesti.
Questo ha anche il vantaggio di disaccoppiare le 
tecnologie utilizzate (p.es. è possibile modificare l'intera 
architettura di persistenza dati lato server in maniera 
completamente invisibile, o trasparente, per il client) e 
quindi permettere la comunicazione tra sistemi e 
linguaggi diversi.

ARPANET
ARPANET , sviluppata negli anni '60, 
era la prima rete di computer, 
collegando istituzioni militari e 
università, ponendo le basi per la 
comunicazione digitale moderna.
TCP/IP Nascita del Web
Il protocollo TCP/IP , adottato nel 
1983, ha sostituito NCP , permettendo 
la comunicazione tra diversi sistemi 
operativi e migliorando l'affidabilità 
del trasferimento dati.
Con la creazione di HTML e URL, 
Tim Berners-Lee ha dato vita al 
World Wide Web, rivoluzionando 
l'accesso alle informazioni e 
cambiando il panorama digitale per 
sempre.
Protocollo HTTP
Il protocollo HTTP è stato introdotto 
negli anni '90, consentendo la 
trasmissione di contenuti web. Ha 
trasformato il modo in cui gli utenti 
interagiscono con le informazioni 
online.
Timeline delle origini


HTML: Il 
linguaggio 
fondamentale 
del web
Hyper T ext Markup Language, creato da Tim Berners-
Lee, è un linguaggio di markup essenziale che definisce 
la struttura delle pagine web. Permette di posizionare e 
formattare contenuti visibili nei browser per l'utente 
finale.

Richieste HTTP
Esempio del primo HTTP , basata su due soli 
oggetti: request e response.
Ma con l'evoluzione del web, è nata l'esigenza di fornire 
all'utente dei contenuti dinamici, ossia che si adattassero 
alle sue azioni o che potessero modificare il contesto 
applicativo: risultati di ricerca, form di contatto, pagine 
personalizzate.
Si giunge dapprima ad un'interattività lato server: Common 
Gateway Interface permetteva al server web di eseguire 
programmi esterni per generare HTML al volo.

Esempio di 
codice CGI in 
Perl
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
Così nel 1995 nacque PHP , da Java si 
staccò Javascript, nell'HTML si 
cominciarono a vedere tag <script> per 
inserire logiche applicative nelle pagine 
web.

Evoluzione verso le Web Application
E via via, andando avanti, da un insieme di pagine interconnesse, poi di pagine dinamiche, si arriva al 
concetto di Web Application, e anzi, di Single Page Web Application: interi applicativi che girano nel 
browser dell'utente in costante comunicazione con il server.
Roy Fielding, uno dei principali autori della specifica HTTP/1.1, ha definito REST (Representational 
State T ransfer) nella sua dissertazione di dottorato del 2000 presso l'Università della California.
Fielding, avendo lavorato direttamente su HTTP , aveva osservato cosa funzionava e cosa no nel 
protocollo che alimentava il web. La sua intuizione fu: perché inventare nuovi protocolli quando HTTP 
stesso, ben utilizzato, poteva essere la soluzione?
Quindi non inventò (quasi) nulla di nuovo, ma identificò e formalizzò i vincoli architetturali che rendono il 
web scalabile.

Le risorse e i 
loro URI
Fielding ha introdotto il concetto che tutto nel web 
può essere modellato come risorsa identificata da 
un URI. Non "servizi" o "procedure remote", ma 
RISORSE (qualsiasi elemento oggetto di elaborazione)
Un utente è una risorsa:  /users/123
I suoi ordini sono una risorsa:  /users/123/orders
Un ordine specifico:  /orders/456
Questo cambio di prospettiva ha reso le API più 
intuitive e prevedibili.

Stateless Design 
Stateless: ogni richiesta deve contenere tutte le 
informazioni necessarie. Il server non mantiene sessioni tra 
richieste.
Questo implica che il client ha la responsabilità di 
mantenere lo stato della sessione e le informazioni di 
autenticazione.
Perché? Scalabilità. Se il server non deve ricordare lo stato 
delle conversazioni, rimangono più risorse libere e le 
richieste sono gestibili anche da server diversi.

HATEOAS
HATEOAS (Hypermedia As The Engine Of Application State) è 
il vincolo più avanzato (e meno implementato) di REST . L'idea è 
che la risposta dovrebbe contenere link alle azioni successive 
possibili.

I 6 comandamenti REST
Per garantire una piena interoperabilità tra sistemi, le API sviluppate con l’architettura REST seguono questi 6 
principi:
• Interfaccia uniforme (risorse identificate da URI, metodi HTTP , 
rappresentazione oggetti JSON/XML/…, eventualmente HATEOAS)
• Disaccoppiamento client/server (portabilità interfaccia)
• Comunicazioni Stateless (richieste autoconsistenti)
• Cacheability (possibilità di memorizzare le risposte in cache)
• Architettura a strati (possibilità di livelli intermedi, proxy , gateway…)
• Codice on demand (OPZIONALE; il server può inviare applet o script 
per estendere le funzionalità dell’applicazione)

Pratica con 
PokeAPI
Ora mettiamo in pratica quanto appreso 
esplorando la PokeAPI. Utilizzeremo questa API 
RESTful per effettuare richieste e ricevere dati sui 
Pokémon. 
https://pokeapi.co/

Verbi HTTP: le azioni 
fondamentali di REST
Ok, ora aggiungiamo ancora qualche informazione.
I verbi HTTP (o metodi HTTP) definiscono il tipo di 
operazione che vogliamo eseguire su una risorsa. Sono il 
"vocabolario" con cui comunichiamo con un'API REST .
Il protocollo ne prevede 5 principali:
•  GET
• POST
• PUT
• PATCH
• DELETE

I 5 verbi principali
GET - Recupera una risorsa o collezione
• Esempio: `GET /users/123` → ottiene i dati dell'utente 123
• È "safe" (non modifica nulla) e "idempotente" (chiamarlo più volte 
dà lo stesso risultato)
POST - Crea una nuova risorsa
• Esempio: `POST /users` con dati nel body → crea un nuovo 
utente
• Non è idempotente: ogni chiamata crea una nuova risorsa
PUT - Sostituisce completamente una risorsa esistente
• Esempio: `PUT /users/123` → aggiorna tutti i campi dell'utente 
123
• È idempotente: ripetere la stessa richiesta non cambia il risultato
GET
POST
PUT

I 5 verbi principali
PATCH - Aggiorna parzialmente una risorsa
• Esempio: `PATCH /users/123` con 
       `{"email": "nuovo@email.com"}` → modifica solo l'email
• Invia solo i campi da cambiare, non l'intera risorsa
DELETE - Rimuove una risorsa
• Esempio: `DELETE /users/123` → cancella l'utente 123
• È idempotente: dopo la prima cancellazione, la risorsa non 
esiste più
PATCH
DELETE

Perchè sono 
importanti
I verbi HTTP rendono l'API prevedibile e intuitiva.
Invece di avere URL come `/getUserById` o `/deleteUser`, 
usiamo sempre lo stesso pattern: il verbo indica l'azione, 
l'URL indica la risorsa.
Questo è il cuore della filosofia REST .
Riprendendo l’analogia della comunicazione umana, 
questo è il contenuto della comunicazione, ciò che viene 
effettivamente richiesto.

E’ ora di testare!
Ok, per il momento basta con la teoria, è ora di mettere le 
mani in pasta.
Lo faremo utilizzando un tool utilizzo molto comune:
• Postman (https://www.postman.com)
E alcune API pubbliche:
https://swapi.dev
https://jsonplaceholder.typicode.com

Grazie per 
l’attenzione!
Docente: Fabio Abbà fabio.abba@tc-web.it
Via Giovanni Schiaparelli 14,
10148 – Torino (TO)
E-mail: info@tc-web.it
Tel: 011 0466685
Credits: Franco Grivet
franco.grivet@tc-web.it


---

# 2 - JSON, request e response

**File:** `2 - JSON, request e response.pdf`
**Tipo:** `.pdf`
**Dimensione:** 2380.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE Fabio ABBA’
UNITA’ FORMATIVA Competenze informatiche/digitali
ARGOMENTO RESTful API


Quando il web parla chiaro
REST e 
JSON
Fabio Abbà
Docente


In questa lezione, analizzeremo e metteremo alla prova il più 
diffuso formato di rappresentazione degli oggetti scambiati 
sul web: JSON.
Ripasso e 
obiettivi


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
SOAP: il 
veterano


Esempio di chiamata SOAP
Request Response

GraphQL rappresenta un cambio di paradigma: invece di 
endpoint multipli che restituiscono strutture fisse, 
espone un singolo endpoint dove il client specifica 
esattamente quali dati necessita attraverso un 
linguaggio di query. Ad esempio, posso richiedere solo 
nome ed email di un utente, evitando di ricevere 20 
campi inutili. Risolve i problemi di over-fetching e under-
fetching di REST, ma introduce complessità nel caching 
e richiede più lavoro di setup iniziale.
GraphQL: il 
query language 
moderno


Esempio di chiamata GraphQL
Request Response

JSON è il formato di scambio dati più utilizzato nelle 
API RESTful moderne.
È leggero, human-readable e nativamente supportato 
da JavaScript.
La sintassi è semplice, e usa una struttura chiave-
valore separati da ":" e da "," con tipi di dato limitati ma 
sufficienti:
• String: "nome" : "Mario"
• Number: "età" : 30
• Boolean: "attivo" : true
• Null: "telefono" : null
• Array: "tags" : ["fiction", "thriller"]
• Object: "indirizzo" : {"città": "Roma", "cap": "00100"}
REST e JSON


Esempio di 
JSON
Vediamo che JSON supporta nativamente array 
e oggetti, mentre XML richiede una struttura più 
complessa.
Oggetto Json: collezione non ordinata di coppie 
chiave-valore.
Array: lista ordinata di valori.

• Chiavi sempre tra doppi apici: "nome" 
  non 'nome' 
• Niente virgola dopo ultimo elemento: [1, 2, 3] 
  non [1, 2, 3,] 
• Solo doppi apici per stringhe: "testo" 
  non 'testo’ 
• Nomenclatura case-sensitive
Regole 
Sintattiche
JSON è lo standard per le API REST per la sua semplicità e 
universalità.
Non è l'unico formato di rappresentazione delle risorse: si 
trovano comunemente anche XML o HTML.

• No commenti                                                           
• No date native (si usano stringhe ISO 8601)
• No tipi complessi (tutto è stringa, numero o 
booleano)
• Leggero (meno verboso di XML)              
• Facile da leggere e scrivere                        
• Supporto nativo in JavaScript                    
• Parsing veloce                                                  
• Supportato da tutti i linguaggi  moderni
V antaggi e Svantaggi di JSON
Vantaggi di JSON Svantaggi di JSON


Costruiamo ora la rappresentazione JSON di un array di oggetti "libro" che abbiano le 
seguenti  proprietà:
• titolo: string
• genere: string
• autore: string
• editore: string
• numeroPagine: number
PRO: organizzare i libri secondo il genere (suggerimento: ci sarà un oggetto contenitore per i 
generi, e ogni genere sarà un oggetto che conterrà un array di libri).
Usiamo un validatore JSON online per controllare il risultato: https://jsonlint.com/
Esercizio: oggetto libro

Ora usiamo l’array appena creato all’interno di un 
oggetto “libreria” così composto:
• nome: string
• indirizzo: string
• catalogoLibri: libro[ ]
PRO: l’indirizzo diventa un oggetto con I campi via, citta, 
regione.
Controlliamo sempre il risultato sul validatore JSON
https://jsonlint.com/
Esercizio: libreria


Vediamo dunque come si compongono i due oggetti cardine del protocollo HTTP e di tutta la 
comunicazione REST: request e response.
1) il client web (browser, p.es. Chrome) invia al server web (p.es. Apache) una richiesta (REQUEST), ad 
esempio inserendo nella barra del browser un indirizzo; parte una richiesta verso il server che contiene 
tre parti: verb/method (GET, POST, etc) , headers (content lenght: 10) , content : {"requestContent": 
“Ciao mondo”}
Panoramica Request e Response

2) il server web invia al client la risposta (RESPONSE)  che contiene tre parti: status code (1xx, 2xx, 
3xx,4xx,5xx ) , headers (content type: text ) , content : {"responseContent": “Ciao mondo”}
Panoramica Request e Response

Analisi della Request 
(metodi)
VERB/METHOD : sono i metodi HTTP di cui abbiamo già parlato in 
precedenza

Analisi della Request 
(headers)
HEADERS : metadati che possono contenere informazioni sulla request 
(possiamo crearne anche di custom)

Analisi della Request 
(body)
CONTENT: quello che mandiamo al server; sono informazioni che possono 
servire al server (ad esempio dati presenti in un form , un oggetto JSON, un 
file da uploadare...)

La chiamata GET ha una particolarità, ossia l'utilizzo 
dei query parameters: essi sono una parte dell'URL 
che permette di passare informazioni aggiuntive al 
server in una richiesta HTTP.
Si trovano dopo il simbolo ? nell'URL e sono formattati 
come coppie chiave=valore, separati da &:
Query 
Parameters
http://api.example.com/books ? category=fiction
& price_max=50 & sort=title

Analisi della Response: 
(codici di stato)
STATUS CODE: un codice che indica lo stato della risposta (tutto ok, risorsa non 
trovata , errore ). I codici sono predefiniti 
(https://it.wikipedia.org/wiki/Codici_di_stato_HTTP)
Passiamo ora alla Response.

Codici Informativi:  1xx
Indicano che la richiesta è stata ricevuta e il server sta continuando a elaborarla.
• 100 Continue: La richiesta è in corso.
• 101 Switching Protocols: Il server sta cambiando protocollo come richiesto 
dal client.
• 102 Processing: La richiesta è stata ricevuta e il server sta elaborando, ma 
non ha ancora una risposta disponibile.
Analisi della Response: 
(codici di stato)

Successo:  2xx
Indicano che la richiesta è stata ricevuta, compresa e accettata.
• 200 OK: La richiesta è andata a buon fine.
• 201 Created: La richiesta ha portato alla creazione di una nuova risorsa.
• 204 No Content: La richiesta è stata elaborata, ma non ci sono contenuti da 
restituire.
• 206 Partial Content: Solo una parte della risorsa è stata restituita 
Analisi della Response: 
(codici di stato)

Analisi della Response: 
(codici di stato)
Codici di Redirect:  3xx
Indicano che il client deve eseguire ulteriori azioni per completare la richiesta.
• 300 Multiple Choices: Ci sono più opzioni per la risorsa richiesta.
• 301 Moved Permanently: La risorsa è stata spostata permanentemente a un 
nuovo URI.
• 302 Found: La risorsa è stata trovata, ma è temporaneamente disponibile 
altrove.

Analisi della Response: 
(codici di stato)
Errore lato client:  4xx
Indicano che c'è stato un errore nella richiesta del client.
• 400 Bad Request: La richiesta non può essere elaborata a causa di sintassi 
errata.
• 401 Unauthorized: La richiesta richiede autenticazione.
• 403 Forbidden: Il server ha compreso la richiesta, ma rifiuta di autorizzarla.
• 404 Not Found: La risorsa richiesta non è stata trovata.

Analisi della Response: 
(codici di stato)
Errore lato server:  5xx
Indicano che il server ha incontrato un errore o è incapace di gestire la richiesta.
• 500 Internal Server Error: Errore generico del server.
• 502 Bad Gateway: Il server ha ricevuto una risposta non valida da un altro 
server.
• 503 Service Unavailable: Il server non è disponibile per il momento.
• 504 Gateway Timeout: Il server non ha ricevuto una risposta in tempo da un 
altro server..

Analisi della Response: 
(headers)
HEADERS: metadati che possono contenere informazioni sulla response 
(possiamo crearne anche di custom)

Analisi della Response: 
(body)
CONTENT: il contenuto che il server restituisce al client (solitamente in formato 
JSON)

Cookies
C’è infine un altro tipo di dati che spesso viene creato dal server e memorizzato sul client tramite il 
browser: i COOKIES.
I cookies sono piccoli pezzi di dati che il server invia al client e che il browser memorizza e reinvia 
automaticamente nelle richieste successive. Vengono salvati fisicamente su file, e sono utilizzati 
principalmente per mantenere sessioni e preferenze utente (lingua, tema grafico, preferenze…).
Payload (o content, o body) Headers Cookies
Contenuto principale (JSON con 
dati)
Metadati, autenticazione, controllo 
cache
Sessioni, preferenze persistenti
Inviato ogni volta esplicitamente Inviati ogni volta esplicitamente Memorizzati dal browser e inviati 
automaticamente

Ora usiamo gli oggetti che abbiamo creato per creare 
un semplice server node che esponga delle API 
(Application Programming Interface) per gestire la 
nostra libreria.
Ci serviranno:
• un IDE (Visual Studio Code)
• Node.js + Express
Esercitazione 
finale


TOOLS:
• Node.js (https://nodejs.org/docs)
• Express (https://expressjs.com)
• Postman (https://www.postman.com)
CORSI E TUTORIAL:
• MDN Web Docs 
(https://developer.mozilla.org/en-
US/docs/Web/HTTP)
• RESTful API Design (https://restfulapi.net)
Risorse utili


Grazie per 
l’attenzione!
Docente: Fabio Abbà fabio.abba@tc-web.it
Via Giovanni Schiaparelli 14,
10148 – Torino (TO)
E-mail: info@tc-web.it
Tel: 011 0466685
Credits: Franco Grivet
franco.grivet@tc-web.it


---

# 3 - Progettare un’API REST

**File:** `3 - Progettare un’API REST.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1373.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE Fabio ABBA’
UNITA’ FORMATIVA Competenze informatiche/digitali
ARGOMENTO RESTful API


Docente: Fabio Abbà
Creare 
un’API REST


Definizioni
Per API (Application Programming Interface) si intende un insieme di regole e convenzioni che permette a 
due software di comunicare tra loro: è la lingua comune che entrambi parlano e capiscono, il «menu» del 
ristorante che ci dice cosa c’è a disposizione.
Conoscendo la struttura delle API a disposizione, il client invia una richiesta che potrà essere compresa 
dal server, senza bisogno di conoscerne il suo funzionamento interno.
Facciamo l’esempio dell’API di un servizio meteo: essa sarà costituita 
dall’insieme di endpoint (URI) correlati che espongono le risorse fornite da un 
servizio:
• https://weather.api.com/current
• https://weather.api.com/forecast?days=3
• https://weather.api.com/air-quality


Pianificazione di 
un’API
Per creare un'API è utile delinearne 
preventivamente la struttura, ricordando che 
l'architettura REST prevede che gli endpoit da 
chiamare rispecchino le risorse (oggetti) a 
disposizione e facciano uso dei verbi HTTP . 
Qualche convenzione di nomenclatura sarà di 
aiuto.

3
Convenzioni di Nomenclatura
Chiarezza e coerenza negli endpoint
Per cominciare, è importante che si seguano delle convenzioni uniformi in tutto l'applicativo; 
questo rende l'esperienza più prevedibile ed intuitiva per l'utente ma anche per lo sviluppatore 
che deve metterci mano (specialmente se non è stato lui a scrivere quel codice!).
Per esempio: se abbiamo /users/{id}/orders per gli ordini di un utente, dovremmo seguire lo 
stesso pattern per altre relazioni, come /users/{id}/addresses o /products/{id}/reviews

4
Convenzioni di Nomenclatura
Oppure, evitare di usare nomi diversi per lo stesso campo (created_at e creation_date), oppure 
case diversi (created_at e createdAt).
Voi mi direte: basta un po' di buon senso!
E io vi dico che ne sono provviste molte meno persone di quelle che pensate. Ma sorvoliamo...
Per le collezioni di dati si usa il plurale (es. /products, /users); per identificare la singola risorsa si 
usa comunemente il suo id usato come path variable (es. /products/123, /users/456).

5
Convenzioni di Nomenclatura
In questo modo si rende chiaro che si agisce andando a cercare un dettaglio all'interno della 
collezione.
Beninteso: la struttura può annidarsi ulteriormente, ad es. 
/users/456/orders/112233 →  sto andando a cercare tra gli ordini dell'utente 456 quello con
il numero 112233.
La gerarchia del path di solito rispecchia la relazione tra le risorse.

6
Convenzioni di Nomenclatura
Altrettanto importante ai fini della chiarezza è l'uso dei verbi HTTP:
• GET /products -> ritorna la lista di utenti
• GET /products/123 -> ritorna un prodotto specifico
• POST /products -> aggiunge un nuovo prodotto (non è specificato l'id, solitamente è 
aggiunto dal db)
• PUT /products/123 -> aggiorna il prodotto con id 123
• DELETE /products/123 -> elimina il prodotto con id 123

7
Convenzioni di Nomenclatura
Naturalmente le chiamate GET possono prevedere dei query params (?nomeParametro=valore) 
per raffinare la ricerca (comunemente filtraggio, ordinamento o paginazione).
• GET /users?role=admin
• GET /products?page=2&limit=20
• GET /products?sort=field&order=asc

8
Versionamento
Infine, non è una cattiva idea usare una strategia di versionamento.
Se non abbiamo fatto un lavoro osceno destinato ad estinguersi da sè, prima o poi dovremo 
aggiornare qualcosa nel nostro applicativo.
Finchè si aggiungono cose, di solito non si creano grandi problemi. Ma nel caso in cui ci fossero 
eliminazioni di endpoint, campi o comunque modifiche sostanziali alle nostre API, bisognerà 
prevedere un meccanismo per creare una finestra di tempo che consenta agli utenti di 
aggiornare i loro sistemi.
(E, detto tra noi, non è male anche per avere un backup nel caso in cui la nuova versione fosse il 
lavoro osceno di cui sopra...)

9
L'approccio più popolare e diffuso è 
includere la versione nell'URL: 
  /v1/users,  /v2/users,  /v3/users
 La versione è tipicamente subito dopo il 
dominio, prima delle risorse.
È esplicito, immediatamente visibile, e 
facile da implementare e capire.
Versionamento

Riepilogando
Quindi, mettiamo insieme:
• nomenclatura uniforme
• gerarchia nel path
• uso verbi HTTP
• versionamento
Usiamo tutto questo per definire l’API “Catalogo” 
dell'applicazione "libreria" che vogliamo creare.

11
Verifichiamo

Ora a voi!
Create le API relative alla gestione dei clienti 
e degli ordini ad essi correlati.
Per comodità, assumiamo che i clienti siano 
allo stesso livello gerarchico dei libri.
E poi inizieremo a scrivere il codice 
necessario sul nostro server node.js.

Grazie per 
l’attenzione!
Docente: Fabio Abbà fabio.abba@tc-web.it
Via Giovanni Schiaparelli 14,
10148 – Torino (TO)
E-mail: info@tc-web.it
Tel: 011 0466685


---

# 4 - Swagger OpenAPI - Sempl

**File:** `4 - Swagger OpenAPI - Sempl.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1026.0 KB
**Ultima modifica:** 02/07/2026 09:28

---

DOCENTE Fabio ABBA’
UNITA’ FORMATIVA Competenze informatiche/digitali
ARGOMENTO RESTful API


OpenAPI Solutions
Introduzione 
a OpenAPI
Understanding API Standards
Fabio ABBA'
PRESENTED BY

OpenAPI (precedentemente Swagger Specification) è uno standard industriale per descrivere API 
REST in formato machine-readable (tipicamente JSON o YAML).
Definisce un formato strutturato che descrive tutti gli endpoint della nostra API, i parametri che 
accettano, gli schemi dei dati in input e output, i codici di stato HTTP possibili, i metodi di 
autenticazione, esempi, descrizioni testuali.
OpenAPI

Swagger Editor è uno strumento online che 
permette di scrivere e modificare specifiche 
OpenAPI in modo (quasi) intuitivo. 
SWAGGER EDITOR
Swagger UI fornisce un'interfaccia web 
interattiva per visualizzare e testare le API.
SWAGGER UI
Swagger Codegen è un generatore automatico 
di client e server che produce codice sorgente 
in vari linguaggi. Accelera lo sviluppo e 
garantisce coerenza tra implementazione e 
documentazione API.
SWAGGER CODEGEN
Ecosistema 
Swagger
SWAGGER È L'ECOSISTEMA DI STRUMENTI 
CHE IMPLEMENTA QUESTA SPECIFICA, 
COMPRENDENDO EDITOR, GENERATORI DI 
CODICE E INTERFACCE INTERATTIVE.

Vantaggi della documentazione 
OpenAPI
L'uso di OpenAPI garantisce 
un formato universalmente 
riconosciuto, facilitando la 
comunicazione e 
l'integrazione tra team 
diversi e sistemi.
STANDARDIZZAZIONE
Grazie a strumenti come 
Swagger, è possibile ridurre 
errori manuali e mantenere 
la sincronizzazione tra codice 
e documentazione, 
generando automaticamente 
il codice necessario.
AUTOMAZIONE
La documentazione 
OpenAPI consente di 
testare direttamente gli 
endpoint dall'interfaccia, 
rendendo il processo di 
verifica più semplice e 
immediato per gli 
sviluppatori.
TESTING INTEGRATO

Tools aggiuntivi
Vediamo subito in pratica quanto detto.
Per documentare le API della nostra applicazione 
avremo bisogno di un tool aggiuntivo che ci 
semplifichino il lavoro:
• swagger-ui-express: genererà l’interfaccia a 
partire da un file di configurazione (JSON in questo 
caso, ma più comunemente YAML)
Riferimento:
https://medium.com/@im_AnkitTiwari/swaggerizing-
your-node-js-rest-api-a-step-by-step-guide-
267255bf8bbe

Installazione
Cominciamo ad installare quanto serve:
E creiamo (se non l'abbiamo già fatto) una directory 
"doc“ (o swagger) dove inserire il file che servirà a 
generare l’interfaccia.


Esempio JSON
Questo è un esempio in 
formato JSON.

Esempio YAML
Questo è un esempio in 
formato YAML.
E' possibile dare il file .yml in 
pasto a dei servizi che sulla 
base di questo contenuto 
creeranno automaticamente 
la struttura documentata 
delle API che esponiamo.
Molto però dipende dal tipo 
di architettura usata.


Generazione 
interfaccia
Per quanto ci riguarda, noi useremo il file JSON 
per generare l'interfaccia Swagger.
Aggiungiamo il codice necessario:

Interfaccia Swagger
Ora, se avviamo l'applicazione e andiamo sulla pagina "/api-docs", avremo a disposizione un'interfaccia che ci 
mostra gli endpoint disponibili e ci permette di testarli.

Risorse utili
Oltre all'interfaccia intuitiva, c'è un altro grande vantaggio in 
questo approccio: una volta definita la struttura delle API nel file 
swagger.yml (e sperando che non cambi nel frattempo!), esso 
fungerà da riferimento per gli sviluppi sia lato frontend che lato 
backend anche in assenza delle implementazioni complete e in 
maniera completamente indipendente.
• https://swagger.io/docs/specification/v3_0/about/
• https://editor.swagger.io
• https://medium.com/@im_AnkitTiwari/swaggerizing-your-
node-js-rest-api-a-step-by-step-guide-267255bf8bbe
• https://swagger-autogen.github.io/docs/

Grazie per 
l’attenzione!
Fabio ABBA’
fabio.abba@tc-web.it
PRESENTED BY
Via Giovanni Schiaparelli 14,
10148 – Torino (TO)
E-mail: info@tc-web.it
Tel: 011 0466685


---

# 5 - HTTPS, JWT, auth

**File:** `5 - HTTPS, JWT, auth.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1970.1 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE Fabio ABBA’
UNITA’ FORMATIVA Competenze informatiche/digitali
ARGOMENTO RESTful API


Docente: Fabio ABBA’
Sicurezza nelle 
applicazioni 
web


L'importanza 
della sicurezza 
web
L'argomento di oggi è della massima importanza nello 
sviluppo di applicazioni web moderne.
Immaginate di costruire una casa con muri solidi e una 
porta blindata, ma di lasciare la chiave sotto lo zerbino: 
questa è un'applicazione che non applica standard di 
sicurezza, cioè è facilmente violabile. Le vulnerabilità 
possono portare a furti di dati, danni reputazionali e 
perdite finanziarie.

HTTPS: Il 
lucchetto del 
web
Immaginiamo di essere in un bar affollato. Se parlo 
con il mio amico a voce alta, tutti possono sentire la 
nostra conversazione. Questo è HTTP: i dati 
viaggiano in chiaro sulla rete, chiunque può 
intercettarli e leggerli.
Ora immaginiamo di parlare in una lingua segreta 
che solo io e il mio amico conosciamo. Anche se 
qualcuno ascolta, non capisce nulla.
 Questo è HTTPS: i dati sono crittografati.

4
Sicurezza Web
HTTPS e i suoi vantaggi
Crittografia
La crittografia assicura che i dati 
scambiati tra client e server siano 
cifrati. Se un malintenzionato 
intercettasse la comunicazione 
(attacco "Man-in-the-Middle"), 
vedrebbe solo dati incomprensibili.
Integrità
L'integrità garantisce che i dati 
non vengano alterati durante il 
trasferimento. Se un attaccante 
tentasse di modificare i dati, il 
sistema rileverebbe l'anomalia e 
respingerebbe la 
comunicazione.
Autenticazione
L'autenticazione verifica che le 
comunicazioni avvengano con il 
server corretto. Utilizzando 
certificati digitali, si assicura che 
gli utenti si connettano solo a 
fonti affidabili.
HTTPS è la versione sicura del protocollo HTTP . Aggiunge un livello di crittografia chiamato TLS (T ransport 
Layer Security), il successore di SSL. 

Autenticazione e 
autorizzazione
Un altro pilastro della sicurezza delle applicazioni 
web è la combinazione di autenticazione (chi sei?) e 
autorizzazione (cosa puoi fare?).
La strategia più comune e adatta alle API REST 
stateless è quella basata sui JSON Web T okens 
(JWT).

JSON Web 
Token
Un JSON WebT oken è una stringa che contiene 
(codificate) le informazioni che riguardano l'utente 
(idenificativo, ruolo/permessi), specifiche del token 
(emissione e scadenza),  ed altre info customizzabili 
a seconda del contesto applicativo.
T ali informazioni sono firmate lato server secondo la 
specifica JSON Web Signature(JWS), quindi il 
server è in grado di riconoscere se sono state 
generate da lui o meno.

7
Autenticazione JWT
Fondamenti del processo di autenticazione
Login
L'utente invia le sue credenziali 
(es. email e password) a un 
endpoint come “/auth/login”.
Verifica
Il server verifica le credenziali; 
se sono valide, il server crea un 
JWT , ossia una stringa 
codificata che contiene 
informazioni sull'utente (es. ID, 
ruolo) e una firma digitale.
Invio token
Il server invia il token JWT al 
client, permettendo così 
all'utente di accedere a risorse 
protette.


8
Autenticazione JWT
Gestione delle richieste sicure
Richieste Autenticate
Il client deve includere il token JWT 
nell'header Authorization per tutte le 
richieste a endpoint protetti, 
garantendo che solo gli utenti 
autenticati possano accedere alle 
risorse.
Authentication: Bearer <il_tuo_jwt>
Verifica T oken
Prima di processare una 
richiesta, il server verifica la 
firma del token. Se valida, 
estrae i dettagli utente; 
altrimenti, respinge la richiesta 
con un errore 401 Unauthorized.
Risposta al Client
Una volta verificato il token, il 
server invia al client le 
informazioni richieste, 
completando il ciclo di 
autenticazione.


9


Vantaggi 
dell'uso di JWT
Stateless: Il server non ha bisogno di 
memorizzare informazioni sulla sessione. 
Ogni token è auto-contenuto. Questo rende 
l'architettura scalabile.
Portabilità: Un token può essere usato per 
accedere a diverse API o microservizi.

Analisi del JWT
Come si evince dall’esempio, identifichiamo 3 parti in 
un token JWT , separate da un punto:
Header, Payload e Signature.


Analisi del JWT: Header
Decodificando la prima parte del token, scopriamo che si riferisce ad un json che contiene le due voci “typ” e 
“alg”. Il primo ha come valore sempre “ JWT”, mentre il nodo “alg” contiene il nome dell’algoritmo usato per il 
token. Nell'esempio è stato usato l’algoritmo “HMAC-SHA256”.

Analisi del JWT: Payload
La seconda parte del token è il corpo vero e proprio, che contiene dei dati variabili in base al contesto, in formato 
json e codificati in base64. Nel nostro esempio il payload contiene nome e id dell’utente e il timestamp 
dell’emissione del token, ma manca la scadenza del token (!), il che costituisce una potenziale vulnerabilità.

Analisi del JWT: Signature
La terza parte del token è la firma, che assicura l'integrità del token; non è altro che il risultato di una funzione 
hash 256 che prende in input la codifica base64 dell’header concatenandola con un punto alla codifica base64 
del payload, il tutto codificato con una "chiave segreta” definita nell'applicazione, e che solo il server conosce.

Attenzione!
Nota importane: la firma è l'unica parte 
crittografata del token; le informazioni 
contenute del payload sono decifrabili 
facilmente da chiunque entri in possesso del 
token: MAI inserire informazioni sensibili 
(password, informazioni personali, ...) nel 
payload!


Autorizzazione 
nelle 
applicazioni web
L'autorizzazione definisce i permessi degli utenti: cosa 
possono fare e a quali risorse possono accedere. È 
fondamentale per garantire che solo gli utenti autorizzati 
abbiano accesso a funzioni sensibili e dati protetti.
Ad esempio, un utente normale può leggere i prodotti, ma 
solo un admin può crearli o eliminarli.
L'autorizzazione solitamente si implementa con un 
middleware che viene eseguito dopo l'autenticazione e 
che si applica alle rotte definite nell'applicazione.

17
Best practices
• Usare sempre HTTPS in produzione
• Non salvare mai password in chiaro
• Usare JWT per l’autenticazione
• Impostare una scadenza ed eventualmente una 
rotazione dei token
• Mantenere le informazioni sensibili 
(JWT_SECRET , API keys) fuori dal codice in un 
file .env
• Dare agli utenti solo i permessi strettamente 
necessari (autorizzazione)


8
Risorse utili
- How To Use JSON Web Tokens (JWTs) in Express.js | DigitalOcean
- Mastering JWT authentication in Express - GeeksforGeeks


Grazie per l’attenzione!
Docente: Fabio Abbà fabio.abba@tc-web.it
Via Giovanni Schiaparelli 14,
10148 – Torino (TO)
E-mail: info@tc-web.it
Tel: 011 0466685
Credits: Franco Grivet
franco.grivet@tc-web.it


---

# Guida Essenziale alle API RESTful

**File:** `Guida Essenziale alle API RESTful.html`
**Tipo:** `.html`
**Dimensione:** 0.6 KB
**Ultima modifica:** 02/07/2026 09:28

---

<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->



---

# index

**File:** `index.html`
**Tipo:** `.html`
**Dimensione:** 0.6 KB
**Ultima modifica:** 02/07/2026 09:28

---

<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->
<!-- a padding to disable MSIE and Chrome friendly error page -->



---

# ISTRUZIONI MUSICLAB

**File:** `ISTRUZIONI MUSICLAB.md`
**Tipo:** `.md`
**Dimensione:** 8.6 KB
**Ultima modifica:** 02/07/2026 09:28

---

# 🎵 MusicLab — Esercitazione REST API con Node.js, Express e SQLite

## Obiettivo

Costruire un'API RESTful per gestire una collezione musicale, con un frontend HTML (fornito) che consenta di interagire con essa tramite interfaccia grafica.

Al termine dell'esercitazione avrai un server Node.js con Express che espone endpoint REST, un database SQLite con dati reali, e una pagina HTML funzionante per visualizzare e modificare brani e playlist semplicemente inserendo http://localhost:3000 nella barra degli inidirizzi del browser.


---

## Prerequisiti

- Node.js installato (v18 o superiore)
- Un editor di codice (VS Code consigliato)
- Postman per testare gli endpoint (opzionale ma consigliato)

---

## Struttura del progetto

```
musiclab/
├── server.js          ← entry point del server
├── database
    ├── db.js          ← configurazione e inizializzazione del database
    └── musiclab.db    ← file contenente il database
├── frontend
    └── index.html     ← file unico contenente la grafica e le logiche di Frontend
├── routes/
│   ├── songs.js       ← endpoint per i brani
│   └── playlists.js   ← endpoint per le playlist (bonus)
├── package.json
├── package-lock.json
```

---

## Setup iniziale

### 1. Crea la cartella

Crea una cartella chiamata musiclab; poi da VSC entraci dentro tramite il comando File -> Open Folder

### 2. Inizializza il progetto

Apri il Terminale di VSC e assicurati che sia del tipo Git Bash (NON powershell!) e inizializza il progetto tramite il comando

```bash
npm init
```
Ricorda di specificare il file "server.js" come entry point (voce "main" del file package.js) e il type a "module" (non "common").

### 3. Installa le dipendenze e crea lo script di avvio

```bash
npm install express sqlite3 nodemon
```

Terminato il comando, vai nel file package.json appena creato, togli qualsiasi cosa ci sia nell'oggetto "scripts" e al suo interno metti il comando di avvio, in modo che risulti come segue:

```json
"scripts": {
  "start": "nodemon server.js"
}
```

### 4. Crea la struttura di base dell'applicazione evvia il server

Definisci una costante "app" che rappresenti l'applicazione e le altre costanti necessarie (porta, basePath, ...), definisci il comando di avvio del server ( app.listen() ) e avvialo per verificare che tutto parta regolarmente:

```bash
npm start
```

---

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

```sql
CREATE TABLE IF NOT EXISTS playlist_songs (
      playlist_id INTEGER NOT NULL,
      song_id     INTEGER NOT NULL,
      PRIMARY KEY (playlist_id, song_id)
    )
```

---

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

**`PUT /songs/:id`**
- Sostituisce tutti i campi del brano (escluso `id`)
- Se il brano non esiste, restituisci 404
- Restituisci il brano aggiornato, status 200

**`DELETE /songs/:id`**
- Se il brano non esiste, restituisci 404
- Se l'eliminazione riesce, restituisci `{ message: "Brano eliminato" }`, status 200


---

## Parte bonus — Playlist (~1,5 ore)

### Endpoint da implementare

#### Gestione playlist

| Metodo   | Path              | Descrizione                                   |
|----------|-------------------|-----------------------------------------------|
| `GET`    | `/playlists`      | Recupera tutte le playlist                    |
| `GET`    | `/playlists/:id`  | Recupera una playlist con i brani associati   |
| `POST`   | `/playlists`      | Crea una nuova playlist                       |
| `PUT`    | `/playlists/:id`  | Modifica una playlist                         |
| `DELETE` | `/playlists/:id`  | Rimuove una playlist                          |

#### Gestione brani nelle playlist

| Metodo   | Path                            | Descrizione                     |
|----------|---------------------------------|---------------------------------|
| `POST`   | `/playlists/:id/songs`          | Aggiunge un brano alla playlist |
| `DELETE` | `/playlists/:id/songs/:songId`  | Rimuove un brano dalla playlist |

### Indicazioni

**`GET /playlists/:id`**
Deve restituire la playlist con l'array dei brani associati:
```json
{
  "id": 1,
  "name": "Chill Vibes",
  "description": "Musica rilassante",
  "songs": [
    { "id": 3, "title": "Clair de Lune", "artist": "Debussy", "album": "Suite bergamasque", "genre": "Classica", "year": 1905 }
  ]
}
```
Se la playlist esiste ma non ha brani, restituisci `"songs": []`.
Usa una `JOIN` tra `playlists`, `playlist_songs` e `songs`.

**`POST /playlists/:id/songs`**
- Il body deve contenere `{ "song_id": 5 }`
- Verifica che la playlist esista (404 se non esiste)
- Verifica che il brano esista (404 se non esiste)
- Se il brano è già nella playlist, restituisci `{ error: "Brano già presente nella playlist" }`, status 409
- Se va bene, inserisci la riga in `playlist_songs` e restituisci status 201

**`DELETE /playlists/:id/songs/:songId`**
- Rimuove il brano dalla playlist (non elimina il brano dal database)
- Se la combinazione non esiste, restituisci 404

**`DELETE /playlists/:id`**
- Prima di eliminare la playlist, elimina anche le righe corrispondenti in `playlist_songs`
- Restituisci `{ message: "Playlist eliminata" }`, status 200

---

## Suggerimenti generali

- Usa `sqlite3` per le query: le operazioni sono **asincrone** e usano callback. Le tre principali sono:
  - `db.all(sql, params, (err, rows) => {})` — restituisce un array di righe
  - `db.get(sql, params, (err, row) => {})` — restituisce una singola riga (o `undefined` se non trovata)
  - `db.run(sql, params, function(err) { this.lastID })` — esegue INSERT/UPDATE/DELETE; in caso di INSERT, `this.lastID` contiene l'id della riga appena inserita (attenzione: usare `function`, non arrow function, per accedere a `this`)
- Ricorda di abilitare il parsing del body JSON in Express: `app.use(express.json())`
- Testa ogni endpoint con Postman prima di collegarlo al frontend
- Controlla sempre la console del server se qualcosa non funziona

---

## Consegna

Al termine dell'esercitazione dovrai avere:

**Parte base:**
- [ ] Tutti e 7 gli endpoint per i brani funzionanti
- [ ] Frontend con visualizzazione, ricerca, creazione, modifica ed eliminazione brani

**Bonus:**
- [ ] Tutti gli endpoint per le playlist funzionanti
- [ ] Frontend con visualizzazione, creazione, modifica ed eliminazione playlist
- [ ] Possibilità di aggiungere e rimuovere brani da una playlist



---

# JWT e autenticazione

**File:** `JWT e autenticazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 243.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

INTRODUZIONE 
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
soluzione non è quindi adatta a sistemi di produzione: immaginiamo di dover ri-
eseguire ad ogni richiesta le query di autenticazione sul nostro db su un sistema con 
migliaia di utenti online nel singolo istante! Una soluzione completamente 
Stateless, scalabile e con nessuno overhead è quella oggetto di questo articolo: 
JWT (JSON WEB TOKEN) 
 
 
JSON WEB TOKEN 
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
{ 
"sub": "admin", 
"aud": "web", 
"roles": [ 
"ROLE_ADMIN", 
"ROLE_USER" 

], 
"isEnabled": true, 
"exp": 1512975450, 
"iat": 1512968250230 
} 
JWT propone dei campi “standard” da utilizzare nel payload (es: sub, audience, exp 
e iat) ma il programmatore può inserire proprietà aggiuntive (vedi isEnabled e roles 
da me definiti e non contemplati nei clams standard). Andando ad analizzare il json 
del body possiamo interpretare dal token le seguenti info: 
● utente admin (claim sub) 
● ha come target il web (claim aud) 
● ruoli utente ROLE_ADMIN, ROLE_USER (claim roles) 
● utente abilitato (claim isEnabled) 
● info relative al momento in cui è stato creato il token (iat) e sulla data di 
scadenza (exp): momento in cui tale token non sarà più ritenuto valido dal 
server. 
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
autenticarsi. 


2. Il server verifica se le credenziali postate sono corrette. In caso positivo 
costruisce un token jwt utilizzando la chiave segreta e inserendo nel payload 
del token le informazioni utente e le data di creazione e scadenza del token; 
Tale token verrà firmato e autentificato con la sua chiave privata ( importante 
solo il server deve conoscere la chiave privata ) 
3. tale token viene inviato nella risposta all’interno di un header http ( nella 
implementazione che proporremo sotto utilizzeremo l header http X-auth) 
4. Il client salva il token jwt risultato dell’autenticazione, e nelle successive 
richieste richieste inoltra sempre nell’apposito header http X-auth il token 
restituito nel punto 3. Tale token funge da “passaporto” per garantire che tali 
successive richieste sono autenticate. 
5. Il server riceve il token ad ogni successiva richiesta. Ogni volta si assicura 
che il token sia stato firmato e autentificato con la sua chiave privata ed infine 
che non sia scaduto. Poiché il token contiene al suo interno il payload con le 
informazioni necessarie all’autenticazione (es. username e ruoli utente), il 
server eviterà di fare query ogni volta per verificare a quale utente 
corrisponde quel token e di recuperare le info utente necessarie per 
ricostruire lo stato della sessione (ottimo risultato per la scalabilità ed 
eliminando totalmente l’overhead della soluzione BASIC descritta ad inizio 
articolo). 
6. Se passati i controlli descritti dal punto 5, il server tratterà l’utente come 
autenticato e gestirà la richiesta, altrimenti risponderà alla richiesta con un 
codice di errore HTTP 401 (utente non autorizzato). 
 
 
 
INTEGRAZIONE CON AUTHENTICATION PROVIDERS 
 
Quando ci si integra con un Authentication Provider esterno tramite standard 
moderni come OAuth 2.0 e OpenID Connect (OIDC), il flusso si evolve in questo 
modo: 
1. Spostamento delle credenziali: Il proprio server Express non riceve né 
memorizza le password in chiaro o cifrate. La responsabilità di verificare "chi 
è l'utente" viene interamente delegata al provider esterno.  
2. Firme Asimmetriche (RS256 vs HS256): Poiché il token viene generato dal 
provider esterno e consumato dalla nostra API, non si usa più una chiave 
segreta simmetrica condivisa. Il provider firma il JWT utilizzando la propria 
chiave privata (algoritmo asimmetrico, solitamente RS256). La nostra 
applicazione Express scarica periodicamente le chiavi pubbliche del 

provider da un endpoint standardizzato denominato JWKS (JSON Web Key 
Sets) per verificare l'integrità e l'autenticità della firma.  
3. Preservazione dell'architettura Stateless: Una volta che l'applicazione 
Express ha convalidato la firma del token tramite la chiave pubblica del 
provider, il funzionamento rimane strettamente stateless. Il server estrae i 
dettagli dell'utente (i claims, come ID, email o ruoli) direttamente dal payload 
del token , senza la necessità di interrogare il database del provider o 
memorizzare sessioni sul server. Tutto il traffico deve comunque essere 
protetto da HTTPS per evitare attacchi Man-in-the-Middle. 
 


---

# JWT vs HttpOnly cookie

**File:** `JWT vs HttpOnly cookie.pdf`
**Tipo:** `.pdf`
**Dimensione:** 169.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

JWT  vs   HttpOnly  cookie  
1.  JWT  in  header  
Scenario  tipico:  
●  Login  con  POST  /login →  il  server  genera  un  JWT  (spesso  firmato  con  HS256)  
 ●  Il  client  (SPA/JS)  salva  il  token  in:  
 ○  localStorage oppure  
 ○  sessionStorage  
 ●  Ad  ogni  richiesta  →  header:  
 Authorization:  Bearer  <jwt>  
 
Problema  principale  
Se  il  sito  ha  anche  solo  una  vulnerabilità  XSS ,  uno  script  malevolo  può  fare:  
localStorage.getItem("token")   //  oppure  sessionStorage   
e  rubarsi  il  JWT.  
 
A
 
quel
 
punto
 
il
 
token
 
è
 
usabile
 
ovunque
,
 
da
 
chiunque
 
lo
 
possieda.
 
In  più  spesso:  
●  JWT  molto  lunghi  
 ●  scadenza  troppo  ampia  
 ●  troppe  informazioni  dentro  il  payload  
 ●  nessun  meccanismo  di  rotazione  /  revoca  
 
Risultato:  se  il  token  viene  rubato,  l’attaccante  è  loggato  “per  sempre”  finché  il  token  non  
scade.
 
 
 

2.  Cosa  cambia  con  HttpOnly  cookie  
L’idea  moderna  è:  
1.  Il  server,  dopo  il  login,  NON  ti  dà  il  JWT  da  salvare  nel  JS.  
 
Invece,  risponde  con  un  Set-Cookie :  
 
 
Set-Cookie:
 
access_token=<jwt-o-id-sessione>;
 
             HttpOnly;               Secure;               SameSite=Strict;              Path=/  
2.   3.  Il  browser:  
 ○  salva  il  cookie  
 ○  lo  rimanda  automaticamente  in  ogni  richiesta  verso  quel  dominio.  
 
Tu  dal  frontend  non  fai  più:  
 Authorization:  Bearer  ...   ma  semplicemente  chiami  le  API  (fetch/axios)  e  il  browser  allega  i  cookie.  
Perché  è  più  sicuro?  Flag  HttpOnly  →  il  cookie  NON  è  leggibile  da  JavaScript:  
 
 
document.cookie
  
//
 
non
 
mostra
 
il
 
cookie
 
HttpOnly
 
●   Quindi,  anche  se  hai  XSS,  l’attaccante  non  può  rubare  il  token  semplicemente  
leggendolo
 
dal
 
client.
 
 ●  Flag  Secure  →  il  cookie  viaggia  solo  su  HTTPS  (non  in  chiaro).  
 ●  Flag  SameSite :  
 ○  Strict o  Lax riducono  i  rischi  di  CSRF ,  cioè  richieste  da  altri  siti  che  usano  
il
 
tuo
 
cookie.
 
 
 
 

3.  Ma  allora  JWT  sono  “insicuri”?  
Non  è  che  JWT  siano  insicuri  in  sé.  
 
Problemi
 
comuni:
 
1.  Uso  improprio :  
 ○  Token  lunghissimi,  con  un  sacco  di  dati  sensibili.  
 ○  Nessuna  rotazione.  
 ○  Nessuna  revoca  server-side  (“se  ho  un  JWT  valido  posso  bypassare  tutto”).  
 2.  Storage  insicuro  nel  frontend:  
 ○  localStorage +  XSS  =  furto  del  token.  
 3.  Assenza  di  controlli  extra :  
 ○  niente  IP  binding,  niente  device  binding,  niente  controllo  su  user-agent.  
 
Spesso  oggi  si  consiglia  di:  
●  usare  JWT  come  access  token  a  breve  durata  
 ●  tenerli  nel  backend  o  in  cookie  HttpOnly ,  non  nel  JS  leggibile.  
 
4.  Flusso  moderno  tipico  (semplificato)  per  le  tue  
lezioni
 
5.  Confronto  didattico:  Header  JWT  vs  HttpOnly  cookie  
Puoi  sintetizzare  così  ai  ragazzi:  
Aspetto  JWT  in  header  +  localStorage  JWT/Session  in  HttpOnly  Cookie  
Lettura  JS  ✅  sì  (localStorage)  ❌  no  (HttpOnly)  
Rischio  XSS  alto  (token  rubabile)  più  basso  (token  non  leggibile  da  JS)  
Rischio  CSRF  basso  (token  in  header  manuale)  
più  alto  se  SameSite  è  None 

Comodità  client  controlla  header  browser  gestisce  i  cookie  da  solo  
Messaggio  importante  da  passare:  
Non  è  che  “JWT  sono  il  male”  e  “cookie  sono  il  bene”.  
 
Il
 
tema
 
è
 
dove
 
tieni
 
il
 
token
 
e
 
come
 
gestisci
 
XSS/CSRF
.
 
 
 
 
1.  Implementre  Http  CLient  Only  
 
Da  terminale:  
```bash  
npm  install  cookie-parser  
 
 
3.  Modifica  di  server.js per  usare  i  cookie  
In  server.js,  aggiungi  cookie-parser e  (se  usi  una  SPA)  abilita  CORS  con  credenziali.  
server.js  aggiornato  (versione  semplificata)  
//  agganciamo  le  librerie  che  abbiamo  installato  con  node  
const  express  =  require('express');  
const  sqlite3  =  require('sqlite3').verbose();  
const  bodyParser  =  require('body-parser');  
const  cors  =  require('cors');  
const  cookieParser  =  require('cookie-parser');  //  <---  NEW  
 
//  dichiariamo  su  che  porta  risponderà  il  server  web  

const  port  =  3000;  
//creiamo  l’istanza  del  server  
const  app  =  express();  
 
//  Middleware  
//  Se  usi  una  SPA  su  un’altra  porta  (es.  Angular  su  4200),  meglio  così:  
app.use(cors({  
  origin:  'http://localhost:4200',  //  oppure  l'origin  del  tuo  frontend  
  credentials:  true                //  <---  per  mandare  i  cookie  
}));  
 
app.use(bodyParser.json());  
app.use(cookieParser());  //  <---  abilita  lettura  cookie  HttpOnly  
 
//  Importa  le  rotte  
const  coursesRoutes   =  require('./routes/courses');  
const  studentsRoutes  =  require('./routes/students');  
const  teachersRoutes  =  require('./routes/teachers');  
const  authRoutes      =  require('./routes/auth');  
 
//  Usa  le  rotte  
app.use('/api/v1/courses',  coursesRoutes);  
app.use('/api/v1/students',  studentsRoutes);  
app.use('/api/v1/teachers',  teachersRoutes);  
app.use('/api/v1/login',  authRoutes);  
 

//  Avviare  il  server  
app.listen(port,  ()  =>  {  
  console.log(`Server  in  ascolto  sulla  porta  ${port}`);  
});  
 
Così  il  server  è  pronto  a:  
●  leggere  cookie  (req.cookies)  
 ●  permettere  al  browser  di  inviare  cookie  alle  API  (credentials:  true lato  CORS,  
e
 credentials:  'include' lato  fetch/axios).  
 
 
4.  Modifica  della  rotta  di  login  per  usare  
HttpOnly
 
cookie
 
Ora  modifichiamo  routes/auth.js:  invece  di  mandare  il  token  nel  JSON,  lo  mettiamo  in  
un
 
cookie
 
HttpOnly.
 
routes/auth.js  aggiornato  
const  express  =  require('express');  
const  router  =  express.Router();  
const  jwt  =  require('jsonwebtoken');  
const  db  =  require('../db/connection');  
 
const  SECRET_KEY  =  'ChiaveComplessa!';  
 
//  POST  /api/v1/login  
router.post('/',  (req,  res)  =>  {  
  const  {  username,  password  }  =  req.body;  
 

  db.get(  
    'SELECT  *  FROM  docente  WHERE  username  =  ?  AND  password  =  ?',  
    [username,  password],  
    (err,  results)  =>  {  
      if  (err)  {  
        console.error(err);  
        return  res.status(500).send('Errore  nel  database');  
      }  
 
      if  (!results)  {  
        return  res.status(404).json({  message:  'Username  o  password  errati!!'  });  
      }  
 
      //  payload  minimale  
      const  docentePayload  =  {  
        cognome:  results.cognome,  
        nome:  results.nome,  
        materie:  results.materie  
      };  
 
      //  genera  JWT  
      jwt.sign(docentePayload,  SECRET_KEY,  {  expiresIn:  '1h'  },  (err,  token)  =>  {  
        if  (err)  {  
          return  res.status(500).json({  message:  'Errore  nella  creazione  del  token'  
});
 
        }  
 

        //  ***  QUI  CAMBIA:  settiamo  un  cookie  HttpOnly  ***  
        res.cookie('authToken',  token,  {  
          httpOnly:  true,    //  non  leggibile  da  JS  
          secure:  false,     //  in  sviluppo  su  http://localhost  deve  essere  false  
          sameSite:  'lax',   //  protegge  un  minimo  da  CSRF  ed  è  ok  per  molte  SPA  
          maxAge:  60  *  60  *  1000  //  1h  in  millisecondi  
        });  
 
        //  Nel  body  NON  mandiamo  il  token  
        res.status(200).json({  
          message:  'login  ok',  
          docente:  docentePayload  
        });  
      });  
    }  
  );  
});  
 
module.exports  =  router;  
 
In  produzione  con  HTTPS:  basta  mettere  secure:  true.  
 
Su
 
localhost
 
HTTP:
 
deve
 
rimanere
 secure:  false,  altrimenti  il  browser  non  
manda
 
il
 
cookie.
 
 
5.  Middleware  per  verificare  il  JWT  dal  cookie  
Ora  ci  serve  un  middleware  riusabile  per  proteggere  le  rotte  (es.  /courses).  

Crea  un  file,  per  esempio:  middlewares/checkAuth.js:  
//  middlewares/checkAuth.js  
const  jwt  =  require('jsonwebtoken');  
 
const  SECRET_KEY  =  'ChiaveComplessa!';  
 
function  checkAuth(req,  res,  next)  {  
  //  leggiamo  il  cookie  impostato  nel  login  
  const  token  =  req.cookies.authToken;  
 
  if  (!token)  {  
    return  res.status(401).json({  message:  'Token  mancante.  Effettua  il  login.'  });  
  }  
 
  jwt.verify(token,  SECRET_KEY,  (err,  decoded)  =>  {  
    if  (err)  {  
      console.error('Errore  verifica  token:',  err);  
      return  res.status(401).json({  message:  'Token  non  valido  o  scaduto.'  });  
    }  
 
    //  metto  i  dati  del  docente  nella  request,  così  le  rotte  li  possono  usare  
    req.user  =  decoded;  
    next();  
  });  
}  
 

module.exports  =  checkAuth;  
 
 
6.  Proteggere  le  rotte  (esempio  su  courses.js)  
Nel  tuo  routes/courses.js ora  puoi  usare  il  middleware  per  fare  in  modo  che  tutte  le  
operazioni
 
sui
 
corsi
 
richiedano
 
il
 
login.
 
routes/courses.js  aggiornato  (parte  iniziale)  
const  express  =  require('express');  
const  router  =  express.Router();  
const  db  =  require('../db/connection');  
const  checkAuth  =  require('../middlewares/checkAuth');  //  <---  NEW  
 
//  Tutte  le  rotte  sotto  richiedono  autenticazione  
router.use(checkAuth);  
 
/**********   COURSES  ***************/  
 
//  searchAll  
router.get('/',  (req,  res)  =>  {  
  db.all('SELECT  *  FROM  corso',  (err,  results)  =>  {  
    if  (err)  {  
      console.error(err);  
      res.status(500).send('Errore  nel  database');  
    }  else  {  
      res.json(results);  
    }  

  });  
});  
 
//  ...  il  resto  delle  rotte  (GET  /:id,  POST,  PUT,  DELETE)  rimangono  uguali  
 
Oppure,  se  vuoi  che  solo  alcune  rotte  siano  protette,  puoi  fare:  
router.get('/',  checkAuth,  (req,  res)  =>  {  ...  });  
router.post('/',  checkAuth,  (req,  res)  =>  {  ...  });  
 
 
7.  Logout:  come  cancellare  il  cookie  
Ti  conviene  definire  una  rotta,  per  esempio  in  routes/auth.js:  
//  POST  /api/v1/login/logout  
router.post('/logout',  (req,  res)  =>  {  
  res.clearCookie('authToken',  {  
    httpOnly:  true,  
    secure:  false,   //  come  sopra:  false  in  dev,  true  in  produzione  
    sameSite:  'lax'  
  });  
  res.status(200).json({  message:  'Logout  effettuato'  });  
});  
 
E  in  server.js non  devi  cambiare  nulla:  è  sempre  sotto  /api/v1/login.  
 
8.  E  lato  frontend?  

Due  note  veloci  che  puoi  usare  anche  con  i  ragazzi:  
●  Con  fetch:  
 
fetch('http://localhost:3000/api/v1/courses',  {  
  method:  'GET',  
  credentials:  'include'  //  <---  per  mandare  i  cookie  
});  
 
●  Con  Axios:  
 
axios.get('http://localhost:3000/api/v1/courses',  {  
  withCredentials:  true  
});  
 
 
9.  Risposta  secca  alla  tua  domanda  
“Server  in  locale  senza  HTTPS,  con  HttpOnly  cookie  funziona  lo  stesso?”  
●  Sì ,  funziona:  
 ○  HttpOnly funziona  anche  su  HTTP  →  il  cookie  non  è  leggibile  da  JS.  
 ○  Il  vantaggio  contro  XSS  c’è  comunque.  
 ●  L’unica  cosa:  non  puoi  usare  secure:  true (cookie  inviato  solo  su  HTTPS),  quindi  
in
 
sviluppo
 
usi
 secure:  false.  
 ●  In  produzione  è  caldamente  consigliato:  
 ○  HTTPS  
 ○  secure:  true  
 

○  sameSite impostato  correttamente  (es.  lax o  strict a  seconda  dei  casi).  
 
 
Se  vuoi,  nel  prossimo  passo  possiamo:  
●  aggiungere  anche  un  refresh  token  con  secondo  cookie  
 ●  o  preparare  una  slide  per  i  ragazzi  con  il  confronto  “prima/dopo”  e  spiegazioni  
XSS/CSRF.
 
 
 
 


---

# script libri

**File:** `script libri.js`
**Tipo:** `.js`
**Dimensione:** 1.0 KB
**Ultima modifica:** 02/07/2026 09:12

---

export const CREATE_LIBRI_TABLE = `CREATE TABLE IF NOT EXISTS libri (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        titolo TEXT NOT NULL,
                                        autore TEXT NOT NULL,
                                        editore TEXT NOT NULL,
                                        genere TEXT,
                                        numero_pagine INTEGER
                                    )`;

export const SELECT_ALL = "SELECT * FROM libri";

export const SELECT_BY_ID = "SELECT * FROM libri WHERE id = ?";

export const SELECT_BY_TITOLO = "SELECT * FROM libri WHERE LOWER(titolo) LIKE '% || LOWER(?) || %'";

export const INSERT_LIBRO = "INSERT INTO libri (titolo, autore, editore, genere, numero_pagine) VALUES (?, ?, ?, ?, ?)";

export const UPDATE_LIBRO = "UPDATE libri SET titolo = ?, autore = ?, editore = ?, genere = ?, numero_pagine = ? WHERE id = ?";

export const DELETE_LIBRO = "DELETE FROM libri WHERE id = ?";


---

# Test RESTful API Gruppi

**File:** `Test RESTful API Gruppi.docx`
**Tipo:** `.docx`
**Dimensione:** 26.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

Gruppo 1

Test RESTful API  •  ITS Competenze Informatiche/Digitali

Nome: ______________________________   Data: ___________

Questo fascicolo contiene 8 domande di tre tipologie:

  🔍  Correggere Errori – individua e correggi gli errori presenti

  🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B

  ✅  Vero o Falso – indica V o F e motiva brevemente la risposta

Domanda 1   [Correggere Errori]   Argomento: JSON

Il seguente oggetto JSON contiene 3 errori. Individuali e correggi.

{ 

  'nome': 'Mario Rossi',

  "eta": 30,

  "attivo": True,

  "tags": ["admin", "editor",],

}

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

{

  "nome": "Luigi",

  "email": "luigi@example.com"

}

Correzioni e spiegazioni:

Domanda 8   [Abbinamento]   Argomento: Architettura REST

Abbina ogni concetto REST alla sua definizione.

Risposte:  1__   2__   3__   4__   5__   6__

Gruppo 2

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

{

  "libreria": {

    "nome": 'Biblioteca Centrale',

    "libri": [

      { "titolo": "1984", "anno": 1949, },

      { "titolo": "Il Signore degli Anelli", "pagine": null }

    ],

    "aperta": false

  }

}

Correzioni e spiegazioni:

Domanda 3   [Vero o Falso]   Argomento: Architettura REST

Indica VERO o FALSO con motivazione.

Domanda 4   [Abbinamento]   Argomento: Codici di Stato HTTP

Abbina il codice di stato HTTP alla sua famiglia e significato.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 5   [Correggere Errori]   Argomento: Request/Response HTTP

Questa response HTTP ha 3 errori. Correggili.

HTTP/1.1 201

content-type: text/json

{

  id: 42,

  "messaggio": "Utente creato con successo"

}

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

Gruppo 3

Test RESTful API  •  ITS Competenze Informatiche/Digitali

Nome: ______________________________   Data: ___________

Questo fascicolo contiene 8 domande di tre tipologie:

  🔍  Correggere Errori – individua e correggi gli errori presenti

  🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B

  ✅  Vero o Falso – indica V o F e motiva brevemente la risposta

Domanda 1   [Vero o Falso]   Argomento: Principi REST

Indica VERO o FALSO con motivazione.

Domanda 2   [Correggere Errori]   Argomento: JSON

Correggi tutti gli errori presenti nel seguente JSON.

{

  "ordine": {

    "id": "ORD-001"

    "stato": 'pending',

    "totale": 89.90,

    "prodotti": [

      {"nome": "Libro A", "qty": 2},

      {"nome": "Libro B", "qty": 1,}

    ],

    "spedito": False

  }

}

Correzioni e spiegazioni:

Domanda 3   [Abbinamento]   Argomento: Codici di Stato HTTP

Abbina il codice HTTP allo scenario reale.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 4   [Vero o Falso]   Argomento: Request/Response HTTP

Indica VERO o FALSO con motivazione.

Domanda 5   [Correggere Errori]   Argomento: Endpoint REST

Questi endpoint hanno problemi di design. Correggi e spiega.

GET  /api/v1/searchProductByName?name=libro

POST /api/v1/users/delete/99

GET  /api/v1/User/Orders/5

PUT  /api/v1/products        (aggiornare il prodotto con id 7)

Correzioni e spiegazioni:

Domanda 6   [Abbinamento]   Argomento: Architettura REST

Abbina ogni vincolo REST alla sua spiegazione.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 7   [Correggere Errori]   Argomento: Request/Response HTTP

La seguente chiamata REST in JavaScript contiene errori. Trovali e correggi.

fetch('/api/v1/users/10', {

  method: 'REMOVE',

  headers: {

    'Content-Type': 'text/plain'

  },

  body: JSON.stringify({ nome: 'Mario' })

})

Correzioni e spiegazioni:

Domanda 8   [Vero o Falso]   Argomento: OpenAPI/Swagger

Indica VERO o FALSO con motivazione.

Gruppo 4

Test RESTful API  •  ITS Competenze Informatiche/Digitali

Nome: ______________________________   Data: ___________

Questo fascicolo contiene 8 domande di tre tipologie:

  🔍  Correggere Errori – individua e correggi gli errori presenti

  🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B

  ✅  Vero o Falso – indica V o F e motiva brevemente la risposta

Domanda 1   [Correggere Errori]   Argomento: Endpoint REST

Correggi questi endpoint rispettando le convenzioni REST e spiega ogni modifica.

GET  /api/v1/getClienteById/10

POST /api/v1/clienti/10/updateEmail

GET  /api/v1/clienti/10/OrdiniDelCliente

DELETE /api/v1/rimuoviCliente/10

Correzioni e spiegazioni:

Domanda 2   [Vero o Falso]   Argomento: JSON

Indica VERO o FALSO con motivazione.

Domanda 3   [Abbinamento]   Argomento: Request/Response HTTP

Abbina ogni componente HTTP alla sua descrizione.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 4   [Correggere Errori]   Argomento: JSON

Correggi il seguente JSON (contiene 4 errori).

{

  "catalogo": [

    {

      "titolo": "Clean Code",

      "autore": 'Robert C. Martin',

      "anno": 2008

      "disponibile": True,

      "tags": ["programmazione", "best practices",]

    }

  ]

}

Correzioni e spiegazioni:

Domanda 5   [Vero o Falso]   Argomento: Verbi HTTP

Indica VERO o FALSO con motivazione.

Domanda 6   [Abbinamento]   Argomento: Principi REST

Abbina ogni affermazione al principio REST che descrive.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 7   [Abbinamento]   Argomento: Architettura REST / API

Abbina ogni termine alla sua definizione.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 8   [Vero o Falso]   Argomento: Codici di Stato HTTP

Indica VERO o FALSO con motivazione.

Gruppo 5

Test RESTful API  •  ITS Competenze Informatiche/Digitali

Nome: ______________________________   Data: ___________

Questo fascicolo contiene 8 domande di tre tipologie:

  🔍  Correggere Errori – individua e correggi gli errori presenti

  🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B

  ✅  Vero o Falso – indica V o F e motiva brevemente la risposta

Domanda 1   [Vero o Falso]   Argomento: Architettura REST

Indica VERO o FALSO con motivazione.

Domanda 2   [Abbinamento]   Argomento: JSON

Abbina ogni tipo di dato JSON a un esempio corretto.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 3   [Correggere Errori]   Argomento: Endpoint REST

Analizza e correggi questi endpoint non conformi alle best practice REST.

POST /api/v1/clienti/search

GET  /api/v1/createOrder

PUT  /api/v1/orders       (aggiornare ordine con id 77)

GET  /api/v1/Prodotti/CercaPerCategoria?cat=libri

Correzioni e spiegazioni:

Domanda 4   [Abbinamento]   Argomento: Request/Response HTTP

Abbina ogni header HTTP alla sua funzione.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 5   [Vero o Falso]   Argomento: Codici di Stato HTTP

Indica VERO o FALSO con motivazione.

Domanda 6   [Correggere Errori]   Argomento: Request/Response HTTP

Questa sequenza richiesta/risposta ha 4 errori. Trovali e correggi.

--- REQUEST ---

POST /api/v1/libri HTTP/1.1

Host: libreria.example.com

Content-Type: text/html

{

  'titolo': 'Il Nome della Rosa',

  "autore": "Umberto Eco"

}

--- RESPONSE ---

HTTP/1.1 200

Content-Type: application/json

Correzioni e spiegazioni:

Domanda 7   [Abbinamento]   Argomento: Verbi HTTP

Abbina ogni operazione CRUD al corretto verbo HTTP e URL.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 8   [Correggere Errori]   Argomento: JSON

Correggi il seguente JSON (contiene 3 errori).

{

  "cliente": {

    "id": 99,

    "nome": "Anna Bianchi"

    "ordini": [

      { "id": 1001, "totale": 45.50, "pagato": True },

      { "id": 1002, "totale": 12.00, "pagato": false }

    ]

  }

}

Correzioni e spiegazioni:

Gruppo 6

Test RESTful API  •  ITS Competenze Informatiche/Digitali

Nome: ______________________________   Data: ___________

Questo fascicolo contiene 8 domande di tre tipologie:

  🔍  Correggere Errori – individua e correggi gli errori presenti

  🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B

  ✅  Vero o Falso – indica V o F e motiva brevemente la risposta

Domanda 1   [Abbinamento]   Argomento: Architettura REST

Abbina il protocollo/tecnologia alla sua caratteristica principale.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 2   [Vero o Falso]   Argomento: Verbi HTTP

Indica VERO o FALSO con motivazione.

Domanda 3   [Correggere Errori]   Argomento: JSON

Il seguente JSON contiene 4 errori. Individuali e correggi.

{

  'prodotto': {

    "id": 55,

    "nome": "Mouse Wireless",

    "prezzo": 29.99

    "disponibile": True,

    "categorie": ["elettronica", "accessori",],

    "sconto": Null

  }

}

Correzioni e spiegazioni:

Domanda 4   [Vero o Falso]   Argomento: Endpoint REST / Nomenclatura

Indica VERO o FALSO con motivazione.

Domanda 5   [Abbinamento]   Argomento: Codici di Stato HTTP

Uno sviluppatore riceve queste risposte. Abbina ognuna alla causa più probabile.

Risposte:  1__   2__   3__   4__   5__   6__

Domanda 6   [Correggere Errori]   Argomento: Endpoint REST

Ri-progetta questi endpoint secondo le best practice REST. Motiva ogni scelta.

POST /api/v1/checkUserExists/mario@email.com

GET  /api/v1/books/55/doDelete

GET  /api/v1/newOrder

POST /api/v1/users/updatePassword/88

Correzioni e spiegazioni:

Domanda 7   [Vero o Falso]   Argomento: OpenAPI/Swagger

Indica VERO o FALSO con motivazione.

Domanda 8   [Abbinamento]   Argomento: Request/Response HTTP

Abbina ogni scenario alla coppia corretta verbo HTTP + codice di risposta atteso.

Risposte:  1__   2__   3__   4__   5__   6__

