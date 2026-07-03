# JWT e autenticazione

## Panoramica
Una delle esigenze più comuni del WEB è quella di restringere l’accessibilità di una o

## Argomenti trattati
API REST, Data Analytics, Database

---
## Appunti

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
*Fonte: 999_JWT_e_autenticazione.md*
