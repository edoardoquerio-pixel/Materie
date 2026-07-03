# Lezione 16

## Panoramica
### Parte 1: INTRODUZIONE E CONCETTO (30 minuti)

## Argomenti trattati
API REST, Programmazione, Reti

---
## Appunti

# GUIDA DIDATTICA - LEZIONE 19
## Puntatori in C
### DURATA TOTALE: 4 ORE
## STRUTTURA DELLA LEZIONE
### Parte 1: INTRODUZIONE E CONCETTO (30 minuti)
- Cos'è un puntatore
- Analogia della memoria
- Perché sono importanti
### Parte 2: SINTASSI E OPERATORI (60 minuti)
- Operatori & e *
- Dichiarazione e inizializzazione
- Puntatori e costanti
- Errori comuni
### Parte 3: PUNTATORI E ARRAY (60 minuti)
- Relazione array-puntatori
- Aritmetica dei puntatori
- Notazione equivalente
- Iterazione con puntatori
### Parte 4: PASSAGGIO PER RIFERIMENTO (45 minuti)
- Problema del passaggio per valore
- Soluzione con puntatori
- Funzioni che modificano variabili
- Restituzione multipli valori
### Parte 5: PUNTATORI E STRINGHE (45 minuti)
- Stringhe come puntatori
- Funzioni con stringhe
- Array di stringhe
## PARTE 1: INTRODUZIONE E CONCETTO (30 minuti)
### 1.1 Motivazione (5 min)
**Problema con le funzioni normali:**
void incrementa(int x) {
printf("Dentro funzione: x = %d\n", x);
int numero = 10;
incrementa(numero);
printf("Fuori funzione: numero = %d\n", numero);
Dentro funzione: x = 11
Fuori funzione: numero = 10  ← Non è cambiato!
> "La funzione riceve una COPIA del valore, non può modificare l'originale. I puntatori risolvono questo problema!"
### 1.2 Cos'è un Puntatore? (10 min)
**Definizione:**
> Un **puntatore** è una variabile che contiene l'**indirizzo di memoria** di un'altra variabile.
**Analogia dell'edificio:**
La memoria è come un EDIFICIO con appartamenti:
┌─────────────┐
│  0x1000     │ ← Appartamento 1000
│  [int x=42] │    Contiene il valore 42
├─────────────┤
│  0x1004     │ ← Appartamento 1004
│  [int y=10] │    Contiene il valore 10
├─────────────┤
│  0x1008     │ ← Appartamento 1008
│  [int* p]   │    Contiene l'indirizzo 0x1000
│  =0x1000    │    (punta ad x!)
└─────────────┘
Un puntatore è come un POST-IT che dice:
"Il valore che cerchi è nell'appartamento 1000"
**In sintesi:**
- Una variabile **normale** contiene un **valore**
- Un **puntatore** contiene un **indirizzo**
### 1.3 Perché Sono Importanti? (10 min)
**I puntatori permettono di:**
1. **Modificare variabili nelle funzioni** (passaggio per riferimento)
void modifica(int* p) {
*p = 100;  // Cambia l'originale!
2. **Gestire array in modo efficiente**
void stampaArray(int* arr, int dim) {
for (int i = 0; i < dim; i++) {
printf("%d ", arr[i]);
3. **Manipolare stringhe**
char* str = "Ciao";
while (*str != '\0') {
printf("%c", *str);
4. **Creare strutture dati dinamiche** (liste, alberi, grafi)
- Vedremo in seguito con `malloc` e allocazione dinamica
5. **Evitare copie di grandi struct**
void stampaStudente(Studente* s) {  // Passa solo l'indirizzo!
printf("%s\n", s->nome);
### 1.4 Visualizzazione Iniziale (5 min)
Scrivi alla lavagna questo schema:
VARIABILE vs PUNTATORE

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 016_16_guida_didattica_puntatori.md*
