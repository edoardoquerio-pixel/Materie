# Lezione 21

## Panoramica
# Lezione G13: Ordinamento e Stringhe — Operazioni su stringhe con `string.h`

## Argomenti trattati
Data Analytics, API REST, Programmazione

---
## Appunti

# Lezione G13: Ordinamento e Stringhe — Operazioni su stringhe con `string.h`
**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G13 di 19 — Ore corso: 48/76
## PARTE 1 — TEORIA (3 ore)
### 1.1 Introduzione e motivazione
Nella vita reale i dati non sono solo numeri: nomi, cognomi, città, codici fiscali, email — tutto è testo. Un programma che sa gestire e ordinare stringhe è molto più vicino a un'applicazione reale.
Pensiamo a una rubrica telefonica: vogliamo visualizzare l'elenco in ordine alfabetico. Pensiamo a un motore di ricerca: deve trovare una parola all'interno di un testo. Pensiamo a un form di registrazione: deve verificare che la password abbia almeno 8 caratteri e contenga un numero.
Tutte queste operazioni richiedono la manipolazione di stringhe. In C le stringhe non sono un tipo primitivo: sono **array di `char`** terminati da un carattere speciale, il **terminatore nullo `'\0'`**. La libreria `string.h` fornisce le funzioni standard per operare su di esse in modo efficiente e sicuro.
### 1.2 Spiegazione dell'argomento
#### Le stringhe in C: struttura interna
Una stringa in C è un array di caratteri che termina obbligatoriamente con `'\0'` (valore ASCII 0):
char nome[10] = "Mario";
Indice:  [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]  [9]
Valore:  'M'  'a'  'r'  'i'  'o'  '\0'  ?    ?    ?    ?
terminatore nullo
Il terminatore `'\0'` è fondamentale: senza di esso le funzioni non sanno dove finisce la stringa e leggono dati in memoria casuali (comportamento indefinito).
#### Dichiarazione e inizializzazione
// Metodo 1: dimensione esplicita con inizializzazione letterale
char s1[20] = "Ciao";
// Memoria: 'C' 'i' 'a' 'o' '\0' ? ? ? ? ? ...
// Metodo 2: dimensione automatica (conta i char + '\0')
char s2[] = "Mondo";
// Dimensione = 6 (5 caratteri + '\0')
// Metodo 3: array non inizializzato
// Contenuto imprevedibile — va scritto prima di essere letto
// Lettura da tastiera
scanf("%s", s4);         // legge fino al primo spazio
fgets(s4, 50, stdin);    // legge l'intera riga (inclusi spazi)
**Regola critica — NON si usa `=` per assegnare dopo la dichiarazione:**
s = "Ciao";        // ❌ ERRORE di compilazione
s = s2;            // ❌ ERRORE di compilazione
strcpy(s, "Ciao"); // ✅ corretto
strcpy(s, s2);     // ✅ corretto
#### `strlen` — lunghezza della stringa
#include <string.h>
size_t strlen(const char *s);
Conta i caratteri fino a `'\0'` (escluso). Restituisce un `size_t` (intero senza segno).
"Mario"   →   strlen = 5
"Ciao"    →   strlen = 4
""        →   strlen = 0   (stringa vuota: solo '\0')
char nome[] = "Giovanni";
int len = strlen(nome);          // len = 8
char ultimo = nome[len - 1];     // ultimo = 'i'
**Uso frequente:** rimuovere `'\n'` da `fgets`:
fgets(s, sizeof(s), stdin);
if (s[strlen(s) - 1] == '\n')
s[strlen(s) - 1] = '\0';
#### `strcpy` — copia di stringa
char *strcpy(char *dest, const char *src);
Copia `src` in `dest`, incluso il `'\0'` finale. Il buffer `dest` deve essere abbastanza grande.
src:  'C' 'i' 'a' 'o' '\0'
dest: 'C' 'i' 'a' 'o' '\0'
char originale[] = "Programmazione";
char copia[20];
strcpy(copia, originale);
printf("%s\n", copia);  // stampa: Programmazione
**Attenzione al buffer overflow:**
char piccolo[5];
strcpy(piccolo, "Programmazione");  // ❌ PERICOLOSO: scrive fuori dall'array!
#### `strcat` — concatenazione
char *strcat(char *dest, const char *src);
Aggiunge `src` alla fine di `dest`, sovrascrivendo il `'\0'` di `dest`.
Prima:   dest = "Ciao, \0"       src = "Mondo\0"
↑ qui inizia la scrittura
Dopo:    dest = "Ciao, Mondo\0"
char saluto[50] = "Ciao, ";
char nome[] = "Maria";
strcat(saluto, nome);
strcat(saluto, "!");
printf("%s\n", saluto);  // stampa: Ciao, Maria!
**Regola pratica:** la dimensione di `dest` deve essere ≥ `strlen(dest) + strlen(src) + 1`.
#### `strcmp` — confronto di stringhe
int strcmp(const char *s1, const char *s2);
Confronta carattere per carattere secondo il codice ASCII. Restituisce:
┌─────────────────┬──────────────────────────────────────────┐
│ Valore ritorno  │ Significato                              │
├─────────────────┼──────────────────────────────────────────┤

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 021_21_lezione_stringhe_studente_completo.md*
