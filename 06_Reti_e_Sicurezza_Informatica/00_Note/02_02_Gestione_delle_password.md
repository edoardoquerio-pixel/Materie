# 02. Gestione delle password

**File:** `02. Gestione delle password.pdf`
**Tipo:** `.pdf`
**Dimensione:** 28761.6 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Password management
v 3.6.1 ~ feb 2026
changelog

1L’arte 
dell’intrusione

Prevenzione dalle intrusioni
Autenticazione
 CrittografiaAutorizzazione
Controllo degli accessi PASSWORD


Te c n i c h e  d i  i n t r u s i o n e
Default password
Social engineering
Treccani
Attacchi a dizionario
Attacchi a forza bruta
Router, modem, Io T, …
Password profiling, name-
dropping, pretexting, tailgating, 
something for something,…
/usr/share/wordlists
John TheRipper, AirCrack, …


2Attacchi a forza 
bruta
Photo by Pixabay from Pexels

AAAAAAA
RICA TT ARE
J3SIVEK$3
tanta ripetizione = poca entropia
alcune ripetizioni = entropia media
stringa casuale = entropia massima

Cos
’
è una password casuale?
Una password generata casualmente è una stringa di caratteri di 
lunghezza 
 estratti per 
selezione casuale
 da un insieme di simboli 
.
L
 Σ
DEF
Lo 
spazio delle chiavi
 è Il numero di password possibili lunghe 
, ed è 
dato da
L
Quante sono le password di lunghezza ?L
K
=
|
Σ
|
L
Come si misura quanto è robusta una password?
log
a
x
k
= k · log
a
x
log
b
x =
log
k
x
log
k
b
ℍ=log2|Σ|L=Llog2|Σ|=Llog|Σ|
log2
GRANDE GIOVE!
Le sbarrette verticali in questo 
contesto non indicano il valore 
assoluto, ma la 
cardinalità 
dell
’
insieme, ovvero quanti 
elementi contiene l
’
insieme.


Entropia per simbolo (
 )
L
=
1
Set di simboli Cardinalità Entropia
Numeri (0-9) [es: PIN]
 10
 3.332 bit
Esadecimale (0-9, A-F) [es: WEP]
 16
 4 bit
Alfabeto latino (a-z)
 26
 4.7 bit
Alfanumerico (a-z, 0-9)
 36
 5.17 bit
Alfanumerico case sentive (a-z, A-Z, 0-9) 
62
 5.954 bit
ASCII stampabile tranne spazio
 94
 6.555 bit
Codice binario (1 byte)
 256
 8 bit
Si 
pronuncia 
/ˈæski/

Esempio realistico
Supponiamo di generare casualmente (ovvero, ogni simbolo è equiprobabile) 
una password di lunghezza 
  con alfabeto 
 , composto dai 
caratteri ASCII stampabili.
L
=
12
 |
Σ
|
=
94
P
6
zfAm
8
@
o
#
e
4
L
’
entropia della password è calcolata con l
’
equazione
ℍ=log2K=log29412=12log294=12log94
log2=78.655 bit
Sono “buoni” 78 bit di entropia per 
una password?


Robustezza delle password *
molto debole
, potrebbe bastare per tenere lontano il 
vostro gatto. 
debole
, tiene alla larga la maggior parte delle persone, ma 
non Gianpancrazio, l
’
hacker del piano di sopra. Potete 
usarla, al massimo, come password di login del pc. 
ragionevole
, si può usare per la rete e in azienda. 
forte
, potete usarla per proteggere i milioni di euro del 
vostro conto in banca. 
overkill
, manco fossi T ony Stark.
< 28 bit
28-35 bit
36-59 bit
60-127 bit
128+ bit
* Allo stato attuale della potenza computazionale

Te m p i  d i  a t t a c c o
Quando si effettua un attacco brute force, la lunghezza della 
chiave non è nota. 
Si devono testare tutte le combinazioni da una lunghezza minima 
 ad una massima 
.
l
 L
K⋆=|Σ|l+|Σ|l+1+|Σ|l+2+…+|Σ|L
Il tempo di crack 
 è dato da
t t=K⋆⋅1
ν⋅1
N
 è la capacità computazionale 
(numero di chiavi testate al secondo); 
 è il numero di calcolatori usati in 
parallelo.
ν
N
?
?
?
T utte le password 
di lunghezza 
l
T utte le password 
di lunghezza 
L
T utte le password 
di lunghezze 
intermedie

Te m p i  d i  a t t a c c o
L (a-z) (a-z, 0-9)(a-z, A-Z)ASCII
≤ 4
 immediato
immediato
immediato
2 minuti
5
 immediato
2 minuti
 12 minuti
 4 ore
6
 10 minuti
 72 minuti
 10 ore
 18 giorni
7
 4 ore
 43 ore
 23 giorni
 4 anni
8
 4 giorni
 65 giorni
 3 anni
 463 anni
9
 4 mesi
 6 anni
 178 anni 444530 anni
Supponiamo (realisticamente) 
  e 
 . Otteniamo:
N
=
1
ν
=
500
000
“Ma sì, dai, ormai lo sanno tutti che le password devono essere casuali…”
Esponenziale

Password Security Awards
4 - qwerty 
5 - password 
6 - 12345678 
7 - 111111 
8 - 123123 
9 - 1234567890 
10 - 1234567 
11 - qwerty123 
12 - 000000 
13 - 1q2w3e 
14 - aa12345678 
15 - abc123 
16 - password1 
17 - 1234 
18 - qwertyuiop 
19 - 123321 
20 - password123 
21 - 1q2w3e4r5t 
22 - iloveyou 
23 - 654321 
24 - 666666 
25 - 987654321 
26 - 123 
27 - 123456a
1
123456
2
123456789
3
12345
Nordpass (2021) 4TB passwords evaluated.
And the winner is…
SUCHPASSWORD

Password Security Awards
4 - 12345678 
5 - qwerty 
6 - juventus 
7 - 000000 
8 - password 
9 - andrea 
10 - napoli 
11 - francesco 
12 - 111111 
13 - 1234567 
14 - cambiami 
15 - giuseppe 
16 - alessandro 
17 - antonio 
18 - ciaociao 
19 - amoremio 
20 - francesca 
21 - 1234567890 
22 - valentina 
23 - stella 
24 - giovanni 
25 - martina 
26 - 1234 
27 - ciccio
1
123456
2
123456789
3
12345
Nordpass (2021) 4TB passwords evaluated.
Italian Edition
Premio della critica: 
39 - vaff
🍩
🍄
💣
lo

Cosa succede se la 
password non è casuale?
Ricerca euristica


Ricerca euristica
Metodo stupido
AAAAA
AAAA
B
AAA
B
A
AA
B
AA 
… 
ZZZZZ
Metodo furbo
Love
1!
StarWars
12@
P
4$$
w
0
rd
qwerty
#77 
… 
ZZZZZ
I will do it for 
you, Sir.

Ricerca euristica
10%
20%
30%
40%
Simboli
! @ # * . $ & - ? < : , / ) + =
Media
“Aggiungo un 
simbolo
 alla fine così diventa sicura…”


Ricerca euristica
“Aggiungo un 
numero
 alla 
fine così diventa sicura…”


Ricerca euristica
“Aggiungo un 
numero
 alla fine così diventa sicura…”


3Credential 
stuffing

Bene, ma non benissimo
Fonte: Google Security Survey, 2019
riusa la stessa password per 
molti (ma non tutti) gli account
52%
usa password diverse per tutti 
gli account35%
usa la stessa password per 
tutti gli account13%

Bene, ma non benissimo
è, in media, il riuso delle password per un impiegato.
13 volte
delle password viene usata sia per account lavorativi e personali.
50%
Fonte: LastPass, 2018

Bene, ma non benissimo
dei 
data breach
 del 2019 sono dovuti a
 password riutilizzate
.
80%
Fonte: Verizon Data Breach Investigations Report, 2019
FIRST REACTION: SHOCK!

Data breach
Ya h o o, 2 0 1 3
3 miliardi di account
Sony, 2014
100 TB di dati
Anthem, 2015
80 milioni di account
Friend Finder, 2016
412 milioni di account
Equifax, 2017
163 milioni di account
Aadhaar, 2018
FirstAmerican, 2019
Cam4, 2020
1,1 miliardi di account
885 milioni di account
10 miliardi di record
LinkedIn, 2021
700 milioni di account

Epic fail
TVMonde, 2015


Epic fail
TVMonde, 2015
 CBS, 2014


Epic fail
TVMonde, 2015
 CBS, 2014


Matrix è tutto intorno a voi


Password securityfor
dummies
Perché anche la casalinga 
di Voghera possa essere a 
prova di hacker.

E tu quanto ne sai?
Fonte: Google Security Survey, 2019 | US adults, n= 3000
Sa definire 
phishing
 correttamente.60%
Sa definire correttamente 
password 
manager
.55%
Sa definire correttamente 
tutti
 i termini.32%
55%
Sa definire correttamente 
autenticazione multifattore
.

Phishing


Phishing
Spear phishing
Clone phishing
Whaling
mirato ad un individuo o compagnia, alta 
probabilità di successo.
i link di una mail legittima vengono modificati per 
tentare di ingannare il ricevente.
spear phishing
 indirizzato ad alti profili aziendali, 
fanno leva su azioni legali, problemi amministrativi 
o finanziari.
L
’
attaccante cerca di ingannare la vittima convincendola a fornire 
informazioni personali, dati finanziari o codici di accesso, fingendosi 
un ente affidabile in una comunicazione digitale.


Whaling
gophish
Recent Campaigns
Dashboard
Email Sent Email Opened Clicked Link Submitted Data
Gophish è un 
framework open source 
gratuito capace 
di simulare campagne 
di phishing al fine di 
eseguire test di 
sicurezza. 
Phishing: contromisure
Gophish

Phishing
1.
Il lucchetto nel browser non basta: verificate che il sito sia quello 
autentico.
2017 → 3%
2019 → 29%
2020 → 57% 
2.
Visitate direttamente il sito digitando manualmente l
’
indirizzo sul 
browser per verificare l
’
informazione. 
3.
Se siete al computer, potete portare il mouse sopra il link (senza 
cliccare) e vedere il nome del sito in cui andreste a finire se vi cliccaste 
sopra. 
4.
Se si tratta di phishing copiate quel link e segnalatelo alla Polizia Postale 
(
link
). Non è richiesta registrazione. Segnalatelo anche a 
netcraft.com
. 
5.
Cestinate il messaggio.
Whaling


Smishing
“SMS phishing”


Password Manager
Genera
 delle password casuali. 
Si 
ricorda
 le password al posto tuo. 
Compila
 automaticamente i form. 
Segnala
 se le password sono state 
violate.
Perché usare un password manager?

Password manager
Built-in Installazione separata
Low level
Mid level High level

Have I been pwned?
La vostra e-mail è finita in 
un data breach?
1Password Watchtower


Password manager
NON 
CRACCA TE IL 
PASSWORD 
MANAGER!


Autenticazione multifattore
15SEC
Qualcosa che
 Qualcosa che
 Qualcosa che
conosco possiedo sono
Password
 OTP
 Biometria


Autenticazione multifattore
15SEC
conosco possiedo
+
Password
 OTP
La 2FA è la soluzione a tutti i problemi
Biometria

Autenticazione multifattore
15SEC
conosco possiedo
+
Sim swap
Clickjaking
Response 
manipulation
JS file analysis
Missing code integrity 
validation
Refer check bypass
CSFR PoC
Backup code abuse
Bypass 2FA
Password
 OTP
La 2FA non è la soluzione a tutti i problemi


Si salvi chi può…
15SEC
Password
 OTP
 Biometria
Va ricordata
Può essere rubata
Deve essere casuale
 Va inserito a mano
Phishing / SIM swap
Privacy
Hardware

Si salvi il salvabile
15SEC
OTP
 Biometria
Va inserito a mano
Phishing / SIM swap
Privacy
Hardware
Hardware 
security 
module
Qualcosa che
possiedo

Un futuro senza password è possibile
15SEC
Smartphone
 Biometria
Qualcosa che
possiedo
Qualcosa che
sono
+
 = PASSKEYS
???

Passkeys
Standard del W3C che permette 
l'autenticazione senza password 
nei browser, utilizzando chiavi 
crittografiche sicure
(Fast IDentity Online) è un 
insieme di specifiche sviluppate 
dalla FIDO Alliance per 
l
’
autenticazione sicura senza 
password, basato su crittografia a 
chiave pubblica

Passkeys
Riprenderemo le passkey dopo aver 
studiato la crittografia a chiave pubblica

Lato developer
1.
Se possibile, implementare l
’
autenticazione tramite 
passkey 
2.
Altrimenti, implementare l
’
autenticazione a due fattori 
3.
Per quanto possibile prevenire l
’
uso di password deboli 
4.
Non usare la scadenza obbligatoria delle password [
1
] 
5.
Verificare le credenziali continuamente [
2
] 
6.
Non memorizzare MAI le password in chiaro nei 
database! 
7.
Don
’
t panic
.


[spiegazione]
