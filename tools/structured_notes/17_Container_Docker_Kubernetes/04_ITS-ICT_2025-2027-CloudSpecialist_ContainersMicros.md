# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless creiamo immagini

## Panoramica
Unità Formativa (UF): Containers Microservizi

## Argomenti trattati
Cloud, Docker, Reti, Git

---
## Appunti

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
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_creiamo_imm.md*
