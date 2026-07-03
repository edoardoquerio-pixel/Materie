# Reti e Sicurezza Informatica — Appunti Strutturati per Sessione

> **Corso:** ITS ICT Cloud Specialist 2025-2027
> **Materia:** 06_Reti_e_Sicurezza_Informatica

---

## Indice delle Sessioni

1. [Introduzione alla Cybersecurity](#introduzione-alla-cybersecurity)
2. [Gestione Password e Crittografia Base](#gestione-password-e-crittografia-base)
3. [Crittografia Simmetrica (DES/AES)](#crittografia-simmetrica-(des/aes))
4. [Diffie-Hellman e RSA](#diffie-hellman-e-rsa)
5. [Hashing e Certificati Digitali](#hashing-e-certificati-digitali)
6. [Reti: Indirizzamento IPv4 e Subnetting](#reti:-indirizzamento-ipv4-e-subnetting)
7. [VLAN e InterVLAN Routing](#vlan-e-intervlan-routing)
8. [Strumenti: Sistemi Numerici, Entropia](#strumenti:-sistemi-numerici,-entropia)
9. [Social Engineering](#social-engineering)
10. [Soluzioni Esercizi](#soluzioni-esercizi)

---

## Introduzione alla Cybersecurity

### Materiali di Riferimento

- [`01_01_Introduzione_alla_cybersecurity.md`](00_Note/01_01_Introduzione_alla_cybersecurity.md)

#### Contenuto Estratto

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
Qu...

---

## Gestione Password e Crittografia Base

### Materiali di Riferimento

- [`02_02_Gestione_delle_password.md`](00_Note/02_02_Gestione_delle_password.md)

#### Contenuto Estratto

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
dropping, pretexting, tailgating...

---
- [`03_03_Introduzione_alla_crittografia.md`](00_Note/03_03_Introduzione_alla_crittografia.md)

#### Contenuto Estratto

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
tradimento: avr...

---

## Crittografia Simmetrica (DES/AES)

### Materiali di Riferimento

- [`04_04_Crittografia_DES_e_AES.md`](00_Note/04_04_Crittografia_DES_e_AES.md)

#### Contenuto Estratto

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
...

---
- [`09_Approfondimento_su_DES_e_AES.md`](00_Note/09_Approfondimento_su_DES_e_AES.md)

#### Contenuto Estratto

---

La funzione crittograﬁca di DES 
Il DES normale utilizza una funzione che si chiama Feistel (in ﬁgura), che 
lavora su metà del blocco (E, in ﬁgura) e una sottochiave, che vengono 
messe in XOR. Il risultato viene diviso in 8 parti da 6 bit e sostituito con 
una apposita S-Box, ed inﬁne riordinati con una P-Box (permutation box), 
anch’essa ﬁssa. Questa funzione viene ripetuta in ogni sottofase. 
L’algoritmo di espansione della chiave in AES 
L’algoritmo di espansione della chiave prende in...

---

## Diffie-Hellman e RSA

### Materiali di Riferimento

- [`05_05_Diffie-Hellman_key_exchange.md`](00_Note/05_05_Diffie-Hellman_key_exchange.md)

#### Contenuto Estratto

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
I primi due me...

---
- [`06_06_Crittografia_a_chiave_pubblica_e_RSA.md`](00_Note/06_06_Crittografia_a_chiave_pubblica_e_RSA.md)

#### Contenuto Estratto

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
 a...

---
- [`10_Appunti_di_algebra_per_la_crittografia_a_chiave_pubblica_RSA.md`](00_Note/10_Appunti_di_algebra_per_la_crittografia_a_chiave_pubblica_RSA.md)

#### Contenuto Estratto

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
6 I sistemi di...

---

## Hashing e Certificati Digitali

### Materiali di Riferimento

- [`07_07_Certificati_digitali_e_hashing.md`](00_Note/07_07_Certificati_digitali_e_hashing.md)

#### Contenuto Estratto

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
viene distribuita all’interno di un...

---
- [`08_A_Method_for_Obtaining_Digital_Signatures_and_Public-Key_Cryptosystems.md`](00_Note/08_A_Method_for_Obtaining_Digital_Signatures_and_Public-Key_Cryptosystems.md)

#### Contenuto Estratto

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
the intended recipient. Only he ...

---

## Reti: Indirizzamento IPv4 e Subnetting

### Materiali di Riferimento

- [`17_Indirizzamento_IPv4.md`](00_Note/17_Indirizzamento_IPv4.md)

#### Contenuto Estratto

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
DOCENTE Andrea Blanchietti 
UNITA’ 
FORMATIVA Fondamenti di Reti di Calcolatori 
ARGOMENTO Indirizzamento IPv4 

Indirizzamento con protocollo IPv4 
L’indirizzo IPv4 è composto da una sequenza di 32 bit, suddivisa in quattro gruppi da 8 bit l’uno; 
ogni gruppo è definito ottetto. La rappresentazione dell’indirizzo avviene convertendo i singoli 
ottetti dal sistema binario al sistema decimale: si parla di notazione decimale puntata. 
 
 
 
L’indirizzo possi...

---
- [`14_Esercizi_di_subnetting_IPv4.md`](00_Note/14_Esercizi_di_subnetting_IPv4.md)

#### Contenuto Estratto

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
Partizionare in due sottoreti la ...

---
- [`19_Lab_-_Identifying_IPv4_Addresses.md`](00_Note/19_Lab_-_Identifying_IPv4_Addresses.md)

#### Contenuto Estratto

---

 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 1 di 3 
Laboratorio: Individuazione degli indirizzi IPv4  
Obiettivi 
Sezione 1: Individuare gli indirizzi IPv4 
Sezione 2: Classificare gli indirizzi IPv4 
Introduzione e scenario 
In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4). 
Si identificheranno i diversi tipi di indirizzi IPv4 e...

---
- [`23_SOL_Lab_-_Identifying_IPv4_Addresses.md`](00_Note/23_SOL_Lab_-_Identifying_IPv4_Addresses.md)

#### Contenuto Estratto

---

 
© 2017 Cisco e/o i relativi affiliati. Tutti i diritti sono riservati. Questo documento contiene informazioni pubbliche di Cisco. Pagina 1 di 3 
Laboratorio: Individuazione degli indirizzi IPv4  
Obiettivi 
Sezione 1: Individuare gli indirizzi IPv4 
Sezione 2: Classificare gli indirizzi IPv4 
Introduzione e scenario 
In questa attività di laboratorio si esaminerà la struttura degli indirizzi del protocollo Internet versione 4 (IPv4). 
Si identificheranno i diversi tipi di indirizzi IPv4 e...

---

## VLAN e InterVLAN Routing

### Materiali di Riferimento

- [`25_VLAN.md`](00_Note/25_VLAN.md)

#### Contenuto Estratto

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
Spiegare come uno switch inoltra i frame basat...

---
- [`18_InterVLAN_Routing.md`](00_Note/18_InterVLAN_Routing.md)

#### Contenuto Estratto

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
Routing inter-VLAN router-on-a-stick Configurare il router-on-a-stick inter-VLAN...

---
- [`20_LAB_configure-router-on-a-stick-inter-vlan-routing.md`](00_Note/20_LAB_configure-router-on-a-stick-inter-vlan-routing.md)

#### Contenuto Estratto

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
PC-A NIC 192.168.3.3 255.255....

---

## Strumenti: Sistemi Numerici, Entropia

### Materiali di Riferimento

- [`22_Sistemi_Numerici.md`](00_Note/22_Sistemi_Numerici.md)

#### Contenuto Estratto

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
sim...

---
- [`12_Demo_entropia.md`](00_Note/12_Demo_entropia.md)

#### Contenuto Estratto

---




L'**entropia di Shannon** è una misura fondamentale della teoria dell'informazione che quantifica la quantità di "informazione" o "incertezza" contenuta in un messaggio. È definita matematicamente come:

```
H(X) = -∑ P(x) × log₂(P(x))
```

Dove:
- `H(X)` è l'entropia in bit per simbolo
- `P(x)` è la probabilità di occorrenza del simbolo `x`
- La sommatoria è estesa su tutti i possibili simboli


L'entropia misura quanto è "sorprendente" o "imprevedibile" un messaggio:

- **Entropia BASS...

---
- [`21_Script_demo_entropia.md`](00_Note/21_Script_demo_entropia.md)

#### Contenuto Estratto

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
        entropy -= probabili...

---
- [`11_Cifrario_di_cesare.md`](00_Note/11_Cifrario_di_cesare.md)

#### Contenuto Estratto

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
        print("Scelta ...

---

## Social Engineering

### Materiali di Riferimento

- [`15_Estratto_da__Larte_dellinganno__di_Kevin_Mitnick.md`](00_Note/15_Estratto_da__Larte_dellinganno__di_Kevin_Mitnick.md)

#### Contenuto Estratto

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
tendiamo a ﬁdarci immoti...

---

## Soluzioni Esercizi

### Materiali di Riferimento

- [`24_Soluzione_esercizio_AES.md`](00_Note/24_Soluzione_esercizio_AES.md)

#### Contenuto Estratto

---

openssl rand -hex 16 > iv.txt

openssl rand 32 > key.bin

KEY_HEX=$(xxd -p key.bin | tr -d '\n')

IV_HEX=$(cat iv.txt | tr -d '\n')

openssl enc -aes-256-cbc -K "$KEY_HEX" -iv "$IV_HEX" -in messaggio.txt -out messaggio.enc

---
- [`13_Enigma_Keys.md`](00_Note/13_Enigma_Keys.md)

#### Contenuto Estratto

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
| 27 | IV I V    | SSH | EV GX HD JO ...

---

