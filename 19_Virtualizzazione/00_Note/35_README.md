# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 4.6 KB
**Ultima modifica:** 15/06/2026 11:35

---

# container-lab

Strumenti utilizzati:
- git
- Docker
 
## Accesso all’ambiente di laboratorio

Verifiche iniziali:

~$ docker --version  
~$ git --version  

Per installare git, da Powershell:  
~$ winget install --id Git.Git -e  

Per installare Docker, da browser:  
https://www.docker.com/products/docker-desktop/  

## Obiettivi
- Capire i comandi base di Docker
- Creare e avviare container manualmente
- Comprendere networking Docker di base

## Esercizio 1

~$ docker run hello-world  

## Preparazione Esercizio 2 ed Esercizio 3

Clonare il repository GitHub corrente su Cloud shell. Attraverso questa operazione saranno scaricate 2 cartelle contenenti i file degli Esercizi 1 e 2.

~$ git clone https://github.com/paolobelloni-its/ITS-Docker.git

## Esercizio 2

~$ spostarsi nella cartella scaricata LISTA

Il programma python (list.py) in questa cartella fa la lista dei file e delle cartelle presenti nella directory corrente.

### Creare immagine

~$ docker build -t immagine-lista .

NOTA: il punto alla fine della riga fa parte del comando!

#### SPIEGAZIONE
docker build: avvia la costruzione di una immagine Docker

-t immagine-lista: assegna un nome (tag) all’immagine costruita

. : indica il contesto di build, cioè la directory corrente (Docker cerca qui il Dockerfile)

Al termine, l’immagine è salvata localmente.
Verificare la presenza dell’immagine con il comando:

~$ docker images

(
nel caso servisse cancellare immagine:

~$ docker rmi nome-immagine

)

Con il comando seguente si possno vedere le caratteristiche dell'immagine:

~$ docker inspect nome-immagine

### Avvio del container

~$ docker run -it immagine-lista

#### SPIEGAZIONE
docker run: crea e avvia un container

-i: mantiene aperto lo standard input

-t: alloca un terminale (TTY)

immagine-lista: nome dell’immagine da usare

Il container viene eseguito in primo piano

Per uscire dal container: exit

### Terminare il container

Per terminare il container:

~$ docker stop <container_id>

Al termine, verificare la lista dei container in esecuzione con il comando:

~$ docker ps  
oppure  
~$ docker ps -a   
per vedere i container sia in esecuzione che terminati.


## Esercizio 3

~$ spostarsi nella cartella scaricata API

Il programma python (list.py) in questa cartella crea un web server (basato su UVICORN) che espone 3 Application Programming Interface sul localhost:
/ - indica che il server e' pronto ed in ascolto
/add/<nome> - inserisce <nome> in un database SQL creato all'interno del container
/lista - mostra i nomi inseriti nel database

A differenza di esercizio 2, il container in esercizio 3 resta in esecuzione finche' non venga terminato.

### Creare immagine

~$ docker build -t immagine-api .

NOTA: il punto alla fine della riga fa parte del comando!

### Avvio del container

~$ docker run -d -p 8000:8000 --name nome-container immagine-api

#### SPIEGAZIONE
-d: lancia il container in background permettendo di usare ancora la command line interface

-p: esponde la porta 8000 interna al container sulla porta 8000 esternamente al container su host (mappa la porta interna al container 8000 sulla porta 8000 dell'host)

--name: assegna un nome al container, di default il nome e' casuale

### Osservare il container

~$ docker inspect nome-container

oppure:

~$ docker stats nome-container

### Gestire le risorse del container in fase di avvio

~$ docker run -m 512m nome-immagine  
limita la RAM del container a 512MB

~$ docker run --cpus=1 nome-immagine  
assegna al container 1 CPU

~$ docker run --cpu-period=100000 --cpu-quota=50000 nome-immagine
assegna al container 1 una quota di 50ms in un periodo di tempo 100ms (equivale ad usare 0.5 CPU)

~$ docker run --pids-limit 50 nome-immagine
limita il numero dei processi in un container a 50

### Terminare il container

Per terminare il container:

~$ docker stop <container_id>  

## Esercizio 4

Voglio utilizzare un programma non installato sulla mia macchina; posso creare un container con un sistema operativo adatto ed installarlo al suo interno.  
Esempio: SQL  

~$ docker run -it --name ubuntu-sql ubuntu bash  
~$~ apt update  
~$~ apt install -y sqlite3  
~$~ sqlite3 test.db  
.exit  
exit  

# Author  

Paolo Belloni  

📧 paolo.belloni@its-ictpiemonte.it

🎓 Course Information  
Institution: ITS Academy ICt Piemonte 
Course: OS e Sistemi di Virtualizzazione  
Language: Labs in Italian  
📄 License  
Educational materials for ITS Academy.  

Last Updated: April 2026  

