# Lezione 2

## Panoramica
Competenze informatiche/digitali

## Argomenti trattati
Git, API REST, Sicurezza, Data Analytics

---
## Appunti

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
*Fonte: 002_2_-_JSON_request_e_response.md*
