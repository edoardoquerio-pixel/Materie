# Lezione 22

## Panoramica
# Lezione G14: Strutture (`struct`) — Definizione, accesso, array di struct

## Argomenti trattati
Data Analytics, Programmazione

---
## Appunti

# Lezione G14: Strutture (`struct`) — Definizione, accesso, array di struct
**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G14 di 19 — Ore corso: 52/76
## PARTE 1 — TEORIA (3 ore)
### 1.1 Introduzione e motivazione
Nella lezione precedente (G13) abbiamo gestito una rubrica con **due array paralleli**: uno per i nomi e uno per i telefoni. Questo approccio funziona, ma ha un difetto importante: i dati che appartengono allo stesso contatto sono **sparpagliati** in strutture separate. Basta un errore di indice e nome e telefono non corrispondono più.
APPROCCIO CON ARRAY PARALLELI (G13):
nomi[0]  = "Bianchi Mario"   tel[0] = "3337654321"
nomi[1]  = "Rossi Luca"      tel[1] = "3331234567"
nomi[2]  = "Verdi Anna"      tel[2] = "3339876543"
Problema: cosa succede se ordino solo nomi[] e dimentico tel[]?
→ I dati si disallineano e la rubrica è corrotta. ❌
Le **struct** risolvono questo problema raggruppando in un'unica variabile tutti i dati che descrivono la stessa entità del mondo reale. Un contatto ha nome E telefono — perché tenerli separati?
APPROCCIO CON STRUCT:
contatti[0] → { nome: "Bianchi Mario", tel: "3337654321" }
contatti[1] → { nome: "Rossi Luca",    tel: "3331234567" }
contatti[2] → { nome: "Verdi Anna",    tel: "3339876543" }
Nome e telefono viaggiano sempre insieme. ✅
Le struct sono il primo passo verso la **programmazione orientata agli oggetti**: raggruppare dati correlati in un tipo personalizzato è esattamente il concetto alla base delle classi in Java e C++.
### 1.2 Spiegazione dell'argomento
#### Definizione di una struct
Una `struct` è un tipo di dato **composto**, definito dal programmatore, che raggruppa variabili di tipo anche diverso chiamate **campi** (o *membri*).
struct NomeStruct {
/* ... altri campi ... */
**Esempio concreto — un punto nel piano cartesiano:**
**Esempio — uno studente:**
struct Studente {
char cognome[50];
> **Importante:** la definizione di una struct NON alloca memoria — è solo la descrizione di come sarà fatto il tipo. La memoria viene allocata quando si dichiara una **variabile** di quel tipo.
#### Dichiarazione di variabili struct
Dopo aver definito la struct, si dichiarano le variabili:
struct Studente s1;           // variabile singola
struct Studente s2, s3;       // più variabili
// Inizializzazione alla dichiarazione (in ordine dei campi)
struct Studente s4 = {"Mario", "Rossi", 12345, 27.5};
**Visualizzazione in memoria:**
struct Studente s1:
┌────────────────────────────────────────────────┐
│ nome[50]  │ cognome[50] │ matricola │  media   │
│ "Mario"   │ "Rossi"     │   12345   │  27.5    │
└────────────────────────────────────────────────┘
50 byte      50 byte      4 byte     4 byte
Totale ≈ 108 byte
Tutti i campi della stessa variabile struct sono **contigui in memoria** e si spostano sempre insieme.
#### Accesso ai campi: operatore `.`
Per leggere o scrivere un campo di una struct si usa l'**operatore punto** `.`:
struct Studente s;
/* Scrittura dei campi */
strcpy(s.nome, "Luigi");
strcpy(s.cognome, "Bianchi");
s.matricola = 54321;
s.media = 29.0;
/* Lettura dei campi */
printf("Nome: %s %s\n", s.nome, s.cognome);
printf("Matricola: %d\n", s.matricola);
printf("Media: %.1f\n", s.media);
**Schema dell'operatore `.`:**
│  │    └─ campo a cui accedere
│  └─ operatore punto
└─ variabile struct
#### `typedef` — semplificare il nome del tipo
Scrivere `struct Studente` ogni volta è verboso. Il costrutto `typedef` permette di creare un **alias** più breve:
/* Senza typedef */
struct Studente s1;
struct Studente s2;
/* Con typedef */
typedef struct {
char cognome[50];
/* Ora si può scrivere semplicemente: */
> **Convenzione:** i nomi dei tipi definiti con `typedef` si scrivono con la **prima lettera maiuscola** (es. `Studente`, `Punto`, `Prodotto`).
#### Assegnazione tra struct
A differenza degli array, due variabili struct dello stesso tipo si possono assegnare direttamente con `=`: il compilatore copia tutti i campi automaticamente.
Studente a = {"Anna", "Verdi", 11111, 28.5};
b = a;   // copia TUTTI i campi di a in b ✅
/* Equivale a: */
strcpy(b.nome, a.nome);
strcpy(b.cognome, a.cognome);

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 022_22_lezione_struct_studente_completo.md*
