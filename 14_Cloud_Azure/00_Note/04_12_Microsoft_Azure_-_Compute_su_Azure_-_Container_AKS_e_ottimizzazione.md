# 12) Microsoft Azure - Compute su Azure - Container, AKS e ottimizzazione

**File:** `12) Microsoft Azure - Compute su Azure - Container, AKS e ottimizzazione.pptx`
**Tipo:** `.pptx`
**Dimensione:** 72.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Compute su Azure: container, AKS e ottimizzazione (4 ore)

---

Compute su Azure
Container, AKS e ottimizzazione

---

Perché arriviamo ai container
•  una VM porta con sé sistema operativo e gestione completa
•  App Service riduce la gestione del server
•  il container impacchetta applicazione e dipendenze in modo ripetibile
•  il problema diventa: dove faccio girare quel container?

---

Container: idea base
•  un container contiene app, runtime e dipendenze
•  parte da un'immagine container
•  gira in modo più leggero di una VM completa
•  non sostituisce sempre la VM: risponde a un modello diverso di distribuzione

---

Container Instances
•  Azure Container Instances esegue container singoli senza gestire server
•  è adatto a prove rapide, job semplici o processi isolati
•  parti da un'immagine e Azure avvia il container
•  è il modo più diretto per eseguire un container su Azure

---

App Service for Containers
•  porta il modello App Service su applicazioni containerizzate
•  utile quando hai una web app dentro un container
•  mantieni funzionalità come dominio, scaling e gestione piattaforma
•  è un ponte tra PaaS web e mondo container

---

Quando serve Kubernetes
•  quando i container diventano molti
•  quando servono replica, aggiornamenti controllati e self-healing
•  quando l'app è composta da più servizi
•  Kubernetes organizza container su un cluster di nodi

---

AKS: Kubernetes gestito
•  AKS è Azure Kubernetes Service
•  Azure gestisce il piano di controllo Kubernetes
•  tu gestisci nodi, workload, networking e aggiornamenti applicativi
•  sotto ci sono VM, ma non le tratti come VM singole

---

Node pool
•  un node pool è un gruppo di nodi con caratteristiche simili
•  i nodi sono le macchine su cui girano i pod
•  puoi avere pool diversi per workload diversi
•  scegliere i nodi significa scegliere costo e capacità del cluster

---

Network in AKS
•  i pod devono comunicare tra loro
•  alcuni servizi devono essere raggiunti dall'esterno
•  entrano in gioco rete del cluster, servizi e ingress
•  qui tornano concetti già visti: subnet, IP, bilanciamento, sicurezza

---

Aggiornamenti in AKS
•  un cluster va aggiornato nel tempo
•  si aggiornano Kubernetes, nodi e applicazioni
•  gli aggiornamenti vanno pianificati per ridurre interruzioni
•  AKS semplifica, ma non elimina la responsabilità operativa

---

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

Ottimizzazione compute
•  scegli il servizio più semplice che risolve il problema
•  spegni o riduci ciò che non serve
•  usa scaling quando il carico cambia
•  misura prima di aumentare risorse
•  collega sempre prestazioni, disponibilità e costo

---

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

Dove guardare nel portale
•  Container instances: container singoli
•  App Services: web app anche containerizzate
•  Kubernetes services: cluster AKS, node pool e aggiornamenti
•  Container registries: immagini container private
•  Cost Management + Billing: costo di VM, piani, funzioni e cluster

---

Chiusura del blocco
•  il compute Azure va da VM a PaaS, serverless e container
•  più sali di livello, meno gestisci server direttamente
•  più lo scenario è complesso, più cresce il bisogno di architettura e controllo
•  da qui il lavoro pratico è scegliere il servizio minimo adatto al caso
