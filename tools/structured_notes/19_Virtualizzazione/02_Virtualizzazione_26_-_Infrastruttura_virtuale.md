# Virtualizzazione 26 - Infrastruttura virtuale

## Panoramica
Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]

## Argomenti trattati
Virtualizzazione, Cloud, API REST, Reti, Configurazione

---
## Appunti

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]
Unità Formativa
Sistemi di Virtualizzazione
Infrastruttura Virtuale
Infrastruttura Virtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Cloud Service Provider
I livelli di Virtualizzazione 1/4
A che livello eseguire la virtualizzazione?
componenti del sistema.
▪ Interfaccia tra HW e SW (user ISA: istruzioni
macchina non privilegiate, invocabili da ogni
▪ Interfaccia tra HW e SW (system ISA: istruzioni
Sistema: Application Binary
▪ Chiamate di libreria: Application Programming
• Obiettivo della virtualizzazione
▪ Imitare il comportamento di queste interfacce
I livelli di Virtualizzazione 2/4
Cinque livelli di virtualizzazione
• Livello ISA (Instruction Set Architecture).
▪ Si implementa emulando l’ISA, attraverso una traduzione di ogni singola istruzione oppure
attraverso dynamic binary translation (converte in blocchi piuttosto che istruzione per
• Livello Hardware (aka HW Abstraction Layer HAL oppure system VM) .
▪ Bastato su hypervisor.
• Livello Sistema Operativo (aka containers).
• Livello Run-time Library.
• Livello applicazione utente (aka process VM).
I livelli di Virtualizzazione 3/4
I livelli di Virtualizzazione 4/4
VM – Virtualizzazione a livello HW
La Virtualizzazione a livello HW (System Level VM)
• La virtualizzazione a livello HW o system level VM si ottiene attraverso un hypervisor.
• Un Hypervisor è un software di virtualizzazione che permette di eseguire diversi SO
interagendo direttamente con le
contemporaneamente sulla stessa macchina fisica,
risorse fisiche del server. L’hypervisor ha due componenti:
▪ un Kernel – un SO per sistemi operativi;
▪ un Virtual Machine Monitor (VMM), che astrae l’HW per apparire come una
macchina fisica (con CPU, memoria e I/O propri). A volte VMM sinonimo di
• Host – piattaforma base sulla quale sono eseguite le varie VM.
▪ Composta da macchina fisica, opzionalmente SO host, hypervisor.
• Guest – tutto quanto si trova all’interno di una VM.
▪ SO guest e applicazioni eseguite dentro la VM.
La Virtualiz. a livello HW e l’Allocazione delle Risorse
Classificazione della Virtualizzazione a livello HW
Esistono diversi tipi di virtualizzazione a livello HW (o system level virtualization),
distinti in base a:
❖Dove si istanza l’hypervisor:
▪ System hypervisor, o di sistema, chiamato anche type-1, native or bare-metal
▪ Hosted hypervisor, o ospitato, chiamato anche type-2 hypervisor.
❖Come si virtualizzano le istruzioni sensibili e non virtualizzabili.
▪ Full virtualization:
▪ Software-assisted;
▪ Hardware-assisted.
▪ Para-virtualization.
Classificazione della Virtualizzazione a livello HW
Hypervisor di Sistema vs Ospitato 1/2
In quale livello dell’architettura di sistema si colloca l’hypervisor?
➢Direttamente sull’hardware: hypervisor di sistema
➢Sopra il SO host: hypervisor ospitato
Hypervisor di sistema
Hypervisor ospitato
Hypervisor di Sistema vs Ospitato 2/2
• Hypervisor di sistema (type-1): eseguito direttamente sull’hw, offre funzionalità di
virtualizzazione integrate in un SO semplificato (è, di fatto, un SO).
▪ L’hypervisor può avere un’architettura a micro-kernel (solo funzioni di base, no
device driver) o monolitica.
▪ Richiede HW certificato.
▪ Esempi: Xen, KVM (non univocamente riconosciuto), VMware ESX, Hyper-V.
• Hypervisor ospitato (type-2): eseguito sul SO host, accede alle risorse hw tramite le
chiamate di sistema del SO host.
▪ Interagisce con il SO host tramite l’ABI ed emula l’ISA di hw virtuale per i SO guest.
▪ Vantaggio: può usare il SO host per gestire le periferiche ed utilizzare servizi di basso
livello (es. scheduling delle risorse).
▪ Vantaggio: non occorre modificare il SO guest.
▪ Svantaggio: degrado delle prestazioni rispetto a hypervisor di sistema
▪ Esempi: Bochs, Parallels Desktop, VirtualBox.
Full-Virtualization vs Para-Virtualization

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 026_Virtualizzazione_26_-_Infrastruttura_virtuale.md*
