# Lezione 19

## Panoramica
# Lezione: Pila e Coda (Stack e Queue)

## Argomenti trattati
Data Analytics, API REST, Reti

---
## Appunti

# Lezione: Pila e Coda (Stack e Queue)
**Durata totale:** 4 ore
**Teoria:** 1.5 ore | **Esercizi:** 2.5 ore
**Data:** _______________
**Ambiente:** CLion (JetBrains)
> ⚠️ NOTA DIDATTICA: Tutte le implementazioni usano **array e variabili separate** senza `struct`.
# PARTE 1 — TEORIA (1.5 ore)
## 1.1 Introduzione e Motivazione
Immagina di essere in fila alla cassa del supermercato: il primo ad arrivare è il primo a essere servito. Oppure pensa a una pila di piatti: li metti uno sopra l'altro e prendi sempre quello in cima.
Questi due scenari descrivono due strutture dati fondamentali in informatica:
- **Pila (Stack):** LIFO — *Last In, First Out* (l'ultimo inserito è il primo a uscire)
- **Coda (Queue):** FIFO — *First In, First Out* (il primo inserito è il primo a uscire)
**Dove si usano nella realtà e nei programmi?**
- **Stack:** la cronologia "Indietro" del browser, il meccanismo di chiamata delle funzioni, il controllo delle parentesi bilanciate in un compilatore, l'operazione "Annulla" (Ctrl+Z).
- **Queue:** la coda di stampa, i messaggi in attesa di elaborazione, le richieste a un server web, le animazioni in un videogioco.
## 1.2 Spiegazione dell'Argomento
### La Pila (Stack)
Una pila è una struttura in cui gli elementi vengono inseriti e rimossi sempre dalla stessa estremità, chiamata **cima** (*top*).
**Operazioni principali:**
- `push(x)` — inserisce x in cima
- `pop()` — rimuove e restituisce l'elemento in cima
- `peek()` — legge la cima senza rimuoverla
- `isEmpty()` — true se la pila è vuota
- `isFull()` — true se la pila è piena
**Visualizzazione passo-passo:**
Inizio        push(10)      push(20)      push(30)      pop()
+------+      +------+      +------+      +------+
|  10  |<top  |  20  |<top  |  30  |<top  |  20  |<top
+------+      +------+      +------+      +------+
|  10  |      |  20  |      |  10  |
+------+      +------+      +------+
top = -1      top = 0       top = 1       top = 2       top = 1
**Implementazione con array:**
Usiamo un array per memorizzare gli elementi e una variabile intera `top` come indice dell'elemento in cima. Convenzione: `top = -1` significa pila vuota.
Array:   [ 10 | 20 | 30 | -- | -- ]
indici:     0    1    2    3    4
- `push(x)`: incrementa `top`, poi assegna `pila[top] = x`
- `pop()`: salva `pila[top]`, poi decrementa `top`
### La Coda (Queue)
Una coda è una struttura in cui i nuovi elementi entrano in **fondo** (*tail*) ed escono dalla **testa** (*head*).
**Operazioni principali:**
- `enqueue(x)` — inserisce x in fondo
- `dequeue()` — rimuove e restituisce l'elemento in testa
- `isEmpty()` — true se la coda è vuota
- `isFull()` — true se la coda è piena
**Visualizzazione passo-passo:**
Inizio       enqueue(10)   enqueue(20)   enqueue(30)   dequeue()
+------+      +------+---+  +------+---+--+  +------+---+
|  10  |      |  10  |20 |  |  10  |20 |30|  |  20  |30 |
+------+      +------+---+  +------+---+--+  +------+---+
^      ^      ^         ^   ^            ^        ^      ^
h=0   t=0+1   h=0      t=1  h=0         t=2      h=1    t=2
**Implementazione con array:**
Usiamo un array e tre variabili: `head` (indice da cui si estrae), `tail` (prossimo slot libero), `size` (numero elementi presenti).
Array:   [ 10 | 20 | 30 | -- | -- ]
indici:     0    1    2    3    4
^              ^
head=0          tail=3    size=3
Dopo `dequeue()`:
Array:   [ -- | 20 | 30 | -- | -- ]
head=1     tail=3    size=2
### Il Problema della Coda Lineare
La coda lineare ha un limite importante: dopo molte operazioni di `enqueue`/`dequeue`, `tail` raggiunge la fine dell'array anche se ci sono slot liberi all'inizio (quelli già "consumati" dai `dequeue`). Lo spazio non viene mai recuperato.
Dopo 3 enqueue + 2 dequeue:
Array:   [ -- | -- | 30 | -- | -- ]   (MAX = 5)
head=2     tail=3    size=1
Posizioni 0 e 1 sono libere ma inaccessibili!
Se facessi altri 2 enqueue, tail arriverebbe a 5 → fuori dall'array.
### La Coda Circolare (Circular Buffer)
La soluzione è trattare l'array come se fosse **un cerchio**: quando `tail` raggiunge la fine, riparte dall'indice 0. Questo si ottiene con l'operatore **modulo** (`%`).
**Regola chiave:**
tail = (tail + 1) % MAX
head = (head + 1) % MAX
**Visualizzazione — array di 5 slot come cerchio:**
Stato: head=3, tail=1, size=3  →  elementi in posizioni 3, 4, 0
Array:  [ 70 | -- | -- | 30 | 50 ]
^              ^
tail=1         head=3
**Confronto passo-passo con MAX=5:**
Operazione     head  tail  size  Array (indici 0..4)

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 019_19_pila_coda_studente_completo.md*
