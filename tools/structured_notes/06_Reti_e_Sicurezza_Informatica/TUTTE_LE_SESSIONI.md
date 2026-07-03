# 06 - Reti e Sicurezza Informatica — Tutte le Sessioni


---

## Sessione 1: Demo entropia


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

## Sessione 2: Lezione 01


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Introduzione alla cybersecurity
Intervento realizzato da
v 3.3.5 ~ feb 2025
Public Service Announcement
Who am I? Marco Farina, insegno informatica e reti al Maxwell di Nichelino.
Cybersec? Non lavoro nel campo, ma sono appassionato di cybersec e AI.
Topics? Cybersecurity, crittografia, sicurezza web/cloud/database, laboratorio.
Handout? Slide a fine lezione, appunti e attenzione.
Exam? Sulla teoria, una parte a risposta chiusa, una parte aperta.
Questions? Meglio una domanda in più adesso che un esame a settembre.
1Introduzione alla
Cos’è la sicurezza?
Il rischio è la probabilità che accada un certo
evento capace di causare un danno.
È implicata l’esistenza di una sorgente di
pericolo, detta minaccia, e delle possibilità che
essa si trasformi in un danno.
Valutazione del rischio
Il rischio è uguale alla probabilità che si
verifichi l’evento moltiplicata per la gravità del
Cos’è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello personale
Livello aziendale
Livello nazionale
Cos’è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello personale
Cosa vogliamo proteggere?
Cos’è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Idee e brevetti
Livello aziendale
Cosa vogliamo proteggere?
Cos’è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello nazionale
Cosa vogliamo proteggere?
The future of cyberwarfare
Cracking Stuxnet
Uso di arsenali digitali per attaccare una nazione,
causando danni comparabili alla guerra tradizionale.
Spionaggio internazionale
Sabotaggio delle infrastrutture
Shock economico
Eventi climatici
The Global risk landscape, 2019
World Economic Forum
La triade C.I.A.
Indipendentemente dal livello, la triade C.I.A. è il concetto fondamentale.
Confidentiality
Confidenzialità
Confidenzialità
È la proprietà che indica che le informazioni non sono
rese disponibili o divulgate a individui, entità o processi
non autorizzati.
Il concetto non è strettamente sinonimo di privacy, ma
un componente della privacy implementato per
proteggere i dati da visualizzazioni non autorizzate.
Assicura che la completezza e l’accuratezza dei dati
venga mantenuta durante il loro intero ciclo di vita.
Il concetto non è strettamente sinonimo di integrità
referenziale dei database, anche se può essere vista
come un caso speciale di consistenza.
La crittografia è lo strumento più utilizzato perché
assieme all’integrità fornisce anche la confidenzialità.
Affinché i sistemi informativi assolvano la propria
funzione, le informazioni devono essere disponibili
quando richieste.
I sistemi di memorizzazione e calcolo, i controlli di
sicurezza e i canali di comunicazione devono essere
sempre funzionanti.
Uno dei più grandi sforzi è compiuto nel prevenire gli
attacchi di tipo Denial of Service.
Meet Alice, Bob & Eve
il destinatario
Tipologie di attacchi

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 3: Lezione 02


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Password management
Intervento realizzato da
v 3.6.1 ~ feb 2026
dell’intrusione
Prevenzione dalle intrusioni
Controllo degli accessi
Tecniche di intrusione
Default password
Router, modem, IoT, …
Social engineering
Password profiling, namedropping, pretexting, tailgating,
something for something,…
Attacchi a dizionario
/usr/share/wordlists
Attacchi a forza bruta
JohnTheRipper, AirCrack, …
2Attacchi a forza
Photo by Pixabay from Pexels
tanta ripetizione = poca entropia
alcune ripetizioni = entropia media
stringa casuale = entropia massima
Cos’è una password casuale?
Una password generata casualmente è una stringa di caratteri di
estratti per selezione casuale da un insieme di simboli
Quante sono le password di lunghezza ?L
Lo spazio delle chiavi è Il numero di password possibili lunghe
Come si misura quanto è robusta una password?
ℍ = log2 | Σ |L = L log2 | Σ | = L
Le sbarrette verticali in questo
contesto non indicano il valore
assoluto, ma la cardinalità
dell’insieme, ovvero quanti
elementi contiene l’insieme.
Entropia per simbolo (
Numeri (0-9) [es: PIN]
Esadecimale (0-9, A-F) [es: WEP]
Alfabeto latino (a-z)
Alfanumerico (a-z, 0-9)
Alfanumerico case sentive (a-z, A-Z, 0-9) 62
ASCII stampabile tranne spazio
Codice binario (1 byte)
Esempio realistico
Supponiamo di generare casualmente (ovvero, ogni simbolo è equiprobabile)
una password di lunghezza
caratteri ASCII stampabili.
L’entropia della password è calcolata con l’equazione
ℍ = log2 K = log2 9412 = 12 log2 94 = 12
Sono “buoni” 78 bit di entropia per
Robustezza delle password *
molto debole, potrebbe bastare per tenere lontano il
debole, tiene alla larga la maggior parte delle persone, ma
non Gianpancrazio, l’hacker del piano di sopra. Potete
usarla, al massimo, come password di login del pc.
ragionevole, si può usare per la rete e in azienda.
forte, potete usarla per proteggere i milioni di euro del
vostro conto in banca.
overkill, manco fossi Tony Stark.
* Allo stato attuale della potenza computazionale
Tempi di attacco
Quando si effettua un attacco brute force, la lunghezza della
chiave non è nota.
Si devono testare tutte le combinazioni da una lunghezza minima
K⋆ = | Σ |l + | Σ |l+1 + | Σ |l+2 + … + | Σ |L
Tutte le password
Tutte le password
Tutte le password
Il tempo di crack è dato da
è la capacità computazionale
(numero di chiavi testate al secondo);
è il numero di calcolatori usati in
Tempi di attacco
Supponiamo (realisticamente)
N = 1 ν = 500 000
immediato immediato immediato
immediato 2 minuti
“Ma sì, dai, ormai lo sanno tutti che le password devono essere casuali…”
Password Security Awards

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 4: Lezione 03


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Introduzione alla crittografia
Intervento realizzato da
v 2.7.2 ~ feb 2026
Mercoledì 15 Ottobre 1586. È mattina, Mary
Stuart entra nell’affollata aula di giustizia del
castello di Fotheringhay. Anni di prigionia e
l’insorgere di una malattia reumatica hanno
lasciato il segno, ma la regina è dignitosa,
composta e incontestabilmente regale.
Mary, Regina degli scozzesi, è accusata di
tradimento: avrebbe partecipato a un complotto
mirante a sopprimere Elisabetta e a porla sul trono
d’Inghilterra al posto dell’uccisa.
Il segretario di stato Sir Francis Walsingham, ha arrestato
gli altri cospiratori, e dopo averli costretti a confessare, li
ha consegnati al boia. Ora intende dimostrare che Mary
Stuart merita la morte, perché era al corrente della
congiura e vi ha partecipato attivamente. Walsingham sa
bene che Elisabetta non ﬁrmerà la condanna se non sarà
certa della colpevolezza della Stuart.
In primo luogo Mary è regina di Scozia, e molti dubitano
che mandare a morte il capo di un paese straniero rientri
nei poteri di un tribunale inglese. In secondo luogo,
l’esecuzione può creare un pericoloso precedente: se uno
Stato si arroga il diritto di sopprimere il monarca, i capi
di un’eventuale rivolta non avranno scrupoli a fare lo
stesso, ed Elisabetta ha ancora molti nemici. In terzo
luogo, l’imputata è sua cugina, un legame abbastanza
stretto per aumentare la sua titubanza.
stesso, ed Elisabetta ha ancora molti nemici. In terzo
luogo, l’imputata è sua cugina, un legame abbastanza
stretto per aumentare la sua titubanza.
È il mattino del primo giorno del processo, e Mary
siede sola al banco degli imputati, luttuosamente
vestita di nero.
Nei processi per alto tradimento, l’accusato non
può farsi assistere, né può convocare testimoni a
propria discolpa, eppure la situazione non le
sembra disperata, perché ha avuto cura di cifrare
tutta la corrispondenza coi congiurati. Su fogli di
carta, al posto di parole e frasi ha vergato simboli
apparentemente privi di signiﬁcato.
tutta la corrispondenza coi congiurati. Su fogli di
carta, al posto di parole e frasi ha vergato simboli
apparentemente privi di signiﬁcato.
Purtroppo per Mary, Walsingham non è solo il
segretario di Stato, ma anche, come diremo oggi, il
capo del controspionaggio. Appena visti i
messaggi, ha capito chi poteva riuscire a volgerli in
chiaro: Thomas Phelippes, il miglior decrittatore
Se riuscirà a violare la fatale corrispondenza tra
Mary e i cospiratori, la morte della regina sarà
Codici & Segreti, Simon Singh
1La nascita della
Demarato di Sparta
Demarato di Sparta
Istieo di Mileto
Dalla comunicazione alla crittografia
Dalla comunicazione alla crittografia
Il Cifrario di Cesare
S T U V Z A B C D …
meet me after the toga party
OGGV OG CHVGT VJG VQIC RCTVA
Quanto è grande lo spazio delle chiavi?
K⋆ = | Σ | = 26
spazio delle chiavi troppo piccolo.
attacco brute force.
aumentare lo spazio delle chiavi.
Cifratura monoalfabetica
A B C D E F G H I J K L M N O P
A B C D E F G H I J K L M N O P
Cifratura monoalfabetica
A B C D E F G H I J K L M N O P
La permutazione di
costituisce la chiave crittografica.
Quanto è grande lo spazio delle chiavi?
K⋆ = 26! ≈ 4 ⋅ 1026

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 5: Lezione 04


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Crittografia DES e AES
Intervento realizzato da
v 3.1.4 ~ feb 2026
Novecento: dalle lettere ai numeri
Communication Theory of Secrecy
Crittografia a chiave pubblica
1Data Encryption
Right half (32)
#
#
Output (64 bit)
#
Quanto è grande lo spazio delle chiavi?
= 256 ≈ 7,2 ⋅ 1016
Chi: distributed.net & EFF
Performance: 92 miliardi di chiavi al secondo
Tempo: 22 ore e 15 minuti
Costo: 200.000 $
Quanto è grande lo spazio delle chiavi?
= 256 ≈ 7,2 ⋅ 1016
…cifriamo TRE volte. (sigh!)
attacco brute force.
spazio delle chiavi troppo piccolo.
Encryption Standard
Costruzione di AES
Il NIST emette il
Richieste tre caratteristiche:
Sicurezza (chiave da 128+ bit)
Efficienza computazionale
Semplicità di implementazione
L’algoritmo scelto è stato sviluppato da due crittografi belgi, Joan Daemen e Vincent
Rijmen, che lo hanno presentato con il nome di Rijndael, derivato dai loro nomi.
Rijndael, in fiammingo, si pronuncia [ˈrɛindaːl] (“rèin-daal”).
Questo è un blocco di 128
bit preso dal messaggio in
chiaro che deve essere
Notazione esadecimale (esempio):
32 = 0011 0010 (1 byte)
Processo di cifratura
Il procedimento di cifratura del blocco plaintext avviene usando 4
differenti trasformazioni nel round iniziale, nei 9 round principali e nel
In particolare vengono usate quattro fasi, una di permutazione e tre di
๏ Substitute bytes: usa una S-Box per svolgere una sostituzione del
blocco byte per byte.
๏ Shift rows: una semplice permutazione.
๏ Mix columns: una sostituzione che utilizza l’aritmetica sui campi di
๏ Add round key: una semplice operazione di XOR bit-a-bit del blocco
corrente con una porzione della chiave espansa.
Processo di cifratura
Le trasformazioni di AES
Vediamo ora le quattro trasformazioni di AES. Per ogni
trasformazione vedremo come funziona intuitivamente
l’algoritmo di crittografia ed infine come avviene la
trasformazione della chiave.
La trasformazione Substitute byte è una semplice ricerca su una
tabella. AES definisce una matrice di dimensione 16x16 chiamata
S-Box che contiene una permutazione di tutti i 256 valori a 8 bit.
Shift su 1 byte
Shift su 2 byte
Shift su 3 byte
Questa trasformazione opera su una singola colonna.
Ciascun byte di una colonna viene mappato in un
nuovo valore che è una funzione dei quattro byte
presenti nella colonna. La trasformazione può essere
definita dalla moltiplicazione in figura.
Nello standard la trasformazione viene definita considerando
ciascuna colonna come un polinomio di quattro termini con
coefficienti nel campo finito GF(28). Ciascuna colonna viene
moltiplicata modulo (x4+1) per il polinomio fisso a(x) dato da:
a(x) = 3x3 + x2 + x + 2
Nello standard la trasformazione viene definita considerando
ciascuna colonna come un polinomio di quattro termini con
coefficienti nel campo finito GF(28). Ciascuna colonna viene
moltiplicata modulo (x4+1) per il polinomio fisso a(x) dato da:
a(x) = 3x3 + x2 + x + 2
Prodotta nel primo
passo di generazione

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 6: Lezione 05


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Diffie-Hellman-Merkle key exchange
Intervento realizzato da
v 3.4.4 ~ mar 2026
Proprietà delle chiavi crittografiche
La potenza di un sistema crittografico dipende
dalla tecnica usata per condividere la chiave.
Come si può condividere la chiave?
Abingdon Road 42
I primi due metodi non sono utilizzabili in epoca informatica; il
terzo presuppone che una chiave sia già stata scambiata.
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Il metodo dei lucchetti
Perché questo metodo
non può funzionare?
Composizione di cifrature
abcdefghijklmnopqrstuvwxyz
HFSUGTAKVDEOYJBPNXWCQRIMZL
Chiave di Alice
abcdefghijklmnopqrstuvwxyz
CPMGATNOJEFWIQBURYHXSDZKLV
Cifrato da Alice
Decifrato da Bob
Decifrato da Alice
ci vediamo all una
SV RGUVHYB HOO QJH
HD YNSDOLP OBB REO
AJ MQCJLZP LOO VKL
ei cnaiywb yhh zxy
I puzzle di Merkle
I puzzle di Merkle
Ogni puzzle, se risolto,
contiene un ID e una
chiave casuale.
I puzzle di Merkle
casualmente un puzzle
I puzzle di Merkle
casualmente un puzzle
I puzzle di Merkle
Alice invia l’ID a Bob e
tiene copia della chiave
I puzzle di Merkle
Bob sa quale puzzle risolvere
per ottenere la chiave
Alice invia l’ID a Bob e
tiene copia della chiave
I puzzle di Merkle
L’attaccante può intercettare l’ID, ma deve risolvere, in media,
(ovvero la metà di quelli generati) per scoprire la chiave condivisa.
Il metodo dei colori
Chiave segreta condivisa
Chiave segreta condivisa
Insiemi numerici
Insiemi numerici
Teorema della divisione
sono interi, esistono e sono univocamente
determinati gli interi
sono detti rispettivamente il quoziente e il resto della divisione.
più un certo resto
si dice primo se:
Un numero intero
In altre parole, un intero è un primo se è diverso da
ha divisori propri.
a ∈ {−1, 1, p, − p}
1 2p 3p 4 5p 6 7p 8
9 10 11p 12 13p 14 15 16
Teorema fondamentale dell’aritmetica

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 7: Lezione 06


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Crittografia a chiave pubblica e RSA
Intervento realizzato da
v 2.2.3 ~ mar 2026
I favolosi anni ‘70
New Directions in Cryptography
Martin Hellman on cryptography
Diffie explains public-key encryption
Rivest on the origins of RSA
“We propose that it is possible to develop systems in which two parties
communicating solely over a public channel and using only publicly known
techniques can create a secure connection. We examine two approaches to this
problem, called public key cryptosystems and public key distribution systems,
respectively. The first are more powerful, lending themselves to the solution of the
authentication problems, while the second are much closer to realization. ”
New Directions in Cryptography, Whitfield Diffie e Martin Hellman, novembre 1976
Cifrari simmetrici
Permutazioni e sostituzioni
Rompere la simmetria
Chiave pubblica
Asimmetria delle chiavi
Basato su funzioni matematiche
Creare un canale di comunicazione
Creare un canale di comunicazione
Dopo essersi scambiati le chiavi
pubbliche Alice e Bob hanno
instaurato un canale di
comunicazione sicuro.
Inviare un messaggio crittografato
I let him, lol.
Inviare un messaggio crittografato
I let him, lol.
Inviare un messaggio crittografato
Bob usa la chiave pubblica di Alice
per crittografare il messaggio.
Inviare un messaggio crittografato
Inviare un messaggio crittografato
Inviare un messaggio crittografato
I let him, lol.
Alice usa la sua chiave privata per
decrittare il messaggio inviato da Bob.
Inviare un messaggio …?
I let him, lol.
Inviare un messaggio …?
I let him, lol.
Inviare un messaggio …?
Bob usa la sua chiave privata per
crittografare il messaggio.
Inviare un messaggio …?
Inviare un messaggio …?
Inviare un messaggio …?
I let him, lol.
Alice usa la chiave pubblica di Bob per
decrittare il messaggio ricevuto.
Inviare un messaggio autenticato!
I let him, lol.
Alice è sicura che il messaggio
provenga davvero da Bob. Il
messaggio è stato firmato.
Creare canali cifrati multipli
Creare canali cifrati multipli
“God rewards fools”
2RSA Encryption
Encryption function
Principio di identità
Funzione di crittografia
Funzione di decrittografia
Eseguite la cifratura e decifratura per verificare il principio di
identità. Per i calcoli usate wolframalpha.com.
4217 (mod 3233) = 2557
25572753 (mod 3233) = 42
3La matematica di
A caccia di funzioni unidirezionali
Quanto tempo ci vuole
per calcolare … !
p1 ⋅ p2 = 6 700 283 ???
Quanto tempo serve per scomporre un numero in fattori primi!
1889⋅3547=Scomposizione in fattori primi

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 8: Lezione 07


Prof. Marco Farina
Unità formativa
Sicurezza Informatica
Certificati digitali e hashing
Intervento realizzato da
v 3.2.4 ~ apr 2026
Risolvere il Man-in-the-middle
Come possiamo verificare che nessuno si sia
messo in mezzo alla comunicazione!
Verifica manuale
(tra due lezioni…)
Certificazione delle informazioni pubbliche
L’informazione pubblica può essere
falsificata, quindi:
viene distribuita all’interno di un certificato;
il certificato è firmato digitalmente e non
può essere contraffatto.
1La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
La firma digitale
Le funzioni di hashing
Funzione di hashing
Le funzioni di hashing
L’hash è una funzione non invertibile che mappa una stringa di
lunghezza arbitraria in una stringa di lunghezza predefinita.
1. A partire dall’hash non è possibile risalire alla stringa originale.
Le funzioni di hashing
L’hash è una funzione non invertibile che mappa una stringa di
lunghezza arbitraria in una stringa di lunghezza predefinita.
1. A partire dall’hash non è possibile risalire alla stringa originale.
2. L’input può essere di qualunque dimensione.
Le funzioni di hashing
L’hash è una funzione non invertibile che mappa una stringa di
lunghezza arbitraria in una stringa di lunghezza predefinita.
1. A partire dall’hash non è possibile risalire alla stringa originale.
2. L’input può essere di qualunque dimensione.
3. L’output ha una dimensione fissa.
Qualquadra non cosa.
Tutti i messaggi
di tutti gli hash
Qualquadra non cosa.
Tutti i messaggi
di tutti gli hash
Resistenza alle collisioni
Resistenza forte
È computazionalmente impossibile
trovare una qualsiasi coppia
Resistenza debole
Data una stringa
computazionalmente impossibile
trovare la stringa
messaggio ed il
…un altro messaggio
con lo stesso hash è
Una semplice funzione di hashing
Creiamo una funzione
che prende in input
bit e restituisce un digest lungo
Input: 101110100101011
Questa funzione prende il nome di controllo di ridondanza longitudinale.
Back in the days: MD5
Autore: Ron Rivest
Input: di qualunque lunghezza, ovviamente.
Output: 128 bit
OpenSSL: openssl dgst -md5 filename
php: md5($string)
md5_file($filename)
PLEASE DON’T DO THAT
MD5 è deprecato per qualunque funzione di sicurezza.
$notSoSecureDigest = md5("monkey");
$suchStringMuchSecurity = md5(md5("monkey"));

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 9: A Method for Obtaining Digital Signatures and Public-Key Cryptosystems


A Method for Obtaining Digital
Signatures and Public-Key Cryptosystems
R.L. Rivest, A. Shamir, and L. Adleman∗
An encryption method is presented with the novel property that publicly revealing an encryption key does not thereby reveal the corresponding decryption
key. This has two important consequences:
1. Couriers or other secure means are not needed to transmit keys, since a
message can be enciphered using an encryption key publicly revealed by
the intended recipient. Only he can decipher the message, since only he
knows the corresponding decryption key.
2. A message can be “signed” using a privately held decryption key. Anyone
can verify this signature using the corresponding publicly revealed encryption key. Signatures cannot be forged, and a signer cannot later deny
the validity of his signature. This has obvious applications in “electronic
mail” and “electronic funds transfer” systems.
A message is encrypted by representing it as a number M, raising M to a
publicly speciﬁed power e, and then taking the remainder when the result is
divided by the publicly speciﬁed product, n, of two large secret prime numbers
p and q. Decryption is similar; only a diﬀerent, secret, power d is used, where
e · d ≡ 1 (mod (p − 1) · (q − 1)). The security of the system rests in part on
the diﬃculty of factoring the published divisor, n.
Key Words and Phrases: digital signatures, public-key cryptosystems, privacy, authentication, security, factorization, prime number, electronic mail,
message-passing, electronic funds transfer, cryptography.
CR Categories: 2.12, 3.15, 3.50, 3.81, 5.25
∗General permission to make fair use in teaching or research of all or part of this material is
granted to individual readers and to nonproﬁt libraries acting for them provided that ACM’s copyright notice is given and that reference is made to the publication, to its date of issue, and to the fact
that reprinting privileges were granted by permission of the Association for Computing Machinery.
To otherwise reprint a ﬁgure, table, other substantial excerpt, or the entire work requires speciﬁc
permission as does republication, or systematic or multiple reproduction.
This research was supported by National Science Foundation grant MCS76-14294, and the Oﬃce of
Naval Research grant number N00014-67-A-0204-0063.
Author’s Address: Laboratory for Computer Science, Massachusetts Institute of Technology, Cambridge, MA 02139 E-mail addresses: rivest@theory.lcs.mit.edu
The era of “electronic mail” [10] may soon be upon us; we must ensure that two
important properties of the current “paper mail” system are preserved: (a) messages
are private, and (b) messages can be signed . We demonstrate in this paper how to
build these capabilities into an electronic mail system.
At the heart of our proposal is a new encryption method. This method provides
an implementation of a “public-key cryptosystem,” an elegant concept invented by
Diﬃe and Hellman [1]. Their article motivated our research, since they presented
the concept but not any practical implementation of such a system. Readers familiar
with [1] may wish to skip directly to Section V for a description of our method.
II Public-Key Cryptosystems
In a “public key cryptosystem” each user places in a public ﬁle an encryption procedure E. That is, the public ﬁle is a directory giving the encryption procedure of each
user. The user keeps secret the details of his corresponding decryption procedure D.
These procedures have the following four properties:
(a) Deciphering the enciphered form of a message M yields M . Formally,
(b) Both E and D are easy to compute.
(c) By publicly revealing E the user does not reveal an easy way to compute D.
This means that in practice only he can decrypt messages encrypted with E, or
compute D eﬃciently.
(d) If a message M is ﬁrst deciphered and then enciphered, M is the result. For-
An encryption (or decryption) procedure typically consists of a general method
and an encryption key. The general method, under control of the key, enciphers a
message M to obtain the enciphered form of the message, called the ciphertext C.
Everyone can use the same general method; the security of a given procedure will rest
on the security of the key. Revealing an encryption algorithm then means revealing
When the user reveals E he reveals a very ineﬃcient method of computing D(C):
testing all possible messages M until one such that E(M ) = C is found. If property
(c) is satisﬁed the number of such messages to test will be so large that this approach
is impractical.
A function E satisfying (a)-(c) is a “trap-door one-way function;” if it also satisﬁes
(d) it is a “trap-door one-way permutation.” Diﬃe and Hellman [1] introduced the
concept of trap-door one-way functions but did not present any examples. These
functions are called “one-way” because they are easy to compute in one direction but
(apparently) very diﬃcult to compute in the other direction. They are called “trapdoor” functions since the inverse functions are in fact easy to compute once certain
private “trap-door” information is known. A trap-door one-way function which also
satisﬁes (d) must be a permutation: every message is the cipertext for some other
message and every ciphertext is itself a permissible message. (The mapping is “oneto-one” and “onto”). Property (d) is needed only to implement “signatures.”
The reader is encouraged to read Diﬃe and Hellman’s excellent article [1] for
further background, for elaboration of the concept of a public-key cryptosystem, and
for a discussion of other problems in the area of cryptography. The ways in which
a public-key cryptosystem can ensure privacy and enable “signatures” (described in
Sections III and IV below) are also due to Diﬃe and Hellman.
For our scenarios we suppose that A and B (also known as Alice and Bob) are
two users of a public-key cryptosystem. We will distinguish their encryption and
decryption procedures with subscripts: EA, DA, EB, DB.
Encryption is the standard means of rendering a communication private. The sender
enciphers each message before transmitting it to the receiver. The receiver (but no
unauthorized person) knows the appropriate deciphering function to apply to the
received message to obtain the original message. An eavesdropper who hears the
transmitted message hears only “garbage” (the ciphertext) which makes no sense to
him since he does not know how to decrypt it.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 10: Approfondimento su DES e AES


La funzione crittograﬁca di DES
Il DES normale utilizza una funzione che si chiama Feistel (in ﬁgura), che
lavora su metà del blocco (E, in ﬁgura) e una sottochiave, che vengono
messe in XOR. Il risultato viene diviso in 8 parti da 6 bit e sostituito con
una apposita S-Box, ed inﬁne riordinati con una P-Box (permutation box),
anch’essa ﬁssa. Questa funzione viene ripetuta in ogni sottofase.
L’algoritmo di espansione della chiave in AES
L’algoritmo di espansione della chiave prende in input una word di 16 byte
e produce un array lineare di 44 word (176 byte), sufﬁcienti per fornire una
sottochiave al round iniziale e ai 10 main round.
La chiave viene copiata nella prima word della chiave espansa, mentre il
resto viene riempito quattro word per volta (i vari quadrati inizialmente
vuoti delle slide). Ogni word w[i] dipende dalla word immediatamente
precedente w[i–1] e dalla word di quattro posizioni prima w[i–4].
Per tre delle quattro word viene usato un semplice XOR (questo risponde
in parte alla tua domanda).
Per la prima word di ogni blocco (ovvero quella la cui posizione è multiplo
di 4, colorate diversamente nelle slide) viene usata una funzione più
complicata, chiamata “g”.
1. RotWord effettua uno shift a sinistra di un byte. Questo signiﬁca che
[B0,B1,B2,B3] diventa [B1,B2,B3,B0];
2. SubWord effettua una sostituzione usando la S-Box dell’algoritmo
Il risultato viene messo in XOR con una costante, chiamata
Rcon[j] (che in realtà è un vettore, per cui la costante cambia ad
ogni round–capire come funziona e perché va oltre gli scopi del
nostro corso e ha sempre a che fare con i campi di Galois).
Nella ﬁgura c’è uno schema di questi passaggi, chiamati “function g”.

---

## Sessione 11: Appunti di algebra per la crittografia a chiave pubblica RSA


ITS ICT Piemonte
Corso di Sicurezza Informatica
Appunti di Algebra
per la crittograﬁa a chiave
Prof. Marco Farina
marco.farina@its-ictpiemonte.it
Ultima revisione: 18 gennaio 2017.
1 Insiemi di numeri
Introduzione . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Naturali, interi, razionali . . . . . . . . . . . . . . . . . . . . .
2 L’algoritmo di Euclide
3 I numeri primi
4 Relazioni di congruenza
5 Il teorema di Euler-Fermat
6 I sistemi di crittograﬁa
7 L’algoritmo RSA
Il presente testo `e tratto alle lezioni del prof. Alberto Albano presso il
Dipartimento di Informatica dell’Universit`a di Torino.
Questo testo `e stato scritto usando LATEX, sistema originariamente sviluppato da
Leslie Lamport, basato su TEX creato da Donald Knuth.
1 Insiemi di numeri
ITS ICT Piemonte
Insiemi di numeri
I numeri sono cos`ı pervasivi del nostro mondo che se ne comincia a fare
conoscenza nei primi anni di vita e se ne continua a fare un uso via via pi`u
approfondito nella vita quotidiana e nel percorso scolastico ﬁno alle scuole
superiori. Resta tuttavia indispensabile per gli studenti che hanno deciso
di intraprendere studi di carattere scientiﬁco o tecnico ritornarci di nuovo
nei corsi che utilizzano concetti matematici di base. L’esigenza nasce dalla
necessit`a di fare alcuni chiarimenti su alcuni aspetti delicati e profondi dei
numeri, che giocano poi un ruolo fondamentale in tutta quanta la matematica in generale e la crittologia in particolare. Non si tratta tanto di questioni
fondazionali sul concetto di numero, che in questa sede non verranno aﬀrontate, quanto di questioni concrete da tenere ben presenti da chiunque voglia
utilizzare lo strumento matematico con perizia e sicurezza.
1.2 Naturali, interi, razionali
I primi numeri che si incontrano sono gli interi positivi, detti anche
numeri naturali: 1, 2, 3, . . . . L’insieme dei numeri naturali si indica con
il simbolo N. Sono i numeri che servono a contare e che hanno fatto la
prima comparsa nelle societ`a umane svariate migliaia di anni fa. Per fare
misure di quantit`a ﬁsiche come lunghezze, aree, tempi, temperature, ecc.,
`e tuttavia necessario poter disporre di sottoparti dell’unit`a e considerare
quindi numeri frazionari m/n dove m, n ∈ N con n (cid:54)= 0. `E poi conveniente
anche introdurre i numeri con il segno per poter trattare grandezze negative
come possono essere la temperatura, la velocit`a e molte altre grandezze
ﬁsiche. Si ottengono cos`ı i seguenti insiemi numerici:
0, ±1, ±2, . . .
| m, n ∈ Z, n (cid:54)= 0
numeri interi relativi,
numeri razionali.
Si hanno le evidenti inclusioni N ⊆ Z ⊆ Q. Talvolta `e anche utile considerare
numeri interi non negativi,
numeri razionali non negativi.
2 L’algoritmo di Euclide
ITS ICT Piemonte
2 L’algoritmo di Euclide
Da bambini abbiamo imparato che quando si divide 27 per 6 il quoziente
`e 4 ed il resto `e 3, cio`e che
27 = 6 · 4 + 3.
La cosa importante da notare `e che il resto deve essere un intero maggiore
o uguale a 0 e minore in senso stretto di 6. Anche se `e vero che, ad esempio
27 = 6 · 3 + 9,
si prende come resto 3 e non 9 perch´e 3 `e il pi`u piccolo intero positivo per
cui vale l’identit`a.
La propriet`a fondamentale di cui ci stiamo occupando si pu`o enunciare
in modo preciso con il seguente teorema.
Teorema 2.1 (della divisione). Se a ≥ 0 e b > 0 sono interi, esistono e
sono univocamente determinati gli interi q ≥ 0 ed r tali che
q ed r sono detti rispettivamente il quoziente e il resto della divisione.
La determinazione del quoziente e del resto si pu`o fare utilizzando l’algoritmo della divisione che abbiamo imparato nella scuola elementare. Ad
esempio, si provi ad applicare l’algoritmo per ottenere quoziente e resto della
divisione di 2731 diviso 43.
Deﬁnizione 2.1. Dati due interi a e b diciamo che b `e un divisore di a,
e scriviamo b|a se, dividendo a per b si ottiene resto 0, cio`e se a = qb.
Equivalentemente si dice che b divide a, oppure che a `e divisibile per b,
oppure ancora che a `e un multiplo di b.
Deﬁnizione 2.2. Dati due interi a e b, il numero positivo d tale che
1. d | a e d | b,
2. se c | a e c | b allora c | d
`e detto il massimo comun divisore di a e b e denotato con
2 L’algoritmo di Euclide
ITS ICT Piemonte

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 12: Esercizi di subnetting IPv4


Andrea Blanchietti
Fondamenti di Reti di Calcolatori
Esercizi di subnetting IPv4
Creare 16 sottoreti partendo dall’indirizzo di rete 192.168.10.0/24
Partendo dall’indirizzo di rete 172.16.0.0/16 individuare tutte possibili sottoreti
dimensionate su 2000 indirizzi host
Partendo da 172.16.128.0/19 creare otto sottoreti da 1000 indirizzi
Partizionare in due sottoreti la rete 10.0.192.0/20
• Per ogni sottorete indicare l’indirizzo di rete, il primo e l’ultimo indirizzo di
host e l’indirizzo di broadcast
• Quanti bit si devono promuovere?
• Quanti bit rimangono nella parte host dell’indirizzo? Quanti indirizzi di host
utilizzabili per sottorete?

---

## Sessione 13: Estratto da  L'arte dell'inganno  di Kevin Mitnick


L’arte dell’inganno
di Kevin Mitnick. Estratto dal cap. 4: Costruire la ﬁducia
Alcune di queste storie potrebbero indurvi a
pensare che considero perfetti idioti tutti
lavorano, pronti se non
addirittura smaniosi di cedere ogni segreto
che detengono. L’ingegnere sociale sa che
non è vero. Perché i suoi attacchi sono tanto
fortunati? Non perché la gente sia stupida o
priva di buon senso. Come esseri umani
siamo tutti vulnerabili ai raggiri perché
tendiamo a ﬁdarci
immotivatamente se
manipolati in una certa maniera.
in ﬁducia. Se è
L’ingegnere sociale anticipa i sospetti e
resistenze, ed è sempre pronto ribaltare la
programma l’attacco come se fosse una
partita a scacchi, anticipando le domande
che il bersaglio può porgli in modo da avere
sempre la risposta pronta.
Una delle tecniche più classiche prevede di
accattivarsi la ﬁducia della vittima. Come fa
un truffatore a convincervi a ﬁdarvi di lui?
Credetemi, ci riesce.
Fiducia: la chiave dell’inganno
Più l’ingegnere sociale riesce a far sembrare
roba di tutti i giorni il suo contatto, più evita
sospetti. Quando gli altri non hanno motivo
di sospettare, per lui è facile guadagnare la
Una volta ottenuta il ponte levatoio è
abbassato e la porta del castello è spalancata
per farlo entrare a prendere le informazioni
La prima telefonata: Andrea Lopez
Andrea Lopez ha risposto al telefono del
videonoleggio dove lavora, e un attimo dopo
sta sorridendo: è sempre un piacere quando
un cliente si prende il disturbo di dirle che è
contento del servizio. Questo qua ha appena
detto che ha avuto sempre ottime esperienze
con questo negozio, tanto che vorrebbe
mandare una lettera al titolare.
Quando gli chiede il nome del direttore e
l’indirizzo, Andrea dice subito il nome,
Tommy Allison, spiegando anche dove
abita. Il cliente stava per appendere ma
all’ultimo momento ha cambiato
dicendo: “Vorrei anche scrivere alla sede
centrale della vostra rete. Qual è il numero
della vostra ﬁliale?”. Lei gli dà anche questa
la ringrazia, aggiunge
qualche complimento su quanto è stata
gentile e la saluta.
“Una chiamata come questa fa passare più
svelto il turno di lavoro. Come sarebbe bello
se la gente fosse tutta così”,
pensava Andrea.
La seconda telefonata: Ginny
“Grazie per aver chiamato Studio Video.
Sono Ginny, in cosa posso esserle utile?”
“Ciao Ginny, sono Tommy Allison, titolare
di Forest Park, negozio 863. Abbiamo qui
un cliente che vorrebbe noleggiare Rocky 5,
ma abbiamo ﬁnito le copie. Puoi controllare
se ne avete?” le domanda pimpante colui
L’ARTE DELL’INGANNO
che chiama, con il tono di chi conosce
Ginny da una vita.
Lei torna in linea dopo qualche secondo
dicendo che ne hanno tre copie.
“Bene, adesso vedo se ha voglia di passare a
prenderla. Grazie. Se hai bisogno di un
favore basta che chiami e chiedi di Tommy,
sarò lieto di fare il possibile.”
Nelle due settimane seguenti Ginny riceve
tre o quattro chiamate da Tommy per
richieste varie. Sembrano domande
lui suona sempre molto
amichevole senza apparire assillante,
aggiungendo ogni tanto due chiacchiere tipo

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 14: Indirizzamento IPv4


Andrea Blanchietti
Fondamenti di Reti di Calcolatori
Indirizzamento IPv4
Indirizzamento con protocollo IPv4
L’indirizzo IPv4 è composto da una sequenza di 32 bit, suddivisa in quattro gruppi da 8 bit l’uno;
ogni gruppo è definito ottetto. La rappresentazione dell’indirizzo avviene convertendo i singoli
ottetti dal sistema binario al sistema decimale: si parla di notazione decimale puntata.
L’indirizzo possiede una struttura gerarchica: una parte dell’indirizzo definisce la rete nel suo
insieme e la rimanente parte individua l’host (PC, stampante, server, etc.) all’interno della rete. I
bit che definiscono la parte di rete sono individuati dalla subnet mask. Per esempio:
Anche la subnet mask ha una struttura a quattro ottetti e viene utilizzata per individuare la parte
rete all’interno dell’indirizzo. I bit di rete dell’indirizzo corrispondono ai bit con valore 1 nella
subnet mask, mentre i bit della parte host corrispondono ai bit con valore 0; nell’esempio
precedente, la rete è rappresentata dal primo, dal secondo e dal terzo ottetto, contando a partire
La parte di rete è sempre composta dai bit più significativi dell’indirizzo.
192.168.10.______________
Una seconda notazione possibile per indicare i bit di rete all’interno dell’indirizzo è utilizzare il
Prefix Length (tradotto letteralmente in lunghezza del prefisso), ovvero un numero che indica
quanti sono i bit della parte rete.
Usando l’esempio precedente, ho 24 bit di rete:
192.168.10.23/24
Nell’indirizzamento IPv4, per ogni rete vi sono due indirizzi riservati: il network address (indirizzo
di rete, ovvero l’indirizzo che rappresenta la rete nel suo complesso) e il broadcast address
(indirizzo di broadcast, ovvero l’indirizzo per le comunicazioni da un singolo host a tutti gli host
• Nell’indirizzo di rete (network address), tutti i bit della parte host sono pari a 0
• Nell’indirizzo di broadcast, tutti i bit della parte host sono pari a 1
Usando l’esempio precedente, considerando una subnet mask pari a 255.255.255.0:
Network address:
tutti I bit della parte host sono 0
Broadcast address:
tutti I bit della parte host sono 1
Tutti i rimanenti indirizzi compresi fra 192.168.10.1 e 192.168.10.254 sono utilizzabili per
indirizzare gli host all’interno della rete. Il numero di indirizzi disponibili per gli host di una rete
dipende da quanti bit abbiamo a disposizione.
Dato un network address, quanti indirizzi si hanno a disposizione per gli host?
Dati n bit nella parte host di un indirizzo, quante combinazioni si possono ottenere?
Tolgo il network address ed il broadcast e ottengo il numero di indirizzi di host per un certo
indirizzo di rete:
Numero indirizzi disponibili = 2n - 2
Esempio: 192.168.10.____________ 28 – 2 = 254 indirizzi disponibili
Classi di indirizzamento
La struttura originale dell’indirizzamento IPv4 (legacy) prevede tre classi utilizzabili per indirizzare
le reti (indicate con le lettere A, B e C) più due classi ad uso speciale, ovvero la classe D degli
indirizzi multicast e la classe E per usi sperimentali.
• La seconda colonna della tabella indica, per ogni classe, l’intervallo dei valori possibili per il
primo ottetto dell’indirizzo.
• La terza colonna della tabella indica, per ogni classe, l’intervallo dei valori possibili in binario
per il primo ottetto dell’indirizzo.
• La quarta colonna della tabella indica con la lettera N gli ottetti di rete e con la lettera H gli
ottetti della parte host.
• La quinta colonna riporta la subnet nask per le tre classi di indirizzamento A, B e C (non è
prevista per le classi D ed E)
Indirizzi privati
All’interno delle tre classi di indirizzamento (A, B e C), vi sono tre sottogruppi riservati per
indirizzare le reti private e non sono utilizzabili per indirizzare risorse su internet (in generale su
“rete pubblica”); sono definiti indirizzi privati e sono i seguenti:
• CLASSE A: Indirizzo di rete 10.0.0.0 con subnet mask 255.0.0.0, anche indicato con la
notazione 10.0.0.0/8
• CLASSE B: Indirizzi di rete dal 172.16.0.0 al 172.31.0.0 con subnet mask 255.255.0.0
• CLASSE C: Indirizzi di rete 192.168. X .0 con subnet mask 255.255.255.0, dove il terzo
ottetto X può assumere un valore compreso tra 0 e 255
TABELLA RIASSUNTIVA INDIRIZZI IPv4 PRIVATI
INDIRIZZO DI RETE
NOTAZIONE CON PREFIX
192.168.255.0/24
Dato un indirizzo IP, come possiamo risalire all’indirizzo di rete (network address) e
all’indirizzo di broadcast?
Dato un indirizzo IPv4, voglio sapere quale è la rete di appartenenza (ovvero l’indirizzo di rete), a quale
indirizzo di broadcast corrisponde e a quale intervallo degli indirizzi appartiene.
Si deve individuare la parte host e la parte rete dell’indirizzo, in base alla maschera di sottorete o al prefix
ESEMPIO 1. 192.168.10.5/24 è un indirizzo utilizzabile per indirizzare un host e corrisponde a:
192.168.10.0/24
192.168.10.255/24
da 192.168.10.1 a 192.168.10.254
ESEMPIO 2. 172.21.152.12/16 è un indirizzo utilizzabile per indirizzare un host e corrisponde a:
172.21.255.255/8
da 172.21.0.1 a 172.21.255.254
ESEMPIO 3. 10.16.42.10/8 è un indirizzo utilizzabile per indirizzare un host e corrisponde a:
10.255.255.255/8
da 10.0.0.1 a 10.255.255.254

---

## Sessione 15: InterVLAN Routing


Routing inter-VLAN
Obiettivi del modulo
Titolo del modulo: Routing inter-VLAN
Obiettivo del modulo: Risolvere i problemi di routing inter-VLAN sui dispositivi di Layer 3
Titolo argomento
Obiettivo argomento
Funzionamento del routing interVLAN
Descrivere le opzioni per la configurazione del routing
Routing inter-VLAN router-on-a-stick Configurare il router-on-a-stick inter-VLAN routing.
Routing inter-VLAN utilizzando
Configurare il routing inter-VLAN utilizzando lo
switching Layer 3
Risoluzione dei problemi relativi al
routing inter-VLAN
Risolvere i problemi comuni di configurazione tra
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Cos'è il routing inter-VLAN?
Le VLAN vengono utilizzate per segmentare le reti Layer 2 commutate per una serie di motivi.
Indipendentemente dal motivo, gli host in una VLAN non possono comunicare con gli host in un'altra
VLAN a meno che non sia presente un router o uno switch Layer 3 per fornire servizi di routing.
Il routing inter-VLAN è il processo di inoltro del traffico di rete da una VLAN a un'altra VLAN.
Esistono tre opzioni di routing inter-VLAN:
• Routing inter-VLAN legacy - Questa è una soluzione legacy. Ha una scalabilità minima.
• Router-on-a-stick - Questa è una soluzione accettabile per una rete di piccole e medie
• Switch di livello 3 utilizzando interfacce virtuali commutate (SVI) - Questa è la soluzione più
scalabile per organizzazioni di medie e grandi dimensioni.
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Routing legacy inter-VLAN
La prima soluzione di routing inter-VLAN si basava sull'utilizzo di un router con più interfacce
Ethernet. Ogni interfaccia router è stata collegata a una porta switch in diverse VLAN. Le
interfacce del router fungono da gateway predefiniti per gli host locali nella subnet VLAN.
Il routing inter-VLAN legacy utilizzando interfacce fisiche funziona, ma ha una limitazione
significativa. Non è ragionevolmente scalabile perché i router hanno un numero limitato di
interfacce fisiche. La richiesta di un'interfaccia router fisica per VLAN esaurisce rapidamente la
capacità dell'interfaccia fisica di un router.
Nota: Questo metodo di routing inter-VLAN non è più implementato nelle reti commutate ed è
incluso solo a scopo esplicativo.
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Routing router-on-a-stick inter-VLAN
Il metodo di routing inter-VLAN "router-on-a-stick" supera la limitazione del metodo di routing inter-VLAN
legacy. Richiede solo un'interfaccia Ethernet fisica per instradare il traffico tra più VLAN su una rete.
• Un'interfaccia Ethernet router Cisco IOS è configurata come un trunk 802.1Q e collegata a una porta
trunk su uno switch Layer 2. In particolare, l'interfaccia del router è configurata utilizzando subinterfacce
per identificare VLAN instradabili.
Le subinterfacce configurate sono interfacce virtuali basate su software. Ciascuna è associata a
un'unica interfaccia Ethernet fisica. Le subinterfacce sono configurate nel software su un router. Ogni
sottointerfaccia è configurata in modo indipendente con un indirizzo IP e un'assegnazione VLAN. Le
subinterfacce sono configurate per subnet diverse che corrispondono alla loro assegnazione VLAN.
Questo facilita il routing logico.
• Quando il traffico con tag VLAN entra nell'interfaccia del router, viene inoltrato alla sottointerfaccia
VLAN. Dopo che una decisione di routing è stata presa in base all'indirizzo di rete IP di destinazione, il
router determina l'interfaccia di uscita per il traffico. Se l'interfaccia di uscita è configurata come
sottointerfaccia 802.1q, i frame di dati vengono contrassegnati da VLAN con la nuova VLAN e inviati
nuovamente l'interfaccia fisica.
Nota: Il metodo router-on-a-stick del routing inter-VLAN non supera 50 VLAN.
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3
Il metodo moderno per eseguire il routing inter-VLAN consiste nell'utilizzare gli switch di Layer 3 e le
interfacce virtuali commutate (SVI). Un SVI è un'interfaccia virtuale configurata su uno switch Layer 3,
come mostrato nella figura.
Nota: Uno switch Layer 3 è anche chiamato interruttore multilayer in quanto opera al Layer 2 e al Layer
3. Tuttavia, in questo corso usiamo il termine switch Layer 3.
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3 (seguito)
Gli SVI inter-VLAN vengono creati nello stesso modo in cui viene configurata l'interfaccia VLAN di
gestione. L'SVI viene creato per una VLAN esistente sullo switch. Anche se virtuale, l'SVI svolge le
stesse funzioni per la VLAN come farebbe un'interfaccia router. In particolare, fornisce l'elaborazione

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 16: LAB configure-router-on-a-stick-inter-vlan-routing


Lab - Configure Router-on-a-Stick Inter-VLAN Routing
Addressing Table
Default Gateway
Interface Assigned
S1: F0/2-4, F0/7-24, G0/1-2
S2: F0/2-17, F0/19-24, G0/1-2
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public
www.netacad.com
Lab - Configure Router-on-a-Stick Inter-VLAN Routing
Part 1: Build the Network and Configure Basic Device Settings
Part 2: Create VLANs and Assign Switch Ports
Part 3: Configure an 802.1Q Trunk between the Switches
Part 4: Configure Inter-VLAN Routing on the Router
Part 5: Verify Inter-VLAN Routing is working
Background / Scenario
Modern switches use virtual local-area networks (VLANs) to provide segmentation services traditionally
provided by routers in LAN configurations. VLANs address scalability, security, and network management. In
general, VLANs make it easier to design a network to support the goals of an organization. Communication
between VLANs requires a device operating at Layer 3 of the OSI model. Routers in VLAN topologies provide
additional security and traffic flow management.
VLAN trunks are used to span VLANs across multiple devices. Trunks allow the traffic from multiple VLANS to
travel over a single link, while keeping the VLAN identification and segmentation intact. A particular kind of
inter-VLAN routing, called “Router-On-A-Stick”, uses a trunk from the router to the switch to enable all VLANs
to pass to the router.
In this lab, you will create VLANs on both switches in the topology, assign VLANs to switch access ports,
verify that VLANs are working as expected, create VLAN trunks between the two switches and between S1
and R1, and configure Inter-VLAN routing on R1 to allow hosts in different VLANs to communicate, regardless
of which subnet the host resides.
Note: The routers used with CCNA hands-on labs are Cisco 4221 with Cisco IOS XE Release 16.9.4
(universalk9 image). The switches used in the labs are Cisco Catalyst 2960s with Cisco IOS Release 15.2(2)
(lanbasek9 image). Other routers, switches, and Cisco IOS versions can be used. Depending on the model
and Cisco IOS version, the commands available and the output produced might vary from what is shown in
the labs. Refer to the Router Interface Summary Table at the end of the lab for the correct interface identifiers.
Note: Ensure that the routers and switches have been erased and have no startup configurations. If you are
unsure, contact your instructor.
Required Resources
• 1 Router (Cisco 4221 with Cisco IOS XE Release 16.9.4 universal image or comparable)
• 2 Switches (Cisco 2960 with Cisco IOS Release 15.2(2) lanbasek9 image or comparable)
• 2 PCs (Windows with a terminal emulation program, such as Tera Term)
• Console cables to configure the Cisco IOS devices via the console ports
• Ethernet cables as shown in the topology
Part 1: Build the Network and Configure Basic Device Settings
In Part 1, you will set up the network topology and configure basic settings on the PC hosts and switches.
Step 1: Cable the network as shown in the topology.
Attach the devices as shown in the topology diagram, and cable as necessary.
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public
www.netacad.com
Lab - Configure Router-on-a-Stick Inter-VLAN Routing
Step 2: Configure basic settings for the router.
Open configuration window
a. Console into the router and enable privileged EXEC mode.
b. Enter configuration mode.
c. Assign a device name to the router.
d. Disable DNS lookup to prevent the router from attempting to translate incorrectly entered commands as
though they were host names.
e. Assign class as the privileged EXEC encrypted password.
f. Assign cisco as the console password and enable login.
g. Assign cisco as the VTY password and enable login.
h. Encrypt the plaintext passwords.
i. Create a banner that warns anyone accessing the device that unauthorized access is prohibited.
j. Save the running configuration to the startup configuration file.
k. Set the clock on the router.
Note: Use the question mark (?) to help with the correct sequence of parameters needed to execute this
Close configuration window
Step 3: Configure basic settings for each switch.
Open configuration window
a. Console into the switch and enable privileged EXEC mode.
b. Enter configuration mode.
c. Assign a device name to the switch.
d. Disable DNS lookup to prevent the router from attempting to translate incorrectly entered commands as
though they were host names.
e. Assign class as the privileged EXEC encrypted password.
f. Assign cisco as the console password and enable login.
g. Assign cisco as the vty password and enable login.
h. Encrypt the plaintext passwords.
i. Create a banner that warns anyone accessing the device that unauthorized access is prohibited.
j. Set the clock on the switch.
Note: Use the question mark (?) to help with the correct sequence of parameters needed to ex ecute this
k. Copy the running configuration to the startup configuration.
Close configuration window

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 17: Lab - Identifying IPv4 Addresses


Laboratorio: Individuazione degli indirizzi IPv4
Sezione 1: Individuare gli indirizzi IPv4
Sezione 2: Classificare gli indirizzi IPv4
Introduzione e scenario
In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4).
Si identificheranno i diversi tipi di indirizzi IPv4 e i componenti che formano l'indirizzo, come la porzione rete e
dell'host, nonché la subnet mask. I tipi di indirizzi analizzati includono quelli pubblici, privati, unicast e
Risorse necessarie
• Dispositivo con accesso a Internet
• Facoltativo: calcolatore degli indirizzi IPv4
Individuare gli indirizzi IPv4
Nella Sezione 1 vengono forniti alcuni esempi di indirizzi IPv4 e si completeranno le tabelle con le
informazioni appropriate.
Fase 1: Analizzare la tabella riportata di seguito e identificare la porzione rete e dell'host degli
indirizzi IPv4 forniti.
Le prime due righe mostrano alcuni esempi di come completare la tabella.
Sigle della tabella:
N = tutti gli 8 bit di un ottetto sono nella porzione rete dell'indirizzo
n = un bit nella porzione rete dell'indirizzo
H = tutti gli 8 bit di un ottetto sono nella porzione dell'host dell'indirizzo
h = un bit nella porzione dell'host dell'indirizzo
N, n = rete, H, h = host
Indirizzo di rete
192.168.10.10/24
10.101.99.17/23
209.165.200.227/27
172.31.45.252/24
172.16.117.77/20
209.165.202.140/27
192.168.28.45/28
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco.
Laboratorio: Individuazione degli indirizzi IPv4
Fase 2: Analizzare la tabella seguente ed elencare l'intervallo degli indirizzi host e di broadcast
sulla base di una coppia rete/maschera del prefisso.
Le prima riga mostra un esempio di come completare la tabella.
Indirizzo del primo
Indirizzo dell'ultimo
Indirizzo di broadcast
192.168.10.10/24
10.101.99.17/23
209.165.200.227/27
172.31.45.252/24
172.16.117.77/20
209.165.202.140/27
192.168.28.45/28
Sezione 2: Classificare gli indirizzi IPv4
Nella Sezione 2 si identificheranno e classificheranno diversi esempi di indirizzi IPv4.
Fase 1: Analizzare la tabella riportata di seguito e identificare il tipo di indirizzo (rete, host,
multicast o indirizzo di broadcast).
Le prima riga mostra un esempio di come completare la tabella.
Tipo di indirizzo
255.255.255.252
255.255.255.192
255.255.255.240
209.165.202.159
255.255.255.224
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco.
Laboratorio: Individuazione degli indirizzi IPv4
Fase 2: Analizzare la tabella riportata di seguito e identificare l'indirizzo come pubblico o
Indirizzo IP/prefisso
Pubblico o privato
209.165.201.30/27
192.168.255.253/24
10.100.11.103/16
172.30.1.100/28
172.20.18.150/22
128.107.10.1/16
192.135.250.10/24
Fase 3: Analizzare la tabella riportata di seguito e identificare se la coppia indirizzo/prefisso è
un indirizzo dell'host valido.
Indirizzo dell'host
172.16.255.0/16
241.19.10.100/24
192.168.0.254/24
192.31.7.255/24
64.102.255.255/14
198.133.219.8/24
Approfondimento
Perché dovremmo continuare a studiare l'indirizzamento IPv4 se lo spazio degli indirizzi IPv4 disponibile è
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco.

---

## Sessione 18: SOL Lab - Identifying IPv4 Addresses


Laboratorio: Individuazione degli indirizzi IPv4
Sezione 1: Individuare gli indirizzi IPv4
Sezione 2: Classificare gli indirizzi IPv4
Introduzione e scenario
In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4).
Si identificheranno i diversi tipi di indirizzi IPv4 e i componenti che formano l'indirizzo, come la porzione rete e
dell'host, nonché la subnet mask. I tipi di indirizzi analizzati includono quelli pubblici, privati, unicast e
Risorse necessarie
• Dispositivo con accesso a Internet
• Facoltativo: calcolatore degli indirizzi IPv4
Individuare gli indirizzi IPv4
Nella Sezione 1 vengono forniti alcuni esempi di indirizzi IPv4 e si completeranno le tabelle con le
informazioni appropriate.
Fase 1: Analizzare la tabella riportata di seguito e identificare la porzione rete e dell'host degli
indirizzi IPv4 forniti.
Le prime due righe mostrano alcuni esempi di come completare la tabella.
Sigle della tabella:
N = tutti gli 8 bit di un ottetto sono nella porzione rete dell'indirizzo
n = un bit nella porzione rete dell'indirizzo
H = tutti gli 8 bit di un ottetto sono nella porzione dell'host dell'indirizzo
h = un bit nella porzione dell'host dell'indirizzo
N, n = rete, H, h = host
Indirizzo di rete
192.168.10.10/24
10.101.99.17/23
209.165.200.227/27
172.31.45.252/24
172.16.117.77/20
209.165.202.140/27
192.168.28.45/28
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco.
Laboratorio: Individuazione degli indirizzi IPv4
Fase 2: Analizzare la tabella seguente ed elencare l'intervallo degli indirizzi host e di broadcast
sulla base di una coppia rete/maschera del prefisso.
Le prima riga mostra un esempio di come completare la tabella.
Indirizzo del primo
Indirizzo dell'ultimo
Indirizzo di broadcast
192.168.10.10/24
10.101.99.17/23
209.165.200.227/27
172.31.45.252/24
172.16.117.77/20
209.165.202.140/27
192.168.28.45/28
Sezione 2: Classificare gli indirizzi IPv4
Nella Sezione 2 si identificheranno e classificheranno diversi esempi di indirizzi IPv4.
Fase 1: Analizzare la tabella riportata di seguito e identificare il tipo di indirizzo (rete, host,
multicast o indirizzo di broadcast).
Le prima riga mostra un esempio di come completare la tabella.
Tipo di indirizzo
255.255.255.252
255.255.255.192
255.255.255.240
209.165.202.159
255.255.255.224
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco.
Laboratorio: Individuazione degli indirizzi IPv4
Fase 2: Analizzare la tabella riportata di seguito e identificare l'indirizzo come pubblico o
Indirizzo IP/prefisso
Pubblico o privato
209.165.201.30/27
192.168.255.253/24
10.100.11.103/16
172.30.1.100/28
172.20.18.150/22
128.107.10.1/16
192.135.250.10/24
Fase 3: Analizzare la tabella riportata di seguito e identificare se la coppia indirizzo/prefisso è
un indirizzo dell'host valido.
Indirizzo dell'host
172.16.255.0/16
241.19.10.100/24
192.168.0.254/24
192.31.7.255/24
64.102.255.255/14
198.133.219.8/24
Approfondimento
Perché dovremmo continuare a studiare l'indirizzamento IPv4 se lo spazio degli indirizzi IPv4 disponibile è
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco.

---

## Sessione 19: Sistemi Numerici


Andrea Blanchietti
Fondamenti di Reti di Calcolatori
Sistemi numerici – Conversione tra sistemi
Sistema numerico posizionale
Quando si rappresenta un numero tramite un sistema numerico posizionale, valgono alcune regole
• Si deve definire una base (per esempio, nel sistema decimale la base è 10)
• Si definisce un insieme di simboli che saranno le cifre nella rappresentazione del numero; i
simboli andranno sempre da 0 al valore della base – 1
• Le cifre di un numero avranno un peso in base alla loro posizione nel numero
I pesi sono sempre calcolati come potenze della base
Sistema decimale (numero decimale, base 10)
• Simboli: 0 1 2 3 4 5 6 7 8 9
Il valore di un numero decimale è la somma delle potenze di DIECI, ognuna moltiplicata per il
valore della cifra corrispondente:
Esempio: 5127 = 5x103 + 1x102 + 2x101 + 7x100
Sistema binario (numero binario, base 2)
• Simboli 0 e 1 (il numero è rappresentato da una sequenza di 0 e 1)
Il valore di un numero binario è dato dalla somma di potenze di DUE, ognuna moltiplicata per il
valore della cifra corrispondente
Esempio: 10010110 = 1x27+0x26+0x25+1x24+0x23+1x22+1x21+0x20
Sistema esadecimale (numero esadecimale, base 16)
• Simboli: 0 1 2 3 4 5 6 7 8 9 A B C D E F
Il valore di un numero esadecimale è la somma delle potenze di SEDICI, ognuna moltiplicata
per il valore della cifra corrispondente, dove:
– A equivale a 10
– B equivale a 11
– C equivale a 12
– D equivale a 13
– E equivale a 14
– F equivale a 15
Esempio: FE8016 = Fx163 + Ex162 + 8x161 + 0x160
Conversione da un sistema con base qualsiasi ad un sistema base 10
• Si esprime il numero come somma delle potenze della base
• Si calcolano le potenze nel sistema decimale
• Si moltiplicano per le cifre corrispondenti
• Si somma il tutto
Esempio di conversione da binario a decimale
1011001 = 1×26 + 0×25 + 1×24 + 1×23 + 0×22 + 0×21 + 1×20 = 26 + 24 + 23 + 20 = 64 + 16 + 8 + 1 = 89
Esempio di conversione da esadecimale (base 16) a decimale
7B4116 = 7×163 + B×162 + 4×161 + 1×160 = 7×4096 + 11×256 + 4×16 + 1 = 31553
Conversione da decimale ad un numero espresso in una base r qualsiasi
• Si deve dividere ripetutamente per la base r il numero espresso in base 10
I resti delle divisioni rappresentano le cifre della rappresentazione in base r; il primo resto (in
alto) sarà la cifra meno significativa mentre l’ultimo resto (in basso) sarà la cifra più
Esempio: convertire 89 da decimale a binario
Risultato: 1011001
Esempio: convertire 31553 da decimale al corrispondente valore esadecimale
Risultato: 7B4116
Conversione da numero esadecimale a binario e viceversa
• Per passare da esadecimale a binario, ogni cifra di un numero esadecimale genera quattro bit
Esempio: convertire il numero esadecimale 722416 in binario
In binario: 111001000100100
• Per passare da binario a esadecimale, raggruppo i bit a gruppi di quattro partendo da destra
(bit meno significativo) e aggiungendo zeri a sinistra se necessario
Esempio: convertire il numero binario 1010111100011 in esadecimale
Aggiungiamo tre zeri per avere gruppi da 4 bit: 0001010111100011
0001 0101 1110 0011
In esadecimale: 15E316
Tabella di conversione esadecimale/binario
Conversione da numero decimale a numero esadecimale passando per la
rappresentazione nel sistema di numerazione binario
Invece di usare la conversione diretta da un numero decimale ad un numero esadecimale,
proviamo a fare un passaggio intermedio attraverso la rappresentazione binaria.
Dividere per 2 è più semplice rispetto a dividere per 16 (soprattutto nel calcolo dei resti) e passare
da un numero binario a un numero esadecimale è immediato
Esempio: convertire 31553 da decimale al corrispondente valore esadecimale
1. Converto 31553 in binario:
111101101000001
2. Converto il numero binario in esadecimale
0111 1011 0100 0001

---

## Sessione 20: VLAN


Obiettivi del modulo
Titolo del modulo: Protocolli e modelli
Obiettivo del modulo: Spiegare come i protocolli di rete consentono ai dispositivi di accedere alle
risorse di rete locali e remote.
Titolo argomento
Obiettivo argomento
Panoramica sulle VLAN
Spiegare lo scopo delle VLAN in una rete commutata.
VLAN in un ambiente multiswitch
Spiegare come uno switch inoltra i frame basati sulla
configurazione VLAN in un ambiente multi-switch.
Configurazione della VLAN
Configurare una porta switch da assegnare a una VLAN in base ai
Configurare una porta trunk su uno switch LAN.
Protocollo trunking dinamico Configurare il protocollo DTP (Dynamic Trunking Protocol).
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
Definizioni delle VLAN
Le VLAN sono connessioni logiche con altri
dispositivi simili.
L'inserimento di dispositivi in varie VLAN ha le
seguenti caratteristiche:
• Fornisce la segmentazione dei vari gruppi di
dispositivi sugli stessi switch
• Fornire un'organizzazione più gestibile
• Broadcast, multicast e unicast sono isolati
nella singola VLAN
• Ogni VLAN avrà una propria gamma unica
di indirizzamento IP
• Domini di broadcast più piccoli
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
Vantaggi di una
progettazione VLAN
I vantaggi dell'utilizzo delle VLAN
sono i seguenti:
Domini di broadcast
La divisione della LAN riduce il numero di domini broadcast
Maggiore sicurezza
Solo gli utenti della stessa VLAN possono comunicare insieme
Maggiore efficienza IT
Le VLAN possono raggruppare dispositivi con requisiti simili, ad esempio
facoltà e studenti
Riduzione dei costi
Uno switch può supportare più gruppi o VLAN
Prestazioni migliorate
I domini broadcast di piccole dimensioni riducono il traffico, migliorando la
larghezza di banda
Gestione semplificata
Gruppi simili avranno bisogno di applicazioni simili e altre risorse di rete
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
VLAN predefinita
La VLAN 1 è la seguente:
• La VLAN predefinita
• La VLAN nativa predefinita
• La VLAN di gestione
Impossibile eliminare o
Nota: Sebbene non sia
possibile eliminare VLAN1,
Cisco consiglia di assegnare
queste funzionalità predefinite
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Documento
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN (seguito)
• Dedicata al traffico generato dall'utente (email e traffico web).
• VLAN 1 è la VLAN dati predefinita perché tutte le interfacce sono assegnate a questa VLAN.
• Questa viene utilizzata solo per i collegamenti trunk.
• Tutti i frame sono contrassegnati su un collegamento trunk 802.1Q tranne quelli sulla VLAN
VLAN di gestione
• Questa viene utilizzata per il traffico SSH/Telnet VTY e non deve essere trasportata con il
traffico dell'utente finale.
• In genere, la VLAN che è SVI per lo switch Layer 2.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 21: Enigma Keys


ENIGMA M3 - UKW-B Reflector - Dec 1940 - Code Book
Date   Rotors     Ring  Plugboard setting   Pos.
+------------------------------------------------+
| 30 | IV V I    | LSQ | EG KI LA MZ UC WS | FEY |
+------------------------------------------------+
| 29 | V I III   | KNL | EI FG NC OK UQ YM | CNA |
+------------------------------------------------+
| 28 | II III I  | XVP | AJ FR IV WU XN YE | VPN |
+------------------------------------------------+
| 27 | IV I V    | SSH | EV GX HD JO TF WZ | YON |
+------------------------------------------------+
| 26 | II IV I   | FEE | FM HY RC SE TP WV | FZY |
+------------------------------------------------+
| 25 | IV II III | NOX | IB JZ MX PA RE SG | MBR |
+------------------------------------------------+
| 24 | IV I III  | XWX | BO HD LM NE TQ WU | RVC |
+------------------------------------------------+
| 23 | II III IV | PJK | FW GS HZ MN XO YL | KQL |
+------------------------------------------------+
| 22 | I II V    | ZKE | PF QW RD XN YJ ZL | ELU |
+------------------------------------------------+
| 21 | III II I  | VIP | BT MK NY QG RP WJ | ZAR |
+------------------------------------------------+
| 20 | I IV II   | RAT | AK BM GW OI PU TV | PGW |
+------------------------------------------------+
| 19 | I V III   | OGN | FD JR LM QX VI WH | RNF |
+------------------------------------------------+
| 18 | I III IV  | FHE | AG BK FJ HW RI US | ZRN |
+------------------------------------------------+
| 17 | I III V   | IGF | AG BX DV HF IN JO | ZMV |
+------------------------------------------------+
| 16 | I III V   | LGV | CN DY HA JG MS VL | FQB |
+------------------------------------------------+
| 15 | I IV V    | VJH | FZ GH IT JE OQ PK | TYG |
+------------------------------------------------+
| 14 | V I III   | YIT | AC EZ MB QJ TU XV | KRC |
+------------------------------------------------+
| 13 | V III I   | HUM | AV HC JZ NB OT XP | SDZ |
+------------------------------------------------+
| 12 | I IV II   | UQI | CE HK JT UO VS ZP | XON |
+------------------------------------------------+
| 11 | IV V III  | GHQ | BV HF KS QM TA YZ | FOX |
+------------------------------------------------+
| 10 | III I IV  | RBW | EP IG MK RX TN UZ | VDP |
+------------------------------------------------+
|  9 | III V IV  | CAY | EZ LI ON PH UG VA | XIG |
+------------------------------------------------+
|  8 | IV II V   | KTH | GU LE QB TI WC YF | OBF |
+------------------------------------------------+
|  7 | V II IV   | SRK | HC KS LM OB QA XW | LCZ |
+------------------------------------------------+
|  6 | II IV V   | NSE | CZ JG LS PN TO UF | WOO |
+------------------------------------------------+
|  5 | V III II  | WIS | AY BL QH UE VD ZT | WNP |
+------------------------------------------------+
|  4 | V I IV    | MJJ | BL DQ EG FT HC KA | KFB |
+------------------------------------------------+
|  3 | III V II  | EHM | KG PF SU TW YI ZC | FXY |
+------------------------------------------------+
|  2 | IV I II   | FLZ | AC DW EL NK VU ZG | YCM |
+------------------------------------------------+
|  1 | II I IV   | LFI | EK FO JZ PR QY UN | OQM |
+------------------------------------------------+

---

## Sessione 22: Soluzione esercizio AES


# Genera un IV esadecimale corretto
openssl rand -hex 16 > iv.txt
# Genera una chiave binaria
openssl rand 32 > key.bin
# Converti la chiave binaria in esadecimale
KEY_HEX=$(xxd -p key.bin | tr -d '\n')
# Leggi l'IV da file e rimuovi eventuali ritorni a capo
IV_HEX=$(cat iv.txt | tr -d '\n')
# Cifra il messaggio con AES-256-CBC
openssl enc -aes-256-cbc -K "$KEY_HEX" -iv "$IV_HEX" -in messaggio.txt -out messaggio.enc


---
*Totale: 22 sessioni generate il 02/07/2026*