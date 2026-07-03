# Test RESTful API Gruppi

Fonte: `Test RESTful API Gruppi.docx`

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