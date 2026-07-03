# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless DockerCompose

## Panoramica
Unità Formativa (UF): Containers, Microservizi -

## Argomenti trattati
Docker, Linux, Git, API REST

---
## Appunti

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
*Fonte: 2025_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_DockerCompo.md*
