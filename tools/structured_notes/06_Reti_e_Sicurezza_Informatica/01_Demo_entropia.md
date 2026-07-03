# Demo entropia

## Panoramica
# Entropia e Compressione: Teoria e Pratica

## Argomenti trattati
Crittografia, Database, Data Analytics, Sicurezza, Git

---
## Appunti

# Entropia e Compressione: Teoria e Pratica
## 📚 Teoria dell'Informazione
### Cos'è l'Entropia?
L'**entropia di Shannon** è una misura fondamentale della teoria dell'informazione che quantifica la quantità di "informazione" o "incertezza" contenuta in un messaggio. È definita matematicamente come:
H(X) = -∑ P(x) × log₂(P(x))
- `H(X)` è l'entropia in bit per simbolo
- `P(x)` è la probabilità di occorrenza del simbolo `x`
- La sommatoria è estesa su tutti i possibili simboli
### Interpretazione Intuitiva
L'entropia misura quanto è "sorprendente" o "imprevedibile" un messaggio:
- **Entropia BASSA** (vicina a 0): Il messaggio è prevedibile, contiene poca informazione reale
- Esempio: "aaaaaaaaaa..." (sempre la stessa lettera)
- Facile da comprimere
- **Entropia ALTA** (vicina al massimo teorico): Il messaggio è imprevedibile, contiene molta informazione
- Esempio: Una sequenza completamente casuale
- Difficile da comprimere
### Il Limite di Shannon (Teorema della Codifica Sorgente)
Il **Primo Teorema di Shannon** stabilisce che:
> È impossibile comprimere un messaggio sotto la sua entropia senza perdere informazione
Questo significa che se un file ha entropia `H` bit per simbolo, non può essere compresso a meno di `H × N` bit totali (dove `N` è il numero di simboli).
### Relazione tra Entropia e Compressione
La compressione funziona sfruttando la **ridondanza** nei dati:
1. **Ridondanza = Informazione ripetuta o prevedibile**
2. **Algoritmi di compressione cercano pattern e li sostituiscono con rappresentazioni più brevi**
3. **Più ridondanza = maggiore compressibilità**
4. **Meno ridondanza = minore compressibilità**
## 🧪 Esperimento Pratico
### Obiettivo
Dimostrare empiricamente la relazione tra entropia e compressibilità attraverso un esperimento controllato.
### Setup dell'Esperimento
Creiamo due file di 1MB ciascuno:
1. **File A**: Contiene solo la lettera "a" ripetuta 1.048.576 volte
2. **File B**: Contiene caratteri ASCII casuali (dal carattere 32 al 126)
### Ipotesi Teoriche
**File A (solo "a"):**
- Entropia ≈ 0 bit per simbolo (massima prevedibilità)
- Dimensione minima teorica ≈ 0 bytes
- Compressibilità attesa: ~99.9%
**File B (caratteri casuali):**
- Entropia ≈ 6.6 bit per simbolo (circa log₂(95) per 95 caratteri ASCII)
- Dimensione minima teorica ≈ 860KB
- Compressibilità attesa: <20%
### Algoritmi di Compressione Testati
1. **GZIP**: Algoritmo LZ77 + Huffman coding
2. **BZIP2**: Trasformata di Burrows-Wheeler + compressione
3. **LZMA**: Algoritmo avanzato con dizionario
4. **ZLIB**: Simile a GZIP ma più veloce
### Metriche Analizzate
Per ogni combinazione file/algoritmo misuriamo:
- **Entropia originale** (H bit/simbolo)
- **Dimensione compressa** (bytes)
- **Rapporto di compressione** (originale:compresso)
- **Percentuale spazio risparmiato**
- **Tempo di compressione**
- **Efficienza vs limite teorico** (%)
## 🎯 Risultati Attesi
### File con Solo "a"
Entropia: ~0.000 bit/simbolo
Compressione GZIP: ~1,048,576 → ~1,000 bytes (rapporto 1048:1)
Compressione BZIP2: ~1,048,576 → ~200 bytes (rapporto 5242:1)
Efficienza: Molto vicina al limite teorico
### File con Caratteri Casuali
Entropia: ~6.6 bit/simbolo
Compressione GZIP: ~1,048,576 → ~1,040,000 bytes (rapporto 1.01:1)
Compressione BZIP2: ~1,048,576 → ~1,035,000 bytes (rapporto 1.01:1)
Efficienza: Limitata dall'alta entropia
## 💡 Lezioni Apprese
### 1. La Compressione Non È Magia
La compressione non può creare informazione dal nulla. Se un file contiene informazione realmente casuale, non può essere compresso significativamente.
### 2. Pattern = Compressibilità
I file con pattern ripetitivi, strutture regolari o ridondanza si comprimono bene. I file casuali o già compressi (come JPEG, MP3) si comprimono poco.
### 3. Entropia Come Predittore
L'entropia di un file è un eccellente predittore della sua compressibilità massima teorica.
### 4. Algoritmi Diversi, Risultati Simili
Su dati ad alta entropia, tutti gli algoritmi performano similmente perché sono limitati dalla teoria dell'informazione.
## 🌍 Applicazioni nel Mondo Reale
### File di Testo
- **Entropia**: Media (~4-5 bit/simbolo)
- **Compressibilità**: Buona (linguaggio naturale ha pattern)
- **Esempi**: Documenti Word, codice sorgente

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 999_Demo_entropia.md*
