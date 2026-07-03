# 03. Introduzione alla crittografia

**File:** `03. Introduzione alla crittografia.pdf`
**Tipo:** `.pdf`
**Dimensione:** 36103.3 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Introduzione alla crittografia
v 2.7 .2 ~ feb 2026
changelog

Mercoledì 15 Ottobre 1586. È mattina, Mary 
Stuart entra nell’affollata aula di giustizia del 
castello di Fotheringhay . Anni di prigionia e 
l’insorgere di una malattia reumatica hanno 
lasciato il segno, ma la regina è dignitosa, 
composta e incontestabilmente regale. 
Mary , Regina degli scozzesi, è accusata di 
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
stesso, ed Elisabetta ha ancora molti nemici. In terzo 
luogo, l’imputata è sua cugina, un legame abbastanza 
stretto per aumentare la sua titubanza. 

Purtroppo per Mary , Walsingham non è solo il 
segretario di Stato, ma anche, come diremo oggi, il 
capo del controspionaggio. Appena visti i 
messaggi, ha capito chi poteva riuscire a volgerli in 
chiaro: Thomas Phelippes, il miglior decrittatore 
d’Inghilterra.  
Se riuscirà a violare la fatale corrispondenza tra 
Mary e i cospiratori, la morte della regina sarà 
inevitabile. 
Codici & Segreti, Simon Singh
tutta la corrispondenza coi congiurati. Su fogli di 
carta, al posto di parole e frasi ha vergato simboli 
apparentemente privi di signiﬁcato.

1La nascita della 
crittografia

Steganografia
Demarato di Sparta 
(–480)


Steganografia
Demarato di Sparta 
(–480)
Istieo di Mileto 
(–499)


Dalla comunicazione alla crittografia
12345
1
α
β
γ
δ
ε
2
ζ
η
θ
ι
κ
3
λ
µ
ν
ξ
ο
4
π
ρ
σ
τ
υ
5
φ
χ
ψ
ω

Dalla comunicazione alla crittografia
12345
1
α
β
γ
δ
ε
2
ζ
η
θ
ι
κ
3
λ
µ
ν
ξ
ο
4
π
ρ
σ
τ
υ
5
φ
χ
ψ
ω
12345
1
ω
ξ
θ
λ
κ
2
η
α
ο
π
ψ
3
γ
β
τ
υ
χ
4
δ
φ
ρ
µ
ι
5
σ
ν
ε
ζ


Crittografia
Te s t o  i n  
chiaro
Te s t o  
cifrato
Algoritmo di 
cifratura
CIPHERTEXT
PLAINTEXT


Decrittografia
Te s t o  i n  
chiaro
Te s t o  
cifrato
Algoritmo di 
decifratura
PLAINTEXT
CIPHERTEXT


Il Cifrario di Cesare
STUVZABCD
…
…
meet me after the toga party
k=2
OGGV OG CHVGT VJG VQIC RCTVA
Esempio:

Crittoanalisi
Quanto è grande lo spazio delle chiavi?
K⋆=|Σ|=26
Problema:
Conseguenza:
Soluzione?
spazio delle chiavi troppo piccolo.
attacco brute force.
aumentare lo spazio delle chiavi.

Cifratura monoalfabetica
ABCDEFGHIJKLMNOP R TQ S …
ABCDEFGHIJKLMNOP R TQ S …

Cifratura monoalfabetica
ABCDEFGHIJKLMNOP R TQ S …
A BCD EFG H I LMN …P QR T KS JO
La permutazione di 
 costituisce la chiave crittografica.
Σ
Quanto è grande lo spazio delle chiavi?
K⋆=26!≈4⋅1026
n!:=
n
∏k=1
k=1⋅2⋅3⋯⋅n


Crittoanalisi
3%
6%
9%
12%
e a i o n l r t s c d p u m v g h f b q z
Frequenza
the cake is a lie
KOC NDPC AL D BAC
C
D
A
3 volte
2 volte
2 volte
Frequenza
?


Crittoanalisi
the cake is a lie
KOC NDPC AL D BAC
Problema:
Conseguenza:
Soluzione?
dipendenze statistiche nel testo.
attacco statistico.
aumentare entropia testo cifrato.
C
D
A
3 volte
2 volte
2 volte
Frequenza
?

Cifrario polialfabetico
Leon Battista Alberti, 1466


Cifrario polialfabetico
Leon Battista Alberti, 1466
 Giovanni Battista Bellaso, 1553
La forma definitiva del cifrario fu pubblicata da Blaise de 
Vigenère nel 1585 nel libro 
Traicté des Chiffres
 (
Trattato 
sulle scritture segrete
). 
Mary Stuart venne messa sotto accusa nel 1586, ma nelle 
sue comunicazioni non usò il cifrario di Vigenère.


Cifrario di Vigenère
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D 
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E 
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F 
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G 
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H 
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I 
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J 
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K 
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L 
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N 
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O 
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P 
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q 
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R 
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S 
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T 
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V 
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W 
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X 
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
wearediscoveredsaveyourselves
deceptivedeceptivedeceptivede
Password: “
deceptive
”
Messaggio: “
we are discovered, save yourselves
”


Cifrario di Vigenère
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D 
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E 
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F 
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G 
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H 
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I 
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J 
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K 
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L 
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N 
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O 
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P 
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q 
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R 
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S 
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T 
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V 
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W 
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X 
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
w
earediscoveredsaveyourselves
d
eceptivedeceptivedeceptivede
Password: “
deceptive
”
Messaggio: “
we are discovered, save yourselves
”
Z

Cifrario di Vigenère
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D 
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E 
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F 
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G 
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H 
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I 
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J 
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K 
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L 
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N 
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O 
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P 
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q 
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R 
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S 
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T 
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V 
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W 
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X 
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
w
e
arediscoveredsaveyourselves
d
e
ceptivedeceptivedeceptivede
Password: “
deceptive
”
Messaggio: “
we are discovered, save yourselves
”
Z
I

Cifrario di Vigenère
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D 
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E 
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F 
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G 
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H 
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I 
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J 
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K 
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L 
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N 
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O 
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P 
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q 
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R 
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S 
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T 
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V 
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W 
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X 
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
we
a
rediscoveredsaveyourselves
de
c
eptivedeceptivedeceptivede
Password: “
deceptive
”
Messaggio: “
we are discovered, save yourselves
”
ZI
C

Cifrario di Vigenère
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A 
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B 
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C 
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D 
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E 
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F 
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G 
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H 
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I 
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J 
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K 
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L 
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M 
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N 
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O 
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P 
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q 
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R 
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S 
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T 
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U 
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V 
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W 
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X 
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
wearediscoveredsaveyourselves
deceptivedeceptivedeceptivede
Password: “
deceptive
”
Messaggio: “
we are discovered, save yourselves
”
ZICVTWQNGRZGVTWAVZHCQYGLMGZHW
La stessa lettera in punti diversi del messaggio 
viene cifrata con lettere diverse, a seconda della 
corrispondente lettera della password.

Crittoanalisi
wearediscoveredsaveyourselves
deceptivedeceptivedeceptivede
ZICVTWQNGRZGVTWAVZHCQYGLMGZHW
La crittoanalisi completa fu probabilmente effettuata da 
Charles Babbage nel 1854. Non fu mai pubblicata. 
Il metodo di crittoanalisi fu riscoperto in modo indipendente 
da Friedrich Kasiski nel 1863 (T est di Kasiski) e pubblicato nel 
libro 
Die Geheimschriften und die Dechiffrir-Kunst 
(Le 
scritture segrete e l
’
arte di decifrare).
La ripetizione abbassa l
’
entropia ed è quasi sempre un punto di debolezza. A 
partire da questa considerazione si sviluppò un metodo sicuro di crittoanalisi.


Te s t  d i  K a s i s k i
WUMOGIZWYRMHMCESSVLPISCLLGUILEYMV
NGERQLLGAIQGEZKZALQUTKTAZEYHUWRLM
ZWXCHUWRLMSZLBSQWCBMZIXCRFWWYWOQL
ALQATYYZXZGRPQDAVQBZALQBTMJRZLSRB
WOGZUVZEEYJLOYQAEYGTQLKIDMDRMEKLP
RMMAGYXIESEATLKMMTZNVQVZLXUALIJZQ
ZLLRABCMTBQDMRAQESSUXPAGMBTRAVANF
MEKLZVUMCYQUAPAGTQGSSFQDNEGZLAGTQ
TMIFMNMPYIWYGUWEMPMMNMPYIWYXMHKYW
HMRJMMCGQMKSCWUIRGSDVZMKZQTQXMVEC
YZCZKSYCZPIAOYGMEBLLXQCYSSYWYYWOM
Cerchiamo nel crittogramma stringhe che si ripetono.

Te s t  d i  K a s i s k i
WUMOGIZWYRMHMCESSVLPISCLLGUILEYMV
NGERQLLGAIQGEZKZALQUTKTAZEY
 HUWRLM
ZWXC
HUWRLM
SZLBSQWCBMZIXCRFWWYWOQL
ALQATYYZXZGRPQDAVQBZALQBTMJRZLSRB
WOGZUVZEEYJLOYQAEYGTQLKIDMDRMEKLP
RMMAGYXIESEATLKMMTZNVQVZLXUALIJZQ
ZLLRABCMTBQDMRAQESSUXPAGMBTRAVANF
MEKLZVUMCYQUAP
 AGTQ
GSSFQDNEGZL
AGTQ
TMIF
MNMPYI
WYGUWEMPM
MNMPYI
WYXMHKYW
HMRJMMCGQMKSCWUIRGSDVZMKZQTQXMVEC
YZCZKSYCZPIAOYGMEBLLXQCYSSYWYYWOM
Cerchiamo nel crittogramma stringhe che si ripetono.

Te s t  d i  K a s i s k i
WUMOGIZWYRMHMCESSVLPISCLLGUILEYMV
NGERQLLGAIQGEZKZALQUTKTAZEY
 HUWRLM
ZWXC
HUWRLM
SZLBSQWCBMZIXCRFWWYWOQL
ALQATYYZXZGRPQDAVQBZALQBTMJRZLSRB
WOGZUVZEEYJLOYQAEYGTQLKIDMDRMEKLP
RMMAGYXIESEATLKMMTZNVQVZLXUALIJZQ
ZLLRABCMTBQDMRAQESSUXPAGMBTRAVANF
MEKLZVUMCYQUAP
 AGTQ
GSSFQDNEGZL
AGTQ
TMIF
MNMPYI
WYGUWEMPM
MNMPYI
WYXMHKYW
HMRJMMCGQMKSCWUIRGSDVZMKZQTQXMVEC
YZCZKSYCZPIAOYGMEBLLXQCYSSYWYYWOM
1.
chiave di 
1 lettera
 che compie 
10 cicli
 tra le ripetizioni; 
2.
chiave di 
2 lettere
 che compie 
5 cicli
 tra le ripetizioni; 
3.
chiave di 
5 lettere
 che compie 
2 cicli
 tra le ripetizioni; 
4.
chiave di 
10 lettere
 che compie 
1 ciclo
 tra le ripetizioni.
HUWRLM

Te s t  d i  K a s i s k i
WUMOGIZWYRMHMCESSVLPISCLLGUILEYMV
NGERQLLGAIQGEZKZALQUTKTAZEY
 HUWRLM
ZWXC
HUWRLM
SZLBSQWCBMZIXCRFWWYWOQL
ALQATYYZXZGRPQDAVQBZALQBTMJRZLSRB
WOGZUVZEEYJLOYQAEYGTQLKIDMDRMEKLP
RMMAGYXIESEATLKMMTZNVQVZLXUALIJZQ
ZLLRABCMTBQDMRAQESSUXPAGMBTRAVANF
MEKLZVUMCYQUAP
 AGTQ
GSSFQDNEGZL
AGTQ
TMIF
MNMPYI
WYGUWEMPM
MNMPYI
WYXMHKYW
HMRJMMCGQMKSCWUIRGSDVZMKZQTQXMVEC
YZCZKSYCZPIAOYGMEBLLXQCYSSYWYYWOM
Stringa
Distanza
Possibile lunghezza della chiave
2
 3
 4
 5
 6
 7
 8
 9
 10
11
 12
13
14
15
HUWRLM
10
 ✔
 ✔
 ✔
AGTQ
15
 ✔
 ✔
 ✔
MNMPYI 
15
 ✔
 ✔
 ✔

Te s t  d i  K a s i s k i
W
UMOG
I
ZWYR
M
HMCE
S
SVLP
I
SCLL
G
UILE
Y
MV
NG
E
RQLL
G
AIQG
E
ZKZA
L
QUTK
T
AZEY
H
UWRL
M
ZWXC
H
UWRL
M
SZLB
S
QWCB
M
ZIXC
R
FWWY
W
OQL
A
L
QATY
Y
ZXZG
R
PQDA
V
QBZA
L
QBTM
J
RZLS
R
B
WOG
Z
UVZE
E
YJLO
Y
QAEY
G
TQLK
I
DMDR
M
EKLP
R
MMAG
Y
XIES
E
ATLK
M
MTZN
V
QVZL
X
UALI
J
ZQ
ZL
L
RABC
M
TBQD
M
RAQE
S
SUXP
A
GMBT
R
AVAN
F
MEKL
Z
VUMC
Y
QUAP
A
GTQG
S
SFQD
N
EGZL
A
GTQ
T
M
IFMN
M
PYIW
Y
GUWE
M
PMMN
M
PYIW
Y
XMHK
Y
W
HMR
J
MMCG
Q
MKSC
W
UIRG
S
DVZM
K
ZQTQ
X
MVEC
Y
ZCZK
S
YCZP
I
AOYG
M
EBLL
X
QCYS
S
YWYY
W
OM
T utti i multipli della prima lettera della chiave 
 formano un cifrario 
monoalfabetico a sé stante, attaccabile con l
’
analisi statistica.
k
1

Te s t  d i  K a s i s k i
4
8
12
ABCDEFGHIJKLMNOPQRSTUVWXYZ
3
6
9
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Sequenza di 4 lettere poco probabili
A
 E
 I
Possiamo ipotizzare che 
  e dunque che la prima lettera della password sia 
E
.
k
1
=
4
Istogramma lingua italiana
 Istogramma del crittogramma

Te s t  d i  K a s i s k i
W
U
MOG
I
Z
WYR
M
H
MCE
S
S
VLP
I
S
CLL
G
U
ILE
Y
M
V
NG
E
R
QLL
G
A
IQG
E
Z
KZA
L
Q
UTK
T
A
ZEY
H
U
WRL
M
Z
WXC
H
U
WRL
M
S
ZLB
S
Q
WCB
M
Z
IXC
R
F
WWY
W
O
QL
A
L
Q
ATY
Y
Z
XZG
R
P
QDA
V
Q
BZA
L
Q
BTM
J
R
ZLS
R
B
WOG
Z
U
VZE
E
Y
JLO
Y
Q
AEY
G
T
QLK
I
D
MDR
M
E
KLP
R
M
MAG
Y
X
IES
E
A
TLK
M
M
TZN
V
Q
VZL
X
U
ALI
J
Z
Q
ZL
L
R
ABC
M
T
BQD
M
R
AQE
S
S
UXP
A
G
MBT
R
A
VAN
F
M
EKL
Z
V
UMC
Y
Q
UAP
A
G
TQG
S
S
FQD
N
E
GZL
A
G
TQ
T
M
I
FMN
M
P
YIW
Y
G
UWE
M
P
MMN
M
P
YIW
Y
X
MHK
Y
W
HMR
J
M
MCG
Q
M
KSC
W
U
IRG
S
D
VZM
K
Z
QTQ
X
M
VEC
Y
Z
CZK
S
Y
CZP
I
A
OYG
M
E
BLL
X
Q
CYS
S
Y
WYY
W
O
M
I multipli della seconda lettera della chiave 
 formano un secondo cifrario 
monoalfabetico. Il procedimento di analisi è il medesimo del precedente e si 
può facilmente giungere alla conclusione che 
  e dunque che la 
seconda lettera della password è 
M
.
k
2
k
2
=
12

Te s t  d i  K a s i s k i
W
U
M
OG
I
Z
W
YR
M
H
M
CE
S
S
V
LP
I
S
C
LL
G
U
I
LE
Y
M
V
NG
E
R
Q
LL
G
A
I
QG
E
Z
K
ZA
L
Q
U
TK
T
A
Z
EY
H
U
W
RL
M
Z
W
XC
H
U
W
RL
M
S
Z
LB
S
Q
W
CB
M
Z
I
XC
R
F
W
WY
W
O
Q
L
A
L
Q
A
TY
Y
Z
X
ZG
R
P
Q
DA
V
Q
B
ZA
L
Q
B
TM
J
R
Z
LS
R
B
W
OG
Z
U
V
ZE
E
Y
J
LO
Y
Q
A
EY
G
T
Q
LK
I
D
M
DR
M
E
K
LP
R
M
M
AG
Y
X
I
ES
E
A
T
LK
M
M
T
ZN
V
Q
V
ZL
X
U
A
LI
J
Z
Q
ZL
L
R
A
BC
M
T
B
QD
M
R
A
QE
S
S
U
XP
A
G
M
BT
R
A
V
AN
F
M
E
KL
Z
V
U
MC
Y
Q
U
AP
A
G
T
QG
S
S
F
QD
N
E
G
ZL
A
G
T
Q
T
M
I
F
MN
M
P
Y
IW
Y
G
U
WE
M
P
M
MN
M
P
Y
IW
Y
X
M
HK
Y
W
H
MR
J
M
M
CG
Q
M
K
SC
W
U
I
RG
S
D
V
ZM
K
Z
Q
TQ
X
M
V
EC
Y
Z
C
ZK
S
Y
C
ZP
I
A
O
YG
M
E
B
LL
X
Q
C
YS
S
Y
W
YY
W
O
M
Proseguendo l
’
analisi con tutti gli altri gruppi di lettere 
otterremo la password 
EMILY
, che decifra correttamente il 
testo.

Te s t  d i  K a s i s k i
W
U
M
O
G
I
Z
W
Y
R
M
H
M
C
E
S
S
V
L
P
I
S
C
L
L
G
U
I
L
E
Y
M
V
N
G
E
R
Q
L
L
G
A
I
Q
G
E
Z
K
Z
A
L
Q
U
T
K
T
A
Z
E
Y
H
U
W
R
L
M
Z
W
X
C
H
U
W
R
L
M
S
Z
L
B
S
Q
W
C
B
M
Z
I
X
C
R
F
W
W
Y
W
O
Q
L
A
L
Q
A
T
Y
Y
Z
X
Z
G
R
P
Q
D
A
V
Q
B
Z
A
L
Q
B
T
M
J
R
Z
L
S
R
B
W
O
G
Z
U
V
Z
E
E
Y
J
L
O
Y
Q
A
E
Y
G
T
Q
L
K
I
D
M
D
R
M
E
K
L
P
R
M
M
A
G
Y
X
I
E
S
E
A
T
L
K
M
M
T
Z
N
V
Q
V
Z
L
X
U
A
L
I
J
Z
Q
Z
L
L
R
A
B
C
M
T
B
Q
D
M
R
A
Q
E
S
S
U
X
P
A
G
M
B
T
R
A
V
A
N
F
M
E
K
L
Z
V
U
M
C
Y
Q
U
A
P
A
G
T
Q
G
S
S
F
Q
D
N
E
G
Z
L
A
G
T
Q
T
M
I
F
M
N
M
P
Y
I
W
Y
G
U
W
E
M
P
M
M
N
M
P
Y
I
W
Y
X
M
H
K
Y
W
H
M
R
J
M
M
C
G
Q
M
K
S
C
W
U
I
R
G
S
D
V
Z
M
K
Z
Q
T
Q
X
M
V
E
C
Y
Z
C
Z
K
S
Y
C
Z
P
I
A
O
Y
G
M
E
B
L
L
X
Q
C
Y
S
S
Y
W
Y
Y
W
O
M
Proseguendo l
’
analisi con tutti gli altri gruppi di lettere 
otterremo la password 
EMILY
, che decifra correttamente il 
testo.

Te s t  d i  K a s i s k i
W
U
M
O
G
I
Z
W
Y
R
M
H
M
C
E
S
S
V
L
P
I
S
C
L
L
G
U
I
L
E
Y
M
V
N
G
E
R
Q
L
L
G
A
I
Q
G
E
Z
K
Z
A
L
Q
U
T
K
T
A
Z
E
Y
H
U
W
R
L
M
Z
W
X
C
H
U
W
R
L
M
S
Z
L
B
S
Q
W
C
B
M
Z
I
X
C
R
F
W
W
Y
W
O
Q
L
A
L
Q
A
T
Y
Y
Z
X
Z
G
R
P
Q
D
A
V
Q
B
Z
A
L
Q
B
T
M
J
R
Z
L
S
R
B
W
O
G
Z
U
V
Z
E
E
Y
J
L
O
Y
Q
A
E
Y
G
T
Q
L
K
I
D
M
D
R
M
E
K
L
P
R
M
M
A
G
Y
X
I
E
S
E
A
T
L
K
M
M
T
Z
N
V
Q
V
Z
L
X
U
A
L
I
J
Z
Q
Z
L
L
R
A
B
C
M
T
B
Q
D
M
R
A
Q
E
S
S
U
X
P
A
G
M
B
T
R
A
V
A
N
F
M
E
K
L
Z
V
U
M
C
Y
Q
U
A
P
A
G
T
Q
G
S
S
F
Q
D
N
E
G
Z
L
A
G
T
Q
T
M
I
F
M
N
M
P
Y
I
W
Y
G
U
W
E
M
P
M
M
N
M
P
Y
I
W
Y
X
M
H
K
Y
W
H
M
R
J
M
M
C
G
Q
M
K
S
C
W
U
I
R
G
S
D
V
Z
M
K
Z
Q
T
Q
X
M
V
E
C
Y
Z
C
Z
K
S
Y
C
Z
P
I
A
O
Y
G
M
E
B
L
L
X
Q
C
Y
S
S
Y
W
Y
Y
W
O
M
Proseguendo l
’
analisi con tutti gli altri gruppi di lettere 
otterremo la password 
EMILY
, che decifra correttamente il 
testo.

Siedi e non ti vergognare
guancia a guancia, 
ﬁ
anco a 
ﬁ
anco
che m’importa di ogni nome
di ogni grado e ordinamento?
lascia che sia un po’ indiscreto
che ti offra un po’ di vino
gamba questa chiameresti?
scarna è più la tua o la mia?
l’opre non ti salveranno
troppi sono i tuoi peccati
tronchi scabri e rami secchi
vuoti spauracchi, io e te!
colma la ciotola e colma la 
tazza
sveglia, prima che sia giorno
ogni istante un uomo muore
ogni istante un uomo nasce.
 Alfred T ennyson, 
Vision of sin
, 1842

Ottocento: la crittografia militare
1831
1835
T elegrafo
Codice Morse
1854
 Playfair cipher
1855
 Babbage decifra Vigenère
1883
 Principi di Kerckhoffs
1885
 Cifrario Beale
1800
1900
Il sistema deve essere praticamente, se non matematicamente, 
indecifrabile
. 
Il sistema 
non deve essere segreto
, dev’essere in grado di cadere 
nelle mani del nemico senza inconvenienti. 
La sua 
chiave deve essere comunicabile
 senza l’aiuto di note 
scritte, e modi
ﬁ
cabile o modi
ﬁ
cabili a piacimento dei 
corrispondenti. 
Deve essere applicabile alla corrispondenza 
telegra
ﬁ
ca
. 
Deve essere portatile e il suo utilizzo e uso non deve richiedere 
il concorso di più persone. 
È necessario che la sua applicazione sia 
facile da usare
 e che non 
richieda la conoscenza e l'uso di una lunga serie di regole.


2La meccanizzazione 
dei cifrari

Le macchine cifranti
Discret, 1899 
Dr. Friedrich Rehmann, 
Karlsruhe (Germania)
Foto: www.cryptomuseum.com

Novecento: le Guerre Mondiali
SIGABA
Ty p e X
 Enigma
!
 "
#
 Foto: www.cryptomuseum.com


La macchina Enigma


La macchina Enigma


La macchina Enigma


La macchina Enigma


Le chiavi crittografiche di Enigma
Secret Command 
Document
!
Every 
individual 
daily 
key is secret. 
Forbidden to bring 
on aircraft.
Luftwaffe  Machine  
Key  
Nr.649 
Attention!  
Key 
material must not fall 
into enemy hands 
intact. In case of 
danger destroy 

Live demo


Bletchley Park
The only known picture of the gathering known as Captain Ridley
’
s shooting party. 
Photograph: Bletchley Park T rust

Code talkers
Navajo code talkers Henry Bake and George Kirk, December 1943. 
Image: U.S. Marine Corps/National Archives and Records Administration

[
spiegazione
]
[
originale
]
