# Lezione 12

Fonte: `12) Microsoft Azure - Compute su Azure - Container, AKS e ottimizzazione.pptx`

### Slide 1

DOCENTE

Federico Laurianti

UNITÀ FORMATIVA

Microsoft Azure (100 ore)

ARGOMENTO

Compute su Azure: container, AKS e ottimizzazione (4 ore)

---

### Slide 2

Compute su Azure

Container, AKS e ottimizzazione

---

### Slide 3

Perché arriviamo ai container

•  una VM porta con sé sistema operativo e gestione completa
•  App Service riduce la gestione del server
•  il container impacchetta applicazione e dipendenze in modo ripetibile
•  il problema diventa: dove faccio girare quel container?

---

### Slide 4

Container: idea base

•  un container contiene app, runtime e dipendenze
•  parte da un'immagine container
•  gira in modo più leggero di una VM completa
•  non sostituisce sempre la VM: risponde a un modello diverso di distribuzione

---

### Slide 5

Container Instances

•  Azure Container Instances esegue container singoli senza gestire server
•  è adatto a prove rapide, job semplici o processi isolati
•  parti da un'immagine e Azure avvia il container
•  è il modo più diretto per eseguire un container su Azure

---

### Slide 6

App Service for Containers

•  porta il modello App Service su applicazioni containerizzate
•  utile quando hai una web app dentro un container
•  mantieni funzionalità come dominio, scaling e gestione piattaforma
•  è un ponte tra PaaS web e mondo container

---

### Slide 7

Quando serve Kubernetes

•  quando i container diventano molti
•  quando servono replica, aggiornamenti controllati e self-healing
•  quando l'app è composta da più servizi
•  Kubernetes organizza container su un cluster di nodi

---

### Slide 8

AKS: Kubernetes gestito

•  AKS è Azure Kubernetes Service
•  Azure gestisce il piano di controllo Kubernetes
•  tu gestisci nodi, workload, networking e aggiornamenti applicativi
•  sotto ci sono VM, ma non le tratti come VM singole

---

### Slide 9

Node pool

•  un node pool è un gruppo di nodi con caratteristiche simili
•  i nodi sono le macchine su cui girano i pod
•  puoi avere pool diversi per workload diversi
•  scegliere i nodi significa scegliere costo e capacità del cluster

---

### Slide 10

Network in AKS

•  i pod devono comunicare tra loro
•  alcuni servizi devono essere raggiunti dall'esterno
•  entrano in gioco rete del cluster, servizi e ingress
•  qui tornano concetti già visti: subnet, IP, bilanciamento, sicurezza

---

### Slide 11

Aggiornamenti in AKS

•  un cluster va aggiornato nel tempo
•  si aggiornano Kubernetes, nodi e applicazioni
•  gli aggiornamenti vanno pianificati per ridurre interruzioni
•  AKS semplifica, ma non elimina la responsabilità operativa

---

### Slide 12

ACI, App Service for Containers, AKS

Se devo...

Scelta naturale

eseguire un container singolo

Container Instances

pubblicare una web app containerizzata

App Service for Containers

orchestrare molti container

AKS

•  la scelta dipende da complessità e responsabilità operativa

---

### Slide 13

Ottimizzazione compute

•  scegli il servizio più semplice che risolve il problema
•  spegni o riduci ciò che non serve
•  usa scaling quando il carico cambia
•  misura prima di aumentare risorse
•  collega sempre prestazioni, disponibilità e costo

---

### Slide 14

Riepilogo del blocco Compute

Scenario

Servizio

controllo completo dell'OS

VM

web app o API gestita

App Service

codice a evento

Functions

container singolo

Container Instances

orchestrazione container

AKS

---

### Slide 15

Dove guardare nel portale

•  Container instances: container singoli
•  App Services: web app anche containerizzate
•  Kubernetes services: cluster AKS, node pool e aggiornamenti
•  Container registries: immagini container private
•  Cost Management + Billing: costo di VM, piani, funzioni e cluster

---

### Slide 16

Chiusura del blocco

•  il compute Azure va da VM a PaaS, serverless e container
•  più sali di livello, meno gestisci server direttamente
•  più lo scenario è complesso, più cresce il bisogno di architettura e controllo
•  da qui il lavoro pratico è scegliere il servizio minimo adatto al caso