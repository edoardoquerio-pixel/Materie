# Lezione 06

Fonte: `06. Crittografia a chiave pubblica e RSA.pdf`

Docente

Prof. Marco Farina

Unità formativa

Sicurezza Informatica

Argomento

Crittografia a chiave pubblica e RSA

Intervento realizzato da

changelog

v 2.2.3 ~ mar 2026

I favolosi anni ‘70

1969

1971

1974

ArpaNet

FTP

TCP

1978

IP

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

Encryption

1Public Key 

Cifrari simmetrici

PLAIN
TEXT

CIPHER
TEXT

PLAIN
TEXT

Encryption

Decryption

Simmetria

Permutazioni e sostituzioni

Rompere la simmetria

PLAIN
TEXT

CIPHER
TEXT

PLAIN
TEXT

Chiave pubblica

Chiave privata

Asimmetria delle chiavi

Basato su funzioni matematiche

Creare un canale di comunicazione

Creare un canale di comunicazione

canale cifrato

Dopo essersi scambiati le chiavi 
pubbliche Alice e Bob hanno 
instaurato un canale di 
comunicazione sicuro.

Inviare un messaggio crittografato

Steve only 
won because 
I let him, lol.

Inviare un messaggio crittografato

Steve only 
won because 
I let him, lol.

Inviare un messaggio crittografato

HQT3E0m5O
kmKbMPMad
fQqwDrRdr
HGmYshCb4
qOKy6w7RR
Fgtbr6Mh4
8U1QVEIcO

Bob usa la chiave pubblica di Alice 
per crittografare il messaggio.

Inviare un messaggio crittografato

HQT3E0m5O
kmKbMPMad
fQqwDrRdr
HGmYshCb4
qOKy6w7RR
Fgtbr6Mh4
8U1QVEIcO

Inviare un messaggio crittografato

HQT3E0m5O
kmKbMPMad
fQqwDrRdr
HGmYshCb4
qOKy6w7RR
Fgtbr6Mh4
8U1QVEIcO

Inviare un messaggio crittografato

Steve only 
won because 
I let him, lol.

Alice usa la sua chiave privata per 
decrittare il messaggio inviato da Bob.

Inviare un messaggio …?

Steve only 
won because 
I let him, lol.

Inviare un messaggio …?

Steve only 
won because 
I let him, lol.

Inviare un messaggio …?

1LbK3ofOf
0LFTkfxVM
BanTep6Pn
cUciDVOVG
UpWjRbl6O
GZKVCl021
vC7SdNxJm

Bob usa la sua chiave privata per 
crittografare il messaggio.

Inviare un messaggio …?

1LbK3ofOf
0LFTkfxVM
BanTep6Pn
cUciDVOVG
UpWjRbl6O
GZKVCl021
vC7SdNxJm

Inviare un messaggio …?

1LbK3ofOf
0LFTkfxVM
BanTep6Pn
cUciDVOVG
UpWjRbl6O
GZKVCl021
vC7SdNxJm

Inviare un messaggio …?

Steve only 
won because 
I let him, lol.

Alice usa la chiave pubblica di Bob per 
decrittare il messaggio ricevuto.

…perché!

Inviare un messaggio autenticato!

Steve only 
won because 
I let him, lol.

Bob Stark

Alice è sicura che il messaggio 
provenga davvero da Bob. Il 
messaggio è stato firmato.

Creare canali cifrati multipli

Creare canali cifrati multipli

“God rewards fools”

1976…

Computer 
science lab, 
7th floor

…1977

Ron Rivest

Leonard 
Adleman

Adi Shamir

Ron Rivest

Leonard 
Adleman

Adi Shamir

2RSA Encryption

Encryption function

PLAIN
TEXT

CIPHER
TEXT

Me (mod n) = C

Principio di identità

PLAIN
TEXT

CIPHER
TEXT

PLAIN
TEXT

Me (mod n) = C

Cd (mod n) = M

Funzione di crittografia

Funzione di decrittografia

Esempio

Eseguite la cifratura e decifratura per verificare il principio di 
identità. Per i calcoli usate wolframalpha.com. 

M = 42
e = 17
n = 3233
d = 2753

Me (mod n) = C
Cd (mod n) = M

Soluzione:
4217 (mod 3233) = 2557

25572753 (mod 3233) = 42

 
 
 
3La matematica di 

RSA

A caccia di funzioni unidirezionali

Quanto tempo ci vuole 
per calcolare … !

6 700 283 10s
p1 ⋅ p2 = 6 700 283 ???

Quanto tempo serve per scomporre un numero in fattori primi!

1889⋅3547=Scomposizione in fattori primi
per gli amici, “fattorizzazione”
p1 ⋅ p2 = 6 700 283

Come si fattorizza un numero?

Trovare il più piccolo numero primo 

p1
Abbiamo una formula per calcolarlo?

 la cui divisione è intera (ovvero dà resto 0).

No, quindi dobbiamo procedere per divisioni successive.

E quindi quanto tempo ci vuole?

La complessità computazionale è data dal numero di divisioni che devo fare.

E quante divisioni devo fare?

Dipende da quanti numeri primi ci sono prima di 

.p1

Quanti numeri primi ci sono prima di ?x
Funzione enumerativa π(x)
.x

Conta quanti numeri primi ci sono prima di 

Attenzione: 
contesto non ha niente a 
che fare con il numero 
3,14…

 in questo 

π

La funzione 
sconosciuta.

π(x)

 è ad oggi 

È approssimabile con la 
x/ln(x)
.
funzione 

π(x)
x/ln(x)

lim
x→∞

= 1

Quindi quante divisioni devo fare?
p1 ⋅ p2 = 6 700 283

π(1889) = 290

1889
ln(1889)

≈ 250

1 moltiplicazione: circa 10 secondi

290 divisioni: circa 48 minuti

La moltiplicazione di due primi è una funzione unidirezionale.

227018012937850141935804051202045867410612359627
6658390709402187921517148311913989487013309111104
49016834009494838468182995180417635079489225907
74925466088171879259465921026597046700449819899
096862039460017743094473811056991294128542891880
85536270740767072259373777266697344097736124333
63973080517630915068363107953126072395203652900
321058488395079814523072994171857157962974549950
235053160409198591937180233074148804462179228008
31766040938656344571034778553457121080530736394
53592393265186603051504106096643731332367283153
93235000679371075419554373624332483612425259458
68802353916766181532375855504886901432221349733

p1 ⋅ p2 =

227018012937850141935804051202045867410612359627
6658390709402187921517148311913989487013309111104
49016834009494838468182995180417635079489225907
74925466088171879259465921026597046700449819899
096862039460017743094473811056991294128542891880
85536270740767072259373777266697344097736124333
63973080517630915068363107953126072395203652900
321058488395079814523072994171857157962974549950
235053160409198591937180233074148804462179228008
31766040938656344571034778553457121080530736394
53592393265186603051504106096643731332367283153
93235000679371075419554373624332483612425259458
68802353916766181532375855504886901432221349733

Tutto molto bello, ma…
come si calcolano le chiave pubblica e privata!

1. Scegliere due numeri primi molto grandi per ottenere 
.φ(n)

2. Calcolare la funzione 

.n

3. Scegliere di conseguenza l’esponente 

.e

4. Calcolare 

.d

Scegliere due numeri primi molto grandi
Questo è il primo ostacolo: come troviamo numeri primi da 2048 bit!

Test di Miller-Rabin

write n as 2r·d + 1 with d odd (by factoring out powers of 2 from n − 1)
WitnessLoop: repeat k times:
 pick a random integer a in the range [2, n − 2]
 x ← ad mod n
 if x = 1 or x = n − 1 then
 continue WitnessLoop
 repeat r − 1 times:
 x ← x2 mod n
 if x = n − 1 then
 continue WitnessLoop
 return “composite”
return “probably prime”

La precisione può essere aumentata a scapito del tempo di esecuzione.

Scegliere due numeri primi molto grandi
Questo è il primo ostacolo: come troviamo numeri primi da 2048 bit!

Test di Miller-Rabin

p ⋅ q = n

Numeri primi molto grandi

Primo pezzo della 
chiave pubblica

Calcolare la funzione φ(n)

φ

La funzione 
toziente) è definita per ogni 
1 z
 e 
degli interi compresi tra 

 di Eulero (detta anche funzione 
z ∈ ℤ
 come il numero 
z
 coprimi con 
.

Leonhard Euler 

Basilea, 15 aprile 1707 

San Pietroburgo, 18 
settembre 1783

a b
 e 

Gli interi 
nessun divisore comune, eccetto 
1
equivalente, se il loro M.C.D. è 
.

 si dicono coprimi se e solo se non hanno 

1 −1
 e 

 o, in modo 

6 35
 e 
Ad esempio, 
 sono coprimi, perché non hanno 
6 27
nessun divisore comune, mentre 
 e 
3
perché entrambi sono divisibili per 
.

 non sono coprimi 

Calcolare la funzione φ(n)

φ

La funzione 
toziente) è definita per ogni 
1 z
 e 
degli interi compresi tra 

 di Eulero (detta anche funzione 
z ∈ ℤ
 come il numero 
z
 coprimi con 
.

Esempio

φ(8) = 4
8
, poiché i numeri minori di 
1 3 5 7
.
, 
, 

 e 

Quanto vale 

φ(11)

!

8
 coprimi con 

 sono: 

Leonhard Euler 

Basilea, 15 aprile 1707 

San Pietroburgo, 18 
settembre 1783

φ(11) = 10
sono coprimi con esso.

, poiché essendo 

Corollario
11

 primo, tutti i numeri 

Calcolare la funzione φ(n)

Cosa sono i 
punti sulla 
diagonale!

I numeri primi!

Proprietà della funzione φ
1. Primalità φ(p) = (p − 1)
2. Moltiplicatività φ(ab) = φ(a) ⋅ φ(b)
n := (p ⋅ q) → φ(n) = φ(p ⋅ q)

(per la moltiplicatività)

(per la primalità)

= φ(p) ⋅ φ(q)
= (p − 1)(q − 1)

Scegliere gli esponenti 

 e e d

e
Scegliamo un numero 
 che sia:

2
relativamente piccolo, maggiore di 
 e minore di 
.φ(n)
coprimo con 
gli standard solitamente usano il numero 

65537

.

φ(n)
;

Questo numero viene usato per una questione di efficienza 
computazionale e risparmio energetico. La sua rappresentazione 
binaria infatti è 10000000000000001, ovvero un numero 
sufficientemente grande ma con solo due 1 al suo interno.

Scegliere gli esponenti 

 e e d

e
Scegliamo un numero 
 che sia: 

2
relativamente piccolo, maggiore di 
 e minore di 
coprimo con 
gli standard solitamente usano il numero 

φ(n)
. 

65537

.

φ(n)
; 

d
Calcoliamo la chiave privata 

 risolvendo l’equazione:

ed (mod φ(n)) = 1

Il calcolo è facilmente risolvibile tramite l’algoritmo esteso di Euclide.

Crittoanalisi
d
Per individuare la chiave privata 
 è sufficiente per Eve risolvere 
l’equazione

ed (mod φ(n)) = 1

d
L’attaccante ha però due incognite: la chiave privata 
 e la 
funzione toziente 

φ(n)
.

Eve ha due modi per calcolare 

:φ(n)

n
contare i coprimi con 
 (non conosciamo una formula) oppure
n
fattorizzare 

 (non conosciamo una formula).

Entrambi i calcoli sono computazionalmente impossibili.

Riassumendo…

1. Scegliere due numeri primi molto grandi 

p q
 e 

;

2. Calcolare 

n = p ⋅ q
;
φ(n) = (p−1) ⋅ (q−1)
3. Calcolare 
;
e
φ(n)
 coprimo e minore di 
;
ed (mod φ(n)) = 1
p q
;
 e 

6. Cancellare 

4. Scegliere 

5. Risolvere 

d
 per calcolare 
;

d
7. Tenere segreta la chiave privata 
 e distribuire la 

chiave pubblica 

(e, n)

.

RSA factoring Challenge
Le chiavi RSA oggi comunemente usate sono di 2048 bit.

n
Il più grande 
829 bit. È stato fattorizzato il 28 febbraio 2020.

 ad oggi fattorizzato è RSA-250, un numero di 

RSA-250 
140324650240744961264423072839333563008614715144755017797754920881
418023447140136643345519095804679610992851872470914587687396261921
557363047454770520805119056493106687691590019759405693457452230589
325976697471681738069364894699871578494975937497937 
= 
641352894770715802787901901705773890848250147429434472081168596320
24532344630238623598752668347708737661925585694639798853367 
x 
333720275949781565562260106053551142279407603447675546667845209870
23841729210037080257448673296881877565718986258036932062711

The greatest cryptographers of 
all time

Shamir

Rivest

Adleman Merkle

Hellman Diffie