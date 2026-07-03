# Lezione 24

## Panoramica
# Lezione G16: Strutture e Gestione File — Lettura e Scrittura su File

## Argomenti trattati
Data Analytics, Database, API REST, Sicurezza

---
## Appunti

# Lezione G16: Strutture e Gestione File — Lettura e Scrittura su File
**Durata totale:** 4 ore
**Teoria:** 3 ore | **Esercizi:** 1 ora
**Data:** _______________
**Ambiente:** CLion (JetBrains)
**Giornata:** G16 di 19 — Ore corso: 64/76
# PARTE 1 — TEORIA (3 ore)
## 1.1 Introduzione e Motivazione
Finora tutti i dati del nostro programma esistono soltanto mentre il programma è in esecuzione: appena termina, ogni array, ogni struct, ogni variabile scompare. Immagina un programma gestionale per una piccola biblioteca: se alla chiusura del programma l'elenco dei libri viene perso, il sistema è inutilizzabile.
La **gestione dei file** risolve questo problema: permette di salvare dati su disco e rileggerne ad ogni avvio, rendendo i programmi **persistenti**.
Combinando `struct` (già note da G14–G15) con la lettura/scrittura su file otteniamo uno degli strumenti più potenti del C standard: la capacità di costruire archivi dati rudimentali, simili a un database minimo.
## 1.2 Spiegazione dell'Argomento
### 1.2.1 Il tipo `FILE` e le funzioni principali
In C la gestione dei file avviene tramite un **puntatore a FILE**:
`FILE` è un tipo definito in `<stdio.h>`. Il puntatore `fp` non punta direttamente al file su disco, ma a una struttura interna che gestisce il buffer e lo stato del file.
**Apertura e chiusura:**
fopen(nome_file, modalità)  →  restituisce FILE* oppure NULL se errore
fclose(fp)                  →  chiude il file e svuota il buffer
**Modalità di apertura:**
┌──────┬──────────────────────────────────────────────────────────┐
│ Modo │ Significato                                              │
├──────┼──────────────────────────────────────────────────────────┤
│ "r"  │ Lettura — il file deve esistere                          │
│ "w"  │ Scrittura — crea nuovo o svuota se esiste               │
│ "a"  │ Append — aggiunge in fondo, crea se non esiste           │
│ "rb" │ Lettura binaria                                          │
│ "wb" │ Scrittura binaria                                        │
│ "ab" │ Append binario                                           │
└──────┴──────────────────────────────────────────────────────────┘
### 1.2.2 File di testo vs file binari
**File di testo:** i dati vengono salvati come caratteri leggibili. Un intero `42` viene scritto come due byte: `'4'` e `'2'`. Utile per file leggibili con un editor.
**File binari:** i dati vengono scritti esattamente come sono in memoria. Un intero `42` occupa 4 byte (la sua rappresentazione binaria). Più compatti e veloci, ma non leggibili direttamente.
Testo:   [ '4' ][ '2' ][ '\n' ]   → 3 byte
Binario: [ 0x00 ][ 0x00 ][ 0x00 ][ 0x2A ]  → 4 byte (big-endian)
### 1.2.3 Operazioni su file di testo
**Scrittura con `fprintf`:**
fprintf(fp, formato, argomenti);
// Esattamente come printf, ma scrive su file
**Lettura con `fscanf`:**
fscanf(fp, formato, &variabile);
// Esattamente come scanf, ma legge da file
// Restituisce il numero di valori letti (utile per rilevare EOF)
**Lettura/scrittura di righe con `fgets` / `fputs`:**
fgets(buffer, dimensione, fp);   // legge una riga (include '\n')
fputs(stringa, fp);              // scrive una stringa (senza '\n' automatico)
**Rilevamento fine file:**
while (fscanf(fp, ...) == n_campi) { ... }  // preferibile
while (!feof(fp)) { ... }                   // meno robusto, evitare come condizione principale
### 1.2.4 Operazioni su file binari: `fwrite` e `fread`
Questi due comandi permettono di leggere/scrivere blocchi di memoria raw.
fwrite(ptr, dim_elemento, n_elementi, fp);
fread(ptr, dim_elemento, n_elementi, fp);
Entrambe restituiscono il numero di elementi effettivamente scritti/letti.
**Esempio concettuale:**
struct Libro libro = {"Il nome della rosa", "Eco", 1980};
fwrite(&libro, sizeof(struct Libro), 1, fp);
│          │                │
│          │                └── quanti elementi
│          └─────────────────── dimensione di ciascuno
└────────────────────────────── indirizzo da cui leggere
### 1.2.5 Salvataggio e caricamento di array di struct
Il pattern più comune in C per la persistenza dei dati è:
SALVATAGGIO                        CARICAMENTO
──────────                         ───────────
apri file in "wb"                  apri file in "rb"
fwrite(array, sizeof(T), n, fp)    n = fread(array, sizeof(T), MAX, fp)
chiudi file                        chiudi file
usa n come dimensione effettiva
### 1.2.6 Schema generale del flusso
├─► fopen("dati.bin", "wb") ──────────────────────────────────────►  FILE SU DISCO
│         │                                                              dati.bin
│    fwrite(&struct, sizeof, n, fp)  ────────────────────────────►   [raw bytes...]
│    fclose(fp)
└─► fopen("dati.bin", "rb") ──────────────────────────────────────►  FILE SU DISCO
│                                                              dati.bin
fread(&struct, sizeof, MAX, fp) ◄──────────────────────────────  [raw bytes...]
usa i dati in memoria
### 1.2.7 Controllo errori — sempre obbligatorio
FILE *fp = fopen("archivio.bin", "rb");
if (fp == NULL) {

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 024_24_lezione_strutture_file_studente_completo.md*
