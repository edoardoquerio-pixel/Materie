# Virtualizzazione 26 - VM e Openstack

## Panoramica
Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]

## Argomenti trattati
Virtualizzazione, Cloud, Reti, API REST, Configurazione

---
## Appunti

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Sistemi di Virtualizzazione
Macchina Virtuale e Openstack
Infrastruttura Virtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Cloud Service Provider
Come si realizza il Cloud Computing?
▪ Attraverso software non troppo diverso da hypervisor, ma creato per
gestire il cloud.
▪ Orchestratore di macchina virtuali.
▪ Openstack: piattaforma software per il management di un cloud.
▪ Progetto iniziato nel 2010 dalla collaborazione tra Rackspace e la
Come si realizza il Cloud Computing? (1)
▪ Si avvale delle sue
funzionalità per creare
un cloud di macchine
Come si realizza il Cloud Computing? (2)
Libvirt per gestire eterogeneità
▪ Si avvale di libvirt:
▪ Permette di interagire con
Gestione delle Risorse in Pool
La Gestione delle Risorse (Resource Management)
Resource Management
Un processo per allocare, a favore delle macchine virtuali (VM), le risorse di una
macchina fisica o di un cluster di macchine fisiche, al fine di ottimizzare l’utilizzo
complessivo delle risorse.
• A cosa serve la gestione delle risorse?
▪ Controlla l’uso delle risorse.
▪ Impedisce che una singola VM monopolizzi le risorse.
▪ Alloca le risorse opportunamente, in base alle priorità assegnate alle varie VM.
• Le risorse devono essere messe in pool (Resource Pooling), allo scopo di gestirle
“centralmente”.
• Risorse = CPU, memoria, rete e storage.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Il Resource Pooling
Resource Pooling
È una astrazione logica delle risorse fisiche aggregate, che ne abilita la gestione
• Un pool è creato a partire da una macchina fisica o da un insieme di machine fisiche (cluster).
▪ Questo resource pool di partenza è definito parent resource pool.
• A partire dal parent resource pool (iniziale), gli Amministratori di sistema possono allocare le
risorse ad una applicazione o a delle VM.
▪ Le risorse allocate, a partire dal parent pool, per una specifica applicazione o alla singola VM si definiscono
child resource pool.
• Tre indicatori vengono usati per controllare le risorse consumate dai diversi pool o dalle VM.
• Si parla di Key Performance Indicator (KPI). Questi sono:
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Il Resource Pooling: un esempio
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
Share, Limit e Reservation
• Share Limit e Reservation sono dei parametri (variabili) che controllano le risorse allocate
ed utilizzate da un child resource pool o da una VM.
▪ Quantità di CPU o memoria che una VM o un child pool può avere, rispetto al totale delle
risorse (di CPU o memoria) del parent pool.
▪ Individua la priorità di una VM o child pool.
▪ Massima quantità di CPU o memoria che una VM o un child pool può consumare.
▪ Configurato alla creazione della VM, si può modificare solo a VM spenta.
▪ Quantità di CPU o memoria riservata per una VM o per un child pool.
▪ Una VM non viene attivata, se la quanità di risorse definite dalla reservation non sono
▪ Se la VM non utilizza tutte le risorse riservate, quelle libere vengono allocate ad altre
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
L’ottimizzazione delle risorse di CPU
• Allocare le risorse di una CPU in modo efficiente e appropriato è fondamentale.
• Le moderne CPU sono equipaggiate con core multipli e con hyper-threading.
▪ I processori multi-core hanno,
in una singola CPU (circuito integrato o socket),
diverse unità di processamento (processing unit, a.k.a. core).
▪ L’hyper-threading fa apparire una CPU fisica come due o più CPU logiche.
• L’hypervisor definisce e alloca le CPU virtuali sulla CPU fisiche (analogamente a
come un SO assegna ai diversi processi – o thread – il tempo di CPU).
• L’hypervisor supporta le funzionalità di multi-core, hyper-threading e CPU load-
balancing (bilanciamento del carico) per ottimizzare le risorse della CPU.
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
CPU: pCPU, L-CPU, vCPU
I processori Multi-Core
Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
L’hyper-threading
Un thread o thread di esecuzione, in informatica, è una

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 026_Virtualizzazione_26_-_VM_e_Openstack.md*
