# Lezione 20

## Panoramica
# Lezione: Algoritmi di Ordinamento

## Argomenti trattati
Data Analytics, Programmazione, API REST

---
## Appunti

# Lezione: Algoritmi di Ordinamento
**Durata totale:** 4 ore
**Teoria:** 1.5 ore | **Esercizi:** 2.5 ore
**Data:** _______________
**Ambiente:** CLion (JetBrains)
## PARTE 1 — TEORIA (1.5 ore)
### 1.1 Introduzione e Motivazione
#### Perché ordinare?
Immagina di avere una rubrica telefonica con 1000 contatti in ordine casuale. Cercare "Verdi Mario" richiede di leggere ogni nome, uno per uno, fino a trovarlo — nel caso peggiore, tutti e 1000. Se invece la rubrica è in ordine alfabetico, si apre direttamente nella sezione "V" e in pochi secondi il contatto è trovato.
**Questo è il potere dell'ordinamento:** rendere i dati più facili da consultare, cercare e gestire.
Nella programmazione, ordinare un array è una delle operazioni più frequenti:
- Visualizzare una classifica di punteggi dal più alto al più basso
- Mostrare prodotti dal più economico al più costoso
- Trovare il valore minimo o massimo
- Preparare i dati per algoritmi più efficienti
#### Definizione
Ordinare un array significa riorganizzare i suoi elementi in modo che rispettino un criterio — tipicamente **crescente** (dal più piccolo al più grande) o **decrescente** (dal più grande al più piccolo).
Prima:  [64, 25, 12, 22, 11]
Dopo:   [11, 12, 22, 25, 64]   ← ordine crescente
### 1.2 Spiegazione degli Algoritmi
In questa lezione studiamo tre algoritmi classici, tutti con complessità **O(n²)**: adatti a dataset piccoli e ottimi per capire i principi fondamentali dell'ordinamento.
#### 🫧 Bubble Sort — Ordinamento a Bolle
**Idea di base:** confronta coppie di elementi adiacenti e scambiali se sono nell'ordine sbagliato. Ripeti finché l'array non è ordinato. Gli elementi grandi "affondano" verso destra come bolle che salgono.
**Visualizzazione passo-passo su `[64, 25, 12, 22, 11]`:**
[64, 25, 12, 22, 11]
64 > 25 → SCAMBIA
[25, 64, 12, 22, 11]
64 > 12 → SCAMBIA
[25, 12, 64, 22, 11]
64 > 22 → SCAMBIA
[25, 12, 22, 64, 11]
64 > 11 → SCAMBIA
[25, 12, 22, 11, 64]  ← 64 è al suo posto!
[25, 12, 22, 11 | 64]
25 > 12 → SCAMBIA
[12, 25, 22, 11 | 64]
25 > 22 → SCAMBIA
[12, 22, 25, 11 | 64]
25 > 11 → SCAMBIA
[12, 22, 11, 25 | 64]  ← 25 è al suo posto!
... continua fino a ordinamento completo ...
RISULTATO: [11, 12, 22, 25, 64]
**Struttura del codice:**
Per ogni passata i da 0 a n-2:
Per ogni posizione j da 0 a n-2-i:
Se arr[j] > arr[j+1]:
scambia arr[j] e arr[j+1]
**Caratteristiche:**
- Complessità: O(n²) — due cicli annidati
- Stabile: sì (elementi uguali non vengono scambiati)
- Semplice da capire e implementare
#### 🎯 Selection Sort — Ordinamento per Selezione
**Idea di base:** trova il minimo nell'array non ancora ordinato e mettilo nella posizione corretta. Ripeti riducendo ogni volta la porzione da esaminare.
**Visualizzazione passo-passo su `[64, 25, 12, 22, 11]`:**
PASSO 1: cerca il minimo in [64, 25, 12, 22, 11]
minimo = 11 (indice 4)
scambia posizione 0 con posizione 4
[11 | 25, 12, 22, 64]
PASSO 2: cerca il minimo in [25, 12, 22, 64]
minimo = 12 (indice 2)
scambia posizione 1 con posizione 2
[11, 12 | 25, 22, 64]
PASSO 3: cerca il minimo in [25, 22, 64]
minimo = 22 (indice 3)
scambia posizione 2 con posizione 3
[11, 12, 22 | 25, 64]
PASSO 4: cerca il minimo in [25, 64]
minimo = 25 (indice 3)
nessuno scambio necessario
[11, 12, 22, 25 | 64]
RISULTATO: [11, 12, 22, 25, 64]
**Struttura del codice:**
Per ogni posizione i da 0 a n-2:
Trova l'indice del minimo tra i e n-1
Se il minimo non è già in posizione i:
scambia arr[i] con arr[indice_minimo]
**Caratteristiche:**
- Complessità: O(n²) — sempre, anche su array già ordinato
- Numero di scambi: O(n) — al massimo n-1 scambi (vantaggio!)
- Non stabile: può scambiare elementi uguali distanti

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 020_20_lezione_ordinamento_studente_completo.md*
