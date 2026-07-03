# Linux Server e Amministrazione — Appunti Strutturati

> **Corso:** ITS ICT Cloud Specialist 2025-2027
> **Materia:** 16_Linux_Server_e_Amministrazione

---

## Installazione e Fondamenti

### 📄 14 Linux Server 01 Installazione Debian

**File:** [`14_Linux_Server_01_Installazione_Debian.md`](00_Note/14_Linux_Server_01_Installazione_Debian.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Intallazione Debian 


  2 
Architetture 
 
Differenze nelle architetture: 
 
- Server fisico; 
- Virtual Machine(s); 
- Containers; 
- Cloud; 
- Serverless. 
 
Bare Metal vs. 

*[continua...]*

---

### 📄 15 Linux Server 02 Comandi Essenziali

**File:** [`15_Linux_Server_02_Comandi_Essenziali.md`](00_Note/15_Linux_Server_02_Comandi_Essenziali.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Installazione Debian e Comandi Essenziali 

 
  2 
 
 
 
Programma odierno: 
 
- Leggere e scrivere files; 
- Muoversi nelle directories; 
- Creare utenti; 
- Substitute Use

*[continua...]*

---

## Utenti e Permessi

### 📄 16 Linux Server 03 utenti e permessi

**File:** [`16_Linux_Server_03_utenti_e_permessi.md`](00_Note/16_Linux_Server_03_utenti_e_permessi.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Utenti e permessi 

 
2 
 
 
 
In Debian è possibile utilizzare: 
# useradd 
 
O meglio ancora: 
# adduser  
Per aggiungere utenti. 
 
# useradd 
 
# useradd -D alberto 
# us

*[continua...]*

---

### 📄 39 Linux Server permessi speciali

**File:** [`39_Linux_Server_permessi_speciali.md`](00_Note/39_Linux_Server_permessi_speciali.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Permessi speciali 

[Digitare qui] 
 
 
 
1. Sticky Bit 
Lo sticky bit e un permesso speciale in Linux/Unix che si comporta in modo diverso a seconda che 
venga applicato a una

*[continua...]*

---

## SSH e Reti

### 📄 25 Linux Server 04 SSH

**File:** [`25_Linux_Server_04_SSH.md`](00_Note/25_Linux_Server_04_SSH.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
SSH 


 
2 
SSH (Secure Shell) 
 
SSH è un servizio (ma anche un protocollo) che consente la 
comunicazione sicura via rete (sicura perché crittografata) tra un 
client e un 

*[continua...]*

---

### 📄 26 Linux Server 05 dns hosts

**File:** [`26_Linux_Server_05_dns_hosts.md`](00_Note/26_Linux_Server_05_dns_hosts.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
DNS, file hosts 


 
2 
 
 
Lo scopo di assegnare dei nomi agli indirizzi IP è quello di rendere più facile la 
memorizzazione per le persone. In verità, un indirizzo IP ide

*[continua...]*

---

### 📄 40 Linux Server schede di rete

**File:** [`40_Linux_Server_schede_di_rete.md`](00_Note/40_Linux_Server_schede_di_rete.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Impostazione schede di rete 

 
 
Eventualmente fare uno snapshot della macchina virtuale. 
 
La macchina dovrebbe avere già una scheda di rete NAT. 
 
Impostare una seconda sc

*[continua...]*

---

### 📄 42 networking linux doc

**File:** [`42_networking_linux_doc.md`](00_Note/42_networking_linux_doc.md)

Networking in Linux — ITS Academy 
 
Networking in Linux 
Lezione — Linux Server | ITS Academy 
1. Introduzione 
La configurazione di rete è una competenza fondamentale per chi amministra un server 
Linux. In questa lezione vedremo come funziona lo s

*[continua...]*

---

### 📄 43 networking linux

**File:** [`43_networking_linux.md`](00_Note/43_networking_linux.md)

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Networking

Networking
in Linux
Configurazione, diagnostica e gestione della rete
Linux Server  |  ITS Academy

Agenda
Networking in Linux — ITS Academy
• 1.  Concetti fondamentali — st

*[continua...]*

---

### 📄 47 risoluzione problema rete Debian

**File:** [`47_risoluzione_problema_rete_Debian.md`](00_Note/47_risoluzione_problema_rete_Debian.md)

# risoluzione problema rete Debian 3
# tira su l'interfaccia a mano con l'IP tipico di VirtualBox NAT:

sudo ip link set enp0s3 up
sudo ip addr add 10.0.2.15/24 dev enp0s3
sudo ip route add default via 10.0.2.2
echo "nameserver 8.8.8.8" | sudo tee /e

*[continua...]*

---

## Web Server e DB

### 📄 28 Linux Server 06 http server

**File:** [`28_Linux_Server_06_http_server.md`](00_Note/28_Linux_Server_06_http_server.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Httpd Server: nginx, Apache 

 
2 
Negoziazione Client-Server e status code 
 
Riferimenti: 
 
Architettura 
https://developer.mozilla.org/en-US/docs/Learn/Server-
side/First

*[continua...]*

---

### 📄 29 Linux Server 061 http server esercizio

**File:** [`29_Linux_Server_061_http_server_esercizio.md`](00_Note/29_Linux_Server_061_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio sulla creazione di un sito 

 
 
Esercizio 
 
 
- Creare il dominio socrate.local 
 
• Associare il webserver al dominio socrate.local 
• Servire uno più file html

*[continua...]*

---

### 📄 30 Linux Server 062 http server esercizio

**File:** [`30_Linux_Server_062_http_server_esercizio.md`](00_Note/30_Linux_Server_062_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio sulla creazione di un sito 

 
 
 
 
Esercizio 
 
 
Create i siti 
 
moleantonelliana.local 
palazzomadama.local 
 
Scaletta: 
 
 
Creare il dominio moleantonellian

*[continua...]*

---

### 📄 31 Linux Server 063 http server esercizio

**File:** [`31_Linux_Server_063_http_server_esercizio.md`](00_Note/31_Linux_Server_063_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
 
 
 
Esercizio 
 
Premesse 
 
- Abbiamo creato il sito: 
 
tuoCognome.local 
 
(se non è stato creato, è necessario crearlo); 
 
- Abbiamo

*[continua...]*

---

### 📄 32 Linux Server 064 http server esercizio

**File:** [`32_Linux_Server_064_http_server_esercizio.md`](00_Note/32_Linux_Server_064_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Esercizio sulla configurazione di un sito 

 
 
 
 
Esercizio 
 
Premesse 
 
- Abbiamo creato il sito: 
 
tuoCognome.local 
 
(se non è stato creato, è necessario crearlo); 
 


*[continua...]*

---

### 📄 33 Linux Server 07 mysql

**File:** [`33_Linux_Server_07_mysql.md`](00_Note/33_Linux_Server_07_mysql.md)

1 
 
 
 
 
 
ACA 
Linux Server 
Docente: Wolfgang Cecchin 
Titolo argomento:  
mysql (mariadb) 
 
  

  2 
“Configurazione” del mysql 
 
• Installiamo MySQL; 
• Configuriamo MySQL. 
  

  3 
Installare mysql (mariadb) 
 
MySQL e MariaDB: differenze e

*[continua...]*

---

### 📄 34 Linux Server 08 php

**File:** [`34_Linux_Server_08_php.md`](00_Note/34_Linux_Server_08_php.md)

1 
 
 
 
 
 
ACA 
Linux Server 
Docente: Wolfgang Cecchin 
Titolo argomento:  
php, mysql 
 
  

  2 
“Configurazione” del php e del mysql 
 
• Installiamo il PHP; 
•  Configuriamo Nginx per far funzionare il PHP; 
•  (Configuriamo gli errori); 
• In

*[continua...]*

---

## Strumenti di Sistema

### 📄 07 glances doc

**File:** [`07_glances_doc.md`](00_Note/07_glances_doc.md)

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Glances 
Monitoraggio Avanzato del Sistema 
ITS ICT Piemonte  |  Corso Linux Server  |  A.F. 2025-2026 
1. Introduzione 
Glances è uno strumento di monitoraggio di 

*[continua...]*

---

### 📄 08 glances

**File:** [`08_glances.md`](00_Note/08_glances.md)

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Glances

Glances
Monitoraggio Avanzato del Sistema
ITS ICT Piemonte  |  Corso Linux Server  |  A.F. 2025-2026

Cos'è Glances?
ITS ICT Piemonte  |  Linux Server
Strumento di monitoraggio

*[continua...]*

---

### 📄 11 lezione find

**File:** [`11_lezione_find.md`](00_Note/11_lezione_find.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
find 


Introduzione 
Il comando find è lo strumento principale di Linux per cercare file e directory nel filesystem in base 
a criteri molto diversi: nome, tipo, dimensione, p

*[continua...]*

---

### 📄 12 lezione grep sed awk

**File:** [`12_lezione_grep_sed_awk.md`](00_Note/12_lezione_grep_sed_awk.md)

ITS ICT 
Linux 
DOCENTE: _______________________________ 
UNITÀ FORMATIVA: Strumenti Linux per la gestione dei file 
ARGOMENTO: Ricerca nei file: grep, sed, awk 
 
Introduzione 
Linux mette a disposizione tre strumenti fondamentali per cercare e mani

*[continua...]*

---

### 📄 13 libri data

**File:** [`13_libri_data.md`](00_Note/13_libri_data.md)

INSERT INTO libri (titolo, autore, isbn, pagine, prezzo) VALUES
    ('Il Nome della Rosa',           'Umberto Eco',           '9788845292613',  502,  14.90),
    ('Se questo è un uomo',          'Primo Levi',            '9788806208257',  224,  12.00)

*[continua...]*

---

### 📄 35 Linux Server comando at

**File:** [`35_Linux_Server_comando_at.md`](00_Note/35_Linux_Server_comando_at.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Il comando at 

 
 
 
Il comando at serve a eseguire un comando o uno script una sola volta in un momento futuro 
specifico, senza che tu debba restare loggato. Si usa quando

*[continua...]*

---

### 📄 36 Linux Server cron

**File:** [`36_Linux_Server_cron.md`](00_Note/36_Linux_Server_cron.md)

Linux Server 
 
Docente: Wolfgang Cecchin 
Titolo argomenti:  
- Archivi compressi 
- Cron 
- Processi per il monitoring 

 
2 
 
Creazione di un archivio compresso 
 
Comando tar (“tape archive”) 
 
Creazione di un archivio: 
 
$ tar cvf nomeMioArch

*[continua...]*

---

### 📄 41 Linux Server tool di diagnostica

**File:** [`41_Linux_Server_tool_di_diagnostica.md`](00_Note/41_Linux_Server_tool_di_diagnostica.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Tool di diagnostica 

[Digitare qui] 
 
 
uptime 
Il comando uptime fornisce in una sola riga le informazioni essenziali sullo stato del 
server: 
 
• da quanto tempo il sist

*[continua...]*

---

### 📄 44 panoramica guasti

**File:** [`44_panoramica_guasti.md`](00_Note/44_panoramica_guasti.md)

Panoramica dei guastiCausaGuastoLivelloMacchina# 10.0.0.11 → 10.0.0.1IP rete interna erratoRetedebian31 No regola porta 80HTTP bloccatoFirewalldebian32 /var/www/html → /wordpressnginx root sbagliataServiziodebian33 server_name + wp_optionsNome sito e

*[continua...]*

---

### 📄 46 presentazione grep sed find

**File:** [`46_presentazione_grep_sed_find.md`](00_Note/46_presentazione_grep_sed_find.md)

$ grep -rn "error"
/var/log/ 2>/dev/null
$ sed -i 's/old/new/g'
server.conf
$ find / -perm /4000 \
-type f 2>/dev/null
$ find /etc -name '*.conf'
| xargs grep '127.0.0.1'
ITS ICT — Linux Server
grep, sed, find
Ricerca e manipolazione di file e testo 

*[continua...]*

---

### 📄 48 shell avanzata doc

**File:** [`48_shell_avanzata_doc.md`](00_Note/48_shell_avanzata_doc.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
Shell avanzata 

 
 
 
Shell avanzata 
Reindirizzamento, processi e operatori 
1. File descriptor e reindirizzamento 
Cos'è un file descriptor 
In Linux, tutto è un file: file

*[continua...]*

---

### 📄 49 shell avanzata

**File:** [`49_shell_avanzata.md`](00_Note/49_shell_avanzata.md)

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Shell avanzata

$ _
Shell avanzata
Reindirizzamento, processi e operatori
fd 0/1/2 2>&1 &&  || $? nohup
ITS Academy — Linux Server

Cos'è un file descriptor
In Linux tutto è un file:
ta

*[continua...]*

---

### 📄 53 soluzioni find

**File:** [`53_soluzioni_find.md`](00_Note/53_soluzioni_find.md)

Soluzioni — find 
Ricerca base 
Es. 1  Cercare in tutto il filesystem un file di nome resolv.conf, sopprimendo gli errori.  
$ find / -name "resolv.conf" 2>/dev/null 
La ricerca parte dalla radice /. Il reindirizzamento 2>/dev/null scarta i messaggi 

*[continua...]*

---

### 📄 54 soluzioni grep sed awk

**File:** [`54_soluzioni_grep_sed_awk.md`](00_Note/54_soluzioni_grep_sed_awk.md)

Soluzioni — grep, sed, awk 
File di riferimento: sistema.log  |  utenti.txt  |  webserver.conf  |  vendite.csv 
grep 
Es. 1  Mostrare tutte le righe di sistema.log che contengono la parola ERROR.  
$ grep "ERROR" sistema.log 
 
Es. 2  Mostrare le rig

*[continua...]*

---

### 📄 56 URL nel database WordPress

**File:** [`56_URL_nel_database_WordPress.md`](00_Note/56_URL_nel_database_WordPress.md)

URL nel database WordPress

Da debian3, connettersi al database su debian4:
mysql -h 10.0.0.2 -u wpuser -p WordPress

Aggiornare i due campi:
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'siteurl';

UPDATE wp_options S

*[continua...]*

---

## Shell Avanzata

### 📄 48 shell avanzata doc

**File:** [`48_shell_avanzata_doc.md`](00_Note/48_shell_avanzata_doc.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
Shell avanzata 

 
 
 
Shell avanzata 
Reindirizzamento, processi e operatori 
1. File descriptor e reindirizzamento 
Cos'è un file descriptor 
In Linux, tutto è un file: file

*[continua...]*

---

### 📄 49 shell avanzata

**File:** [`49_shell_avanzata.md`](00_Note/49_shell_avanzata.md)

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Shell avanzata

$ _
Shell avanzata
Reindirizzamento, processi e operatori
fd 0/1/2 2>&1 &&  || $? nohup
ITS Academy — Linux Server

Cos'è un file descriptor
In Linux tutto è un file:
ta

*[continua...]*

---

## WordPress

### 📄 56 URL nel database WordPress

**File:** [`56_URL_nel_database_WordPress.md`](00_Note/56_URL_nel_database_WordPress.md)

URL nel database WordPress

Da debian3, connettersi al database su debian4:
mysql -h 10.0.0.2 -u wpuser -p WordPress

Aggiornare i due campi:
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'siteurl';

UPDATE wp_options S

*[continua...]*

---

### 📄 57 wordpress due macchine doc

**File:** [`57_wordpress_due_macchine_doc.md`](00_Note/57_wordpress_due_macchine_doc.md)

WordPress su Architettura a Due 
Macchine 
Guida pratica per ITS Academy — Linux Server 
1. Architettura dell'esercitazione 
L'obiettivo è mettere in rete due macchine virtuali Debian in modo che: 
 
• debian1 esponga WordPress su nginx, accessibile 

*[continua...]*

---

### 📄 58 wordpress due macchine

**File:** [`58_wordpress_due_macchine.md`](00_Note/58_wordpress_due_macchine.md)

WordPress su Architettura
a Due Macchine
Guida pratica — Linux Server
ITS Academy

Obiettivo dell'esercitazione
• Mettere in rete due macchine Debian in VirtualBox
• debian1 → frontend: nginx + WordPress (accessibile dall'esterno)
• debian2 → backend

*[continua...]*

---

## Esercizi e Soluzioni

### 📄 01 Consegna Esercitazione doc

**File:** [`01_Consegna_Esercitazione_doc.md`](00_Note/01_Consegna_Esercitazione_doc.md)

ITS ICT Piemonte — Linux Server 
Pagina 1 
 
ESERCITAZIONE 
Diagnostica e messa in sicurezza di un'infrastruttura WordPress 
Docente: Wolfgang Cecchin 
Scenario 
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno la realizzazione del propr

*[continua...]*

---

### 📄 02 Consegna Esercitazione ppt

**File:** [`02_Consegna_Esercitazione_ppt.md`](00_Note/02_Consegna_Esercitazione_ppt.md)

ESERCITAZIONE
Diagnostica e messa in sicurezza
di un'infrastruttura WordPress
Docente: Wolfgang Cecchin

Scenario
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno un sito WordPress su due VM 
Debian. Alla consegna, il sito non funziona.


*[continua...]*

---

### 📄 04 Esercizio Ripasso Finale CSP

**File:** [`04_Esercizio_Ripasso_Finale_CSP.md`](00_Note/04_Esercizio_Ripasso_Finale_CSP.md)

ITS ICT Piemonte  ·  Linux Server ESERCIZIO — StudioFoto Arcobaleno 
Pag. 1 
 
ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 
ESERCIZIO 
Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 
Traccia da consegnare allo studen

*[continua...]*

---

### 📄 17 Linux Server 031 Esercizio-su-utenti-permessi

**File:** [`17_Linux_Server_031_Esercizio-su-utenti-permessi.md`](00_Note/17_Linux_Server_031_Esercizio-su-utenti-permessi.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

  2 
Esercizio 
 
Nella home directory (eventualmente in Documenti) creare 
quattro files: 
 
- Per il primo file: solo l’utente proprietario

*[continua...]*

---

### 📄 18 Linux Server 032 Esercizio-su-utenti-permessi

**File:** [`18_Linux_Server_032_Esercizio-su-utenti-permessi.md`](00_Note/18_Linux_Server_032_Esercizio-su-utenti-permessi.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Esercizio 
 
PARTE 1 
 
- Creare un utente emilio; 
- Creare un utente ignazio; 
- Creare un utente ivan; 
- Creare un g

*[continua...]*

---

### 📄 19 Linux Server 033 Esercizio-su-utenti-permessi - passaggi

**File:** [`19_Linux_Server_033_Esercizio-su-utenti-permessi_-_passaggi.md`](00_Note/19_Linux_Server_033_Esercizio-su-utenti-permessi_-_passaggi.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Consegna: 
1. Creare i seguenti utenti:  
o marco, laura, simone, elena 
2. Creare i seguenti gruppi:  
o fotografi, pos

*[continua...]*

---

### 📄 20 Linux Server 033 Esercizio-su-utenti-permessi - soluzione

**File:** [`20_Linux_Server_033_Esercizio-su-utenti-permessi_-_soluzione.md`](00_Note/20_Linux_Server_033_Esercizio-su-utenti-permessi_-_soluzione.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
 
 
Comandi: 
 
 
1. Creazione degli utenti 
bash 
sudo adduser marco 
sudo adduser laura 
sudo adduser simone 
sudo add

*[continua...]*

---

### 📄 21 Linux Server 033 Esercizio-su-utenti-permessi

**File:** [`21_Linux_Server_033_Esercizio-su-utenti-permessi.md`](00_Note/21_Linux_Server_033_Esercizio-su-utenti-permessi.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Esercizio 
 
Scenario: 
Marco è il titolare di un piccolo studio fotografico. Ha tre 
dipendenti: 
• Laura - fotografa s

*[continua...]*

---

### 📄 22 Linux Server 034 Esercizio-su-utenti-permessi - passaggi

**File:** [`22_Linux_Server_034_Esercizio-su-utenti-permessi_-_passaggi.md`](00_Note/22_Linux_Server_034_Esercizio-su-utenti-permessi_-_passaggi.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Consegna: 
1. Creare i seguenti utenti:  
o giulia, andrea, chiara, luca, sara 
2. Creare i seguenti gruppi:  
o scritto

*[continua...]*

---

### 📄 23 Linux Server 034 Esercizio-su-utenti-permessi - soluzione

**File:** [`23_Linux_Server_034_Esercizio-su-utenti-permessi_-_soluzione.md`](00_Note/23_Linux_Server_034_Esercizio-su-utenti-permessi_-_soluzione.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Soluzione - Comandi 
 
1. Creazione degli utenti 
bash 
sudo adduser giulia 
sudo adduser andrea 
sudo adduser chiara 
s

*[continua...]*

---

### 📄 24 Linux Server 034 Esercizio-su-utenti-permessi

**File:** [`24_Linux_Server_034_Esercizio-su-utenti-permessi.md`](00_Note/24_Linux_Server_034_Esercizio-su-utenti-permessi.md)

1 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
  2 
Esercizio 
 
Scenario: 
Giulia gestisce una piccola casa editrice chiamata "Pagine 
Nuove". Il team è composto da: 
• An

*[continua...]*

---

### 📄 27 Linux Server 0501 Esercizio nome host

**File:** [`27_Linux_Server_0501_Esercizio_nome_host.md`](00_Note/27_Linux_Server_0501_Esercizio_nome_host.md)

SOFTWARE DEVELOPER 
Linux Server 
Docente: Wolfgang Cecchin 
Titolo argomento: DNS, File Host esercizio 
 

 
 
 
Esercizio 
 
 
Creare i nomi domini 
 
tuoCognome.local 
tuoCognome 
 
all’interno della macchina virtuale. 
 
 
Connettersi alla macchi

*[continua...]*

---

### 📄 29 Linux Server 061 http server esercizio

**File:** [`29_Linux_Server_061_http_server_esercizio.md`](00_Note/29_Linux_Server_061_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio sulla creazione di un sito 

 
 
Esercizio 
 
 
- Creare il dominio socrate.local 
 
• Associare il webserver al dominio socrate.local 
• Servire uno più file html

*[continua...]*

---

### 📄 30 Linux Server 062 http server esercizio

**File:** [`30_Linux_Server_062_http_server_esercizio.md`](00_Note/30_Linux_Server_062_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio sulla creazione di un sito 

 
 
 
 
Esercizio 
 
 
Create i siti 
 
moleantonelliana.local 
palazzomadama.local 
 
Scaletta: 
 
 
Creare il dominio moleantonellian

*[continua...]*

---

### 📄 31 Linux Server 063 http server esercizio

**File:** [`31_Linux_Server_063_http_server_esercizio.md`](00_Note/31_Linux_Server_063_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Esercizio su utenti e permessi 

 
 
 
 
Esercizio 
 
Premesse 
 
- Abbiamo creato il sito: 
 
tuoCognome.local 
 
(se non è stato creato, è necessario crearlo); 
 
- Abbiamo

*[continua...]*

---

### 📄 32 Linux Server 064 http server esercizio

**File:** [`32_Linux_Server_064_http_server_esercizio.md`](00_Note/32_Linux_Server_064_http_server_esercizio.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Esercizio sulla configurazione di un sito 

 
 
 
 
Esercizio 
 
Premesse 
 
- Abbiamo creato il sito: 
 
tuoCognome.local 
 
(se non è stato creato, è necessario crearlo); 
 


*[continua...]*

---

### 📄 37 Linux Server esercizi ripasso meta corso

**File:** [`37_Linux_Server_esercizi_ripasso_meta_corso.md`](00_Note/37_Linux_Server_esercizi_ripasso_meta_corso.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Esercitazione 

 
2 
 
 
 
Attività preliminari (facciamo un po’ di pulizia) – 
Rimozione degli utenti non necessari: 
 
Backup della macchina: 
- Con la macchina virtuale spen

*[continua...]*

---

### 📄 38 Linux Server esercizi ripasso meta corso2

**File:** [`38_Linux_Server_esercizi_ripasso_meta_corso2.md`](00_Note/38_Linux_Server_esercizi_ripasso_meta_corso2.md)

DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Esercitazioni di ripasso 

 
2 
 
 
 
Attività preliminari (facciamo un po’ di pulizia) – 
Rimozione degli utenti non necessari: 
 
Backup della macchina: 
- Con la macchina vi

*[continua...]*

---

### 📄 45 Passaggi Ripasso Finale CSP

**File:** [`45_Passaggi_Ripasso_Finale_CSP.md`](00_Note/45_Passaggi_Ripasso_Finale_CSP.md)

ITS ICT Piemonte  ·  Linux Server PASSAGGI — StudioFoto Arcobaleno 
Pag. 1 
 
ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 
PASSAGGI 
Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 
Guida operativa passo-passo 
Durata

*[continua...]*

---

### 📄 47 risoluzione problema rete Debian

**File:** [`47_risoluzione_problema_rete_Debian.md`](00_Note/47_risoluzione_problema_rete_Debian.md)

# risoluzione problema rete Debian 3
# tira su l'interfaccia a mano con l'IP tipico di VirtualBox NAT:

sudo ip link set enp0s3 up
sudo ip addr add 10.0.2.15/24 dev enp0s3
sudo ip route add default via 10.0.2.2
echo "nameserver 8.8.8.8" | sudo tee /e

*[continua...]*

---

### 📄 50 Soluzione Ripasso Finale CSP

**File:** [`50_Soluzione_Ripasso_Finale_CSP.md`](00_Note/50_Soluzione_Ripasso_Finale_CSP.md)

ITS ICT Piemonte  ·  Linux Server SOLUZIONE — StudioFoto Arcobaleno 
Pag. 1 
 
ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 
SOLUZIONE 
Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 
Comandi, configurazioni e verific

*[continua...]*

---

## DevOps

### 📄 03 DevOps per non DevOps- slides del Meet tenuto allAgile Community Torino 2018

**File:** [`03_DevOps_per_non_DevOps-_slides_del_Meet_tenuto_allAgile_Community_Torino_2018.md`](00_Note/03_DevOps_per_non_DevOps-_slides_del_Meet_tenuto_allAgile_Community_Torino_2018.md)

© 2018 Droplet
+Agile meetup | 5 Dicembre:  
INTRODUZIONE A DEVOPS 
PER NON DEVOPS
IN COLLABORAZIONE CON


© 2018 Droplet
 2
*DROPLET SI OCCUPA  DI   
e-commerce 
e digital 
experience 
dal 2003.
BENVENUTI! 
Siamo  
 
WOLFGANG CECCHIN SOCIO FONDATORE

*[continua...]*

---

## Laboratori e Progetti

### 📄 13 libri data

**File:** [`13_libri_data.md`](00_Note/13_libri_data.md)

INSERT INTO libri (titolo, autore, isbn, pagine, prezzo) VALUES
    ('Il Nome della Rosa',           'Umberto Eco',           '9788845292613',  502,  14.90),
    ('Se questo è un uomo',          'Primo Levi',            '9788806208257',  224,  12.00)

*[continua...]*

---

### 📄 55 tabella libri

**File:** [`55_tabella_libri.md`](00_Note/55_tabella_libri.md)

CREATE TABLE IF NOT EXISTS libri (
    id          INT             UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titolo      VARCHAR(255)    NOT NULL,
    autore      VARCHAR(150)    NOT NULL,
    isbn        CHAR(13)        UNIQUE NOT NULL,
    pagine   

*[continua...]*

---

