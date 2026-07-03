# Lezione 1

## Panoramica
Competenze informatiche/digitali

## Argomenti trattati
Git, API REST, Data Analytics, Reti

---
## Appunti

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
*Fonte: 001_1_-_Introduzione_a_REST.md*
