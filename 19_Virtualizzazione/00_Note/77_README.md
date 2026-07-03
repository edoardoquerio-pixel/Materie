# README

**File:** `README.md`
**Tipo:** `.md`
**Dimensione:** 2.1 KB
**Ultima modifica:** 16/06/2026 11:51

---

# Terraform/OpenTofu – Microservices Lab

Questo repository contiene un semplice esercizio su **microservizi** basato su **OpenTofu**.

Sono presenti tre microservizi indipendenti:
- `users`
- `threads`
- `post`

Ogni microservizio espone una **API REST** ed è eseguito in un **container Docker**.
I 3 container rappresentano servizi separati (users, threads, posts) tipici di una architettura microservizi REST.  
Ogni servizio espone un’API HTTP su porta 3000 e gestisce una parte indipendente del dominio applicativo.  

Ogni servizio è un’app Node.js containerizzata con un Dockerfile e buildata come immagine separata.  
I container vengono eseguiti da Terraform usando il provider Docker, con porte mappate (3001–3003) e rete comune.  

I 3 container insieme simulano una mini applicazione di social network (tipo Twitter / Threads / Reddit light).  

users → gestisce gli utenti (chi sei)  
threads → gestisce le discussioni (topic / conversazioni)  
posts → gestisce i messaggi (contenuti dentro le discussioni)  

Esattamente come nei social reali:  
- utente crea thread  
- nel thread ci sono i post  

---

## Prerequisiti
- Docker
- OpenTofu

Verifica:

~$ docker --version  
~$ tofu --version

## Avvio
Clona il repository:
~$ git clone https://github.com/paolobelloni-its/microservices.git  
~$ cd microservices  
La cartella microservices contiene il file main.tf e altre 3 cartelle, ciascuna con dentro un Dockerfile.  

Lanciare i container: spostarsi nella cartella che contiene il file main.tf 
~$ tofu init  
~$ tofu plan  
~$ tofu apply    

Verificare che i container siano attivi:  
~$ docker ps  

## Uso delle API  
~$ curl http://localhost:3001/  
~$ curl http://localhost:3001/api/users  
~$ curl http://localhost:3001/api/users/1  

~$ curl http://localhost:3002/  
~$ curl http://localhost:3002/api/threads/  
~$ curl http://localhost:3002/api/threads/1  

~$ curl http://localhost:3003/  
~$ curl http://localhost:3003/api/posts/by-user/1  
~$ curl http://localhost:3003/api/posts/in-thread/1  

## Arrestare i container  
~$ tofu destroy

