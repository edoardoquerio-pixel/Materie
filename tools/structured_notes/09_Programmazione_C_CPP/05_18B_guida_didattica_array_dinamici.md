# 18B guida didattica array dinamici

## Panoramica
## Array Dinamici in C: malloc e calloc

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

# GUIDA DIDATTICA - LEZIONE 20
## Array Dinamici in C: malloc e calloc
### DURATA TOTALE: 5 ORE (con realloc)
## STRUTTURA DELLA LEZIONE
### Parte 1: MOTIVAZIONE (30 minuti)
- Limite degli array statici
- Concetto di allocazione dinamica
- Stack vs Heap
### Parte 2: MALLOC (60 minuti)
- Sintassi e parametri
- sizeof e calcolo dei byte
- Controllo NULL
- free e buone pratiche
### Parte 3: CALLOC (45 minuti)
- Sintassi e differenze da malloc
- Quando usare calloc
- Esempi pratici
### Parte 4: REALLOC (45 minuti)
- Ridimensionare la memoria
- Sintassi e comportamento
- Array dinamici che crescono
### Parte 5: PRATICA GUIDATA (60 minuti)
- Tre esercizi costruiti insieme alla classe
### Parte 6: ERRORI COMUNI E RIEPILOGO (45 minuti)
- Dangling pointer
- Riepilogo e domande
## PARTE 1: MOTIVAZIONE (30 minuti)
### 1.1 Il Problema degli Array Statici (10 min)
Scrivi questo codice alla lavagna e chiedi alla classe cosa non va:
int voti[30];  // Cosa succede se ho 31 studenti?
// Cosa succede se ho solo 5 studenti?
**Problema 1 — Dimensione fissa troppo piccola:**
#define MAX 30
// Arriva il 31° studente...
// Non c'è spazio! Non possiamo fare nulla.
**Problema 2 — Spreco di memoria:**
int voti[1000];  // Alloco spazio per 1000 studenti
// Oggi ci sono solo 5 studenti.
// 995 spazi allocati per nulla!
**Problema 3 — Dimensione non nota a priori:**
// L'utente decide quanti elementi vuole a runtime.
// Con un array statico non possiamo saperlo
// prima di eseguire il programma.
printf("Quanti voti? ");
scanf("%d", &n);
int voti[n];  // ⚠️ VLA: tecnicamente permesso in C99
// ma sconsigliato: non funziona su tutti i compilatori
// e non è mai sicuro per dimensioni grandi
> "Ci serve un modo per allocare la **quantità esatta** di memoria necessaria, decidendo **durante l'esecuzione**."
### 1.2 Memoria Statica vs Dinamica (10 min)
**Dove vivono le variabili in C?**
┌──────────────────────────────────────────┐
│                MEMORIA                   │
├──────────────────────────────────────────┤
│  STACK (pila delle chiamate)             │
│  • Variabili locali                      │
│  • Parametri delle funzioni              │
│  • Gestita automaticamente               │
│  • Dimensione limitata (~1-8 MB)         │
│                                          │
│  int x = 10;      → qui                  │
│  int arr[5];      → qui                  │
├──────────────────────────────────────────┤
│  HEAP (memoria libera)                   │
│  • Allocazione dinamica con malloc/calloc│
│  • Gestita MANUALMENTE dal programmatore │
│  • Dimensione molto grande (GB)          │
│  • Deve essere liberata con free()       │
│                                          │
│  malloc(...)      → alloca qui           │
│  calloc(...)      → alloca qui           │
└──────────────────────────────────────────┘
**Schema con esempio concreto:**
Codice:                   Memoria durante l'esecuzione:
int n = 5;                STACK:
int* arr = malloc(...);   ┌─────────────────┐
│ n      = 5      │
│ arr    = 0x2A00 │ → punta alla heap
└─────────────────┘
HEAP (indirizzo 0x2A00):

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 018_18B_guida_didattica_array_dinamici.md*
