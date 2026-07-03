# Lezione 7

## Panoramica
LEZIONE 7 - Variabili e Tipi di Dato

## Argomenti trattati
Data Analytics, API REST

---
## Appunti

LEZIONE 7 - Variabili e Tipi di Dato
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
7.1 Concetto di Variabile (15 min)
Cos’è una Variabile?
Una variabile è un contenitore che può memorizzare un valore in memoria durante
l’esecuzione del programma.
Analogia: Una variabile è come una scatola etichettata:
Nome (etichetta): identifica la variabile
Tipo (dimensione scatola): determina cosa può contenere
Valore (contenuto): dato memorizzato
Indirizzo (posizione): dove si trova in memoria
┌─────────────────────┐
│ Nome: eta │ ← Etichetta
├─────────────────────┤
│ Tipo: int │ ← Tipo di dato
├─────────────────────┤
│ Valore: 25 │ ← Contenuto
├─────────────────────┤
│ Indirizzo: 0x7fff │ ← Posizione memoria
└─────────────────────┘
Caratteristiche Variabili in C
1. Tipizzazione Statica:
Il tipo è dichiarato e non cambia
Controllato a compile-time
// x è intero e rimarrà intero
// ERRORE! Non puoi assegnare stringa
2. Dichiarazione Obbligatoria:
Devi dichiarare prima di usare
Il compilatore riserva spazio in memoria
// Dichiarazione
// Assegnazione
// Dichiarazione + Inizializzazione
3. Scope (Ambito):
Locali: dentro funzioni, visibili solo lì
Globali: fuori funzioni, visibili ovunque
int globale = 100; // Variabile globale
int locale = 50; // Variabile locale
printf("%d\n", globale); // OK
printf("%d\n", locale);
void altra_funzione() {
printf("%d\n", globale); // OK
printf("%d\n", locale);
// ERRORE! locale non visibile qui
Memoria e Variabili
Quando dichiari una variabile, il compilatore:
Alloca spazio in memoria (RAM o registri)
Assegna indirizzo univoco
Associa nome all’indirizzo
Esempio in memoria:
Indirizzo | Variabile | Valore
----------|-----------|--------
0x1000 | int x | 42
0x1004 | float y | 3.14
0x1008 | char c | 'A'
0x1009 | int z | 100
7.2 Tipi di Dato Primitivi (25 min)
Il C offre diversi tipi primitivi (built-in) per memorizzare dati.
1. int (Integer)
int anno = 2024;
int temperatura = -5;
Dimensione: tipicamente 4 byte (32 bit)
Range: -2,147,483,648 a +2,147,483,647
Uso: numeri interi, contatori, indici
2. short (Short Integer)
short giorno = 15;
short mese = 10;
Dimensione: tipicamente 2 byte (16 bit)
Range: -32,768 a +32,767
Uso: quando serve meno spazio
3. long (Long Integer)
long popolazione = 1400000000L; // Nota la 'L'
long distanza = 384400000L;
Dimensione: tipicamente 4 o 8 byte
Range: almeno come int, spesso 64 bit
Uso: numeri molto grandi
long long big_number = 9223372036854775807LL; // Nota 'LL'
Dimensione: 8 byte (64 bit)
Range: -9,223,372,036,854,775,808 a +9,223,372,036,854,775,807
Uso: numeri enormi (timestamp, grandi calcoli)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 007_lezione7_variabili_input.md*
