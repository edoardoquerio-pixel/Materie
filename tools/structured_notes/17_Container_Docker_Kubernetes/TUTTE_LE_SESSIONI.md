# 17 - Container Docker Kubernetes — Tutte le Sessioni


---

## Sessione 1: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless DockerCompose


Software Developer
Unità Formativa (UF): Containers, Microservizi -
Docente: Denis Maggiorotto
Titolo argomento: Docker Compose
Cos’è Docker Compose
Docker Compose è uno strumento per definire ed eseguire applicazioni
compose (multi-container) tramite Docker.
Le applicazioni multi-container vengono definite «as code» all’interno di
uno o più file docker-compose.yaml per poi essere eseguite (o terminate)
con un singolo comando.
Tramite Docker Compose è possibile:
Eseguire ambienti applicativi multipli su di un singolo host
Preservare i dati in volumi quando i container vengono creati
Ri-creare solo i container che sono cambiati
Definire variabili che possono poi essere richiamate nel docker-compose.yaml
Suddividere le dichiarazioni in file multipli
Verifica versione
Con Docker for Desktop, l’utility Docker Compose è già installata
Su Linux invece:
"https://github.com/docker/compose/releases/download
/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o
/usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose –version
docker-compose version 1.25.4, build 8d51620a
Prima di Docker Compose
$ docker build -t myapp .
$ docker network create frontend
$ docker network create backend
$ docker run -d --network backend redis:alpine
$ docker run -d -p 5000:5000 --network frontend --name my-application myapp
$ docker network connect backend my-application
Con Docker Compose
$ docker-compose up
Nel file docker-compose.yaml
Esempio di docker-compose.yaml
Avvio (aggiungere –d per background mode)
$ docker-compose up
Verifica container in esecuzione
$ docker-compose ps
Verifica dei logs
$ docker-compose logs
Stop dei container e rimozione
$ docker-compose down
Tutti i comandi docker-compose
List containers
build Build or rebuild services
help Get help on a command
kill Kill containers
logs View output from containers
port Print the public port for a port binding
pull Pulls service images
run Run a one-off command
scale Set number of containers for a service
start Start services
stop Stop services
restart Restart services
up Create and start containers
Remove stopped containers
E’ possibile generare una nuova immagine
E’ possibile referenziare un’immagine
Determina le dipendenze tra container
Utilizzo delle networks
Creazione delle networks
E’ possibile definire variabili d’ambiente
Politica di restart:
- Unless-stopped
Utilizzo dei volumi
Creazione dei volumi
https://github.com/sunnyvale-academy/ITS-ICT_Containers
17 – Docker Compose
04 - Multicontainer application with Docker Compose

---

## Sessione 2: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless FS Layering e Volumi


Cloud Specialist
Unità Formativa (UF): Containers Microservizi
Docente: Denis Maggiorotto
Titolo argomento: FS Layering e Volumi
File System layering
Containers layers
I containers (e le immagini) sono
composti da layers (livelli).
I livelli delle immagini sono Read Only
(RM), il livello dei container è l’unico
Read/Write (RW)
Containers layers
$ docker build -t expressweb .
Step 1 : FROM node:argon
argon: Pulling from library/node...
Status: Downloaded newer image for node:argon
---> 530c750a346e
Step 2 : RUN mkdir -p /usr/src/app
---> Running in 5090fde23e44
---> 7184cc184ef8
Removing intermediate container 5090fde23e44
Step 3 : WORKDIR /usr/src/app
---> Running in 2987746b5fba
---> 86c81d89b023
Removing intermediate container 2987746b5fba
Step 4 : COPY package.json /usr/src/app/
---> 334d93a151ee
Removing intermediate container a678c817e467
Step 5 : RUN npm install
---> Running in 31ee9721cccb
---> ecf7275feff3
Removing intermediate container 31ee9721cccb
Step 6 : COPY . /usr/src/app
---> 995a21532fce
Removing intermediate container a3b7591bf46d
Step 7 : EXPOSE 8080
---> Running in fddb8afb98d7
---> e9539311a23e
Removing intermediate container fddb8afb98d7
Step 8 : CMD npm start
---> Running in a262fd016da6
---> fdd93d9c2c60
Removing intermediate container a262fd016da6
Successfully built fdd93d9c2c60
Containers layers
$ docker run expressweb
Containers layers
Più container creati dalla stessa
immagine, condividono i layers di
quest’ultima con un enorme risparmio
di spazio disco.
Containers layers
$ docker ps -as
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES SIZE
05f427a92591 nginx:1.17.9 "/bin/bash -c 'sleep…" 12 days ago Exited (1) 12 days ago nginx_1 0B (virtual 127MB)
- size is the size on disk for the writable layer of the container; all data written in the container is
stored there, and this is not shared between containers
- virtual size is the size of the "read-only" layer (the image that the container was started from) plus
the size of the writable layer (size).
Copy-on-write strategy
Tutte le modifiche apportate dal container al filesystem sono memorizzate nel layer RW
Quando viene modificato un file esistente (presente nei layer RO dell’immagine), il driver di archiviazione esegue un'operazione di «copyon-write». Per i driver aufs, overlay e overlay2, l'operazione di «copy-on-write» segue questa sequenza:
- Ricerca tra i livelli dell’immagine del file da modificare. Il processo inizia dal livello più recente (top) fino al livello base (down), un livello alla
- Esegue un'operazione di «copy» sulla prima occorrenza del file trovato, per copiarlo nel livello RW del container.
- Le modifiche vengono apportate a questa copia del file e da quel momento il container non può vedere la copia del file esistente nel
livello inferiore (RO).
Dati all’interno dei container
$ docker run -dit --name my_container_1 acme/my-final-image:1.0 bash \
&& docker run -dit --name my_container_2 acme/my-final-image:1.0 bash
38fa94212a419a082e6a6b87a8e2ec4a44dd327d7069b85892a707e3fc818544
1a174fc216cccf18ec7d4fe14e008e30130b11ede0f0f94a87982e310cf2e765
CONTAINER ID IMAGE COMMAND CREATED STATUS
1a174fc216cc acme/my-final-image:1.0 "bash" About a minute ago Up About a minute my_container_2
38fa94212a41 acme/my-final-image:1.0 "bash" About a minute ago Up About a minute my_container_1
$ sudo du -sh /var/lib/docker/containers/*
32K /var/lib/docker/containers/1a174fc216cccf18ec7d4fe14e008e30130b11ede0f0f94a87982e310cf2e765
32K /var/lib/docker/containers/38fa94212a419a082e6a6b87a8e2ec4a44dd327d7069b85892a707e3fc818544
$ sudo ls /var/lib/docker/containers
Dati all’interno dei container
Il layer RW dei container, inizialmente è vuoto ed occupa all’incirca 32KB.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 3: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless YAML


Introduzione a YAML
YAML, che sta per “YAML Ain’t Markup Language”, è un linguaggio per la rappresentazione
delle informazioni.
Nasce come risposta, leggera e leggibile, a XML ed è molto utilizzato soprattutto per la
costruzione di file di configurazione.
A differenza del XML, per definire delle strutture, non si utilizzano i tag annidati, bensì gli spazi
dell’indentazione.
XML vs JSON vs YAML
Inizio del documento
Chiavi e valori
Stringhe multilinea
Array di stringhe
Conventional block
Oggetti annidati
L’indentazione è necessaria ed ottenuta con spazi (minimo 1, preferibile 2)
Array di oggetti
Conventional block
!!binary indica la presenza di un contenuto codificato in Base64
Fine di un documento
YAML è case sensitive
I file devono avere estensione .yaml (i .yml)
Viene usata l’indentazione con spazi per delineare la struttura (oggetti)
Il carattere TAB non è ammesso
I commenti a singola linea hanno il carattere # separato con uno spazio dal testo che
Ulteriori informazioni
• Sito ufficiale: https://yaml.org
• Ulteriori esempi: https://learnxinyminutes.com/docs/yaml/
• Validatore online: http://www.yamllint.com

---

## Sessione 4: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless creiamo immagini


Cloud Specialist
Unità Formativa (UF): Containers Microservizi
Docente: Denis Maggiorotto
Titolo argomento: Creiamo immagini con Docker
Creare un container
Docker con Node.js
FROM image: Inizializza la build e setta l’immagine base sulla quale
vengono eseguite le istruzioni che seguono.
FROM ubuntu:15.1
RUN command: esegue un comando in un nuovo livello, sopra a quelli
dell’immagine corrente e ne esegue la commit. L’immagine risultante viene
usata dalle prossime istruzioni contenute nel Dockerfile.
RUN yum install httpd
EXPOSE port: informa Docker che il container è in ascolto sulle porte di
rete specificate in fase di runtime. È possibile specificare se la porta è in
ascolto su TCP o UDP e il valore predefinito è TCP se il protocollo non è
ENV key[=value]: Serve a settare una variabile d’ambiente che sarà
disponibile all’interno del container. E’ possibile effettuare l’overraid del
valore dal comando docker run.
COPY srcdest : copia nuovi file o directory da <src> e li aggiunge al
filesystem del container nel percorso <dest>
ADD srcdest : copia nuovi file o directory da <src> e li aggiunge al
filesystem del container nel percorso <dest>.
A differenza di COPY, con ADD src può essere una URL, in secondo luogo,
è possibile estrarre un file tar dall'origine direttamente nella destinazione.
ADD http://myhost.com/file.txt /app
USER user[:group]: imposta il nome utente (o UID) e il gruppo utente (o
GID) da utilizzare durante l'esecuzione dell'immagine e per tutte le
istruzioni RUN, CMD ed ENTRYPOINT che lo seguono nel Dockerfile
USER oracle:oracle
WORKDIR dir : imposta la directory di lavoro per tutte le istruzioni RUN,
CMD, ENTRYPOINT, COPY e ADD che seguono nel Dockerfile
ARG nome[=valore di default]: definisce una variabile che gli utenti
possono passare in fase di compilazione con il comando docker build
utilizzando il flag --build-arg <varname>=<valore>.
VOLUME path: crea un punto di mount con il nome specificato e lo
contrassegna come contenente volumi montati esternamente. I volumi
esterni verranno poi montati dall’istruzione docker run
LABEL chiave=’’valore’’ : aggiunge metadati a un'immagine. Una LABEL è
una coppia chiave-valore.
LABEL version="1.0"
ENTRYPOINT commandparam1 param2: Consente di configurare il
processo che verrà eseguito dentro al container. Questo processo non
potrà essere modificato dal comando docker run.
ENTRYPOINT /usr/sbin/apache2ctl –D FOREGROUND
CMD commandparam1 param2: Consente di configurare il processo che
verrà eseguito dentro al container. Questo processo potrà essere
modificato dal comando docker run.
CMD /usr/sbin/apache2ctl –D FOREGROUND
Dockerfile reference
https://docs.docker.com/engine/reference/builder/
https://github.com/sunnyvale-academy/ITSICT_Containers
Lab 06 – Node.js containers
Creare un container
Docker con Java
https://github.com/sunnyvale-academy/ITSICT_Containers
Lab 07 – Java containers
https://github.com/sunnyvale-academy/ITSICT_Containers
Assignment 01 – Create a Redis server image

---

## Sessione 5: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless deployments


Software Developer
Unità Formativa (UF): Containers, Microservizi -
Docente: Denis Maggiorotto
Titolo argomento: Kubernetes Deployments e
maxUnavailable: the maximum number of pods that can be unavailable
during the update process. This can be an absolute number or percentage
of the replicas count; the default is 25%.
maxSurge: the maximum number of pods that can be created over the
desired number of pods. Again this can be an absolute number or a
percentage of the replicas count; the default is 25%.
Deployment rollout and versioning
Deployment strategy
Deployment strategy
Rolling Update (default)
Deployment strategy
Deployment strategy
https://github.com/sunnyvale-academy/ITS-ICT_Containers
20 – ReplicationController
21 – ReplicaSet
22 – Deployment

---

## Sessione 6: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless introduzione


Cloud Specialist
Unità Formativa (UF): Containers Microservizi
Docente: Denis Maggiorotto
Titolo argomento: Introduzione a Docker
Denis Maggiorotto
Denis Maggiorotto
• Managing Director and shareholder @ Sunnyvale S.r.l.
20 years of experience in ICT consulting
Senior Software / Enterprise Architect @ Major companies in public
utility, telco, TV broadcasting and banking sector
• Oracle University Principal Instructor regarding Java technologies
(Micro Edition, Standard Edition and Enterprise Edition) and Oracle's
middleware products.
Independent IT professional trainer and public speaker
Sistemi virtuali
Denis Maggiorotto
denis.maggiorotto@its-ictpiemonte.it
https://www.linkedin.com/in/denismaggiorotto/
https://github.com/denismaggior8
Introduzione a Docker
…partendo dalla virtualizzazione del SO
Tipologie di virtualizzazione
Permette l’esecuzione di un SO su una CPU completamente differente
Virtualizzazione piena (VirtualBox, Qemu)
Esegue copie di SO completi
Poco efficiente
Para-virtualizzazione (UML, Xen)
Esegue SO completi su architetture particolari (es: XEN/x86)
Segregazione delle risorse
Vantaggi della virtualizzazione
Multi SO: Piu` SO sulla stessa macchina ﬁsica, più ambienti di esecuzione (eterogenei).
Sicurezza: eventuali attacchi da parte di malware o spyware sono conﬁnati alla singola macchina
In ambito didattico: invece di assegnare ad ogni studente un account su una macchina ﬁsica, si assegna
una macchina virtuale.
Risorse: Segregazione delle risorse della macchina ﬁsica (Host) su ciascuna macchina virtuale
Difetti della virtualizzazione
Spreco di risorse: le macchine virtuali possono occupare un bel po’ di risorse hardware: ogni macchina
virtuale non esegue solo una copia di un certo sistema operativo ma sfrutta una copia virtuale di tutto
l'hardware di cui lo stesso sistema operativo necessita per funzionare correttamente.
Un approccio che necessita di RAM e che occupa parecchi cicli di CPU. Sempre più economico se
paragonato all'utilizzo di più macchine a sé stanti ma gravoso dal punto di vista dell'occupazione delle
risorse in alcuni frangenti.
Portabilità: Le tecnologie di virtualizzazione oggi presenti sul mercato non sono del tutto interoperabili,
rendendo così le VM poco portabili tra prodotti di virtualizzazione differenti
Perché virtualizzare un’intera macchina, quando sarebbe possibile virtualizzare
solamente una piccola parte di essa?
I container sono una sorta di sistema operativo sempliﬁcato e virtualizzato su
quello ospitante, insieme a tutti i dati di cui necessita un’applicazione per essere
eseguita: librerie, altri eseguibili, rami del ﬁle system, ﬁle di conﬁgurazione e script.
Ogni container vive in un contesto di esecuzione isolato, con un alto livello di
astrazione e segregazione rispetto agli altri container e al sistema operativo
Storia dei container qui: https://www.internetpost.it/container-linux-storiatecnologia/
I containers Docker
Docker è un progetto open-source che semplifica
l'esecuzione di applicazioni all'interno di container,
utilizzando le funzionalità di isolamento delle risorse offerte
dal kernel Linux, come ad esempio cgroup e namespace, per
consentire a container indipendenti di coesistere sulla stessa
istanza di Linux, evitando però l'installazione e la
manutenzione di una macchina virtuale.
Virtual machines vs containers
Virtual machines vs containers
libcontainer: fornisce un'implementazione per la creazione di container con snamespaces,
cgroups, controllo di accesso al ﬁlesystem. Consente di gestire il ciclo di vita del containers
libvirt: libvirt è un'API open source, un demone e uno strumento di gestione di piattaforme
di virtualizzazione (KVM, Xen, VMware ESXi, QEMU)
LXC: è un ambiente di virtualizzazione a container, che opera a livello del sistema operativo
e permette di eseguire diversi ambienti Linux virtuali isolati tra loro (container).
systemd-nspawn: viene utilizzato per eseguire comandi o un SO in un namespace.
Virtualizza completamente la gerarchia del ﬁle system, nonché l'albero dei processi, i vari
sottosistemi IPC e il nome host e dominio.
cgroups: sono una caratteristica del kernel che consente di controllare e limitare l'utilizzo
delle risorse (CPU, memoria, network I/O, disk I/O) da parte di un processo o gruppo di
namespaces: il compito di namespace è quello di permettere l’astrazione delle risorse (IPC,
rete, punto di mount di /, l’albero dei processi, gli utenti e i gruppi, risoluzione del nomi di
rete) e isolarle dal resto del sistema
Vantaggi dei container Docker
Gli stessi di una macchina virtuale, con l’aggiunta di:
▪ Portabilità delle immagini
▪ Dimensioni più contenute

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 7: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes intro


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

## Sessione 8: ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking


Cloud Specialist
Unità Formativa (UF): Containers Microservizi
Docente: Denis Maggiorotto
Titolo argomento: Container networking
Gestione della rete
all'interno dei container
$ docker run -d --net none busybox sleep 1000
3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3
$ docker exec -it
3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3
/ # ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
ping: sendto: Network is unreachable
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
UP LOOPBACK RUNNING MTU:65536 Metric:1
$ docker network ls
NETWORK ID NAME DRIVER SCOPE
8dae0c4d0380 bridge bridge
22530231e5cd host
bd5e44929d16 none null
$ docker run -d --name container_1 busybox sleep 1000
34886a41f5212abd8cd3aa4062479028899e78f32b44103bade6b67d88b76f75
$ docker exec -it container_1 ifconfig
eth0 Link encap:Ethernet HWaddr 02:42:AC:11:00:02
inet addr:172.17.0.2 Bcast:172.17.255.255 Mask:255.255.0.0
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:10 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:796 (796.0 B) TX bytes:0 (0.0 B)
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
UP LOOPBACK RUNNING MTU:65536 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
$ docker run -d --name container_2 busybox sleep 1000
c8c34dad781a7a5778852de2e40fe922f6b4113759b94928d81c4753f7631b9a
$ docker exec -it container_2 ifconfig
eth0 Link encap:Ethernet HWaddr 02:42:AC:11:00:04
inet addr:172.17.0.4 Bcast:172.17.255.255 Mask:255.255.0.0
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:10 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:796 (796.0 B) TX bytes:0 (0.0 B)
lo Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
UP LOOPBACK RUNNING MTU:65536 Metric:1
RX packets:0 errors:0 dropped:0 overruns:0 frame:0
TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:0 (0.0 B) TX bytes:0 (0.0 B)
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms
--- 172.17.0.4 ping statistics ---
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms
--- 172.17.0.4 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.069/0.072/0.076 ms
$ docker exec -it container_1 ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=117 time=33.251 ms
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max = 33.251/33.251/33.251 ms
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
$ docker exec -it container_1 ping 172.17.0.4
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
$ docker exec -it container_1 ping 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
$ docker exec -it container_1 ping 172.17.0.4

*[Contenuto troncato — vedi file originale per dettagli completi]*

---

## Sessione 9: ITS-ICT 2025-2027-CloudSpecialist Microservices intro


2025-2027 Cloud specialist
UF: Containers-Microservices-Servlerless
Docente: Denis Maggiorotto
Denis Maggiorotto
Denis Maggiorotto
• Managing Director and shareholder @ Sunnyvale S.r.l.
20 years of experience in ICT consulting
Senior Software / Enterprise Architect @ Major companies in public
utility, telco, TV broadcasting and banking sector
• Oracle University Principal Instructor regarding Java technologies
(Micro Edition, Standard Edition and Enterprise Edition) and Oracle's
middleware products.
Independent IT professional trainer and public speaker
Denis Maggiorotto
denis.maggiorotto@its-ictpiemonte.it
https://www.linkedin.com/in/denismaggiorotto/
https://github.com/denismaggior8
L'architettura software a microservizi si riferisce ad una tecnica per
progettare applicazioni flessibili ed altamente scalabili,
scomponendo il software in servizi discreti che implementano
specifiche funzioni di business.
Questi servizi possono quindi essere sviluppati, distribuiti e scalati
in modo indipendente.
Ogni microservizio comunica con altri servizi tramite API
(Application Programming Interface) e protocolli standardizzati, e
possono essere scritti in linguaggi differenti o con tecnologie
Ciò differisce completamente dai sistemi costruiti con strutture
monolitiche, in cui i servizi erano inestricabilmente interconnessi, e
potevano essere scalati solo insieme.
Poiché ogni servizio ha una funzionalità ben precisa, è molto più
piccolo in termini di dimensioni e complessità.
Il termine microservizio deriva da questo progetto di funzionalità
discreta, non dalla sua dimensione fisica.
L’architettura a microservizi arriva per risolvere le problematiche di altre due
architettura molto utilizzate in precedenza (e in alcuni casi utilizzate ancora
SOA (Service Oriented Architecture)
Un po’ di storia
Architettura monolitica
L’architettura originale, dalla quale sono derivate le altre
Tutte le componenti software vengono eseguite in un singolo
Non vi è alcun tipo di distribuzione delle sue componenti
Tutte le classi, le librerie ed altre componenti del software
hanno un alto livello di dipendenza fra loro
Spesso ci si riferisce a questi tipi di software col termine «Silo»
Architettura monolitica
Architettura monolitica
Spesso questi software non espongono nessuna interfaccia per
essere utilizzati da altri software (API)
Architettura monolitica
Architettura monolitica
Processo di sviluppo waterfall
Il modello waterfall è una scomposizione delle attività di progetto in fasi
sequenziali e lineari, in cui ciascuna fase dipende dai risultati conseguiti
dalla precedente e costituisce il prerequisito per la fase successiva.
L'approccio è tipico del modello architetturale monolitico.
Nello sviluppo del software, tende ad essere tra gli approcci meno iterativi
e flessibili, poiché il progresso scorre in gran parte in una direzione ("verso il
basso" come una cascata) attraverso le fasi di ideazione, avvio, analisi,
progettazione, costruzione, test, implementazione e manutenzione .
Processo di sviluppo waterfall
Vantaggi architettura monolitica
Più facile da progettare (no rete, no latenza, no protocolli di
comunicazione, tutto in un singolo processo)
E’ più performante (no latenze di rete, no overhead per
serializzazione/deserializzazione oggetti, etc)
E’ più facile da gestire (file di log centralizzati, unico processo da
Service Oriented Architecture (SOA)
Il termine fu coniano nel 1998
Le applicazioni sono composte da processi che espongono servizi al
Ogni servizio «pubblicizza» le proprie funzionalità tramite file
contenenti metadati
E’ modello architetturale che si basa molto sugli standard XML, XML
Schema, XSLT, SOAP, WSDL, etc…
Spesso viene fatto uso di Enterprise Service Bus (ESB) per mediare tra
client e servizi o tra un servizio e l’altro (autenticazione, trasformazione,
adattamento di protocollo)
Service Oriented Architecture (SOA)
Service Oriented Architecture (SOA)
Vantaggi architettura SOA
Dati e funzionalità vengono condivisi in modalità standard

*[Contenuto troncato — vedi file originale per dettagli completi]*


---
*Totale: 9 sessioni generate il 02/07/2026*