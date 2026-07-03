# Reti e Sicurezza Informatica — Quaderno di Appunti

> **Materia:** 06_Reti_e_Sicurezza_Informatica
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [01 Introduzione alla cybersecurity](#01-introduzione-alla-cybersecurity)
2. [02 Gestione delle password](#02-gestione-delle-password)
3. [03 Introduzione alla crittografia](#03-introduzione-alla-crittografia)
4. [04 Crittografia DES e AES](#04-crittografia-des-e-aes)
5. [05 Diffie-Hellman key exchange](#05-diffie-hellman-key-exchange)
6. [06 Crittografia a chiave pubblica e RSA](#06-crittografia-a-chiave-pubblica-e-rsa)
7. [07 Certificati digitali e hashing](#07-certificati-digitali-e-hashing)
8. [A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](#a-method-for-obtaining-digital-signatures-and-public-key-cryptosystems)
9. [Approfondimento su DES e AES](#approfondimento-su-des-e-aes)
10. [Appunti di algebra per la crittografia a chiave pubblica RSA](#appunti-di-algebra-per-la-crittografia-a-chiave-pubblica-rsa)
11. [Cifrario di cesare](#cifrario-di-cesare)
12. [Demo entropia](#demo-entropia)
13. [Enigma Keys](#enigma-keys)
14. [Esercizi di subnetting IPv4](#esercizi-di-subnetting-ipv4)
15. [Estratto da  Larte dellinganno  di Kevin Mitnick](#estratto-da--larte-dellinganno--di-kevin-mitnick)
16. [Indirizzamento IPv4](#indirizzamento-ipv4)
17. [InterVLAN Routing](#intervlan-routing)
18. [Lab - Identifying IPv4 Addresses](#lab---identifying-ipv4-addresses)
19. [LAB configure-router-on-a-stick-inter-vlan-routing](#lab-configure-router-on-a-stick-inter-vlan-routing)
20. [Script demo entropia](#script-demo-entropia)
21. [Sistemi Numerici](#sistemi-numerici)
22. [SOL Lab - Identifying IPv4 Addresses](#sol-lab---identifying-ipv4-addresses)
23. [Soluzione esercizio AES](#soluzione-esercizio-aes)
24. [VLAN](#vlan)

---

# 01. Introduzione alla cybersecurity

**File:** `01. Introduzione alla cybersecurity.pdf`
**Tipo:** `.pdf`
**Dimensione:** 23812.8 KB
**Ultima modifica:** 02/07/2026 09:28

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Introduzione alla cybersecurity
v 3.3.5 ~ feb 2025
changelog

Public Service Announcement
Who am I?
Marco Farina, insegno informatica e reti al Maxwell di Nichelino.
Cybersec?
Non lavoro nel campo, ma sono appassionato di 
cybersec 
e 
AI
.
To p i c s ?
Cybersecurity, crittografia, sicurezza web/cloud/database, laboratorio.
Exam?
Sulla teoria, una parte a risposta chiusa, una parte aperta.
Questions?
Meglio una domanda in più adesso che un esame a settembre.
Handout?
Slide a fine lezione, 
appunti
 e 
attenzione
.

1Introduzione alla 
cybersecurity

Cos
’
è la sicurezza?
Valutazione del rischio
Il rischio è la 
probabilità
 che accada un certo 
evento capace di causare un danno. 
È implicata l
’
esistenza di una sorgente di 
pericolo, detta 
minaccia
, e delle possibilità che 
essa si trasformi in un 
danno
.
r=p⋅d
 Il rischio è uguale alla probabilità che si 
verifichi l
’
evento moltiplicata per la gravità del 
danno.


Cos
’
è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello personale Livello aziendale
 Livello nazionale


Cos
’
è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello personale
Dispositivi
Identità
Social
 Lavoro
Sanità
Finanze
Cosa vogliamo proteggere
?

Cos
’
è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello aziendale
Idee e brevetti
 Finanze
 Hardware  
Software
Dipendenti
 Clienti
 Dati
Cosa vogliamo proteggere
?

Cos
’
è la sicurezza informatica?
Protezione dei dati, dei dispositivi e dei sistemi interconnessi.
Livello nazionale
Cyberwarfare
Comunicazione
Segreti
 Intelligence
Energia
Cittadini
Cosa vogliamo proteggere
?

The future of cyberwarfare
Cracking Stuxnet

Cyberwarfare
Uso di arsenali digitali per attaccare una nazione, 
causando danni comparabili alla guerra tradizionale.
Spionaggio internazionale 
Sabotaggio delle infrastrutture 
Propaganda 
Shock economico
Entry level
estremamente 
basso
Danni
potenzialmente 
devastanti


Cyberwarfare
Impatto
Plausibilità
Cyber-attacks
Eventi climatici 
estremi
avg
avg
The Global risk landscape, 2019 
World Economic Forum
Pandemia
Inflazione


La triade C.I.A.
100%
Confidentiality Integrity Availability
Confidenzialità
 Integrità
 Disponibilità
Indipendentemente dal livello, la triade C.I.A. è il concetto fondamentale.


Confidenzialità
È la proprietà che indica che le informazioni non sono 
rese disponibili o divulgate a individui, entità o processi 
non autorizzati.
Il concetto non è strettamente sinonimo di privacy, ma 
un 
componente della privacy
 implementato per 
proteggere i dati da visualizzazioni non autorizzate.


Integrità
Assicura che la completezza e l
’
accuratezza dei dati 
venga mantenuta durante il loro intero ciclo di vita.
Il concetto non è strettamente sinonimo di integrità 
referenziale dei database, anche se può essere vista 
come un caso speciale di consistenza.
La crittografia è lo strumento più utilizzato perché 
assieme all
’
integrità fornisce anche la confidenzialità.


Disponibilità
Affinché i sistemi informativi assolvano la propria 
funzione, le informazioni devono essere disponibili 
quando richieste.
I sistemi di memorizzazione e calcolo, i controlli di 
sicurezza e i canali di comunicazione devono essere 
sempre funzionanti.
100%
Uno dei più grandi sforzi è compiuto nel prevenire gli 
attacchi di tipo 
Denial of Service
.


2Attacks & 
attackers

Meet Alice, Bob & Eve
Alice
il mittente
Bob
il destinatario
Eve
l
’
attaccante


Tipologie di attacchi
Attivi
Mascheramento 
(
spoofing
)
Ripetizione 
(
replay
)
Modifica
 Denial of Service
Ripudio
Il sistema o le risorse 
vengono alterate 
dall
’
attaccante.


Tipologie di attacchi
Passivi
Lettura dei messaggi
Analisi e statistiche
Il sistema o le risorse 
non
 sono alterate 
dall
’
attaccante.


Cyber attackers
“Script kiddies”
Abilità limitate 
Uso di tool professionali 
Danni potenzialmente devastanti 
T racce spesso non coperte
Mafiaboy (2000): 15 anni, denial of 
service causa 1,7
$
 miliardi di danni.


White hat
Classe
Legale buono
Allineamento
Usa le sue abilità per scopi leciti e legali. 
Conduce 
penetration-test
 per scoprire vulnerabilità delle reti o 
dei sistemi informatici. 
Agisce con autorizzazione scritta, sotto contratto e nei limiti 
definiti dall
’
azienda committente. 
Al termine dell
’
attività stila un report per aiutare l
’
azienda a 
risolvere i problemi di sicurezza.
Comunemente conosciuto come 
hacker etico, è uno dei lavori più 
ricercati negli ultimi anni.
Cyber attackers

Gray hat
Classe
Caotico buono
Allineamento
Compiono atti illegali, ma non per scopo di lucro. 
Sono spesso guidati dalla curiosità e dal mettere alla prova le 
proprie abilità di hacking. 
Le vulnerabilità vengono scoperte illegalmente o con metodi non 
etici. 
Risolvono le vulnerabilità scoperte sotto compenso oppure 
divulgano le informazioni nel web senza venderle.
Spinto dalla curiosità si aggira 
nel meandri del web alla ricerca 
di vulnerabilità zero-day.
Cyber attackers

Black hat
Classe
Caotico malvagio
Allineamento
È un attaccante malintenzionato con intenti criminali. Lavora per 
causare un danno, o per prelevare informazioni private e 
confidenziali, con o senza vantaggio personale (profitto 
economico o politico). 
Mantiene segrete vulnerabilità ed exploit per sfruttarli 
attivamente. 
Può vendere i propri servizi sul dark web.
Il dark web è l
’
habitat naturale in 
cui mietono vittime senza pietà.
Cyber attackers

Cyber attackers
Organized hackers
Organizzazioni criminali
 Hacktivist
 State-sponsored


3Vulnerabilità e 
malware

Vulnerabilità
È un punto debole del sistema in cui le misure di sicurezza 
sono assenti, ridotte o compromesse. 
DEF
Una qualunque vulnerabilità non nota agli sviluppatori. 
Costituiscono una grave minaccia alla sicurezza.
Un attacco che sfrutta una vulnerabilità per eseguire un 
rootkit o per creare comportamenti imprevisti nel sistema.
Zero Day
Exploit
Un metodo alternativo all
’
autenticazione per superare le 
difese informatiche di un sistema.Backdoor
Rootkit
 Un software malevolo in grado di mascherare la propria 
presenza ideato per abilitare l
’
accesso ad un sistema.


Vulnerabilità
È un punto debole del sistema in cui le misure di sicurezza 
sono assenti, ridotte o compromesse. 
DEF
tempo
esiste
scoperta da 
attaccante
(zero day)
Rischio potenziale
scoperta da 
azienda
nota al 
pubblico aggiornamento
Rischio elevato
Rischio estremo

Vulnerabilità
Software Hardware Protocolli
Buffer overflow 
Injection 
Broken authentication 
Broken access control 
Security misconfiguration 
…
Spectre & Meltdown 
Rowhammer 
Directory trasversal 
Secure Enclave 
…
Procedure di sicurezza 
Controllo degli accessi 
Componenti obsoleti 
Sicurezza fisica 
…

Malware
Virus Trojan Worm Ransomware
Spyware Keylogger
 Scareware / 
RoguewareBotnet


Le vulnerabilità sono ovunque. 
Un attaccante si appiglierà a 
qualunque cosa.

Cosa sta succedendo secondo voi?

Thermal attacks


Thermal attacks
0 secondi
 30 secondi
 60 secondi


Keystroke attack



---

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


---

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


---

# 04. Crittografia DES e AES

**File:** `04. Crittografia DES e AES.pdf`
**Tipo:** `.pdf`
**Dimensione:** 18312.9 KB
**Ultima modifica:** 02/07/2026 09:25

---

Intervento realizzato da
Docente
Unità formativa
Argomento
Prof. Marco Farina
Sicurezza Informatica
Crittografia DES e AES
v 3.1.4 ~ feb 2026
changelog

Novecento: dalle lettere ai numeri
1943
1949
Bletchley Park
Communication Theory of Secrecy 
Systems
1969
 ARPANET
1976
 DES
1977
 Crittografia a chiave pubblica
1994
 SSL
1900
2000
1989
 World Wide Web


1Data Encryption 
Standard

DES
Input (64 bit)
Initial 
permutation
Left half (32)
Right half (32) Cipher 
function
⊕
Cipher 
function
⊕
Cipher 
function
⊕
Final 
permutation
Output (64 bit)
Key (64 bit)
Key 
permutation
L half (28)
R half (28)
L shift
L shift
Permutation
L shift
L shift
Permutation
L shift
L shift
Permutation
Subkey #1 (48)
Subkey #2 (48)
Subkey #16 (48)
Round 1
 Round 2
 Round 16

Crittoanalisi
Quanto è grande lo spazio delle chiavi?
K⋆=|Σ|L=256≈7,2⋅1016
Deep Crack
Chi
: 
distributed.net
 & EFF
Anno
: 1999
CPU
: 1536
Performance
: 92 miliardi di chiavi al secondo
Te m p o
: 22 ore e 15 minuti
Costo
: 200.000 
$

Crittoanalisi
Quanto è grande lo spazio delle chiavi?
K⋆=|Σ|L=256≈7,2⋅1016
Problema:
Conseguenza:
Soluzione?
spazio delle chiavi troppo piccolo.
attacco brute force.
…cifriamo TRE volte. (sigh
!
)


2Advanced 
Encryption Standard

Costruzione di AES
1997
Il NIST emette il 
bando per la 
costruzione di 
AES
Richieste tre caratteristiche: 
Sicurezza (chiave da 128+ bit) 
Efficienza computazionale 
Semplicità di implementazione
1999
L
’
algoritmo scelto è stato sviluppato da due crittografi belgi, Joan Daemen e Vincent 
Rijmen, che lo hanno presentato con il nome di 
Rijndael
, derivato dai loro nomi. 
Rijndael
, in fiammingo, si pronuncia [
ˈ
r
ɛ
inda
ː
l] (“rèin-daal”).

Input
328831e0
435a3137
f6309807
a88da234
2b28ab09
7eaef7cf
15d2154f
16a6883c
State
 Cipher Key
32
= 0011 0010 (1 byte)
Notazione esadecimale (esempio):
Questo è un blocco di 128 
bit preso dal messaggio in 
chiaro che deve essere 
cifrato.

Input
328831e0
435a3137
f6309807
a88da234
2b28ab09
7eaef7cf
15d2154f
16a6883c
State
 Cipher Key
al processo di 
cifratura
all’espansione 
della chiave

Processo di cifratura
Il procedimento di cifratura del blocco plaintext avviene usando 4 
differenti trasformazioni nel 
round iniziale
, nei 
9 round principali
 e nel 
round finale
.
In particolare vengono usate quattro fasi, una di permutazione e tre di 
sostituzione:
๏
Substitute bytes
: usa una 
S-Box
 per svolgere una sostituzione del 
blocco byte per byte.
๏
Shift rows
: una semplice permutazione.
๏
Mix columns
: una sostituzione che utilizza l
’
aritmetica sui campi di 
Galois 
GF(2
8
)
.
๏
Add round key
: una semplice operazione di XOR bit-a-bit del blocco 
corrente con una porzione della chiave espansa.

Processo di cifratura
State
AddRoundKey
SubBytes
ShiftRows
MixColumns
AddRoundKey
SubBytes
ShiftRows
AddRoundKey
Initial 
round
9/11/13 
main  
rounds
ﬁ
nal 
round
Cipher 
key
Round 
key 1-9
Round 
key 10

Le trasformazioni di AES
SubBytes
ShiftRows
MixColumns
AddRoundKey
Vediamo ora le quattro trasformazioni di AES. Per ogni 
trasformazione vedremo come funziona intuitivamente 
l
’
algoritmo di crittografia ed infine come avviene la 
trasformazione della chiave.

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19
La trasformazione 
Substitute byte
 è una semplice ricerca su una 
tabella. AES definisce una matrice di dimensione 16x16 chiamata 
S-Box
 che contiene una permutazione di tutti i 256 valori a 8 bit.

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
19D4

SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
D4


SubBytes
a09ae9
3df4c6f8
e3e28d48
be2b2a08
D4e0b81e
27bfb441
11985d52
aef1e530


ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
27

ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
Shift su 1 byte27

ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
27
Shift su 2 byte

ShiftRows
D4e0b81e
bfb441
11985d52
aef1e530
27
Shift su 3 byte

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30aef1e5

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30
aef1e5
02
03
01
01
01
02
03
01
01
01
02
03
03
01
01
02
×
Questa trasformazione opera su una singola colonna. 
Ciascun byte di una colonna viene mappato in un 
nuovo valore che è una funzione dei quattro byte 
presenti nella colonna. La trasformazione può essere 
definita dalla moltiplicazione in figura.

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30
aef1e5
02
03
01
01
01
02
03
01
01
01
02
03
03
01
01
02
×
Nello standard la trasformazione viene definita considerando 
ciascuna colonna come un polinomio di quattro termini con 
coefficienti nel campo finito 
GF(2
8
)
. Ciascuna colonna viene 
moltiplicata modulo (
x
4
+1) per il polinomio fisso 
a
(
x
) dato da:
=
04
66
81
e5
a ( x )=3 x
3
+ x
2
+ x +2

MixColumns
e0b81e
b44127
521198
D4
bf
5d
30
aef1e5
02
03
01
01
01
02
03
01
01
01
02
03
03
01
01
02
×
Nello standard la trasformazione viene definita considerando 
ciascuna colonna come un polinomio di quattro termini con 
coefficienti nel campo finito 
GF(2
8
)
. Ciascuna colonna viene 
moltiplicata modulo (
x
4
+1) per il polinomio fisso 
a
(
x
) dato da:
=04
66
81
e5
a ( x )=3 x
3
+ x
2
+ x +2

MixColumns
e0b81e
b44127
521198
aef1e5
04
66
81
e5

MixColumns
e0b81e
b44127
521198
aef1e5
04
66
81
e5
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c

AddRoundKey
04
66
81
e5
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a0
fa
fe
17
88
54
2c
b1
23
a3
39
39
2a
6c
76
05
Round key
Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey
04
66
81
e5
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a0
fa
fe
17
Round key
⊕
a4
9c
7f
f2
=
88
54
2c
b1
23
a3
39
39
2a
6c
76
05
Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
Round key
a4
9c
7f
f2
88
54
2c
b1
23
a3
39
39
2a
6c
76
05
Prodotta nel primo 
passo di generazione 
delle chiavi

AddRoundKey
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a4
9c
7f
f2

AddRoundKey
e0
cb
19
9a
48
f8
d3
7a
28
06
26
4c
a4
9c
7f
f2
68
9f
35
2b
6b
5b
ea
43
02
6a
50
49

Rounds
I passi visti fin ora vengono applicati alla parola in input altre 9 
volte. Il round finale non include la trasformazione MixColumns.
Nel nostro esempio, il plaintext produce il seguente ciphertext:
39
02
dc
19
25
dc
11
6a
84
09
85
0b
1d
fb
97
32
328831e0
435a3137
f6309807
a88da234

Key schedule
La chiave di cifratura subisce un procedimento di 
espansione
 per 
generare 11 
chiavi parziali
, usate nel
’
initial round
, nei 9 
main round 
e nel 
final round
.
…
Cipher key
La chiave espansa può essere vista come un array di parole di 32 
bit, numerate da 0 a 43. La prima colonna è riempita con la chiave 
crittografica.
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
1.
applicare le trasformazioni 
RotWord
 e 
SubBytes
 alla 
precedente parola 
w
i-1
w
i

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
1.
applicare le trasformazioni 
RotWord
 e 
SubBytes
 alla 
precedente parola 
w
i-1
w
i
w
i-1
cf
4f
3c
09
RotWord

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
w
i
w
i-1
8a
84
eb
01
SubByte 
con S-Box

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
2.
Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima w
i-4
 più una 
costante 
Rcon
w
i
w
i-1
8a
84
eb
01
SubByte 
con S-Box

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
2.
Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima w
i-4
 più una 
costante 
Rcon
w
i
w
i-1
w
i-4
8a
84
eb
01
SubByte 
con S-Box
2b
7e
15
16
⊕

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
Le parole in posizione 
multiplo di 4 (
w
4
, 
w
8
, …, 
w
40
) 
vengono calcolate:
2.
Si somma (XOR) il risultato 
con la parola di 4 posizioni 
prima w
i-4
 più una 
costante 
Rcon
w
i
w
i-1
w
i-4
8a
84
eb
01
SubByte 
con S-Box
2b
7e
15
16
⊕
 ⊕
01
00
00
00
=
a0
fa
fe
17

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
a0
fa
fe
17
Cipher key
Round key 1

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
…
a0
fa
fe
17
Cipher key
Round key 1

Key schedule
2b
28
ab
09
7e
ae
f7
cf
15
d2
15
4f
16
a6
88
3c
a0
88
23
2a
fa
54
a3
6c
fe
2c
39
76
17
b1
39
05
f2
7a
59
73
c2
96
35
59
95
b9
80
f6
f2
43
7a
7f
d0
c9
e1
b6
14
ee
3f
63
f9
25
0c
0c
a8
89
c8
a6
…
Cipher key
Round key 1
Round key 2
 Round key 10
Riassumendo, il procedimento di 
key schedule
 è: 
๏
l’input è una parola di 32 bit e un numero di iterazione 
i
. L’output è 
una parola di 32 bit; 
๏
la parola in input viene copiata nell’output; 
๏
si applica la funzione 
Rotate
 de
ﬁ
nita precedentemente per ruotare 
l’output di otto bit verso sinistra; 
๏
si applica la 
S-box di R
ĳ
ndael
 su tutti e quattro i singoli byte della 
parola di output; 
๏
solo sul primo byte della parola di output, si applica l’or esclusivo tra 
il byte e 
Rcon(
i
)
.

Sicurezza di AES
AES per garantire la sua sicurezza effettua:
๏
10 round per la chiave a 128 bit,
๏
12 round per la chiave a 192 bit,
๏
14 round per la chiave a 256 bit.
I migliori attacchi sono riusciti a forzare l’AES con:
๏
7 round e chiave di 128 bit,
๏
8 round e chiave di 192 bit,
๏
9 round e chiave di 256 bit.
Attualmente, secondo i documenti segreti trafugati da 
Edward Snowden, l’NSA sta facendo ricerche per capire se 
un attacco basato sulla 
statistica tau
 possa aiutare a 
rompere AES.
 Non chiedetemi cosa 
essa sia, non lo so. 
!

Prestazioni
AES funziona su una grande varietà di dispositivi: dalle 
smart card a 8 bit 
ﬁ
no ai super-computer.
Attualmente, sui processori Intel Core i3/i5/i7, AMD APU e le 
cpu che supportano il set di istruzioni AES-NI, la cifratura 
AES arriva ad avere un throughput di 
700 MB/s per thread
.
AESDELIVERY
700 MB/s!

Learn by doing
La libreria openssl fornisce un’implementazione sicura 
dei principali cifrari. È bene provare a familiarizzare 
con alcuni dei comandi possibili.
Manuale eBook gratuito: 
https://www.feistyduck.com/books/
openssl-cookbook/
Approfondimento ed esercizi: 
https://rainbow-bits.notion.site/
openssl-aes-salt



---

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



---

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


---

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



---

# A Method for Obtaining Digital Signatures and Public-Key Cryptosystems

**File:** `A Method for Obtaining Digital Signatures and Public-Key Cryptosystems.pdf`
**Tipo:** `.pdf`
**Dimensione:** 177.8 KB
**Ultima modifica:** 02/07/2026 09:24

---

A Method for Obtaining Digital
Signatures and Public-Key Cryptosystems
R.L. Rivest, A. Shamir, and L. Adleman∗
Abstract
An encryption method is presented with the novel property that publicly re-
vealing an encryption key does not thereby reveal the corresponding decryption
key. This has two important consequences:
1. Couriers or other secure means are not needed to transmit keys, since a
message can be enciphered using an encryption key publicly revealed by
the intended recipient. Only he can decipher the message, since only he
knows the corresponding decryption key.
2. A message can be “signed” using a privately held decryption key. Anyone
can verify this signature using the corresponding publicly revealed en-
cryption key. Signatures cannot be forged, and a signer cannot later deny
the validity of his signature. This has obvious applications in “electronic
mail” and “electronic funds transfer” systems.
A message is encrypted by representing it as a number M, raising M to a
publicly speciﬁed power e, and then taking the remainder when the result is
divided by the publicly speciﬁed product, n, of two large secret prime numbers
p and q. Decryption is similar; only a diﬀerent, secret, power d is used, where
e·d≡ 1 (mod ( p− 1)· (q− 1)). The security of the system rests in part on
the diﬃculty of factoring the published divisor, n.
Key Words and Phrases : digital signatures, public-key cryptosystems, pri-
vacy, authentication, security, factorization, prime number, electronic mail,
message-passing, electronic funds transfer, cryptography.
CR Categories: 2.12, 3.15, 3.50, 3.81, 5.25
∗General permission to make fair use in teaching or research of all or part of this material is
granted to individual readers and to nonproﬁt libraries acting for them provided that ACM’s copy-
right notice is given and that reference is made to the publication, to its date of issue, and to the fact
that reprinting privileges were granted by permission of the Association for Computing Machinery.
To otherwise reprint a ﬁgure, table, other substantial excerpt, or the entire work requires speciﬁc
permission as does republication, or systematic or multiple reproduction.
This research was supported by National Science Foundation grant MCS76-14294, and the Oﬃce of
Naval Research grant number N00014-67-A-0204-0063.
Author’s Address: Laboratory for Computer Science, Massachusetts Institute of Technology, Cam-
bridge, MA 02139 E-mail addresses: rivest@theory.lcs.mit.edu

I Introduction
The era of “electronic mail” [10] may soon be upon us; we must ensure that two
important properties of the current “paper mail” system are preserved: (a) messages
are private, and (b) messages can be signed. We demonstrate in this paper how to
build these capabilities into an electronic mail system.
At the heart of our proposal is a new encryption method. This method provides
an implementation of a “public-key cryptosystem,” an elegant concept invented by
Diﬃe and Hellman [1]. Their article motivated our research, since they presented
the concept but not any practical implementation of such a system. Readers familiar
with [1] may wish to skip directly to Section V for a description of our method.
II Public-Key Cryptosystems
In a “public key cryptosystem” each user places in a public ﬁle an encryption proce-
dureE. That is, the public ﬁle is a directory giving the encryption procedure of each
user. The user keeps secret the details of his corresponding decryption procedure D.
These procedures have the following four properties:
(a) Deciphering the enciphered form of a message M yields M. Formally,
D(E(M) =M. (1)
(b) Both E and D are easy to compute.
(c) By publicly revealing E the user does not reveal an easy way to compute D.
This means that in practice only he can decrypt messages encrypted with E, or
compute D eﬃciently.
(d) If a message M is ﬁrst deciphered and then enciphered, M is the result. For-
mally,
E(D(M) =M. (2)
An encryption (or decryption) procedure typically consists of a general method
and an encryption key . The general method, under control of the key, enciphers a
message M to obtain the enciphered form of the message, called the ciphertext C .
Everyone can use the same general method; the security of a given procedure will rest
on the security of the key. Revealing an encryption algorithm then means revealing
the key.
When the user revealsE he reveals a very ineﬃcient method of computing D(C):
testing all possible messages M until one such that E(M) =C is found. If property
(c) is satisﬁed the number of such messages to test will be so large that this approach
is impractical.
A functionE satisfying (a)-(c) is a “trap-door one-way function;” if it also satisﬁes
(d) it is a “trap-door one-way permutation.” Diﬃe and Hellman [1] introduced the
2

concept of trap-door one-way functions but did not present any examples. These
functions are called “one-way” because they are easy to compute in one direction but
(apparently) very diﬃcult to compute in the other direction. They are called “trap-
door” functions since the inverse functions are in fact easy to compute once certain
private “trap-door” information is known. A trap-door one-way function which also
satisﬁes (d) must be a permutation: every message is the cipertext for some other
message and every ciphertext is itself a permissible message. (The mapping is “one-
to-one” and “onto”). Property (d) is needed only to implement “signatures.”
The reader is encouraged to read Diﬃe and Hellman’s excellent article [1] for
further background, for elaboration of the concept of a public-key cryptosystem, and
for a discussion of other problems in the area of cryptography. The ways in which
a public-key cryptosystem can ensure privacy and enable “signatures” (described in
Sections III and IV below) are also due to Diﬃe and Hellman.
For our scenarios we suppose that A and B (also known as Alice and Bob) are
two users of a public-key cryptosystem. We will distinguish their encryption and
decryption procedures with subscripts: EA,DA,EB,DB.
III Privacy
Encryption is the standard means of rendering a communication private. The sender
enciphers each message before transmitting it to the receiver. The receiver (but no
unauthorized person) knows the appropriate deciphering function to apply to the
received message to obtain the original message. An eavesdropper who hears the
transmitted message hears only “garbage” (the ciphertext) which makes no sense to
him since he does not know how to decrypt it.
The large volume of personal and sensitive information currently held in comput-
erized data banks and transmitted over telephone lines makes encryption increasingly
important. In recognition of the fact that eﬃcient, high-quality encryption techniques
are very much needed but are in short supply, the National Bureau of Standards has
recently adopted a “Data Encryption Standard” [13, 14], developed at IBM. The new
standard does not have property (c), needed to implement a public-key cryptosystem.
All classical encryption methods (including the NBS standard) suﬀer from the
“key distribution problem.” The problem is that before a private communication can
begin, another private transaction is necessary to distribute corresponding encryption
and decryption keys to the sender and receiver, respectively. Typically a private
courier is used to carry a key from the sender to the receiver. Such a practice is not
feasible if an electronic mail system is to be rapid and inexpensive. A public-key
cryptosystem needs no private couriers; the keys can be distributed over the insecure
communications channel.
How can Bob send a private message M to Alice in a public-key cryptosystem?
First, he retrievesEA from the public ﬁle. Then he sends her the enciphered message
EA(M). Alice deciphers the message by computing DA(EA(M)) = M. By property
(c) of the public-key cryptosystem only she can decipher EA(M). She can encipher a
3

private response with EB, also available in the public ﬁle.
Observe that no private transactions between Alice and Bob are needed to estab-
lish private communication. The only “setup” required is that each user who wishes
to receive private communications must place his enciphering algorithm in the public
ﬁle.
Two users can also establish private communication over an insecure communi-
cations channel without consulting a public ﬁle. Each user sends his encryption key
to the other. Afterwards all messages are enciphered with the encryption key of the
recipient, as in the public-key system. An intruder listening in on the channel cannot
decipher any messages, since it is not possible to derive the decryption keys from the
encryption keys. (We assume that the intruder cannot modify or insert messages into
the channel.) Ralph Merkle has developed another solution [5] to this problem.
A public-key cryptosystem can be used to “bootstrap” into a standard encryption
scheme such as the NBS method. Once secure communications have been established,
the ﬁrst message transmitted can be a key to use in the NBS scheme to encode all
following messages. This may be desirable if encryption with our method is slower
than with the standard scheme. (The NBS scheme is probably somewhat faster if
special-purpose hardware encryption devices are used; our scheme may be faster on
a general-purpose computer since multiprecision arithmetic operations are simpler to
implement than complicated bit manipulations.)
IV Signatures
If electronic mail systems are to replace the existing paper mail system for business
transactions, “signing” an electronic message must be possible. The recipient of a
signed message has proof that the message originated from the sender. This quality
is stronger than mere authentication (where the recipient can verify that the message
came from the sender); the recipient can convince a “judge” that the signer sent the
message. To do so, he must convince the judge that he did not forge the signed
message himself! In an authentication problem the recipient does not worry about
this possibility, since he only wants to satisfy himself that the message came from the
sender.
An electronic signature must be message-dependent, as well as signer-dependent.
Otherwise the recipient could modify the message before showing the message-signature
pair to a judge. Or he could attach the signature to any message whatsoever, since
it is impossible to detect electronic “cutting and pasting.”
To implement signatures the public-key cryptosystem must be implemented with
trap-door one-way permutations (i.e. have property (d)), since the decryption algo-
rithm will be applied to unenciphered messages.
How can user Bob send Alice a “signed” messageM in a public-key cryptosystem?
He ﬁrst computes his “signature” S for the message M using DB:
S =DB(M) .
4

(Deciphering an unenciphered message “makes sense” by property (d) of a public-
key cryptosystem: each message is the ciphertext for some other message.) He then
encryptsS usingEA (for privacy), and sends the result EA(S) to Alice. He need not
send M as well; it can be computed from S.
Alice ﬁrst decrypts the ciphertext with DA to obtain S. She knows who is the
presumed sender of the signature (in this case, Bob); this can be given if necessary in
plain text attached toS. She then extracts the message with the encryption procedure
of the sender, in this case EB (available on the public ﬁle):
M =EB(S) .
She now possesses a message-signature pair ( M,S ) with properties similar to those
of a signed paper document.
Bob cannot later deny having sent Alice this message, since no one else could have
createdS =DB(M). Alice can convince a “judge” that EB(S) =M, so she has proof
that Bob signed the document.
Clearly Alice cannot modify M to a diﬀerent version M′, since then she would
have to create the corresponding signature S′ =DB(M′) as well.
Therefore Alice has received a message “signed” by Bob, which she can “prove”
that he sent, but which she cannot modify. (Nor can she forge his signature for any
other message.)
An electronic checking system could be based on a signature system such as the
above. It is easy to imagine an encryption device in your home terminal allowing
you to sign checks that get sent by electronic mail to the payee. It would only be
necessary to include a unique check number in each check so that even if the payee
copies the check the bank will only honor the ﬁrst version it sees.
Another possibility arises if encryption devices can be made fast enough: it will
be possible to have a telephone conversation in which every word spoken is signed by
the encryption device before transmission.
When encryption is used for signatures as above, it is important that the en-
cryption device not be “wired in” between the terminal (or computer) and the com-
munications channel, since a message may have to be successively enciphered with
several keys. It is perhaps more natural to view the encryption device as a “hardware
subroutine” that can be executed as needed.
We have assumed above that each user can always access the public ﬁle reliably.
In a “computer network” this might be diﬃcult; an “intruder” might forge messages
purporting to be from the public ﬁle. The user would like to be sure that he actually
obtains the encryption procedure of his desired correspondent and not, say, the en-
cryption procedure of the intruder. This danger disappears if the public ﬁle “signs”
each message it sends to a user. The user can check the signature with the public ﬁle’s
encryption algorithm EPF . The problem of “looking up” EPF itself in the public ﬁle
is avoided by giving each user a description ofEPF when he ﬁrst shows up (in person)
to join the public-key cryptosystem and to deposit his public encryption procedure.
He then stores this description rather than ever looking it up again. The need for a
5

courier between every pair of users has thus been replaced by the requirement for a
single secure meeting between each user and the public ﬁle manager when the user
joins the system. Another solution is to give each user, when he signs up, a book
(like a telephone directory) containing all the encryption keys of users in the system.
V Our Encryption and Decryption Methods
To encrypt a message M with our method, using a public encryption key ( e,n ),
proceed as follows. (Here e and n are a pair of positive integers.)
First, represent the message as an integer between 0 and n− 1. (Break a long
message into a series of blocks, and represent each block as such an integer.) Use any
standard representation. The purpose here is not to encrypt the message but only to
get it into the numeric form necessary for encryption.
Then, encrypt the message by raising it to the eth power modulo n. That is, the
result (the ciphertext C) is the remainder when Me is divided by n.
To decrypt the ciphertext, raise it to another power d, again modulo n. The
encryption and decryption algorithms E and D are thus:
C ≡ E(M)≡Me (mod n), for a message M .
D(C)≡Cd (mod n), for a ciphertext C .
Note that encryption does not increase the size of a message; both the message
and the ciphertext are integers in the range 0 to n− 1.
The encryption key is thus the pair of positive integers ( e,n ). Similarly, the
decryption key is the pair of positive integers ( d,n ). Each user makes his encryption
key public, and keeps the corresponding decryption key private. (These integers
should properly be subscripted as in nA,eA, and dA, since each user has his own set.
However, we will only consider a typical set, and will omit the subscripts.)
How should you choose your encryption and decryption keys, if you want to use
our method?
You ﬁrst compute n as the product of two primes p and q:
n =p·q .
These primes are very large, “random” primes. Although you will make n public,
the factors p andq will be eﬀectively hidden from everyone else due to the enormous
diﬃculty of factoring n. This also hides the way d can be derived from e.
You then pick the integerd to be a large, random integer which is relatively prime
to (p− 1)· (q− 1). That is, check that d satisﬁes:
gcd(d, (p− 1)· (q− 1)) = 1
(“gcd” means “greatest common divisor”).
6

The integere is ﬁnally computed fromp,q , andd to be the “multiplicative inverse”
of d, modulo (p− 1)· (q− 1). Thus we have
e·d≡ 1 (mod ( p− 1)· (q− 1)).
We prove in the next section that this guarantees that (1) and (2) hold, i.e. thatE
andD are inverse permutations. Section VII shows how each of the above operations
can be done eﬃciently.
The aforementioned method should not be confused with the “exponentiation”
technique presented by Diﬃe and Hellman [1] to solve the key distribution problem.
Their technique permits two users to determine a key in common to be used in a
normal cryptographic system. It is not based on a trap-door one-way permutation.
Pohlig and Hellman [8] study a scheme related to ours, where exponentiation is done
modulo a prime number.
VI The Underlying Mathematics
We demonstrate the correctness of the deciphering algorithm using an identity due
to Euler and Fermat [7]: for any integer (message) M which is relatively prime to n,
Mφ(n)≡ 1 (mod n) . (3)
Hereφ(n) is the Euler totient function giving number of positive integers less than n
which are relatively prime to n. For prime numbers p,
φ(p) =p− 1 .
In our case, we have by elementary properties of the totient function [7]:
φ(n) = φ(p)·φ(q)
= ( p− 1)· (q− 1) (4)
= n− (p +q) + 1.
Since d is relatively prime to φ(n), it has a multiplicative inverse e in the ring of
integers modulo φ(n):
e·d≡ 1 (mod φ(n)). (5)
We now prove that equations (1) and (2) hold (that is, that deciphering works
correctly if e and d are chosen as above). Now
D(E(M)) ≡ (E(M))d≡ (Me)d (mod n) =Me·d (mod n)
E(D(M)) ≡ (D(M))e≡ (Md)e (mod n) =Me·d (mod n)
and
Me·d≡Mk·φ(n)+1 (mod n) (for some integer k).
7

From (3) we see that for all M such that p does not divide M
Mp−1≡ 1 (mod p)
and since (p− 1) divides φ(n)
Mk·φ(n)+1≡M (mod p).
This is trivially true when M≡ 0 (mod p), so that this equality actually holds for
all M. Arguing similarly for q yields
Mk·φ(n)+1≡M (mod q) .
Together these last two equations imply that for all M,
Me·d≡Mk·φ(n)+1≡M (mod n).
This implies (1) and (2) for all M, 0≤ M < n. Therefore E and D are inverse
permutations. (We thank Rich Schroeppel for suggesting the above improved version
of the authors’ previous proof.)
VII Algorithms
To show that our method is practical, we describe an eﬃcient algorithm for each
required operation.
A How to Encrypt and Decrypt Eﬃciently
Computing Me (mod n) requires at most 2 · log2(e) multiplications and 2 · log2(e)
divisions using the following procedure (decryption can be performed similarly using
d instead of e):
Step 1. Let ekek−1...e1e0 be the binary representation of e.
Step 2. Set the variable C to 1.
Step 3. Repeat steps 3a and 3b for i =k,k− 1,..., 0:
Step 3a. Set C to the remainder of C2 when divided by n.
Step 3b. If ei = 1, then set C to the remainder of C·M when divided by n.
Step 4. Halt. Now C is the encrypted form of M.
This procedure is called “exponentiation by repeated squaring and multiplication.”
This procedure is half as good as the best; more eﬃcient procedures are known.
Knuth [3] studies this problem in detail.
The fact that the enciphering and deciphering are identical leads to a simple
implementation. (The whole operation can be implemented on a few special-purpose
integrated circuit chips.)
A high-speed computer can encrypt a 200-digit message M in a few seconds;
special-purpose hardware would be much faster. The encryption time per block in-
creases no faster than the cube of the number of digits in n.
8

B How to Find Large Prime Numbers
Each user must (privately) choose two large random numbers p and q to create his
own encryption and decryption keys. These numbers must be large so that it is not
computationally feasible for anyone to factor n = p·q. (Remember that n, but not
p or q, will be in the public ﬁle.) We recommend using 100-digit (decimal) prime
numbersp and q, so that n has 200 digits.
To ﬁnd a 100-digit “random” prime number, generate (odd) 100-digit random
numbers until a prime number is found. By the prime number theorem [7], about
(ln 10100)/2 = 115 numbers will be tested before a prime is found.
To test a large number b for primality we recommend the elegant “probabilistic”
algorithm due to Solovay and Strassen [12]. It picks a random number a from a
uniform distribution on{1,...,b − 1}, and tests whether
gcd(a,b ) = 1 and J(a,b ) =a(b−1)/2 (mod b), (6)
where J(a,b ) is the Jacobi symbol [7]. If b is prime (6) is always true. If b is com-
posite (6) will be false with probability at least 1 /2. If (6) holds for 100 randomly
chosen values of a then b is almost certainly prime; there is a (negligible) chance of
one in 2 100 that b is composite. Even if a composite were accidentally used in our
system, the receiver would probably detect this by noticing that decryption didn’t
work correctly. When b is odd, a≤ b, and gcd(a,b ) = 1, the Jacobi symbol J(a,b )
has a value in{−1, 1} and can be eﬃciently computed by the program:
J(a,b ) =if a = 1 then 1 else
if a is even then J(a/2,b )· (−1)(b2−1)/8
else J(b (mod a),a )· (−1)(a−1)·(b−1)/4
(The computations of J(a,b ) and gcd(a,b ) can be nicely combined, too.) Note that
this algorithm does not test a number for primality by trying to factor it. Other
eﬃcient procedures for testing a large number for primality are given in [6,9,11].
To gain additional protection against sophisticated factoring algorithms, p and q
should diﬀer in length by a few digits, both ( p− 1) and (q− 1) should contain large
prime factors, and gcd( p− 1,q− 1) should be small. The latter condition is easily
checked.
To ﬁnd a prime number p such that (p− 1) has a large prime factor, generate a
large random prime number u, then let p be the ﬁrst prime in the sequence i·u + 1,
for i = 2, 4, 6,.... (This shouldn’t take too long.) Additional security is provided by
ensuring that (u− 1) also has a large prime factor.
A high-speed computer can determine in several seconds whether a 100-digit num-
ber is prime, and can ﬁnd the ﬁrst prime after a given point in a minute or two.
Another approach to ﬁnding large prime numbers is to take a number of known
factorization, add one to it, and test the result for primality. If a prime p is found
9

it is possible to prove that it really is prime by using the factorization of p− 1. We
omit a discussion of this since the probabilistic method is adequate.
C How to Choose d
It is very easy to choose a number d which is relatively prime to φ(n). For example,
any prime number greater than max( p,q ) will do. It is important that d should be
chosen from a large enough set so that a cryptanalyst cannot ﬁnd it by direct search.
D How to Compute e from d and φ(n)
To compute e, use the following variation of Euclid’s algorithm for computing the
greatest common divisor of φ(n) and d. (See exercise 4.5.2.15 in [3].) Calculate
gcd(φ(n),d ) by computing a seriesx0,x 1,x 2,... , wherex0≡φ(n),x 1 =d, andxi+1≡
xi−1 (mod xi), until an xk equal to 0 is found. Then gcd( x0,x 1) = xk−1. Compute
for each xi numbers ai and bi such that xi = ai·x0 +bi·x1. If xk−1 = 1 then bk−1
is the multiplicative inverse of x1 (mod x0). Since k will be less than 2 log 2(n), this
computation is very rapid.
If e turns out to be less than log 2(n), start over by choosing another value of d.
This guarantees that every encrypted message (except M = 0 or M = 1) undergoes
some “wrap-around” (reduction modulo n) .
VIII A Small Example
Consider the case p = 47,q = 59,n = p·q = 47· 59 = 2773, and d = 157. Then
φ(2773) = 46· 58 = 2668, and e can be computed as follows:
x0 = 2668, a0 = 1, b0 = 0,
x1 = 157, a1 = 0, b1 = 1,
x2 = 156, a2 = 1, b2 =−16 (since 2668 = 157· 16 + 156) ,
x3 = 1, a3 =−1, b3 = 17 (since 157 = 1· 156 + 1) .
Therefore e = 17, the multiplicative inverse (mod 2668) of d = 157.
Withn = 2773 we can encode two letters per block, substituting a two-digit num-
ber for each letter: blank = 00, A = 01, B = 02, . . . , Z = 26. Thus the message
ITS ALL GREEK TO ME
(Julius Caesar, I, ii, 288, paraphrased) is encoded:
0920 1900 0112 1200 0718 0505 1100 2015 0013 0500
Since e = 10001 in binary, the ﬁrst block (M = 920) is enciphered:
M 17 = (((((1)2·M)2)2)2)2·M = 948 (mod 2773) .
10

The whole message is enciphered as:
0948 2342 1084 1444 2663 2390 0778 0774 0219 1655 .
The reader can check that deciphering works: 948 157≡ 920 (mod 2773), etc.
IX Security of the Method: Cryptanalytic Ap-
proaches
Since no techniques exist to prove that an encryption scheme is secure, the only test
available is to see whether anyone can think of a way to break it. The NBS standard
was “certiﬁed” this way; seventeen man-years at IBM were spent fruitlessly trying to
break that scheme. Once a method has successfully resisted such a concerted attack it
may for practical purposes be considered secure. (Actually there is some controversy
concerning the security of the NBS method [2].)
We show in the next sections that all the obvious approaches for breaking our
system are at least as diﬃcult as factoring n. While factoring large numbers is not
provably diﬃcult, it is a well-known problem that has been worked on for the last three
hundred years by many famous mathematicians. Fermat (1601?-1665) and Legendre
(1752-1833) developed factoring algorithms; some of today’s more eﬃcient algorithms
are based on the work of Legendre. As we shall see in the next section, however, no
one has yet found an algorithm which can factor a 200-digit number in a reasonable
amount of time. We conclude that our system has already been partially “certiﬁed”
by these previous eﬀorts to ﬁnd eﬃcient factoring algorithms.
In the following sections we consider ways a cryptanalyst might try to determine
the secret decryption key from the publicly revealed encryption key. We do not
consider ways of protecting the decryption key from theft; the usual physical security
methods should suﬃce. (For example, the encryption device could be a separate
device which could also be used to generate the encryption and decryption keys, such
that the decryption key is never printed out (even for its owner) but only used to
decrypt messages. The device could erase the decryption key if it was tampered with.)
A Factoring n
Factoringn would enable an enemy cryptanalyst to “break” our method. The factors
of n enable him to compute φ(n) and thus d. Fortunately, factoring a number seems
to be much more diﬃcult than determining whether it is prime or composite.
A large number of factoring algorithms exist. Knuth [3, Section 4.5.4] gives an
excellent presentation of many of them. Pollard [9] presents an algorithm which
factors a number n in time O(n1/4).
The fastest factoring algorithm known to the authors is due to Richard Schroeppel
(unpublished); it can factor n in approximately
exp
√
ln(n)·ln(ln(n)) = n
√
ln ln(n)/ ln(n)
11

= (ln( n))
√
ln(n)/ ln(ln(n))
steps (here ln denotes the natural logarithm function). Table 1 gives the number of
operations needed to factor n with Schroeppel’s method, and the time required if
each operation uses one microsecond, for various lengths of the number n (in decimal
digits).
Table 1
Digits Number of operations Time
50 1 .4× 1010 3.9 hours
75 9 .0× 1012 104 days
100 2 .3× 1015 74 years
200 1 .2× 1023 3.8× 109 years
300 1 .5× 1029 4.9× 1015 years
500 1 .3× 1039 4.2× 1025 years
We recommend that n be about 200 digits long. Longer or shorter lengths can
be used depending on the relative importance of encryption speed and security in
the application at hand. An 80-digit n provides moderate security against an attack
using current technology; using 200 digits provides a margin of safety against future
developments. This ﬂexibility to choose a key-length (and thus a level of security) to
suit a particular application is a feature not found in many of the previous encryption
schemes (such as the NBS scheme).
B Computing φ(n) Without Factoring n
If a cryptanalyst could computeφ(n) then he could break the system by computing d
as the multiplicative inverse ofe moduloφ(n) (using the procedure of Section VII D).
We argue that this approach is no easier than factoring n since it enables the
cryptanalyst to easily factor n using φ(n). This approach to factoring n has not
turned out to be practical.
How can n be factored using φ(n)? First, (p +q) is obtained from n and φ(n) =
n− (p +q) + 1. Then (p−q) is the square root of (p +q)2− 4n. Finally, q is half the
diﬀerence of (p +q) and (p−q).
Therefore breaking our system by computing φ(n) is no easier than breaking our
system by factoring n. (This is why n must be composite; φ(n) is trivial to compute
if n is prime.)
C Determining d Without Factoring n or Computing φ(n).
Of course, d should be chosen from a large enough set so that a direct search for it is
unfeasible.
12

We argue that computing d is no easier for a cryptanalyst than factoring n, since
once d is known n could be factored easily. This approach to factoring has also not
turned out to be fruitful.
A knowledge ofd enablesn to be factored as follows. Once a cryptanalyst knowsd
he can calculate e·d− 1, which is a multiple of φ(n). Miller [6] has shown that n can
be factored using any multiple of φ(n). Therefore if n is large a cryptanalyst should
not be able to determine d any easier than he can factor n.
A cryptanalyst may hope to ﬁnd a d′ which is equivalent to thed secretly held by
a user of the public-key cryptosystem. If such values d′ were common then a brute-
force search could break the system. However, all such d′ diﬀer by the least common
multiple of (p− 1) and (q− 1), and ﬁnding one enables n to be factored. (In (3) and
(5), φ(n) can be replaced by lcm( p− 1,q− 1).) Finding any such d′ is therefore as
diﬃcult as factoring n.
D Computing D in Some Other Way
Although this problem of “computing e-th roots modulo n without factoring n” is
not a well-known diﬃcult problem like factoring, we feel reasonably conﬁdent that it
is computationally intractable. It may be possible to prove that any general method
of breaking our scheme yields an eﬃcient factoring algorithm. This would establish
that any way of breaking our scheme must be as diﬃcult as factoring. We have not
been able to prove this conjecture, however.
Our method should be certiﬁed by having the above conjecture of intractability
withstand a concerted attempt to disprove it. The reader is challenged to ﬁnd a way
to “break” our method.
X Avoiding “Reblocking” When Encrypting A Signed
Message
A signed message may have to be “reblocked” for encryption since the signaturen may
be larger than the encryption n (every user has his own n). This can be avoided as
follows. A threshold valueh is chosen (sayh = 10199) for the public-key cryptosystem.
Every user maintains two public (e,n ) pairs, one for enciphering and one for signature-
veriﬁcation, where every signaturen is less thanh, and every encipheringn is greater
thanh. Reblocking to encipher a signed message is then unnecessary; the message is
blocked according to the transmitter’s signature n.
Another solution uses a technique given in [4]. Each user has a single ( e,n ) pair
wheren is between h and 2h, where h is a threshold as above. A message is encoded
as a number less than h and enciphered as before, except that if the ciphertext is
greater than h, it is repeatedly re-enciphered until it is less than h. Similarly for
decryption the ciphertext is repeatedly deciphered to obtain a value less than h. If n
is near h re-enciphering will be infrequent. (Inﬁnite looping is not possible, since at
worst a message is enciphered as itself.)
13

XI Conclusions
We have proposed a method for implementing a public-key cryptosystem whose se-
curity rests in part on the diﬃculty of factoring large numbers. If the security of our
method proves to be adequate, it permits secure communications to be established
without the use of couriers to carry keys, and it also permits one to “sign” digitized
documents.
The security of this system needs to be examined in more detail. In particular,
the diﬃculty of factoring large numbers should be examined very closely. The reader
is urged to ﬁnd a way to “break” the system. Once the method has withstood all
attacks for a suﬃcient length of time it may be used with a reasonable amount of
conﬁdence.
Our encryption function is the only candidate for a “trap-door one-way permuta-
tion” known to the authors. It might be desirable to ﬁnd other examples, to provide
alternative implementations should the security of our system turn out someday to be
inadequate. There are surely also many new applications to be discovered for these
functions.
Acknowledgments. We thank Martin Hellman, Richard Schroeppel, Abraham
Lempel, and Roger Needham for helpful discussions, and Wendy Glasser for her
assistance in preparing the initial manuscript. Xerox PARC provided support and
some marvelous text-editing facilities for preparing the ﬁnal manuscript.
Received April 4, 1977; revised September 1, 1977.
References
1. Diﬃe, W., and Hellman, M. New directions in cryptography. IEEE Trans. Inform.
Theory IT-22, (Nov. 1976), 644-654.
2. Diﬃe, W., and Hellman, M. Exhaustive cryptanalysis of the NBS data encryption
standard. Computer 10 (June 1977), 74-84.
3. Knuth, D. E. The Art of Computer Programming, Vol 2: Seminumerical Algo-
rithms. Addison-Wesley, Reading, Mass., 1969.
4. Levine, J., and Brawley, J.V. Some cryptographic applications of permutation
polynomials. Cryptologia 1 (Jan. 1977), 76-92.
5. Merkle, R. Secure communications over an insecure channel. Submitted to Comm.
ACM.
6. Miller, G.L. Riemann’s hypothesis and tests for primality. Proc. Seventh Annual
ACM Symp. on the Theory of Comptng. Albuquerque, New Mex., May 1975, pp.
234-239; extended vers. available as Res. Rep. CS-75-27, Dept. of Comptr. Sci., U. of
Waterloo, Waterloo, Ont., Canada, Oct. 1975.
7. Niven, I., and Zuckerman, H.S. An Introduction to the Theory of Numbers. Wiley,
New York, 1972.
8. Pohlig, S.C., and Hellman, M.E. An improved algorithm for computing logarithms
over GF (p) and its cryptographic signiﬁcance. To appear in IEEE Trans. Inform.
Theory, 1978.
14

9. Pollard, J.M. Theorems on factorization and primality testing. Proc. Camb. Phil.
Soc. 76 (1974), 521-528.
10. Potter, R.J., Electronic mail. Science 195, 4283 (March 1977), 1160-1164.
11. Rabin, M.O., Probabilistic algorithms. In Algorithms and Complexity , J. F.
Traub, Ed., Academic Press, New York, 1976, pp. 21-40.
12. Solovay, R., and Strassen, V. A Fast Monte-Carlo test for primality. SIAM J.
Comptng. (March 1977), 84-85.
13. Federal Register, Vol. 40, No. 52, March 17, 1975.
14. Federal Register, Vol. 40, No. 149, August 1, 1975.
15


---

# Approfondimento su DES e AES

**File:** `Approfondimento su DES e AES.pdf`
**Tipo:** `.pdf`
**Dimensione:** 211.1 KB
**Ultima modifica:** 02/07/2026 09:25

---

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


1.RotWord effettua uno shift a sinistra di un byte. Questo signiﬁca che 
[B0,B1,B2,B3] diventa [B1,B2,B3,B0]; 
2.SubWord effettua una sostituzione usando la S-Box dell’algoritmo 
principale; 
3.Il risultato viene messo in XOR con una costante, chiamata 
Rcon[j] (che in realtà è un vettore, per cui la costante cambia ad 
ogni round–capire come funziona e perché va oltre gli scopi del 
nostro corso e ha sempre a che fare con i campi di Galois). 
Nella ﬁgura c’è uno schema di questi passaggi, chiamati “function g”. 



---

# Appunti di algebra per la crittografia a chiave pubblica RSA

**File:** `Appunti di algebra per la crittografia a chiave pubblica RSA.pdf`
**Tipo:** `.pdf`
**Dimensione:** 284.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

ITS ICT Piemonte
Corso di Sicurezza Informatica
Appunti di Algebra
per la crittograﬁa a chiave
pubblica RSA.
Prof. Marco Farina
marco.farina@its-ictpiemonte.it
Ultima revisione: 18 gennaio 2017.

Indice
1 Insiemi di numeri 2
1.1 Introduzione . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Naturali, interi, razionali . . . . . . . . . . . . . . . . . . . . . 2
2 L’algoritmo di Euclide 3
3 I numeri primi 5
4 Relazioni di congruenza 6
5 Il teorema di Euler-Fermat 7
6 I sistemi di crittograﬁa 11
7 L’algoritmo RSA 13
Il presente testo ` e tratto alle lezioni del prof. Alberto Albano presso il
Dipartimento di Informatica dell’Universit` a di Torino.
Questo testo ` e stato scritto usando LATEX, sistema originariamente sviluppato da
Leslie Lamport, basato su TEX creato da Donald Knuth.

1 Insiemi di numeri ITS ICT Piemonte
1 Insiemi di numeri
1.1 Introduzione
I numeri sono cos` ı pervasivi del nostro mondo che se ne comincia a fare
conoscenza nei primi anni di vita e se ne continua a fare un uso via via pi` u
approfondito nella vita quotidiana e nel percorso scolastico ﬁno alle scuole
superiori. Resta tuttavia indispensabile per gli studenti che hanno deciso
di intraprendere studi di carattere scientiﬁco o tecnico ritornarci di nuovo
nei corsi che utilizzano concetti matematici di base. L’esigenza nasce dalla
necessit` a di fare alcuni chiarimenti su alcuni aspetti delicati e profondi dei
numeri, che giocano poi un ruolo fondamentale in tutta quanta la matemati-
ca in generale e la crittologia in particolare. Non si tratta tanto di questioni
fondazionali sul concetto di numero, che in questa sede non verranno aﬀron-
tate, quanto di questioni concrete da tenere ben presenti da chiunque voglia
utilizzare lo strumento matematico con perizia e sicurezza.
1.2 Naturali, interi, razionali
I primi numeri che si incontrano sono gli interi positivi, detti anche
numeri naturali: 1 , 2, 3,... . L’insieme dei numeri naturali si indica con
il simbolo N. Sono i numeri che servono a contare e che hanno fatto la
prima comparsa nelle societ` a umane svariate migliaia di anni fa. Per fare
misure di quantit` a ﬁsiche come lunghezze, aree, tempi, temperature, ecc.,
` e tuttavia necessario poter disporre di sottoparti dell’unit` a e considerare
quindi numeri frazionari m/n dovem,n∈ N con n̸= 0. `E poi conveniente
anche introdurre i numeri con il segno per poter trattare grandezze negative
come possono essere la temperatura, la velocit` a e molte altre grandezze
ﬁsiche. Si ottengono cos` ı i seguenti insiemi numerici:
Z =
{
0,±1,±2,...
}
numeri interi relativi,
Q =
{m
n |m,n∈ Z, n̸= 0
}
numeri razionali.
Si hanno le evidenti inclusioni N⊆ Z⊆ Q. Talvolta ` e anche utile considerare
gli insiemi
Z+ =
{
m∈ Z|m≥ 0
}
numeri interi non negativi,
Q+ =
{
q∈ Q|q≥ 0
}
numeri razionali non negativi.
pagina 2

2 L’algoritmo di Euclide ITS ICT Piemonte
2 L’algoritmo di Euclide
Da bambini abbiamo imparato che quando si divide 27 per 6 il quoziente
` e 4 ed ilresto ` e 3, cio` e che
27 = 6· 4 + 3.
La cosa importante da notare ` e che il resto deve essere un intero maggiore
o uguale a 0 e minore in senso stretto di 6. Anche se ` e vero che, ad esempio
27 = 6· 3 + 9,
si prende come resto 3 e non 9 perch´ e 3 ` e il pi` u piccolo intero positivo per
cui vale l’identit` a.
La propriet` a fondamentale di cui ci stiamo occupando si pu` o enunciare
in modo preciso con il seguente teorema.
Teorema 2.1 (della divisione). Se a≥ 0 e b > 0 sono interi, esistono e
sono univocamente determinati gli interi q≥ 0 ed r tali che
a =bq +r e 0≤r<b.
q ed r sono detti rispettivamente il quoziente e il resto della divisione.
La determinazione del quoziente e del resto si pu` o fare utilizzando l’al-
goritmo della divisione che abbiamo imparato nella scuola elementare. Ad
esempio, si provi ad applicare l’algoritmo per ottenere quoziente e resto della
divisione di 2731 diviso 43.
Deﬁnizione 2.1. Dati due interi a e b diciamo che b ` e undivisore di a,
e scriviamo b|a se, dividendo a per b si ottiene resto 0, cio` e se a = qb.
Equivalentemente si dice che b divide a, oppure che a ` e divisibile perb,
oppure ancora che a ` e unmultiplo di b.
Deﬁnizione 2.2. Dati due interi a e b, il numero positivo d tale che
1. d|a e d|b,
2. se c|a e c|b allora c|d
` e detto ilmassimo comun divisore di a e b e denotato con
d = (a,b ).
pagina 3

2 L’algoritmo di Euclide ITS ICT Piemonte
La condizione 1 dice ched ` e un divisore comune dia eb, e la condizione 2
dice che ogni divisore comune dia eb ` e anche un divisore did. Per esempio,
6 ` e un divisore comune di 60 ed 84, ma non ` e il massimo comun divisore,
dato che 12| 60 e 12| 84, ma 12 ∤ 6 (il simbolo ∤ signiﬁca “non divide”).
Deﬁnizione 2.3. Due numeri a,b sono detti coprimi se (a,b ) = 1.
Esiste un famoso metodo per calcolare il massimo comun divisore di due
interi, basato sull’uso del quoziente e del resto.
Teorema 2.2 (Algoritmo di Euclide) . Il massimo comun divisore di due
interi a, b si ottiene con il metodo delle divisioni successive seguenti:
a =bq +r0
b =r0q0 +r1
r0 =r1q1 +r2
...
rn−2 =rn−1qn−1 +rn
rn−1 =rnqn + 0
Poich´ e i restiri, con 0≤ i≤ n, sono positivi e decrescenti, dopo un
numero ﬁnito di passi la divisione d` a resto0. L’ultimo resto non nullo rn ` e
il massimo comun divisore di a,b .
Se gi` a il primo resto ` e uguale a zero,b divide a e quindi (a,b ) =b.
Esempio. Determinare il massimo comun divisore di 1776 e 1492.
Soluzione. Si ha:
(1776, 1492) = (1492, 284), essendo 1776 = 1· 1492 + 284
(1492, 284) = (284, 72), essendo 1492 = 5· 284 + 72
(284, 72) = (72, 68), essendo 284 = 3· 72 + 68
(72, 68) = (68, 4), essendo 72 = 1· 68 + 4
(68, 4) = 4, essendo 68 = 17· 4.
Teorema 2.3 (Identit` a di Bezout). Se d = (a,b ) ` e il massimo comun
divisore di a e b, allora esistono due interi m edn tali che
d =ma +nb.
ma +nb ` e detta unacombinazione lineare di a e b con coeﬃcientim ed
n.
pagina 4

3 I numeri primi ITS ICT Piemonte
3 I numeri primi
Un concetto di fondamentale importanza nella storia e nella pratica della
matematica ` e quello dinumero primo. Un numero intero p si dice primo
se
• p̸= 0, 1,−1;
• per ogni a∈ Z se a divide p allora a∈{ 1,−1,p,−p}.
In altre parole, un intero ` e un primo se ` e diverso da 0, 1,-1, e non ha
divisori propri.
Il Lemma seguente descrive un’importante propriet` a dei numeri primi.
Lemma 3.1. Siano a,b,p ∈ Z conp primo:
se p|ab allora p|a o p|b.
Dimostrazione. supponiamo che p|ab. Se p|a la dimostrazione ` e banale;
assumiamo quindi anche chep ∤a. Allora (a,p ) = 1, quindi esistonox,y∈ Z
tali che xa +yp = 1, da cui si ottiene
b = 1· b =xab +ypb;
poich´ ep|ab, segue che p divide b.
Dimostriamo ora il cosiddetto Teorema Fondamentale dell’Aritmetica.
Teorema 3.1. Siaz∈ Z un intero diverso da 0,1,-1. Allora esistono numeri
primi p1,p 2,...,p n tali che
z =p1·p2·p3·... ·pn.
Inoltre tale fattorizzazione ` e unica a meno del segno dei numeri primi e del
loro ordine nel prodotto.
Dimostrazione. (esistenza) Supponiamo prima z > 0 (quindi z ≥ 2) e
applichiamo il principio di induzione nella seconda forma.
Se z = 2 allora la dimostrazione ` e banale. Supponiamo ora che z≥ 3
e che, per ipotesi induttiva, una fattorizzazione in prodotto di primi esista
per ogni 2≤k≤z− 1.
Sez ` e primo, allora ` e gi` a fattorizzato (con un solo fattore). Supponiamo
quindi chez non sia primo. Allora z ha almeno un divisore propriok; quindi
pagina 5

4 Relazioni di congruenza ITS ICT Piemonte
z =kb con 2≤k,b≤z−1. Ma, per ipotesi induttiva, k eb sono un prodotto
di numeri primi, e quindi anche z ` e tale.
Sia oraz <0; allora−z >0 e quindi, per quanto appena visto,−z =p1·
p2·p3·...·pn, conp1·p2·...·pn numeri primi; quindiz = (−p1)·p2·p3·...·pn.
La prova di esistenza ` e completata.
Dimostrazione. (unicit` a) Supponiamo chep1,p 2,...,p n eq1,q 2,...,q s siano
primi tali che
p1·p2...p n =z =q1·q2...q s.
Allora p1|z = q1·q2...q s, quindi per l’osservazione che segue il Lemma
precedente, p1 divide almeno uno dei qi A meno di riordinare q1·q2...q s
possiamo supporre che p1|q1, ma allora, essendo primi, p1 = q1 oppure
p1 =−q1.
Dividendo ora z per p1 si ottiene dunque
p2·p3... pn = z
p1
=±q2·q3...q s.
Procedendo in questo modo alla ﬁne si ricava n =s, ed anche l’unicit` a dei
primi nelle due fattorizzazioni, a meno dell’ordine e dei segni.
Teorema 3.2 (di Euclide). Esistono inﬁniti numeri primi positivi.
Dimostrazione. Supponiamo per assurdo che l’insieme dei numeri primi po-
sitivi sia ﬁnito, e siano allora p1,p 2,...,p t tutti i numeri primi positivi
distinti. Consideriamo il numero intero
N =p1·p2·p3...p t + 1.
Allora N≥ 2 e c’` e un fattore primoq di N. Essendo primo, q deve essere
uno dei pi; ma allora q|p1· p2...p t e quindi q divide N−p1· p2...p t = 1,
che ` e assurdo.
4 Relazioni di congruenza
Deﬁnizione 4.1. Fissato un interon, (n≥ 2), due interia,b∈ Z sono detti
congruenti modulo n se n|b−a. In questo caso si scrive
a≡b (mod n).
Teorema 4.1. Due interi sono congruenti modulo n se e solo se divisi per
n danno lo stesso resto.
pagina 6

5 Il teorema di Euler-Fermat ITS ICT Piemonte
Dimostrazione. Consideriamo gli interi a e b. Dividendoli per n, otteniamo
a =q1n +r1, b =q2n +r2, con 0 ≤r1,r 2,<n.
Se r1 =r2, allora (b−a) = (q2−q1)n, cio` ea e b sono congruenti modulo n
Viceversa, se a≡b (mod n), allora b−a =kn, da cui
b =a +kn =q1n +r1 +kn = (q1 +k)n +r1.
Dal Teorema della Divisione il resto ` e univocamente determinato e quindi,
confrontandob =q2n +r2 e b = (q1 +k)n +r1, si ha che r1 =r2.
Il teorema precedente assicura che si pu` o scegliere come rappresentante
di ogni classe il resto della divisione pern. Possiamo allora usare la notazione
seguente:
Zn ={0, 1, 2,..., n− 1},
essendo 0, 1, 2,...,n − 1 i possibili resti della divisione di un numero per n.
Esempio. Dato n = 3, Z3 ` e formato dalle 3 classi di congruenza seguenti:
0 ={..., −6,−3, 0, 3, 6, 9,... },
1 ={..., −5,−2, 1, 4, 7, 10,... },
2 ={..., −4,−1, 2, 5, 8, 11,... }.
`E possibile deﬁnire delle operazioni di somma e prodotto in Zn.
5 Il teorema di Euler-Fermat
In questa sezione vedremo una sorprendente applicazione della teoria
delle congruenze. Nel 1736 Euler diede una dimostrazione di una aﬀerma-
zione di Fermat (1601-1665) che riguardava la relazione fra le potenze di un
numero e le sue classi di congruenza modulo un numero primo. Euler riusc` ı
anche a dimostrare una generalizzazione di questa aﬀermazione, valida per
ogni numero intero n, e non solo per i numeri primi. Ed ` e proprio usan-
do questo teorema (o meglio, una sua variante) che recentemente, Rivest,
Shamir e Adleman hanno inventato un metodo di crittograﬁa estremamente
eﬃciente e sicuro. Il metodo RSA ` e uno dei pi` u usati oggi (per esempio,
` e implementato nel programma di pubblico dominio PGP – Pretty Good
Privacy) ed ` e usato da molte autorit` a di certiﬁcazione riconosciute in rete.
Cominciamo enunciando quello che ` e comunemente conosciuto come il
Piccolo Teorema di Fermat.
pagina 7

5 Il teorema di Euler-Fermat ITS ICT Piemonte
Teorema 5.1 (Piccolo Teorema di Fermat). Sia p un numero primo, e sia
a un intero non divisibile per p. Allora
ap−1≡ 1 mod p.
Dimostrazione. Consideriamo i multipli di a
m1 =a, m 2 = 2a, m 3 = 3a, ..., m p−1 = (p− 1)a.
Nessuna coppia di questi numeri interi pu` o essere congrua modulop: infatti,
in tal caso, p sarebbe un divisore di mr−ms = (r−s)a, dove r ed s
sono numeri interi 1 ≤ r < s≤ p− 1, e poich´ er−s ` e minore dip ed
inoltre p non divide a per ipotesi, questo non ` e possibile. Dunque i numeri
m1,m 2,...,m p−1 sono congrui ai numeri 1 , 2,...,p − 1, considerati in un
ordine opportuno- Ma allora moltiplicando si ha
m1m2...m p−1 = 1· 2· 3··· (p− 1)ap−1≡ 1· 2· 3··· (p− 1) mod p,
e se per brevit` a poniamoK = 1· 2· 3··· (p− 1) possiamo scrivere
K(ap−1− 1)≡ 0 mod p.
Ma K non ` e divisibile perp, perch´ e nessuno dei suoi fattori lo ` e, e dunque
deve essere (ap−1− 1) divisibile per p, cio` e
ap−1≡ 1 mod p.
Notiamo che se n non ` e un numero primo, allora non si pu` o dire che
an−1 ≡ 1 mod n, in generale. Per esempio, se n = 4 e a = 3, si ha
33 = 27 ≡ 3 mod 4. Ci si pu` o dunque chiedere se ci sia una potenza di
a che sia congrua ad 1 modulo n. La risposta ` e s` ı, e l’esponente corretto ` e
stato trovato da Euler.
Deﬁnizione 5.1. Per un numero intero positivo n, indichiamo con ϕ(n) il
numero degli interi compresi fra 1 ed n coprimi con n.
pagina 8

5 Il teorema di Euler-Fermat ITS ICT Piemonte
Per esempio,
ϕ(1) = 1 perch´ e 1 ` e coprimo con 1,
ϕ(2) = 1 1 ` e coprimo con 2,
ϕ(3) = 2 1 e 2 sono coprimi con 3,
ϕ(4) = 2 1 e 3 sono coprimi con 4,
ϕ(5) = 4 1 , 2, 3 e 4 sono coprimi con 5,
ϕ(6) = 2 1 e 5 sono coprimi con 6,
ϕ(7) = 6 1 , 2, 3, 4, 5 e 6 sono coprimi con 7,
ϕ(8) = 4 1 , 3, 5 e 7 sono coprimi con 8,
ϕ(9) = 6 1 , 2, 4, 5, 7 e 8 sono coprimi con 9,
ϕ(10) = 4 1 , 3, 7 e 9 sono coprimi con 10,
... ...
Una propriet` a della funzioneϕ ` e evidente:
se p ` e un numero primo, alloraϕ(p) =p− 1,
in quanto tutti i numeri 1 , 2,...,p − 1 sono coprimi con p. Altrettanto
semplice ` e calcolareϕ(n) per un numero che sia potenza di un primo. La
formula ` e la seguente:
se n =pa, con p numero primo, allora ϕ(n) =pa−pa−1.
Infatti, i numeri non coprimi con pa sono tutti i multipli di p, e ne ne sono
pa−1 minori di pa. Notiamo che se a = 1 (cio` en =p ` e primo) ritroviamo la
stessa formula di prima. Per esempio, ϕ(125) =ϕ(53) = 53− 52 = 100.
L’ultima propriet` a della funzioneϕ ` e quella che consente di calcolare
ϕ(n) per un numero qualsiasi. La formula ` e
se m e n sono coprimi, cio` e (m,n ) = 1, allora ϕ(m·n) =ϕ(m)·ϕ(n)
Per esempio, usando la tabella precedente, si ha ϕ(21) = ϕ(3· 7) = 12,
ϕ(30) = ϕ(5· 6) = 8, e cos` ı via. Come vediamo, ` e molto semplice calcolare
ϕ(n) se si conosce la fattorizzazione di n. Questa ` e la propriet` a che verr` a
sfruttata nell’algoritmo RSA.
Vediamo ora il Teorema di Euler-Fermat.
Teorema 5.2 (di Euler-Fermat). Sia n un intero positivo e a un intero
coprimo con n. Allora
aϕ(n)≡ 1 mod n.
pagina 9

5 Il teorema di Euler-Fermat ITS ICT Piemonte
Osserviamo che, se n ` e primo, alloraϕ(n) =n− 1 e quindi ritroviamo il
Teorema di Fermat.
Ci si pu` o anche chiedere cosa capiti se ( a,n ) ̸= 1. Per esempio, se
n = 6,a = 2, si ha
22≡ 4 mod 6
23≡ 2 mod 6
24≡ 2 mod 6
e cos` ı via, e vediamo che le potenze di 2 modulo 6 alternano fra 2 e 4 e non
si ottiene mai 1. Osserviamo per` o che il teorema di Euler-Fermat si pu` o
enunciare in modo equivalente come
Teorema 5.3 (di Euler-Fermat). Sia n un intero positivo ed a un intero
coprimo con n. Allora
aϕ(n)+1≡a mod n.
In questa forma la conclusione del teorema vale anche per n = 6, a = 2.
Non ` e per` o possibile eliminare del tutto l’ipotesi chea ed n siano coprimi
come mostra l’esempio n = 12, a = 2: si ha
22≡ 4 mod 12
23≡ 8 mod 12
24≡ 4 mod 12
25≡ 8 mod 12
e tutte le potenze successive alternano fra 4 e 8, e dunque non si riottiene
pi` u 2. Se per` o facciamo un’ipotesi sun, ` e possibile eliminare la condizione
chea ed n siano coprimi.
Deﬁnizione 5.2. Un intero n si dice libero da quadrati se ` e il prodotto
di numeri primi distinti, cio` e se non ` e divisibile per nessun quadrato> 1.
Per esempio, 6 = 2· 3 ` e libero da quadrati, mentre 12 = 2· 2· 3 non lo
` e. Con questa deﬁnizione si pu` o enunciare il seguente teorema:
Teorema 5.4. Se n =p1·p2,··· pk ` e libero da quadrati, allora
aϕ(n)+1≡a mod n
per ogni interoa.
pagina 10

6 I sistemi di crittograﬁa ITS ICT Piemonte
Osserviamo che la conclusione ` e la stessa del Teorema di Euler-Fermat,
ma l’ipotesi (a,n ) = 1 ` e stata sostituita dall’ipotesi n libero da quadrati.
Usando il Teorema 5.4 si pu` o dimostrare facilmente per induzione che vale
il seguente risultato pi` u generale:
Deﬁnizione 5.3. Se n =p1·p2,··· pk ` e libero da quadrati allora
ahϕ(n)+1≡a mod n
per ogni interoa e per ogni interoh≥ 1.
6 I sistemi di crittograﬁa
Il problema della crittograﬁa ` e semplice da enunciare: ci sono due per-
sone, il mittente ed il destinatario1, che chiameremoA eB, che vogliono co-
municare fra loro senza che nessun altro possa leggere i loro messaggi. Dato
un messaggio M, che possiamo immaginare essere una sequenza di simboli
o numeri,A usa una funzione f (ovvero un algoritmo) che trasforma M in
un’altra sequenza C e invia questa sequenza. B usa un’altra funzione g che
trasformaC di nuovo nel messaggio originaleM. Naturalmente, se qualcuno
intercettaC non deve essere in grado di usare la funzione g per decodiﬁcare
il messaggio.
L’idea di sistema crittograﬁco pu` o dunque essere resa mediante uno
schema del tipo:
M
f
−→C
g
− →M
doveM ` e l’insieme deimessaggi,C quello dei messaggi cifrati edf eg sono
funzioni tali che
f◦g =ιM
(quindi ` e necessario chef sia iniettiva). f ` e la procedura dicifratura e g
quella di decifratura.
Per ottenere ci` o, di solito si usa unachiave (per esempio una password).
Dunque la funzione che codiﬁca f non ha come argomento solo il messaggio
M, ma anche un altro parametro, la chiave k. In simboli
f(M,k ) =C
e la funzione g tale che
g(C,k ) =M
1In letteratura spesso chiamati Alice e Bob.
pagina 11

6 I sistemi di crittograﬁa ITS ICT Piemonte
cosicch´ e, conoscendo la chiave, si possa decrittare il messaggio. Questo
schema, che usa la stessa chiave k sia per la codiﬁca che per la decodiﬁca,
si chiama simmetrico.
In crittograﬁa si suppone che tutti siano a conoscenza dell’algoritmo che
usano f e g, perch´ e ` e sempre possibile avere questa informazione mediante
attivit` a di spionaggio o simili. Basare la segretezza delle comunicazioni sulla
segretezza dell’algoritmo non ` e una buona idea. Invece la segretezza ` e basata
sul fatto che solo ilA eB conoscono la chiave. Infatti, l’algoritmo viene usato
sempre, mentre la chiave pu` o essere cambiata ogni volta. In questo modo,
anche se qualcuno “ruba” una chiave, la pu` o usare solo poche volte.
Questa situazione (cambiare spesso la chiave) richiede per` o un modo di
comunicare sicuro fraA eB. Un altro problema ` e il seguente: se vi ` e un solo
ricevente, ma molti mittenti, tutti i mittenti conoscono la chiave, e possono
leggere i messaggi l’uno dell’altro, cosa che un mittente certamente non
vuole. Questo ` e il problema che il metodo a chiave pubblica vuole risolvere.
Lo schema ` e il seguente:
B comunica pubblicamente una chiavee.A codiﬁca il messaggio
usando la funzione f = (M,e ) = C e trasmette il messaggio.
B possiede un’altra chiave d privata. B decodiﬁca il messaggio
usando g = (C,d ) =M.
Questo elimina il problema della distribuzione delle chiavi, e anche la chiave
che serve per codiﬁcare non ` e quella che decodiﬁca, e quindi solo B pu` o
leggere i messaggi. Questo schema ` e stato proposto per la prima volta
da Whitﬁeld Diﬃe e Martin Hellman nel 1976. Uno schema diﬀerente di
crittograﬁa a chiave pubblica ` e stato proposto nello stesso anno da Ralph
Merkle.
Per fare un’analogia, un metodo simmetrico ` e come una cassaforte, e
la chiave ` e la combinazione per aprirla. Una persona che ha la chiave pu` o
aprire la cassaforte e depositare un documento (codiﬁcare un messaggio).
Un’altra persona con la chiave pu` o aprire la cassaforte e prendere il docu-
mento (decodiﬁcare il messaggio). Chi non ha la chiave (l’avversario, la spia,
ecc.) deve scassinare la cassaforte. Un metodo a chiave pubblica invece ` e
come una buca delle lettere. Chiunque pu` o inﬁlare una lettera nella buca
(codiﬁcare il messaggio con la chiave pubblica), ma solo il proprietario della
buca ha la chiave per aprirla facilmente (decodiﬁcare il messaggio). Tutti
gli altri devono scassinare la buca delle lettere, e questo ` e possibile, e anche
pi` u facile che scassinare una cassaforte, ma richiede tempo. Se il padrone
della buca ritira spesso la sua posta oppure se cambia spesso la serratura,
la sua posta ` e al sicuro.
pagina 12

7 L’algoritmo RSA ITS ICT Piemonte
Naturalmente, la domanda ` e: funzionif eg con le propriet` a richieste da
questo schema esistono? Si pu` o pensare che se si conosce la chiave e usata
per codiﬁcare il messaggio, e la funzionef che eﬀettua la codiﬁca, deve essere
possibile in qualche modo decodiﬁcare il messaggio, e cio` e un simile schema
non pu` o funzionare. L’intuizione di Rivest, Shamir e Adleman (1978) ` e stata
che ` e possibile costruire funzionif e g tali che:
1. mediante la chiave privata d la decodiﬁca ` e semplice e rapida, e
2. usando la conoscenza della funzione f e della chiave pubblica e, la
decodiﬁca ` e possibile ma richiede troppo tempo per essere utile.
Per esempio, troppo tempo pu` o voler dire che eseguire tutti i calcoli necessa-
ri, anche usando i computer pi` u veloci a disposizione, richiede alcuni anni.`E
chiaro che leggere un messaggio segreto alcuni anni dopo che ` e stato scritto
non ` e di grande utilit` a.
7 L’algoritmo RSA
Descriviamo ora l’algoritmo RSA che, fra tutti gli algoritmi proposti per
la crittograﬁa a chiave pubblica che si sono rivelati sicuri, ` e il pi` u semplice
sia da capire che da implementare.
B sceglie due numeri primi p e q, molto grandi, li moltiplica e forma il
numeron =pq, che ` e libero da quadrati. Sappiamo cheϕ(n) = (p−1)(q−1).
Ora sceglie un numero e che sia coprimo con ϕ(n). La chiave pubblica per
codiﬁcare i messaggi ` e la coppia (n,e ). La funzione f per la codiﬁca ` e la
seguente:
• si trasforma il messaggio in un numeroM, minore din, Se il messaggio
` e molto lungo, lo si spezza in blocchi pi` u piccoliM1,...,M k;
• si calcola Ci =M e
i mod n per ogni i;
• si trasmette C1,...,C k.
Per decodiﬁcare, si procede nel modo seguente: consideriamo l’equazione
ex≡ 1 mod ϕ(n).
Poich´ ee ` e coprimo conϕ(n), questa equazione ha una soluzione d, per cui
valeed = 1 +hϕ(n). Allora la funzione g di decodiﬁca ` e:
• si calcola Mi =Cd
i mod n.
pagina 13

7 L’algoritmo RSA ITS ICT Piemonte
Infatti
Cd
i = (M e
i )d =M ed
i =M 1+hϕ(n)
i ≡Mi mod n =Mi
dove la congruenza ` e vera in virt` u della deﬁnizione 5.3 e l’ultima eguaglianza
vale in quanto Mi<n .
Facciamo qualche esempio semplice, tralasciando i calcoli. Se prendiamo
p = 47 e q = 71, allora
n = 47· 71 = 3337
La chiave pubblica e deve essere coprima con
ϕ(3337) = (p− 1)(q− 1) = 46· 79 = 3220
Scegliamo a caso un numero e coprimo con 3220, ad esempio e = 79, che
essendo primo ` e sicuramente coprimo con 3220. In questo caso, calcolando
con l’algoritmo di Euclide si ottiene
3220 = 40· 79 + 60
79 = 1· 60 + 19
60 = 3· 19 + 3
19 = 6· 3 + 1
Calcolando con i resti si ottiene
(79, 3220) = 1 = 1019· 79− 25· 3220
e dunque abbiamo la chiave privata d = 1019. Rendiamo pubblici n ed e,
teniamo segreto d ed eliminiamo p e q.
Per codiﬁcare il messaggio
M = 6882326879666683
per prima cosa lo spezziamo in blocchi pi` u piccoli. Poich´ e n = 3337 ha
quattro cifre, blocchi di tre cifre vanno bene. Dunque il messaggio si spezza
in
M1 = 688
M2 = 232
M3 = 687
M4 = 966
M5 = 668
M6 = 003
pagina 14

7 L’algoritmo RSA ITS ICT Piemonte
Il primo blocco ` e codiﬁcato da
68879 mod 3337 = 1570 = C1
Notiamo che non bisogna elevare 688 alla 79-esima potenza (numero molto
grande) e poi ridurre modulo 3337. Invece, si calcola 688 2 e si riduce modulo
3337, poi si moltiplica di nuovo per 688 e si riduce nuovamente modulo 3337
e cos` ı via, e in ogni passo i numeri sono piccoli. Ci sono metodi per calcolare
queste potenze in modo ancora pi` u veloce di quello descritto, rendendo cos` ı
la codiﬁca del messaggio veloce.
Ripetendo gli stessi passi su tutti gli altri blocchi otteniamo il messaggio
codiﬁcato
C = 1570 2756 2091 2276 2423 158
Decodiﬁcare il messaggio richiede le stesse operazioni usando l’esponente
d = 1019 sui blocchi di C. Si ha
15701019 mod 3337 = 688 = M1
e in modo simile per i blocchi successivi.
Perch´ e questo metodo ` e sicuro? In fondo, per ottenere la chiave privata
d basta conoscere ϕ(n) e tutti conoscono n. Il modo pi` u rapido di calcolare
ϕ(n) ` e avere la decomposizionen =pq, cio` e dobbiamo fattorizzaren. Negli
anni recenti sono stati sviluppati molti metodi di fattorizzazione, ed il mi-
gliore di quelli attualmente noti si chiama “General Number Field Sieve”,
abbreviato in GFNS. La matematica che sta dietro questi algoritmi ` e molto
complicata, e non possiamo in queste note dire niente al riguardo.
Piuttosto, ` e interessante vedere alcuni risultati concreti. I dati che cite-
remo sono in continua evoluzione, perci` o possono diventare obsoleti anche
molto presto. Un aspetto interessante del problema della fattorizzazione ` e
costituito dai cosiddetti RSA Challanges , le “sﬁde RSA”, che consistono in
una serie di numeri da fattorizzare. Iniziata negli anni ’90, questa sﬁda ` e
uﬃcialmente terminata nel 2007.2 L’ultimo nuemero fattorizzato (12 dicem-
bre 2009) ` e noto come RSA 768, cio` e ` e un numero che in rappresentazione
2Un archivio ` e disponibile presso http://www.emc.com/emc-plus/rsa-labs/
historical/the-rsa-challenge-numbers.htm
pagina 15

7 L’algoritmo RSA ITS ICT Piemonte
binaria ha 768 cifre, in notazione decimale ha 232 cifre. Il numero ` e:
123018668453011775513049495838496272077285
356959533479219732245215172640050726365751
874520219978646938995647494277406384592519
255732630345373154826850791702612214291346
167042921431160222124047927473779408066535
1419597459856902143413
e i suoi due fattori primi sono
334780716989568987860441698482126908177047
949837137685689124313889828837938780022876
14711652531743087737814467999489
e
3674604366679959042824463379962795263227915
8164343087642676032283815739666511279233373
417143396810270092798736308917
Il tempo necessario per fattorizzare questi numeri ` e notevole. L’algoritmo
GNFS ` e composto da due parti, una preliminare per cercare una serie di
equazioni lineari da risolvere (sieving step) e una seconda in cui si risolve un
sistema di equazioni (matrix step). La prima pu` o essere eseguita in parallelo
su pi` u calcolatori, mentre la seconda deve essere fatta tutta insieme.
La fattorizzazione di RSA 768 ha richiesto l’equivalente di circa 1500
anni di lavoro di un processore AMD Opteron a 2.2 Ghz con 2GB di RAM
per il primo passo, mentre la risoluzione del sistema ha richiesto sei mesi di
lavoro ad un cluster di 80 processori AMD Opteron a 2.2 Ghz. In termini
di tempo reale, i calcoli per la fattorizzazione sono durati un paio di anni. 3
In confronto RSA 663, un po’ pi` u piccolo, ha richiesto circa la met` a del
tempo. Si stima che fattorizzare RSA 1024, con 1024 cifre binarie (309 cifre
decimali) richieda circa 1000 volte il tempo occorso per fattorizzare RSA
768.
Cosa possiamo concludere: chiavi a 1024 bit sono abbastanza sicure oggi
e per ancora (forse) molti anni, mentre chiavi a 640 bits sono gi` a insicure.
3http://eprint.iacr.org/2010/006.pdf
pagina 16

7 L’algoritmo RSA ITS ICT Piemonte
Si potrebbe osservare: non ` e necessario trovare i fattori p e q, ma solo
calcolareϕ(n). In questo caso per` o, se conosciamop eq sappiamo calcolare
ϕ(n) semplicemente, bastano due sottrazioni e una moltiplicazione:
ϕ(n) = (p− 1)(q− 1)
Viceversa, conoscendo n e ϕ(n) ` e facile trovarep e q, basta risolvere una
equazione di secondo grado. Ponendo B = pq e A = p + q si ha che
l’equazione
x2−Ax +B = 0
ha come soluzioni esattamente p e q. Quindi, conoscendo ϕ(n) si ha un
algoritmo che in pochi passi, una somma e la risoluzione di un’equazione di
secondo grado, consente di fattorizzare il numero n. Dunque la complessit` a
di calcolo per determinareϕ(n) ` e equivalente alla complessit` a di fattorizzare
il numero n che, come abbiamo visto, ` e piuttosto grande.
Questo spiega perch´ e il metodo ` e sicuro.`E per` o importante osservare
che nessuno ha mai dimostrato che fattorizzare il numero n ` e veramente
cos` ı diﬃcile, ma solo che i migliori algoritmi conosciuti sono troppo lenti.
Potrebbe capitare che un giorno qualcuno scopra un metodo pi` u eﬃciente
per fattorizzare i numeri, ed allora il metodo RSA non sarebbe pi` u sicuro.
La crittograﬁa ` e un argomento aﬀascinante, ed ` e un campo in cui l’av-
vento dei computer ha portato grandi novit` a e possibilit` a di utilizzo.`E bene
osservare che non sempre il mittente ed il ricevente sono esseri umani, ma
potrebbero essere entrambi computer che devono comunicare fra loro, per
esempio un telefono cellulare che comunica con la rete di telefonia (non vo-
gliamo che un telefono non autorizzato possa mettersi in contatto ed usare
le risorse della rete oppure che qualcuno possa intercettare la trasmissione
e ascoltare le nostre telefonate), oppure un computer che manda una richie-
sta ad un server, per esempio per fare una stampa (non vogliamo che tutti
possano usare le nostre stampanti) e cos` ı via. Quindi ` e importante avere dei
metodi semplici per trasmettere in sicurezza.
La sicurezza di un sistema per` o non ` e solo nella matematica che si usa,
ma anche nel protocollo. Possiamo avere il sistema pi` u sicuro del mon-
do, ma se riveliamo la chiave privata ad un estraneo la nostra sicurezza ` e
irrimediabilmente compromessa.
pagina 17


---

# Cifrario di cesare

**File:** `Cifrario di cesare.py`
**Tipo:** `.py`
**Dimensione:** 0.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

def encrypt_char(char: str, key: int) -> str:
    if char.isupper():
        return chr((ord(char) - 65 + key) % 26 + 65)
    elif char.islower():
        return chr((ord(char) - 97 + key) % 26 + 97)
    return char


def encrypt(text: str, key: int) -> str:
    result = ''
    for char in text:
        result += encrypt_char(char, key)
    return result


def main():
    action = input("Vuoi (c)ifrare o (d)ecifrare? ").strip().lower()
    if action not in ('c', 'd'):
        print("Scelta non valida.")
        return

    text = input("Inserisci il testo: ")
    key = int(input("Inserisci la chiave: "))

    if action == 'd':
        key = -key

    result = encrypt(text, key)
    print(f"Risultato: {result}")


if __name__ == '__main__':
    main()


---

# Demo entropia

**File:** `Demo entropia.md`
**Tipo:** `.md`
**Dimensione:** 13.9 KB
**Ultima modifica:** 02/07/2026 09:25

---

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


---

# Enigma Keys

**File:** `Enigma Keys.txt`
**Tipo:** `.txt`
**Dimensione:** 3.1 KB
**Ultima modifica:** 02/07/2026 09:28

---

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

# Esercizi di subnetting IPv4

**File:** `Esercizi di subnetting IPv4.pdf`
**Tipo:** `.pdf`
**Dimensione:** 164.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

 
 
 
 
 
 
 
 
 
 
 
 
  
DOCENTE Andrea Blanchietti 
UNITA’ 
FORMATIVA Fondamenti di Reti di Calcolatori 
ARGOMENTO Esercizi di subnetting IPv4 

 
Esercizio 1 
Creare 16 sottoreti partendo dall’indirizzo di rete 192.168.10.0/24 
Esercizio 2 
Partendo dall’indirizzo di rete 172.16.0.0/16 individuare tutte possibili sottoreti 
dimensionate su 2000 indirizzi host 
Esercizio 3 
Partendo da 172.16.128.0/19 creare otto sottoreti da 1000 indirizzi 
Esercizio 4 
Partizionare in due sottoreti la rete 10.0.192.0/20  
 
Richieste 
• Per ogni sottorete indicare l’indirizzo di rete, il primo e l’ultimo indirizzo di 
host e l’indirizzo di broadcast 
• Quanti bit si devono promuovere? 
• Quanti bit rimangono nella parte host dell’indirizzo? Quanti indirizzi di host 
utilizzabili per sottorete?  
 
 
 
 
 


---

# Estratto da _L'arte dell'inganno_ di Kevin Mitnick

**File:** `Estratto da _L'arte dell'inganno_ di Kevin Mitnick.pdf`
**Tipo:** `.pdf`
**Dimensione:** 33.1 KB
**Ultima modifica:** 02/07/2026 09:25

---

L’arte dell’inganno di Kevin Mitnick. Estratto dal cap. 4: Costruire la ﬁducia 
Alcune di queste storie potrebbero indurvi a 
pensare che considero perfetti idioti tutti 
coloro che lavorano, pronti se non 
addirittura smaniosi di cedere ogni segreto 
che detengono. L’ingegnere sociale sa che 
non è vero. Perché i suoi attacchi sono tanto 
fortunati? Non perché la gente sia stupida o 
priva di buon senso. Come esseri umani 
siamo tutti vulnerabili ai raggiri perché 
tendiamo a ﬁdarci immotivatamente se 
manipolati in una certa maniera. 
L’ingegnere sociale anticipa i sospetti e 
resistenze, ed è sempre pronto ribaltare la 
sﬁducia in ﬁducia. Se è in gamba 
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
loro ﬁducia. 
Una volta ottenuta il ponte levatoio è 
abbassato e la porta del castello è spalancata 
per farlo entrare a prendere le informazioni 
che cerca. 
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
all’ultimo momento ha cambiato idea 
dicendo: “V orrei anche scrivere alla sede 
centrale della vostra rete. Qual è il numero 
della vostra ﬁliale?”. Lei gli dà anche questa 
informazione, lui la ringrazia, aggiunge 
qualche complimento su quanto è stata 
gentile e la saluta. 
“Una chiamata come questa fa passare più 
svelto il turno di lavoro. Come sarebbe bello 
se la gente fosse tutta così”, 
 pensava Andrea. 
La seconda telefonata: Ginny 
“Grazie per aver chiamato Studio Video. 
Sono Ginny , in cosa posso esserle utile?” 
“Ciao Ginny , sono Tommy Allison, titolare 
di Forest Park, negozio 863. Abbiamo qui 
un cliente che vorrebbe noleggiare Rocky 5, 
ma abbiamo ﬁnito le copie. Puoi controllare 
se ne avete?” le domanda pimpante colui 
L’ARTE DELL’INGANNO KEVIN MITNICK 1

che chiama, con il tono di chi conosce 
Ginny da una vita. 
Lei torna in linea dopo qualche secondo 
dicendo che ne hanno tre copie. 
“Bene, adesso vedo se ha voglia di passare a 
prenderla. Grazie. Se hai bisogno di un 
favore basta che chiami e chiedi di Tommy , 
sarò lieto di fare il possibile.” 
Nelle due settimane seguenti Ginny riceve 
tre o quattro chiamate da Tommy per 
richieste varie. Sembrano domande 
legittime e lui suona sempre molto 
amichevole senza apparire assillante, 
aggiungendo ogni tanto due chiacchiere tipo 
“Hai sentito dell’incendio a Oak Park? 
Hanno chiuso un sacco di strade” eccetera. 
Quelle telefonate sono un piccolo diversivo 
dalla routine, e Ginny è sempre lieta di 
riceverle. 
Un giorno Tommy fa una telefonata 
dall’aria sconvolta. “ Avete per caso problemi 
con i computer?” 
“No, perché?” ribatte Ginny . 
“Un tipo è andato a sbattere contro un palo 
del telefono e il tecnico dice che ﬁno a 
quando non l’avranno sistemato un pezzo di 
città rimarrà senza telefono e senza 
Internet.” 
“Oh no, si è fatto male quel tipo?” 
“L’hanno portato via in ambulanza. A 
proposito, avrei bisogno di una mano. c’è 
qui un vostro cliente che vorrebbe 
noleggiare Il Padrino II, ma non ha la tessera 
dietro. Potreste controllare i dati?” 
“Certo” 
Tommy fornisce il nome e l’indirizzo del 
cliente, che Ginny trova nel computer, 
dandogli il numero della tessera. 
“Ha qualche pagamento in sospeso o in 
ritardo?” domanda Tommy . 
“Non vedo nulla.” 
“Perfetto. Adesso segno a mano e inserisco 
dopo i dati appena i computer riprendono a 
marciare. Ah, vorrebbe addebitare sulla 
Visa che usa da voi, solo che non ce l’ha con 
sé. Mi dai il numero e la data di scadenza?” 
Lei acconsente. Allora Tommy dice: “Grazie 
per l’aiuto, ci risentiamo.” e appende. 
Analisi dell’attacco. 
Le prime chiamate di Tommy a Ginny 
servivano solo per ottenere la sua ﬁducia. 
Quando è arrivato il momento dell’attacco 
vero e proprio lei aveva la guardia abbassata 
e ha accettato Tommy per quel che diceva 
di essere, il titolare di un altro negozio della 
catena. E perché no? Lo conosceva. Solo 
per telefono, è ovvio, però la loro era 
un’amicizia di lavoro, la base della ﬁducia. 
Una volta che lei l’ha accettato come ﬁgura 
credibile, come un negoziante della loro 
rete, la ﬁducia c’era già e il resto è stato una 
passeggiata. 
La tecnica dell’accattivarsi la ﬁducia è una 
delle tattiche più efﬁcaci dell’ingegneria 
sociale. Dovete sempre domandarvi se 
conoscete sul serio la persona con cui state 
parlando. In certi rari casi potrebbe non 
rivelarsi chi sostiene di essere, Quindi 
dobbiamo imparare a osservare, a riﬂettere 
e a veriﬁcare l’identità.
L’ARTE DELL’INGANNO KEVIN MITNICK 2


---

# Indirizzamento IPv4

**File:** `Indirizzamento IPv4.pdf`
**Tipo:** `.pdf`
**Dimensione:** 339.6 KB
**Ultima modifica:** 02/07/2026 09:24

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
DOCENTE Andrea Blanchietti 
UNITA’ 
FORMATIVA Fondamenti di Reti di Calcolatori 
ARGOMENTO Indirizzamento IPv4 

Indirizzamento con protocollo IPv4 
L’indirizzo IPv4 è composto da una sequenza di 32 bit, suddivisa in quattro gruppi da 8 bit l’uno; 
ogni gruppo è definito ottetto. La rappresentazione dell’indirizzo avviene convertendo i singoli 
ottetti dal sistema binario al sistema decimale: si parla di notazione decimale puntata. 
 
 
 
L’indirizzo possiede una struttura gerarchica: una parte dell’indirizzo definisce la rete nel suo 
insieme e la rimanente parte individua l’host (PC, stampante, server, etc.) all’interno della rete. I 
bit che definiscono la parte di rete sono individuati dalla subnet mask. Per esempio: 
Indirizzo:  192.168.10.23 
Subnet mask:  255.255.255.0 
Anche la subnet mask ha una struttura a quattro ottetti e viene utilizzata per individuare la parte 
rete all’interno dell’indirizzo. I bit di rete dell’indirizzo corrispondono ai bit con valore 1 nella 
subnet mask, mentre i bit della parte host corrispondono ai bit con valore 0; nell’esempio 
precedente, la rete è rappresentata dal primo, dal secondo e dal terzo ottetto, contando a partire 
da sinistra: 
192.168.10.______________ 
La parte di rete è sempre composta dai bit più significativi dell’indirizzo. 


Una seconda notazione possibile per indicare i bit di rete all’interno dell’indirizzo è utilizzare il 
Prefix Length (tradotto letteralmente in lunghezza del prefisso), ovvero un numero che indica 
quanti sono i bit della parte rete. 
Usando l’esempio precedente, ho 24 bit di rete: 
192.168.10.23/24 
Nell’indirizzamento IPv4, per ogni rete vi sono due indirizzi riservati: il network address (indirizzo 
di rete, ovvero l’indirizzo che rappresenta la rete nel suo complesso) e il broadcast address 
(indirizzo di broadcast, ovvero l’indirizzo per le comunicazioni da un singolo host a tutti gli host 
della rete).  
• Nell’indirizzo di rete (network address), tutti i bit della parte host sono pari a 0  
• Nell’indirizzo di broadcast, tutti i bit della parte host sono pari a 1 
Usando l’esempio precedente, considerando una subnet mask pari a 255.255.255.0: 
 
Network address:  192.168.10.0   tutti I bit della parte host sono 0 
 
Broadcast address:  192.168.10.255   tutti I bit della parte host sono 1 
 
Tutti i rimanenti indirizzi compresi fra  192.168.10.1  e  192.168.10.254  sono utilizzabili per 
indirizzare gli host all’interno della rete. Il numero di indirizzi disponibili per gli host di una rete 
dipende da quanti bit abbiamo a disposizione.  
  

Dato un network address, quanti indirizzi si hanno a disposizione per gli host?  
Dati n bit nella parte host di un indirizzo, quante combinazioni si possono ottenere? 
2n 
Tolgo il network address ed il broadcast e ottengo il numero di indirizzi di host per un certo 
indirizzo di rete: 
Numero indirizzi disponibili = 2n - 2 
 
Esempio:  192.168.10.____________                                      28 – 2 = 254 indirizzi disponibili 
 
 
Classi di indirizzamento 
La struttura originale dell’indirizzamento IPv4 (legacy) prevede tre classi utilizzabili per indirizzare 
le reti (indicate con le lettere A, B e C) più due classi ad uso speciale, ovvero la classe D degli 
indirizzi multicast e la classe E per usi sperimentali. 
 
• La seconda colonna della tabella indica, per ogni classe, l’intervallo dei valori possibili per il 
primo ottetto dell’indirizzo. 
• La terza colonna della tabella indica, per ogni classe, l’intervallo dei valori possibili in binario 
per il primo ottetto dell’indirizzo. 
n = 8 
8 bit 


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
• CLASSE B: Indirizzi di rete dal   172.16.0.0   al   172.31.0.0   con subnet mask 255.255.0.0  
• CLASSE C: Indirizzi di rete 192.168. X .0 con subnet mask 255.255.255.0, dove il terzo 
ottetto X può assumere un valore compreso tra 0 e 255  
 
TABELLA RIASSUNTIVA INDIRIZZI IPv4 PRIVATI 
CLASSE INDIRIZZO DI RETE SUBNET MASK NOTAZIONE CON PREFIX 
LENGTH 
A 10.0.0.0 255.0.0.0 10.0.0.0/8 
B 172.16.0.0 
 
 
 
172.31.0.0 
 
255.255.0.0 172.16.0.0/16 
 
 
172.31.0.0/16 
oppure 
172.16.0.0/12 
C   192.168.0.0 
 
 
 
 
192.168.255.0 
 
255.255.255.0   192.168.0.0/24 
 
 
 
192.168.255.0/24 
oppure 
192.168.0.0/16 
 
  

Dato un indirizzo IP, come possiamo risalire all’indirizzo di rete (network address) e 
all’indirizzo di broadcast?  
Dato un indirizzo IPv4, voglio sapere quale è la rete di appartenenza (ovvero l’indirizzo di rete), a quale 
indirizzo di broadcast corrisponde e a quale intervallo degli indirizzi appartiene. 
Si deve individuare la parte host e la parte rete dell’indirizzo, in base alla maschera di sottorete o al prefix 
length 
ESEMPIO 1.  192.168.10.5/24 è un indirizzo utilizzabile per indirizzare un host e corrisponde a: 
RETE 192.168.10.0/24 
BROADCAST 192.168.10.255/24 
HOST RANGE da 192.168.10.1  a  192.168.10.254 
SUBNET MASK 255.255.255.0 
ESEMPIO 2.  172.21.152.12/16 è un indirizzo utilizzabile per indirizzare un host e corrisponde a: 
RETE 172.21.0.0/16 
BROADCAST 172.21.255.255/8 
HOST RANGE da 172.21.0.1  a  172.21.255.254 
SUBNET MASK 255.255.0.0 
ESEMPIO 3.  10.16.42.10/8 è un indirizzo utilizzabile per indirizzare un host e corrisponde a: 
RETE 10.0.0.0/8 
BROADCAST 10.255.255.255/8 
HOST RANGE da 10.0.0.1  a  10.255.255.254 
SUBNET MASK 255.0.0.0 
 
 
 
 
 


---

# InterVLAN Routing

**File:** `InterVLAN Routing.pdf`
**Tipo:** `.pdf`
**Dimensione:** 810.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

Routing inter-VLAN

2
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Obiettivi del modulo
Titolo del modulo: Routing inter-VLAN
Obiettivo del modulo: Risolvere i problemi di routing inter-VLAN sui dispositivi di Layer 3
Titolo argomento Obiettivo argomento
Funzionamento del routing inter-
VLAN
Descrivere le opzioni per la configurazione del routing 
tra VLAN.
Routing inter-VLAN router-on-a-stick Configurare il router-on-a-stick inter-VLAN routing.
Routing inter-VLAN utilizzando 
switch Layer 3
Configurare il routing inter-VLAN utilizzando lo 
switching Layer 3
Risoluzione dei problemi relativi al 
routing inter-VLAN
Risolvere i problemi comuni di configurazione tra 
VLAN.

3
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Funzionamento del routing
inter-VLAN

4
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
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
dimensioni.
• Switch di livello 3 utilizzando interfacce virtuali commutate (SVI)- Questa è la soluzione più 
scalabile per organizzazioni di medie e grandi dimensioni. 

5
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Funzionamento del routing inter-VLAN
Routing legacy inter-VLAN
• La prima soluzione di routing inter-VLAN si basava sull'utilizzo di un router con più interfacce 
Ethernet. Ogni interfaccia router è stata collegata a una porta switch in diverse VLAN. Le 
interfacce del router fungono da gateway predefiniti per gli host locali nella subnet VLAN.
• Il routing inter-VLAN legacy utilizzando interfacce fisiche funziona, ma ha una limitazione 
significativa. Non è ragionevolmente scalabile perché i router hanno un numero limitato di 
interfacce fisiche. La richiesta di un'interfaccia router fisica per VLAN esaurisce rapidamente la 
capacità dell'interfaccia fisica di un router.
• Nota: Questo metodo di routing inter-VLAN non è più implementato nelle reti commutate ed è 
incluso solo a scopo esplicativo.


6
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Funzionamento del routing inter-VLAN
Routing router-on-a-stick inter-VLAN
Il metodo di routing inter-VLAN "router-on-a-stick" supera la limitazione del metodo di routing inter-VLAN 
legacy. Richiede solo un'interfaccia Ethernet fisica per instradare il traffico tra più VLAN su una rete.
• Un'interfaccia Ethernet router Cisco IOS è configurata come un trunk 802.1Q e collegata a una porta 
trunk su uno switch Layer 2. In particolare, l'interfaccia del router è configurata utilizzando subinterfacce 
per identificare VLAN instradabili.
• Le subinterfacce configurate sono interfacce virtuali basate su software. Ciascuna è associata a 
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

7
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3
Il metodo moderno per eseguire il routing inter-VLAN consiste nell'utilizzare gli switch di Layer 3 e le 
interfacce virtuali commutate (SVI). Un SVI è un'interfaccia virtuale configurata su uno switch Layer 3, 
come mostrato nella figura.
Nota: Uno switch Layer 3 è anche chiamato interruttore multilayer in quanto opera al Layer 2 e al Layer 
3. Tuttavia, in questo corso usiamo il termine switch Layer 3.


8
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Funzionamento del routing inter-VLAN
Routing inter-VLAN su uno switch di Layer 3 (seguito)
Gli SVI inter-VLAN vengono creati nello stesso modo in cui viene configurata l'interfaccia VLAN di 
gestione. L'SVI viene creato per una VLAN esistente sullo switch. Anche se virtuale, l'SVI svolge le 
stesse funzioni per la VLAN come farebbe un'interfaccia router. In particolare, fornisce l'elaborazione 
Layer 3 per i pacchetti inviati a o da tutte le porte switch associate a tale VLAN.
Di seguito sono riportati i vantaggi dell'utilizzo di switch Layer 3 per il routing inter-VLAN:
• Sono molto più veloci del router-on-a-stick perché tutto è hardware commutato e instradato.
• Non è necessario alcun collegamento esterno dallo switch al router per il routing.
• Essi non sono limitati a un collegamento perché Layer 2 EtherChannels può essere utilizzato 
come collegamenti trunk tra gli switch per aumentare la larghezza di banda.
• La latenza è molto inferiore perché i dati non devono lasciare lo switch per essere instradati a una 
rete diversa.
• Sono più comunemente distribuiti in una LAN del campus rispetto ai router.
• L'unico svantaggio è che gli interruttori Layer 3 sono più costosi.

9
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-
on-a-stick

10
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-on-a-stick
Scenario di router-on-a-stick
• Nella figura, l'interfaccia R1 GigabitEthernet 0/0/1 è 
collegata alla porta S1 FastEthernet 0/5. La porta S1 
FastEthernet 0/1 è collegata alla porta S2 FastEthernet 0/1. 
Si tratta di collegamenti trunk necessari per inoltrare il 
traffico all'interno e tra le VLAN.
• Per instradare VLAN, l'interfaccia R1 GigabitEthernet 0/0/1 è 
logicamente suddivisa in tre subinterfacce, come mostrato 
nella tabella. La tabella mostra anche le tre VLAN che 
verranno configurate sugli switch.
• Si supponga che R1, S1 e S2 hanno configurazioni di base 
iniziali. Attualmente PC1 e PC2 non possono eseguire il 
ping a vicenda perché si trovano su reti separate. Solo S1 e 
S2 possono eseguire il ping a vicenda, ma sono 
irraggiungibili da PC1 o PC2 perché sono anche su reti 
diverse.
• Per consentire ai dispositivi di eseguire il ping reciproco, gli 
switch devono essere configurati con VLAN e trunking e il 
router deve essere configurato per il routing inter-VLAN.
Sottointerfacc
ia VLAN Indirizzo IP
G0/0/1.10 10 192.168.10.1/24
G0/0/1.20 20 192.168.20.1/24
G0/0/1.30 99 192.168.99.1/24


11
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-on-a-stick
Configurazione VLAN e Trunking S1
Per configurare S1 con VLAN e trunking, completare i passaggi seguenti:
• Passo 1. Creare e assegnare un nome alle VLAN. 
• Passo 2. Creare l'interfaccia di gestione.
• Passo 3. Configurare le porte di accesso.
• Passo 4. Configurare le porte trunking. 

12
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-on-a-stick
Configurazione VLAN e Trunking S2
La configurazione per S2 
è simile a S1.


13
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-on-a-stick
Configurazione sottointerfaccia R1
Il metodo router-on-a-stick richiede di creare una sottointerfaccia per ogni VLAN da instradare. 
Viene creata una sottointerfaccia utilizzando il comando interfaceinterface_id subinterface_id in 
modalità di configurazione globale. La sintassi dell'interfaccia secondaria è l'interfaccia fisica 
seguita da un punto e un numero di sottointerfaccia. Anche se non richiesto, è consuetudine 
abbinare il numero di sottointerfaccia con il numero VLAN.
Ogni sottointerfaccia viene quindi configurata con i seguenti due comandi:
• encapsulation dot1q vlan_id [native] - Questo comando configura la sottointerfaccia per 
rispondere al traffico incapsulato 802.1Q dal file specificato vlan-id. L'opzione parola 
chiave native viene aggiunta solo per impostare la VLAN nativa su qualcosa di diverso da 
VLAN 1.
• ip addressip-address subnet-mask - Questo comando configura l'indirizzo IPv4 della 
sottointerfaccia. Questo indirizzo in genere funge da gateway predefinito per la VLAN 
identificata.
Ripetere il processo per ogni VLAN da instradare. A ogni sottointerfaccia del router deve essere 
assegnato un indirizzo IP su una subnet univoca affinché si verifichi il routing. Quando tutte le 
subinterfacce sono state create, abilitare l'interfaccia fisica utilizzando il comando di 
configurazione dell'interfaccia no shutdown. Se l'interfaccia fisica è disabilitata, tutte le 
sottointerfacce sono disabilitate.

14
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-on-a-stick
Configurazione sottointerfaccia R1 (seguito)
Nella configurazione, le 
subinterfacce R1 G0/0/1 sono 
configurate per VLAN 10, 20 e 
99.


15
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Router-on-a-stick Inter-VLAN Routing
Verifica della connettività tra PC1 e PC2
La configurazione del router-on-a-stick è 
completa dopo che il trunk switch e le 
subinterfacce del router sono state configurate. 
La configurazione può essere verificata da 
host, router e switch.
Da un host, verificare la connettività a un host 
in un'altra VLAN utilizzando il comando ping. È 
una buona idea verificare prima la 
configurazione IP dell'host corrente utilizzando 
il comando host di Windows ipconfig.
Quindi, utilizzare ping per verificare la 
connettività con PC2 e S1, come mostrato 
nella figura. L'output ping conferma con 
successo il routing inter-VLAN in funzione.


16
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN router-on-a-stick
Verifica del routing inter-VLAN di router-on-a-stick
Oltre all'utilizzo del ping tra dispositivi, è possibile utilizzare i seguenti comandi 
show per verificare e risolvere i problemi della configurazione del router-on-a-
stick.
• show ip route
• show ip interface brief
• show interfaces
• show interfaces trunk

17
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN 
utilizzando Switch Layer 3

18
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Switch Layer 3 di routing inter-VLAN
Il routing inter-VLAN che utilizza il metodo router-on-a-stick è semplice da implementare per 
un'organizzazione di piccole e medie dimensioni. Tuttavia, una grande azienda richiede un 
metodo più veloce e molto più scalabile per fornire il routing inter-VLAN.
Le LAN del campus aziendale utilizzano switch Layer 3 per fornire il routing inter-VLAN. Gli 
switch Layer 3 utilizzano la commutazione basata su hardware per ottenere velocità di 
elaborazione dei pacchetti superiori rispetto ai router. Gli switch Layer 3 sono comunemente 
implementati anche negli armadi di cablaggio a livello di distribuzione aziendale.
Le funzionalità di uno switch Layer 3 includono la possibilità di eseguire le seguenti operazioni:
• Instradare da una VLAN all'altra utilizzando più interfacce virtuali commutate (SVIS).
• Convertire un switchport Layer 2 in un'interfaccia Layer 3 (cioè una porta instradata). Una 
porta instradata è simile a un'interfaccia fisica su un router Cisco IOS.
• Per fornire il routing inter-VLAN, gli switch Layer 3 utilizzano gli SVI. Gli SVI sono 
configurati utilizzando lo stesso comando interface vlan vlan-id utilizzato per creare l'SVI 
di gestione su uno switch Layer 2. È necessario creare un SVI Layer 3 per ciascuna delle 
VLAN instradabili.

19
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Scenario di switch Layer 3
Nella figura, lo switch Layer 
3, D1, è collegato a due host 
su diverse VLAN. PC1 è in 
VLAN 10 e PC2 è in VLAN 
20, come mostrato. Lo switch 
Layer 3 fornirà servizi di 
routing inter-VLAN ai due 
host.


20
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Configurazione di switch Layer 3
Per configurare S1 con VLAN e trunking, completare i 
passaggi seguenti:
• Passo 1. Creare le VLAN. Nell'esempio vengono 
utilizzati VLAN 10 e 20. 
• Passo 2. Creare le interfacce VLAN SVI. L'indirizzo IP 
configurato fungerà da gateway predefinito per gli host 
nella rispettiva VLAN. 
• Passo 3. Configurare le porte di accesso. Assegnare la 
porta appropriata alla VLAN richiesta. 
• Passo 4. Abilitare il routing IP. Eseguire il comando di 
configurazione globale routing ip per consentire lo 
scambio di traffico tra VLAN 10 e 20. Questo comando 
deve essere configurato per abilitare il routing inter-VLAN 
su uno switch Layer 3 per IPv4.


21
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Verifica di switch Layer 3 di routing inter-VLAN
Il routing inter-VLAN utilizzando uno switch Layer 3 è più semplice da configurare rispetto 
al metodo router-on-a-stick. Al termine della configurazione, la configurazione può essere 
verificata verificando la connettività tra gli host.
• Da un host, verificare la connettività a un host in un'altra VLAN utilizzando il comando 
ping. È una buona idea verificare prima la configurazione IP dell'host corrente 
utilizzando il comando host di Windows ipconfig.
• Successivamente, verificare la connettività con PC2 utilizzando il comando host di 
Windows ping. L'uscita ping riuscita conferma che il routing inter-VLAN è operativo.

22
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Routing su switch Layer 3
Se le VLAN devono essere raggiungibili da altri dispositivi di Layer 3, devono essere 
pubblicizzate utilizzando routing statico o dinamico. Per abilitare il routing su uno switch di 
Layer 3, è necessario configurare una porta instradata.
Una porta instradata viene creata su uno switch di Layer 3 disabilitando la funzione 
switchport su una porta di Layer 2 collegata a un altro dispositivo di Layer 3. In 
particolare, la configurazione del comando di configurazione dell'interfaccia no 
switchport su una porta di Layer 2 lo converte in un'interfaccia di Layer 3. Quindi 
l'interfaccia può essere configurata con una configurazione IPv4 per connettersi a un 
router o a un altro switch Layer 3.

23
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Scenario di routing su switch Layer 3
Nella figura, lo switch D1 Layer 3 configurato in 
precedenza è ora collegato a R1. R1 e D1 sono 
entrambi in un dominio del protocollo di routing 
OSPF (Open Shortest Path First). Supponiamo 
che Inter-VLAN sia stato implementato con 
successo su D1. Anche l'interfaccia G0/0/1 di R1 
è stata configurata e abilitata. Inoltre, R1 utilizza 
OSPF per pubblicizzare le sue due reti, 
10.10.10.0/24 e 10.20.20.0/24.
Nota: La configurazione di routing OSPF è 
trattata in un altro corso. In questo modulo, i 
comandi di configurazione OSPF saranno forniti a 
voi in tutte le attività e valutazioni. Non è 
necessario comprendere la configurazione per 
abilitare il routing OSPF sullo switch Layer 3.


24
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Routing inter-VLAN utilizzando Layer 3 Switch
Configurazione routing su switch Layer 3
Completare i passaggi seguenti per configurare D1 per l'instradamento con R1:
• Passo 1. Configurare la porta instradata. Utilizzare il comando no switchport per convertire la 
porta in una porta instradata, quindi assegnare un indirizzo IP e una subnet mask. Attivare la porta.
• Passo 2. Abilitare il routing. Utilizzare il comando di configurazione globale ip routing per abilitare 
il routing.
• Passo 3. Configurare il routing. Utilizzare un metodo di routing appropriato. In questo esempio, è 
configurato Single-Area OSPFv2
• Passo 4. Verificare il routing. Usare il comando show ip route .
• Passo 5. Verificare la connettività. Utilizzare il comando ping per verificare la raggiungibilità.

25
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risoluzione dei problemi 
relativi al routing inter-VLAN

26
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risoluzione dei problemi relativi al routing inter-VLAN
Problemi comuni in inter-VLAN
Ci sono una serie di motivi per cui una configurazione inter-VLAN potrebbe non funzionare. Tutti sono 
legati a problemi di connettività. Innanzitutto, controllare il layer fisico per risolvere eventuali problemi in 
cui un cavo potrebbe essere collegato alla porta errata. Se le connessioni sono corrette, utilizzare 
l'elenco nella tabella per altri motivi comuni per cui la connettività tra VLAN potrebbe non riuscire.
Tipo di problema Come risolvere il problema Come verificare
VLAN mancanti
•Creare (o ricreare) la VLAN se non esiste.
•Assicurarsi che la porta host sia assegnata alla VLAN 
corretta.
show vlan [brief]
show interfaces switchport
ping
Cambiare i problemi della 
porta del trunk
•Assicurarsi che i trunk siano configurati correttamente.
•Assicurarsi che la porta sia una porta trunk e abilitata.
show interface trunk
show running-config
Cambiare i problemi della 
porta di accesso
•Assegnare VLAN corretta alla porta di accesso.
•Assicurarsi che la porta sia una porta di accesso e 
abilitata.
•Host non è configurato correttamente nella subnet 
errata.
show interfaces switchport
show running-config interface
ipconfig
Problemi di configurazione 
del router
•L'indirizzo IPv4 della sottointerfaccia del router è 
configurato in modo errato.
•La sottointerfaccia del router viene assegnata all'ID 
VLAN.
show ip interface brief
show interfaces

27
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risoluzione dei problemi relativi al routing inter-VLAN
Scenario di risoluzione dei problemi relativi al routing inter-
VLAN
Esempi di alcuni di questi problemi di routing 
inter-VLAN saranno ora trattati in modo più 
dettagliato. Questa topologia verrà utilizzata 
per tutti questi problemi.
Router R1 Sottointerfacce
Sottointerfac
cia VLAN Indirizzo IP
G0/0/0.10 10 192.168.10.1/24
G0/0/0.20 20 192.168.20.1/24
G0/0/0.30 99 192.168.99.1/24


28
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risoluzione dei problemi relativi al routing inter-VLAN
VLAN mancanti
Un problema di connettività tra VLAN potrebbe 
essere causato da una VLAN mancante. La 
VLAN potrebbe mancare se non è stata creata, 
è stata cancellata accidentalmente o non è 
consentita sul collegamento trunk.
Quando una VLAN viene eliminata, tutte le 
porte assegnate a tale VLAN diventano inattive. 
Rimangono associati alla VLAN (e quindi 
inattivi) finché non vengono assegnate a una 
nuova VLAN o ricreate la VLAN mancante. 
Ricreare la VLAN mancante riassegnerà 
automaticamente gli host.
Utilizzare il comando show interface interface-
id switchport per verificare l'appartenenza 
VLAN della porta.


29
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risoluzione dei problemi relativi al routing inter-VLAN
Problemi switch porte trunk
Un altro problema per il routing tra VLAN include le porte switch configurate in modo errato. 
In una soluzione inter-VLAN legacy, questo potrebbe essere causato quando la porta del 
router di connessione non viene assegnata alla VLAN corretta.
Tuttavia, con una soluzione router-on-a-stick, la causa più comune è una porta trunk 
configurata in modo errato.
• Verificare che la porta che si connette al router sia configurata correttamente come 
collegamento trunk utilizzando il comando show interface trunk.
• Se tale porta è mancante dall'output, esaminare la configurazione della porta con il 
comando show running-config interface X per vedere come è configurata la porta.


30
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risoluzione dei problemi relativi al routing inter-VLAN
Problemi di accesso alle porte switch
Quando si sospetta un problema con una 
configurazione della porta di accesso switch, 
utilizzare i comandi di verifica per esaminare la 
configurazione e identificare il problema.
Un indicatore comune di questo problema è il 
PC con la configurazione corretta dell'indirizzo 
(indirizzo IP, subnet mask, gateway 
predefinito), ma non è in grado di eseguire il 
ping del gateway predefinito.
• Utilizzare il comando show vlan brief, 
show interface X switchport o show 
running-config interface interface X per 
verificare l'assegnazione dell'interfaccia 
VLAN.


31
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Risolvere i problemi comuni di configurazione tra VLAN
Problemi di configurazione router
I problemi di configurazione del router-on-a-stick sono solitamente correlati a 
configurazioni errate della subinterfaccia.
• Verificare lo stato dell'interfaccia secondaria utilizzando il comando show ip interface 
brief. 
• Verificare quali VLAN ciascuna delle sottointerfacce è presente. Per fare ciò, il 
comando show interfaces è utile ma genera una grande quantità di output non 
richiesto aggiuntivo. L'output dei comandi può essere ridotto utilizzando i filtri dei 
comandi IOS. In questo esempio, utilizzare la parola chiave include per identificare 
che solo le righe contenenti le lettere "Gig" o "802.1Q"


32
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
4.5 Quiz e pratica

33
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Cosa ho appreso in questo modulo? 
• Il routing inter-VLAN è il processo di inoltro del traffico di rete da una VLAN a un'altra VLAN. 
• Tre opzioni includono legacy, router-on-a-stick e Layer 3 switch utilizzando SVI. 
• Per configurare uno switch con VLAN e trunking, completare la procedura seguente: creare e assegnare 
un nome alle VLAN, creare l'interfaccia di gestione, configurare le porte di accesso e configurare le porte di 
trunking. 
• Il metodo router-on-a-stick richiede la creazione di una sottointerfaccia per ogni VLAN da instradare. Una 
sottointerfaccia viene creata utilizzando il comando di modalità di configurazione globale interface_id 
subinterface_id . 
• A ogni sottointerfaccia del router deve essere assegnato un indirizzo IP su una subnet univoca affinché si 
verifichi il routing. Quando tutte le subinterfacce sono state create, l'interfaccia fisica deve essere abilitata 
utilizzando il comando di configurazione dell'interfaccia no shutdown. 
• Le LAN del campus aziendale utilizzano switch Layer 3 per fornire il routing inter-VLAN. Gli switch Layer 3 
utilizzano la commutazione basata su hardware per ottenere velocità di elaborazione dei pacchetti 
superiori rispetto ai router. 
• Le funzionalità di uno switch Layer 3 includono il routing da una VLAN all'altra utilizzando più interfacce 
virtuali commutate (SVI) e la conversione di una commutazione Layer 2 in un'interfaccia Layer 3 (ad 
esempio, una porta instradata). 
• Per fornire il routing inter-VLAN, gli switch Layer 3 utilizzano gli SVI. Gli SVI sono configurati utilizzando lo 
stesso comando interface vlan vlan-id utilizzato per creare la gestione SVI su uno switch Layer 2. 

34
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Cosa ho appreso in questo modulo? (seguito)
• Per configurare uno switch con VLANS e trunking, completare la procedura seguente: creare il VLANS, 
creare le interfacce VLAN SVI, configurare le porte di accesso e abilitare il routing IP. 
• Per abilitare il routing su uno switch di Layer 3, è necessario configurare una porta instradata. Una porta 
instradata viene creata su uno switch di Layer 3 disabilitando la funzione switchport su una porta di Layer 2 
collegata a un altro dispositivo di Layer 3. L'interfaccia può essere configurata con una configurazione IPv4 
per connettersi a un router o a un altro switch Layer 3. 
• Per configurare uno switch di Layer 3 per l'instradamento con un router, attenersi alla seguente procedura: 
configurare la porta instradata, abilitare il routing, configurare il routing, verificare il routing e verificare la 
connettività.
• Ci sono una serie di motivi per cui una configurazione inter-VLAN potrebbe non funzionare. Tutti sono 
correlati a problemi di connettività come VLAN mancanti, problemi di porta trunk switch, problemi di porta 
di accesso switch e problemi di configurazione del router. 
• Una VLAN potrebbe mancare se non è stata creata, è stata eliminata accidentalmente o non è consentita 
sul collegamento trunk. 
• Un altro problema per il routing tra VLAN include le porte switch configurate in modo errato. 
• In una soluzione inter-VLAN legacy, una porta switch configurata in modo errato potrebbe essere causata 
quando la porta del router di connessione non è assegnata alla VLAN corretta. 

35
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Cosa ho appreso in questo modulo? (seguito)
• Con una soluzione router-on-a-stick, la causa più comune è una porta trunk configurata in modo errato. 
• Quando si sospetta un problema con una configurazione della porta di accesso switch, utilizzareping e 
show interfaces interface-id switchport per identificare il problema. 
• I problemi di configurazione del router con configurazioni router-on-a-stick sono solitamente correlati a 
configurazioni errate della subinterfaccia. Verificare lo stato dell'interfaccia secondaria utilizzando il 
comando show ip interface brief.

36
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Modulo 4: Configurazione di base del dispositivo
Nuovi termini e comandi
▪ Routing inter-VLAN
▪ Router-on-a-stick
▪ encapsulation dot1q X [ native ]
▪ no switchport
▪ router ospf
▪ ip routing


---

# Lab - Identifying IPv4 Addresses

**File:** `Lab - Identifying IPv4 Addresses.pdf`
**Tipo:** `.pdf`
**Dimensione:** 610.8 KB
**Ultima modifica:** 02/07/2026 09:24

---

 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 1 di 3 
Laboratorio: Individuazione degli indirizzi IPv4  
Obiettivi 
Sezione 1: Individuare gli indirizzi IPv4 
Sezione 2: Classificare gli indirizzi IPv4 
Introduzione e scenario 
In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4). 
Si identificheranno i diversi tipi di indirizzi IPv4 e i componenti che formano l'indirizzo, come la porzione rete e 
dell'host, nonché la subnet mask. I tipi di indirizzi analizzati includono quelli pubblici, privati, unicast e 
multicast. 
Risorse necessarie 
• Dispositivo con accesso a Internet 
• Facoltativo: calcolatore degli indirizzi IPv4 
Sezione 1: Individuare gli indirizzi IPv4 
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
Indirizzo 
IP/prefisso 
Rete/host 
N, n = rete, H, h = host Subnet mask Indirizzo di rete 
192.168.10.10/24 N.N.N.H 255.255.255.0 192.168.10.0 
10.101.99.17/23 N.N.nnnnnnnh.H 255.255.254.0 10.101.98.0 
209.165.200.227/27    
172.31.45.252/24    
10.1.8.200/26    
172.16.117.77/20    
10.1.1.101/25    
209.165.202.140/27    
192.168.28.45/28    
 

Laboratorio: Individuazione degli indirizzi IPv4 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 2 di 3 
Fase 2: Analizzare la tabella seguente ed elencare l'intervallo degli indirizzi host e di broadcast 
sulla base di una coppia rete/maschera del prefisso. 
Le prima riga mostra un esempio di come completare la tabella. 
Indirizzo 
IP/prefisso 
Indirizzo del primo 
host 
Indirizzo dell'ultimo 
host Indirizzo di broadcast 
192.168.10.10/24 192.168.10.1 192.168.10.254 192.168.10.255 
10.101.99.17/23    
209.165.200.227/27    
172.31.45.252/24    
10.1.8.200/26    
172.16.117.77/20    
10.1.1.101/25    
209.165.202.140/27    
192.168.28.45/28    
Sezione 2: Classificare gli indirizzi IPv4 
Nella Sezione 2 si identificheranno e classificheranno diversi esempi di indirizzi IPv4. 
Fase 1: Analizzare la tabella riportata di seguito e identificare il tipo di indirizzo (rete, host, 
multicast o indirizzo di broadcast). 
Le prima riga mostra un esempio di come completare la tabella. 
Indirizzo IP Subnet mask Tipo di indirizzo 
10.1.1.1 255.255.255.252 host 
192.168.33.63 255.255.255.192  
239.192.1.100 255.252.0.0  
172.25.12.52 255.255.255.0  
10.255.0.0 255.0.0.0  
172.16.128.48 255.255.255.240  
209.165.202.159 255.255.255.224  
172.16.0.255 255.255.0.0  
224.10.1.11 255.255.255.0  
 
 
 

Laboratorio: Individuazione degli indirizzi IPv4 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 3 di 3 
Fase 2: Analizzare la tabella riportata di seguito e identificare l'indirizzo come pubblico o 
privato. 
Indirizzo IP/prefisso Pubblico o privato 
209.165.201.30/27  
192.168.255.253/24  
10.100.11.103/16  
172.30.1.100/28  
192.31.7.11/24  
172.20.18.150/22  
128.107.10.1/16  
192.135.250.10/24  
64.104.0.11/16  
Fase 3: Analizzare la tabella riportata di seguito e identificare se la coppia indirizzo/prefisso è 
un indirizzo dell'host valido. 
Indirizzo 
IP/prefisso 
Indirizzo dell'host 
valido? Motivo 
127.1.0.10/24   
172.16.255.0/16   
241.19.10.100/24   
192.168.0.254/24   
192.31.7.255/24   
64.102.255.255/14   
224.0.0.5/16   
10.0.255.255/8   
198.133.219.8/24   
Approfondimento 
Perché dovremmo continuare a studiare l'indirizzamento IPv4 se lo spazio degli indirizzi IPv4 disponibile è 
vuoto? 
_____________________________________________________________________________________ 
_____________________________________________________________________________________ 


---

# LAB configure-router-on-a-stick-inter-vlan-routing

**File:** `LAB configure-router-on-a-stick-inter-vlan-routing.pdf`
**Tipo:** `.pdf`
**Dimensione:** 189.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

 
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public Page 1 of 5 www.netacad.com 
Lab - Configure Router-on-a-Stick Inter-VLAN Routing 
Topology 
 
Addressing Table 
Device Interface  IP Address Subnet Mask Default Gateway  
R1 G0/0/1.3 192.168.3.1 255.255.255.0 N/A 
R1 
G0/0/1.4 192.168.4.1 255.255.255.0 
N/A 
R1 
G0/0/1.8 N/A N/A 
N/A 
S1 VLAN 3 192.168.3.11 255.255.255.0 192.168.3.1 
S2 VLAN 3 192.168.3.12 255.255.255.0 192.168.3.1 
PC-A NIC 192.168.3.3 255.255.255.0 192.168.3.1 
PC-B NIC 192.168.4.3 255.255.255.0 192.168.4.1 
VLAN Table 
VLAN Name Interface Assigned 
3 Management 
S1: VLAN 3 
S2: VLAN 3 
S1: F0/6 
4 Operations S2: F0/18 
7 ParkingLot 
S1: F0/2-4, F0/7-24, G0/1-2  
S2: F0/2-17, F0/19-24, G0/1 -2  
8 Native N/A 


Lab - Configure Router-on-a-Stick Inter -VLAN Routing 
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public Page 2 of 5 www.netacad.com 
Objectives 
Part 1: Build the Network and Configure Basic Device Settings 
Part 2: Create VLANs and Assign Switch Ports  
Part 3: Configure an 802.1Q Trunk between the Switches  
Part 4: Configure Inter -VLAN Routing on the Router  
Part 5: Verify Inter -VLAN Routing is working  
Background / Scenario 
Modern switches use virtual local -area networks (VLANs) to provide segmentation services traditionally 
provided by routers in LAN configurations. VLANs address scalability, security, and network management.  In 
general, VLANs make it easier to design a netw ork to support the goals of an organization. Communication 
between VLANs requires a device operating at Layer 3 of the OSI model. Routers in VLAN topologies provide 
additional security and traffic flow management.  
VLAN trunks are used to span VLANs across multiple devices. Trunks allow the traffic from multiple VLANS to 
travel over a single link, while keeping the VLAN identification and segmentation intact. A particular kind of 
inter-VLAN routing, called “Router -On-A-Stick”, uses a trunk from the router to  the switch to enable all VLANs 
to pass to the router.  
In this lab, you will create VLANs on both switches in the topology, assign VLANs to switch access ports, 
verify that VLANs are working as expected, create VLAN trunks between the two switches and betw een S1 
and R1, and configure Inter -VLAN routing on R1 to allow hosts in different VLANs to communicate, regardless 
of which subnet the host resides.  
Note: The routers used with CCNA hands -on labs are Cisco 4221 with Cisco IOS XE Release 16.9.4 
(universalk9 image). The switches used in the labs are Cisco Catalyst 2960s with Cisco IOS Release 15.2(2) 
(lanbasek9 image). Other routers, switches, and Cisco IOS versions can be used . Depending on the model  
and Cisco IOS version, the commands available and the output produced might vary from what is shown in 
the labs. Refer to the Router Interface Summary T able at the end of the lab for the correct interface identifiers. 
Note: Ensure that the routers and switches have been erased and have no startup configurations. If you are 
unsure, contact your instructor.  
Required Resources 
• 1 Router (Cisc o 4221 with Cisco IOS XE Release 16.9.4 universal image or comparable)  
• 2 Switches (Cisco 2960 with Cisco IOS Release 15.2(2) lanbasek9 image or comparable)  
• 2 PCs (Windows with a terminal emulation program, such as Tera Term)  
• Console cables to co nfigure the Cisco IOS devices via the console ports  
• Ethernet cables as shown in the topology  
Instructions 
Part 1: Build the Network and Configure Basic Device Settings 
In Part 1, you will set up the network topology and configure basic settings on the PC hosts and switches.  
Step 1: Cable the network as shown in the topology. 
Attach the devices as shown in the topology diagram, and cable as necessary.  

Lab - Configure Router-on-a-Stick Inter -VLAN Routing 
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public Page 3 of 5 www.netacad.com 
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
Note: Use the question mark ( ?) to help with the correct sequence of parameters needed to execute th is 
command. 
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
Note: Use the question mark ( ?) to help with the correct sequence of parameters needed to ex ecute this 
command. 
k. Copy the running configuration to the startup configuration.  
Close configuration window 
Step 4: Configure PC hosts. 
Refer to the Addressing Table for PC host address information.  
Part 2: Create VLANs and Assign Switch Ports 
In Part 2, you will create VLANs, as specified in the table above, on both switches. You will then assign the 
VLANs to the appropriate interface. The show vlan  command is used to verify your configuration settings. 
Complete the following tasks on each switch.  

Lab - Configure Router-on-a-Stick Inter -VLAN Routing 
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public Page 4 of 5 www.netacad.com 
Step 1: Create VLANs on both switches. 
Open configuration window 
a. Create and name the required VLANs on each switch from the table above.  
b. Configure the management i nterface and default gateway on each switch using the IP address 
information in the Addressing Table.  
c. Assign all unused ports on both switches to the ParkingLot VLAN, configure them for static access mode, 
and administratively deactivate them.  
Note: The i nterface range command is helpful to accomplish this task with as few commands as 
necessary. 
Step 2: Assign VLANs to the correct switch interfaces. 
a. Assign used ports to the appropriate VLAN (specified in the VLAN table above) and configure them for 
static access m ode. Be sure to do this on both switches  
b. Issue the show vlan  brief command and verify that the VLANs are assigned to the correct interfaces.  
Close configuration window 
Part 3: Configure an 802.1Q Trunk Between the Switches 
In Part 3, you will manually configure in terface F0/1 as a trunk.  
Step 1: Manually configure trunk interface F0/1. 
Open configuration window 
a. Change the switchport mode on interface F0/1 to force trunking. Make sure to do this on both switches.  
b. As a part of the trunk configuration, set the native VLAN to 8 on both switches. You may see error 
messages temporarily while the two interfaces are configured for different native VLANs.  
c. As another part of trunk configuration, specify that VLANs 3, 4, and 8 are only allowed to cross the trunk.  
d. Issue the show interfaces trunk command to verify trunking ports, the Native VLAN and allowed VLANs 
across the trunk.  
Step 2: Manually configure S1’s trunk interface F0/5 
a. Configure the F0/5 on S1 with the same trunk parameters as F0/1. This is the trunk to the router.  
b. Save the running configuration to the startup configuration file on S1 and S2.  
c. Issue the show interfaces trunk command to verify trunking.  
Question: 
Why does F0/5 not appear in the list of trunks?  
Type your answers here.  
Close configuration window 
Part 4: Configure Inter-VLAN Routing on the Router 
Open configuration window 
a. Activate interface G0/0/1 on the router.  
b. Configure sub -interfaces for each VLAN as specified in the IP addressing table. All sub -interfaces use 
802.1Q encapsulation. Ensure the sub -interface for the nativ e VLAN does not have an IP address 
assigned. Include a description for each sub -interface. 
c. Use the show ip interface brief  command to verify the sub -interfaces are operational.  
Close configuration window 

Lab - Configure Router-on-a-Stick Inter -VLAN Routing 
© 2013 - 2019 Cisco and/or its affiliates. All rights reserved. Cisco Public Page 5 of 5 www.netacad.com 
Part 5: Verify Inter-VLAN Routing is Working 
Step 1: Complete the following tests from PC-A. All should be successful. 
Note: You may have to disable the PC firewall for pings to be successful.  
a. Ping from PC -A to its default gateway.  
b. Ping from PC -A to PC-B 
c. Ping from PC -A to S2 
Step 2: Complete the following test from PC-B. 
From the command prompt on PC -B, issue the tracert command to the address of PC -A. 
Question: 
What intermediate IP addresses are shown in the results?  
Type your answers here.  
Router Interface Summary Table 
Router Model  Ethernet Interface #1  Ethernet Interface #2 Serial Interface #1  Serial Interface #2  
1800 
Fast Ethernet 0/0 
(F0/0) 
Fast Ethernet 0/1 
(F0/1) Serial 0/0/0 (S0/0/0) Serial 0/0/1 (S0/0/1) 
1900 
Gigabit Ethernet 0/0 
(G0/0) 
Gigabit Ethernet 0/1 
(G0/1) Serial 0/0/0 (S0/0/0) Serial 0/0/1 (S0/0/1) 
2801 
Fast Ethernet 0/0 
(F0/0) 
Fast Ethernet 0/1 
(F0/1) Serial 0/1/0 (S0/1/0) Serial 0/1/1 (S0/1/1) 
2811 
Fast Ethernet 0/0 
(F0/0) 
Fast Ethernet 0/1 
(F0/1) Serial 0/0/0 (S0/0/0) Serial 0/0/1 (S0/0/1) 
2900 
Gigabit Ethernet 0/0 
(G0/0) 
Gigabit Ethernet 0/1 
(G0/1) Serial 0/0/0 (S0/0/0) Serial 0/0/1 (S0/0/1) 
4221 
Gigabit Ethernet 0/0 /0 
(G0/0/0) 
Gigabit Ethernet 0/0 /1 
(G0/0/1) Serial 0/1/0 (S0/1/0) Serial 0/1/1 (S0/1/1) 
4300 
Gigabit Ethernet 0/0 /0 
(G0/0/0) 
Gigabit Ethernet 0/0 /1 
(G0/0/1) Serial 0/1/0 (S0/1/0) Serial 0/1/1 (S0/1/1) 
Note: To find out how the router is configured, look at the interfaces to identify the type of router and how many 
interfaces the router has. There is no way to effectively list all the combinations of configura tions for each router 
class. This table includes identifiers for the possible combinations of Ethernet and Serial interfaces in the device. 
The table does not include any other type of interface, even though a specific router may contain one. An 
example of this might be an ISDN BRI interface. The string in parenthesis is the legal abbreviation that can be 
used in Cisco IOS commands to represent the interface.  
End of Document 


---

# Script demo entropia

**File:** `Script demo entropia.py`
**Tipo:** `.py`
**Dimensione:** 7.5 KB
**Ultima modifica:** 02/07/2026 09:25

---

import os
import random
import zlib
import gzip
import bz2
import lzma
import math
from collections import Counter
import time

def calculate_entropy(data):
    """Calcola l'entropia di Shannon di una sequenza di dati"""
    if not data:
        return 0
    
    # Conta la frequenza di ogni byte
    counter = Counter(data)
    length = len(data)
    
    # Calcola l'entropia
    entropy = 0
    for count in counter.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
    
    return entropy

def theoretical_min_size(entropy, data_size):
    """Calcola la dimensione minima teorica in base all'entropia"""
    return (entropy * data_size) / 8  # in bytes

def create_files():
    """Crea i due file di test da 1MB ciascuno"""
    print("🔧 Creazione dei file di test...")
    
    # File 1: Solo lettere 'a' (1MB)
    file1_name = "file_solo_a.txt"
    with open(file1_name, 'w', encoding='utf-8') as f:
        # 1MB = 1,048,576 bytes
        f.write('a' * 1048576)
    
    # File 2: Caratteri ASCII casuali (1MB)
    file2_name = "file_ascii_random.txt"
    with open(file2_name, 'w', encoding='utf-8') as f:
        # Genera caratteri ASCII casuali (32-126)
        random_chars = ''.join(chr(random.randint(32, 126)) for _ in range(1048576))
        f.write(random_chars)
    
    print(f"✅ Creati {file1_name} e {file2_name}")
    return file1_name, file2_name

def compress_file(filename, method='gzip'):
    """Comprime un file usando l'algoritmo specificato"""
    with open(filename, 'rb') as f:
        data = f.read()
    
    if method == 'gzip':
        compressed = gzip.compress(data, compresslevel=9)
        suffix = '.gz'
    elif method == 'bz2':
        compressed = bz2.compress(data, compresslevel=9)
        suffix = '.bz2'
    elif method == 'lzma':
        compressed = lzma.compress(data, preset=9)
        suffix = '.xz'
    elif method == 'zlib':
        compressed = zlib.compress(data, level=9)
        suffix = '.zlib'
    
    compressed_filename = f"{filename}_{method}{suffix}"
    with open(compressed_filename, 'wb') as f:
        f.write(compressed)
    
    return compressed_filename, len(compressed)

def analyze_file(filename):
    """Analizza un file calcolando entropia e statistiche"""
    with open(filename, 'rb') as f:
        data = f.read()
    
    size = len(data)
    entropy = calculate_entropy(data)
    min_theoretical_size = theoretical_min_size(entropy, size)
    
    # Conta caratteri unici
    unique_chars = len(set(data))
    
    return {
        'size': size,
        'entropy': entropy,
        'min_theoretical_size': min_theoretical_size,
        'unique_chars': unique_chars,
        'data': data
    }

def print_separator():
    print("=" * 80)

def print_header(title):
    print(f"\n{'=' * 20} {title} {'=' * 20}")

def main():
    print("🎯 ANALISI PRATICA DI ENTROPIA E COMPRESSIONE")
    print("Questo script dimostra empiricamente i limiti teorici della compressione")
    print_separator()
    
    # Crea i file
    file1, file2 = create_files()
    
    # Analizza i file originali
    print_header("ANALISI DEI FILE ORIGINALI")
    
    print("\n📊 FILE 1 - Solo lettere 'a':")
    analysis1 = analyze_file(file1)
    print(f"   Dimensione: {analysis1['size']:,} bytes (1MB)")
    print(f"   Entropia: {analysis1['entropy']:.6f} bit per simbolo")
    print(f"   Caratteri unici: {analysis1['unique_chars']}")
    print(f"   Dimensione minima teorica: {analysis1['min_theoretical_size']:.2f} bytes")
    print(f"   💡 Spiegazione: Un file con solo 'a' ha entropia quasi 0!")
    print(f"      Questo significa che contiene pochissima informazione reale.")
    
    print("\n📊 FILE 2 - ASCII casuali:")
    analysis2 = analyze_file(file2)
    print(f"   Dimensione: {analysis2['size']:,} bytes (1MB)")
    print(f"   Entropia: {analysis2['entropy']:.6f} bit per simbolo")
    print(f"   Caratteri unici: {analysis2['unique_chars']}")
    print(f"   Dimensione minima teorica: {analysis2['min_theoretical_size']:.2f} bytes")
    print(f"   💡 Spiegazione: Caratteri casuali hanno alta entropia!")
    print(f"      Contengono molta informazione e sono difficili da comprimere.")
    
    # Compressione
    print_header("COMPRESSIONE CON DIVERSI ALGORITMI")
    
    algorithms = ['gzip', 'bz2', 'lzma', 'zlib']
    
    for file_name, analysis, file_desc in [(file1, analysis1, "Solo 'a'"), 
                                          (file2, analysis2, "ASCII casuali")]:
        print(f"\n🗜️  COMPRESSIONE: {file_desc}")
        print(f"   File originale: {file_name}")
        
        for algo in algorithms:
            start_time = time.time()
            compressed_file, compressed_size = compress_file(file_name, algo)
            compress_time = time.time() - start_time
            
            compression_ratio = analysis['size'] / compressed_size
            space_saved = analysis['size'] - compressed_size
            percentage_saved = (space_saved / analysis['size']) * 100
            
            print(f"\n   📁 {algo.upper()}:")
            print(f"      File compresso: {compressed_file}")
            print(f"      Dimensione: {compressed_size:,} bytes")
            print(f"      Rapporto compressione: {compression_ratio:.2f}:1")
            print(f"      Spazio risparmiato: {space_saved:,} bytes ({percentage_saved:.1f}%)")
            print(f"      Tempo compressione: {compress_time:.3f} secondi")
            
            # Confronto con il limite teorico
            if analysis['min_theoretical_size'] > 0:
                efficiency = analysis['min_theoretical_size'] / compressed_size * 100
                print(f"      Efficienza vs limite teorico: {efficiency:.1f}%")
    
    # Analisi teorica finale
    print_header("ANALISI TEORICA E CONCLUSIONI")
    
    print("\n🧠 TEORIA DELL'INFORMAZIONE:")
    print("   • L'ENTROPIA misura la quantità di informazione in un messaggio")
    print("   • Più alta è l'entropia, più informazione c'è da rappresentare")
    print("   • Il LIMITE DI SHANNON stabilisce il limite teorico di compressione")
    print("   • Nessun algoritmo può comprimere oltre questo limite senza perdere informazione")
    
    print(f"\n📈 RISULTATI EMPIRICI:")
    print(f"   • File con solo 'a': Entropia ≈ {analysis1['entropy']:.4f} bit/simbolo")
    print(f"     → Comprimibile quasi al 100% (pochissima informazione reale)")
    print(f"   • File casuale: Entropia ≈ {analysis2['entropy']:.4f} bit/simbolo")
    print(f"     → Difficile da comprimere (molta informazione reale)")
    
    print(f"\n🎯 CONCLUSIONI PRATICHE:")
    print(f"   • Dati ripetitivi (bassa entropia) = alta compressibilità")
    print(f"   • Dati casuali (alta entropia) = bassa compressibilità")
    print(f"   • Gli algoritmi di compressione cercano pattern per ridurre la ridondanza")
    print(f"   • Il limite teorico di Shannon è raramente raggiunto in pratica")
    
    print(f"\n🔍 APPLICAZIONI REALI:")
    print(f"   • File di testo: Spesso comprimibili (linguaggio ha pattern)")
    print(f"   • Immagini JPEG: Già compresse, difficili da comprimere ulteriormente")
    print(f"   • File eseguibili: Moderatamente comprimibili")
    print(f"   • Dati crittografati: Quasi incomprimibili (sembrano casuali)")
    
    print_separator()
    print("✅ ANALISI COMPLETATA!")
    print("I file compressi sono stati salvati nella directory corrente.")
    
    # Pulizia opzionale
    print(f"\n🧹 Per pulire i file generati, esegui:")
    print(f"   rm file_solo_a.txt* file_ascii_random.txt*")

if __name__ == "__main__":
    main()



---

# Sistemi Numerici

**File:** `Sistemi Numerici.pdf`
**Tipo:** `.pdf`
**Dimensione:** 236.2 KB
**Ultima modifica:** 02/07/2026 09:28

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
DOCENTE Andrea Blanchietti 
UNITA’ 
FORMATIVA Fondamenti di Reti di Calcolatori 
ARGOMENTO Sistemi numerici – Conversione tra sistemi 
numerici 

Sistema numerico posizionale 
Quando si rappresenta un numero tramite un sistema numerico posizionale, valgono alcune regole 
generali: 
• Si deve definire una base (per esempio, nel sistema decimale la base è 10) 
• Si definisce un insieme di simboli che saranno le cifre nella rappresentazione del numero; i 
simboli andranno sempre da 0 al valore della base – 1 
• Le cifre di un numero avranno un peso in base alla loro posizione nel numero 
• I pesi sono sempre calcolati come potenze della base 
Sistema decimale (numero decimale, base 10) 
• Base = 10  
• Simboli: 0 1 2 3 4 5 6 7 8 9 
• Il valore di un numero decimale è la somma delle potenze di DIECI, ognuna moltiplicata per il 
valore della cifra corrispondente: 
Esempio: 5127 = 5x103 + 1x102 + 2x101 + 7x100  
Sistema binario (numero binario, base 2) 
• Base = 2 
• Simboli 0 e 1 (il numero è rappresentato da una sequenza di 0 e 1) 
• Il valore di un numero binario è dato dalla somma di potenze di DUE, ognuna moltiplicata per il 
valore della cifra corrispondente 
Esempio: 10010110 = 1x27+0x26+0x25+1x24+0x23+1x22+1x21+0x20 
Sistema esadecimale (numero esadecimale, base 16) 
• Base = 16  
• Simboli: 0 1 2 3 4 5 6 7 8 9 A B C D E F 
• Il valore di un numero esadecimale è la somma delle potenze di SEDICI, ognuna moltiplicata 
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
• I resti delle divisioni rappresentano le cifre della rappresentazione in base r; il primo resto (in 
alto) sarà la cifra meno significativa mentre l’ultimo resto (in basso) sarà la cifra più 
significativa. 
Esempio: convertire 89 da decimale a binario  
 Base Resto 
89 2 1 
44 2 0 
22 2 0 
11 2 1 
5 2 1 
2 2 0 
1 2 1 
0   
 
Risultato: 1011001 
 
1011001 

 
Esempio: convertire 31553 da decimale al corrispondente valore esadecimale 
 Base Resto 
31553 16 1 
1972 16 4 
123 16 11 (B) 
7 16 7 
0   
 
Risultato: 7B4116 
 
Conversione da numero esadecimale a binario e viceversa 
• Per passare da esadecimale a binario, ogni cifra di un numero esadecimale genera quattro bit 
Esempio: convertire il numero esadecimale 722416   in binario  
  7  2  2  4 
  0111  0010  0010  0100 
 In binario: 111001000100100 
 
• Per passare da binario a esadecimale, raggruppo i bit a gruppi di quattro partendo da destra 
(bit meno significativo) e aggiungendo zeri a sinistra se necessario 
Esempio: convertire il numero binario 1010111100011 in esadecimale 
 Aggiungiamo tre zeri per avere gruppi da 4 bit: 0001010111100011   
   0001 0101 1110 0011 
   1 5 E 3  
 In esadecimale: 15E316 
 
  
7B4116 

Tabella di conversione esadecimale/binario 
BINARIO ESADECIMALE DECIMALE 
0 0 0 0 0 0 
0 0 0 1 1 1 
0 0 1 0 2 2 
0 0 1 1 3 3 
0 1 0 0 4 4 
0 1 0 1 5 5 
0 1 1 0 6 6 
0 1 1 1 7 7 
1 0 0 0 8 8 
1 0 0 1 9 9 
1 0 1 0 A 10 
1 0 1 1 B 11 
1 1 0 0 C 12 
1 1 0 1 D 13 
1 1 1 0 E 14 
1 1 1 1 F 15 
 
 
Conversione da numero decimale a numero esadecimale passando per la 
rappresentazione nel sistema di numerazione binario 
Invece di usare la conversione diretta da un numero decimale ad un numero esadecimale, 
proviamo a fare un passaggio intermedio attraverso la rappresentazione binaria.   
Dividere per 2 è più semplice rispetto a dividere per 16 (soprattutto nel calcolo dei resti) e passare 
da un numero binario a un numero esadecimale è immediato 
  

 
Esempio: convertire 31553 da decimale al corrispondente valore esadecimale 
1. Converto 31553 in binario: 
 Base Resto 
31553 2 1 
15776 2 0 
7888 2 0 
3944 2 0 
1972 2 0 
986 2 0 
493 2 1 
246 2 0 
123 2 1 
61 2 1 
30 2 0 
15 2 1 
7 2 1 
3 2 1 
1 2 1 
0   
 
2. Converto il numero binario in esadecimale 
 
        0111   1011   0100   0001 
 
 
 7 B 4 116       
 
 
 
 
 
111101101000001 
7B4116 


---

# SOL Lab - Identifying IPv4 Addresses

**File:** `SOL Lab - Identifying IPv4 Addresses.pdf`
**Tipo:** `.pdf`
**Dimensione:** 608.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 1 di 3 
Laboratorio: Individuazione degli indirizzi IPv4  
Obiettivi 
Sezione 1: Individuare gli indirizzi IPv4 
Sezione 2: Classificare gli indirizzi IPv4 
Introduzione e scenario 
In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4). 
Si identificheranno i diversi tipi di indirizzi IPv4 e i componenti che formano l'indirizzo, come la porzione rete e 
dell'host, nonché la subnet mask. I tipi di indirizzi analizzati includono quelli pubblici, privati, unicast e 
multicast. 
Risorse necessarie 
• Dispositivo con accesso a Internet 
• Facoltativo: calcolatore degli indirizzi IPv4 
Sezione 1: Individuare gli indirizzi IPv4 
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
Indirizzo 
IP/prefisso 
Rete/host 
N, n = rete, H, h = host Subnet mask Indirizzo di rete 
192.168.10.10/24 N.N.N.H 255.255.255.0 192.168.10.0 
10.101.99.17/23 N.N.nnnnnnnh.H 255.255.254.0 10.101.98.0 
209.165.200.227/27    
172.31.45.252/24    
10.1.8.200/26    
172.16.117.77/20    
10.1.1.101/25    
209.165.202.140/27    
192.168.28.45/28    
 

Laboratorio: Individuazione degli indirizzi IPv4 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 2 di 3 
Fase 2: Analizzare la tabella seguente ed elencare l'intervallo degli indirizzi host e di broadcast 
sulla base di una coppia rete/maschera del prefisso. 
Le prima riga mostra un esempio di come completare la tabella. 
Indirizzo 
IP/prefisso 
Indirizzo del primo 
host 
Indirizzo dell'ultimo 
host Indirizzo di broadcast 
192.168.10.10/24 192.168.10.1 192.168.10.254 192.168.10.255 
10.101.99.17/23    
209.165.200.227/27    
172.31.45.252/24    
10.1.8.200/26    
172.16.117.77/20    
10.1.1.101/25    
209.165.202.140/27    
192.168.28.45/28    
Sezione 2: Classificare gli indirizzi IPv4 
Nella Sezione 2 si identificheranno e classificheranno diversi esempi di indirizzi IPv4. 
Fase 1: Analizzare la tabella riportata di seguito e identificare il tipo di indirizzo (rete, host, 
multicast o indirizzo di broadcast). 
Le prima riga mostra un esempio di come completare la tabella. 
Indirizzo IP Subnet mask Tipo di indirizzo 
10.1.1.1 255.255.255.252 host 
192.168.33.63 255.255.255.192  
239.192.1.100 255.252.0.0  
172.25.12.52 255.255.255.0  
10.255.0.0 255.0.0.0  
172.16.128.48 255.255.255.240  
209.165.202.159 255.255.255.224  
172.16.0.255 255.255.0.0  
224.10.1.11 255.255.255.0  
 
 
 

Laboratorio: Individuazione degli indirizzi IPv4 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 3 di 3 
Fase 2: Analizzare la tabella riportata di seguito e identificare l'indirizzo come pubblico o 
privato. 
Indirizzo IP/prefisso Pubblico o privato 
209.165.201.30/27  
192.168.255.253/24  
10.100.11.103/16  
172.30.1.100/28  
192.31.7.11/24  
172.20.18.150/22  
128.107.10.1/16  
192.135.250.10/24  
64.104.0.11/16  
Fase 3: Analizzare la tabella riportata di seguito e identificare se la coppia indirizzo/prefisso è 
un indirizzo dell'host valido. 
Indirizzo 
IP/prefisso 
Indirizzo dell'host 
valido? Motivo 
127.1.0.10/24   
172.16.255.0/16   
241.19.10.100/24   
192.168.0.254/24   
192.31.7.255/24   
64.102.255.255/14   
224.0.0.5/16   
10.0.255.255/8   
198.133.219.8/24   
Approfondimento 
Perché dovremmo continuare a studiare l'indirizzamento IPv4 se lo spazio degli indirizzi IPv4 disponibile è 
vuoto? 
_____________________________________________________________________________________ 
_____________________________________________________________________________________ 


---

# Soluzione esercizio AES

**File:** `Soluzione esercizio AES.txt`
**Tipo:** `.txt`
**Dimensione:** 0.4 KB
**Ultima modifica:** 02/07/2026 09:28

---

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

# VLAN

**File:** `VLAN.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1059.7 KB
**Ultima modifica:** 02/07/2026 09:28

---

VLAN

2
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Obiettivi del modulo
Titolo del modulo: Protocolli e modelli
Obiettivo del modulo: Spiegare come i protocolli di rete consentono ai dispositivi di accedere alle 
risorse di rete locali e remote. 
Titolo argomento Obiettivo argomento
Panoramica sulle VLAN Spiegare lo scopo delle VLAN in una rete commutata.
VLAN in un ambiente multi-
switch
Spiegare come uno switch inoltra i frame basati sulla 
configurazione VLAN in un ambiente multi-switch.
Configurazione della VLAN Configurare una porta switch da assegnare a una VLAN in base ai 
requisiti.
Trunk VLAN Configurare una porta trunk su uno switch LAN.
Protocollo trunking dinamico Configurare il protocollo DTP (Dynamic Trunking Protocol).

3
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN

4
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
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


5
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Vantaggi di una 
progettazione VLAN
I vantaggi dell'utilizzo delle VLAN 
sono i seguenti: 
Vantaggi Descrizione
Domini di broadcast
più piccoli
La divisione della LAN riduce il numero di domini broadcast
Maggiore sicurezza Solo gli utenti della stessa VLAN possono comunicare insieme
Maggiore efficienza IT Le VLAN possono raggruppare dispositivi con requisiti simili, ad esempio 
facoltà e studenti
Riduzione dei costi Uno switch può supportare più gruppi o VLAN
Prestazioni migliorate I domini broadcast di piccole dimensioni riducono il traffico, migliorando la 
larghezza di banda
Gestione semplificata Gruppi simili avranno bisogno di applicazioni simili e altre risorse di rete


6
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN
VLAN predefinita
La VLAN 1 è la seguente: 
• La VLAN predefinita
• La VLAN nativa predefinita
• La VLAN di gestione 
predefinita
• Impossibile eliminare o 
rinominare
Nota: Sebbene non sia 
possibile eliminare VLAN1, 
Cisco consiglia di assegnare 
queste funzionalità predefinite 
ad altre VLAN


7
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN (seguito) 
VLAN dati 
• Dedicata al traffico generato dall'utente (email e traffico web). 
• VLAN 1 è la VLAN dati predefinita perché tutte le interfacce sono assegnate a questa VLAN.
VLAN nativa
• Questa viene utilizzata solo per i collegamenti trunk. 
• Tutti i frame sono contrassegnati su un collegamento trunk 802.1Q tranne quelli sulla VLAN 
nativa. 
VLAN di gestione 
• Questa viene utilizzata per il traffico SSH/Telnet VTY e non deve essere trasportata con il 
traffico dell'utente finale.
• In genere, la VLAN che è SVI per lo switch Layer 2. 

8
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Panoramica sulle VLAN
Tipi di VLAN (seguito) 
VLAN voce  
• È necessaria una VLAN separata perché il 
traffico vocale richiede:
• Larghezza di banda garantita
• Priorità QoS alta
• Capacità di evitare la congestione
• Ritardo inferiore a 150 ms dall'origine alla 
destinazione
• L'intera rete deve essere progettata per 
supportare la voce.


9
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente 
multi-switch

10
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Definizione di trunk VLAN
Un trunk è un collegamento point-to-
point tra due dispositivi di rete.
Funzioni del trunk Cisco:
• Consente più di una VLAN
• Estende la VLAN su tutta la rete
• Per impostazione predefinita, 
supporta tutte le VLAN
• Supporta trunking 802.1Q


11
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Reti senza VLAN
Senza VLAN, tutti i dispositivi collegati agli switch riceveranno tutto il traffico unicast, 
multicast e broadcast.


12
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Reti con VLAN
Con le VLAN, il traffico unicast, multicast e broadcast è limitato a una VLAN. Senza un 
dispositivo di Layer 3 per collegare le VLAN, i dispositivi in VLAN diverse non possono 
comunicare. 


13
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Identificazione VLAN con un tag
• L'intestazione IEEE 802.1Q è 4 Byte
• Quando il tag viene creato, FCS deve essere 
ricalcolato.
• Quando viene inviato ai dispositivi finali, questo tag 
deve essere rimosso e il FCS ricalcolato nuovamente 
al suo numero originale.
Campo tag VLAN 802.1Q Funzione
Tipo • Campo a 2 byte con 0x8100 esadecimale
• Questo è indicato come Tag Protocol ID (TPID)
Priorità utente • Valore a 3 bit che supporta 
Canonical Format Identifier (CFI) • Valore a 1 bit che può supportare frame token ring su Ethernet
VLAN ID (VID) • Identificatore VLAN a 12 bit in grado di supportare fino a 4096 
VLAN


14
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
VLAN nativa e tag 802.1Q
Basi trunk 802.1Q:
• Il tagging viene in genere eseguito su tutte le 
VLAN.
• L'uso di una VLAN nativa è stato progettato 
per l'uso legacy, come l'hub nell'esempio.
• A meno che non sia cambiato, VLAN1 è la 
VLAN nativa.
• Entrambe le estremità di un collegamento 
trunk devono essere configurate con la 
stessa VLAN nativa.
• Ogni trunk è configurato separatamente, 
quindi è possibile avere una VLAN nativa 
diversa su trunk separati.


15
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Tagging Voice VLAN
Il telefono VoIP è uno switch a tre porte:
• Lo switch utilizzerà CDP per informare il telefono della 
VLAN Voice.
• Il telefono contrassegnerà il proprio traffico (Voice) e può 
impostare Cost of Service (Cos). CoS è QoS per il Layer 
2.
• Il telefono potrebbe o non può etichettare i frame dal PC.
Traffico Funzione del tagging
Voice VLAN Taggato con un valore di priorità di classe di servizio (CoS) appropriato
Access VLAN Può anche essere taggata con un valore di priorità CoS di Layer 2
Access VLAN Non è contrassegnata (nessun valore di priorità CoS di Layer 2)


16
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Esempio di verifica Voice VLAN
Il comando show interfaces fa0/18 switchport può mostrarci sia dati che VLAN vocali 
assegnati all'interfaccia.


17
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
VLAN in un ambiente multi-switch
Packet Tracer – Indagine su un'implementazione VLAN
In questa attività Packet Tracer, si potrà:
• Parte 1: Osservare il traffico broadcast in un'implementazione VLAN
• Parte 2: Osservare il traffico broadcast senza VLAN

18
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN

19
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Intervalli VLAN su switch Catalyst
Gli switch Catalyst 2960 e 3650 supportano 
oltre 4000 VLAN.
Intervallo normale VLAN 1 — 1005 Intervallo esteso VLAN 1006 - 4095
Utilizzato in piccole e medie imprese Usato da ⁪provider di servizi
1002 — 1005 sono riservati alle VLAN legacy Sono in Running-Config
1, 1002 - 1005 vengono creati 
automaticamente e non possono essere 
eliminati
Supporta meno funzioni VLAN
Memorizzati nel file vlan.dat in flash Richiede configurazioni VTP
VTP può sincronizzare tra gli switch


20
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Comandi di creazione VLAN
I dettagli VLAN vengono memorizzati nel file vlan.dat. È possibile creare VLAN in 
modalità di configurazione globale.
Attività Comando IOS
Accedere alla modalità di 
configurazione globale. Switch# configure terminal
Creare una VLAN con un numero ID 
valido. Switch(config)# vlan vlan-id
Specificare un nome univoco per 
identificare la VLAN. Switch(config-vlan)# name vlan-name
Ritornare alla modalità privileged EXEC. Switch(config-vlan)# end
Accedere alla modalità di 
configurazione globale. Switch# configure terminal

21
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Esempio di creazione VLAN
• Se Student PC sarà nella VLAN 20, 
creeremo prima la VLAN e poi la 
denomineremo.
• Se non gli viene assegnato un nome, 
Cisco IOS gli assegnerà un nome 
predefinito di vlan e il numero a quattro 
cifre della VLAN. Ad esempio vlan0020 
per VLAN 20.
Prompt Comando
S1# Configure terminal
S1(config)# vlan 20
S1(config-vlan)# name student
S1(config-vlan)# end


22
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Comandi di assegnazione porta VLAN
Una volta creata la VLAN, possiamo quindi assegnarla alle interfacce corrette.
Attività Comando
Accedere alla modalità di configurazione globale. Switch# configure terminal
Accedere alla modalità di configurazione 
dell’interfaccia. Switch(config)# interface interface-id
Impostare la porta in modalità di accesso. Switch(config-if)# switchport mode access
Assegnare la porta a una VLAN. Switch(config-if)# switchport access vlan vlan-id
Ritornare alla modalità privileged EXEC. Switch(config-if)# end

23
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Esempio di assegnazione porta VLAN
Possiamo assegnare la VLAN 
all'interfaccia porta.
• Una volta assegnata al dispositivo la 
VLAN, il dispositivo finale avrà 
bisogno delle informazioni 
sull'indirizzo IP per tale VLAN
• Qui, Student PC riceve 172.17.20.22
Prompt Comando
S1# Configure terminal
S1(config)# Interface fa0/18
S1(config-if)# Switchport mode access
S1(config-if)# Switchport access vlan 20
S1(config-if)# end


24
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
VLAN Data e Voice
Una porta di accesso può essere 
assegnata solo a una VLAN dati. 
Tuttavia, può anche essere 
assegnato a una VLAN Voice per 
quando un telefono e un dispositivo 
finale sono spenti dalla stessa porta 
di switch.


25
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Esempio di VLAN Data e Voice
• Vogliamo creare e denominare sia VLAN 
Voice che Data.
• Oltre ad assegnare la VLAN Data, 
assegneremo anche la VLAN Voice e 
accenderemo QoS per il traffico vocale 
all'interfaccia.
• Lo switch catalyst più recente creerà 
automaticamente la VLAN, se non esiste già, 
quando viene assegnata a un'interfaccia.
Nota: QoS non viene affrontato in questo 
corso. Qui mostriamo l'uso del comando mls 
qos trust [cos | device cisco-phone | dscp | 
ip-precedence] .


26
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Verifica informazioni 
VLAN
Usare il comando show vlan. La 
sintassi completa è la seguente: 
show vlan [brief | id vlan-id | name
vlan-name | summary]
Attività Opzione di comando
Visualizzare il nome VLAN, lo stato e le relative porte una VLAN per 
riga. brief
Visualizzare le informazioni sul numero ID VLAN identificato. id vlan-id
Visualizzare le informazioni sul nome VLAN identificato. Il vlan name
è una stringa ASCII da 1 a 32 caratteri. name vlan-name
Visualizzare le informazioni di riepilogo della VLAN. Riepilogo


27
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Modificare l'appartenenza alla 
porta VLAN
Esistono diversi modi per cambiare 
l'appartenenza alla VLAN:
• Reinserire il comando switchport access 
vlan vlan-id 
• Utilizzare no switchport access vlan per 
riposizionare l'interfaccia in VLAN 1
Utilizzare brief show vlan o i comandi show 
interface fa0/18 switchport per verificare la 
corretta associazione VLAN.


28
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Eliminare VLAN
Eliminare le VLAN con il comando no vlan vlan-id
Attenzione: Prima di eliminare una VLAN, riassegnare tutte le porte membro a una VLAN 
diversa. 
• Eliminare tutte le VLAN con i comandi delete flash:vlan.dat o delete vlan.dat .
• Ricaricare lo switch quando si eliminano tutte le VLAN.
Nota: Per ripristinare l'impostazione predefinita di fabbrica: scollegare tutti i cavi dati, 
cancellare la configurazione di avvio ed eliminare il file vlan.dat, quindi ricaricare il 
dispositivo.

29
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Configurazione VLAN
Packet Tracer — Configurazione VLAN
In questo Packet Tracer, verranno raggiunti i seguenti obiettivi:
• Verificare la configurazione VLAN predefinita
• Configurare VLAN
• Assegnare VLAN alle porte

30
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN

31
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Comandi di configurazione del trunk
Configurare e verificare i trunk VLAN. I trunk sono layer 2 e trasportano il traffico per tutte le 
VLAN.
Attività Comando IOS
Enter global configuration mode. Switch# configure terminal
Accedere alla modalità di configurazione 
dell’interfaccia. Switch(config)# interface interface-id
Impostare la porta sulla modalità trunking 
permanente. Switch(config-if)# switchport mode trunk
Impostare la VLAN nativa su qualcosa di 
diverso dalla VLAN 1.
Switch(config-if)# switchport trunk native vlan 
vlan-id
Specificare l'elenco delle VLAN da 
autorizzare sul collegamento trunk.
Switch(config-if)# switchport trunk allowed 
vlan vlan-list
Ritornare alla modalità privileged EXEC. Switch(config-if)# end

32
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Esempio di configurazione del 
trunk
Le subnet associate a ogni VLAN sono:
• VLAN 10 - Faculty/Staff - 172.17.10.0/24
• VLAN 20 - Student - 172.17.20.0/24
• VLAN 30 - Guest - 172.17.30.0/24
• VLAN 99 - Native - 172.17.99.0/24
La porta F0/1 su S1 è 
configurata come porta trunk.
Nota: Questo presuppone uno 
switch 2960 che utilizza il tag 
802.1q. Gli switch di Layer 3 
richiedono che l'incapsulamento 
sia configurato prima della 
modalità trunk. 
Prompt Comando
S1(config)# Interface fa0/1
S1(config-if)# Switchport mode trunk
S1(config-if)# Switchport trunk native vlan 99
S1(config-if)# Switchport trunk allowed vlan 10,20,30,99
S1(config-if)# terminare


33
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Verifica della configurazione 
trunk
Impostare la modalità trunk e vlan nativo.
Notare sh int fa0/1 switchport :
• È impostato su trunk amministrativo
• È impostato come trunk operativamente 
(funzionante)
• L'incapsulamento è dot1q
• VLAN nativa impostata su VLAN 99 
• Tutte le VLAN create sullo switch 
passeranno il traffico su questo trunk


34
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Ripristinare il trunk allo stato predefinito
• Ripristina le impostazioni predefinite 
del trunk con il comando no.
• Tutte le VLAN hanno consentito di 
passare il traffico
• VLAN nativa = VLAN 1
• Verificare le impostazioni predefinite 
con un comando sh int fa0/1 
switchport .


35
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Ripristinare il trunk allo stato predefinito (seguito)
Ripristinare il trunk in una modalità di accesso 
con il comando switchport mode access :
• È impostato su un'interfaccia di accesso 
amministrativo
• È impostato come interfaccia di accesso 
operativamente (funzionante)


36
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Packet Tracer — Configurazione trunk
In questo Packet Tracer, verranno raggiunti i seguenti obiettivi:
• Verificare VLAN
• Configurare trunk

37
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Trunk VLAN
Laboratorio — Configurare VLAN e trunks
In questa attività di laboratorio si seguiranno i seguenti passi:
• Implementare la rete e configurare le impostazione di base del dispositivo
• Creare VLAN e assegnare porte switch
• Gestire le assegnazioni delle porte VLAN e il database VLAN
• Configurare un trunk 802.1Q tra gli switch
• Eliminare il database VLAN

38
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol

39
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Introduzione a DTP
Dynamic Trunking Protocol (DTP) è un protocollo proprietario di Cisco.
Le caratteristiche DTP sono le seguenti:
• Attivo per impostazione predefinita su Catalyst 2960 e 2950 switch
• Dynamic-auto è predefinito sugli switch 2960 e 2950
• Può essere disattivato con il comando nonegotiate
• Può essere riattivato impostando l'interfaccia su dynamic-auto
• L'impostazione di uno switch su un trunk statico o un accesso statico eviterà problemi di 
negoziazione con il trunk in modalità switchport o i comandi di accesso in modalità 
switchport.


40
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Modalità di negoziazione interfaccia
Il comando switchport mode prevede opzioni aggiuntive.
Utilizzare il comando di configurazione dell'interfaccia switchport nonegotiate per 
interrompere la negoziazione DTP.
Opzione Descrizione
access Modalità di accesso permanente e negozia per convertire il 
collegamento adiacente in un collegamento di accesso
dynamic auto Diventa un'interfaccia trunk se l'interfaccia adiacente è impostata sulla 
modalità trunk o desiderable
dynamic desirable Cerca attivamente di diventare un trunk negoziando con altre interfacce 
auto o desirable
trunk Modalità di trunking permanente e negozia per convertire il 
collegamento adiacente in un collegamento trunk

41
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Risultati di una configurazione DTP
Le opzioni di configurazione DTP sono le seguenti:
Dynamic Auto Dynamic 
Desirable Trunk Access
Dynamic Auto Access Trunk Trunk Access
Dynamic 
Desirable Trunk Trunk Trunk Access
Trunk Trunk Trunk Trunk Connettività 
limitata
Access Access Access Connettività 
limitata Access

42
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Dynamic Trunking Protocol
Verifica della modalità DTP
La configurazione DTP predefinita dipende 
dalla versione e dalla piattaforma Cisco 
IOS.
▪ Utilizzare il comando show dtp 
interface per determinare la modalità 
DTP corrente.
▪ La best practice consiglia di impostare le 
interfacce per l'accesso o il trunk e per 
disattivare DTP


43
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica 

44
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Packet Tracer – Implementare VLAN e Trunking
In questo Packet Tracer, verranno raggiunti i seguenti obiettivi:
• Configurare VLAN
• Assegnare porte alle VLAN
• Configurare trunking statico
• Configurare trunking dinamico

45
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Laboratorio — Implementare VLAN e Trunking
In questa attività di laboratorio si seguiranno i seguenti passi:
• Implementare la rete e configurare le impostazione di base del dispositivo
• Creare VLAN e assegnare porte switch
• Configurare un trunk 802.1Q tra gli switch

46
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Che cosa ho appreso in questo modulo?
• Le VLAN si basano su connessioni logiche anziché fisiche.
• Le VLAN possono segmentare le reti in base alla funzione, al team o 
all'applicazione.
• Ogni VLAN è considerata una rete logica separata.
• Un trunk è un collegamento point-to-point che porta più di una VLAN. 
• I campi dei tag VLAN includono tipo, priorità utente, CFI e VID.
• Per supportare VoIP è necessaria una VLAN vocale separata.
• Le configurazioni VLAN a intervallo normale vengono memorizzate nel file 
vlan.dat in flash.
• Una porta di accesso può appartenere a una VLAN dati alla volta, ma può anche 
avere una VLAN vocale.

47
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Cosa ho appreso in questo modulo? (seguito)
• Un trunk è un collegamento di Layer 2 tra due switch che trasporta il traffico per 
tutte le VLAN.
• Il tunk avrà bisogno di tagging per le varie VLAN, in genere 802.1q.
• Il tag IEEE 802.1q consente di eseguire il provisioning di una VLAN nativa che 
rimarrà senza tag.
• Un'interfaccia può essere impostata su trunking o non trunking.
• La negoziazione del trunk è gestita dal Dynamic Trunking Protocol (DTP).
• DTP è un protocollo proprietario Cisco che gestisce la negoziazione trunk

48
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Pratica del modulo e Quiz
Nuovi Termini e Comandi
• VLAN
• Dominio di broadcast logico
• VLAN dati
• VLAN predefinita
• VLAN nativa
• VLAN di gestione
• show vlan brief
• VLAN voce
• Trunk VLAN
• Segmentazione VLAN
• Rete
• Tagging VLAN
• Canonical Format Identifier (CFI)
• Priorità utente
• ID VLAN
• Tipo
• show interfaces int switchport

49
© 2016 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati.   Documento 
riservato Cisco
Quiz e pratica
Nuovi termini e comandi
• VLAN a intervallo normale
• VLAN a gamma estesa
• vlan vlan-id
• name vlan-name
• switchport mode access
• switchport access vlan 
vlan-id
• Intervallo interfaccia
• no switchport access vlan 
vlan-id
• vlan vlan-id
• delete flash:vlan.dat
• delete vlan.dat
• show vlan
• show interfaces
• show vlan summary
• show interfaces vlan 
vlan_id
• switchport mode trunk
• switchport trunk allowed 
vlan vlan_list
• switchport trunk native 
vlan vlan_id
• no switchport trunk 
allowed vlan
• no switchport trunk native 
vlan
• show interfaces 
switchport
• no switchport access vlan 
vlan_id
• show interfaces trunk
• show interfaces int_id 
trunk

