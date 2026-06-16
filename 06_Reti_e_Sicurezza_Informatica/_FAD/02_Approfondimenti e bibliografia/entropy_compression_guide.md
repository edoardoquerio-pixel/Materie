# Entropia e Compressione: Teoria e Pratica

## 📚 Teoria dell'Informazione

### Cos'è l'Entropia?

L'**entropia di Shannon** è una misura fondamentale della teoria dell'informazione che quantifica la quantità di "informazione" o "incertezza" contenuta in un messaggio. È definita matematicamente come:

```
H(X) = -∑ P(x) × log₂(P(x))
```

Dove:
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

---

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

---

## 🎯 Risultati Attesi

### File con Solo "a"

```
Entropia: ~0.000 bit/simbolo
Compressione GZIP: ~1,048,576 → ~1,000 bytes (rapporto 1048:1)
Compressione BZIP2: ~1,048,576 → ~200 bytes (rapporto 5242:1)
Efficienza: Molto vicina al limite teorico
```

### File con Caratteri Casuali

```
Entropia: ~6.6 bit/simbolo
Compressione GZIP: ~1,048,576 → ~1,040,000 bytes (rapporto 1.01:1)
Compressione BZIP2: ~1,048,576 → ~1,035,000 bytes (rapporto 1.01:1)
Efficienza: Limitata dall'alta entropia
```

---

## 💡 Lezioni Apprese

### 1. La Compressione Non È Magia

La compressione non può creare informazione dal nulla. Se un file contiene informazione realmente casuale, non può essere compresso significativamente.

### 2. Pattern = Compressibilità

I file con pattern ripetitivi, strutture regolari o ridondanza si comprimono bene. I file casuali o già compressi (come JPEG, MP3) si comprimono poco.

### 3. Entropia Come Predittore

L'entropia di un file è un eccellente predittore della sua compressibilità massima teorica.

### 4. Algoritmi Diversi, Risultati Simili

Su dati ad alta entropia, tutti gli algoritmi performano similmente perché sono limitati dalla teoria dell'informazione.

---

## 🌍 Applicazioni nel Mondo Reale

### File di Testo
- **Entropia**: Media (~4-5 bit/simbolo)
- **Compressibilità**: Buona (linguaggio naturale ha pattern)
- **Esempi**: Documenti Word, codice sorgente

### Immagini RAW
- **Entropia**: Variabile (dipende dal contenuto)
- **Compressibilità**: Eccellente (molti pixel simili)
- **Esempi**: BMP, TIFF non compressi

### Immagini JPEG
- **Entropia**: Alta (già ottimizzate)
- **Compressibilità**: Scarsa (già compresse)
- **Motivo**: L'algoritmo JPEG ha già rimosso la ridondanza

### File Crittografati
- **Entropia**: Massima (~8 bit/simbolo)
- **Compressibilità**: Quasi nulla
- **Motivo**: Crittografia produce output pseudo-casuale

### Database
- **Entropia**: Variabile (dipende dai dati)
- **Compressibilità**: Spesso buona (dati strutturati)
- **Esempi**: Backup SQL, file CSV

---

## 🔐 Sicurezza delle Password e Entropia

### Entropia nelle Password: Una Questione di Vita o di Morte Digitale

L'entropia non è solo un concetto teorico per la compressione dati, ma è **fondamentale per la sicurezza informatica**, specialmente per le password. Una password con bassa entropia è come una porta di casa con una serratura di cartone.

### Calcolo dell'Entropia delle Password

L'entropia di una password dipende da:

1. **Dimensione dell'alfabeto** (quanti caratteri diversi possibili)
2. **Lunghezza della password**
3. **Casualità nella scelta**

#### Formula Base
```
Entropia = log₂(Alfabeto^Lunghezza)
```

#### Esempi di Alfabeti
- **Solo minuscole**: 26 caratteri (a-z)
- **Minuscole + maiuscole**: 52 caratteri (a-z, A-Z)
- **Alfanumeriche**: 62 caratteri (a-z, A-Z, 0-9)
- **Alfanumeriche + simboli**: ~95 caratteri (ASCII stampabili)

### Esempi Pratici di Entropia

| Tipo Password | Esempio | Alfabeto | Lunghezza | Entropia (bit) |
|---------------|---------|----------|-----------|----------------|
| PIN | `1234` | 10 | 4 | 13.3 |
| Password debole | `password` | 26 | 8 | 37.6 |
| Password comune | `Password123` | 62 | 11 | 65.4 |
| Password forte | `Tr0ub4dor&3` | 95 | 11 | 72.0 |
| Password molto forte | `zK9#mL$2vN8@qW` | 95 | 14 | 91.7 |
| Passphrase | `horse battery staple correct` | 27 | 27 | 127.1 |

### Tempo di Brute Force: Scenario Realistico

**Scenario**: Attaccante con laptop gaming di fascia alta (2024)
- **GPU**: RTX 4090 o equivalente
- **Capacità**: ~100 miliardi di hash/secondo (per algoritmi veloci come MD5)
- **Capacità realistica**: ~1 miliardo di hash/secondo (per algoritmi sicuri come bcrypt)

#### Tabella Tempi di Attacco

| Entropia (bit) | Combinazioni possibili | Tempo medio brute force |
|----------------|------------------------|-------------------------|
| 13 (PIN 4 cifre) | 10,000 | **0.005 millisecondi** |
| 20 | 1,048,576 | **0.5 millisecondi** |
| 30 | 1,073,741,824 | **0.5 secondi** |
| 40 | 1,099,511,627,776 | **9 minuti** |
| 50 | 1,125,899,906,842,624 | **6 giorni** |
| 60 | 1,152,921,504,606,846,976 | **18 anni** |
| 70 | 1,180,591,620,717,411,303,424 | **18,700 anni** |
| 80 | 1,208,925,819,614,629,174,706,176 | **19 milioni di anni** |
| 90 | 1,237,940,039,285,380,274,899,124,224 | **19 miliardi di anni** |
| 100 | 1,267,650,600,228,229,401,496,703,205,376 | **20 trilioni di anni** |

### Password Comuni vs Password Casuali

#### Password Comune: "Password123!"
```
Entropia apparente: ~70 bit (se fosse casuale)
Entropia reale: ~10-20 bit (è in dizionari comuni)
Tempo di attacco: Secondi (con dizionari)
```

#### Password Casuale: "zK9#mL$2vN8@"
```
Entropia reale: ~78 bit
Tempo di attacco: ~300 milioni di anni
```

### Metodi di Attacco Reali

Gli attaccanti non usano sempre brute force puro:

#### 1. **Attacco a Dizionario**
- Testa milioni di password comuni
- Efficace contro password "umane"
- Tempo: minuti/ore

#### 2. **Attacco Ibrido**
- Dizionario + variazioni (Password123, password!)
- Molto efficace nella pratica
- Tempo: ore/giorni

#### 3. **Attacco per Regole**
- Sfrutta pattern umani comuni
- "password" → "Password123!"
- Tempo: giorni/settimane

#### 4. **Brute Force Puro**
- Testa tutte le combinazioni possibili
- Usato solo come ultima risorsa
- Tempo: secondo l'entropia

### Raccomandazioni Pratiche

#### Entropia Minima Raccomandata

| Utilizzo | Entropia Minima | Esempio |
|----------|-----------------|---------|
| **Account non critici** | 40+ bit | Password di 8 caratteri misti |
| **Account importanti** | 60+ bit | Password di 10 caratteri misti |
| **Account critici** | 80+ bit | Password di 12+ caratteri misti |
| **Chiavi crittografiche** | 128+ bit | Chiavi generate casualmente |

#### Strategie per Alta Entropia

1. **Lunghezza > Complessità**
   ```
   "horse battery staple correct" (entropia ~127 bit)
   è meglio di
   "Tr0ub4d0r&3" (entropia ~72 bit)
   ```

2. **Casualità Vera**
   - Usare generatori di password casuali
   - Evitare pattern umani riconoscibili

3. **Passphrases**
   - 4-6 parole casuali dal dizionario
   - Facili da ricordare, difficili da craccare

### Falsi Miti sulla Sicurezza delle Password

#### ❌ **Mito**: "Sostituire 'o' con '0' rende sicura la password"
**Realtà**: Gli attaccanti conoscono queste sostituzioni comuni

#### ❌ **Mito**: "8 caratteri bastano se sono complessi"
**Realtà**: Lunghezza è più importante della complessità

#### ❌ **Mito**: "Se non è nel dizionario è sicura"
**Realtà**: Gli attaccanti usano regole e pattern

#### ✅ **Verità**: Solo l'entropia reale conta

### Strumenti per Misurare l'Entropia delle Password

#### Online (per test)
- **zxcvbn**: Libreria che stima l'entropia reale
- **How Secure Is My Password**: Calcola tempi di brute force

#### Programmatici
```python
import math
import string

def calculate_password_entropy(password):
    # Determina l'alfabeto usato
    alphabet_size = 0
    if any(c.islower() for c in password):
        alphabet_size += 26
    if any(c.isupper() for c in password):
        alphabet_size += 26
    if any(c.isdigit() for c in password):
        alphabet_size += 10
    if any(c in string.punctuation for c in password):
        alphabet_size += len(string.punctuation)
    
    # Calcola entropia
    entropy = len(password) * math.log2(alphabet_size)
    return entropy, alphabet_size
```

### Impatto delle Violazioni di Dati

Quando un database di password viene compromesso:

#### Hash Deboli (MD5, SHA1)
- **Velocità crack**: 100+ miliardi hash/secondo
- **Password con <60 bit entropia**: Compromesse in ore

#### Hash Forti (bcrypt, scrypt, Argon2)
- **Velocità crack**: 1-1000 hash/secondo
- **Password con 50+ bit entropia**: Sicure per decenni

### Generazione di Password Sicure

#### Metodo 1: Generatore Casuale
```python
import secrets
import string

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Entropia: ~95^16 = ~105 bit
```

#### Metodo 2: Diceware (Passphrases)
```python
import secrets

# Lista di 7776 parole (log2(7776) ≈ 12.9 bit per parola)
def generate_passphrase(num_words=6):
    # 6 parole = 6 × 12.9 ≈ 77 bit di entropia
    words = ["word1", "word2", ...]  # Lista Diceware
    return " ".join(secrets.choice(words) for _ in range(num_words))
```

### Conclusioni sulla Sicurezza

1. **L'entropia è l'unica vera misura della sicurezza delle password**
2. **Pattern umani riducono drasticamente l'entropia reale**
3. **La lunghezza è più importante della complessità**
4. **60+ bit di entropia dovrebbero essere il minimo per account importanti**
5. **L'hashing forte può compensare password più deboli**

**Regola d'oro**: Se puoi ricordare facilmente la tua password, probabilmente non è abbastanza sicura (a meno che non sia una passphrase lunga).

---

## 🔬 Esperimenti Aggiuntivi

### Variazioni Possibili

1. **Testare file misti**: 50% "a" + 50% casuali
2. **Analizzare file reali**: PDF, immagini, video
3. **Confrontare lingue diverse**: Entropia dell'italiano vs inglese vs cinese
4. **Testare sequenze matematiche**: Pi greco, numeri primi, sequenze di Fibonacci

### Domande di Ricerca

- Come varia l'entropia in base alla lunghezza del file?
- Quale algoritmo è più efficiente su diversi tipi di dati?
- Come influisce la codifica dei caratteri (UTF-8 vs ASCII)?

---

## 📖 Approfondimenti Teorici

### Entropia Condizionale

```
H(X|Y) = H(X,Y) - H(Y)
```

Misura l'incertezza di X dato Y. Utile per analizzare la compressione basata su contesto.

### Informazione Mutua

```
I(X;Y) = H(X) - H(X|Y)
```

Quantifica quanto X e Y si "informano" a vicenda. Rilevante per algoritmi di compressione avanzati.

### Entropia di Rényi

Generalizzazione dell'entropia di Shannon per diversi ordini α:

```
H_α(X) = (1/(1-α)) × log₂(∑ pᵢᵅ)
```

Utile per analisi più sofisticate dei dati.

---

## 🛠️ Strumenti e Risorse

### Software per Analisi Entropia
- **ent**: Utilità Unix per calcolare entropia
- **binwalk**: Analisi entropia di file binari
- **Python**: librerie `scipy.stats`, `numpy`

### Algoritmi di Compressione Moderni
- **Zstandard (zstd)**: Veloce e efficiente
- **Brotli**: Ottimizzato per il web
- **LZFSE**: Algoritmo Apple
- **LZ4**: Ultraveloce per applicazioni real-time

### Risorse Teoriche
- "Elements of Information Theory" - Cover & Thomas
- "Introduction to Data Compression" - Sayood
- Papers originali di Claude Shannon (1948)

---

## 📝 Conclusioni

Questo esperimento dimostra concretamente che:

1. **L'entropia è un limite fondamentale** alla compressione
2. **La teoria di Shannon si applica nella pratica**
3. **Comprendere l'entropia aiuta a scegliere algoritmi appropriati**
4. **Non tutti i dati sono uguali** dal punto di vista informazionale

La teoria dell'informazione non è solo matematica astratta, ma ha applicazioni pratiche concrete che utilizziamo quotidianamente in tecnologie come ZIP, JPEG, MP3, e nelle comunicazioni digitali.

---

*Per eseguire l'esperimento pratico, utilizzare lo script Python allegato che implementa tutti i calcoli e le analisi descritte in questa guida.*