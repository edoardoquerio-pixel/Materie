# API RESTful — Appunti Strutturati per Sessione

> **Corso:** ITS ICT Cloud Specialist 2025-2027  
> **Materia:** 12_RESTful_API

---

## Indice delle Sessioni

1. [Introduzione a REST](#introduzione-a-rest)
2. [JSON e Formati](#json-e-formati)
3. [Progettazione API](#progettazione-api)
4. [Swagger/OpenAPI](#swagger-openapi)
5. [JWT e Autenticazione](#jwt-e-autenticazione)
6. [Guide e Istruzioni](#guide-e-istruzioni)
7. [Frontend e Test](#frontend-e-test)

---

## Introduzione a REST

### Materiali


### Contenuti


## JSON e Formati

### Materiali


### Contenuti


## Progettazione API

### Materiali


### Contenuti


## Swagger/OpenAPI

### Materiali


### Contenuti


## JWT e Autenticazione

### Materiali

- [`09_JWT_e_autenticazione.md`](00_Note/09_JWT_e_autenticazione.md)
- [`10_JWT_vs_HttpOnly_cookie.md`](00_Note/10_JWT_vs_HttpOnly_cookie.md)

### Contenuti

INTRODUZIONE 
Una delle esigenze più comuni del WEB è quella di restringere l’accessibilità di una o 
più pagine di un applicazione web ai soli utenti autenticati o addirittura ad una 
ristretta cerchia di utenti (ad es. agli utenti admin). Questa esigenza si presenta 
anche nel mondo delle API. Nella prima parte di questo articolo spiegherò il principio 
su cui si basa JWT mentre nella seconda pa

*[Contenuto troncato — vedi file completo]*

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
Se  il  sito  ha  anche  solo  una  vulnerab

*[Contenuto troncato — vedi file completo]*

---


## Guide e Istruzioni

### Materiali

- [`08_ISTRUZIONI_MUSICLAB.md`](00_Note/08_ISTRUZIONI_MUSICLAB.md)
- [`06_Guida_Essenziale_alle_API_RESTful.md`](00_Note/06_Guida_Essenziale_alle_API_RESTful.md)

### Contenuti

# 🎵 MusicLab — Esercitazione REST API con Node.js, Express e SQLite

## Obiettivo

Costruire un'API RESTful per gestire una collezione musicale, con un frontend HTML (fornito) che consenta di interagire con essa tramite interfaccia grafica.

Al termine dell'esercitazione avrai un server Node.js con Express che espone endpoint REST, un database SQLite con dati reali, e una pagina HTML funzionante p

*[Contenuto troncato — vedi file completo]*

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
<!-- a padding to disable MSIE and Chrome frien

*[Contenuto troncato — vedi file completo]*

---


## Frontend e Test

### Materiali

- [`11_script_libri.md`](00_Note/11_script_libri.md)
- [`07_index.md`](00_Note/07_index.md)
- [`12_Test_RESTful_API_Gruppi.md`](00_Note/12_Test_RESTful_API_Gruppi.md)

### Contenuti

export const CREATE_LIBRI_TABLE = `CREATE TABLE IF NOT EXISTS libri (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        titolo TEXT NOT NULL,
                                        autore TEXT NOT NULL,
                                        editore TEXT NOT NULL,
                                        genere TEXT,
            

*[Contenuto troncato — vedi file completo]*

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
<!-- a padding to disable MSIE and Chrome frien

*[Contenuto troncato — vedi file completo]*

---

Gruppo 1

Test RESTful API  •  ITS Competenze Informatiche/Digitali

Nome: ______________________________   Data: ___________

Questo fascicolo contiene 8 domande di tre tipologie:

  🔍  Correggere Errori – individua e correggi gli errori presenti

  🔗  Abbinamento – collega ogni voce della Colonna A alla voce corretta della Colonna B

  ✅  Vero o Falso – indica V o F e motiva brevemente la rispos

*[Contenuto troncato — vedi file completo]*

---


