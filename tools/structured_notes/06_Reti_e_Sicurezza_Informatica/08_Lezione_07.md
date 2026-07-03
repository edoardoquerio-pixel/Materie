# Lezione 07

## Panoramica
Come possiamo verificare che nessuno si sia

## Argomenti trattati
Sicurezza, Git, Data Analytics, API REST, Reti

---
## Appunti

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
*Fonte: 007_07_Certificati_digitali_e_hashing.md*
