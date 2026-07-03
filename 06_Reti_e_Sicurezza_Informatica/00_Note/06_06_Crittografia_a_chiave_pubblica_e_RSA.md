# 06. Crittografia a chiave pubblica e RSA

**File:** `06. Crittografia a chiave pubblica e RSA.pdf`
**Tipo:** `.pdf`
**Dimensione:** 22130.0 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Crittografia a chiave pubblica e RSA
v 2.2.3 ~ mar 2026
changelog

I favolosi anni ‘70
1969
ArpaNet
1971
FTP
1974
TCP
1978
IP
“We propose that it is possible to develop systems in which two parties 
communicating solely over a public channel and using only publicly known 
techniques can create a secure connection. We examine two approaches to this 
problem, called 
public key cryptosystems
 and 
public key distribution systems
, 
respectively. The first are more powerful, lending themselves to the solution of the 
authentication problems, while the second are much closer to realization. ” 
New Directions in Cryptography
, Whitfield Diffie e Martin Hellman, novembre 1976
Diffie explains public-key encryption
Martin Hellman on cryptography
New Directions in Cryptography
Rivest on the origins of RSA


1Public Key 
Encryption


Cifrari simmetrici
CIPHERTEXT
PLAINTEXT
 PLAINTEXT
Encryption
 Decryption
Simmetria
 Permutazioni e sostituzioni

Rompere la simmetria
CIPHERTEXT
PLAINTEXT
 PLAINTEXT
Chiave pubblica
 Chiave privata
Asimmetria delle chiavi
 Basato su funzioni matematiche

Creare un canale di comunicazione

canale cifrato
Creare un canale di comunicazione
Dopo essersi scambiati le chiavi 
pubbliche Alice e Bob hanno 
instaurato un canale di 
comunicazione sicuro.

Inviare un messaggio crittografato
S
t
e
v
e 
o
n
l
y 
w
o
n 
b
e
c
a
u
s
e 
I 
l
e
t 
h
i
m
, 
l
o
l
.

Inviare un messaggio crittografato
S
t
e
v
e 
o
n
l
y 
w
o
n 
b
e
c
a
u
s
e 
I 
l
e
t 
h
i
m
, 
l
o
l
.

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
H
Q
T
3
E
0
m
5
O
k
m
K
b
M
P
M
a
d
f
Q
q
w
D
r
R
d
r
H
G
m
Y
s
h
C
b
4
q
O
K
y
6
w
7
R
R
F
g
t
b
r
6
M
h
4
8
U
1
Q
V
E
I
c
O

Inviare un messaggio crittografato
H
Q
T
3
E
0
m
5
O
k
m
K
b
M
P
M
a
d
f
Q
q
w
D
r
R
d
r
H
G
m
Y
s
h
C
b
4
q
O
K
y
6
w
7
R
R
F
g
t
b
r
6
M
h
4
8
U
1
Q
V
E
I
c
O

Inviare un messaggio crittografato
Steve only 
won because 
I let him, lol.
Alice usa la sua chiave privata per 
decrittare il messaggio inviato da Bob.

Inviare un messaggio …?
S
t
e
v
e 
o
n
l
y 
w
o
n 
b
e
c
a
u
s
e 
I 
l
e
t 
h
i
m
, 
l
o
l
.

Inviare un messaggio …?
S
t
e
v
e 
o
n
l
y 
w
o
n 
b
e
c
a
u
s
e 
I 
l
e
t 
h
i
m
, 
l
o
l
.

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
1
L
b
K
3
o
f
O
f
0
L
F
T
k
f
x
V
M
B
a
n
T
e
p
6
P
n
c
U
c
i
D
V
O
V
G
U
p
W
j
R
b
l
6
O
G
Z
K
V
C
l
0
2
1
v
C
7
S
d
N
x
J
m

Inviare un messaggio …?
1
L
b
K
3
o
f
O
f
0
L
F
T
k
f
x
V
M
B
a
n
T
e
p
6
P
n
c
U
c
i
D
V
O
V
G
U
p
W
j
R
b
l
6
O
G
Z
K
V
C
l
0
2
1
v
C
7
S
d
N
x
J
m

Inviare un messaggio …?
Steve only 
won because 
I let him, lol.
Alice usa la chiave pubblica di Bob per 
decrittare il messaggio ricevuto.
…perché
/questionmark

Inviare un messaggio 
autenticato
!
Steve only 
won because 
I let him, lol.
Alice è sicura che il messaggio 
provenga davvero da Bob. Il 
messaggio è stato 
firmato
.
Bob Stark

Creare canali cifrati multipli


Creare canali cifrati multipli


“God rewards fools”
Computer 
science lab, 
7th floor
1976…
 …1977

Ron 
R
ivest
Adi 
S
hamir
Leonard 
A
dleman

Ron 
R
ivest
Adi 
S
hamir
Leonard 
A
dleman

2RSA Encryption


Encryption function
Me(modn)=C
CIPHERTEXT
PLAINTEXT


Principio di identità
Me(modn)=C Cd(modn)=M
CIPHERTEXT
PLAINTEXT
 PLAINTEXT
Funzione di crittografia
 Funzione di decrittografia

Esempio
Eseguite la cifratura e decifratura per verificare il 
principio di 
identità
. Per i calcoli usate wolframalpha.com. 
 
 
 
M
=
42
e
=
17
n
=
3233
d
=
2753
Me(modn)=C
Cd(modn)=M
4217(mod3233)=2557 25572753(mod3233)=42
Soluzione:

3La matematica di 
RSA


A caccia di funzioni unidirezionali
1889/uni22C53547=
6700283
10s
Quanto tempo ci vuole 
per calcolare … 
/questionmark
p1/uni22C5p2=6700283???
Quanto tempo serve per scomporre un numero in fattori primi
/questionmark

Scomposizione in fattori primi
per gli amici, “fattorizzazione”
p1/uni22C5p2=6700283
T rovare il più piccolo numero primo 
 la cui divisione è intera (ovvero dà resto 0).
p
1
No, quindi dobbiamo procedere per divisioni successive.
La complessità computazionale è data dal numero di divisioni che devo fare.
Come si fattorizza un numero?
Abbiamo una formula per calcolarlo?
E quindi quanto tempo ci vuole?
Dipende da quanti numeri primi ci sono prima di 
.
p
1
E quante divisioni devo fare?

Quanti numeri primi ci sono prima di 
?
x
Funzione enumerativa /uni03C0(x)
Conta
 quanti numeri primi ci sono prima di 
.
x
La funzione 
  è ad oggi 
sconosciuta.
/uni03C0
(
x
)
È approssimabile con la 
funzione 
 .
x
/
ln
(
x
)
limx/uni2192/uni221E
/uni03C0(x)
x/ln(x)=1
Attenzione: 
 in questo 
contesto non ha niente a 
che fare con il numero 
/uni03C0
3,14
…

Quindi quante divisioni devo fare?
p1/uni22C5p2=6700283
/uni03C0(1889)=290 1889
ln(1889)/uni2248250
1 moltiplicazione: circa 10 secondi
290 divisioni: circa 
48 minuti
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
p1/uni22C5p2=

Tutto molto bello, ma…
come si calcolano le chiave pubblica e privata
/questionmark
1.
Scegliere due numeri primi molto grandi per ottenere 
.
n
2.
Calcolare la funzione 
 .
/uni03C6
(
n
)
3.
Scegliere di conseguenza l’esponente 
.
e
4.
Calcolare 
.
d

Scegliere due numeri primi molto grandi
Questo è il primo ostacolo: come troviamo numeri primi da 2048 bit
/questionmark
Te s t  d i  M i l l e r - R a b i n
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
Questo è il primo ostacolo: come troviamo numeri primi da 2048 bit
/questionmark
Te s t  d i  M i l l e r - R a b i n
p/uni22C5q=n
Numeri primi molto grandi
 Primo pezzo della 
chiave pubblica


Calcolare la funzione 
/uni03C6
(
n
)
Leonhard Euler 
Basilea, 15 aprile 1707  
San Pietroburgo, 18 
settembre 1783
Gli interi 
 e 
 si dicono 
coprimi
 se e solo se non hanno 
nessun divisore comune, eccetto 
 e 
  o, in modo 
equivalente, 
se il loro M.C.D. è 
.
a
b
1
−
1
1
Ad esempio, 
 e 
 sono coprimi, perché non hanno 
nessun divisore comune, mentre 
 e 
 non sono coprimi 
perché entrambi sono divisibili per 
.
6
35
6
27
3
La funzione 
 di Eulero (detta anche 
funzione 
toziente
) è definita per ogni 
  come il numero 
degli interi compresi tra 
 e 
 coprimi con 
.
/uni03C6
z
/uni2208
/uni2124
1
z
 z


Calcolare la funzione 
/uni03C6
(
n
)
Leonhard Euler 
Basilea, 15 aprile 1707  
San Pietroburgo, 18 
settembre 1783
La funzione 
 di Eulero (detta anche 
funzione 
toziente
) è definita per ogni 
  come il numero 
degli interi compresi tra 
 e 
 coprimi con 
.
/uni03C6
z
/uni2208
/uni2124
1
z
 z
, poiché i numeri minori di 
 coprimi con 
 sono: 
, 
, 
 e 
.
/uni03C6
(
8
)
=
4
 8
 8
1
3
5
7
, poiché essendo 
 primo, tutti i numeri 
sono coprimi con esso.
/uni03C6
(
11
)
=
10
 11
Esempio
Corollario
Quanto vale 
 /questionmark
/uni03C6
(
11
)


Calcolare la funzione 
/uni03C6
(
n
)
Cosa sono i 
punti sulla 
diagonale
/questionmark
I numeri primi!

Proprietà della funzione 
/uni03C6
1. Primalità/uni03C6(p)=(p−1)
2. Moltiplicatività/uni03C6(ab)=/uni03C6(a)/uni22C5/uni03C6(b)
n:=(p/uni22C5q)/uni2192/uni03C6(n)=/uni03C6(p/uni22C5q)
=/uni03C6(p)/uni22C5/uni03C6(q)
=(p−1)(q−1)
(per la moltiplicatività)
(per la primalità)

Scegliere gli esponenti 
 e 
e
d
Questo numero viene usato per una questione di efficienza 
computazionale e risparmio energetico. La sua rappresentazione 
binaria infatti è 
10000000000000001
, ovvero un numero 
sufficientemente grande ma con solo due 1 al suo interno.
Scegliamo un numero 
 che sia:
e
relativamente piccolo, maggiore di 
 e minore di 
 ;
2
 /uni03C6
(
n
)
coprimo con 
 .
/uni03C6
(
n
)
gli standard solitamente usano il numero 
 .
65537

Scegliere gli esponenti 
 e 
e
d
Scegliamo un numero 
 che sia: 
relativamente piccolo, maggiore di 
 e minore di 
 ; 
coprimo con 
 . 
gli standard solitamente usano il numero 
 .
e
2
 /uni03C6
(
n
)
/uni03C6
(
n
)
65537
Calcoliamo la chiave privata 
 risolvendo l’equazione:
d
ed(mod/uni03C6(n))=1
Il calcolo è facilmente risolvibile tramite l’
algoritmo esteso di Euclide
.

Crittoanalisi
Per individuare la chiave privata 
 è sufficiente per Eve risolvere 
l’equazione
d
ed(mod/uni03C6(n))=1
L ’attaccante ha però due incognite: la chiave privata 
 e la 
funzione toziente 
 .
d
/uni03C6
(
n
)
Eve ha due modi per calcolare 
 :
/uni03C6
(
n
)
contare i coprimi con 
 (
non
 conosciamo una formula) oppure
n
fattorizzare 
 (
non
 conosciamo una formula).
n
Entrambi i calcoli sono 
computazionalmente impossibili
.

Riassumendo…
1.
Scegliere due numeri primi molto grandi 
 e 
;
p
q
2.
Calcolare 
 ;
n
=
p
/uni22C5
q
3.
Calcolare 
 ;
/uni03C6
(
n
)
=
(
p
−
1
)
/uni22C5
(
q
−
1
)
4.
Scegliere 
 coprimo e minore di 
 ;
e
 /uni03C6
(
n
)
5.
Risolvere 
  per calcolare 
;
e
d
(
mod
/uni03C6
(
n
)
)
=
1
 d
6.
Cancellare 
 e 
;
p
q
7.
T enere segreta la chiave privata 
 e distribuire la 
chiave pubblica 
 .
d
(
e
,
n
)

RSA factoring Challenge
Le chiavi RSA oggi comunemente usate sono di 2048 bit.
Il più grande 
 ad oggi fattorizzato è 
RSA-250
, un numero di 
829 bit. È stato fattorizzato il 28 febbraio 2020.
n
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


Shamir
 Rivest
 Adleman
 Merkle
 Hellman
Diffie
The greatest cryptographers of 
all time
