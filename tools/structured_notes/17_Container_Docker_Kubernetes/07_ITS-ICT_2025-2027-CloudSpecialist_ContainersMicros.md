# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes intro

## Panoramica
Unità Formativa (UF): Containers, Microservizi -

## Argomenti trattati
Kubernetes, Cloud, Linux, Git, Data Analytics

---
## Appunti

Software Developer
Unità Formativa (UF): Containers, Microservizi -
Docente: Denis Maggiorotto
Titolo argomento: Introduzione a kubernetes
L’orchestratore di container per eccellenza
Dal monolite ai micro servizi
Lo sviluppo diventa agile
Waterfall Vs Agile
Il movimento DevOps
I principi del DevOps (CALMS)
Gli strumenti del DevOps (solo una piccola parte)
Le applicazioni diventano multi container (microservices)
Troppi container?
Perché Kubernetes
Cos’è Kubernetes
Kubernetes is an open source
container orchestration engine for
automating deployment, scaling,
and management of containerized
The open source project is hosted
by the Cloud Native Computing
Kubernetes dal 2017 è il secondo progetto OO dopo Linux
https://github.com/sunnyvale-academy/ITS-ICT_Containers
18 – Kubernetes
L’architettura di
Kubernetes ed il Pod
L’architettura di Kubernetes
L’architettura di Kubernetes
L’architettura di Kubernetes
L’architettura di Kubernetes
Eseguire un’applicazione su Kubernetes
Kubernetes APIs
Kubernetes APIs
Kubernetes APIs
Kubernetes APIs
Multi container Pods
E’ possibile inserire più di un
Container all’interno del Pod.
Questa pratica è utile per
avere uno o più Containers che
supportano il Container
principale (Sidecar pattern)
Quando il carico utente
aumenta, la pratica comune è
quella di aumentare il fattore
di replica dei Pod (le istanze) e
non il numero di container in
Running the first Pod
Running the first Pod
Ogni risorsa Kubernetes
può esser descritta in
YAML, la cui struttura di
base è formata dalle
seguenti chiavi (tutte
apiVersion rappresenta la versione delle API che useremo per creare la nostra
risorsa (in questo caso un Pod). E’ necessario specificare l’apiVersion corretta per
ogni risorsa (vedi tabella).
kind rappresenta il tipo di risorsa da creare. In questo caso il Pod
metadata racchiude delle informazioni fondamentali per il Pod. Qui vediamo il
nome (obbligatorio) ed una label (app). Parleremo delle label in seguito.
spec (specification) racchiude i containers che il Pod avrà al suo interno. La
struttura di spec dipende dal tipo di risorsa (in questo caso Pod).
$ kubectl create –f pod-definition.yml
Altri Pods con YAML
Single container
Multi container
https://github.com/sunnyvale-academy/ITS-ICT_Containers
ReplicationController,
ReplicaSet e Deployment
Pod lifecycle (Pod status)
ReplicationController (deprecato in favore di ReplicaSet)
ReplicationController
ReplicationController
ReplicationController
Per specificare il numero di repliche aggiungiamo:
ReplicationController
$ kubectl create –f rc-definition.yml
$ kubectl get replicationcontroller
$ kubectl get pods
https://github.com/sunnyvale-academy/ITS-ICT_Containers

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_Kubernetes_.md*
