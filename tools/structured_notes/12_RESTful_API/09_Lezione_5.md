# Lezione 5

## Panoramica
Competenze informatiche/digitali

## Argomenti trattati
Git, API REST, Sicurezza, Data Analytics, Reti

---
## Appunti

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
*Fonte: 005_5_-_HTTPS_JWT_auth.md*
