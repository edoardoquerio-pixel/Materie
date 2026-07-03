# Lezione 4

Fonte: `4 - Swagger OpenAPI - Sempl.pdf`

DOCENTE

Fabio ABBA’

UNITA’ FORMATIVA

Competenze informatiche/digitali

ARGOMENTO

RESTful API

OpenAPI Solutions

Introduzione 
a OpenAPI

Understanding API Standards

PRESENTED BY

Fabio ABBA'

OpenAPI

OpenAPI (precedentemente Swagger Specification) è uno standard industriale per descrivere API 
REST in formato machine-readable (tipicamente JSON o YAML).

Definisce un formato strutturato che descrive tutti gli endpoint della nostra API, i parametri che 
accettano, gli schemi dei dati in input e output, i codici di stato HTTP possibili, i metodi di 
autenticazione, esempi, descrizioni testuali.

Ecosistema 
Swagger

SWAGGER È L'ECOSISTEMA DI STRUMENTI 
CHE IMPLEMENTA QUESTA SPECIFICA, 
COMPRENDENDO EDITOR, GENERATORI DI 
CODICE E INTERFACCE INTERATTIVE.

SWAGGER EDITOR

Swagger Editor è uno strumento online che 
permette di scrivere e modificare specifiche 
OpenAPI in modo (quasi) intuitivo. 

SWAGGER UI

Swagger UI fornisce un'interfaccia web 
interattiva per visualizzare e testare le API.

SWAGGER CODEGEN

Swagger Codegen è un generatore automatico 
di client e server che produce codice sorgente 
in vari linguaggi. Accelera lo sviluppo e 
garantisce coerenza tra implementazione e 
documentazione API.

Vantaggi della documentazione 
OpenAPI

STANDARDIZZAZIONE

AUTOMAZIONE

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
sviluppatori.

Tools aggiuntivi

Vediamo subito in pratica quanto detto.
Per documentare le API della nostra applicazione 
avremo bisogno di un tool aggiuntivo che ci 
semplifichino il lavoro:

• swagger-ui-express: genererà l’interfaccia a 

partire da un file di configurazione (JSON in questo 
caso, ma più comunemente YAML)

Riferimento:
https://medium.com/@im_AnkitTiwari/swaggerizingyour-node-js-rest-api-a-step-by-step-guide267255bf8bbe

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

Oltre all'interfaccia intuitiva, c'è un altro grande vantaggio in 
questo approccio: una volta definita la struttura delle API nel file 
swagger.yml (e sperando che non cambi nel frattempo!), esso 
fungerà da riferimento per gli sviluppi sia lato frontend che lato 
backend anche in assenza delle implementazioni complete e in 
maniera completamente indipendente.

Risorse utili

• https://swagger.io/docs/specification/v3_0/about/
• https://editor.swagger.io
• https://medium.com/@im_AnkitTiwari/swaggerizing-yournode-js-rest-api-a-step-by-step-guide-267255bf8bbe

• https://swagger-autogen.github.io/docs/

Grazie per 
l’attenzione!

PRESENTED BY

Fabio ABBA’

fabio.abba@tc-web.it

Via Giovanni Schiaparelli 14,
10148 – Torino (TO)
E-mail: info@tc-web.it
Tel: 011 0466685