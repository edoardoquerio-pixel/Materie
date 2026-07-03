# Lezione 16

Fonte: `guida didattica lezione16.md`

# GUIDA DIDATTICA - LEZIONE 16
## Funzioni: Parte 2 (Ricorsione, Prototipazione, Best Practices)

### DURATA TOTALE: 4 ORE

---

## STRUTTURA DELLA LEZIONE

### Parte 1: RIPASSO (1 ora)
- Svolgimento esercizi di ripasso Lezione 15
- Correzione e discussione

### Parte 2: TEORIA LEZIONE 16 (1.5 ore)
- Funzioni ricorsive
- Prototipazione
- Funzioni void avanzate
- Variabili static
- Best practices

### Parte 3: PRATICA GUIDATA (1 ora)
- Esercizi svolti insieme

### Parte 4: ESERCIZI AUTONOMI (30 minuti)
- Esercizi individuali o a coppie

---

## PARTE 1: RIPASSO (60 minuti)

### Attività: Svolgimento Esercizi Ripasso

**Organizzazione:**
- I primi 3 esercizi: guidati insieme
- Esercizio 4: a coppie o individualmente
- Esercizio sfida: facoltativo per chi finisce prima

**Tempistiche:**
- Esercizio 1: 10 min
- Esercizio 2: 10 min
- Esercizio 3: 10 min
- Esercizio 4: 15 min
- Correzione e discussione: 15 min

**Punti chiave da ribadire durante la correzione:**
- L'importanza dei prototipi
- Il passaggio per valore delle variabili semplici
- Gli array vengono passati per riferimento (anticipazione!)
- La validazione dell'input nelle funzioni

---

## PARTE 2: TEORIA LEZIONE 16 (90 minuti)

### 2.1 FUNZIONI RICORSIVE (35 minuti)

**Introduzione (5 min):**
> "Una funzione ricorsiva è come le matrioske russe: ogni funzione contiene una versione più piccola di sé stessa!"

**Concetti fondamentali:**
1. **Caso base**: condizione di uscita (SEMPRE necessario!)
2. **Caso ricorsivo**: chiamata a sé stessa con parametri ridotti

**Esempio 1: Fattoriale (10 min)**

esempio:
```
5! = 5 × 4!
   = 5 × 4 × 3!
   = 5 × 4 × 3 × 2!
   = 5 × 4 × 3 × 2 × 1!
   = 5 × 4 × 3 × 2 × 1
   = 120
```

codice:
```c
int fattoriale(int n) {
    // Caso base: STOP!
    if (n == 0 || n == 1) {
        return 1;
    }
    // Caso ricorsivo: chiama sé stessa
    return n * fattoriale(n - 1);
}
```

**Visualizzazione dello stack (10 min):**

Stack per `fattoriale(5)`:
```
╔═══════════════╗
║ fattoriale(5) ║ → aspetta fattoriale(4)
╠═══════════════╣
║ fattoriale(4) ║ → aspetta fattoriale(3)
╠═══════════════╣
║ fattoriale(3) ║ → aspetta fattoriale(2)
╠═══════════════╣
║ fattoriale(2) ║ → aspetta fattoriale(1)
╠═══════════════╣
║ fattoriale(1) ║ → RITORNA 1 ✓
╚═══════════════╝

Poi risale:
fattoriale(2) ritorna 2 × 1 = 2
fattoriale(3) ritorna 3 × 2 = 6
fattoriale(4) ritorna 4 × 6 = 24
fattoriale(5) ritorna 5 × 24 = 120
```

**⚠️ ATTENZIONE: Errori comuni (5 min)**

Cosa NON fare:
```c
// ERRORE 1: Manca il caso base
int sbagliata(int n) {
    return n * sbagliata(n - 1);  // Ricorsione infinita!
}

// ERRORE 2: Caso base irraggiungibile
int sbagliata2(int n) {
    if (n == 0) return 0;
    return n + sbagliata2(n + 1);  // n aumenta invece di diminuire!
}
```

**Esempio 2: Somma primi N numeri (5 min)**

```c
int somma(int n) {
    if (n == 0) return 0;         // Caso base
    return n + somma(n - 1);      // Caso ricorsivo
}

// somma(5) = 5 + somma(4)
//          = 5 + 4 + somma(3)
//          = 5 + 4 + 3 + 2 + 1 + 0
//          = 15
```

**🎯 ESERCIZIO RAPIDO DA FARE INSIEME:**
"Scriviamo insieme una funzione ricorsiva per calcolare la potenza: `pow(base, esp)`"

Soluzione:
```c
int potenza(int base, int esp) {
    if (esp == 0) return 1;              // Qualsiasi numero^0 = 1
    return base * potenza(base, esp - 1);
}
```

---

### 2.2 PROTOTIPAZIONE (20 minuti)

**Motivazione (5 min):**

Problema:
```c
// Questo NON compila!
int main() {
    int risultato = somma(5, 3);  // ERRORE: somma non è ancora stata dichiarata
    return 0;
}

int somma(int a, int b) {
    return a + b;
}
```

**Soluzione: Prototipazione (5 min)**

```c
// PROTOTIPO (dichiarazione)
int somma(int a, int b);

// Main può stare in alto
int main() {
    int risultato = somma(5, 3);  // OK!
    return 0;
}

// DEFINIZIONE (implementazione)
int somma(int a, int b) {
    return a + b;
}
```

**Vantaggi della prototipazione:**
1. Main() in alto → più leggibile
2. Funzioni che si chiamano a vicenda
3. Separazione interfaccia/implementazione
4. Preparazione per header files (.h)

**Ricorsione mutua (10 min):**

```c
// Senza prototipi: ERRORE!
int pari(int n) {
    if (n == 0) return 1;
    return dispari(n - 1);  // ERRORE: dispari non dichiarata!
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n - 1);
}
```

```c
// Con prototipi: OK!
int pari(int n);      // Prototipo
int dispari(int n);   // Prototipo

int pari(int n) {
    if (n == 0) return 1;
    return dispari(n - 1);  // OK!
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n - 1);     // OK!
}
```

---

### 2.3 FUNZIONI VOID AVANZATE (15 minuti)

**Richiamo concetto (3 min):**
- void = nessun valore di ritorno
- Utili per: stampa, modifica array, operazioni

**Esempi pratici (7 min):**

```c
// 1. Stampa formattata
void stampaIntestazione(char titolo[]) {
    printf("\n");
    printf("================================\n");
    printf("  %s\n", titolo);
    printf("================================\n");
}

// 2. Modifica array
void azzeraArray(int arr[], int dim) {
    for (int i = 0; i < dim; i++) {
        arr[i] = 0;
    }
}

// 3. Return anticipato
void stampaSePositivo(int n) {
    if (n <= 0) {
        printf("Numero non valido!\n");
        return;  // Esce subito
    }
    printf("Numero valido: %d\n", n);
}
```

**💡 IMPORTANTE (5 min):**

> "Le funzioni void NON ritornano valori, ma possono MODIFICARE gli array che ricevono come parametri!"

Esempio:
```c
void raddoppiaValori(int arr[], int dim) {
    for (int i = 0; i < dim; i++) {
        arr[i] *= 2;
    }
}

int main() {
    int numeri[] = {1, 2, 3, 4, 5};
    raddoppiaValori(numeri, 5);
    // numeri è ora {2, 4, 6, 8, 10}
}
```

---

### 2.4 VARIABILI STATIC (10 minuti)

**Introduzione (3 min):**
> "Le variabili static sono come la memoria di una funzione: ricordano il loro valore tra una chiamata e l'altra!"

**Esempio contatore (4 min):**

```c
void contatoreNormale() {
    int contatore = 0;  // Ricomincia da 0 ogni volta
    contatore++;
    printf("Chiamata #%d\n", contatore);
}

void contatoreStatic() {
    static int contatore = 0;  // Si inizializza UNA SOLA VOLTA
    contatore++;
    printf("Chiamata #%d\n", contatore);
}

int main() {
    contatoreNormale();  // Stampa: 1
    contatoreNormale();  // Stampa: 1 (riparte da 0!)
    contatoreNormale();  // Stampa: 1
    
    printf("\n");
    
    contatoreStatic();   // Stampa: 1
    contatoreStatic();   // Stampa: 2
    contatoreStatic();   // Stampa: 3 (ricorda il valore!)
}
```

**Quando usare static (3 min):**
- Contatori di chiamate
- Cache/memoization
- Generatori di ID univoci
- Stato interno della funzione

---

### 2.5 BEST PRACTICES (10 minuti)

**1. Nomi significativi**
```c
// ❌ BAD
int f(int x, int y) { return x + y; }

// ✅ GOOD
int calcolaSomma(int addendo1, int addendo2) {
    return addendo1 + addendo2;
}
```

**2. Una funzione, un compito**
```c
// ❌ BAD: fa troppe cose
void gestisciUtente(char nome[], int eta) {
    printf("Nome: %s\n", nome);
    printf("Età: %d\n", eta);
    if (eta >= 18) {
        printf("Maggiorenne\n");
    }
    // calcoli complessi...
    // validazioni...
    // salvataggio...
}

// ✅ GOOD: funzioni separate
void stampaUtente(char nome[], int eta);
int isMaggiorenne(int eta);
void salvaUtente(char nome[], int eta);
```

**3. Validazione input**
```c
float dividi(float a, float b) {
    if (b == 0) {
        printf("ERRORE: divisione per zero!\n");
        return 0;
    }
    return a / b;
}
```

**4. Principio DRY (Don't Repeat Yourself)**
```c
// ❌ Codice ripetuto
printf("Area rettangolo 1: %d\n", base1 * altezza1);
printf("Area rettangolo 2: %d\n", base2 * altezza2);
printf("Area rettangolo 3: %d\n", base3 * altezza3);

// ✅ Usa una funzione
int calcolaArea(int base, int altezza) {
    return base * altezza;
}
```

**5. Principio KISS (Keep It Simple, Stupid)**
```c
// ❌ Troppo complesso
int isPari(int n) {
    if (n % 2 == 0) {
        return 1;
    } else {
        return 0;
    }
}

// ✅ Semplice e chiaro
int isPari(int n) {
    return n % 2 == 0;
}
```

---

## PARTE 3: PRATICA GUIDATA (60 minuti)

### Esercizio Guidato 1: Fibonacci Ricorsivo (15 min)

**Da fare insieme alla lavagna/schermo:**

```c
/*
Sequenza di Fibonacci:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Regola:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
*/

int fibonacci(int n) {
    // Casi base
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    // Caso ricorsivo
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    printf("Sequenza di Fibonacci:\n");
    for (int i = 0; i <= 10; i++) {
        printf("fib(%d) = %d\n", i, fibonacci(i));
    }
    return 0;
}
```

**Discussione:**
- Disegnare l'albero delle chiamate per `fibonacci(5)`
- Far notare che calcola gli stessi valori più volte
- Introdurre il concetto di memoization (opzionale)

---

### Esercizio Guidato 2: Conta Cifre Ricorsivo (15 min)

**Problema:**
"Creiamo una funzione ricorsiva che conta quante cifre ha un numero"

**Ragionamento insieme:**
- 5 → 1 cifra
- 42 → 2 cifre
- 123 → 3 cifre

**Approccio ricorsivo:**
- Caso base: n < 10 → 1 cifra
- Caso ricorsivo: conta 1 + cifre(n/10)

**Soluzione:**
```c
int contaCifre(int n) {
    // Gestione numeri negativi
    if (n < 0) {
        n = -n;
    }
    
    // Caso base
    if (n < 10) {
        return 1;
    }
    
    // Caso ricorsivo
    return 1 + contaCifre(n / 10);
}

// Test
printf("123 ha %d cifre\n", contaCifre(123));     // 3
printf("5 ha %d cifre\n", contaCifre(5));         // 1
printf("9876 ha %d cifre\n", contaCifre(9876));   // 4
```

---

### Esercizio Guidato 3: Menu con Funzioni (30 min)

**Creare insieme un menu interattivo che usa tutte le tecniche:**

```c
#include <stdio.h>

// Prototipi
void stampaMenu();
int leggiScelta();
void eseguiScelta(int scelta);
int fattoriale(int n);
int fibonacci(int n);
int potenza(int base, int esp);
void stampaStatistiche();

// Variabile static per statistiche
static int totaleOperazioni = 0;

int main() {
    int scelta;
    
    do {
        stampaMenu();
        scelta = leggiScelta();
        eseguiScelta(scelta);
    } while (scelta != 0);
    
    printf("\nProgramma terminato.\n");
    stampaStatistiche();
    
    return 0;
}

void stampaMenu() {
    printf("\n================================\n");
    printf("   CALCOLATRICE RICORSIVA\n");
    printf("================================\n");
    printf("1. Fattoriale\n");
    printf("2. Fibonacci\n");
    printf("3. Potenza\n");
    printf("4. Statistiche\n");
    printf("0. Esci\n");
    printf("================================\n");
}

int leggiScelta() {
    int scelta;
    printf("Scelta: ");
    scanf("%d", &scelta);
    return scelta;
}

void eseguiScelta(int scelta) {
    int n, base, esp;
    
    switch (scelta) {
        case 1:
            printf("Inserisci n: ");
            scanf("%d", &n);
            printf("%d! = %d\n", n, fattoriale(n));
            totaleOperazioni++;
            break;
            
        case 2:
            printf("Inserisci n: ");
            scanf("%d", &n);
            printf("fib(%d) = %d\n", n, fibonacci(n));
            totaleOperazioni++;
            break;
            
        case 3:
            printf("Inserisci base: ");
            scanf("%d", &base);
            printf("Inserisci esponente: ");
            scanf("%d", &esp);
            printf("%d^%d = %d\n", base, esp, potenza(base, esp));
            totaleOperazioni++;
            break;
            
        case 4:
            stampaStatistiche();
            break;
            
        case 0:
            printf("Uscita...\n");
            break;
            
        default:
            printf("Scelta non valida!\n");
    }
}

int fattoriale(int n) {
    if (n == 0 || n == 1) return 1;
    return n * fattoriale(n - 1);
}

int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int potenza(int base, int esp) {
    if (esp == 0) return 1;
    return base * potenza(base, esp - 1);
}

void stampaStatistiche() {
    printf("\n=== STATISTICHE ===\n");
    printf("Operazioni eseguite: %d\n", totaleOperazioni);
}
```

---

## PARTE 4: ESERCIZI AUTONOMI (30 minuti)

**Assegna gli esercizi del file "esercizi_lezione16.md"**

**Organizzazione:**
- Esercizi 1-2: individuali (base)
- Esercizi 3-4: a coppie (intermedi)
- Esercizio sfida: per chi finisce prima

**Circola tra i banchi per:**
- Rispondere a domande
- Verificare la comprensione
- Aiutare chi è in difficoltà
- Sfidare chi è avanti

---

## CHIUSURA E DOMANDE (10 minuti)

### Riepilogo Rapido:

**Oggi abbiamo imparato:**
1. ✅ Le funzioni ricorsive (caso base + caso ricorsivo)
2. ✅ La prototipazione delle funzioni
3. ✅ Le funzioni void avanzate
4. ✅ Le variabili static
5. ✅ Le best practices

### Domande per verificare comprensione:

1. "Cosa succede se dimentichi il caso base in una funzione ricorsiva?"
2. "Perché usiamo i prototipi?"
3. "Qual è la differenza tra una variabile locale normale e una static?"

---

<details>
<summary><b>📝 RISPOSTE PER IL DOCENTE</b></summary>

### 1. Cosa succede senza caso base?

**Risposta attesa dagli studenti:**
- Si ottiene una ricorsione infinita
- La funzione continua a chiamare se stessa all'infinito
- Si esaurisce la memoria dello stack (stack overflow)
- Il programma va in crash con errore "Segmentation fault"

**Dimostrazione pratica da fare:**
```c
// Mostra questo codice ed eseguilo
int sbagliata(int n) {
    printf("n = %d\n", n);
    return n + sbagliata(n - 1);  // Nessun caso base!
}

int main() {
    sbagliata(5);
    return 0;
}

// Output:
// n = 5
// n = 4
// n = 3
// ...
// n = -9834
// ...
// Segmentation fault (core dumped)
```

**Approfondimento per gli studenti avanzati:**
- Lo stack ha dimensione limitata (tipicamente 1-8 MB)
- Ogni chiamata ricorsiva aggiunge un "frame" allo stack
- Quando lo stack si riempie → crash
- Alcuni linguaggi hanno "tail call optimization" che previene questo problema

---

### 2. Perché usiamo i prototipi?

**Risposta attesa dagli studenti:**
- Per poter chiamare funzioni prima di definirle
- Per tenere il main() in alto nel file
- Per permettere a funzioni di chiamarsi a vicenda

**Spiegazione completa da dare:**

**Motivo 1: Ordine di lettura del compilatore**
```c
// Senza prototipo: ERRORE!
int main() {
    somma(5, 3);  // ERRORE: somma non è ancora stata dichiarata!
    return 0;
}

int somma(int a, int b) {
    return a + b;
}

// Con prototipo: OK!
int somma(int a, int b);  // Prototipo

int main() {
    somma(5, 3);  // OK: il compilatore sa che somma esiste
    return 0;
}

int somma(int a, int b) {
    return a + b;
}
```

**Motivo 2: Organizzazione del codice**
- main() in alto → più facile da leggere
- Funzioni di utilità in basso
- Separazione tra "cosa fa" (prototipo) e "come lo fa" (definizione)

**Motivo 3: Ricorsione mutua**
```c
// Senza prototipi: impossibile!
int pari(int n) {
    if (n == 0) return 1;
    return dispari(n-1);  // ERRORE: dispari non dichiarata
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n-1);
}

// Con prototipi: OK!
int pari(int n);     // Prototipi necessari
int dispari(int n);

int pari(int n) {
    if (n == 0) return 1;
    return dispari(n-1);  // OK!
}

int dispari(int n) {
    if (n == 0) return 0;
    return pari(n-1);     // OK!
}
```

**Motivo 4: Preparazione per file header (.h)**
- I prototipi vanno nei file .h
- Le definizioni vanno nei file .c
- Permette di creare librerie

---

### 3. Differenza tra variabile locale e static?

**Risposta attesa dagli studenti:**
- Variabile locale: si azzera ad ogni chiamata
- Variabile static: mantiene il valore tra le chiamate
- Static viene inizializzata una sola volta

**Dimostrazione pratica da fare insieme:**

```c
void contatoreNormale() {
    int conta = 0;        // Si ricrea ogni volta
    conta++;
    printf("Normale: %d\n", conta);
}

void contatoreStatic() {
    static int conta = 0; // Si inizializza UNA SOLA VOLTA
    conta++;
    printf("Static: %d\n", conta);
}

int main() {
    printf("=== VARIABILE NORMALE ===\n");
    contatoreNormale();  // Stampa: 1
    contatoreNormale();  // Stampa: 1 (ricomincia da 0!)
    contatoreNormale();  // Stampa: 1
    
    printf("\n=== VARIABILE STATIC ===\n");
    contatoreStatic();   // Stampa: 1
    contatoreStatic();   // Stampa: 2 (ricorda il valore!)
    contatoreStatic();   // Stampa: 3
    
    return 0;
}
```

**Tabella comparativa da mostrare:**

| Caratteristica | Variabile locale | Variabile static |
|----------------|------------------|------------------|
| **Inizializzazione** | Ad ogni chiamata | Una volta sola |
| **Durata** | Durante la funzione | Tutta l'esecuzione |
| **Valore iniziale** | Indeterminato* | 0 (default) |
| **Memoria** | Stack | Segmento dati |
| **Visibilità** | Solo nella funzione | Solo nella funzione |
| **Uso tipico** | Calcoli temporanei | Contatori, cache |

*Nota: variabili locali non inizializzate contengono "spazzatura"

**Casi d'uso pratici:**

1. **Contatore di chiamate**
```c
void logChiamata() {
    static int chiamate = 0;
    chiamate++;
    printf("Questa funzione è stata chiamata %d volte\n", chiamate);
}
```

2. **Generatore ID univoci**
```c
int generaID() {
    static int ultimoID = 0;
    ultimoID++;
    return ultimoID;
}

// Uso:
int id1 = generaID();  // 1
int id2 = generaID();  // 2
int id3 = generaID();  // 3
```

3. **Cache/Memoization**
```c
int fibonacci(int n) {
    static int cache[100];  // Mantiene i valori calcolati
    static int inizializzato = 0;
    
    if (!inizializzato) {
        for (int i = 0; i < 100; i++) cache[i] = -1;
        inizializzato = 1;
    }
    
    if (n <= 1) return n;
    if (cache[n] != -1) return cache[n];
    
    cache[n] = fibonacci(n-1) + fibonacci(n-2);
    return cache[n];
}
```

**Errore comune da evidenziare:**
```c
void sbagliata() {
    static int x = funzioneComplessa();  // ERRORE!
    // L'inizializzazione di static deve essere con valore costante!
}

void corretta() {
    static int x = 10;  // OK: valore costante
}
```

</details>

### Compiti per casa (opzionale):

- Completare tutti gli esercizi
- Provare a scrivere 3 funzioni ricorsive originali
- Refactoring di un vecchio programma usando le best practices

---

## NOTE PER IL DOCENTE

### ⚠️ Punti critici da monitorare:

1. **Ricorsione infinita**: molti studenti dimenticano il caso base
2. **Stack overflow**: far capire che la ricorsione ha limiti
3. **Confusione prototype/definizione**: ribadire la differenza
4. **Static**: concetto astratto, serve tempo

### 💡 Suggerimenti:

- Usa MOLTI disegni per la ricorsione (stack, alberi)
- Fai eseguire gli esempi passo-passo alla lavagna
- Collega i concetti a situazioni reali
- Incoraggia gli studenti a "pensare ricorsivamente"

### 📊 Valutazione comprensione:

- Chi scrive funzioni ricorsive corrette al primo tentativo: ottimo
- Chi le scrive con aiuto: buono
- Chi fatica con il caso base: serve rinforzo
- Chi non capisce la ricorsione: serve ripasso 1-1

### 🎯 Obiettivi raggiunti se gli studenti:

- ✅ Scrivono funzioni ricorsive con caso base
- ✅ Usano correttamente i prototipi
- ✅ Applicano le best practices
- ✅ Comprendono il concetto di static

---

**Buona lezione! 🚀**
