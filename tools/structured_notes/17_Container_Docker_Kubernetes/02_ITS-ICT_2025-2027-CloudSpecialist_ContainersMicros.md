# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless FS Layering e Volumi

## Panoramica
Unità Formativa (UF): Containers Microservizi

## Argomenti trattati
Cloud, Docker, Data Analytics, Git, API REST

---
## Appunti

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
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_FS_Layering.md*
