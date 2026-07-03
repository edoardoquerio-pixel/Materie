# Lezione 02

## Panoramica
Password profiling, namedropping, pretexting, tailgating,

## Argomenti trattati
Sicurezza, Crittografia, Reti, Data Analytics, Git

---
## Appunti

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
*Fonte: 002_02_Gestione_delle_password.md*
