# Virtualizzazione 26 - La Virtualizzazione di Networking

## Panoramica
Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]

## Argomenti trattati
Virtualizzazione, Reti, Cloud, Sicurezza, API REST

---
## Appunti

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Elementi di Virtualizzazione
La Virtualizzazione della Rete (Networking)
Il Modello ISO OSI
La Virtualizzazione delle Rete 1/4
Network Virtualization
È il processo di segmentazione logica o raggruppamento di reti fisiche che porta alla
creazione di entità logiche single o multiple ma indipendenti, chiamate reti virtuali.
➢Una rete virtuale appare come una rete fisica ai nodi a questa connessi.
➢Il processo di virtualizzazione delle reti abilita la condivisione delle risorse di rete.
➢La virtualizzazione abilita il raggruppamento funzionale di nodi con gli stessi requisiti in
una unica rete virtuale, indipendentemente dalla loro localizzazione geografica.
➢Permette la comunicazione diretta tra nodi appartenenti alla stessa rete virtuale, senza
necessità di instradare i pacchetti, anche se attestati a reti fisiche diverse.
l’instradamento del traffico è necessario quando comunicano due nodi
appartenenti a due reti virtuali diverse, anche se attestati alla stessa rete fisica.
➢Segrega il traffico di gestione (incluso il network broadcast) all’interno della singola rete
virtuale, evitando che si propaghi in altre reti.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
La Virtualizzazione delle Rete 2/4
▪ adattatori di rete;
▪ ripetitori e hub.
• Fornisce connettività tra:
▪ server fisici che ospitano hypervisor;
▪ server fisici e client;
▪ server fisici e sistemi di storage.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
La Virtualizzazione delle Rete 3/4
• Si trova all’interno dei serve fisici.
• È composta da switch logici chiamati
switch virtuali, con funzione simile
agli switch fisici.
all’interno di un server fisico.
dell’hypervisor.
• Connette alla rete fisica.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
La Virtualizzazione delle Rete 4/4
• La rete di VM e la rete fisica sono virtualizzate per creare delle reti virtuali (p. es. Virtual Local
Area Network VLAN o Virtual Storage Area Network VSAN)
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Virtual Networking della VM 1/4
Virtual Networking della VM 2/4
• Creare sottoreti virtuali mediante switch di rete virtuali interni ed
• Una rete virtuale è una rete privata definita dal software in un
ambiente virtuale.
• Uno switch di rete virtuale esterno consente di instradare il traffico
verso la rete esterna.
• Uno switch di rete virtuale interno non gestisce il traffico verso la
rete esterna. Viene usato per la costituzione di sottoreti virtuali.
VM1: due NIC virtuali VNIC1 e VNIC2, ognuna connessa ad uno switch
virtuale e quindi a ciascuna delle reti virtuali.
Le richieste che provengono da VNIC3 verranno trasmesse alla rete
fisica e al mondo esterno. Le risposte a tale richiesta seguono il
percorso al contrario, attraverso la NIC fisica, attraverso lo switch
virtuale esterno e di nuovo alla NIC virtuale della VM.
Le richieste da VNIC2 saranno inoltrare allo switch virtuale interno per
la comunicazione con altre macchine virtuali.
La VM3 può effettuare richieste solo tramite lo switch virtuale interno.
Questa è una strategia comune in un ambiente virtuale per proteggere
applicazioni e server da attacchi indesiderati:
senza una connessione a una scheda di rete fisica, la VM3 non può
essere vista, tanto meno attaccata, da una fonte esterna.
• VM1 funge da firewall e, con pratiche di sicurezza appropriate,
protegge i dati contenuti nell'altra VM.
Virtual Networking della VM 3/4
• Rispetto alla slide precedente, aggiunto un
ulteriore switch virtuale per separare due
• Possono essere diverse organizzazioni
aziendali che richiedono spazi di
separati in cui lavorare (es: la produzione è
separata dal test e dallo sviluppo).
• Questa architettura migliora inoltre le
prestazioni riducendo il traffico su ogni
segmento e migliora la sicurezza limitando
l'accesso a ciascuna area.
• Una terza macchina virtuale viene aggiunta
all'host e può comunicare solo con il nuovo
switch virtuale esterno.
Virtual Networking della VM 4/4

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 026_Virtualizzazione_26_-_La_Virtualizzazione_di_Networking.md*
