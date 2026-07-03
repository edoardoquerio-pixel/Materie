# Lezione 23

## Panoramica
# Lezione G15: Strutture, Oggetti e Progetto Faber

## Argomenti trattati
Data Analytics, API REST, Programmazione, Sicurezza

---
## Appunti

# Lezione G15: Strutture, Oggetti e Progetto Faber
**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G15 di 19 — Ore corso: 56/76
## PARTE 1 — TEORIA (3 ore)
### 1.1 Introduzione e motivazione
Immagina di dover gestire un archivio di dipendenti di un'azienda. Per ogni dipendente ti servono: nome, cognome, età, stipendio, reparto. Con quello che sai finora, dovresti usare array separati:
char nomi[100][50];
char cognomi[100][50];
float stipendi[100];
char reparti[100][30];
Questo approccio è fragile: se vuoi spostare il dipendente numero 5 in un'altra posizione, devi aggiornare tutti e cinque gli array separatamente. Un errore è quasi garantito.
Le **strutture** (`struct`) risolvono questo problema: permettono di raggruppare dati di tipo diverso sotto un unico nome. Sono il mattone fondamentale della programmazione orientata ai dati — e, come vedremo, il precursore diretto degli **oggetti** della programmazione orientata agli oggetti (OOP).
Il **Progetto Faber** è un sistema gestionale per un negozio di strumenti musicali. Oggi costruiremo insieme le strutture dati che lo sostengono: un catalogo di strumenti, un registro di vendite, e le funzioni per gestirli.
### 1.2 Spiegazione dell'argomento
#### 1.2.1 Ripasso: cos'è una `struct`
Una `struct` è un tipo di dato composto, definito dal programmatore, che raccoglie variabili (chiamate **campi** o **membri**) anche di tipo diverso.
struct NomeTipo {
**Dichiarazione di una variabile:**
struct NomeTipo variabile;
**Accesso ai campi (operatore punto):**
variabile.campo1 = valore;
**Memoria — come è organizzata una struct:**
struct Punto { int x; int y; };
+--------+--------+
|   x    |   y    |
| 4 byte | 4 byte |
+--------+--------+
indirizzo della struct
Ogni campo occupa spazio contiguo in memoria. La dimensione totale è (almeno) la somma dei campi — il compilatore può aggiungere padding per l'allineamento.
#### 1.2.2 `typedef` — dare un nome pulito alla struct
Scrivere `struct Strumento s;` ogni volta è verboso. Con `typedef` possiamo rinominare il tipo:
typedef struct {
char categoria[30];
Ora possiamo scrivere semplicemente:
Questa è la forma moderna e preferita in C.
#### 1.2.3 Inizializzazione di una struct
**Modo 1 — inizializzazione per posizione:**
Strumento s = {"Chitarra Classica", "Cordofoni", 349.90f, 5};
**Modo 2 — inizializzazione per nome (C99, più leggibile):**
Strumento s = {
.nome = "Chitarra Classica",
.categoria = "Cordofoni",
.prezzo = 349.90f,
**Modo 3 — assegnazione campo per campo:**
strcpy(s.nome, "Chitarra Classica");
strcpy(s.categoria, "Cordofoni");
s.prezzo = 349.90f;
s.quantita = 5;
⚠️ Per i campi stringa, non usare `=` ma sempre `strcpy()` — oppure `snprintf()` se vuoi più sicurezza.
#### 1.2.4 Array di struct
È la combinazione più utile: un catalogo, un archivio, un registro.
Strumento catalogo[100]:
catalogo[0]             catalogo[1]             catalogo[2]
+------------------+   +------------------+   +------------------+
| nome: "Chitarra" |   | nome: "Violino"  |   | nome: "Tromba"   |
| cat:  "Cordof."  |   | cat:  "Cordof."  |   | cat:  "Ottoni"   |
| prezzo: 349.90   |   | prezzo: 890.00   |   | prezzo: 520.00   |
| quantita: 5      |   | quantita: 2      |   | quantita: 8      |
+------------------+   +------------------+   +------------------+
catalogo[0].prezzo = 399.90f;
printf("%s: %.2f €\n", catalogo[1].nome, catalogo[1].prezzo);
#### 1.2.5 Struct come parametri di funzione
**Passaggio per valore (copia):** la funzione riceve una copia. Modifiche non si propagano.
void stampa_strumento(Strumento s) {
printf("[%s] %s — %.2f €, qty: %d\n",
s.categoria, s.nome, s.prezzo, s.quantita);
**Passaggio per indirizzo (puntatore):** la funzione lavora sull'originale. Modifiche si propagano. Si usa l'operatore `->` per accedere ai campi.
void applica_sconto(Strumento *s, float percentuale) {
s->prezzo *= (1.0f - percentuale / 100.0f);
Regola pratica:
- Se la funzione **legge** la struct → passa per valore (o `const *`)
- Se la funzione **modifica** la struct → passa per puntatore
#### 1.2.6 Operatore `->` vs `.`
Strumento s;          →  s.prezzo         (variabile diretta)
Strumento *p = &s;   →  p->prezzo        (puntatore)
(*p).prezzo      (equivalente, ma più verboso)
Accesso diretto:              Accesso tramite puntatore:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 023_23_lezione_strutture_oggetti_faber_studente_completo.md*
