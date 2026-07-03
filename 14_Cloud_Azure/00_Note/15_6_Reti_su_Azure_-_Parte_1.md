# 6) Reti su Azure - Parte 1

**File:** `6) Reti su Azure - Parte 1.pptx`
**Tipo:** `.pptx`
**Dimensione:** 67.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITA' FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Reti su Azure - Parte 1 (2 ore)

---

Reti su Azure - Parte 1
VNet, subnet, NSG e accesso RDP come caso guida

---

Argomenti
•  Perche' la rete conta in Azure
•  VNet e Subnet: i blocchi base
•  NSG: regole allow/deny sul traffico
•  RDP su una VM Windows: cosa deve esserci per collegarsi
•  Caso guida: relazione tra regola TCP 3389 e accesso alla VM
•  Segmentazione, troubleshooting e casi piu' realistici

---

Dove siamo nel percorso
•  Dopo identita', permessi e governance, passiamo al livello rete
•  La rete decide chi raggiunge cosa e su quale porta
•  Qui iniziamo dalla parte piu' concreta: una VM gia' esistente e il suo NSG
•  Una VM gia' esistente con il suo NSG e' un buon caso iniziale per leggere l'effetto delle regole

---

I pezzi minimi della rete in Azure
Oggetto
A cosa serve
VNet
La rete privata nel cloud
Subnet
Una porzione della VNet
NIC
La scheda di rete della VM
Public IP
L'indirizzo pubblico per accesso da Internet
NSG
Le regole che permettono o bloccano traffico
•  Per il caso RDP bastano soprattutto VM + Public IP + NSG

---

VNet e Subnet
•  Una VNet e' la tua rete privata in Azure
•  Una Subnet divide la rete in zone piu' piccole
•  Le subnet servono per separare carichi di lavoro e applicare regole diverse
•  Piu' avanti useremo questa logica per distinguere frontend, backend e management

---

NSG: concetti chiave
•  Un Network Security Group contiene regole Allow o Deny
•  Le regole valgono su traffico inbound o outbound
•  Un NSG si puo' associare a una subnet o a una NIC
•  Le regole hanno una priority: numero piu' basso = precedenza piu' alta
•  Le regole di default esistono gia', ma le regole custom possono prevalere

---

RDP: condizioni minime di accesso
•  Una VM Windows accesa
•  Un Public IP sulla VM, se il collegamento e' diretto da Internet
•  Una regola inbound TCP 3389 che consenta il traffico verso la VM
•  Credenziali valide della macchina virtuale
“Se la porta 3389 non e' consentita, la connessione RDP non parte.”

---

Dove lo vedi nel portale
•  Apri la Virtual machine
•  Nel menu vai su Networking > Network settings
•  Controlla se c'e' una regola che consente TCP 3389
•  Apri il Network security group associato
•  In Inbound security rules leggi, modifichi o elimini la regola

---

Caso guida: RDP e regola 3389
•  Se esiste una regola inbound TCP 3389 che consente il traffico, la VM puo' accettare nuove connessioni RDP
•  Se la regola manca oppure viene negata, la connessione RDP fallisce
•  L'esito dipende anche da priority, source, protocol e scope
•  Il punto non e' memorizzare clic, ma leggere il legame tra regola di rete e accessibilita' della VM
La rete non e' sfondo: decide concretamente se un accesso e' possibile oppure no.

---

Attenzione: cosa osservare davvero
•  Gli NSG sono stateful: una sessione gia' aperta puo' restare attiva
•  Se togli la regola, di solito falliscono le nuove connessioni RDP
•  La stessa porta puo' avere esiti diversi in base a priority, source e scope
•  Una regola con source My IP e' piu' sicura di una con source Any

---

Sviluppi del tema
•  Subnet e segmentazione della rete
•  Differenza tra NSG su subnet e su NIC
•  Effective security rules e verifica del risultato finale
•  Altri casi: HTTP, HTTPS, regole troppo larghe, regole troppo strette
Il punto chiave e' che una regola di rete cambia davvero il comportamento della VM.
