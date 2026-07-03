# 05. Diffie-Hellman key exchange

**File:** `05. Diffie-Hellman key exchange.pdf`
**Tipo:** `.pdf`
**Dimensione:** 25969.4 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Diffie-Hellman-Merkle key exchange
v 3.4.4 ~ mar 2026
changelog

1Le chiavi 
crittografiche

Proprietà delle chiavi crittografiche
Condivisa
Casuale Protetta
La potenza di un sistema crittografico dipende 
dalla tecnica usata per condividere la chiave.

Come si può condividere la chiave?
KEY
EXPRESS
Alice Liddell
Abingdon Road 42
Oxford
A mano Te r z a  p a r t e
Canale 
sicuro
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
non può funzionare
?


Composizione di cifrature
Chiave di Bob
abcdefghijklmnopqrstuvwxyz 
CPMGATNOJEFWIQBURYHXSDZKLV
Chiave di Alice
abcdefghijklmnopqrstuvwxyz 
HFSUGTAKVDEOYJBPNXWCQRIMZL
ci vediamo all una
SV RGUVHYB HOO QJH
HD YNSDOLP OBB REO
AJ MQCJLZP LOO VKL
ei cnaiywb yhh zxy
Messaggio
Cifrato da Bob
Cifrato da Alice
Decifrato da Bob
Decifrato da Alice


I puzzle 
di Merkle


I puzzle di Merkle
Bob genera 
 puzzle e 
li pubblica.
2
n

I puzzle di Merkle
482739
857
Ogni puzzle, se risolto, 
contiene un ID e una 
chiave casuale.
Bob genera 
 puzzle e 
li pubblica.
2
n

I puzzle di Merkle
Bob genera 
 puzzle e 
li pubblica.
2
n
Alice sceglie 
casualmente un puzzle

I puzzle di Merkle
Bob genera 
 puzzle e 
li pubblica.
2
n
Alice sceglie 
casualmente un puzzle
182374
537
…e lo risolve.

I puzzle di Merkle
Alice invia l
’
ID a Bob e 
tiene copia della chiave
182374
537


I puzzle di Merkle
Alice invia l
’
ID a Bob e 
tiene copia della chiave
182374
537
182374
Bob sa quale puzzle risolvere 
per ottenere la chiave

I puzzle di Merkle
537
L
’
attaccante può intercettare l
’
ID, ma deve risolvere, in media, 
  puzzle 
(ovvero la metà di quelli generati) per scoprire la chiave condivisa.
2
n
−
1

Il metodo dei colori


Chiave segreta condivisa


Chiave segreta condivisa
Dati pubblici


2Fondamenti di 
matematica
NO.

Insiemi numerici
 
Complessi
ℕ
 
Reali
ℤ
 
Razionali
ℚ
 
Interi
ℝ
 
Naturali
ℂ
 
Immaginari
𝕀
3
11
−1
π
3+2i
2

Insiemi numerici
 
Complessi
ℕ
 
Reali
ℤ
 
Razionali
ℚ
 
Interi
ℝ
 
Naturali
ℂ
 
Immaginari
𝕀
3
11
−1
π
3+2i
2


Te o r e m a  d e l l a  d i v i s i o n e
DEF
Se 
  e 
  sono interi, esistono e sono univocamente 
determinati gli interi 
  ed 
 tali che 
a
≥
0
b
>
0
q
≥
0
 r
     e     
a
=
b
q
+
r
 0
≤
r
<
|
b
|
 ed 
 sono detti rispettivamente il 
quoziente
 e il 
resto
 della divisione.
q
 r
q
 q
 …
 q
 q
 r
a
 blocchi grandi 
 più un certo resto 
.
b
 q
 r

I numeri primi
DEF
Un numero intero 
 si dice primo se:
p
๏
 ;
p
≠
{
−
1,
1,
0
}
๏
per ogni 
 , se 
 divide 
, allora 
 .
a
∈
ℝ
 a
 p
 a
∈
{
−
1,
1,
p
,
−
p
}
In altre parole, un intero è un primo se è diverso da 
  e non 
ha 
divisori propri
.
{
−
1,
1,
0
}
PRIME AWARDS
1
2
p
3
p
4
5
p
6
7
p
8
9
10
11
p
12
13
p
14
15
16


Te o r e m a  fondamentale
 dell
’
aritmetica
60
80
100
180
160
140
120
MA TH DEPARTMENT
EUCLIDE
DEF
Sia 
  un intero diverso da 
 . Allora esistono numeri 
primi  
   tali che
z
∈
ℝ
 {
−
1,
0,
1
}
p
1
,
p
2
,
…
,
p
n
 
z
=
p
1
⋅
p
2
⋅
…
⋅
p
n
Inoltre tale 
fattorizzazione
 è unica, a meno del segno dei numeri primi 
e del loro ordine nel prodotto.
Fattorizzazione
Euclide (Grecia, -III/-V sec.), negli 
Elementi
, insieme all
’
esistenza 
della fattorizzazione, aveva dimostrato una proposizione, oggi nota 
come 
lemma di Euclide
, dalla quale si ricava la proprietà di 
fattorizzazione unica. 
Il teorema fu poi dimostrato esplicitamente per la prima volta da 
Gauss nelle 
Disquisitiones Arithmeticae
.

Aritmetica dell
’
orologio
12
3
4
57
8
10
11
2
1
6
9
Siamo a Londra e sono le 9 del mattino. Abbiamo un 
appuntamento tra 8 ore. A che ora abbiamo l
’
appuntamento
?

Aritmetica dell
’
orologio
12
3
4
57
8
10
11
2
1
6
9

Aritmetica dell
’
orologio
12
3
4
57
8
10
11
2
1
6
9
Siamo a Londra e sono le 9 del mattino. Abbiamo un 
appuntamento tra 8 ore. A che ora abbiamo 
l
’
appuntamento
?
Qual è il rapporto tra il  e il ?517

Aritmetica dell
’
orologio
12
3
4
57
8
10
11
2
1
6
9
Siamo a Londra e sono le 9 del mattino. Abbiamo un 
appuntamento tra 8 ore. A che ora abbiamo 
l
’
appuntamento
?
Qual è il rapporto tra il  e il ?517
 è il resto della divisione intera tra 
  e 
!
5
 17
12
Possiamo definire tutte le operazioni aritmetiche nel 
“mondo dell
’
orologio” .
Possiamo astrarre l
’
idea di orologio e immaginarlo con  
ore sul quadrante.
n

Relazioni di congruenza
DEF
Fissiamo un intero 
, con 
 . I due numeri 
  sono detti 
congruenti modulo 
 se 
 . In questo caso si scrive
n
 n
≥
2
 a
,
b
∈
ℝ
n
n
|
(
b
−
a
)
a
≡
b
mod
n
o, equivalentemente, 
 .
a
mod
n
=
b
Esempio (orologio).
Fissiamo 
  e scegliamo 
  e 
 .
n
=
12
 a
=
3
b
=
15
Questi numeri sono congruenti in modulo 
 se 
 , che è 
vero. Dunque:
12
12
|
(
15
−
3
)
3
≡
15
mod
12

Invertibilità di una funzione
DEF
Se una funzione  
  è sia iniettiva che suriettiva, allora esiste 
una corrispondenza biunivoca tra i due insiemi 
 e 
.
f
:
X
→
Y
X
Y
Si può in questo caso definire la funzione inversa
f
−
1
(
y
)
⟺
f
(
x
)
=
y
Una funzione viene detta 
unidirezionale
 (
one-way function
) se è 
computazionalmente difficile da invertire.


3Diffie-Hellman-
Merkle Key Exchange

Diffie, Hellman e Merkle
Whitfield Diffie
Martin Hellman
Ralph Merkle
Dopo due millenni di buio il problema 
dello scambio delle chiavi viene risolto 
nel 1976. 
È il primo metodo pratico per scambiare 
chiavi crittografiche in un canale insicuro 
ed è tutt
’
oggi comunemente usato.

A caccia di funzioni unidirezionali
an=b b=
nvolte
a⋅a⋅…⋅a
an≡bmodc b=
Quantevolte?
a⋅a⋅…⋅a
Non esiste un modo facile per calcolarlo
! 
Bisogna provare tutti i numeri
!

Esempio
3xmod7=1Problema:
31mod7=1
32mod7=1
33mod7=1
34mod7=1
35mod7=1
36mod7=1
Nope.3=7⋅0+3
9=7⋅1+2
27=7⋅3+6
81=7⋅11+4
243=7⋅34+5
729=7⋅104+1
Nope.
Nope.
Nope.
Nope.
F**k yeah!
Soluzione:x=6n,n∈ℝ,n≥0

La funzione “logaritmo discreto”
ax=bmodn
gi=bmodp
Il modulo è un 
numero primo 
 e la base dell
’
esponente è un 
generatore
 del 
 .
p
 mod
p
Ma… cosa diavolo è un generatore
?


Cosa sono i generatori di un numero primo?
1
6
2
2
3
12
4
4
5
7
6
8
7
14
8
16
9
11
10
15
11
5
12
13
13
10
14
9
15
3
16
1
i=1 61mod17=6
i=2 62mod17=2
i=3 63mod17=12
…
i=(p−1) 616mod17=1
i
6imod17
Possiamo quindi verificare che 
  è un generatore di 
  poiché dal calcolo vengono 
generati tutti i numeri da
 a 
 .
g
=
6
 p
=
17
1
p
−
1
Esempio:
scegliamo 
  e 
 . Calcoliamo 
  con 
g
=
6
p
=
17
 6
i
mod
p
 i
=
[
1,
p
−
1
]
In un gruppo di interi modulo n, un numero primo relativo a n genera tutti gli elementi del gruppo, infatti se si 
utilizza la moltiplicazione mod n per generare elementi da un numero primo si può generare qualsiasi 
elemento del gruppo. 
In generale, un generatore di un gruppo è un elemento che “genera” il gruppo, ovvero che 
moltiplicato per un elemento del gruppo genera un altro elemento del gruppo e cosi via.

Chiave segreta condivisa
Dati pubblici


K è la chiave 
segreta 
condivisa
XB∈[1,p−1]
YB=gXB(modp)
XA∈[1,p−1]
YA=gXA(modp)
YA YB
K=YXB
A (modp) K=YXA
B (modp)
Di comune accordo vengono scelti 
 e 
.
g
p
L
’
algoritmo Diffie-Hellman-Merkle


XB=10∈[1,16]
YB=610(mod17)=15
XA=15∈[1,16]
YA=615(mod17)=3
YA=3 YB=15
K=310(mod17)=8 K=1515(mod17)=8
Di comune accordo vengono scelti 
  e 
 .
g
=
6
p
=
17
L
’
algoritmo Diffie-Hellman-Merkle


Dimostrazione
Supponiamo per assurdo che 
 .
K
A
≠
K
B
Per definizione sappiamo che 
  e che 
 .
Y
A
=
g
X
A
(
mod
p
)
 Y
B
=
g
X
B
(
mod
p
)
Sappiamo inoltre che:
KA=YXA
B (modp) KB=YXB
A (modp)
Ora sostituiamo nelle equazioni precedenti le definizioni di 
 e di 
:
Y
A
 Y
B
KA=(gXB(modp))
XA
(modp) KB=(gXA(modp))
XB
(modp)
KA=gXBXA(modp) KB=gXAXB(modp)
Otteniamo che 
 , che contraddice l
’
ipotesi per assurdo rendendola falsa.
K
A
=
K
B

Crittoanalisi
Eve conosce il numero primo 
 , il generatore 
  e i valori 
pubblici 
  e 
 .
p
=
17
 g
=
6
Y
A
=
3
Y
B
=
15
A partire da questi dati può calcolare la chiave condivisa 
?
K
1
6
2
2
3
12
4
4
5
7
6
8
7
14
8
16
9
11
10
15
11
5
12
13
13
10
14
9
15
3
16
1
i
6imod17
Eve deve calcolare tutte le equazioni 
  finché non trova 
 oppure 
.
g
i
mod
p
 Y
A
 Y
B
A questo punto il logaritmo discreto è invertito poiché viene individuata la 
componente segreta 
 oppure 
.
X
A
 X
B
 può quindi essere facilmente calcolata con la sua equazione.
K


Perché la procedura è sicura?
Perché nelle implementazioni reali si usano numeri di
300
cifre

4Man-in-the-
middle attack

Man-in-the-middle attack
Alice e Bob devono scambiarsi l
’
informazione pubblica.
Eve controlla il canale di comunicazione.


Man-in-the-middle attack
Alice e Bob inviano l
’
informazione, ma Eve le intercetta.


Man-in-the-middle attack
Alice e Bob inviano l
’
informazione, ma Eve le intercetta.


Man-in-the-middle attack
Eve crea delle versioni fraudolente delle informazioni pubbliche di Bob e Alice.


Man-in-the-middle attack
Eve spedisce le versioni fraudolente ingannando entrambi.


Man-in-the-middle attack
Alice e Bob credono di aver condiviso una chiave, ma l
’
hanno in realtà condivisa 
con Eve, che ora sta in mezzo alla conversazione e può intercettare tutto.
B-EB-E A-E A-E
Comunicazione
 Comunicazione
cifrata
 cifrata
Intercettazione
Expectation
Reality


Risolvere il Man-in-the-middle
Canale
Come possiamo verificare che nessuno si sia 
messo in mezzo alla comunicazione
? 
Verifica manuale Certificazione
(tra due lezioni…)

Contromisure: T elegram
@marcofarina


Contromisure: T elegram
@marcofarina
Video call
Secret chats

Contromisure: WhatsApp


Contromisure: WhatsApp


Contromisure: WhatsApp


Contromisure: WhatsApp


Contromisure: WhatsApp


Contromisure: WhatsApp


Contromisure: WhatsApp


Contromisure: WhatsApp


Quindi nel mondo reale si usa DHM?
Te l e g r a m  Vo i c e  C a l l  a u t h e n t i c a t i o n
“Keys for end-to-end encrypted calls are generated using the Diffie-
Hellman key exchange. Users who are on a call can ensure that there is no 
MitM by comparing key visualizations.”
Signal key agreement protocol
“This document describes the "X3DH" (or "Extended T riple Diffie-
Hellman") key agreement protocol. X3DH establishes a shared secret key 
between two parties who mutually authenticate each other based on 
public keys. X3DH provides forward secrecy and cryptographic 
deniability.”


5Crittografia 
end-to-end

Execute 
order 66.
Instant messaging: plain text


Execute 
order 66.
Instant messaging: plain text

Execute 
order 66.
Instant messaging: plain text

Execute 
order 66.
Instant messaging: encryption

Execute 
order 66.
1.
Diffie-Hellman Key Exchange 
DHKE
Instant messaging: encryption

Execute 
order 66.
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
AES Enc
Instant messaging: encryption

Execute 
order 66.
akdslncshlm
mxdksjc
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
AES Enc
Instant messaging: encryption

Execute 
order 66.
akdslncshlm
mxdksjc
AES Enc
Instant messaging: encryption

Execute 
order 66.
akdslncshlm
mxdksjc
Execute 
order 66.
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
mlcch0jod8b
kcnkrhxur
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
mlcch0jod8b
kcnkrhxur
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
mlcch0jod8b
kcnkrhxur
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
1.
Diffie-Hellman Key Exchange
mlcch0jod8b
kcnkrhxur
AES Enc
DHKE
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
dfkjsdnecri2
undn8woue
1.
Diffie-Hellman Key Exchange
2.
AES Encryption
mlcch0jod8b
kcnkrhxur
AES Enc
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
dfkjsdnecri2
undn8woue
mlcch0jod8b
kcnkrhxur
AES Enc
AES Enc
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
dfkjsdnecri2
undn8woue
mlcch0jod8b
kcnkrhxur
AES Enc
AES Enc
Execute 
order 66.
Instant messaging: encryption

Execute 
order 66.
Execute 
order 66.
mlcch0jod8b
kcnkrhxur
AES Enc
AES Enc
Instant messaging: encryption

Execute 
order 66.
Instant messaging: end-to-end encryption

Execute 
order 66.
1.
Diffie-Hellman Key Exchange
Instant messaging: end-to-end encryption

Execute 
order 66.
akdslncshlm
mxdksjc
1.
Diffie-Hellman Key Exchange
2.
AES Encryption
Instant messaging: end-to-end encryption

Execute 
order 66.
akdslncshlm
mxdksjc
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
Instant messaging: end-to-end encryption


Execute 
order 66.
akdslncshlm
mxdksjc
akdslncshlm
mxdksjc
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
Instant messaging: end-to-end encryption


Execute 
order 66.
akdslncshlm
mxdksjc
akdslncshlm
mxdksjc
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
Instant messaging: end-to-end encryption


Execute 
order 66.
akdslncshlm
mxdksjc
akdslncshlm
mxdksjc
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
Instant messaging: end-to-end encryption


Execute 
order 66.
akdslncshlm
mxdksjc
akdslncshlm
mxdksjc
Execute 
order 66.
1.
Diffie-Hellman Key Exchange 
2.
AES Encryption
Instant messaging: end-to-end encryption

