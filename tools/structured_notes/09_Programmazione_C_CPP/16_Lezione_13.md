# Lezione 13

## Panoramica
Un array è una struttura dati che permette di memorizzare più valori dello stesso tipo

## Argomenti trattati
API REST

---
## Appunti

LEZIONE 13 - Array
Monodimensionali
PARTE TEORICA (2h)
1. Concetto di Array
Un array è una struttura dati che permette di memorizzare più valori dello stesso tipo
in una sequenza contigua di memoria, accessibili tramite un indice.
Perché usare gli array?
Gestire collezioni di dati correlati (es: voti di studenti, temperature del mese)
Evitare di dichiarare decine di variabili separate
Facilitare l’elaborazione di grandi quantità di dati
Permettere l’accesso rapido tramite indice
Caratteristiche principali:
Tutti gli elementi hanno lo stesso tipo di dato
La dimensione è fissa (definita alla dichiarazione)
Gli elementi sono contigui in memoria
L’accesso avviene tramite indice che parte da 0
Rappresentazione in memoria:
Array: int numeri[5];
Indici: 0 1 2 3 4
┌─────┬─────┬─────┬─────┬─────┐
numeri │ 10 │ 20 │ 30 │ 40 │ 50 │
└─────┴─────┴─────┴─────┴─────┘
Indirizzi: 1000 1004 1008 1012 1016 (ogni int occupa 4 byte)
2. Dichiarazione e Inizializzazione
tipo nomeArray[dimensione];
Esempi di dichiarazione:
// Array di 30 interi
float temperature[12]; // Array di 12 float
// Array di 50 caratteri
double prezzi[100];
// Array di 100 double
Inizializzazione:
// Metodo 1: Inizializzazione alla dichiarazione
int numeri[5] = {10, 20, 30, 40, 50};
// Metodo 2: Inizializzazione parziale (i restanti elementi sono 0)
int numeri[5] = {10, 20}; // {10, 20, 0, 0, 0}
// Metodo 3: Dimensione automatica
int numeri[] = {10, 20, 30, 40, 50}; // Dimensione = 5
// Metodo 4: Inizializzazione a zero
int numeri[5] = {0}; // Tutti gli elementi a 0
// Metodo 5: Senza inizializzazione (valori casuali!)
int numeri[5]; // ATTENZIONE: contiene valori casuali (garbage)
Esempio completo:
#include <stdio.h>
// Dichiarazione e inizializzazione
int numeri[5] = {10, 20, 30, 40, 50};
// Dichiarazione senza inizializzazione
float temperature[7];
// Inizializzazione manuale
temperature[0] = 18.5;
temperature[1] = 19.2;
temperature[2] = 21.0;
temperature[3] = 22.5;
temperature[4] = 20.8;
temperature[5] = 19.5;
temperature[6] = 18.0;
3. Accesso agli Elementi
L’accesso agli elementi avviene tramite l’operatore di indicizzazione [] utilizzando un
indice da 0 a dimensione-1.
nomeArray[indice]
Lettura e scrittura:
int numeri[5] = {10, 20, 30, 40, 50};
int primo = numeri[0];
int terzo = numeri[2];
int ultimo = numeri[4]; // ultimo = 50
numeri[0] = 100; // Modifica il primo elemento
numeri[2] = 300; // Modifica il terzo elemento
// Uso in espressioni
int somma = numeri[0] + numeri[1]; // somma = 100 + 20 = 120
numeri[3] = numeri[1] * 2;
// numeri[3] = 20 * 2 = 40
ATTENZIONE agli indici:
// CORRETTO: indici da 0 a 4
array[0] = 10; // OK
array[4] = 50; // OK
// ERRORE: indice fuori range
// ERRORE! Non esiste array[5]
array[-1] = 10; // ERRORE! Indice negativo
array[10] = 99; // ERRORE! Accesso fuori dai limiti
Conseguenze degli errori di indice:

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 013_lezione_13_array.md*
