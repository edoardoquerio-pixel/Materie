# Virtualizzazione 26 - Infrastruttura virtuale

**File:** `Virtualizzazione 26 - Infrastruttura virtuale.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1959.0 KB
**Ultima modifica:** 02/07/2026 09:25

---

Paolo BELLONI [paolo.belloni@its-ictpiemonte.it]DOCENTE
Sistemi di VirtualizzazioneUnità Formativa
Infrastruttura VirtualeArgomento


P . Belloni  | 
InfrastrutturaVirtuale
Componenti software (softwarizzate, astratte) che abilitano l’esecuzione di
applicazioni senza disporre di una macchina fisica
• Macchine Virtuali
• Container
• K8S
• Cloud Service Provider
2

P . Belloni  | 
I livelli di Virtualizzazione1/4
A che livello eseguire la virtualizzazione?
• Dipende dalle interfacce offerte dai vari
componenti del sistema.
▪ Interfaccia tra HW e SW (user ISA: istruzioni
macchina non privilegiate, invocabili da ogni
programma).
▪ Interfaccia tra HW e SW (system ISA: istruzioni
macchina invocabili solo da programmi
privilegiati).
▪ Chiamate di Sistema: Application Binary
Interface.
▪ Chiamate di libreria: Application Programming
Interface.
• Obiettivo della virtualizzazione
▪ Imitare il comportamento di queste interfacce
3
1
1
2
2
3
4
3 4

P . Belloni  | 
I livelli di Virtualizzazione2/4
Cinque livelli di virtualizzazione
• Livello ISA (Instruction Set Architecture).
▪ Si implementa emulando l’ISA, attraverso una traduzione di ogni singola istruzione oppure
attraverso dynamic binary translation (converte in blocchi piuttosto che istruzione per
istruzione).
• Livello Hardware (aka HW Abstraction Layer HAL oppure system VM) .
▪ Bastato su hypervisor.
• Livello Sistema Operativo (aka containers).
• Livello Run-time Library.
• Livello applicazione utente (aka process VM).
4

P . Belloni  | 
I livelli di Virtualizzazione3/4
5


P . Belloni  | 
I livelli di Virtualizzazione4/4
6


VM – Virtualizzazionea livello HW
7

P . Belloni  | 
La Virtualizzazionea livello HW (System Level VM)
• La virtualizzazione a livello HW o system level VM si ottiene attraverso un hypervisor.
Definizioni
• Un Hypervisor è un software di virtualizzazione che permette di eseguire diversi SO
contemporaneamente sulla stessa macchina fisica, interagendo direttamente con le
risorse fisiche del server. L’hypervisor ha due componenti:
▪ un Kernel – un SO per sistemi operativi;
▪ un Virtual Machine Monitor (VMM), che astrae l’HW per apparire come una
macchina fisica (con CPU, memoria e I/O propri). A volte VMM sinonimo di
hypervisor.
• Host – piattaforma base sulla quale sono eseguite le varie VM.
▪ Composta da macchina fisica, opzionalmente SO host, hypervisor.
• Guest – tutto quanto si trova all’interno di una VM.
▪ SO guest e applicazioni eseguite dentro la VM.
8

P . Belloni  | 
La Virtualiz. a livello HW e l’ Allocazionedelle Risorse
9


P . Belloni  | 
Classificazionedella Virtualizzazionea livello HW  
Esistono diversi tipi di virtualizzazione a livello HW (o system level virtualization),
distinti in base a:
❖Dove si istanza l’hypervisor:
▪ System hypervisor, o di sistema, chiamato anche type-1, native or bare-metal 
hypervisor;
▪ Hosted hypervisor, o ospitato, chiamato anche type-2 hypervisor.
❖Come si virtualizzano le istruzioni sensibili e non virtualizzabili.
▪ Full virtualization:
▪ Software-assisted;
▪ Hardware-assisted.
▪ Para-virtualization.
10

P . Belloni  | 
Classificazione della Virtualizzazione a livello HW 
11
Container

P . Belloni  | 
Hypervisor di Sistema vs Ospitato 1/2
In quale livello dell’architettura di sistema si colloca l’hypervisor?
➢Direttamente sull’hardware: hypervisor di sistema
➢Sopra il SO host: hypervisor ospitato
12
Hardware
Hypervisor
Hardware
Hypervisor
Host OS
Application
Guest OS-1
VM-1
Application
Guest OS-n
VM-n
Application
Guest OS-1
VM-1
Application
Guest OS-n
VM-n
Host Guest
Host Guest
Hypervisor di sistema Hypervisor ospitato

P . Belloni  | 
Hypervisor di Sistema vs Ospitato 2/2
• Hypervisor di sistema (type-1): eseguito direttamente sull’hw, offre funzionalità di
virtualizzazione integrate in un SO semplificato (è, di fatto, un SO).
▪ L’hypervisor può avere un’architettura a micro-kernel (solo funzioni di base, no
device driver) o monolitica.
▪ Richiede HW certificato.
▪ Esempi: Xen, KVM (non univocamente riconosciuto), VMware ESX, Hyper-V.
• Hypervisor ospitato (type-2): eseguito sul SO host, accede alle risorse hw tramite le
chiamate di sistema del SO host.
▪ Interagisce con il SO host tramite l’ ABIed emula l’ISA di hw virtuale per i SO guest.
▪ Vantaggio: può usare il SO host per gestire le periferiche ed utilizzare servizi di basso
livello (es. scheduling delle risorse).
▪ Vantaggio: non occorre modificare il SO guest.
▪ Svantaggio: degrado delle prestazioni rispetto a hypervisor di sistema
▪ Esempi: Bochs, Parallels Desktop, VirtualBox.
13

P . Belloni  | 
Virtualizzazione completa (full)
▪ L’hypervisor espone ad ogni VM interfacce hw
simulate funzionalmente identiche a quelle
della sottostante macchina fisica.
▪ L’hypervisor intercetta le richieste di accesso
privilegiato all’hw (ad es. istruzioni di I/O) e ne
emula il comportamento atteso.
▪ Esempi: KVM, VMware ESXi, Microsoft Hyper-
V.
Full-Virtualization vs Para-Virtualization
Quale modalità di dialogo tra la VM e hypervisor per l’accesso alle risorse fisiche,
ovvero come gestire l’esecuzione di istruzioni privilegiate?
➢Virtualizzazione completa
➢Paravirtualizzazione
14
Para-Virtualizzazione
▪ L’hypervisor espone ad ogni VM interfacce hw
simulate funzionalmente simili (ma non
identiche) a quelle della sottostante macchina
fisica.
▪ Non viene emulato l’hw, ma viene creato uno
strato minimale di sw (Virtual Hardware API)
per assicurare la gestione delle VM ed il loro
isolamento.
▪ Esempi: Xen, Oracle VM (basato su Xen),
PikeOS.

P . Belloni  | 
Riassumendo i diversi approcci di Virtualizzazione
15
Host Hardware (x86)
Ring 3
Ring 2
Ring 1
Ring 0
User Apps
Hypervisor
Guest OS
User Apps
Hypervisor
Para-virtualized
Guest OS
User Apps
Hypervisor
Guest OS
Hypercall
Binary Translation
OS Request Trap to VMM
Paravirtualization Full Virtualization HW-Assisted
Xen, KVM VMware ESX/ESXi, 
Microsoft Hyper-V 
Intel VT-x, AMD-V

P . Belloni  | 
L’operativitàdella Virtual Machine (VM)
• Dal punto di vista dell’utente, una VM è
un logical compute system (sistema
logico per il processamento dei dati).
▪ Lavora su un SO e ha applicazioni come
una macchina fisica.
▪ Dispone di componenti virtuali come
CPU, RAM, dischi e interface di rete.
▪ Dal punto di vista dell’hypervisor invece:
▪ Una VM è un insieme discreto di file (file
di configurazione, file di dischi virtuali,
file di virtual BIOS, file di VM swap e log
file).
16Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
SERVER
VM1 VM3VM2
Hypervisor
Driver
CPU
Driver Driver
NIC
Driver
DISKMemory
OS2 OS2
ApplicationApplication
OS1
Application

P . Belloni  | 
I file della Virtual Machine (VM) 1/2
17Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
I file della Virtual Machine (VM) 2/2
18Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
DescriptionUsageFile
Virtual machine configuration filevmname.vmx.vmx
Additional virtual machine 
configuration files
vmname.vmxf.vmxf
Virtual disk characteristicsvmname.vmdk.vmdk
Virtual machine data diskvmname-flat.vmdk-flat.vmdk
Virtual machine BIOS or EFI 
configuration
vmname.nvram or nvram.nvram
Virtual machine paging backup filevmname.vmem.vmem
Virtual machine snapshots 
information (metadata) file
vmname.vmsd.vmsd
Virtual machine memory snapshot 
file
vmname.vmsn.vmsn
Virtual machine swap filevmname.vswp.vswp
Virtual machine suspend filevmname.vmss.vmss
Current virtual machine log filevmware.log.log
Old virtual machine log filesvmware-#.log (where # is a number 
starting with 1)
-#.log
Scoreboard files contain 
performance information about 
the VM
vmware-#.scoreboard (where # is a
number starting with 1)
.scoreboard
Location: storage/datastore1/vmname

P . Belloni  | 
I file system per la gestione dei file di VM
19Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011
I file system (formati) supportati da hypervisor sono:
• Virtual Machine File System (VMFS).
▪ È un file aggregato che permette alle diverse macchine fisiche di
leggere/scrivere sullo stesso storage contemporaneamente.
▪ Può essere istanziato su storage esterno FC e iSCSI, oltre che su storage locale.
• Network File System (NFS).
▪ Abilita l’archiviazione dei file di VM su un file server remoto (Network
Attached Storage NAS).
▪ Il client NFS è implementato in hypervisor.

P . Belloni  | 
L’HW della Virtual Machine
20Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011


P . Belloni  | 
I componentiHW della Virtual Machine (VM)
21Source: EMC2, Cloud Infrastructure and Service, Student Guide, 2011

Container – Virtualizzazionea 
livello SO
22

P . Belloni  | 
La Virtualizzazionea livello di SO 1/2
• Finora abbiamo considerato la virtualizzazione a livello hardware.
• Analizziamo ora la virtualizzazione a livello di sistema operativo (o container-
based virtualization).
• Permette di eseguire molteplici ambienti di esecuzione tra di loro isolati
all’interno di un singolo SO.
▪ Tali ambienti sono chiamati:
➢container;
➢jail;
➢zone;
➢virtual execution environment (VE).
23

P . Belloni  | 
La Virtualizzazionea livello di SO 2/2
24
Type 1
Virtualizzazione a livello SOVirtualizzazione a livello HW
Type 2
Heavy-weight Light-weight
Hardware
Container Engine
OS
Application
Container-1
Application
Container-n

P . Belloni  | 
La Virtualizzazionea livello di SO: Vantaggi
Rispetto alla virtualizzazione a livello HW.
• Minimo degrado delle prestazioni.
➢ Le applicazioni invocano direttamente le system call, senza mediazioni di hypervisor.
• Tempo di startup e shutdown minimi.
➢ Secondi per container, minuti per VM.
• Alta densità.
➢ Centinaia di istanze sulla singola macchina fisica (PM).
• Dimensione dell’immagine più piccola (footprint).
➢ Non include il kernel di SO.
• Possibilità di condividere le pagine di memoria tra i diversi container in esecuzione sulla
stessa PM.
• Portabilità e interoperabilità migliori.
• Le applicazioni su container sono indipendenti dall’ambiente di esecuzione.
25

P . Belloni  | 
La Virtualizzazionea livello di SO: Svantaggi
Rispetto alla virtualizzazione a livello HW.
• Minore flessibilità.
➢Non posso coesistere diversi SO sulla stessa PM.
• Solo applicazioni native per i SO supportati (p. es. solo applicazioni native per
Linux).
• Meno isolamento.
• Maggiore rischio di vulnerabilità.
• La singola vulnerabilità nel kernel di SO compromette l’intero sistema.
26

P . Belloni  | 
Confrontotra Virtualizzazionea livello HW vs SO
27


P . Belloni  | 
Metodologieper Virtualizzazionea livello di SO (1)
• Il kernel del SO consente l’esistenza di diverse istanze isolate di spazi d’utente, chiamate
container, che condividono però le risorse (di CPU, memoria e storage) di un SO host.
• Ogni container è costituito da:
➢ insieme di processi;
➢ file system;
➢ utenti;
➢ interface di rete con relativi indirizzi IP;
➢ tabelle di routing;
➢ regole di configurazione del firewall, … .
• I container condividono lo stesso SO, in particolare, il kernel di SO.
28


P . Belloni  | 
Solo Linux?
• Windows e OS X supportano la virtualizzazione basata su container.
➢Docker Desktop è una applicazione per Windows e Mac (o Linux) che
permette di installare un Docker Engine su Windows OS > 10 o MacOS.
• Alternative: installare una VM con Linux come guest OS e utilizzare la
virtualizzazione basata su SO all’interno della VM.
➢Ovviamente, impatto sulle prestazioni.
➢Le applicazioni containerizzate devono girare su Linux (non sono possibili
applicazioni native OS X o Windows).
29

P . Belloni  | 
I container abilitano nuove tecnologie
• In sintesi, l’uso dei container permette di avere l’applicazione e tutte le sue
dependencies (tutto il sw che serve per farla funzionare correttamente, in pratica
i file bins/libs – binary e le librerie) in un singolo “contenitore”, che permette
quindi di eseguirlo pressoché in ogni ambiente.
• I container risultano più efficienti rispetto alle VM, perché utilizzano meno
risorse.
Inoltre,
• I container sono la tecnologia chiave per abilitare i micro-servizi (microservice) e il
cloud serverless (serverless computing).
30

P . Belloni  | 
I Microservice
31


P . Belloni  | 
Container as a Service – CaaS
• Anche la tecnologia di virtualizzazione a livello di SO, basata su container, viene
usata dai provider per offrire i servizi del Cloud. Si parla in questo caso di
Container as a Service.
• Il servizio cloud di CaaS permette di sviluppare e gestire delle applicazioni usando
i container.
• Il CaaS si colloca tra IaaS e PaaS. Tuttavia sarebbe più appropriato classificarlo
come un sottocaso di IaaS, in cui la risorsa base è rappresentata dal container.
• Tecnologia ampiamente diffusa sul mercato:
➢Amazon Elastic Container Service (ECS);
➢Microsoft Azure Container;
➢Google Container Engine;
➢Alauda (CaaS solution);
➢Docker Cloud.
32

P . Belloni  | 
Container Orchestration
• Quando un’applicazione è costituita da più container (multi-container application),
distribuiti in cluster dinamici su larga scala, si rende necessario l’utilizzo di una
piattaforma funzionale che gestisca il ciclo di vita dei suoi container costituenti.
• Questa piattaforma prende il nome di Orchestrator.
• L’orchestrator permette di configurare, attivare/istanziare (deployment), monitorare e
controllare dinamicamente le applicazioni su container. Di fatto, integra e gestisce i
container allocando le risorse rese necessarie dalle richieste degli utenti.
• Alcuni esempi:
➢ Kubernetes (K8s);
➢ Docker Swarm;
➢ Amazon Elastic Container Service;
➢ Google Kubernetes Engine;
➢ Marathon;
➢ Nomad (container orchestrator per Mesos).
33
Servizi Cloud “fully-managed”

P . Belloni  | 
Il modello Google: tutto è su container
• Da anni Google ha cambiato il suo paradigma di gestione dei DC, da V-DC
machine-oriented a V-DC application-oriented.
• Questo application-oriented shift, come viene chiamato, è stato possibile grazie
alla trasformazione dei V-DC utilizzando la tecnologia dei container.
• “Goal: let container technology operate at Google scale.
▪ Everything at Google runs in containers.
▪ Google launches several billion containers per week into Google Cloud”.
• Fondamentale il ruolo di un orchestrator nell’ottenere tali strabilianti prestazioni.
▪ Borg and Omega, sono sistemi proprietari puramente interni a Google,
predecessori di Kubernetes.
▪ Kubernetes: piattaforma di container orchestration open-source.
34

P . Belloni  | 
Kubernetes (K8s)
• “Google’s Kubernetes, also known as K8s, is an open-source system for
automating deployment, scaling, and management of containerized applications”.
• http://kubernetes.io
• Principali caratteristiche:
➢Portable: public, private, hybrid, multi-cloud;
➢Extensible: modular, pluggable, hookable, composable;
➢Self-healing: auto-placement, auto-restart, auto-replication, auto-scaling of
containers.
• Funziona su piattaforme di cloud pubblico e privato (AWS, Microsoft Azure,
OpenStack, Apache Mesos) e anche su bare metal.
• Standard di fatto, offerto dalla maggioranza dei provider come servizio Cloud.
35
Source: http://kubernetes.io


P . Belloni  | 
Kubernetes (K8s): Pod
• Pod: the smallest deployable units of computing that you can create and manage in
Kubernetes.
• A Pod (as in a pod of whales or pea pod) is a group of one or more (tightly coupled)
containers, with shared storage and network resources, and a specification for how to
run the containers.
• A Pod's contents are always co-located and co-scheduled, and run in a shared context.
• The shared context of a Pod is a set of Linux namespaces, cgroups, and potentially other
facets of isolation - the same things that isolate a container. So a Pod is similar to a set of
containers with shared namespaces and shared filesystem volumes.
• Kubernetes gives pods their own IP addresses and a single DNS name for a set of pods, 
and can load-balance across them.
• Users organize pods using labels:
▪ Label: arbitrary key/value pair attached to pod;
▪ E.g., role=frontend and stage=production.
36Source: http://kubernetes.io


P . Belloni  | 
Kubernetes (K8s): architettura1/3
37Source: https://kubernetes.io/docs/concepts/overview/components/


P . Belloni  | 
Kubernetes (K8s): architettura2/3
38Source: https://kubernetes.io/docs/concepts/overview/components/


P . Belloni  | 
Kubernetes (K8s): architettura3/3
39
• L’architetturadi K8s è organizzata secondo un framework master-worker.


P . Belloni  | 
Un approccio innovativoallo sviluppo del sw 1/3
• I container forniscono una nuovo modo per costruire, impacchettare, condividere
e distribuire le applicazioni.
• In particolare, i container supportano l’introduzione di nuove metodologie per lo
sviluppo e la distribuzione del sw: CI/CD e DevOps e Agile.
40
• Continuous Integration and Continuous
Deployment CI/CD: questo paradigma
descrive le fasi chiave in un flusso
automatico di sviluppo e distribuzione del
sw. Questo flusso include design, coding,
testing, integrazione, delivery, validation e
deployment, prima della fase di operation
nell’ambiente finale.
• I container (più della VM) permettono agli
sviluppatori di creare codice in modo
collaborativo, condividendo facilmente le
immagini sw, mentre semplificano la
distribuzione verso le differenti
infrastrutture.


P . Belloni  | 
Un approccio innovativoallo sviluppo del sw 2/3
41
• Development and Operations
DevOps: Metodologia di sviluppo sw
creata per ridurre o eliminare il divario
tra sviluppo e operation, enfatizzando
comunicazione, collaborazione,
integrazione, quality assurance e
delivery con un deployment
automatico.
• Di fatto, la metodologia vuole
bilanciare l’aspirazione per veloci
cambiamenti del team di sviluppo con
il desiderio di stabilità del team di
operation, attraverso comunicazione e
collaborazione efficaci.


P . Belloni  | 
Un approccio innovativoallo sviluppo del sw 3/3
42
• DevOps è una pratica di sviluppo agile e una
mentalità che utilizza principi agili
(collaborazione, comunicazione, utilizzo degli
strumenti giusti) per semplificare la
costruzione, il test e il rilascio del software.
• CI/CD è una tattica DevOps, che utilizza i giusti
strumenti di test automatizzati per
implementare lo sviluppo agile.
• Agile è un ampio framework che comprende le
altre due pratiche. Si concentra sui processi
che evidenziano il cambiamento mentre
accelera la distrubuzione. È una filosofia di
sviluppo software che viene implementata in
varie metodologie: Scrum, Kanban, Scaled
Agile Framework (SAFe), ecc.
• Tutte e tre le pratiche hanno lo stesso
obiettivo: creare software migliore in minor
tempo. Queste pratiche si sovrappongono
quasi sempre.


IaC
43

P . Belloni  | 
Infrastructure as Code (IaC)
• Infrastructure as Code (IaC) è un approccio che permette di definire, creare e gestire
l’infrastruttura IT tramite codice, invece di configurazioni manuali.
• Concetti chiave:
✓ Infrastruttura descritta con file di testo
✓ Versionabile (Git)
✓ Automatizzabile e ripetibile (idempotenza)
✓ Specifico lo stato desiderato (IaC dichiarativa, la più recente [2010] vs IaC procedurale/imperativa)
• Quale infrastruttura?
➢ Container Docker
➢ Volumi e reti
➢ VM e cluster Kubernetes (anche su AWS o Azure)
• Esempio: creo VM, rete e storage scrivendo codice invece di usare una console cloud
44

P . Belloni  | 
Infrastructure as Code (IaC): Perchè?
• IaC risolve i limiti della gestione manuale
✓Coerenza tra ambienti (dev / test / prod)
✓Riproducibilità dell’infrastruttura
✓Riduzione degli errori umani
✓Velocità di creazione degli ambienti
• Il configuration drift è la situazione in cui lo stato reale
dell’infrastruttura non coincide più con lo stato definito nel
codice (IaC).
➢In pratica: il codice dice una cosa, l’infrastruttura reale ne fa un’altra
✓Qualcuno modifica a mano un server (SSH, console cloud)
✓Una configurazione cambia fuori dal codice
✓Script procedurali vengono eseguiti solo parzialmente
45

P . Belloni  | 
Infrastructure as Code (IaC)
Come si usa (flusso tipico)?
• Scrivo codice IaC
• Versiono su Git
• plan → anteprima
• apply → crea/modifica infrastruttura
46

P . Belloni  | 
Infrastructure as Code (IaC): dichiarativavs 
procedurale
1. Crea una VM
2. Installa Docker
3. Avvia il container
4. Crea directory
Descrive i passi da eseguire,
nell’ordine, per ottenere
l’infrastruttura desiderata
47
Voglio:
- 1 VM
- 1 container in esecuzione
- 1 volume persistente
Descrive lo stato finale
desiderato dell’infrastruttura,
senza specificare i passi per
arrivarci

P . Belloni  | 
Infrastructure as Code (IaC): Come si implementa?
• File di definizione (codice)
• Motore che applica lo stato desiderato
Dipendenze tecnologiche: IaC non vive da sola, dipende da:
➢Virtualizzazione (VM, hypervisor)
➢Container (Docker, Kubernetes)
➢Cloud (pubblico, privato, ibrido)
➢API dell’infrastruttura
• IaC non è solo cloud: vale anche per data center on-prem
• Use case: Creare ambienti test e produzione identici
48

P . Belloni  | 
Infrastructure as Code (IaC): Architettura
[ File IaC ]     
↓
[ Motore IaC ]     
↓
[ Provider / Driver ]
↓
[ Infrastruttura reale ]
49

P . Belloni  | 
Infrastructure as Code (IaC): Come si implementa?
• Il motore è il componente che interpreta il codice IaC e lo
trasforma in azioni reali sull’infrastruttura, chiamando le API del
cloud o della piattaforma sottostante
• Cosa fa concretamente un motore IaC?
➢Legge il codice/template (YAML, JSON, HCL, Bicep, ecc.)
➢Valida che sia corretto
➢Calcola lo stato desiderato
➢Confronta lo stato desiderato con quello reale
➢Decide le operazioni da eseguire (create / update / delete)
➢Chiama le API dell’infrastruttura
➢Tiene traccia dello stato (implicitamente o esplicitamente)
50

P . Belloni  | 
Infrastructure as Code (IaC): Linguaggi e Strumenti
51
Uso tipicoTipoOpen SourceProduttoreLinguaggioStrumento
Multi-cloudDichiarativoParzialeHashiCorpHCLTerraform
Fork di 
Terraform per 
restare open-
source
DichiarativoSìLinux 
FoundationHCLOpenTofu
Configurazione
OS/appProceduraleSìRed HatYAMLAnsible
Solo AWSDichiarativoNoAWSYAML/JSONCloudFormation
Solo AzureDichiarativoSi Microsoft AzureBicep/ARM JSONARM

P . Belloni  | 
Infrastructure as Code (IaC): Vantaggi
• Source of Truth: il codice è la verità ufficiale
• Ambienti coerenti e ripetibili
• Automazione e velocità
• Base del DevOps
• Integrazione con GitHub
✓Codice IaC in repository Git
✓Pull Request = modifica infrastruttura
✓CI/CD → deploy automatico dell’infra
❑ATT: errore di codice = errore di infra!
52

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
aws = {
source = "hashicorp/aws"
version = "~> 5.0"
}
}
}
53

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
aws = {
source = "hashicorp/aws"
version = "~> 6.0"
}
}
}
provider "aws" {
region = "eu-west-1" # esempio: Irlanda
}
############################################
# 2. Region corrente (lettura dinamica)
############################################
data "aws_region" "current" {}
54

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
############################################
# 3. Availability Zones
# Le AZ sono unità di isolamento fisico
# Concettualmente ≃ datacenter
############################################
data "aws_availability_zones" "available" {
state = "available"
}
############################################
# 4. VPC esistente
# In AWS la VPC è il perimetro di rete principale
############################################
data "aws_vpc" "selected" {
tags = {
Name = "main-vpc"
}
}
55

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
############################################
# 5. Subnet esistente
# Le subnet sono sempre:
# - dentro una VPC
# - associate a UNA sola AZ
############################################
data "aws_subnet" "public_a" {
vpc_id = data.aws_vpc.selected.id
availability_zone = data.aws_availability_zones.available.names[0]
tags = {
Name = "public-a"
}
}
56

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
############################################
# 6. Security Group
# Firewall STATEFUL
# Associato a ENI / EC2 / LB
############################################
data "aws_security_group" "web_sg" {
name = "web-sg"
vpc_id = data.aws_vpc.selected.id
}
############################################
# 7. Network ACL (NACL)
# Firewall STATELESS
# Associato alle subnet
############################################
data "aws_network_acl" "main" {
vpc_id = data.aws_vpc.selected.id
tags = {
Name = "main-nacl"
}
}
57

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
azurerm = {
source = "hashicorp/azurerm"
version = "~> 3.0"
}
}
}
58

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
google = {
source = "hashicorp/google"
version = "~> 5.0"
}
}
}
59

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
kubernetes = {
source = "hashicorp/kubernetes"
version = "~> 2.0"
}
}
}
60

P . Belloni  | 
Infrastructure as Code (IaC):
alcuni provider ufficiali Terraform
terraform {
required_providers {
vsphere = {
source = "hashicorp/vsphere"
version = "~> 2.0"
}
}
}
61
