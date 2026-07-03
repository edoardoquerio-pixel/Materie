# 07. Certificati digitali e hashing

**File:** `07. Certificati digitali e hashing.pdf`
**Tipo:** `.pdf`
**Dimensione:** 13268.1 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Certificati digitali e hashing
v 3.2.4 ~ apr 2026
changelog

Risolvere il Man-in-the-middle
Canale
Come possiamo verificare che nessuno si sia 
messo in mezzo alla comunicazione
/questionmark 
Verifica manuale Certificazione
(tra due lezioni…)


Certificato
Certificazione delle informazioni pubbliche
L ’informazione pubblica può essere 
falsificata, quindi:
viene distribuita all’interno di un certificato;
il certificato è firmato digitalmente e non 
può essere contraffatto.
Chiave 
pubblica e 
info
Firma 
digitale


1La firma digitale

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT


La firma digitale
PLAINTEXT


La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm

La firma digitale
PLAINTEXT
PLAINTEXT
Hashing 
algorithm
=?

La firma digitale
PLAINTEXT
Hashing 
algorithm
=?
PLAINTEXT
Hashing 
algorithm
PLAINTEXT


2Algoritmi di 
hashing

Le funzioni di hashing
Messaggio
Hash
H=h(M)
Funzione di hashing
M
h
H

Le funzioni di hashing
L ’hash è una 
funzione non invertibile
 che mappa una stringa di 
lunghezza arbitraria in una stringa di lunghezza predefinita.
1.
A partire dall’hash non è possibile risalire alla stringa originale.

Le funzioni di hashing
L ’hash è una funzione non invertibile che mappa una stringa di 
lunghezza arbitraria
 in una stringa di lunghezza predefinita.
1.
A partire dall’hash non è possibile risalire alla stringa originale.
2.
L ’input può essere di qualunque dimensione.

Le funzioni di hashing
L ’hash è una funzione non invertibile che mappa una stringa di 
lunghezza arbitraria in una stringa di 
lunghezza predefinita
.
1.
A partire dall’hash non è possibile risalire alla stringa originale.
2.
L ’input può essere di qualunque dimensione.
3.
L ’output ha una dimensione fissa.

Qualquadra non cosa.
T utti i messaggi 
possibili
di tutti gli hash 
possibili.
sono di più

Qualquadra non cosa.
Collisioni
T utti i messaggi 
possibili
di tutti gli hash 
possibili.
sono di più

Resistenza alle collisioni
Data una stringa 
 è 
computazionalmente impossibile 
trovare la stringa 
  tale che 
.
x
y
/uni2260
x
h
(
y
)
=
h
(
x
)
Resistenza debole
È computazionalmente impossibile 
trovare una qualsiasi coppia  
tale che 
 .
(
x
,
y
)
h
(
x
)
=
h
(
y
)
Resistenza forte
…
Fissato un 
messaggio ed il 
suo hash…
…un altro messaggio 
con lo stesso hash è 
impossibile da 
trovare.
Nope
/exclamationmark
Nope
/exclamationmark
Nope
/exclamationmark
Nope
/exclamationmark
Nope
/exclamationmark
Nope
/exclamationmark

Una semplice funzione di hashing
Input:
101110100101011
Creiamo una funzione 
  che prende in input 
 bit e restituisce un 
digest
 lungo 
.
h
(
x
)
 n
 5
/u1D7F7/u1D7F6/u1D7F7/u1D7F7/u1D7F7/uni2295
/u1D7F6/u1D7F7/u1D7F6/u1D7F6/u1D7F7/uni2295
/u1D7F6/u1D7F7/u1D7F6/u1D7F7/u1D7F7=
/u1D7F7/u1D7F6/u1D7F7/u1D7F6/u1D7F7Output:
Questa funzione prende il nome di 
controllo di ridondanza longitudinale.

Back in the days: MD5
Anno:
1991
Autore:
Ron Rivest
Input:
di qualunque lunghezza, ovviamente.
Output:
128 bit
OpenSSL:
openssl dgst -md5 filename
php:
md5($string)
md5_file($filename)

PLEASE DON’T DO THA T
MD5 è 
deprecato
 per qualunque funzione di sicurezza.
Ho ucciso per 
molto meno.
<?php 
 $notSoSecureDigest = md5("monkey"); 
 $suchStringMuchSecurity = md5(md5("monkey")); 
$pleaseKillMeNow =    
md5(md5(md5(md5(md5(md5(md5(md5(md5(md5(md5(md5("monkey")))))))))))); 
?>

Secure Hash Algorithm
SHA è una famiglia di algoritmi.
SHA-1 SHA-2 SHA-3
(deprecato dal 2011)
Digital Certificate signatures
Email PGP/GPG signatures
Software vendor signatures
Software updates
ISO checksums
Backup systems
Deduplication systems
GIT
...
shattered.it
(2001)
SHA-224
SHA-256
SHA-384
SHA-512
(2015)
algoritmo Keccak
openssl dgst -sha256 filename
(Si pronuncia k
ɛ
t
ʃ
æk, 
un po’ come ketchup, 
ma con la k finale)

3I certificati digitali

Certificare la chiave pubblica
Certificato digitale
www.avengers.comSubject:
CertificationAuthority1Issuer:
Validity:
10/03/2023
Public Key:
 Signature:

Public Key Infrastructure
Web Server 
avengers.com
Certificate Authority
Registration Authority
HTTPS request
Root 
Certificate Authority
CA certificate
Subject certificate
Subject
Relying party
OCSP Responder 
(Online Certificate 
Status Protocol) 
CRL distribution point
Certificate 
Revocation 
List (CRL)


avengers.comSubject:
CA1Issuer:
Validity:
10/03/2022
Public Key:
Server certificate
X.509 Certificate issuance
Web Server
Certificate Authority
Root CA
CA1Subject:
RootCAIssuer:
Validity:
10/03/2024
Public Key:
CA1 certificate
RootCASubject:
RootCAIssuer:
Validity:
10/03/2032
Public Key:
RootCA certificate
Self-sign
RootCA sign
CA1 sign

Questo certificato, con 
una chiave pubblica 
falsificata, può essere 
sostituito a quello 
originale perché ha la 
stessa firma digitale, 
data da una collisione!
Perché le collisioni sono pericolose?
avengers.comSubject:
Public Key:
3F4AC50A
Signature:
01AB9F5E
Certificato 
Digitale
avengers.comSubject:
Public Key:
5D9197D5
Signature:
72026ECB
CerTificato 
digitale
avengers.comSubject:
Public Key:
67CFA2B7
Signature:
7AA52331
CertifiCato 
digitale
avengers.comSubject:
Public Key:
C7AA9930
Signature:
01AB9F5E
Certificato 
digitAle
avengers.comSubject:
Public Key:
28199261
Signature:
5D35EC64
CertificatO 
digitale
…
Se riuscissi a trovare 
una collisione potrei 
creare un certificato 
falso!
L ’algoritmo di hash scelto è estremamente importante per evitare le collisioni
/exclamationmark

4HTTPS e TLS

Considerazioni sulla web security
Complessità Escalation Utonti
I contenuti web  sono 
straordinariamente 
complessi e possono 
nascondere problemi 
di sicurezza.
I server web possono 
essere exploitati e 
usati come trampolino 
verso la rete aziendale 
interna.
Gli utenti tipici dei 
servizi web non sono 
addestrati alle 
tematiche della 
security.

Approcci alla web security
Network
 T ransport
 Application
HTTP
 FTP
 SMTP
TCP
IP/IP Sec
HTTP
 FTP
 SMTP
TLS/SSL
TCP
IP
S/MIME
 HTTPS
Kerberos
 SMTP
 HTTP
UDP
 TCP
IP

Transport Layer Security
Privacy Integrità Identificazione
Sembri ingrassato
Algoritmi crittografici 
per nascondere il 
traffico dati.
I dati non vengono 
alterati durante il 
transito in rete.
Il certificato digitale 
permette di identificare 
l’altra parte coinvolta.

SSL/TLS
Fase 1
Negoziazione fra le parti 
degli algoritmi da utilizzare
Fase 2
Scambio delle chiavi 
e autenticazione
Fase 3
Cifratura simmetrica e 
autenticazione dei messaggi
Diffie-Hellman
 RSA
 AES-256
 HMAC-SHA

https://
HTTPS è la combinazione di HTTP e SSL/TLS che implementa una connessione 
sicura tra browser (client) e web server, fornendo:
Autenticazione del sito
 Protezione della privacy
Integrità dei dati
Con l’utilizzo di HTTPS viene usata la porta 443 e viene invocato TLS che cifra:
l’URL del documento richiesto;
il contenuto del documento;
il contenuto dei form riempiti dall’utente;
i cookie scambiati tra browser e web server;
il contenuto dell’header HTTP.

Puoi trovare TLS in…
VPN
 instant message
Web
HTTPS
e-mail
S/MIME

Esercizio: S/MIME
https://extrassl.actalis.it/portal/uapub/freemail

