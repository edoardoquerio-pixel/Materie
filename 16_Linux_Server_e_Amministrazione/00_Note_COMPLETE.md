# Linux Server e Amministrazione — Quaderno di Appunti

> **Materia:** 16_Linux_Server_e_Amministrazione
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [Consegna Esercitazione doc](#consegna-esercitazione-doc)
2. [Consegna Esercitazione ppt](#consegna-esercitazione-ppt)
3. [DevOps per non DevOps- slides del Meet tenuto allAgile Community Torino 2018](#devops-per-non-devops--slides-del-meet-tenuto-allagile-community-torino-2018)
4. [Esercizio Ripasso Finale CSP](#esercizio-ripasso-finale-csp)
5. [Firewall Linux doc](#firewall-linux-doc)
6. [Firewall Linux presentazione](#firewall-linux-presentazione)
7. [glances doc](#glances-doc)
8. [glances](#glances)
9. [Lezione Diagnostica doc](#lezione-diagnostica-doc)
10. [Lezione Diagnostica ppt](#lezione-diagnostica-ppt)
11. [lezione find](#lezione-find)
12. [lezione grep sed awk](#lezione-grep-sed-awk)
13. [libri data](#libri-data)
14. [Linux Server 01 Installazione Debian](#linux-server-01-installazione-debian)
15. [Linux Server 02 Comandi Essenziali](#linux-server-02-comandi-essenziali)
16. [Linux Server 03 utenti e permessi](#linux-server-03-utenti-e-permessi)
17. [Linux Server 031 Esercizio-su-utenti-permessi](#linux-server-031-esercizio-su-utenti-permessi)
18. [Linux Server 032 Esercizio-su-utenti-permessi](#linux-server-032-esercizio-su-utenti-permessi)
19. [Linux Server 033 Esercizio-su-utenti-permessi - passaggi](#linux-server-033-esercizio-su-utenti-permessi---passaggi)
20. [Linux Server 033 Esercizio-su-utenti-permessi - soluzione](#linux-server-033-esercizio-su-utenti-permessi---soluzione)
21. [Linux Server 033 Esercizio-su-utenti-permessi](#linux-server-033-esercizio-su-utenti-permessi)
22. [Linux Server 034 Esercizio-su-utenti-permessi - passaggi](#linux-server-034-esercizio-su-utenti-permessi---passaggi)
23. [Linux Server 034 Esercizio-su-utenti-permessi - soluzione](#linux-server-034-esercizio-su-utenti-permessi---soluzione)
24. [Linux Server 034 Esercizio-su-utenti-permessi](#linux-server-034-esercizio-su-utenti-permessi)
25. [Linux Server 04 SSH](#linux-server-04-ssh)
26. [Linux Server 05 dns hosts](#linux-server-05-dns-hosts)
27. [Linux Server 0501 Esercizio nome host](#linux-server-0501-esercizio-nome-host)
28. [Linux Server 06 http server](#linux-server-06-http-server)
29. [Linux Server 061 http server esercizio](#linux-server-061-http-server-esercizio)
30. [Linux Server 062 http server esercizio](#linux-server-062-http-server-esercizio)
31. [Linux Server 063 http server esercizio](#linux-server-063-http-server-esercizio)
32. [Linux Server 064 http server esercizio](#linux-server-064-http-server-esercizio)
33. [Linux Server 07 mysql](#linux-server-07-mysql)
34. [Linux Server 08 php](#linux-server-08-php)
35. [Linux Server comando at](#linux-server-comando-at)
36. [Linux Server cron](#linux-server-cron)
37. [Linux Server esercizi ripasso meta corso](#linux-server-esercizi-ripasso-meta-corso)
38. [Linux Server esercizi ripasso meta corso2](#linux-server-esercizi-ripasso-meta-corso2)
39. [Linux Server permessi speciali](#linux-server-permessi-speciali)
40. [Linux Server schede di rete](#linux-server-schede-di-rete)
41. [Linux Server tool di diagnostica](#linux-server-tool-di-diagnostica)
42. [networking linux doc](#networking-linux-doc)
43. [networking linux](#networking-linux)
44. [panoramica guasti](#panoramica-guasti)
45. [Passaggi Ripasso Finale CSP](#passaggi-ripasso-finale-csp)
46. [presentazione grep sed find](#presentazione-grep-sed-find)
47. [risoluzione problema rete Debian](#risoluzione-problema-rete-debian)
48. [shell avanzata doc](#shell-avanzata-doc)
49. [shell avanzata](#shell-avanzata)
50. [Soluzione Ripasso Finale CSP](#soluzione-ripasso-finale-csp)
51. [Soluzioni Esercitazione doc](#soluzioni-esercitazione-doc)
52. [Soluzioni Esercitazione presentazione](#soluzioni-esercitazione-presentazione)
53. [soluzioni find](#soluzioni-find)
54. [soluzioni grep sed awk](#soluzioni-grep-sed-awk)
55. [tabella libri](#tabella-libri)
56. [URL nel database WordPress](#url-nel-database-wordpress)
57. [wordpress due macchine doc](#wordpress-due-macchine-doc)
58. [wordpress due macchine](#wordpress-due-macchine)

---

# Consegna Esercitazione doc

**File:** `Consegna Esercitazione doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 100.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte — Linux Server 
Pagina 1 
 
ESERCITAZIONE 
Diagnostica e messa in sicurezza di un'infrastruttura WordPress 
Docente: Wolfgang Cecchin 
Scenario 
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno la realizzazione del proprio sito 
web WordPress, ospitato su un'infrastruttura a due macchine virtuali Debian:  
Macchina Ruolo Rete 
debian3 Frontend — nginx + WordPress + PHP-
FPM 
Solo Host + rete interna 
debian4 Backend — MariaDB Solo rete interna 
 
Le due macchine comunicano attraverso una rete interna privata (intnet, rete 10.0.0.0/24). Il 
sito WordPress su debian3 si collega al database MariaDB su debian4 tramite questa rete.  
Al momento della consegna, l'azienda Acme scopre che il sito non funziona e che 
l'infrastruttura presenta diversi problemi di configurazione. L'azienda vi incarica di intervenire.  
Informazioni di accesso 
 Dettagli 
debian3 SSH dalla macchina Windows, porta 2222, autenticazione con 
username e password 
debian4 Non raggiungibile via SSH. Accesso esclusivamente dalla console 
VirtualBox (equivalente all'accesso fisico in sala server) 
Username its-usr 
Password Its2026 
Fase 1 — Report diagnostico 
Prima di intervenire sulla configurazione, Acme chiede un report scritto da presentare al 
fornitore che ha eseguito il lavoro. Il report deve documentare ogni problema riscontrato, 
indicando per ciascuno: 
• Cosa non funziona — il sintomo osservato (es. "il sito non risponde nel browser") 
• Dove si trova il problema — il file di configurazione, la regola o il servizio coinvolto 
• Perché non funziona — la causa tecnica (es. "il firewall blocca la porta 80 in ingresso")  
Suggerimento: procedete con metodo, verificando un livello alla volta — prima la rete, poi il 
firewall, poi i servizi — su ciascuna macchina. 
Fase 2 — Ripristino e messa in sicurezza 
Una volta completato il report, Acme chiede di correggere tutti i problemi individuati e 
rendere il sito WordPress raggiungibile dal PC Windows. 

ITS ICT Piemonte — Linux Server 
Pagina 2 
Per visualizzare il sito dal browser Windows, aggiungere una riga nel file 
C:\Windows\System32\drivers\etc\hosts: 
192.168.56.111  acme.local 
 
Il sito deve rispondere al nome acme.local — L'infrastruttura è attualmente configurata con 
un nome generico scelto dal fornitore. Acme richiede che il sito risponda al nome 
acme.local, sia nella configurazione di nginx che in quella di WordPress. 
Oltre alla correzione dei guasti, Acme richiede che l'infrastruttura rispetti i seguenti requisiti di 
sicurezza: 
Requisiti di sicurezza 
Firewall su entrambe le macchine — Entrambe le VM devono avere un firewall iptables 
attivo con policy di default DROP sulla catena INPUT. Le porte aperte devono essere 
esclusivamente quelle necessarie: 
• debian3: SSH (2222), HTTP (80), traffico dalla rete interna 
• debian4: SSH (2222) solo dalla rete interna, MariaDB (3306) solo dalla rete interna  
Accesso SSH a debian4 solo da debian3 — Nessun accesso diretto dall'esterno a debian4. 
L'unico modo per raggiungerla via SSH deve essere passando da debian3 attraverso la rete 
interna. 
MariaDB non esposto all'esterno — Il database deve essere in ascolto esclusivamente 
sull'interfaccia di rete interna (10.0.0.2), non su tutte le interfacce. 
Persistenza — Tutte le configurazioni (rete, firewall, servizi) devono sopravvivere a un riavvio 
della macchina. 
Consegna 
Alla fine dell'esercitazione, consegnare: 
1. Report diagnostico della Fase 1 (formato libero, ma chiaro e strutturato) 
2. Descrizione degli interventi eseguiti nella Fase 2, con i comandi utilizzati e una breve 
motivazione per ciascuno 


---

# Consegna Esercitazione ppt

**File:** `Consegna Esercitazione ppt.pdf`
**Tipo:** `.pdf`
**Dimensione:** 111.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

ESERCITAZIONE
Diagnostica e messa in sicurezza
di un'infrastruttura WordPress
Docente: Wolfgang Cecchin

Scenario
L'azienda Acme S.r.l. ha commissionato a un fornitore esterno un sito WordPress su due VM 
Debian. Alla consegna, il sito non funziona.
Macchina Ruolo Rete
debian3 Frontend — nginx + WordPress + PHP-FPM Solo Host + rete interna
debian4 Backend — MariaDB Solo rete interna
Comunicazione via rete interna privata intnet (10.0.0.0/24)
debian3 (frontend) debian4 (backend)
intnet 10.0.0.0/24

Informazioni di accesso
Dettagli
debian3 SSH dalla macchina Windows, porta 2222
Autenticazione con username e password
debian4 Non raggiungibile via SSH
Accesso dalla console VirtualBox
Username its-usr
Password Its2026

Fase 1 — Report diagnostico
Acme chiede un report scritto da presentare al fornitore. Per ogni problema:
Cosa non funziona
Il sintomo osservato
Dove si trova
File, regola o servizio
Perché non funziona
La causa tecnica
Suggerimento: procedete per livelli — rete → firewall → servizi — su ciascuna macchina.

Fase 2 — Ripristino e messa in sicurezza
Correggere i guasti e rendere il sito raggiungibile come acme.local
192.168.56.111  acme.local
→ aggiungere in C:\Windows\System32\drivers\etc\hosts
Il sito deve rispondere al nome acme.local — sia nella configurazione di nginx (server_name) che 
in WordPress (tabella wp_options nel database).

Requisiti di sicurezza
Firewall su entrambe le macchine
iptables attivo, policy DROP su INPUT.
debian3: SSH (2222), HTTP (80)
debian4: SSH (2222) + MariaDB (3306) solo da 
rete interna
SSH a debian4 solo da debian3
Nessun accesso diretto dall'esterno.
Passare per la rete interna.
MariaDB non esposto
In ascolto solo su 10.0.0.2,
non su tutte le interfacce.
Persistenza
Tutte le configurazioni devono
sopravvivere a un riavvio.

Consegna
1  Report diagnostico
Formato libero, chiaro e strutturato
2  Descrizione degli interventi
Comandi utilizzati e motivazione


---

# DevOps per non DevOps- slides del Meet tenuto all'Agile Community Torino, 2018

**File:** `DevOps per non DevOps- slides del Meet tenuto all'Agile Community Torino, 2018.pdf`
**Tipo:** `.pdf`
**Dimensione:** 25797.4 KB
**Ultima modifica:** 02/07/2026 09:27

---

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
 
WOLFGANG CECCHIN SOCIO FONDATORE DI DROPLET* 
 
MARCO BOZZOLAN, GESTORE SISTEMI DROPLET*

© 2018 Droplet
 3
SUMMARY:  
 
COME ARRIVIAMO A DEVOPS?, WOLFGANG CECCHIN 
 
DEVOPS DEMO, MARCO BOZZOLAN 
CONSIDERAZIONI FINALI 

© 2018 Droplet
DEVOPS:  
Quali sono gli  
                       
 4SCENARI
?

© 2018 Droplet
 5
SCENARI… 
:-(
DEVOPS

© 2018 Droplet
 6
OPS
DEVWORSE SCENARIO 

© 2018 Droplet
 7
WORSE SCENARIO 
EVEN
VS.
Mr. BUSINESS
OPS
VS.
DEV
VS.

© 2018 Droplet
 8
MA 
COME ARRIVIAMO A 
DEVOPS?, 

© 2018 Droplet
 
 
 
 
REWIND 
RIAVVOLGIAMO IL NASTRO… 
FACCIAMO UN  

© 2018 Droplet
…E FACCIAMO 
QUALCHE 
PASSO 
INDIETRO…

© 2018 Droplet


© 2018 Droplet
MMM… 
LO ABBIAMO RIAVVOLTO 
TROPPO :-)

© 2018 Droplet
RIAVVOLGIAMO IL NASTRO: 
OPERATIONS 
OK, FERMIAMOCI UN PÒ PRIMA E PARLIAMO DI “STORIA” E DI 
 

© 2018 Droplet
 14
L’ETÀ DEL FERRO PRIMA DEL 2001 D.C. 
 
RIAVVOLGIAMO IL NASTRO: 
OPS 

© 2018 Droplet
 15
ETÀ “DEL FERRO” “BARE METAL” 
 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.
OPS 

© 2018 Droplet
AMBIENTI: 
•Dev; 
•CQ (AKA “Test", “System Test”, “Pre-prod”, “Gold”, 
“Staging”); 
•Produzione.
 16
ETÀ DEL FERRO “BARE METAL” 
 
OPS 

© 2018 Droplet
RIDONDANZA E SCALING: 
•Raid (ridondanza sui dischi); 
•Macchine di backup (cloni); 
•Cluster; 
•…
 17
ETÀ DEL FERRO “BARE METAL” 
 
OPS 

© 2018 Droplet
E SE QUALCOSA SI SPACCA? 
Repeat again and again:
 18
ETÀ DEL FERRO “BARE METAL” 
 
OPS 
Assemblaggio hardware; 
•Installazione sistema operativo; 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.
:-(

© 2018 Droplet
 19
L’ETÀ DELLE 
VIRTUAL MACHINES DAL 2001 D.C. 
 
L’ETÀ DEL FERRO PRIMA DEL 2001 D.C. 
RIAVVOLGIAMO IL NASTRO: 
OPS 

© 2018 Droplet
 20
ETÀ DELLE VIRTUAL 
MACHINES  
OPS 
L’INFRASTRUTTURA

© 2018 Droplet
 21
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.
      ETÀ DEL FERRO “BARE METAL” 
 
OPS 

© 2018 Droplet
 22
ETÀ DELLE VIRTUAL 
MACHINES  
OPS 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; +allocazione risorse; 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet
VANTAGGI: 
•Le VM si clonano (CQ, Dev, PROD) e si spostano; 
•Le risorse delle VM si possono aumentare con pochi click.
 23
ETÀ DELLE VIRTUAL 
MACHINES  
OPS 

© 2018 Droplet
SVANTAGGI: 
•Devono essere allocate delle risorse hardware ad hoc.
 24
ETÀ DELLE VIRTUAL 
MACHINES  
OPS 

© 2018 Droplet
PRODOTTI PRINCIPALI: 
•VMWare ESX(i) Server; 
•KVM; 
•Oracle Virtual Box; 
•Menzione speciale: Vagrant (2010); 
 25
ETÀ DELLE VIRTUAL 
MACHINES  
OPS 

© 2018 Droplet
 26
L’ETÀ DEI  
CONTAINER DAL 2008 D.C. 
 
L’ETÀ DEL FERRO PRIMA DEL 2001 D.C. 
 
L’ETÀ DELLE VIRTUAL MACHINES DAL DEL 2001 D.C. 
 
OPS 
RIAVVOLGIAMO IL NASTRO: 

© 2018 Droplet
 27
ETÀ DEI CONTAINER 
 
OPS 
COSA CAMBIA?

© 2018 Droplet
 28
       ETÀ DELLE VIRTUAL 
MACHINES  
OPS 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; +allocazione risorse 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet
 29
ETÀ DEI CONTAINER 
 
OPS 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; +allocazione risorse 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet
VANTAGGI: 
•I container si clonano (Dev, CQ, PROD) e si spostano; 
•Le risorse si possono aumentare con pochi click; 
•L’allocazione delle risorse è dinamica; 
•Non devo occuparmi del sistema operativo sottostante; 
•Ospitano “piccole porzioni” di software.
 30
ETÀ DEI CONTAINER 
 
OPS 

© 2018 Droplet
MA… 
•Devo occuparmi del software all’interno del Container.
 31
ETÀ DEI CONTAINER 
 
OPS 

© 2018 Droplet
PRODUTTORI: 
•Linux LXC (2008); 
•Docker (2013).
 32
ETÀ DEI CONTAINER 
 
OPS 
ORCHESTRATORI DI CONTAINER: 
•OpenStack; 
•Kubernetes.

© 2018 Droplet
 33
CONFIGURATION 
MANAGEMENT SYSTEM DAL 2006 D.C. (CIRCA)  
L’ETÀ DELLE VIRTUAL MACHINES 
DAL DEL 2001 D.C. 
 
L’ETÀ DEI CONTAINERS 
DAL DEL 2008 D.C. 
 
L’ETÀ DEL FERRO 
PRIMA DEL 2001 D.C. 
 
RIAVVOLGIAMO IL NASTRO: 
OPS 

© 2018 Droplet
 34
      ETÀ DEI CONTAINER 
 
OPS 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; +allocazione risorse 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet
 35
CONFIGURATION 
MANAGEMENT SYSTEM 
 
OPS 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; +allocazione risorse; 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet
VENDORS:  
•Puppet; 
•Chef; 
•Salt;
 36
CONFIGURATION 
MANAGEMENT SYSTEM 
 
OPS 
•Ansible; 
•Terraform; 
•Cloudformation.

© 2018 Droplet
 37
L’ETA DEL CLOUD 
DAL 2006 D.C.  
L’ETÀ DELLE VIRTUAL MACHINES 
DAL DEL 2001 D.C. 
 
L’ETÀ DEI CONTAINERS 
DAL DEL 2008 D.C. 
 
L’ETÀ DEL FERRO 
PRIMA DEL 2001 D.C. 
 
RIAVVOLGIAMO IL NASTRO: 
L’ETÀ DEL CMS 
DAL DEL 2006 D.C. 
 
OPS 

© 2018 Droplet
 38
      CONFIGURATION 
MANAGEMENT SYSTEM 
 
OPS 
OPERAZIONI SUI SERVER: 
•Assemblaggio hardware; 
•Installazione sistema operativo; +allocazione risorse; 
•Installazione e conﬁgurazione software accessori (utenti, librerie); 
•Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet
 39
OPS 
CHE COSA RIMANE DA FARE?
ETÀ DEL CLOUD 
 

© 2018 Droplet
NON VOGLIAMO PIÙ DIPENDERE DAL FERRO; 
 
VOGLIAMO FARE TUTTO QUELLO CHE 
ABBIAMO DETTO FINORA, 
MAN MANO CHE NE ABBIAMO BISOGNO: 
VOGLIAMO AMBIENTI CLOUD “SCALABILI”.
 40
OPS 
ETÀ DEL CLOUD 
 

© 2018 Droplet
VENDORS: 
•Amazon AWS - EC2: Elastic Compute Cloud; 
•Google Cloud Platform; 
•Microsoft Azure; 
•SoftLayer.
 41
OPS 
ETÀ DEL CLOUD 
 

© 2018 Droplet
EVERYTHING AS SERVICE (EASS) 
•SaaS (Software as Service); 
•PaaS (Platform as Service); 
•IaaS (Infrastructure as Service).
 42
OPS 
ETÀ DEL CLOUD 
 

© 2018 Droplet
 43
RIAVVOLGIAMO IL NASTRO: 
L’ETÀ DELLE VIRTUAL MACHINES 
DAL DEL 2001 D.C. 
 
L’ETÀ DEI CONTAINERS 
DAL DEL 2008 D.C. 
 
L’ETÀ DEL FERRO 
PRIMA DEL 2001 D.C. 
 
L’ETÀ DEL CMS 
DAL DEL 2006 D.C. 
 
SERVERLESS 
 
L’ETÀ DEL CLOUD 
DAL DEL 2015 D.C. 
 
OPS 

© 2018 Droplet
VOGLIAMO CHE IL CODICE SI ATTIVI IN BASE A 
DETERMINATI EVENTI 
 
OVVERO 
 
VOGLIAMO PAGARE SOLO QUELLO CHE USIAMO 
VERAMENTE.
 44
OPS SERVERLESS (LAMBDA) 
 

© 2018 Droplet
VENDORS: 
•Amazon Lambda; 
•Google Cloud Functions; 
•Azure Functions.
 45
VENDORS: 
•Amazon Lambda; 
•Google Cloud Functions; 
•Azure Functions.
OPS SERVERLESS (LAMBDA) 
 

© 2018 Droplet
DEVELOPERS 
RIAVVOLGIAMO IL NASTRO: 
OK, ORA L’ALTRA FACCIA DELLA MEDAGLIA. PARLIAMO DI 
 

© 2018 Droplet
 47
BEST PRACTICES: •VERSIONAMENTO DEL CODICE.
RIAVVOLGIAMO IL NASTRO: 
DEV 

© 2018 Droplet
VANTAGGI: 
•Se sbaglio, posso ritornare facilmente alla versione precedente; 
•Sviluppo in team: risoluzione dei conﬂitti; 
•Tracking: so chi ha inserito una speciﬁca modiﬁca e perché; 
•Communicate in code.
 48
DEV 
BEST PRACTICES VERSIONAMENTO DEL CODICE 
 

© 2018 Droplet
PRODOTTI: 
•CVS; 
•Apache SVN (dal 2000); 
•Mercurial; 
•Git.
 49
DEV 
BEST PRACTICES VERSIONAMENTO DEL CODICE 
 
GESTORI: 
 
 MICROSOFT GITHUB, 
GITLAB, 
RHODECODE, 
ATLASSIAN BITBUCKET.

© 2018 Droplet
 50
RIAVVOLGIAMO IL NASTRO: 
- BEST PRACTICES 
- VERSIONAMENTO DEL CODICE 
 
SVILUPPO BASATO 
SUI TEST 
 
DEV 

© 2018 Droplet
KENT BECK,  
EXTREME PROGRAMMING 
EXPLAINED, 
1999.
 51
DEV SVILUPPO BASATO SUI 
TEST 
 


© 2018 Droplet
•Scrivo il test; 
•Eseguo il test, che non deve passare; 
•Scrivo il codice; 
•Eseguo il test, che passa; 
•Modiﬁco il codice.
 52
DEV 
SVILUPPO BASATO 
SUI TEST 

© 2018 Droplet
METODOLOGIE DI TEST: 
•Acceptance Test Driven Development; 
•Test Driven Development; 
•Behaviour Driven Development. 
 53
DEV SVILUPPO BASATO SUI 
TEST 
 
TIPI DI TEST: 
•Acceptance Tests; 
•Unit Testing; 
•Functional Tests / Integration 
Tests.

© 2018 Droplet
STRUMENTI OPER UNIT TESTING: 
•JUnit; 
•PHPUnit; 
•Nose; 
•Live Unit Testing.
 54
DEV SVILUPPO BASATO SUI 
TEST 
 

© 2018 Droplet
SOFTWARE: 
•Jenkins; 
•Travis CI; 
•GoCD; 
•Concourse.
 55
DEV SVILUPPO BASATO SUI 
TEST 
 

© 2018 Droplet
 56
RIAVVOLGIAMO IL NASTRO: 
DEV 
- BEST PRACTICES 
- VERSIONAMENTO DEL CODICE 
- SVILUPPO BASATO SUI TEST 
 
SVILUPPO BASATO 
SUI MISCROSERVIZI  

© 2018 Droplet
AJAX (2005) E 
JQUERY (2006)
 57
E poi… 
 
Angular,js 
React.js 
Vue.js
DEV SVILUPPO BASATO SUI 
MICROSERVIZI 
 


© 2018 Droplet
PROGRAMMAZIONE FUNZIONALE E LAMBDA 
(REACTIVE MANIFESTO - 2014) 
 58
DEV SVILUPPO BASATO SUI 
MICROSERVIZI 
 

© 2018 Droplet
 59
RIAVVOLGIAMO IL NASTRO: 
DEV 
- VERSIONAMENTO DEL CODICE 
- SVILUPPO BASATO SUI TEST 
- SVILUPPO BASATO SUI MICROSERVIZI 
 
MENO DOCUMENTAZIONE, 
PIÙ CODICE  

© 2018 Droplet
ROBERT MARTIN,  
CLEAN CODE, 
2004.
 60
DEV LA DOCUMENTAZIONE 
DEVE MORIRE 
 


© 2018 Droplet
FINALMENTE!
DEVOPS? 
 

© 2018 Droplet
 62
UN NUOVO SCENARIO 

© 2018 Droplet
 
AUTOMATION: CONTINUOS INTEGRATION + CONTINUOS DELIVERY
 63
DEVOPS? 
 

© 2018 Droplet
WITH TOOLS
 64
DEVOPS? 
 

© 2018 Droplet
 
AUTOMATION: CONTINUOUS INTEGRATION + CONTINUOUS DELIVERY
 65
DEVOPS? 
 

© 2018 Droplet
•Plan: Dev + Ops. Si ipotizza un piano e si scelgono le metriche. 
•Create: Sviluppo basato sui test; 
•Verify: Test automatici; 
•Package: Artifacts; 
•Release:  Deploy in Sviluppo o in Produzione; 
•Conﬁgure: Conﬁguration Management System; 
•Monitor: KPI Systems + Business,
 66
DEVOPS? 
 

© 2018 Droplet
INSPECT AND ADAPT 
 
DASHBOARD DI PERFORMANCES 
Sistemi (Prometheus, Collectd, Graphite) 
+ Business 
+ Analytics.
 67
MONITORING? 
 
DEVOPS 

© 2018 Droplet
 68
LE PIPELINES CONSENTONO DI 
AUTOMATIZZARE I PROCESSI 
DEVOPS.
PIPELINES 
 
DEVOPS 


© 2018 Droplet
 69
IT’S DEMO TIME!
DEVOPS
NOW LIVE!
CON MARCO 

© 2018 Droplet
•Plan; 
•Create: Source control - Git + Rhodecode; 
•Verify: Test automatici - Jenkins; 
•Package: Container; 
•Release:  Deploy in Sviluppo o in Produzione - Jenkins; 
•Conﬁgure: Infrastruttura come codice - Ansible; 
•Monitor.
 70
COSA VEDREMO OGGI?? 
 
DEVOPS 

© 2018 Droplet
CAVEAT!  

© 2018 Droplet
•DevOps non è un’etichetta;
CAVEAT!  
 72


© 2018 Droplet
•DevOps non è un’etichetta; 
•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management;
 73
CAVEAT!  


© 2018 Droplet
•DevOps non è un’etichetta; 
•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 
•DevOps non è un insieme di strumenti;
 74
CAVEAT!  


© 2018 Droplet
•DevOps non è un’etichetta; 
•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 
•DevOps non è un insieme di strumenti; 
•DevOps non è una bacchetta magica;
 75
CAVEAT!  


© 2018 Droplet
•DevOps non è un’etichetta; 
•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 
•DevOps non è un insieme di strumenti; 
•DevOps non è una bacchetta magica; 
•DevOps non è DevOps(TM);
 76
CAVEAT!  


© 2018 Droplet
•DevOps non è un’etichetta; 
•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 
•DevOps non è un insieme di strumenti; 
•DevOps non è una bacchetta magica; 
•DevOps non è DevOps(TM); 
•DevOps non “ﬁnisce”.
 77
CAVEAT!  


© 2018 Droplet
BONUS TRACK 
DEVOPS? 
 

© 2018 Droplet
 79
COME PORTARE 
DEVOPS 
IN AZIENDA
DEVOPS 
QUANDO L’AMBIENTE 
“REMA NATURALMENTE CONTRO” 
MA ABBIAMO SEMPRE 
FATTO COSI’ PERCHE’ADESSO 
DOBBIAMO CAMBIARE? 
 

© 2018 Droplet
 80
UNA 
MEZZA 
IDEA 
L’AVREI!

© 2018 Droplet
 81
MMM.. 
NON ANCORA 
BRUCE… 
PROVIAMO CON 
LARMAN

© 2018 Droplet
“
 82Culture follows 
structure
- Craig Larman -

© 2018 Droplet
 83
LA STRUTTURA DETERMINA LA 
CULTURA
DEVOPS 
QUARTA LEGGE DI LARMAN: Larman’s Laws of Organizational Behavior observes that… 
1.Organizations are implicitly optimized to avoid changing the status quo middle- and ﬁrst-
level manager and single-specialist positions & power structures. 
2.As a corollary to (1), any change initiative will be reduced to redeﬁning or overloading the 
new terminology to mean basically the same as status quo. 
3.As a corollary to (1), any change initiative will be derided as “purist”, “theoretical”, and 
“needing pragmatic customization for local concerns”—which deﬂects from addressing 
weaknesses and manager/specialist status quo. 
4.Culture follows structure. 
Craig Larman

© 2018 Droplet
LA STRUTTURA 
DETERMINA LA CULTURA
QUARTA LEGGE DI LARMAN: 
The systems-thinking thought-leader John Seddon explains 
 
“culture follows structure” 
this way: 
Attempting to change an organization’s culture is a folly, it always fails. Peoples’ 
behavior (the culture) is a product of the system; when you change the system 
peoples’ behavior changes. 
 84
DEVOPS 

© 2018 Droplet
Stewart Brand lo riassunse nel modo migliore: 
 
«Puoi provare a cambiare la testa della gente, ma stai solo 
perdendo tempo. Cambia gli strumenti che hanno in mano, 
e cambierai il mondo». 
Alessandro Baricco, The Game, 2018. 
Steward Brand, The Next Whole Earth Catalog: Access to 
Tools, 1968 
 85
CAMBIA GLI STRUMENTI 
CHE HAI IN MANO
DEVOPS 


© 2018 Droplet
 86


© 2018 Droplet
“
 87GRAZIE*“*un grazie speciale a CORVALLIS per l’ospitalità


---

# Esercizio Ripasso Finale CSP

**File:** `Esercizio Ripasso Finale CSP.pdf`
**Tipo:** `.pdf`
**Dimensione:** 112.2 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte  ·  Linux Server ESERCIZIO — StudioFoto Arcobaleno 
Pag. 1 
 
ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 
ESERCIZIO 
Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 
Traccia da consegnare allo studente 
Durata: 2 ore  ·  Valutazione: 16 punti (1 per punto) — sufficienza a 10 
  

ITS ICT Piemonte  ·  Linux Server ESERCIZIO — StudioFoto Arcobaleno 
Pag. 2 
Consegna. Ti viene affidata una VM Debian 12 minimale. Lo StudioFoto Arcobaleno 
deve disporre di un piccolo server con sito PHP, database e accesso remoto sicuro. 
Per ogni punto riporta i comandi usati e/o il contenuto dei file modificati, con 
l'output di verifica dove richiesto. 
Ambiente di partenza 
• VM Debian 12 in installazione minimale 
• Utente di lavoro: its-usr / Its2026, con privilegi sudo 
• Interfacce VirtualBox: NAT (enp0s3), Solo Host (enp0s8) 
 
Parte 1 — Utenti, gruppi e permessi  (~25 min) 
1. Imposta l'hostname arcobaleno-srv in modo persistente e verificalo. 
2. Crea il gruppo fotografi e gli utenti anna e luca, entrambi membri del gruppo, 
con home e shell /bin/bash. 
3. Crea la directory condivisa /srv/scatti e configurala affinché: i membri di 
fotografi possano leggere/scrivere, ogni nuovo file erediti il gruppo fotografi, e 
ciascuno possa cancellare solo i propri file. Spiega quali bit speciali hai usato e 
perché. 
Parte 2 — Rete  (~15 min) 
4. Configura un IP statico su enp0s8: 192.168.56.120/24, lasciando il NAT (enp0s3) 
in DHCP. 
5. Aggiungi in /etc/hosts un record che associ db.arcobaleno.local a 10.0.0.2 e 
verifica la risoluzione. 
Parte 3 — Accesso remoto SSH  (~15 min) 
6. Abilita l'accesso a its-usr tramite chiave pubblica. 
7. Configura OpenSSH per disabilitare il login di root e l'autenticazione tramite 
password. Ricarica il servizio e verifica che sia attivo. 
Parte 4 — Web server nginx + PHP  (~20 min) 
8. Installa nginx e PHP-FPM (ricorda: NON il metapacchetto generico php). 
9. Crea /var/www/arcobaleno/info.php con phpinfo() e configura un virtual host 
minimale che lo serva. Verifica che PHP venga interpretato (non scaricato). 
Parte 5 — Database MariaDB  (~15 min) 
10. Installa MariaDB ed esegui la messa in sicurezza iniziale. 
11. Crea il database arcobaleno_db e l'utente wpuser con privilegi limitati al solo 
arcobaleno_db. Verifica il login con il nuovo utente. 
Parte 6 — Processi e servizi  (~10 min) 

ITS ICT Piemonte  ·  Linux Server ESERCIZIO — StudioFoto Arcobaleno 
Pag. 3 
12. Verifica lo stato di nginx, php-fpm e mariadb e abilitane l'avvio automatico al 
boot. 
13. Avvia sleep 1000 & , individua il suo PID e terminalo con il segnale appropriato. 
Parte 7 — Automazione (cron) e firewall (iptables)  (~15 min) 
14. Scrivi /usr/local/bin/backup-scatti.sh che crei un archivio scatti-AAAA-MM-
GG.tar.gz di /srv/scatti in /var/backups/. Rendilo eseguibile e pianificalo con 
cron ogni notte alle 02:30. 
15. Installa iptables (non preinstallato su Debian minimale) e definisci regole con 
policy di default DROP in INPUT che consentano: loopback, traffico 
ESTABLISHED,RELATED, SSH e HTTP. Rendile persistenti. 
Parte 8 — Diagnostica  (~5 min) 
1. Un fotografo segnala che il sito non risponde. Descrivi la procedura 
diagnostica bottom-up (rete → firewall → servizio → applicazione) indicando 
almeno un comando di verifica per ogni livello. 


---

# Firewall Linux doc

**File:** `Firewall Linux doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 300.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Firewall: iptables, ufw 


 
 
 
Firewall in Linux 
iptables e ufw 
Cos'è un firewall 
Un firewall è un sistema che controlla il traffico di rete in entrata e in uscita sulla base di un 
insieme di regole. Su un server Linux, il firewall è fondamentale per proteggere i servizi 
esposti: si decide esplicitamente cosa è permesso, e tutto il resto viene bloccato. 
 
Il kernel Linux gestisce il filtraggio dei pacchetti attraverso un sottosistema chiamato 
Netfilter. Gli strumenti iptables e ufw sono semplicemente interfacce per scrivere 
regole che Netfilter applica. 
 
Nota: Il successore moderno di iptables è nftables, diventato predefinito a partire da Debian 10. 
Su sistemi recenti, il comando iptables è in realtà un wrapper che traduce i comandi in regole 
nftables sottostanti. Per i server applicativi standard, iptables e ufw restano comunque lo 
strumento pratico di riferimento. 
 
Parte 1 — iptables 
Come funziona iptables 
iptables organizza le regole in tabelle e catene. 
 
La tabella più usata è filter, che contiene tre catene predefinite: 
• INPUT — traffico diretto al server stesso 
• OUTPUT — traffico generato dal server 
• FORWARD — traffico che transita attraverso il server (usato nei router) 
 
Ogni pacchetto viene confrontato con le regole della catena, dall'alto verso il basso. Alla 
prima regola che corrisponde viene applicata l'azione (chiamata target): 
• ACCEPT — il pacchetto viene accettato 
• DROP — il pacchetto viene scartato silenziosamente 
• REJECT — il pacchetto viene rifiutato con un messaggio di errore 
 
Se nessuna regola corrisponde, si applica la policy di default della catena. 
 
Installazione 
Su Debian è disponibile nei repository ufficiali: 

 
 
 
sudo apt install iptables 
 
Visualizzare le regole correnti 
sudo iptables -L -v -n 
 
• -L — elenca le regole 
• -v — output verboso (mostra contatori, interfacce) 
• -n — mostra IP e porte in formato numerico (non fa lookup DNS) 
 
La sintassi di base 
sudo iptables -A CATENA -p protocollo --dport porta -j TARGET 
 
• -A — appende la regola in fondo alla catena (append) 
• -I — inserisce la regola in cima (o in una posizione specifica) 
• -p — protocollo (tcp, udp, icmp) 
• --dport — porta di destinazione 
• -j — azione da eseguire (jump) 
 
Esempi pratici 
Accettare le connessioni SSH (porta 22) 
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT 
 
Accettare il traffico HTTP e HTTPS 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT 
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT 
 
Accettare traffico sulla loopback 
Indispensabile — senza questa regola molti servizi locali smettono di funzionare: 
 
sudo iptables -A INPUT -i lo -j ACCEPT 
 
Accettare connessioni già stabilite 
Fondamentale: senza questa regola il server non riceve le risposte alle proprie richieste 
(aggiornamenti apt, query DNS, ecc.): 

 
 
 
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
 
Bloccare un indirizzo IP specifico 
sudo iptables -A INPUT -s 192.168.1.50 -j DROP 
 
Permettere o bloccare il ping in entrata 
# Permettere 
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT 
 
# Bloccare 
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP 
 
Se la policy di default è già DROP, la regola di blocco è ridondante — il ping verrebbe 
ignorato comunque. Diventa necessaria solo se la policy è ACCEPT e si vuole bloccare 
esplicitamente il ping lasciando aperto il resto. 
 
Impostare la policy di default a DROP 
Supponiamo di avere un server nginx con le regole precedenti già configurate. Si imposta la 
policy di default per bloccare tutto il resto: 
 
sudo iptables -P INPUT DROP 
 
Da questo momento il server accetta solo SSH, HTTP, HTTPS e le connessioni già stabilite. 
Tutto il resto viene silenziosamente ignorato. 
 
Eliminare regole 
Per eliminare una regola, si usa -D con la stessa sintassi usata per aggiungerla: 
 
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT 
 
Oppure si elencano le regole con i numeri di riga e si elimina per numero: 
 
sudo iptables -L INPUT --line-numbers 
sudo iptables -D INPUT 3 
 
Svuotare tutte le regole (flush) 

 
 
Durante le prove in laboratorio, per ripartire da zero: 
 
sudo iptables -F 
sudo iptables -P INPUT ACCEPT 
sudo iptables -P OUTPUT ACCEPT 
sudo iptables -P FORWARD ACCEPT 
 
Configurazione tramite file di regole 
Invece di digitare le regole una per una, è possibile scriverle in un file di testo e caricarle 
tutte in una volta. Questo è il formato usato anche da iptables-persistent internamente. 
 
Un esempio di file di configurazione tipico per un server: 
 
*filter 
:INPUT DROP 
:FORWARD DROP 
:OUTPUT ACCEPT 
 
-A INPUT -i lo -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT 
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
-A INPUT -p icmp --icmp-type echo-request -j ACCEPT 
 
COMMIT 
 
Vediamo cosa fa ogni parte: 
 
Le policy di default 
:INPUT DROP 
:FORWARD DROP 
:OUTPUT ACCEPT 
 
Imposta il comportamento per i pacchetti che non corrispondono a nessuna regola. INPUT e 
FORWARD vengono scartati (approccio deny by default — il più sicuro), mentre il traffico in 
uscita è libero. 
 
Le regole 
-A INPUT -i lo -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT 
 
Permette il traffico sulla loopback. Necessario per i servizi locali che comunicano tra loro, ad 
esempio PHP che si connette a MySQL su 127.0.0.1. 
 

 
 
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
 
Permette le risposte a connessioni già avviate dal server. Senza questa regola, il server non 
riceverebbe nessuna risposta alle proprie richieste (aggiornamenti apt, query DNS, ecc.). 
 
-A INPUT -p icmp --icmp-type echo-request -j ACCEPT 
 
Permette il ping in entrata. Utile per verificare che il server sia raggiungibile dalla rete. 
 
Caricare il file 
Il file viene salvato in /etc/iptables.rules e caricato con: 
 
sudo iptables-restore < /etc/iptables.rules 
 
È equivalente a digitare ogni regola a mano, ma più rapido e riproducibile. Su questo 
formato si basa anche la persistenza automatica descritta nella sezione seguente. 
 
Persistenza delle regole 
Le regole iptables non sopravvivono al riavvio. Vengono caricate in memoria e al riavvio 
si azzerano. Per renderle persistenti su Debian si installa: 
 
sudo apt install iptables-persistent 
 
Le regole vengono salvate in /etc/iptables/rules.v4 (IPv4) e 
/etc/iptables/rules.v6 (IPv6). Per salvare lo stato corrente: 
 
sudo netfilter-persistent save 
 
 
Parte 2 — ufw 
Cos'è ufw 
ufw (Uncomplicated Firewall) è un frontend per iptables progettato per semplificare la 
gestione del firewall. Invece di ragionare in termini di catene e target, si lavora con concetti 
più diretti: abilita questa porta, blocca questo IP. Dietro le quinte, ufw scrive comunque 
regole iptables, ma non è necessario gestirle a mano. 

 
 
 
Installazione e stato 
sudo apt install ufw 
 
Per vedere lo stato attuale: 
 
sudo ufw status 
 
Se ufw è disabilitato, l'output sarà semplicemente Status: inactive. 
 
Per uno stato più dettagliato con le regole numerate: 
 
sudo ufw status numbered 
sudo ufw status verbose 
 
Abilitare e disabilitare 
sudo ufw enable 
sudo ufw disable 
 
Attenzione: Prima di abilitare ufw su un server remoto, assicurarsi di aver aggiunto la regola per 
SSH. Altrimenti ci si taglia fuori dalla macchina. 
 
Aggiungere regole 
Permettere una porta 
sudo ufw allow 22/tcp 
sudo ufw allow 80/tcp 
sudo ufw allow 443/tcp 
 
ufw conosce i servizi più comuni per nome: 
 
sudo ufw allow ssh 
sudo ufw allow http 
sudo ufw allow https 
 
Permettere un profilo applicazione 

 
 
Alcuni pacchetti (nginx, OpenSSH, ecc.) installano profili ufw predefiniti in 
/etc/ufw/applications.d/. Si può usarli direttamente: 
 
sudo ufw allow 'Nginx Full'    # permette sia 80 che 443 
sudo ufw allow 'OpenSSH' 
 
Per vedere i profili disponibili: 
 
sudo ufw app list 
 
Bloccare un indirizzo IP 
sudo ufw deny from 192.168.1.50 
 
Permettere l'accesso solo da una subnet specifica 
Scenario pratico: un database MySQL che deve essere raggiungibile solo dai server nella 
rete interna 192.168.10.0/24, non dall'esterno. 
 
sudo ufw allow from 192.168.10.0/24 to any port 3306 
 
Permettere una connessione su una specifica interfaccia di rete 
sudo ufw allow in on eth0 to any port 80 
 
Eliminare regole 
Con il numero di riga (da ufw status numbered): 
 
sudo ufw delete 3 
 
Oppure con la stessa sintassi usata per creare la regola: 
 
sudo ufw delete allow 80/tcp 
 
Policy di default 
La configurazione tipica per un server: 
 

 
 
sudo ufw default deny incoming 
sudo ufw default allow outgoing 
 
Si nega tutto il traffico in entrata e si aprono solo le porte necessarie, mentre si lascia libero 
il traffico in uscita. 
 
Logging 
ufw può registrare nei log di sistema le connessioni bloccate o accettate: 
 
sudo ufw logging on 
 
I livelli disponibili sono low, medium, high, full. Il default è low. 
 
I log vengono scritti in /var/log/ufw.log e sono leggibili anche con: 
 
sudo journalctl | grep UFW 
 
Reset 
Per riportare ufw allo stato iniziale, eliminando tutte le regole: 
 
sudo ufw reset 
 
 
iptables vs ufw — quando usare quale 
 
 iptables ufw 
Controllo Granulare, completo Semplificato 
Curva di 
apprendimento 
Ripida Bassa 
Uso tipico Server avanzati, script, router Server applicativi standard 
Persistenza Manuale (iptables-persistent) Automatica 
Leggibilità regole Bassa Alta 
 

 
 
In un contesto professionale, iptables viene usato quando si ha bisogno di controllo fine — 
ad esempio per NAT, port forwarding, o regole complesse su firewall di rete. ufw è la scelta 
naturale per un server applicativo standard dove si vogliono semplicemente aprire le porte 
necessarie e bloccare tutto il resto. 


---

# Firewall Linux presentazione

**File:** `Firewall Linux presentazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 464.3 KB
**Ultima modifica:** 02/07/2026 09:27

---

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Firewall: iptables, ufw

Firewall in Linux
iptables & ufw — controllo del traffico di rete
Linux Server  ·  ITS Academy

Cos'è un firewall
• Controlla il traffico di rete in entrata e in uscita sulla base di regole
• Decide esplicitamente cosa è permesso — tutto il resto viene 
bloccato
• Su Linux: il sottosistema Netfilter nel kernel gestisce il filtraggio dei 
pacchetti
• iptables e ufw sono interfacce per scrivere regole che Netfilter 
applica
KERNEL
Netfilter
iptables
ufw
Nota: nftables è il successore di iptables (Debian 10+). Su sistemi moderni iptables è un wrapper su nftables.

Parte 1
iptables

Tabelle e catene
Le catene (tabella filter) I target
INPUT traffico diretto al server
OUTPUT traffico generato dal server
FORWARD traffico in transito (router)
ACCEPT pacchetto accettato
DROP scartato silenziosamente
REJECT rifiutato con messaggio errore
Nota: Se nessuna regola corrisponde, si applica la policy di default della catena.

Installazione e visualizzazione
Installazione
Su Debian non è sempre preinstallato:
sudo apt install iptables
Visualizzare le regole
sudo iptables -L -v -n
-L elenca tutte le regole
-v output verboso (contatori, interfacce)
-n formato numerico — no lookup DNS

Sintassi di base
sudo iptables -A CATENA -p protocollo --dport porta -j TARGET
Opzioni principali Protocolli e porte
-A append — aggiunge in fondo alla catena
-I insert — aggiunge in cima (o posizione N)
-D delete — elimina la regola
-P policy — imposta comportamento default
-F flush — elimina tutte le regole
-p tcp / udp / icmp
--dport porta di destinazione
--sport porta di origine
-s indirizzo IP sorgente
-j azione: ACCEPT / DROP / REJECT

Regole comuni
Permetti servizi
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
Regole essenziali (sempre necessarie)
# Loopback
sudo iptables -A INPUT -i lo -j ACCEPT
# Connessioni già stabilite
sudo iptables -A INPUT -m state \
--state ESTABLISHED,RELATED -j ACCEPT
Senza queste due regole il server non risponde correttamente ai propri 
servizi locali e alle risposte di rete.
Scenario: server nginx
Dopo le regole sopra, imposta la policy a DROP:
sudo iptables -P INPUT DROP
Da questo momento accetta solo SSH, HTTP, HTTPS e connessioni già 
stabilite.

Ping e blocco IP
Ping in entrata (ICMP echo-request)
# Permettere
sudo iptables -A INPUT -p icmp \
--icmp-type echo-request -j ACCEPT
# Bloccare
sudo iptables -A INPUT -p icmp \
--icmp-type echo-request -j DROP
Nota: Se la policy è già DROP, il blocco è ridondante. Serve solo se la 
policy è ACCEPT.
Bloccare un IP e eliminare regole
# Bloccare un IP
sudo iptables -A INPUT -s 192.168.1.50 -j DROP
#### Eliminazione di regole precedentemente impostate ####
# Eliminare per sintassi
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT
# Eliminare per numero di riga
sudo iptables -L INPUT --line-numbers
sudo iptables -D INPUT 3
Flush (laboratorio — ripartire da zero):
sudo iptables -F && sudo iptables -P INPUT ACCEPT

File di regole e persistenza
Formato file /etc/iptables.rules
*filter
:INPUT DROP
:FORWARD DROP
:OUTPUT ACCEPT
-A INPUT -i lo -s 127.0.0.1 -d 127.0.0.1 -j 
ACCEPT
-A INPUT -m state --state ESTABLISHED,RELATED -j 
ACCEPT
-A INPUT -p icmp --icmp-type echo-request -j 
ACCEPT
COMMIT
Caricare e rendere persistenti le regole
Caricare il file:
sudo iptables-restore < /etc/iptables.rules
Equivalente a digitare ogni regola a mano — più rapido e riproducibile.
Persistenza al riavvio:
sudo apt install iptables-persistent
sudo netfilter-persistent save
• Regole salvate in /etc/iptables/rules.v4 (IPv4) e rules.v6 (IPv6)
• Caricate automaticamente a ogni avvio

Parte 2
ufw

Uncomplicated Firewall — ufw
Frontend semplificato per iptables
• Scrive regole iptables in automatico — non serve gestirle a mano
• Si lavora con concetti diretti: abilita questa porta, blocca questo IP
• La persistenza è automatica (a differenza di iptables)
Installazione e stato
sudo apt install ufw
sudo ufw status
sudo ufw status numbered
sudo ufw status verbose
Abilitare e disabilitare
sudo ufw enable
sudo ufw disable
sudo ufw reset
Attenzione: Prima di ufw enable su un server remoto, aggiungere sempre la 
regola per SSH.

Regole ufw
Permettere porte e servizi
sudo ufw allow 22/tcp
sudo ufw allow ssh      # per nome
sudo ufw allow http
sudo ufw allow https
# Profilo applicazione (nginx, OpenSSH...)
sudo ufw allow 'Nginx Full'
sudo ufw app list        # profili disponibili
Blocco e restrizioni avanzate
# Bloccare un IP
sudo ufw deny from 192.168.1.50
# Solo da una subnet (es. MySQL interno)
sudo ufw allow from 192.168.10.0/24 \
to any port 3306
# Su interfaccia specifica
sudo ufw allow in on eth0 to any port 80
Nota: Scenario tipico: database MySQL accessibile solo dalla rete interna 192.168.10.0/24.

Policy, logging ed eliminare regole
Policy di default
sudo ufw default deny incoming
sudo ufw default allow outgoing
Nega tutto in entrata, apre solo le porte necessarie. Traffico in uscita 
libero.
Eliminare regole
sudo ufw status numbered
sudo ufw delete 3
sudo ufw delete allow 80/tcp
Logging
sudo ufw logging on
# livelli: low / medium / high / full
• Log in /var/log/ufw.log
• Leggibile anche con: sudo journalctl | grep UFW
Profili applicazione
Alcuni pacchetti installano profili predefiniti in 
/etc/ufw/applications.d/ — es. Nginx Full permette sia la porta 80 
che la 443 con un unico comando.

iptables vs ufw — quando usare quale
iptables ufw
Controllo Granulare, completo Semplificato
Curva di apprendimento Ripida Bassa
Uso tipico Server avanzati, script, router Server applicativi standard
Persistenza Manuale (iptables-persistent) Automatica
Leggibilità regole Bassa Alta
In ambito professionale, iptables per controllo fine (NAT, port forwarding, firewall di rete). ufw per server applicativi standard.


---

# glances doc

**File:** `glances doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3918.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Glances 
Monitoraggio Avanzato del Sistema 
ITS ICT Piemonte  |  Corso Linux Server  |  A.F. 2025-2026 
1. Introduzione 
Glances è uno strumento di monitoraggio di sistema scritto in Python che fornisce 
una panoramica completa delle risorse in tempo reale, in un'unica schermata 
interattiva. Rispetto a top e htop, Glances integra CPU, RAM, swap, disco, rete, 
processi, temperatura, container e molto altro, tutto in un'interfaccia coerente e 
altamente configurabile. 
  
Caratteristiche principali: 
• Interfaccia ncurses a colori con soglie visive (verde / giallo / arancio / rosso) 
• Modalità standalone, client/server e web browser 
• Export dei dati verso CSV, InfluxDB, Prometheus, Elasticsearch e altri 
• API REST integrata 
• Supporto per container Docker/Podman 
2. Tre Modi per Installare Pacchetti Python 
Prima di installare Glances è utile capire le differenze tra i metodi di installazione 
disponibili su Debian. 
  
Metodo Comando esempio Quando usarlo 
apt apt install glances Pacchetti di sistema; spesso versioni datate o 
incomplete 
pip3 pip3 install glances Librerie per progetti in sviluppo; usare sempre 
dentro un venv 
pipx pipx install glances Strumenti CLI: ambiente isolato, comando 
disponibile globalmente 
  
Perché non pip3 install globale?  Su Debian 12, pip3 install globale è bloccato per 
default. Il flag --break-system-packages lo forza, ma può sovrascrivere librerie di 
sistema e causare conflitti. Il nome del flag è già un avviso. 
pipx è la soluzione corretta per strumenti CLI come Glances: ogni applicazione vive 
nel proprio ambiente virtuale isolato, il sistema rimane pulito, il comando è 
disponibile nel PATH come un normale programma. 
  
Nota: pipx si installa con apt, non con pip3 
Usare apt per installare pipx, poi pipx per installare Glances: 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
apt install pipx -y 
pipx ensurepath && source ~/.bashrc 
3. Installazione 
Metodo 1 — pip3 (adatto a VM di laboratorio) 
# Installare pip3 se non presente 
apt install python3-pip -y 
  
# Installare Glances con i moduli web 
pip3 install --break-system-packages 'glances[web]' 
  
Metodo 2 — pipx (consigliato su sistemi reali) 
apt install pipx -y 
pipx ensurepath && source ~/.bashrc 
pipx install glances 
pipx inject glances fastapi uvicorn jinja2 aiofiles 
  
Metodo da evitare per la modalità web 
# La versione apt è incompleta: mancano i file statici per glances -w 
# apt install glances   <-- NON usare per la modalità web 
  
Verifica dell'installazione 
glances --version 
4. Avvio e Navigazione di Base 
Avvio standalone 
glances 
  
Navigazione da tastiera 
Tasto Azione 
q / ESC Uscire dall'interfaccia 
h Mostrare la guida 
1 Dettaglio per ogni CPU core 
d Mostrare/nascondere I/O disco 
n Mostrare/nascondere rete 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Tasto Azione 
f Mostrare/nascondere filesystem 
p Ordinare processi per CPU% 
m Ordinare processi per memoria 
i Ordinare per I/O 
t Statistiche di rete aggregate 
w Cancellare log di avvisi 
/ Filtrare processi per nome 
5. Anatomia dell'Interfaccia 
┌─────────────────────────────────────────────────────┐ 
│  hostname   uptime   load avg   utente   ora         │ 
├──────────┬──────────────────┬────────────────────────┤ 
│  CPU     │   MEMORIA        │   SWAP                 │ 
├──────────┴──────────────────┴────────────────────────┤ 
│  RETE (interfacce, TX/RX)                            │ 
│  DISCO (I/O, lettura/scrittura)                      │ 
│  FILESYSTEM (partizioni, uso %)                      │ 
├──────────────────────────────────────────────────────┤ 
│  PROCESSI (PID, utente, CPU%, MEM%, nome)            │ 
└──────────────────────────────────────────────────────┘ 
  
Colori di soglia: 
Colore Soglia Significato 
Verde -- Normale 
Giallo careful Attenzione 
Arancio warning Avviso 
Rosso critical Critico 
6. Modalità Operative 
6.1 Modalità Web (browser) 
Permette di monitorare il server da qualsiasi browser senza client installato. 
# Avviare il web server (porta default: 61208) 
glances -w 
  
# Specificare porta e bind address 
glances -w --port 61208 --bind 0.0.0.0 
Aprire nel browser: http://IP-SERVER:61208 
  
6.2 Modalità Server/Client (via rete) 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Sul server: 
glances -s --port 61209 
Sul client: 
glances -c IP-SERVER --port 61209 
  
6.3 Modalità Non Interattiva (output per script) 
# Output testuale una tantum 
glances --stdout cpu.user,mem.percent,load 
  
# Output CSV 
glances --stdout-csv cpu.user,mem.percent 
7. Configurazione 
Il file di configurazione si trova nei seguenti percorsi: 
/etc/glances/glances.conf       # globale (tutti gli utenti) 
~/.config/glances/glances.conf  # utente corrente 
  
Personalizzare le soglie CPU 
[cpu] 
careful=60 
warning=80 
critical=90 
  
Escludere interfacce di rete 
[network] 
hide=lo,docker0 
  
Abilitare il plugin Docker 
[docker] 
enable=true 
8. Export dei Dati 
# Export verso file CSV 
glances --export csv --export-csv-file /tmp/glances_stats.csv 
  
# Export verso InfluxDB (richiede: pipx inject glances influxdb-client) 
glances --export influxdb 
  

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
Configurazione export CSV in glances.conf 
[csv] 
path=/var/log/glances/stats.csv 
9. Utilizzo in Script e Automazione 
#!/bin/bash 
# Alert via email se CPU supera l'80% 
  
CPU=$(glances --stdout cpu.total --quiet | tail -n1) 
if (( $(echo "$CPU > 80" | bc -l) )); then 
    echo "ALERT: CPU al ${CPU}%" | mail -s "CPU Alert" admin@azienda.it 
fi 
10. Confronto con Altri Strumenti 
Caratteristica top htop Glances 
Interfaccia ncurses          
Vista rete in tempo reale        
Vista disco I/O        
Vista filesystem        
Modalità web browser        
Client/server remoto        
Export dati        
Docker/container        
Soglie visive colorate         
11. Strumento di Supporto: stress-ng 
stress-ng genera carico artificiale sul sistema. In laboratorio è utile per osservare il 
comportamento di Glances sotto stress e verificare visivamente le soglie di allerta. 
apt install stress-ng -y 
  
Comando Effetto 
stress-ng --cpu 2 --timeout 30s Carica 2 core CPU al 100% per 30 secondi 
stress-ng --vm 2 --vm-bytes 256M --timeout 
30s 
Stress sulla memoria RAM 
stress-ng --hdd 1 --timeout 30s Stress sul disco 
stress-ng --cpu 2 --timeout 30s --metrics-
brief 
Stress CPU con statistiche finali 

ITS ICT Piemonte  |  Corso Linux Server 
Glances — Monitoraggio Avanzato del Sistema 
  
In laboratorio 
Aprire due terminali: Glances in uno, stress-ng nell'altro. 
Osservare i colori CPU passare da verde → giallo → arancio → rosso in tempo reale.  
12. Esercizio Pratico 
Scenario — StudioFoto Arcobaleno 
L'amministratore deve configurare un sistema di monitoraggio leggero sul server Debian  
principale, accessibile anche via browser dai tecnici interni. 
  
Obiettivi: 
1. Installare stress-ng e Glances sul server Debian tramite pip3. 
2. Personalizzare le soglie CPU nel file di configurazione (careful=60, warning=80, 
critical=90). 
3. Avviare Glances in modalità web sulla porta 61208. 
4. Connettersi via browser da un'altra VM e verificare le metriche. 
5. In un secondo terminale, eseguire stress-ng --cpu 2 --timeout 60s e osservare il 
cambio di colore in Glances. 
6. Esportare un campione di statistiche in CSV e verificarne il contenuto. 


---

# glances

**File:** `glances.pdf`
**Tipo:** `.pdf`
**Dimensione:** 363.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Glances

Glances
Monitoraggio Avanzato del Sistema
ITS ICT Piemonte  |  Corso Linux Server  |  A.F. 2025-2026

Cos'è Glances?
ITS ICT Piemonte  |  Linux Server
Strumento di monitoraggio di sistema scritto in 
Python che fornisce una panoramica completa 
delle risorse in tempo reale in un'unica 
schermata interattiva.
Rispetto a top e htop integra CPU, RAM, swap, 
disco, rete, processi, temperatura e container —
tutto in un'interfaccia coerente e configurabile.
Caratteristiche principali
• Interfaccia ncurses a colori con soglie 
visive
• Modalità standalone, client/server e web
• Export verso CSV, InfluxDB, Prometheus...
• API REST integrata
• Supporto Docker/Podman

Tre Modi per Installare Pacchetti Python
ITS ICT Piemonte  |  Linux Server
Metodo Comando esempio Quando usarlo
apt apt install glances Pacchetti di sistema; spesso versioni datate o incomplete
pip3 pip3 install glances Librerie per progetti in sviluppo; usare dentro un venv
pipx pipx install glances
 Strumenti CLI: ambiente isolato, comando nel PATH
Nota: pipx si installa con apt, non con pip3
apt install pipx -y
pipx ensurepath && source ~/.bashrc

Installazione di Glances
ITS ICT Piemonte  |  Linux Server
Metodo 1 — pip3  (VM di laboratorio)
# Installare pip3 se non presente
apt install python3-pip -y
# Installare Glances con moduli web
pip3 install --break-system-packages \
'glances[web]'
Metodo 2 — pipx  (sistemi reali)
apt install pipx -y
pipx ensurepath && source ~/.bashrc
pipx install glances
pipx inject glances fastapi uvicorn
Attenzione: la versione apt è incompleta per la modalità web (mancano i file statici). Usare sempre pip3 
o pipx.
Verifica: glances --version

Avvio e Navigazione di Base
ITS ICT Piemonte  |  Linux Server
Avvio standalone
glances
Avvia l'interfaccia interattiva sul terminale 
corrente.
Tasto Azione
q / ESC Uscire
h Guida rapida
1 Dettaglio per CPU core
d I/O disco
n Rete
f Filesystem
p / m Ordina per CPU / memoria
i Ordina per I/O
w Cancella avvisi
/ Filtra processi per nome

L'Interfaccia di Glances
ITS ICT Piemonte  |  Linux Server
┌─────────────────────────────────────────────────────────────┐
│  hostname   uptime   load avg   utente   ora                 │
├──────────────┬─────────────────────┬────────────────────────┤
│  CPU         │   MEMORIA           │   SWAP                 │
├──────────────┴─────────────────────┴────────────────────────┤
│  RETE (interfacce, TX/RX)  |  DISCO (I/O)  |  FILESYSTEM   │
├─────────────────────────────────────────────────────────────┤
│  PROCESSI (PID, utente, CPU%, MEM%, nome)                   │
└─────────────────────────────────────────────────────────────┘
Soglie visive:
Verde — Normale Giallo — Careful Arancio — Warning Rosso — Critical

Modalità Web — glances -w
ITS ICT Piemonte  |  Linux Server
Avvia Glances come web server: accessibile da qualsiasi browser senza installare client sulle macchine 
di monitoraggio.
# Avviare il web server (porta default: 61208)
glances -w
# Porta e bind address personalizzati
glances -w --port 61208 --bind 0.0.0.0
http://
IP-SERVER:61208
Richiede l'installazione con moduli web:
pip3 install --break-system-packages 'glances[web]'   # oppure: pipx inject glances fastapi uvicorn

Modalità Server/Client e Non Interattiva
ITS ICT Piemonte  |  Linux Server
Server/Client — monitoraggio remoto
Sul server:
glances -s --port 61209
Sul client:
glances -c IP-SERVER --port 61209
Non Interattiva
# Output testuale
glances --stdout \
cpu.user,mem.percent
# Output CSV
glances --stdout-csv \
cpu.user,mem.percent
Riepilogo delle modalità operative
standalone → glances              web    → glances -w
server     → glances -s           client → glances -c IP

Configurazione — glances.conf
ITS ICT Piemonte  |  Linux Server
Percorsi del file di configurazione:
/etc/glances/glances.conf       # globale (tutti gli utenti)
~/.config/glances/glances.conf  # utente corrente
Soglie CPU
[cpu]
careful=60
warning=80
critical=90
Escludere rete
[network]
hide=lo,docker0
Plugin Docker
[docker]
enable=true

Export dei Dati e Automazione
ITS ICT Piemonte  |  Linux Server
Export dei dati
# Export CSV
glances --export csv \
--export-csv-file /tmp/stats.csv
# Export InfluxDB
glances --export influxdb
In glances.conf:
[csv]
path=/var/log/glances/stats.csv
Script di automazione
#!/bin/bash
# Alert se CPU > 80%
CPU=$(glances --stdout \
cpu.total --quiet | tail -n1)
if (( $(echo "$CPU > 80" | bc -l) )); then
echo "ALERT: CPU ${CPU}%" |
mail -s "CPU Alert" admin@it
fi

Confronto: top vs htop vs Glances
ITS ICT Piemonte  |  Linux Server
Caratteristica top htop Glances
Interfaccia ncurses
Vista rete in tempo reale
Vista disco I/O
Vista filesystem
Modalità web browser
Client/server remoto
Export dati
Docker/container
Soglie visive colorate


Strumento di Supporto: stress-ng
ITS ICT Piemonte  |  Linux Server
stress-ng genera carico artificiale sul sistema — utile per osservare Glances sotto stress e verificare le 
soglie visive in laboratorio.
apt install stress-ng -y
Comando stress-ng Effetto
--cpu 2 --timeout 30s Carica 2 core CPU al 100% per 30s
--vm 2 --vm-bytes 256M --timeout 30s Stress sulla memoria RAM
--hdd 1 --timeout 30s Stress sul disco
--cpu 2 --timeout 30s --metrics-brief Stress CPU con statistiche finali
In laboratorio
Aprire due terminali: Glances in uno, stress-ng nell'altro.
Osservare CPU passare da verde → giallo → arancio → rosso in tempo reale.

Esercizio Pratico — StudioFoto Arcobaleno
ITS ICT Piemonte  |  Linux Server
Scenario
L'amministratore deve configurare un sistema di monitoraggio leggero sul server Debian principale, accessibile via 
browser dai tecnici interni.
1.  Installare stress-ng e Glances sul server Debian tramite pip3.
2.  Personalizzare le soglie CPU (careful=60, warning=80, critical=90).
3.  Avviare Glances in modalità web sulla porta 61208.
4.  Connettersi via browser da un'altra VM e verificare le metriche.
5.  Eseguire stress-ng --cpu 2 --timeout 60s e osservare il cambio di colore.
6.  Esportare le statistiche in CSV e verificarne il contenuto.

Riepilogo
Glances — vista completa su CPU, RAM, disco, rete e container
Installazione — pip3 o pipx (mai apt per la modalità web)
Tre modalità — standalone, web browser, server/client remoto
Configurazione — soglie visive, export dati, plugin Docker
stress-ng — strumento di test per le soglie in laboratorio
Domande?


---

# Lezione Diagnostica doc

**File:** `Lezione Diagnostica doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3914.8 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte — Linux Server 
Pagina 1 
 
LEZIONE 
Strumenti di diagnostica per sistemi Linux 
Docente: Wolfgang Cecchin 
1. L'approccio a strati 
Quando un sistema non funziona, la tentazione è provare soluzioni a caso. L'approccio 
professionale è diverso: si ragiona dal basso verso l'alto, verificando un livello alla volta.  
Livello 4 — Applicazione     WordPress, configurazione virtual host 
Livello 3 — Servizio         nginx, MariaDB, PHP-FPM, SSH 
Livello 2 — Firewall         iptables, policy, regole 
Livello 1 — Rete             interfacce, IP, routing, DNS 
 
💡 Non ha senso indagare il livello superiore se quello inferiore è rotto. Se la rete non 
funziona, il firewall è irrilevante. Se il firewall blocca tutto, il servizio non è raggiungibile.  
2. Livello 1 — Diagnostica di rete 
Interfacce e indirizzi IP 
ip a                          # tutte le interfacce con IP 
ip a show enp0s8              # una interfaccia specifica 
ip link show                  # stato UP/DOWN delle interfacce 
Cosa cercare: l'interfaccia è UP? Ha un indirizzo IP? L'indirizzo è quello giusto? La netmask è 
corretta? 
Routing 
ip route show                 # tabella di routing 
ip r                          # forma abbreviata 
Cosa cercare: c'è un default gateway? Punta all'indirizzo giusto? 
Connettività 
ping -c 4 10.0.0.2           # raggiungibilità di un host sulla LAN 
ping -c 4 8.8.8.8            # raggiungibilità di internet 
traceroute 8.8.8.8           # percorso dei pacchetti 
Cosa cercare: il ping risponde? Se no, il problema è locale (mittente) o remoto 
(destinatario)? Traceroute mostra dove si ferma il traffico? 
Configurazione persistente 
cat /etc/network/interfaces   # configurazione Debian 
Cosa cercare: le righe auto, iface, address, netmask, gateway corrispondono a quello che 
ci aspettiamo? 

ITS ICT Piemonte — Linux Server 
Pagina 2 
DNS 
cat /etc/resolv.conf          # server DNS configurati 
cat /etc/hosts                # risoluzione locale 
  

ITS ICT Piemonte — Linux Server 
Pagina 3 
3. Livello 2 — Diagnostica del firewall 
Visualizzare le regole attive 
sudo iptables -L -n --line-numbers     # regole leggibili con numeri di riga 
sudo iptables -L INPUT -n -v           # solo catena INPUT, con contatori 
sudo iptables-save                     # dump completo in formato restore 
L'opzione -n è importante: senza di essa, iptables tenta di risolvere ogni IP in un nome DNS, 
rallentando enormemente l'output. 
Cosa cercare 
Policy di default: la prima riga dice Chain INPUT (policy DROP) o (policy ACCEPT)? Con 
policy DROP, tutto ciò che non è esplicitamente permesso viene scartato.  
Ordine delle regole: iptables le legge dall'alto verso il basso e si ferma alla prima che 
corrisponde. Una regola di DROP prima di una di ACCEPT vince. 
Porte aperte: ci sono regole ACCEPT per le porte dei servizi necessari (22/2222 per SSH, 80 per 
HTTP, 3306 per MariaDB)? 
Traffico di ritorno: c'è una regola per ESTABLISHED,RELATED? Senza di essa, le risposte alle 
connessioni in uscita vengono bloccate (es. apt update non funziona).  
File di persistenza 
cat /etc/iptables/rules.v4    # regole salvate (iptables-persistent) 
💡 Se le regole in memoria (iptables -L) sono diverse da quelle nel file, al prossimo riavvio 
si torna alla versione del file. 
4. Livello 3 — Diagnostica dei servizi 
Stato dei servizi 
sudo systemctl status nginx              # stato di nginx 
sudo systemctl status mariadb            # stato di MariaDB 
sudo systemctl status ssh                # stato di SSH 
sudo systemctl status php8.2-fpm         # stato di PHP-FPM 
Cosa cercare: il servizio è active (running) oppure failed? Se failed, il messaggio d'errore dice 
cosa è andato storto. 
Porte in ascolto 
sudo ss -tulnp                           # tutte le porte in ascolto 
sudo ss -tulnp | grep :80               # solo la porta 80 
sudo ss -tulnp | grep :3306             # solo la porta 3306 
Questo comando è fondamentale. Mostra non solo se un servizio è in ascolto, ma anche su 
quale indirizzo: 
Output Significato 
0.0.0.0:80 nginx ascolta su tutte le interfacce (OK) 

ITS ICT Piemonte — Linux Server 
Pagina 4 
127.0.0.1:3306 MariaDB ascolta solo sulla loopback (non 
raggiungibile dalla rete) 
10.0.0.2:3306 MariaDB ascolta solo sulla rete interna (corretto per il 
backend) 
Test di configurazione 
sudo nginx -t                            # verifica sintassi nginx 
sudo sshd -t                             # verifica sintassi SSH 
sudo nginx -T                            # mostra configurazione completa nginx 
Questi comandi controllano la sintassi senza toccare il servizio in esecuzione. Sono sicuri da 
eseguire in qualsiasi momento. 
Log 
sudo journalctl -u nginx --no-pager -n 30     # ultimi 30 log di nginx 
sudo journalctl -u mariadb --no-pager -n 30   # ultimi 30 log di MariaDB 
sudo journalctl -u ssh --no-pager -n 30       # ultimi 30 log di SSH 
I log spesso contengono il messaggio d'errore esatto che spiega perché un servizio non 
parte o non risponde. 
  

ITS ICT Piemonte — Linux Server 
Pagina 5 
5. Livello 4 — Diagnostica applicativa 
Test di connessione al database 
mysql -h 10.0.0.2 -u wpuser -p          # connessione remota a MariaDB 
Se fallisce, la causa può essere a qualsiasi livello inferiore: rete (IP sbagliato), firewall (porta 
bloccata), servizio (bind-address sbagliato) o permessi MySQL (utente non autorizzato per 
quell'IP). 
Test del web server 
curl -I http://localhost                 # header di risposta di nginx 
curl -s http://localhost | head -20      # primi 20 righe della pagina 
💡 Se nginx risponde localmente ma non dall'esterno, il problema è al livello firewall.  
Configurazione nginx 
sudo nginx -T | grep root               # percorso della document root 
sudo nginx -T | grep server_name         # nome a cui risponde nginx 
sudo nginx -T | grep php                 # configurazione PHP-FPM 
ls -la /var/www/wordpress/               # contenuto della directory WordPress 
Nome del sito (server_name) 
Se il server_name non corrisponde a quello che digitiamo nel browser, nginx può servire il sito 
sbagliato. Il nome deve coincidere con quello impostato nel file hosts del client.  
URL di WordPress nel database 
WordPress salva il proprio indirizzo nella tabella wp_options. Se nginx risponde ma WordPress 
fa redirect a un URL diverso, il problema è nel database: 
mysql -h 10.0.0.2 -u wpuser -p wordpress 
 
SELECT option_name, option_value FROM wp_options 
WHERE option_name IN ('siteurl', 'home'); 
I campi siteurl e home devono contenere l'URL con cui si vuole raggiungere il sito. Se 
contengono un nome diverso, WordPress genera redirect e link che puntano all'indirizzo 
sbagliato. 
6. Buone pratiche di troubleshooting 
Cambiare una cosa alla volta. Dopo ogni modifica, verificare se il problema è risolto prima di 
passare alla successiva. Cambiare tre cose insieme e poi scoprire che funziona non insegna 
quale fosse il problema. 
Documentare prima, agire poi. Prima di modificare un file, annotare lo stato attuale. Un cat 
o un iptables -L prima dell'intervento permette di tornare indietro se la modifica peggiora la 
situazione. 
Leggere gli errori. Connection refused è diverso da Connection timed out: il primo indica 
che il servizio non è in ascolto, il secondo che un firewall sta bloccando il traffico.  
Il comando tee 

ITS ICT Piemonte — Linux Server 
Pagina 6 
Nella gestione di iptables incontrerete spesso questa sintassi: 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
tee legge dallo standard input e scrive contemporaneamente su un file e sullo standard 
output — come un raccordo a T idraulico. Il motivo per cui si usa sudo tee invece del 
redirect > è che il redirect viene eseguito dalla shell prima di sudo, quindi non ha i permessi di 
root per scrivere sul file. Con tee che gira come root tramite sudo, il problema non si pone.  
7. Riepilogo comandi 
Obiettivo Comando 
Interfacce e IP ip a 
Routing ip route show 
Connettività ping, traceroute 
Config persistente cat /etc/network/interfaces 
Regole firewall sudo iptables -L -n --line-numbers 
Stato servizi sudo systemctl status <servizio> 
Porte in ascolto sudo ss -tulnp 
Test sintassi nginx sudo nginx -t 
Log servizi sudo journalctl -u <servizio> -n 30 
Test DB remoto mysql -h IP -u utente -p 
Test web locale curl -I http://localhost 
Config nginx completa sudo nginx -T 
URL WordPress SELECT ... FROM wp_options 
Salvare regole iptables sudo iptables-save | sudo tee ... 
 


---

# Lezione Diagnostica ppt

**File:** `Lezione Diagnostica ppt.pdf`
**Tipo:** `.pdf`
**Dimensione:** 170.5 KB
**Ultima modifica:** 02/07/2026 09:22

---

LEZIONE
Strumenti di diagnostica
per sistemi Linux
Docente: Wolfgang Cecchin

L'approccio a strati
Ragionare dal basso verso l'alto, un livello alla volta.
4 Applicazione WordPress, virtual host, wp_options
3 Servizio nginx, MariaDB, PHP-FPM, SSH
2 Firewall iptables, policy, regole
1 Rete Interfacce, IP, routing, DNS
Non ha senso indagare il livello superiore se quello inferiore è rotto.

Livello 1 — Interfacce e IP
L'interfaccia è UP? Ha l'IP giusto? C'è un default gateway?
# Tutte le interfacce con IP
ip a
# Una interfaccia specifica
ip a show enp0s8
# Stato UP/DOWN
ip link show
# Tabella di routing
ip route show

Livello 1 — Connettività e DNS
Ping risponde? Traceroute dove si ferma? Config persistente corretta?
# Raggiungibilità LAN
ping -c 4 10.0.0.2
# Raggiungibilità internet
ping -c 4 8.8.8.8
# Percorso dei pacchetti
traceroute 8.8.8.8
# Configurazione persistente
cat /etc/network/interfaces
# DNS
cat /etc/resolv.conf
cat /etc/hosts

Livello 2 — Regole firewall
# Regole con numeri di riga (-n = no DNS lookup)
sudo iptables -L -n --line-numbers
# Solo catena INPUT con contatori
sudo iptables -L INPUT -n -v
# Dump completo in formato restore
sudo iptables-save
# Regole salvate (persistenza)
cat /etc/iptables/rules.v4

Livello 2 — Cosa cercare
Policy di default
Chain INPUT (policy DROP) o (policy ACCEPT)?
Con DROP, tutto ciò che non è permesso viene 
scartato.
Ordine delle regole
Top-to-bottom, first match wins.
Una regola DROP prima di ACCEPT vince.
Porte aperte
ACCEPT per 2222 (SSH), 80 (HTTP),
3306 (MariaDB)?
Traffico di ritorno
Regola per ESTABLISHED,RELATED?
Senza, apt update non funziona.

Livello 3 — Stato dei servizi
active (running) o failed? I log dicono perché.
# Stato dei servizi
sudo systemctl status nginx
sudo systemctl status mariadb
sudo systemctl status ssh
sudo systemctl status php8.2-fpm
# Test sintassi (senza riavviare)
sudo nginx -t
sudo sshd -t
sudo nginx -T              # config completa
# Log degli ultimi 30 messaggi
sudo journalctl -u nginx --no-pager -n 30
sudo journalctl -u mariadb --no-pager -n 30

Livello 3 — Porte in ascolto
sudo ss -tulnp
Mostra non solo SE un servizio è in ascolto, ma anche su QUALE indirizzo:
Output Significato
0.0.0.0:80 nginx ascolta su tutte le interfacce ✓ OK
127.0.0.1:3306 MariaDB ascolta solo su loopback ✗ Non raggiungibile dalla 
rete
10.0.0.2:3306 MariaDB ascolta su rete interna ✓ Corretto per backend
La differenza tra "la porta è aperta sul firewall" e "il servizio è in ascolto su quell'interfaccia" è cruciale.

Livello 4 — Diagnostica applicativa
Se nginx risponde localmente ma non dall'esterno → problema firewall.
# Test connessione DB da debian3
mysql -h 10.0.0.2 -u wpuser -p
# Test web server locale
curl -I http://localhost
curl -s http://localhost | head -20
# Configurazione nginx
sudo nginx -T | grep root
sudo nginx -T | grep server_name
sudo nginx -T | grep php
# Contenuto directory WordPress
ls -la /var/www/wordpress/

Livello 4 — URL di WordPress nel database
WordPress salva il proprio indirizzo nella tabella wp_options. Se nginx risponde ma WordPress fa 
redirect, il problema è qui:
mysql -h 10.0.0.2 -u wpuser -p wordpress
SELECT option_name, option_value
FROM wp_options
WHERE option_name IN ('siteurl', 'home');
siteurl e home devono contenere l'URL corretto (es. http://acme.local).
Se contengono un nome diverso → redirect e link sbagliati.

Buone pratiche di troubleshooting
Cambiare una cosa alla volta
Dopo ogni modifica, verificare. Cambiare tre cose insieme non insegna quale fosse il problema.
Documentare prima, agire poi
Un cat o un iptables -L prima dell'intervento permette di tornare indietro.
Leggere gli errori
Connection refused ≠ Connection timed out.
Il primo: servizio non in ascolto.
Il secondo: firewall blocca.

Il comando tee
sudo iptables-save | sudo tee /etc/iptables/rules.v4
tee legge dallo stdin e scrive su un file E sullo stdout — come un raccordo a T idraulico.
iptables-save tee → stdout
↓ file
/etc/iptables/rules.v4

Riepilogo comandi
Obiettivo Comando
Interfacce e IP ip a
Routing ip route show
Connettività ping / traceroute
Regole firewall iptables -L -n --line-numbers
Stato servizi systemctl status <servizio>
Porte in ascolto ss -tulnp
Test sintassi nginx nginx -t / nginx -T
Log servizi journalctl -u <servizio> -n 30
Test DB remoto mysql -h IP -u utente -p
URL WordPress SELECT ... FROM wp_options
Salvare iptables iptables-save | sudo tee ...


---

# lezione find

**File:** `lezione find.pdf`
**Tipo:** `.pdf`
**Dimensione:** 4058.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
find 


Introduzione 
Il comando find è lo strumento principale di Linux per cercare file e directory nel filesystem in base 
a criteri molto diversi: nome, tipo, dimensione, proprietario, permessi, data di modifica e altro 
ancora. 
A differenza di ls, che elenca i contenuti di una directory, find esplora ricorsivamente l'albero del 
filesystem a partire da un punto di inizio specificato. 
 
1. Sintassi generale 
$ find [percorso] [criteri] [azione] 
 
Elemento Descrizione 
[percorso] Punto di partenza della ricerca. Si usa / per tutto il filesystem, . per la 
directory corrente, /etc per limitare la ricerca 
[criteri] Uno o più filtri: nome, tipo, proprietario, permessi, dimensione, data...  
[azione] Cosa fare con i file trovati. Se omessa, il default è -print (stampa il 
percorso). Si può usare -exec per eseguire comandi 
 
2. Criteri di ricerca principali 
2.1  Nome del file  (-name, -iname) 
Comando Significato 
find / -name "hosts" Cerca un file chiamato esattamente "hosts" 
find / -name "hosts*" Cerca file il cui nome inizia con "hosts" (* = qualsiasi 
suffisso) 
find / -name "*.conf" Cerca tutti i file con estensione .conf 
find / -iname "hosts" Come -name, ma case-insensitive (HOSTS, Hosts, 
hosts...) 
 
📘 NOTA: Il carattere * è un glob (wildcard), non un'espressione regolare. Deve essere 
racchiuso tra virgolette per evitare che la shell lo espanda prima di passarlo a find.  
 
2.2  Tipo di file  (-type) 
Opzione Tipo cercato 
-type f File regolari 
-type d Directory 
-type l Link simbolici 
 
2.3  Proprietario  (-user, -group) 
L'opzione -user filtra i file appartenenti a un utente specifico: 
$ find / -user linda 
Trova tutti i file nel filesystem il cui proprietario è l'utente linda. 

 
$ find /home -group sviluppo -type f 
Trova tutti i file regolari in /home appartenenti al gruppo sviluppo. 
 
2.4  Dimensione  (-size) 
L'opzione -size accetta un valore con unità e un prefisso che indica il confronto:  
Esempio Significato 
find / -size +2G + = maggiore di 2 GiB 
find / -size -100M - = minore di 100 MiB 
find / -size 4k Esattamente 4 KiB (raro in pratica) 
find / -type f -
size +100M Solo file regolari con dimensione superiore a 100 MiB 
 
2.5  Data di modifica  (-mtime, -mmin) 
Esempio Significato 
find /etc -mtime -1 File modificati nelle ultime 24 ore 
find /etc -mtime +7 File non modificati da più di 7 giorni 
find /tmp -mmin -30 File modificati negli ultimi 30 minuti 
 
3. Ricerca per permessi  (-perm) 
L'opzione -perm permette di cercare file in base ai loro permessi in notazione ottale. Esistono tre 
formati con significati distinti: 
 
3.1  Tre formati di -perm a confronto 
Formato Esempio Significato 
-perm NNNN find . -perm 755 Corrispondenza esatta: il file deve avere 
esattamente quei permessi e nessun altro 
-perm -NNNN find . -perm -111 Tutti i bit devono essere presenti, ma il file 
può averne anche altri (sottoinsieme) 
-perm /NNNN find . -perm /4000 Almeno uno dei bit indicati deve essere 
presente (OR logico) 
 
3.2  I permessi speciali: SUID, SGID, Sticky bit 
I bit speciali si specificano come quarta cifra ottale (la più significativa). Sono fondamentali per la 
sicurezza del sistema. 
 
Bit Valore ottale Effetto 
SUID 4000 Su file eseguibile: viene eseguito con i permessi del 
proprietario del file (es. passwd esegue come root) 
SGID 2000 Su file: esegue con i permessi del gruppo. Su directory: i 
nuovi file ereditano il gruppo della directory 

Sticky bit 1000 
Su directory (es. /tmp): solo il proprietario può eliminare o 
rinominare i propri file, anche se la directory è scrivibile 
da tutti 
 
3.3  Esempi pratici con -perm 
Comando Cosa trova 
find / -perm /4000 File con il bit SUID attivo (formato /) 
find / -perm /2000 File con il bit SGID attivo 
find / -type d -perm /1000 Directory con sticky bit attivo 
find / -perm /7000 File con almeno uno dei permessi speciali (SUID, 
SGID o Sticky) 
find . -perm -111 File eseguibili da user, group e others (tutti e tre i bit 
x presenti) 
find . -perm -002 File scrivibili da "others" (rischio sicurezza) 
find / -perm 755 File con esattamente rwxr-xr-x e nessun altro bit 
 
⚠️ ATTENZIONE: I file con SUID o SGID attivi rappresentano un punto critico per la 
sicurezza. Un file SUID di proprietà di root, se vulnerabile, può essere sfruttato per ottenere 
privilegi di amministratore. È buona pratica censire periodicamente questi file con: find / -
perm /7000 -type f 2>/dev/null 
 
4. Azioni sui file trovati 
4.1  -exec: eseguire un comando su ogni file trovato 
L'opzione -exec permette di eseguire un comando su ciascun file trovato da find. La sintassi 
richiede due elementi obbligatori: 
 
Elemento Significato 
{} Segnaposto che viene sostituito dal percorso del file trovato in ogni 
iterazione 
\; 
Termina il comando -exec. Il backslash (\) è necessario come carattere di 
escape per impedire alla shell di interpretare il punto e virgola come 
separatore di comandi 
 
Sintassi completa 
$ find [percorso] [criteri] -exec comando {} \; 
 
Copiare tutti i file di un utente in una directory 
$ find / -user linda -exec cp {} /root/linda \; 
Per ogni file di proprietà di linda, esegue cp file /root/linda. Il {} viene sostituito dal percorso 
completo del file trovato ad ogni iterazione. 
 
Trovare file con SUID e listarli in dettaglio 
$ find / -perm /4000 -type f -exec ls -lh {} \; 

 
Trovare file in /etc che contengono una stringa e copiarli 
$ find /etc -exec grep -l student {} \; -exec cp {} find/contents/ \; 2>/dev/null 
Esegue due azioni concatenate: prima grep -l per trovare i file che contengono "student", poi cp 
per copiarli. I due -exec vengono eseguiti in sequenza sullo stesso file trovato. 
 
Alternativa con + (più efficiente) 
$ find / -user linda -exec cp {} /root/linda/ + 
Il terminatore + (al posto di \;) raggruppa tutti i file in un'unica chiamata al comando, come 
farebbe xargs. È più efficiente ma il comando deve accettare più argomenti 
contemporaneamente. 
 
4.2  Pipeline con xargs 
In alternativa a -exec, si può usare una pipeline con xargs per passare i risultati di find a un altro 
comando: 
 
$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1" 
Trova tutti i file regolari in /etc/ e cerca la stringa 127.0.0.1 in ciascuno di essi. Equivale a grep -r 
"127.0.0.1" /etc/ ma con il controllo aggiuntivo -type f. 
 
📘 NOTA: xargs è generalmente più efficiente di -exec ... \; perché raggruppa gli 
argomenti in meno chiamate al comando. Tuttavia, con nomi di file contenenti spazi è 
necessario usare: find ... -print0 | xargs -0 comando 
 
4.3  -printf: output personalizzato 
$ find /etc -name '*ini' -printf '%s, %p\n' | sort -rn 
Mostra dimensione in byte (%s) e percorso (%p) di ogni file .ini trovato, ordinati per dimensione 
decrescente (sort -rn). 
 
5. Sopprimere gli errori con 2>/dev/null 
Quando si esegue find a partire dalla radice del filesystem (/), si incontrano spesso directory non 
accessibili all'utente corrente, come /proc, /sys o directory di altri utenti. Questi accessi negati 
generano messaggi di errore su standard error (stderr) che rendono l'output difficile da leggere. 
 
Il reindirizzamento 2>/dev/null scarta tutti i messaggi di errore: 
 
Elemento Valore Significato 
2 stderr File descriptor 2 = standard error (messaggi di errore) 
> redirige Reindirizza l'output verso... 
/dev/null cestino Dispositivo speciale che scarta tutto ciò che riceve 
 
Forma tipica 
$ find / -name "hosts" 2>/dev/null 
Cerca il file "hosts" in tutto il filesystem, ignorando i messaggi "Permission denied".  

 
$ find / -perm /4000 -type f 2>/dev/null 
Trova tutti i file SUID nel sistema, senza mostrare gli errori di accesso negato.  
 
💡 Buona pratica Aggiungere 2>/dev/null quasi sempre quando si usa find su / o su 
directory di sistema. La ricerca resta funzionale e l'output è pulito.  
 
6. Escludere percorsi con !  -path 
Per escludere specifici percorsi dalla ricerca si usa ! (NOT logico) insieme a -path: 
$ find / -name "student" -type f ! -path '*/proc/*' ! -path '*/tmp/*' 
Cerca file chiamati "student" in tutto il filesystem, escludendo le directory /proc e /tmp. Questo è 
utile per evitare i filesystem virtuali e le directory temporanee che raramente contengono i file di 
interesse. 
 
7. Riepilogo delle opzioni principali 
Opzione Descrizione 
-name "pattern" Cerca per nome (case-sensitive, supporta glob *) 
-iname "pattern" Come -name ma case-insensitive 
-type f|d|l Filtra per tipo: file (f), directory (d), link simbolico (l) 
-user nome File appartenenti all'utente specificato 
-group nome File appartenenti al gruppo specificato 
-size +N[kMG] File di dimensione maggiore di N. Unità: k=KiB, M=MiB, G=GiB 
-mtime -N File modificati negli ultimi N giorni 
-perm NNNN Permessi esatti 
-perm -NNNN Tutti i bit indicati presenti (altri possibili) 
-perm /NNNN Almeno uno dei bit indicati presente 
-exec cmd {} \; Esegue un comando su ogni file trovato 
-printf 'formato' Stampa l'output in formato personalizzato 
! -path '*/dir/*' Esclude un percorso dalla ricerca 
2>/dev/null Sopprime i messaggi "Permission denied" 
 
8. Esercizi 
Ricerca base 
Es. 1 — Cercare in tutto il filesystem un file di nome resolv.conf, sopprimendo gli errori. 
Es. 2 — Trovare tutti i file con estensione .log nella directory /var/log. 
Es. 3 — Trovare tutte le directory che si chiamano backup a partire da /home. 
Es. 4 — Trovare i file di proprietà del tuo utente in /tmp. 
 

Ricerca per dimensione e data 
Es. 5 — Trovare tutti i file regolari di dimensione superiore a 100 MiB nel filesystem.  
Es. 6 — Trovare i file in /etc modificati nelle ultime 24 ore. 
 
Permessi 
Es. 7 — Trovare tutti i file nel sistema con il bit SUID attivo. Aggiungere 2>/dev/null per un output 
pulito. 
Es. 8 — Trovare le directory con lo sticky bit attivo (come /tmp). 
Es. 9 — Trovare tutti i file con almeno uno dei permessi speciali (SUID, SGID, Sticky) attivi.  
Es. 10 — Trovare i file scrivibili da "others" in /home (potenziale rischio sicurezza). 
 
Azioni e pipeline 
Es. 11 — Trovare tutti i file di configurazione (*.conf) modificati negli ultimi 7 giorni in /etc e 
visualizzarli con ls -lh usando -exec. 
Es. 12 — Cercare in /etc/ tutti i file che contengono la stringa 127.0.0.1 usando find + xargs grep. 
Es. 13 — Trovare tutti i file di proprietà dell'utente mario e copiarli in /root/backup_mario/, usando -
exec. 
Es. 14 (avanzato) — Trovare file chiamati student nel filesystem, escludendo /proc e /tmp, 
sopprimendo gli errori. 


---

# lezione grep sed awk

**File:** `lezione grep sed awk.pdf`
**Tipo:** `.pdf`
**Dimensione:** 158.5 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT 
Linux 
DOCENTE: _______________________________ 
UNITÀ FORMATIVA: Strumenti Linux per la gestione dei file 
ARGOMENTO: Ricerca nei file: grep, sed, awk 
 
Introduzione 
Linux mette a disposizione tre strumenti fondamentali per cercare e manipolare il testo nei file: 
• grep — cerca righe che contengono un pattern 
• sed — trasforma il testo (cerca e sostituisce) 
• awk — elabora testo strutturato a colonne 
 
I file di esempio utilizzati in questa lezione si trovano nella cartella ~/esercizi/. 
 
1. grep — Cercare nei file 
Il comando grep (Global Regular Expression Print) cerca le righe di un file che corrispondono a un 
pattern e le stampa sullo standard output. Non modifica mai i file. 
Sintassi 
$ grep [opzioni] "pattern" file 
 
Opzioni principali 
Opzione Significato 
-i Ricerca case-insensitive (maiuscole = minuscole) 
-r Ricerca ricorsiva in tutte le sottodirectory 
-n Mostra il numero di riga prima di ogni risultato 
-v Inverte la ricerca: mostra le righe che NON corrispondono 
-l Mostra solo i nomi dei file con almeno una corrispondenza 
-c Conta il numero di righe corrispondenti 
-E Abilita le espressioni regolari estese (ERE) 
-w Cerca solo parole intere (word match) 
 
Esempi pratici 
Ricerca semplice 
$ grep "ERROR" sistema.log 
Cerca tutte le righe che contengono la parola ERROR nel file sistema.log. 
 
Ricerca case-insensitive con numero di riga 
$ grep -n -i "error" sistema.log 
Trova sia ERROR sia error sia Error, mostrando il numero di riga per ogni risultato. 
 
Ricerca invertita 

$ grep -v "^#" webserver.conf 
Mostra tutte le righe del file di configurazione che non iniziano con # (cioè esclude i commenti). 
 
Ricerca ricorsiva 
$ grep -rl "password" /etc/ 
Cerca la parola password in tutti i file dentro /etc/ e mostra solo i nomi dei file trovati. 
 
Uso di espressioni regolari 
$ grep -E "ERROR|WARNING" sistema.log 
Cerca le righe che contengono ERROR oppure WARNING (operatore | = OR). 
 
NOTA: grep non modifica mai i file. Serve solo per trovare e visualizzare righe. Per 
modificare il testo si usa sed. 
 
Ancore nelle espressioni regolari 
Ancora Esempio Significato 
^ grep "^root" utenti.txt Righe che iniziano con "root" 
$ grep "bash$" utenti.txt Righe che terminano con "bash" 
. grep "er.ore" file.txt Il punto sostituisce un qualsiasi carattere 
 
2. sed — Modificare il testo 
Il comando sed (Stream EDitor) legge un file riga per riga, applica una trasformazione e stampa il 
risultato. Di default non modifica il file originale: l'output va sullo standard output. Con l'opzione -i 
la modifica avviene direttamente sul file. 
Sintassi 
$ sed [opzioni] 'comando' file 
 
Il comando di sostituzione: s/// 
Il comando più usato di sed è s (substitute): 
$ sed 's/testo_vecchio/testo_nuovo/flag' file 
 
Flag Significato 
(nessuno) Sostituisce solo la prima occorrenza per ogni riga 
g Sostituisce tutte le occorrenze nella riga (global) 
i Sostituzione case-insensitive 
2 Sostituisce solo la seconda occorrenza 
 
Esempi pratici 
Sostituzione semplice (output su terminale) 
$ sed 's/WARNING/ATTENZIONE/' sistema.log 

Mostra il file con WARNING sostituito da ATTENZIONE nella prima occorrenza di ogni riga. Il file originale 
non viene modificato. 
 
Sostituzione con modifica in-place 
$ sed -i 's/porta = 80/porta = 8080/' webserver.conf 
Modifica direttamente il file webserver.conf, cambiando il valore della porta. 
 
ATTENZIONE: L'opzione -i modifica il file in modo irreversibile. Prima di usarla, verificare il 
risultato senza -i per accertarsi che la sostituzione sia corretta. 
 
Copia di sicurezza automatica con -i 
$ sed -i.bak 's/WARNING/ATTENZIONE/g' sistema.log 
Crea automaticamente una copia di backup sistema.log.bak prima di modificare il file. 
 
Eliminare righe che corrispondono a un pattern 
$ sed '/^#/d' webserver.conf 
Il comando d (delete) elimina le righe che corrispondono al pattern. In questo caso elimina tutti i 
commenti dall'output. 
 
Visualizzare solo un intervallo di righe 
$ sed -n '1,5p' sistema.log 
Con -n (no print) e il comando p mostra solo le righe dalla 1 alla 5. 
 
Workflow consigliato: grep + sed 
Passo 1 — verificare cosa verrà modificato con grep: 
$ grep "livello = WARNING" webserver.conf 
Passo 2 — eseguire la sostituzione con sed (senza -i prima): 
$ sed 's/livello = WARNING/livello = ERROR/' webserver.conf 
Passo 3 — se l'output è corretto, applicare con -i: 
$ sed -i 's/livello = WARNING/livello = ERROR/' webserver.conf 
 
3. awk — Elaborare testo strutturato 
Il comando awk è uno strumento di elaborazione del testo ottimizzato per file con dati a colonne 
(log, CSV, output di comandi). Divide ogni riga in campi e permette di selezionare, filtrare e 
calcolare. 
Sintassi 
$ awk [opzioni] 'pattern { azione }' file 
 
Variabili predefinite 
Variabile Significato 
$0 L'intera riga corrente 
$1, $2, 
... Il primo, secondo, ... campo della riga 
NF Numero totale di campi nella riga corrente 

NR Numero di riga corrente (a partire da 1) 
FS Field Separator: separatore di campo (default: spazio). Si imposta con -F 
 
Esempi pratici 
Stampare una colonna specifica 
$ awk '{print $1}' sistema.log 
Stampa solo la prima colonna (la data) di ogni riga del log. 
 
Usare un separatore personalizzato 
$ awk -F: '{print $1, $3}' utenti.txt 
Usa : come separatore di campo e stampa nome utente (campo 1) e UID (campo 3).  
 
Filtrare per valore di un campo 
$ awk -F: '$3 > 1000 {print $1, $3, $6}' utenti.txt 
Mostra solo gli utenti con UID maggiore di 1000 (utenti normali), con nome, UID e home directory.  
 
Lavorare con file CSV 
$ awk -F, '$3 == "fotocamere" {print $2, $6}' vendite.csv 
Mostra nome prodotto e totale solo per le vendite della categoria fotocamere. 
 
Calcolare la somma di una colonna 
$ awk -F, 'NR>1 {sum += $6} END {print "Totale vendite:", sum}' vendite.csv 
Somma tutti i valori del campo totale (colonna 6) saltando la riga di intestazione (NR>1), poi 
stampa il risultato alla fine. 
 
Contare le occorrenze per categoria 
$ awk -F, 'NR>1 {contatore[$3]++} END {for (cat in contatore) print cat, 
contatore[cat]}' vendite.csv 
Conta quante vendite ci sono per ogni categoria usando un array associativo.  
 
4. Combinare gli strumenti in pipeline 
La vera potenza di grep, sed e awk emerge quando vengono combinati in pipeline con |. 
 
Trovare i file modificati di recente che contengono un pattern 
$ find /etc -name "*.conf" -mtime -7 | xargs grep -l "porta" 
 
Estrarre gli IP che hanno fallito il login 
$ grep "Failed password" sistema.log | awk '{print $11}' | sort | uniq -c | sort -rn 
Estrae le righe con login falliti, prende l'IP (campo 11), conta le occorrenze e le ordina per 
frequenza decrescente. 
 
Mostrare gli utenti reali con la loro shell 
$ grep -v "nologin\|false" utenti.txt | awk -F: '{print $1, "→", $7}' 
Esclude gli utenti di sistema e mostra solo quelli con una shell interattiva reale.  

 
5. Riepilogo comparativo 
Comando Modifica file? Scopo principale Quando usarlo 
grep No Cercare pattern nel 
testo 
Trovare righe che contengono 
una stringa o pattern 
sed Sì con -i Modificare il testo 
(sostituire, eliminare) 
Sostituire testo, eliminare righe, 
trasformare stream 
awk No Elaborare testo a 
colonne 
Analizzare CSV, log, calcoli su 
colonne 
 
6. Esercizi 
File disponibili nella cartella ~/esercizi/: 
 
File Contenuto 
sistema.log Log di sistema con eventi, errori e accessi SSH 
utenti.txt File in formato /etc/passwd con utenti di sistema e reali 
webserver.conf File di configurazione di un server web con commenti 
vendite.csv Dati di vendita in formato CSV con intestazione 
 
Esercizi grep 
Es. 1 — Mostrare tutte le righe di sistema.log che contengono la parola ERROR. 
Es. 2 — Mostrare le righe di sistema.log che contengono ERROR oppure WARNING (usare -E). 
Es. 3 — Contare quante volte appare Failed password nel file di log. 
Es. 4 — In utenti.txt mostrare solo gli utenti la cui shell è /bin/bash. 
Es. 5 — In webserver.conf mostrare tutte le righe non vuote e non commentate (escludere righe 
che iniziano con # o sono vuote). 
 
Esercizi sed 
Es. 6 — Nel file webserver.conf, sostituire WARNING con ERROR solo a video (senza modificare il file). 
Es. 7 — Nel file webserver.conf, eliminare tutte le righe di commento (che iniziano con #) 
dall'output. 
Es. 8 — Nel file sistema.log, sostituire server01 con webserver.lan e salvare il risultato in un nuovo 
file sistema_mod.log. 
 
Esercizi awk 
Es. 9 — Da utenti.txt, estrarre e stampare solo il nome utente (campo 1) e la home directory 
(campo 6) usando : come separatore. 
Es. 10 — Da vendite.csv, mostrare solo le righe della categoria obiettivi con prodotto e prezzo 
unitario. 
Es. 11 — Da vendite.csv, calcolare il totale delle vendite per ogni venditore. 

Es. 12 (avanzato) — Da sistema.log, estrarre tutti gli indirizzi IP che compaiono nel log e contare 
quante volte appare ciascuno. 
 


---

# libri data

**File:** `libri data.sql`
**Tipo:** `.sql`
**Dimensione:** 1.0 KB
**Ultima modifica:** 02/07/2026 09:22

---

INSERT INTO libri (titolo, autore, isbn, pagine, prezzo) VALUES
    ('Il Nome della Rosa',           'Umberto Eco',           '9788845292613',  502,  14.90),
    ('Se questo è un uomo',          'Primo Levi',            '9788806208257',  224,  12.00),
    ('Il Gattopardo',                'Giuseppe Tomasi di Lampedusa', '9788845270939', 318, 13.50),
    ('La Divina Commedia',           'Dante Alighieri',       '9788804673507',  672,   9.90),
    ('Cent anni di solitudine',      'Gabriel García Márquez','9788804668237',  432,  14.00),
    ('1984',                         'George Orwell',         '9788845298257',  328,  11.90),
    ('Il Signore degli Anelli',      'J.R.R. Tolkien',        '9788845298264',  1200, 29.90),
    ('Harry Potter e la Pietra Filosofale', 'J.K. Rowling',   '9788877827022',  320,  10.90),
    ('Il Piccolo Principe',          'Antoine de Saint-Exupéry', '9788861930797', 96,  8.90),
    ('Delitto e Castigo',            'Fëdor Dostoevskij',     '9788845280627',  640,  13.90);


---

# Linux Server 01 Installazione Debian

**File:** `Linux Server 01 Installazione Debian.pdf`
**Tipo:** `.pdf`
**Dimensione:** 581.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
 
Bare Metal vs. Virtual Machines vs. Containers 
 
 
 
 
Fonte: 
https://www.youtube.com/watch?v=TvnZTi_gaNc 
https://diveintodocker.com/ 
  


  3 
Container vs. Severless 
 
 
 
Fonte: 
https://us.nttdata.com/en/blog/tech-blog/serverless-vs-ec2-vs-containers-a-comparative-
study 


  4 
Macchine Virtuali 
 
https://en.wikipedia.org/wiki/Virtual_machine 
 
Alcune Virtual Machines: 
• VM Ware 
• Virtual Box 
• Parallels (per Mac OS) 
• KVM (per Linux) 
• QUEMU 
• Xen 
 
Curiosità 
 
Sistema Operativo Qubes OS 
https://www.qubes-os.org/ 
 
“Security by Isolation”: Qubes utilizza varie Virtual Machines Xen per creare 
ambienti isolati. 
 
  

  5 
 
 
Distribuzioni Unix 
 
Fonte: 
https://en.wikipedia.org/wiki/List_of_Unix_systems 
 
Distribuzioni Linux 
https://en.wikipedia.org/wiki/Linux_distribution 
Immagine: 
https://upload.wikimedia.org/wikipedia/commons/b/b5/Linux_Distribution_Timeline_21_
10_2021.svg 
  


  6 
Principali famiglie di distribuzioni Linux 
 
• Redhat (Fedora, CentOS); 
• Debian (Ubuntu); 
• SuSE Linux; 
• Slackware; 
• Gentoo; 
• Arch linux 
• Android (?!) 
  

  7 
Installazione Virtual Machine VM Ware Workstation 
 
  


  8 
 
 
 
 


  9 
 
                                                                                                                                                                                                                                                                                                  



---

# Linux Server 02 Comandi Essenziali

**File:** `Linux Server 02 Comandi Essenziali.pdf`
**Tipo:** `.pdf`
**Dimensione:** 274.7 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
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
- Substitute User e Sudo; 
- Installare pacchetti 
  

 
  3 
 
  
La shell 
 
https://it.wikipedia.org/wiki/Shell_Unix 
 
https://en.wikipedia.org/wiki/Unix_shell 
 
Esistono vari tipi di shell: 
sh, zsh, bash… 
 
 
Muoversi agevolmente con la shell: 
 
Il tab fornisce l’autocomplete dei comandi noti; 
la freccia in su serve per scorrere la history dei comandi (vedi anche il 
comando “history”); 
CTRL + D effettua il logout; 
CTRL + C interrompe un comando; 
q serve per uscire dalla modalità lettura di alcuni programmi (man); 
~ : è la home directory. 
 
Il comando: 
$ clear # “pulisce” il terminale  

 
  4 
Struttura dei comandi in Linux 
 
La struttura di un comando in Linux è: 
Comando + opzioni + parametri 
 
Es: 
ls = list 
 
 
ls -lah =  
list  
- l = long listening form 
- a = all 
- h = human readable 
 
 
ls -lah /home = 
list  
- l = long listening form 
- a = all 
- h = human readable 
   /home = della directory home 
 
ls -lah /home = fai l’elenco del contenuto (ls) della directory home (/home), 
usando la modalità estesa (long listening form), mostrando tutti i file (all), in 
modo che siano comprensibile da un utente umano 
 
 
Opzioni brevi  
$ ls -lah /home 
 
Opzioni in forma estesa 
$ ls -l --all --human-readable /home 

 
  5 
Manuali ed help dei comandi 
 
$ man ls 
$ ls --help  

 
  6 
 
 
 
Creare file e reindirizzare l’input verso un file 
 
 
$ touch MioFile  
 
$ echo “ciao mondo” > mioFile  
$ echo “ciao mondo” >> mioFile 
 
$ ls > output_ls 
 
Leggere un file 
 
$ cat MioFile 
 
Scrivere un file 
 
$ nano MioFile 
 
Oppure (curiosità): 
 
$ vi MioFile  
 
(:i per scrivere 
:w per salvare 
:q per uscire 
:wq per scrivere e salvare 
:q! per forzare l’uscita) 
 
                                                               
  

 
  7 
Creare directories, Copiare, rinominare, cancellare un file 
 
$ mkdir miaDir #creo una directory 
 
$ cp source destination # copia 
$ cp -R source destination # copia una directory  (copia ricorsiva) 
$ mv oldName newName # rinomino un file 
$ rm file # cancella il file 
$ rm -r directory # rimuove una directory e il suo contenuto 
 
L’opzione -f forza (per lo più evitare di usarla). 
 
 
 
 
 
 
  

 
  8 
 
Muoversi nel file system 
 
$ cd # change directory 
 
$ pwd # quale è la directory corrente? 
 
Simboli “speciali” 
 
. = è la directory stessa; 
.. = è la directory superior; 
/ = è la directory principale del sistema (la root); 
~ = è la home dell’utente (~ è la tilde; su linux usare i tasti: alt gr + ì ) 
 
$ cd / # vado nella directory  root del sistema 
 
$cd - # torno alla directory precedente 
 
$ tree -L 1 / # vedo l’alberatura del sistema  

 
  9 
FHS Filesystem Hierarchy Standard 
 
Riferimenti: 
 
https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard 
 
 
 
 
 
 
Attenzione nelle moderne distribuzioni alcuni directories “puntano” ad altre. 
 
  


 
  10 
 
 
 
Gli utenti 
 
 
root (individuato con #): è l’amministratore del sistema 
 
su = substitute user 
 
 
sudo = “substitute user do” (“super user do”); esegue il comando per un 
altro utente- 
 
E’ necessario aggiungere l’utente in /etc/sudoers.d 
 
Creare un file con il nome utente e aggiungere all’’interno: 
user   ALL=(ALL:ALL) ALL 
 
• The first ALL is the users allowed to use the sudo command.  
• The second ALL defines the hosts (servers) on which sudo can be 
employed.  
• The third ALL is the user you are running the command as. 
• The last ALL defines the commands allowed. 
 
 
Nota: la home di root è /root 
 
Attenzione non confondere: 
l’utente root; 
la home di root che è /root; 
la root directory che è /. 
 
   
  

 
  11 
   
Aggiungere utenti: 
 
# useradd 
 
# useradd -D alberto 
# useradd -d /var/marco marco 
 
# groupadd 
 
File che gestiscono gli utenti 
 
Il file /etc/passwd 
Il file /etc/group 
Il file /etc/shadow 
Il file /etc/shadow 
 
Cambiare password di un utente 
 
Cambiare la propria password: 
$ passwd 
 
Cambiare la password di un utente: 
# passwd marco 
 
  

 
  12 
Link simbolici 
 
$ ln -s file nomeLink                
 
Comando tar (“tape archive”) 
 
Creazione di un archivio: 
 
$ tar cvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 
 
Estrazione di un archivio: 
 
$ tar xvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 
 
 
Creazione di un archivio compresso - compressore gzip – opzione z : 
 
$ tar czvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 file2… 
 
Estrazione di un archivio: 
 
$ tar xzvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 file2… 
 
 
Creazione di un archivio compresso - compressore bz2 – opzione j: 
 
 
$ tar cjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 
 
Estrazione di un archivio: 
 
$ tar xjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 
 
  

 
  13 
 
 
Installazione pacchetti in Debian  
 
Directory di configurazione per i repositories (lo vedremo per il PHP)  
/etc/apt.d  
Per aggiornare i repositories:  
# apt update  
Per installare i pacchetti:  
# apt install  
Attenzione!  
Usare con molta cautela:  
# apt upgrade  
Effettua l’upgrade dei pacchetti disponibili  
                                                                                                                                                                                                                                       


---

# Linux Server 03 utenti e permessi

**File:** `Linux Server 03 utenti e permessi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 206.7 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
 
 
 
 
 
 
 
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
# useradd -d /var/marco marco 
 
# groupadd 
 
File che gestiscono gli utenti 
 
Il file /etc/passwd 
Il file /etc/group 
Il file /etc/shadow 
Il file /etc/gshadow 
 
Aggiungere un utente a un gruppo: 
 
sudo usermod -a -G groupname username 
groups utente → vedo a quali gruppi appartiene l’utente 
 
Cambiare password di un utente 
 
Cambiare la propria password: 
$ passwd 
 
Cambiare la password di un utente: 
# passwd marco 
 

 
  3 
Aggiungo un utente: 
 
# useradd marco 
 
Imposto una password per l’utente 
# passwd marco 
 
Che cosa è capitato? 
 
Lo vedo nel file:  
/etc/passwd 
La cartella /home/marco e /home/alberto non è stata creata, 
infatti c’è bisogno 
di un parametro. 
 
Cancello l’utente e lo ricreo: 
# userdel marco 
 
 
# useradd -m marco 
 
Creare utenti senza home: 
# useradd -M 
 
Creo un secondo utente: 
 
# useradd -m alberto 
 
Imposto una password per l’utente 
# passwd alberto 
 
Faccio il login come Alberto. 
Che shell sto usando? 
$ echo "$SHELL" 
 
Vado a vedere le home directories. 

 
  4 
 
Come Marco provo a entrare nella home di Alberto e creare un 
file: 
$ touch mioFile 
 
Non posso. 
 
Perché? 
 
Perché non ho i permessi: 
drwxr-xr-x  2 alberto alberto 4,0K nov 13 11:17 alberto 
 
 
  

 
  5 
 
I permessi sono organizzati in 3 gruppi: 
- User; 
- Group; 
- Other; 
 
Per ciascuno di questi gruppi viene indicato: 
- Nessun permesso: -; 
- Lettura: r; 
- Scrittura: w; 
- Esecuzione: x. 
 
La lettera “d” in prima posizione indica che si tratta di una 
directory. 
 
Per cambiare permessi: 
$ chmod permissions filename 
 
Ci sono due modi per cambiare permessi. 
  

 
  6 
 
Modalità numerica: 
 
Number Permission Type Symbol 
0 No Permission --- 
1 Execute --x 
2 Write -w- 
3 Execute + Write -wx 
4 Read r-- 
5 Read + Execute r-x 
6 Read +Write rw- 
7 Read + Write +Execute rwx 
 
Esempio: 
$ chmod 764 mioFile 
 
- il proprietario ha tutti i permessi; 
- il gruppo cui appartiene l’utente può leggere e scrivere; 
- Tutti gli altri possono solo leggere. 
 
  

 
  7 
 
Modalità simbolica: 
 
Operator Description 
+ Adds a permission to a file or 
directory 
- Removes the permission 
= Sets the permission and 
overrides the permissions set 
earlier. 
 
User Denotations 
u user/owner 
g group 
o other 
a all 
 
Esempi: 
$ chmod o=rwx mioFile 
 
Tutti gli altri possono leggere, scrivere ed eseguire. 
 
$ chmod g+x 
 
Aggiungo i permessi di esecuzione al gruppo. 
 
$ chmod g-r tolgo i permessi di lettura al gruppo. 
 
Altri comandi utili: 
 

 
  8 
Aggiungere un gruppo: 
# groupadd mynewgroup 
 
Cambiare il gruppo: 
# chgroup 
 
Aggiungere un utente a un gruppo: 
# usermod -a -G examplegroup exampleusername 
(oppure è possibile editare il file /etc/passwd). 
 
 
Cambiare proprietario: 
# chown 
 
Opzione ricorsiva: 
$ chmod -R 755 miaDir 
$ chown -R user:group mioFile. 
 
 
Esercizio: 
Creare una directory e far sì che entrambi gli utenti possano 
scrivere file all’interno. 


---

# Linux Server 03.1 Esercizio-su-utenti-permessi

**File:** `Linux Server 03.1 Esercizio-su-utenti-permessi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 104.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  
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
 
- Per il primo file: solo l’utente proprietario può leggere, scrivere, 
eseguire; 
- Per il secondo file: solo l’utente proprietario e il gruppo ristretto 
possono: leggere, scrivere, eseguire; 
- Per il terzo file: solo l’utente proprietario e il gruppo users possono: 
leggere, scrivere, eseguire; 
- Per il quarto file: tutti possono leggere, scrivere eseguire. 


---

# Linux Server 03.2 Esercizio-su-utenti-permessi

**File:** `Linux Server 03.2 Esercizio-su-utenti-permessi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 203.0 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
- Creare un gruppo interni; 
- Creare un gruppo esterni; 
 
- Assegno 
ignazio e ivan al gruppo interni 
emilio al gruppo esterni 
 
- ignazio vuole creare una sua cartella Documenti (se non c’è 
crearla); 
 
 
 
PARTE 2 
- All’interno di Documenti creare 3 cartelle: 
 
pvt 
interni 
esterni 
 
pvt → solo Ignazio ha accesso in lettura e scrittura; 
interni → hanno accesso Ignazio e Ivan in lettura e scrittura, 
Emilio non può leggere la cartella. 
esterni → hanno accesso tutti, in lettura e scrittura. 
 
All’interno di esterni creare un file 
fileEmilio leggibilie e scrivibile solo da Emilio. 
 
 


---

# Linux Server 03.3 Esercizio-su-utenti-permessi - passaggi

**File:** `Linux Server 03.3 Esercizio-su-utenti-permessi - passaggi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 142.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
o fotografi, postprod, direzione 
3. Assegnare gli utenti ai gruppi:  
o laura e simone al gruppo fotografi 
o elena al gruppo postprod 
o marco al gruppo direzione 
o marco anche al gruppo fotografi e postprod 
4. Creare la struttura directory: 
   /home/studio/ 
   ├── raw/ 
   ├── elaborati/ 
   └── archivio/ 
5. Impostare i permessi in modalità ottale:  
Directory Proprietario Gruppo 
Permes
si ottali 
Risultato 
atteso 
/home/studi
o/ 
marco direzione 755 
Marco: rwx, 
direzione: r -x, 
altri: r-x 
/home/studi
o/raw/ 
marco fotografi 770 
Marco: rwx, 
fotografi: rwx, 
altri: nessuno 

 
  3 
Directory Proprietario Gruppo 
Permes
si ottali 
Risultato 
atteso 
/home/studi
o/elaborati/ 
marco postprod 770 
Marco: rwx, 
postprod: 
rwx, altri: 
nessuno 
/home/studi
o/archivio/ 
marco direzione 750 
Marco: rwx, 
direzione: r -x, 
altri: nessuno 
6. Creare i seguenti file e impostare i permessi:  
o In /home/studio/raw/ creare il file foto001.raw:  
▪ Permessi: 660 (proprietario e gruppo leggono e 
scrivono) 
o In /home/studio/elaborati/ creare il file 
foto001_edit.jpg:  
▪ Permessi: 640 (proprietario legge/scrive, gruppo 
solo legge) 
o In /home/studio/archivio/ creare il file listino_prezzi.txt:  
▪ Permessi: 600 (solo il proprietario legge e scrive) 
 
Verifica: 
• Accedere come simone e verificare di poter creare un file 
in /home/studio/raw/ 

 
  4 
• Accedere come elena e verificare di NON poter accedere 
a /home/studio/raw/ 
• Accedere come elena e verificare di poter modificare file 
in /home/studio/elaborati/ 
• Accedere come laura e verificare di poter solo leggere i file 
in /home/studio/elaborati/ (se aggiunta al gruppo) 
 
 
 
 


---

# Linux Server 03.3 Esercizio-su-utenti-permessi - soluzione

**File:** `Linux Server 03.3 Esercizio-su-utenti-permessi - soluzione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 121.8 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
sudo adduser elena 
Il comando adduser chiederà interattivamente la password e le informazioni aggiuntive 
(nome completo, telefono, ecc.). Per le informazioni opzionali puoi premere Invio per 
saltarle. 
 
2. Creazione dei gruppi 
bash 
sudo addgroup fotografi 
sudo addgroup postprod 
sudo addgroup direzione 
 
3. Assegnazione utenti ai gruppi 
bash 
sudo usermod -aG fotografi laura 
sudo usermod -aG fotografi simone 
sudo usermod -aG postprod elena 
sudo usermod -aG direzione marco 
sudo usermod -aG fotografi marco 
sudo usermod -aG postprod marco 
 
4. Creazione della struttura directory 
bash 
sudo mkdir -p /home/studio/raw 
sudo mkdir -p /home/studio/elaborati 

 
  3 
sudo mkdir -p /home/studio/archivio 
 
5. Impostazione proprietari e gruppi delle directory 
bash 
sudo chown marco:direzione /home/studio 
sudo chown marco:fotografi /home/studio/raw 
sudo chown marco:postprod /home/studio/elaborati 
sudo chown marco:direzione /home/studio/archivio 
 
6. Impostazione permessi in modalità ottale 
bash 
sudo chmod 755 /home/studio 
sudo chmod 770 /home/studio/raw 
sudo chmod 770 /home/studio/elaborati 
sudo chmod 750 /home/studio/archivio 
 
7. Creazione dei file 
bash 
sudo touch /home/studio/raw/foto001.raw 
sudo touch /home/studio/elaborati/foto001_edit.jpg 
sudo touch /home/studio/archivio/listino_prezzi.txt 
Impostare proprietari dei file: 
bash 
sudo chown marco:fotografi /home/studio/raw/foto001.raw 
sudo chown marco:postprod /home/studio/elaborati/foto001_edit.jpg  
sudo chown marco:direzione /home/studio/archivio/listino_prezzi.txt  
Impostare permessi dei file: 
bash 
sudo chmod 660 /home/studio/raw/foto001.raw 
sudo chmod 640 /home/studio/elaborati/foto001_edit.jpg 
sudo chmod 600 /home/studio/archivio/listino_prezzi.txt 
 
8. Verifica 
 
Verificare la struttura creata: 

 
  4 
 
bash 
ls -la /home/studio/ 
ls -la /home/studio/raw/ 
ls -la /home/studio/elaborati/ 
ls -la /home/studio/archivio/ 
 
Verificare i gruppi degli utenti: 
bash 
groups marco 
groups laura 
groups simone 
groups elena 
 
Testare l'accesso come simone (può scrivere in raw): 
bash 
su - simone 
touch /home/studio/raw/test_simone.raw 
ls -la /home/studio/raw/ 
exit 
 
Testare l'accesso come elena (NON può accedere a raw): 
bash 
su - elena 
ls /home/studio/raw/    # Dovrebbe dare "Permission denied" 
touch /home/studio/elaborati/test_elena.jpg    # Dovrebbe funzionare  
exit 
 
Testare che elena non possa accedere all'archivio: 
bash 
su - elena 
ls /home/studio/archivio/    # Dovrebbe dare "Permission denied" 
exit 
 


---

# Linux Server 03.3 Esercizio-su-utenti-permessi

**File:** `Linux Server 03.3 Esercizio-su-utenti-permessi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 98.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
• Laura - fotografa senior 
• Simone - fotografo junior 
• Elena - addetta alla post-produzione 
Lo studio ha bisogno di organizzare i file sul server Linux in base ai 
ruoli: 
• I fotografi (Laura e Simone) devono poter accedere alle 
foto grezze 
• Solo la post-produzione (Elena) deve poter modificare le 
foto elaborate 
• Marco deve avere accesso completo a tutto 
 


---

# Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi

**File:** `Linux Server 03.4 Esercizio-su-utenti-permessi - passaggi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 146.0 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
o scrittori, editing, grafica, amministrazione 
3. Assegnare gli utenti ai gruppi:  
o andrea e chiara al gruppo scrittori 
o luca al gruppo editing 
o luca anche al gruppo scrittori (deve leggere i 
manoscritti) 
o sara al gruppo grafica 
o giulia ai gruppi amministrazione, scrittori, editing, 
grafica 
4. Creare la struttura directory: 
   /home/casaeditrice/ 
   ├── manoscritti/ 
   ├── bozze/ 
   ├── grafica/ 
   │   ├── copertine/ 
   │   └── impaginazione/ 
   └── amministrazione/ 
5. Impostare i permessi in modalità ottale:  

 
  3 
 
6. Creare i seguenti file e impostare i permessi:  
o In /home/casaeditrice/manoscritti/ creare 
romanzo_capitolo1.txt:  
▪ Proprietario: giulia, Gruppo: scrittori 
▪ Permessi: 660 
Directory 
Propri
etario 
Gruppo Permessi ottali Risultato atteso 
/home/casae
ditrice/ 
giulia 
amministrazion
e 
755 Giulia: rwx, tutti: r-x 
/home/casae
ditrice/manos
critti/ 
giulia scrittori 770 
Giulia: rwx, scrittori: 
rwx, altri: nessuno 
/home/casae
ditrice/bozze/ 
giulia editing 770 
Giulia: rwx, editing: 
rwx, altri: nessuno 
/home/casae
ditrice/grafica
/ 
giulia grafica 770 
Giulia: rwx, grafica: 
rwx, altri: nessuno 
/home/casae
ditrice/grafica
/copertine/ 
giulia grafica 770 
Giulia: rwx, grafica: 
rwx, altri: nessuno 
/home/casae
ditrice/grafica
/impaginazion
e/ 
giulia grafica 770 
Giulia: rwx, grafica: 
rwx, altri: nessuno 
/home/casae
ditrice/ammini
strazione/ 
giulia 
amministrazion
e 
700 Solo Giulia: rwx 

 
  4 
o In /home/casaeditrice/bozze/ creare 
romanzo_corretto.txt:  
▪ Proprietario: giulia, Gruppo: editing 
▪ Permessi: 660 
o In /home/casaeditrice/grafica/copertine/ creare 
bozza_copertina.png:  
▪ Proprietario: giulia, Gruppo: grafica 
▪ Permessi: 660 
o In /home/casaeditrice/amministrazione/ creare 
contratti.txt:  
▪ Proprietario: giulia, Gruppo: amministrazione 
▪ Permessi: 600 
 
Verifica: 
• Accedere come andrea e verificare di poter creare un file 
in /home/casaeditrice/manoscritti/ 
• Accedere come luca e verificare di poter leggere i file in 
/home/casaeditrice/manoscritti/ 
• Accedere come luca e verificare di poter scrivere in 
/home/casaeditrice/bozze/ 
• Accedere come sara e verificare di NON poter accedere a 
/home/casaeditrice/manoscritti/ 
• Accedere come sara e verificare di poter scrivere in 
/home/casaeditrice/grafica/copertine/ 

 
  5 
• Accedere come andrea e verificare di NON poter 
accedere a /home/casaeditrice/amministrazione/ 
 


---

# Linux Server 03.4 Esercizio-su-utenti-permessi - soluzione

**File:** `Linux Server 03.4 Esercizio-su-utenti-permessi - soluzione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 110.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
sudo adduser luca 
sudo adduser sara 
Per ogni utente, adduser chiederà la password e le informazioni opzionali (premi Invio per 
saltarle). 
 
2. Creazione dei gruppi 
bash 
sudo addgroup scrittori 
sudo addgroup editing 
sudo addgroup grafica 
sudo addgroup amministrazione 
 
3. Assegnazione utenti ai gruppi 
bash 
sudo usermod -aG scrittori andrea 
sudo usermod -aG scrittori chiara 
sudo usermod -aG editing luca 
sudo usermod -aG scrittori luca 
sudo usermod -aG grafica sara 
sudo usermod -aG amministrazione giulia 
sudo usermod -aG scrittori giulia 
sudo usermod -aG editing giulia 
sudo usermod -aG grafica giulia 
 
4. Creazione della struttura directory 
bash 
sudo mkdir -p /home/casaeditrice/manoscritti 

 
  3 
sudo mkdir -p /home/casaeditrice/bozze 
sudo mkdir -p /home/casaeditrice/grafica/copertine 
sudo mkdir -p /home/casaeditrice/grafica/impaginazione 
sudo mkdir -p /home/casaeditrice/amministrazione 
 
5. Impostazione proprietari e gruppi delle directory 
bash 
sudo chown giulia:amministrazione /home/casaeditrice 
sudo chown giulia:scrittori /home/casaeditrice/manoscritti 
sudo chown giulia:editing /home/casaeditrice/bozze 
sudo chown giulia:grafica /home/casaeditrice/grafica 
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine 
sudo chown giulia:grafica /home/casaeditrice/grafica/impaginazione  
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione  
 
6. Impostazione permessi in modalità ottale 
bash 
sudo chmod 755 /home/casaeditrice 
sudo chmod 770 /home/casaeditrice/manoscritti 
sudo chmod 770 /home/casaeditrice/bozze 
sudo chmod 770 /home/casaeditrice/grafica 
sudo chmod 770 /home/casaeditrice/grafica/copertine 
sudo chmod 770 /home/casaeditrice/grafica/impaginazione 
sudo chmod 700 /home/casaeditrice/amministrazione 
 
7. Creazione dei file 
bash 
sudo touch /home/casaeditrice/manoscritti/romanzo_capitolo1.txt  
sudo touch /home/casaeditrice/bozze/romanzo_corretto.txt 
sudo touch /home/casaeditrice/grafica/copertine/bozza_copertina.png  
sudo touch /home/casaeditrice/amministrazione/contratti.txt 
Impostare proprietari dei file: 
bash 
sudo chown giulia:scrittori /home/casaeditrice/manoscritti/romanzo_capitolo1.txt  

 
  4 
sudo chown giulia:editing /home/casaeditrice/bozze/romanzo_corretto.txt  
sudo chown giulia:grafica /home/casaeditrice/grafica/copertine/bozza_copertina.png  
sudo chown giulia:amministrazione /home/casaeditrice/amministrazione/contratti.txt  
Impostare permessi dei file: 
bash 
sudo chmod 660 /home/casaeditrice/manoscritti/romanzo_capitolo1.txt  
sudo chmod 660 /home/casaeditrice/bozze/romanzo_corretto.txt 
sudo chmod 660 /home/casaeditrice/grafica/copertine/bozza_copertina.png  
sudo chmod 600 /home/casaeditrice/amministrazione/contratti.txt  
 
8. Comandi di verifica 
Verificare la struttura creata: 
bash 
ls -la /home/casaeditrice/ 
ls -la /home/casaeditrice/manoscritti/ 
ls -la /home/casaeditrice/bozze/ 
ls -la /home/casaeditrice/grafica/ 
ls -la /home/casaeditrice/grafica/copertine/ 
ls -la /home/casaeditrice/amministrazione/ 
Verificare i gruppi degli utenti: 
bash 
groups giulia 
groups andrea 
groups chiara 
groups luca 
groups sara 
 
Test accesso come andrea (scrittore): 
bash 
su - andrea 
touch /home/casaeditrice/manoscritti/nuovo_capitolo.txt    # Deve funzionare  
ls /home/casaeditrice/bozze/    # Permission denied 
ls /home/casaeditrice/amministrazione/    # Permission denied 
exit 

 
  5 
 
Test accesso come luca (editor): 
bash 
su - luca 
cat /home/casaeditrice/manoscritti/romanzo_capitolo1.txt    # Deve funzionare (è nel 
gruppo scrittori) 
touch /home/casaeditrice/bozze/nuova_correzione.txt    # Deve funzionare  
ls /home/casaeditrice/grafica/    # Permission denied 
exit 
 
Test accesso come sara (grafica): 
bash 
su - sara 
touch /home/casaeditrice/grafica/copertine/nuova_copertina.png    # Deve funzionare 
ls /home/casaeditrice/manoscritti/    # Permission denied 
ls /home/casaeditrice/bozze/    # Permission denied 
ls /home/casaeditrice/amministrazione/    # Permission denied 
exit 
 
Test accesso come giulia (amministrazione - accesso totale): 
bash 
su - giulia 
ls /home/casaeditrice/manoscritti/    # Deve funzionare 
ls /home/casaeditrice/bozze/    # Deve funzionare 
ls /home/casaeditrice/grafica/    # Deve funzionare 
cat /home/casaeditrice/amministrazione/contratti.txt    # Deve funzionare  
exit 
 
Riepilogo permessi ottali usati 
Ottale Simbolico Significato 
700 rwx------ Solo proprietario ha accesso completo 
755 rwxr-xr-x Proprietario: tutto; altri: lettura ed esecuzione 
770 rwxrwx--- Proprietario e gruppo: tutto; altri: nessuno 

 
  6 
Ottale Simbolico Significato 
660 rw-rw---- Proprietario e gruppo: lettura/scrittura 
600 rw------- Solo proprietario: lettura/scrittura 
 


---

# Linux Server 03.4 Esercizio-su-utenti-permessi

**File:** `Linux Server 03.4 Esercizio-su-utenti-permessi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 98.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
• Andrea - scrittore 
• Chiara - scrittrice 
• Luca - editor/correttore di bozze 
• Sara - grafica (impaginazione e copertine) 
La casa editrice ha bisogno di organizzare i file sul server Linux: 
• Gli scrittori (Andrea e Chiara) devono poter lavorare sui 
manoscritti 
• L'editor (Luca) deve poter leggere i manoscritti e modificare 
le bozze corrette 
• La grafica (Sara) deve poter accedere solo alla cartella 
delle copertine e dell'impaginazione 
• Giulia deve avere accesso completo a tutto, inclusi i file 
amministrativi 
 


---

# Linux Server 04 SSH

**File:** `Linux Server 04 SSH.pdf`
**Tipo:** `.pdf`
**Dimensione:** 345.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
 
 
 
 
 
 
 
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
client e un server. 
 
Attraverso SSH un utente può inviare comandi a un computer 
remoto. 
 
Precedentemente per collegarsi alle macchine si utilizzava 
Telnet: servizio che è stato abbandonato, perché la 
comunicazione tra client e server avveniva in chiaro. 
 
Approfondimenti: 
 
https://en.wikipedia.org/wiki/Secure_Shell 
 
 
Utilizziamo VM Workstation con NAT 
 
Per evitare di avere conflitti con altre macchine (e con la rete di 
ITS) utilizziamo VM Ware Workstation con NAT (“Network Address 
Translation”) 
 
Soluzione per Virtual Box: 
Utilizzare scheda solo host, eventualmente aggiungendo una 
seconda scheda. 
 
https://www.slideshare.net/powerhan96/networking-between-
host-and-guest-v-ms-in-virtual-box 
 

 
  3 
 
 
 
 
Installiamo su Debian il server SSH 
 
Aggiorniamo i repositories: 
$ sudo apt update 
 
$ sudo apt install openssh-server 
 
Controlliamo di avere installato: 
 


 
  4 
$ sudo systemctl status sshd 
 
Controlliamo che sia in ascolto sulla porta 22: 
 
$ netstat -tulpn | grep 22 
 
Impostiamo il server SSH perché parta all’avvio: 
 
$ sudo systemctl enable ssh 
 
Nel caso in cui sia installato un firewall, dobbiamo consentire l’ingresso per 
ssh: 
 
$ sudo ufw allow ssh 
 
 
Il file di configurazione di ssh si trova all’interno di /etc 
 
Attenzione: 
/etc/ssh/ssh_config → è il file di configurazione del client  ssh del 
sistema 
/etc/ssh/sshd_config → è il file di configurazione del server ssh 
 
Invece: 
 
/etc/ssh/ssh_config.d → è una directory. Vengono includi tutti i 
files di configurazione del client ssh del sistema 
 
/etc/ssh/sshd_config.d → è una directory. Vengono includi tutti i 
files di configurazione del server ssh del sistema 
 
A noi, se vogliamo modificare le configurazioni di ssh, interessa 
modificare il file: 
/etc/sshd_config 
 
Individiuamo l’IP della macchina 
 

 
  5 
$ hostname -I 
Dalla macchina Windows (cioè la macchina host) possiamo 
utilizzare un client ssh per connettersi alla macchina: 
 
$ ssh its-user@ip-della-macchina-guest 
 
 
Crittografia simmetrica 
 
https://it.wikipedia.org/wiki/Crittografia_simmetrica 
 
 
  


 
  6 
Crittografia asimmetrica 
 
https://it.wikipedia.org/wiki/Crittografia_asimmetrica 
 
 
 
 
 
  


 
  7 
Connessione tramite SSH 
 
SSH utilizza crittografia simmetrica per crittografare la 
connessione tra client e server. La crittografia del canale in 
modalità asimmetrica sarebbe troppo onerosa (troppo lenta) a 
livello di calcolo. 
 
Tuttavia la fase di autentificazione può avvenire attraverso 
crittografia asimmetrica e chiave pubblica. 
 
Nella powershell di Windows generiamo una coppia di chiavi 
pubblica/privata (non specificando nulla verrà usato l’algoritmo 
RSA): 
 
> ssh-keygen 
 
 
 
  


 
  8 
Nella home dell’utente è stata creata una cartella .ssh con le 
chiavi pubbliche e private. 
 
 
 
 
In Debian andiamo a copiare la chiave pubblica nella cartella 
/root/.ssh 
 
Ci sono molti modi per farlo, ad esempio da Windows: 
 
> scp .\id_rsa.pub its-user@192.168.206.128:/home/its-user 
> ssh its-user@192.168.206.128 
 
E poi nella macchina Debian: 
 
$ cat id_rsa.pub >> ~/.ssh/authorized_keys 
 
Il contenuto del file authorizes_keys è una lista di chiavi 
pubbliche: 
 
 
 



---

# Linux Server 05 dns hosts

**File:** `Linux Server 05 dns hosts.pdf`
**Tipo:** `.pdf`
**Dimensione:** 265.5 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ 
FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
DNS, file hosts 


 
2 
 
 
Lo scopo di assegnare dei nomi agli indirizzi IP è quello di rendere più facile la 
memorizzazione per le persone. In verità, un indirizzo IP identifica un'interfaccia di rete 
associata con un dispositivo come una scheda di rete. Poiché ogni macchina può avere più 
schede e più interfacce per ogni scheda, un singolo computer può avere più nomi nel 
sistema dei nomi di dominio. 
 
 
https://debian-handbook.info/browse/it-IT/stable/sect.hostname-name-service.html 
 
 
Il servizio DNS 
 
 
https://it.wikipedia.org/wiki/Nome_di_dominio 
 
https://it.wikipedia.org/wiki/Domain_Name_System 
 
 
 
Interrogare il DNS 
 
$ dig google.com 
 
The most important section is the ANSWER section: 
• The first column lists the name of the server that was queried 
• The second column is the Time to Live, a set timeframe after which the record is 
refreshed 
• The third column shows the class of query – in this case, “IN” stands for Internet 
• The fourth column displays the type of query – in this case, “A” stands for an A 
(address) record 
•  The final column displays the IP address associated with the domain name 
 
Tipi di record DNS - Wikipedia 
 
 

 
  3 
Ricordarsi: 
 
A NAME = Address Name 
CNAME = Canonical Name 
MX = Mail Server 

 
  4 
Associare un nome a un IP 
 
E’ possibile associare il nome di un dominio a un server (o meglio a un IP) attraverso il 
servizio DNS. 
 
E’ possibile tuttavia informare la macchina locale dell’associazione di un nome dominio e 
IP attraverso il file “hosts”. 
 
Posizione su Linux / Mac: 
/etc/hosts  
 
Nota bene: molti file di configurazione importanti in Linux si trovano nella directory /etc 
 
Posizione su Windows: 
c:\Windows\System32\Drivers\etc\hosts 
 
Sintassi del file hosts: 
127.0.0.1 localhost  
192.168.0.1 mioSito.example.com mioSito 
127.0.1.1 mercoledi.local 
 
 
 
 


---

# Linux Server 05.01 Esercizio nome host

**File:** `Linux Server 05.01 Esercizio nome host.pdf`
**Tipo:** `.pdf`
**Dimensione:** 203.5 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
 
SOFTWARE DEVELOPER 
Linux Server 
Docente: Wolfgang Cecchin 
Titolo argomento: DNS, File Host esercizio 
 

 
 
 
Esercizio 
 
 
Creare i nomi domini 
 
tuoCognome.local 
tuoCognome 
 
all’interno della macchina virtuale. 
 
 
Connettersi alla macchina virtuale usando il nome dominio: 
 
tuCognome.local 
 


---

# Linux Server 06 http server

**File:** `Linux Server 06 http server.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1076.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
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
side/First_steps/Client-Server_overview 
 
Codici si stato 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status 
 
https://it.wikipedia.org/wiki/Codici_di_stato_HTTP 
 
 
Architettura statica: 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 
  3 
 
Architettura dinamica: 
 
  


 
  4 
 
 
“Configurazione” di un webserver 
 
 
• Assegniamo un nome al server; 
•  Troviamo uno spazio per mettere i files; 
• Diciamo al webserver come associare il nome ai files da servire; 
• Configuriamo i log. 
  

 
  5 
Installazione nginx 
 
$ sudo apt update 
$ sudo apt install nginx 
Far partire, riavviare, fermare, conoscere lo stato di Nginx 
$ sudo systemctl start nginx 
$ sudo systemctl restart nginx 
$ sudo systemctl stop nginx 
$ sudo systemctl status nginx 
Di default Nginx è in ascolto sulla porta 80 
(di default anche Apache!). 
Testare e ricaricare la configurazione di nginx: 
$ sudo nginx -t 
$ sudo systemctl reload nginx 
 
  

 
  6 
Configurazione di nginx 
 
 
I file di configurazione si trovano in: 
/etc/nginx 
La configurazione dei siti si trova in: 
/etc/nginx/sites-available 
Esiste una configurazione di default, quindi se io digito nel browser della mia macchina 
locale un sito che ho impostato in /etc/hosts, ad esempio: 
http://localhost 
http://mercoledi.local 
mi risponde la pagina di default di Nginx. 
  

 
  7 
 
 
  


 
  8 
Creiamo una directory in cui inserire i file del sito. 
Ad esempio: 
/var/www/mercoledi.local 
oppure: 
/srv/www/mercoledi.local 
 
La configurazione del sito devo inserirla in: 
/etc/nginx/sites-available 
ma il sito va attivato con link simbolico in: 
/etc/nginx/sites-enabled 
 
Configurazione minima del file: 
/etc/nginx/sites-available/mercoledi.local.conf 
 
server { 
 listen 80; 
 listen [::]:80; 
  
 server_name mercoledi.local; 
  
 root /var/www/mercoledi.local; 
 index index.html; 
  
 location / { 
  try_files $uri $uri/ =404; 
 } 
} 
In questo modo sto dicendo che chiamando 
http://mercoledi.local 
mi vengono serviti i files che si trovano nella directory: 
/var/www/mercoledi.local 
Attenzione! Non abbiamo ancora attivato il sito! 
  

 
  9 
Configuriamo i log del web server 
 
/var/log è la directory in cui si trovano i files di log dei principali servizi su Linux. 
I log sono gestiti dal servizio (detto anche “demone”) syslogd, che tra le altre cose si 
occupa anche della compressione. 
 
Aggiungiamo i log specifici per questo sito: 
 
server { 
 listen 80; 
 listen [::]:80; 
  
 server_name mercoledi.local; 
  
 root /var/www/mercoledi.local; 
 index index.html; 
  
 location / { 
  try_files $uri $uri/ =404; 
 } 
access_log /var/log/nginx/mercoledi.local.log; 
error_log    /var/log/nginx/mercoledi.local.error.log: 
} 
  

 
  10 
Codici di stato http 
 
All’interno dei log sono memorizzate le risposte e gli errori del web server. 
Esempio: 
 
 
 
 
Approfondimenti sui codici di risposta http: 
https://it.wikipedia.org/wiki/Codici_di_stato_HTTP 
  


 
  11 
Attivazione di un sito 
 
 
Attiviamo il sito. 
 
Ricordate? 
La configurazione del sito devo inserirla in: 
 
/etc/nginx/sites-available 
 
ma il sito va attivato con link simbolico in: 
 
/etc/nginx/sites-enabled 
 
Per creare un link usiamo la sintassi: 
 
$ sudo ln -s source nomeLink 
 
Creiamo un link simbolico: 
 
$ sudo ln -s /etc/nginx/sites-available/mercoledi.conf /etc/nginx/sites-
enabled/mercoledi.conf 
 
Verifico la configurazione e ricarico nginx: 
$ sudo nginx -t 
$ sudo systemctl reload nginx 
 
  

 
  12 
Riepilogo 
• Configuriamo /etc/hosts; 
 
• Abbiamo creato una directory per il sito: 
/var/www/mercoledi.local; 
 
• Abbiamo configurato il sito inserendo la configurazione in: 
/etc/nginx/sites-available/mercoledi.local.conf; 
 
• Abbiamo impostato i log su: 
/var/log/nginx/mercoledi.local.log e mercoledi.local.error.log 
 
• Abbiamo attivato il sito creando un link che punta 
da sites/available a sites/enabled; 
 
Abbiamo verificato la configurazione e riavviato Nginx. 
 
  

 
  13 
Configurazione di Apache 2 
 
Normalmente si sceglie di utilizzare Nginx o Apache2. Tuttavia in casi particolari 
possiamo scegliere di averli entrambi sulla stessa macchina: 
 
$ sudo apt install apache2 
 
Modifichiamo le porte su cui ascolta Apache: 
/etc/apache2/ports.conf 
 
Modificando la seguente riga: 
Listen 8080 
 
Andiamo nella directory: 
/etc/apache2/sites-available 
 
Cambiamo la configurazione di default, cioè il file: 
000-default.conf  
Specificando: 
 
<VirtualHost *:8080> 
 
(Nota: se - al contrario - voglio cambiare le porte su cui ascolta Nginx devo invece 
modificare i seguenti file: 
nginx.conf 
alla riga: 
listen 80 default_server 
 
e la configurazione di default di Nginx). 
  

 
  14 
Far partire, riavviare, fermare, conoscere lo stato di Apache2: 
$ sudo systemctl start apache2 
$ sudo systemctl restart apache2 
$ sudo systemctl stop apache2 
$ sudo systemctl status apache2 
Testare e ricaricare la configurazione di Apache2: 
$ sudo apachectl -t 
$ sudo systemctl reload apache2 
  

 
  15 
Ma chi è in ascolto sulla porta 80 e chi sulla 8080? 
 
Installiamo il seguente pacchetto Debian: 
$ sudo apt install net-tools 
 
e lanciamo: 
$ sudo netstat -tulpn 
 
 
  


 
  16 
Configurazione di Apache 2 
 
Vogliamo adesso creare un caso pratico: 
 
vogliamo che all’host merc.apache.local (inventato or ora) risponda Apache 
(ma prima lo configureremo perché risponda con http://merc.apache.local:8080) 
 
Creiamo in /etc/hosts un entry: 
 
127.0.1.1               merc.apache.local 
 
Chiamando: 
http://merc.apache.local 
Chi mi risponde? 
 
Posso analizzare gli headers http per verificarlo. 
Ad esempio, installando cURL (client for URL): 
 
$ sudo apt install curl 
 
$ curl -I merc.apache.local 
 
HTTP/1.1 301 Moved Permanently 
Server: nginx/1.16.0 
Date: Mon, 21 Oct 2019 20:36:07 GMT 
 
Mi sta rispondendo Nginx e non Apache. 
  

 
  17 
Attenzione! L’installazione di Apache appena effettuata è andata a sovrascrivere la pagina 
di default di Nginx in 
/var/www/html/index.html 
 
In realtà solo il file HTML è stato sovrascritto: ci sta rispondendo Nginx che è in ascolto 
sulla porta 80, porta di default per il webserver. 
 
 
 
Per evitare di essere di nuovo ingannati, creiamo una pagina html generica di default: 
 
/var/www/html/index.html 
<html> 
<head> 
  <title> 
   Pagina di default 
  </title> 
 </head> 
 
 <body> 
  <h1>Pagina di default</h1> 
 </body> 
</html>   


 
  18 
 
Ma come configuriamo un sito con Apache? 
 
Con la stessa procedura di Nginx, cioè: 
 
• Configuriamo /etc/hosts; 
 
• Creiamo una directory per il sito: 
/var/www/merc.apache.local; 
 
• Configuriamo il sito inserendo la configurazione in: 
/etc/apache2/sites-available/merc.apache.local.conf; 
 
• Impostiamo i log su: 
/var/log/apache2/merc.apache.local.log e merc.apache.local.error.log 
 
• Attiviamo il sito creando un link che punta 
da sites/available a sites/enabled; 
 
Verifichiamo la configurazione e riavviamo Apache. 
  

 
  19 
Creiamo una directory in cui inserire i file del sito. 
Ad esempio: 
/var/www/merc.apache.local 
La configurazione del sito devo inserirla in: 
/etc/apache2/sites-available 
ma il sito va attivato con link simbolico in: 
/etc/apache2/sites-enabled 
Configurazione minima del file: 
/etc/Apache2/sites-available/merc.apache2.local.conf 
<VirtualHost *:8080> 
        ServerName merc.apache.local 
        ServerAdmin webmaster@localhost 
        DocumentRoot /var/www/merc.apache.local 
        ErrorLog ${Apache2_LOG_DIR}/merc.apache.local.error.log 
        CustomLog ${Apache2_LOG_DIR}/merc.apache.local.access.log combined 
</VirtualHost> 
In questo modo sto dicendo che chiamando 
http://merc.apache.local:8080 
mi vengono serviti i files che si trovano nella directory: 
/var/www/merc.apache.local 
Attenzione! Non abbiamo ancora attivato il sito!  

 
  20 
Attiviamo il sito. 
 
La configurazione del sito va inserita in: 
/etc/apache2/sites-available 
 
ma il sito va attivato con link simbolico in: 
/etc/apache2/sites-enabled 
 
Per creare un link uso la sintassi: 
$ sudo ln -s source nomeLink 
Creo un link simbolico: 
$ sudo ln -s /etc/apache2/sites-available/mer.apache.conf /etc/apache2/sites-
enabled/mer.apache2.conf 
Verifico la configurazione e ricarico Apache2: 
$ sudo apachectl -t 
$ sudo systemctl reload apache2 
  

 
  21 
Per evitare di annoiarci con operazioni ripetitive, il team di sviluppo di Apache ha creato 
un comando che esegue per noi queste operazioni: 
 
$ sudo a2ensite merc.apache.local.conf 
 
$ sudo a2dissite merc.apache.local.conf 
  

 
  22 
Quindi adesso sullo stesso host  ci rispondono:  
nginx sulla porta 80 
http://merc.apache.local 
 
e 
Apache2 sulla porta 8080 
http://merc.apache.local:8080 
 
 
 
 
 
  


 
  23 
Ma come facciamo a far sì che su un host mi risponda Apache, quando c’è Nginx di 
mezzo? 
Dobbiamo configurare Nginx come reverse proxy. 
 
Posso ad esempio crearmi una configurazione /etc/nginx/sites-available/apache.conf che 
contenga: 
server { 
    listen 80; 
    server_name merc.apache.local; 
 
    location / { 
        proxy_pass http://merc.apache.local:8080; 
        proxy_set_header Host $host; 
        proxy_set_header X-Real-IP $remote_addr; 
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; 
        proxy_set_header X-Forwarded-Proto $scheme; 
    } 
} 
 
(Ovviamente perché sia attiva va linkato in /etc/nginx/sites-enabled/ ). 
 
Approfondimenti: https://www.digitalocean.com/community/tutorials/how-to-configure-
nginx-as-a-web-server-and-reverse-proxy-for-apache-on-one-ubuntu-18-04-server 
 


---

# Linux Server 06.1 http server esercizio

**File:** `Linux Server 06.1 http server esercizio.pdf`
**Tipo:** `.pdf`
**Dimensione:** 202.4 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
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
• Reindirizzare i log 
 
 
Passaggi: 
- Creare il file di configurazione; 
- Nel file di configurazione indicare: 
o Server_name; 
o Posizione dei files; 
o Posizione dei log; 
- Testare la sintassi; 
- Riavviare il server 
- Controllare che sia tutto ok. 
 


---

# Linux Server 06.2 http server esercizio

**File:** `Linux Server 06.2 http server esercizio.pdf`
**Tipo:** `.pdf`
**Dimensione:** 208.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
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
 
 
Creare il dominio moleantonelliana.local 
 
 
Associare il webserver al dominio moleantonelliana.local 
 
• Servire uno più file html 
• Reindirizzare i log 
 
 
Passaggi: 
- Creare il file di configurazione; 
- Nel file di configurazione indicare: 
o Server_name; 
o Posizione dei files; 
o Posizione dei log; 
- Testare la sintassi; 
- Riavviare il server 
- Controllare che sia tutto ok. 
 


---

# Linux Server 06.3 http server esercizio

**File:** `Linux Server 06.3 http server esercizio.pdf`
**Tipo:** `.pdf`
**Dimensione:** 104.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
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
 
- Abbiamo uno spazio sul server che contiene i files del sito (una 
directory sul server). 
 
Utilizzare Filezilla per scaricare / caricare i files. 
 
Creare un menu e le pagine corrispondenti alle seguenti voci: 
 
- Chi sono; 
- Studi; 
- Hobbies; 
- Film (inserire una lista di film / serie TV preferiti); 
- Sport… 
- (altre voci) 
 
 


---

# Linux Server 06.4 http server esercizio

**File:** `Linux Server 06.4 http server esercizio.pdf`
**Tipo:** `.pdf`
**Dimensione:** 104.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
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
 
- Abbiamo uno spazio sul server che contiene i files del sito (una 
directory sul server). 
 
Utilizzare Filezilla per scaricare / caricare i files. 
 
Creare un menu e le pagine corrispondenti alle seguenti voci: 
 
- Chi sono; 
- Studi; 
- Hobbies; 
- Film (inserire una lista di film / serie TV preferiti); 
- Sport… 
- (altre voci) 
 
 


---

# Linux Server 07 mysql

**File:** `Linux Server 07 mysql.pdf`
**Tipo:** `.pdf`
**Dimensione:** 343.8 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
 
MySQL e MariaDB: differenze e similitudini 
1) Origine e storia 
MySQL nasce nel 1995 e diventa uno dei database relazionali open source più diffusi al 
mondo. Nel 2010 viene acquisito da Oracle, che ne mantiene lo sviluppo con una doppia 
licenza: community (GPL) e commerciale. 
MariaDB nasce nel 2009 come fork diretto di MySQL, creato dagli stessi fondatori 
originali (Michael "Monty" Widenius e altri) proprio in risposta all'acquisizione da parte di 
Oracle, temendo una chiusura del progetto. Il nome deriva da Maria, figlia di Widenius 
(come MySQL derivava da "My", l'altra figlia). 
La sintassi tra le due versioni è comune al 95%. Dalla versione 10.x di MariaDB in poi, la 
compatibilità con MySQL non è più garantita al 100% — alcune funzionalità avanzate di 
MySQL non esistono in MariaDB e viceversa. 
 
 
Regola pratica: MariaDB è la scelta più comune nelle distribuzioni Debian/Ubuntu (è il 
pacchetto installato di default con apt install mariadb-server), mentre MySQL è più 
frequente in ambienti enterprise o su sistemi Red Hat/CentOS.  
 
 
$ sudo apt install mariadb-server  
 
 
$ sudo systemctl start mariadb 
 
$ sudo systemctl enable mariadb 
 
$ sudo systemctl status mariadb 
 
 
 
 
 
 
 
 
 

  4 
Creazione utenti e creazione di un semplice database 
 
Entrare nel mysql, utilizzando il client: 
 
$ sudo mysql -u root -p 
 
-u = user 
- p = password 
 
 
Per creare un datbase: 
 
CREATE DATABASE miodatabase; 
 
SHOW DATABASES; 
 
Per usarlo: 
USE miodatabase; 
 
 
Per creare un utente per utilizzare il database: 
 
CREATE USER 'its-usr'@'localhost' IDENTIFIED BY 'password'; 
 
Per attribuire i privilegi: 
 
GRANT ALL PRIVILEGES ON miodatabase.* TO 'username'@'localhost'; 
 
FLUSH PRIVILEGES; 
 
Forma deprecata: 
 
GRANT ALL ON nomedb.* TO 'its-usr'@'localhost' IDENTIFIED BY 'password'; 
(creava utente privilege in un solo passaggio. 
 
L’utente è attivo solo per localhost, cioè solo per la macchina locale. 
 
 
 
Per cancellare un utente (revoca anche i privilegi): 
 
DROP USER IF EXISTS 'its-usr'@'localhost'; 
 

  5 
Creare un utente che si connetta da qualsiasi IP 
(sconsigliabile) 
 
CREATE USER 'its-usr'@'%' IDENTIFIED BY 'password'; 
GRANT ALL PRIVILEGES ON miodatabase.* TO 'its-usr'@'%'; 
FLUSH PRIVILEGES; 
 
Attenzione! 
Per accedere da remoto è anche necessario modificare il file: 
 
/etc/mysql/mariadb.conf.d/50-server.cnf 
Modificare la configurazione: 
 
bind-address            = 0.0.0.0 
 
Avvertenze di sicurezza  
 
• Non usare @'%' in produzione — preferire sempre un IP specifico o una subnet 
(@'192.168.1.%') 
 
• Non esporre la porta 3306 su Internet — usare una VPN o un tunnel SSH 
 
• Il bind su 0.0.0.0 espone il database su tutte le interfacce di rete, inclusa quella 
pubblica se present 
 
 
 
Approfondimento: Apici singoli, Backtick, Virgolette 
doppie 
 
' Apici singoli — stringhe e valori 
Usati per delimitare valori letterali: stringhe, password, date. 
 
SELECT * FROM utenti WHERE nome = 'Mario'; 
 
INSERT INTO prodotti (nome) VALUES ('Laptop'); 
 
CREATE USER 'its-usr'@'localhost' IDENTIFIED BY 'password'; 
 

  6 
 
` Backtick — identificatory 
(Linux / Windows: Altgr + ì; oppure Windows: Alt + 96 su tastierino numerico) 
 
Usati per delimitare nomi di oggetti del database: tabelle, colonne, database. Necessari 
quando il nome: 
• coincide con una parola riservata di SQL 
• contiene spazi o caratteri speciali 
 
-- "select" è una parola riservata: senza backtick darebbe errore 
SELECT `select`, `order` FROM `my-table`; 
 
-- Normalmente non servono, ma non fanno mai male 
SELECT `nome`, `cognome` FROM `utenti`; 
 
I backtick servono solo in casi particolari. Se i nomi delle tabelle e colonne sono normali 
(niente spazi, niente parole riservate), puoi scrivere senza. 
 
-- Questi sono equivalenti se "utenti" non è una parola riservata: 
SELECT nome FROM utenti; 
SELECT `nome` FROM `utenti`; 
 
 
" " Virgolette doppie 
 
Hanno un comportamento variabile a seconda delle configurazioni del database. 
 
 
Esportare databases 
 
 
 
mysqldump -u root -p nome_database > backup.sql 
 
# Include la creazione del database stesso 
mysqldump -u root -p --databases nome_database > backup.sql 
 
# Dump di più database 
mysqldump -u root -p --databases db1 db2 db3 > backup.sql 
 
# Dump di tutti i database 
mysqldump -u root -p --all-databases > backup_completo.sql 
 

  7 
 
Importare databases 
mysql -u root -p nome_database < backup.sql 
Se il dump è stato fatto con --databases (include il CREATE DATABASE): 
# Non serve specificare il database, è già nel file 
mysql -u root -p < backup.sql 


---

# Linux Server 08 php

**File:** `Linux Server 08 php.pdf`
**Tipo:** `.pdf`
**Dimensione:** 304.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
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
• Installiamo i moduli del PHP che ci occorrono; 
 
  

  3 
Utilizzando un web server PHP può essere eseguito in tre modalità: CGI, FastCGI o come 
modulo dedicato del web server.  
 
CGI è l’acronimo di Common Gateway Interface; si tratta di uno standard (RFC 3875) 
utilizzato dai web server per interfacciarsi con applicazioni esterne. È stato il primo 
strumento utilizzato per lo sviluppo di applicazioni web in C/C++ o Perl all’inizio degli anni 
’90. Per ogni richiesta del web server su pagine dinamiche, come ad esempio quelle con 
estensione .php, l’interfaccia CGI si preoccupa di eseguire l’interprete del linguaggio e di 
restituire la risposta. Questo approccio consente di avere un isol amento dell’esecuzione del 
codice tra web server e linguaggio interpretato ma rende il sistema inefficiente dal punto di 
vista delle performance, poiché l’interfaccia è riallocata a ogni richiesta HTTP. Ormai questa 
tecnologia non viene più utilizzata nelle moderne applicazioni PHP perché considerata poco 
efficiente in presenza di altro traffico.  
FastCGI è una tecnologia più recente, basata sullo stesso principio di funzionamento del 
CGI, ma con la differenza che la comunicazione tra web server e FastCGI è gestita attraverso 
socket. Un modulo FastCGI rimane in ascolto di eventuali richieste HTTP in memoria e non 
deve essere rieseguito continuamente. Questa soluzione garantisce performance migliori 
rispetto al CGI, soprattutto per applicazioni ad altro traffico. Ad esempio, il web server nginx 
e Internet Information Service (IIS) utilizzano entrambi la modalità FastCGI per 
l’esecuzione di applicazioni PHP.  
Un’altra alternativa per eseguire il codice PHP in ambito web è l’utilizzo di un modulo 
dedicato del web server. Questa modalità è stata, ed è tuttora, molto utilizzata con il web 
server Apache grazie alla sua facilità di installazione e alle sue performance. Utilizzando un 
modulo dedicato, le chiamate agli script PHP vengono gestite direttamente dal web server, 
senza dover utilizzare un livello ulteriore di comunicazione, come nel caso di CGI o 
FastCGI. Apache rimane a tutt’oggi il web server più utilizzat o, con una quota di utilizzo 
intorno al 50%. Nginx sta diventando sempre più popolare, soprattutto nei casi di 
applicazioni web ad altro traffico.  
 
Enrico Zimuel, Sviluppare in PHP 7 
  

  4 
 
Installiamo il PHP 
 
Nginx utilizza il PHP in modalità FastCGI, mentre Apache lo utilizza come modulo. 
 
Infatti per installare il PHP con Nginx si usa il php-fpm (FastCGI Process Manager): 
 
$sudo apt install php php-fpm 
 
Procediamo con l’installazione del PHP_FPM. 
$ sudo systemctl start php8.4-fpm 
 
$ sudo systemctl enable php8.4-fpm 
 
$ sudo systemctl status php8.4-fpm 
  

  5 
Configuriamo nginx 
 
Nel file di configurazione del nostro sito aggiungiamo: 
# pass PHP scripts to FastCGI server 
 
        # 
        location ~ \.php$ { 
        include snippets/fastcgi-php.conf; 
        # 
        #       # With php-fpm (or other unix sockets): 
        fastcgi_pass unix:/var/run/php/php8.4-fpm.sock; 
        #       # With php-cgi (or other tcp sockets): 
 
        # fastcgi_pass 127.0.0.1:9000; 
        } 
 
Aggiungere anche: 
 
        index index.html index.php; 
  

  6 
Solo su macchine di sviluppo, configuriamo il PHP perché si vedano gli errori 
 
 
Dove si trovano i files di configurazione del PHP? 
In  
/etc/php/ 
 
Editiamo il file : 
/etc/php/8.4/fpm/php.ini 
per lo sviluppo 
display_errors = On 
error_reporting = E_ALL 
 
Attenzione! In produzione devono essere: 
display_errors = Off  
error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT 


---

# Linux Server comando at

**File:** `Linux Server comando at.pdf`
**Tipo:** `.pdf`
**Dimensione:** 96.4 KB
**Ultima modifica:** 02/07/2026 09:27

---

 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
 
Il comando at 

 
 
 
Il comando at serve a eseguire un comando o uno script una sola volta in un momento futuro 
specifico, senza che tu debba restare loggato. Si usa quando non vuoi una schedulazione ripetitiva 
come con cron.wikipedia 
Uso base 
La forma tipica è: 
bash 
at ORARIO 
Dopo aver dato il comando, scrivi i comandi da eseguire e poi chiudi con Ctrl+D. at assegna un 
numero di job al task pianificato. 
Esempio: 
bash 
at 09:00 
echo "Ciao" > /tmp/test.txt 
Ctrl+D 
Controllare e rimuovere job 
• atq mostra i job in coda per l’utente corrente. 
atrm <numero_job> rimuove un job pianificato. 
• at -l è un alias comune per elencare i job, e at -r per rimuoverli.  
Formati dell’orario 
Puoi indicare orari semplici come 09:00, oppure parole come now + 1 hour, noon, midnight a seconda 
dell’implementazione e della manpage disponibile. In alcune versioni puoi anche usare il formato 
POSIX con -t. 
Permessi 
L’uso di at può essere controllato da /etc/at.allow e /etc/at.deny: se esiste at.allow, solo gli utenti lì 
elencati possono usarlo. Root può sempre usarlo.man+1 
Quando usarlo 
Usalo per cose come: 
• un backup che deve partire una volta sola. 
• l’invio di un file a una certa ora. 
• una pulizia temporanea o un riavvio programmato. 
 


---

# Linux Server cron

**File:** `Linux Server cron.pdf`
**Tipo:** `.pdf`
**Dimensione:** 202.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

  
 
 
 
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
 
$ tar cvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 
 
Estrazione di un archivio: 
 
$ tar xvf nomeMioArchivio.tar directory1 directory2 dirctory3 file1 file2… 
 
 
Creazione di un archivio compresso - compressore gzip – opzione z : 
 
$ tar czvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 
file2… 
 
Estrazione di un archivio: 
 
$ tar xzvf nomeMioArchivio.tar.gz directory1 directory2 dirctory3 file1 
file2… 
 
 
Creazione di un archivio compresso - compressore bz2 – opzione j: 
 
 
$ tar cjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 
 
Estrazione di un archivio: 
 
$ tar xjvf nomeMioArchivio.tar.bz2 directory1 directory2 dirctory3 file1… 
 
  

 
   3 
 
Temporizzare (“schedulare”) comandi 
 
Ogni utente al proprio crontab che permette di gestire lo scheduling dei programmi 
 
 
 
 
 
https://crontab.guru/ 
 
Es (dopo aver creato una cartella du): 
 
0 7 * * * du -shc --exclude=proc --exclude=run /* > /var/log/du/output-du-$(date '+\%Y-
\%m-\%d').log 
 
  


 
   4 
 
Programmi per il monitoring del sistema 
 
Processi attualmente in uso: 
 
# top 
 
Oppure: 
# htop 
 
Carico della macchina: 
# uptime 
 
Consumo della memoria: 
# vmstat 
O 
# free -m 
 
Utilizzo della CPU e IO: 
# iostat 
 
Processi attivi: 
# ps aux 
Trovare un processo: 
# ps aux | grep nomeProcesso 
 
Albero dei processi: 
# pstree 
 
Uccidere un processo: 
# kill -1234 
Uccidere un processo e i suoi figli: 
# kill -9 1234 
 
Spazio disco: 
# df -h 
 
Dimensione files: 
# du – shc /miaDir 
 
Spazio occupato nel disco: 
 
# du -shc --exclude=proc --exclude=run /*  
 

 
   5 
Quali porte sono utilizzate (installare net-tools): 
 
# netstat -tulp 
 
 


---

# Linux Server esercizi ripasso meta corso

**File:** `Linux Server esercizi ripasso meta corso.pdf`
**Tipo:** `.pdf`
**Dimensione:** 200.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
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
- Con la macchina virtuale spenta, creare un’istantanea (snapshot) della 
macchina; 
Rimozione utenti: 
- Accendere la macchina e cancellare gli utenti non necessari (userdel); 
- Lasciare solo l’utente principale (che si chiamerà its-usr o avrà il nome 
che avete dato voi all’utente). 
 
 
Consegna esercizio 1 
 
(Effettuare queste operazioni utilizzando la shell). 
 
Siete amministratori della macchina dell’azienda acme srl. 
 
- Come amministratore della macchina creare una cartella acme che si 
trovi in home 
- Creare due gruppi: 
dipendenti 
collaboratori 
- All’interno della cartella acme creare due cartelle: 
dipendenti 
collaboratori 
Alla cartella dei collaboratori possono accedere tutti; 
Alla cartella dei dipendenti possono accedere solo i dipendenti. 
 
  

 
3 
 
 
 
 
Davide Rossi nel gennaio 2022 incomincia a lavorare per l’azienda Acme srl. 
 
- Come amministratore della macchina di Davide Rossi creare un utente 
per Davide Rossi; 
- Assegnare Davide al gruppo dipendenti; 
- Davide all’interno della propria home crea una cartella Documenti. 
All’interno della cartella Documenti crea una cartella lavoro. 
All’interno della cartella lavoro, Davide crea una cartella con l’anno e 
poi crea una cartella per ogni mese. 
Si vuole avere la seguente struttura: 
home 
--- davide 
---- Documenti 
--------- lavoro 
------------------ 2022 
------------------------- gennaio 
------------------------- febbraio 
… 
------------------------- dicembre 
------------------ 2023 
------------------------- gennaio 
 
All’interno di ciascuna directory, creare un file che si chiama 
report.txt 
 
- Davide a un certo punto non si ricorda più la sua password. Come 
amministratore di sistema cambiargli la password. 
 
- Verificate che Davide possa entrare in SSH con user name e password. 
 
- Come Davide creare una coppia di chiavi dalla macchina Windows (o 
Mac). 
 
Suggerimento: per evitare di sovrascrivere le chiavi, create una nuova 
cartella in cui immagazzinare le nuove chiavi. 
 

 
4 
 
- Come amministratore di sistema predisponete l’accesso a SSH con 
chiave per Davide e disabilitate l’accesso con password. 
 
Suggerimento: Davide può scegliere una chiave privata  diversa da 
quella di default con cui entrare, usando il comando: 
ssh-add \percorsoWindows\chiave 
 
Nel gennaio 2023 Davide Rossi trova un altro impiego e pertanto lascia la 
Acme srl. 
 
- Prima di cancellare l’utente di Davide, l’amministratore di sistema è 
incaricato di salvare una copia della cartella lavoro nella cartella 
/home/acme/dipendenti. Predisporre una cartella con il lavoro di 
Davide; 
 
- Tale copia deve poter essere consultata in sola lettura e non modificata 
dagli altri utenti; 
 
- L’amministratore di sistema infine cancella l’utenza di Davide. 
 
Nel febbraio 2023 viene assunto l’utente CarloVerdi, che è un collaboratore in 
partita iva dell’azienda. 
 
- Creare l’utente Carlo Verdi; 
- Assegnare l’utente carlo al gruppo collaboratori; 
- Si vuole dare all’utente carlo i permessi di amministratore della 
macchina (dare la possibilità all’utente carlo di diventare 
amministratore con sudo; 
- Accertarsi che l’utente possa accedere in SSH tramite chiave; 
 
Secondo indicazioni della dirigenza, l’utente carlo deve poter modificare i 
files che furono di Davide: 
 
- Lasciare una copia dei files in sola lettura nella cartella dipendenti; 
- Creare una seconda copia dei files in lettura e scrittura nella cartella 
collaboratori, in modo che siano modificabili da carlo e dal gruppo 
collaboratori. 
 
 

 
5 
 
 
 
 
- Utilizzando un client grafico SFTP (SSH File Transfer Protocol), 
caricare dei files all’interno della cartella Documenti di carlo. 
 
 
L’azienda acme vuole creare il proprio sito aziendale. 
Incominciamo a creare l’hostname. 
 
- Creare l’hostname acme e acme.local 
- Verificare che: 
o E’ possibile effettuare il ping su acme.local; 
o E’ possibile entrare un SSH utilizzando il nome host acme.local; 
o Che la pagina di default di nginx risponde sull’host acme.local. 
 


---

# Linux Server esercizi ripasso meta corso2

**File:** `Linux Server esercizi ripasso meta corso2.pdf`
**Tipo:** `.pdf`
**Dimensione:** 281.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
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
- Con la macchina virtuale spenta, creare un’istantanea (snapshot) della 
macchina; 
 
 
Consegna esercizio 2 
 
Federica ha 45 anni e si occupa di programmazione e sistemi in un’azienda. 
Divorziata, si è poi risposata. 
La sua famiglia è composta – oltre che dall’attuale compagno (o marito) - da 
quattro figli: 
Paolo e Pietro di 3 e 6 anni; 
Giovanni e Giacomo di 12 e 14 anni. 
 
All’interno del proprio computer di casa ha creato un media server, in cui 
memorizza i film che acquista o che scarica ( legalmente con regolare utilizzo 
dei DRM). 
 
Il server di casa che utilizza come media server è una piattaforma Linux. 
 
Federica vorrebbe far sì che i figli di 6 e 3 anni abbiano accesso ai contenuti 
riservati ai bambini di 6 anni; e che i figli di 12 e 14 abbiano accesso  ai 
contenuti fino a 18 anni. Infine vorrebbe che lei e l’attuale compagno (che non 
è un utente tecnico e che non avrà un account nel sistema) abbiano accesso a 
tutti i contenuti. 
 
- Creare i seguenti utenti: 
federica, paolo, pietro, giovanni, giacomo 
- Aggiungere federica come sudo user; 
- Creare i seguenti gruppi: 
piccoli, grandi, adulti 
- Assegnare paolo e pietro al gruppo piccoli; 
- Assegnare giovanni e giacomo al gruppo grandi; 

 
3 
 
- Assegnare federica al gruppo adulti; 
- Creare una directory: 
/home/contenuti 
- All’interno della directory /home/contenuti creare due directories: 
piccoli 
grandi 
adulti 
- Fare in modo che: 
o Il gruppo piccoli abbia accesso alla sola cartella piccoli; 
o Il gruppo grandi abbia accesso alla cartella piccoli e alla cartella 
grandi; 
o federica abbia accesso a tutto. 
 
Federica vuol far sì che il figlio giovanni possa caricare i film in SFTP. 
Verificare che giovanni possa entrare sul sever in SFTP e possa 
caricare un file. 
 
Federica vuole inoltre creare un blog per la famiglia. 
Creare l’host 
famiglia.local e famiglia 
e verificare che nginx risponda su quell’host con la pagina di default. 
 
 
 
 
 
 


---

# Linux Server permessi speciali

**File:** `Linux Server permessi speciali.pdf`
**Tipo:** `.pdf`
**Dimensione:** 228.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Permessi speciali 

[Digitare qui] 
 
 
 
1. Sticky Bit 
Lo sticky bit e un permesso speciale in Linux/Unix che si comporta in modo diverso a seconda che 
venga applicato a una directory o a un file eseguibile. 
 
1.1 Applicazione su una directory 
Quando lo sticky bit e impostato su una directory, solo il proprietario del file puo eliminare o 
rinominare i propri file all'interno di quella directory, anche se altri utenti hanno i permessi di 
scrittura sulla directory stessa. 
L'esempio classico e la directory /tmp: 
 
$ ls -ld /tmp 
drwxrwxrwt 10 root root 4096 feb 26 10:00 /tmp 
 
La t finale nei permessi indica che lo sticky bit e attivo. Tutti gli utenti possono scrivere in /tmp, ma 
nessuno puo cancellare i file degli altri. 
 
1.2 Impostare lo sticky bit 
E possibile impostare lo sticky bit con chmod in forma simbolica o numerica (il valore 1 come 
quarto ottetto): 
 
# Con chmod simbolico 
chmod +t /percorso/directory 
 
# Con chmod numerico (il 4° ottetto) 
chmod 1777 /percorso/directory 
 
1.3 Rimuovere lo sticky bit 
 
chmod -t /percorso/directory 
 
1.4 Verifica e simboli 
Per verificare se lo sticky bit e attivo: 
 
ls -ld /percorso/directory 
 
Differenza tra t e T nella visualizzazione dei permessi: 
• t (minuscolo) — sticky bit attivo, bit di esecuzione per others attivo 
• T (maiuscolo) — sticky bit attivo, bit di esecuzione per others NON attivo 

[Digitare qui] 
 
 
1.5 Caso pratico in ambiente server 
Creazione di una directory condivisa tra piu utenti del team in cui ognuno puo scrivere ma non 
cancellare i file altrui: 
 
mkdir /srv/shared 
chmod 1777 /srv/shared 
 
1.6 Nota: comportamento legacy sui file 
Storicamente, lo sticky bit su un file eseguibile indicava al kernel di mantenere l'immagine del 
processo in swap dopo l'esecuzione. Nei sistemi moderni questo comportamento e completamente 
ignorato. 
 
 
2. SUID Bit (Set User ID) 
La s visibile su /usr/bin/passwd e il SUID bit (Set User ID). Quando impostato su un file eseguibile, 
il processo gira con i privilegi del proprietario del file al momento dell'esecuzione, 
indipendentemente da chi lo ha lanciato. 
 
$ ls -l /usr/bin/passwd 
-rwsr-xr-x 1 root root 68208 mag  4  2023 /usr/bin/passwd 
 
La s al posto della x nel gruppo dei permessi del proprietario indica il SUID attivo. 
 
2.1 Perche passwd ne ha bisogno 
Le password degli utenti sono salvate nel file /etc/shadow, accessibile solo da root: 
 
$ ls -l /etc/shadow 
-rw-r----- 1 root shadow 1234 feb 26 10:00 /etc/shadow 
 
Un utente normale non puo scrivere in /etc/shadow. Grazie al SUID, quando viene eseguito 
passwd il processo ottiene temporaneamente i privilegi di root, ma il programma e scritto in modo 
da permettere la modifica solo della propria password. 
 
2.2 Impostare il SUID 
 
# Con chmod simbolico 
chmod u+s /percorso/file 
 
# Con chmod numerico (il valore 4 come quarto ottetto) 
chmod 4755 /percorso/file 

[Digitare qui] 
 
 
2.3 Attenzione: implicazioni di sicurezza 
I file con SUID sono un vettore di attacco comune in ambito di privilege escalation. Un file SUID 
root mal scritto puo essere sfruttato per ottenere privilegi di root non autorizzati. 
E buona pratica monitorare periodicamente quali file hanno il SUID attivo: 
 
find / -perm -4000 -type f 2>/dev/null 
 
 
 
3. Riepilogo dei Bit Speciali 
 
Bit Valore Simbolo Effetto 
SUID 4 s (permessi 
owner) 
Esegue con i privilegi del proprietario del file 
SGID 2 s (permessi 
gruppo) 
Esegue con i privilegi del gruppo proprietario 
Sticky 1 t (permessi 
others) 
Solo il proprietario puo eliminare i propri file 
 
 
4. Nota sul SGID (Set Group ID) 
In modo analogo al SUID, il SGID bit (valore 2) puo essere impostato su file o directory: 
• Su file eseguibili: il processo gira con i privilegi del gruppo proprietario del file 
• Su directory: i nuovi file creati all'interno ereditano il gruppo della directory anziche quello 
del creatore — utile per cartelle condivise di gruppo 
 
# Impostare SGID su una directory 
chmod g+s /percorso/directory 
chmod 2775 /percorso/directory 
 


---

# Linux Server schede di rete

**File:** `Linux Server schede di rete.pdf`
**Tipo:** `.pdf`
**Dimensione:** 165.7 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
  
DOCENTE 
 
Wolfgang Cecchin 
UNITA’ FORMATIVA 
 
Linux Server 
ARGOMENTO 
Impostazione schede di rete 

 
 
Eventualmente fare uno snapshot della macchina virtuale. 
 
La macchina dovrebbe avere già una scheda di rete NAT. 
 
Impostare una seconda scheda di rete “solo host”. 
 
Fare una copia del file interfaces: 
 
$ sudo /etc/network/interfaces /etc/network/interfaces.bk 
 
Modificate il file interfaces: 
 
$ sudo nano /etc/network/interfaces 
 
 
Cambiare il file in modo che contenga queste righe 
(non modificare l’interfaccia di loopback, cioè lo, 
queste righe vanno aggiunte in fondo): 
 
# The primary network interface 
allow-hotplug enp0s3 
iface enp0s3 inet dhcp 
# This is an autoconfigured IPv6 interface 
iface enp0s3 inet6 auto 
 
Spiegazioni: 
 
• allow-hotplug enp0s3: abilita l'interfaccia se detectata (es. USB, PCI hotplug) o all'avvio. Se 
non c'è auto, non parte automaticamente al boot.manpages.debian+1 
 
• iface enp0s3 inet dhcp: IPv4 via DHCP (chiede IP/gateway/DNS al server DHCP, es. 
VirtualBox NAT assegna 10.0.2.15).  
 
• iface enp0s3 inet6 auto: IPv6 automatico (SLAAC/RA, senza indirizzo statico). 
 
 
$ sudo ifdown enp0s3 
$ sudo ifup enp0s3 
 
 


---

# Linux Server tool di diagnostica

**File:** `Linux Server tool di diagnostica.pdf`
**Tipo:** `.pdf`
**Dimensione:** 240.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
 
 
 
  
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
 
• da quanto tempo il sistema e' acceso 
• quanti utenti sono collegati 
• il load average degli ultimi 1, 5 e 15 minuti 
 
$ uptime 
 
 10:32:04 up 14 days, 3:21,  2 users,  load average: 0.12, 0.08, 0.05 
 
Lettura campo per campo: 
 
• 10:32:04 — ora corrente del sistema 
• up 14 days, 3:21 — il sistema e' acceso da 14 giorni, 3 ore e 21 minuti. Il formato e' giorni, 
poi ore:minuti 
• 2 users — numero di sessioni utente aperte (terminali, SSH...) 
• load average: 0.12, 0.08, 0.05 — carico medio nell'ultimo 1 minuto, 5 minuti e 15 minuti 
 
Il load average 
Indica quanti processi sono in attesa di essere eseguiti dalla CPU, mediato nel 
tempo. 
I tre valori rappresentano rispettivamente la media dell'ultimo 1 minuto, 5 minuti e 
15 minuti. 
 
Il valore di riferimento e' il numero di core della CPU: 
 
• load average < numero di core — il sistema e' a riposo, c'e' capacita' libera 
• load average = 1.0 su 1 core — CPU al 100%, situazione limite ma non critica 
• load average > numero di core — ci sono processi che aspettano la CPU: il sistema e' 
sovraccarico 
 
I tre valori vanno letti insieme: un picco solo nel primo (1 min) e' passeggero; se 
anche il terzo (15 min) e' alto, il problema e' strutturale. 
 
Esempio: load average 0.12, 0.08, 0.05 su un sistema a 4 core — tutto tranquillo. 
Esempio: load average 7.50, 6.20, 4.10 su un sistema a 4 core — il sistema e' sotto 
stress. 
 
Quanti core ha il mio sistema? 
 
$ nproc 
 
$ lscpu | grep 'CPU(s)' 
 
Analisi della memoria RAM: free 
Il comando free mostra la memoria totale, usata, libera e la quota di swap. 
L'opzione -h presenta i valori in formato leggibile, scegliendo automaticamente 
l'unita' piu' adatta. 
 
$ free -h 
 

[Digitare qui] 
 
 
              total        used        free      shared  buff/cache   available 
Mem:           15Gi        3,2Gi       9,1Gi      283Mi        3,0Gi       11Gi 
Swap:         2,0Gi          0B        2,0Gi 
 
Cosa significa buff/cache? 
Linux usa la RAM libera come cache disco per migliorare le prestazioni. 
La colonna available e' quella che conta davvero: indica quanta memoria puo' 
essere usata da nuovi processi. 
 
Messaggi del kernel: dmesg 
dmesg mostra i messaggi del kernel dal momento del boot. 
E' il primo strumento da consultare in caso di problemi hardware. 
 
• Rilevamento e inizializzazione dei dispositivi hardware 
• Errori di driver 
• Problemi con dischi e filesystem 
• Messaggi di errore della rete 
 
$ dmesg | tail -50 
 
$ dmesg | grep -i error 
 
$ dmesg | grep -iE "error|fail|warn|critical" 
 
$ dmesg | grep -i sda 
 
$ dmesg | grep -i nvme 
 
L'opzione -T mostra i timestamp in formato leggibile: 
 
$ dmesg -T | grep -i error 
 
Le parole chiave piu' importanti da cercare: 
 
• error, fail — errori generici di dispositivi o driver 
• I/O error, timeout — il disco non risponde o e' lento 
• EXT4-fs error — filesystem corrotto 
• Out of memory — il sistema ha esaurito la RAM 
• Hardware Error — errore segnalato direttamente dall'hardware 
 
Regola pratica: un messaggio che appare una volta puo' essere normale. Se si 
ripete molte volte, c'e' un problema reale. 
 
Log di sistema: journalctl 
journalctl e' il tool per consultare il journal di systemd. 
Raccoglie in modo centralizzato i log di tutti i servizi e del kernel. 
 
Comando Descrizione 
journalctl -xe Ultimi log con contesto esteso (errori recenti) 
journalctl -b Log del boot corrente 
journalctl -b -1 Log del boot precedente 

[Digitare qui] 
 
 
journalctl -b -2 Due boot fa (utile dopo un crash) 
journalctl -u ssh Log di un servizio specifico 
journalctl -f Segue i log in tempo reale (come tail -f) 
journalctl -p err Solo messaggi di errore 
journalctl -p warning Messaggi di warning e superiori 
journalctl --since '1 hour ago' Ultimi 60 minuti 
journalctl --since 'today' Log di oggi 
 
# journalctl -b -1 -p err 
 
Cosa cercare in journalctl: 
 
• failed, error — servizi che non si avviano o vanno in errore 
• un servizio che si ripete in loop — segnale di un crash ripetuto 
• kernel: Hardware Error — errore hardware segnalato dal kernel 
 
Analisi dei dischi 
I dispositivi in /dev/ 
In Linux tutti i dispositivi hardware sono rappresentati come file nella cartella /dev/. 
I dischi non fanno eccezione. 
 
• /dev/hda, /dev/hdb... — dischi IDE (vecchio standard, ormai obsoleto). La lettera indica il 
disco: hda e' il primo, hdb il secondo. 
 
• /dev/sda, /dev/sdb... — dischi SATA, SAS o USB. SATA e' il collegamento standard per 
hard disk e SSD nei PC moderni. SAS e' la versione enterprise, piu' veloce e affidabile, usata nei 
server. La lettera indica il disco: sda e' il primo, sdb il secondo. Le partizioni si indicano con un 
numero: sda1, sda2... 
 
• /dev/nvme0n1, /dev/nvme1n1... — dischi NVMe, collegati direttamente al bus PCIe. Sono 
molto piu' veloci di SATA. Il nome segue il formato nvmeXnY: X e' il numero del controller (0, 1, 2...), 
Y e' il numero del namespace (quasi sempre 1). Le partizioni si indicano con p: nvme0n1p1, 
nvme0n1p2... 
 
Struttura dispositivi: lsblk 
lsblk elenca tutti i dispositivi a blocchi (dischi, partizioni, LVM) con struttura ad 
albero. 
E' il primo comando da usare per conoscere il nome dei dispositivi, che servira' poi 
in df, smartctl e altri strumenti. 
 
$ lsblk 
 
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT 
sda           8:0    0   500G  0 disk 
├─sda1        8:1    0   499G  0 part / 
└─sda2        8:2    0     1G  0 part [SWAP] 
nvme0n1     259:0    0   1,8T  0 disk 
├─nvme0n1p1 259:1    0   512M  0 part /boot/efi 
└─nvme0n1p2 259:2    0   1,8T  0 part /data 

[Digitare qui] 
 
 
 
$ lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE 
 
Spazio sui filesystem: df 
df -h mostra lo spazio usato e libero su ogni filesystem montato. 
 
$ df -h 
 
Filesystem      Size  Used Avail Use% Mounted on 
/dev/sda1        20G   12G  6,8G  64% / 
/dev/sdb1       500G  230G  245G  49% /data 
 
Attenzione alla colonna Use%: sopra il 90% il filesystem e' quasi pieno. 
 
Spazio per directory: du 
$ du -sh /var/log 
 
$ du -h /var | sort -rh | head -20 
 
Mostrare lo spazio occupato da ogni directory di primo livello sotto /: 
 
$ sudo du --max-depth=1 -hx / 
 
L'opzione --max-depth=1 limita la profondita' a un solo livello, senza scendere 
nelle sottodirectory. 
L'opzione -x rimane sullo stesso filesystem, escludendo /proc, /sys, /dev che 
contengono file virtuali del kernel e non dati reali. 
 
Mostrare il totale per ogni directory con somma finale: 
 
$ sudo du -sxhc --exclude=proc * 
 
L'opzione -s mostra solo il totale per ogni argomento. L'opzione -c aggiunge una 
riga finale con il totale complessivo. 
 
Disco pieno — come diagnosticare 
Prima si verifica quale filesystem ha esaurito lo spazio: 
 
$ df -h 
 
Se una riga mostra Use% al 100% (o vicino), quella e' la partizione piena. 
A quel punto si scende nelle directory per trovare il colpevole: 
 
$ sudo du --max-depth=1 -hx / 
 
Si individua la directory piu' grande, poi si scende di un livello: 
 
$ sudo du --max-depth=1 -hx /var 
 
$ sudo du --max-depth=1 -hx /var/log 
 

[Digitare qui] 
 
 
Si continua a scendere finche' non si trova il file o la directory che occupa lo 
spazio inaspettato. 
I soliti sospettati sono: /var/log (log cresciuti troppo), /var/cache, /tmp, /home. 
 
Salute dei dischi: smartctl 
smartctl legge i dati S.M.A.R.T. direttamente dal disco per valutarne lo stato di 
salute. 
Il nome del device da usare si ricava con lsblk. 
Attenzione: il percorso completo /dev/ e' obbligatorio, altrimenti il sistema non 
trova il dispositivo. 
 
# apt install smartmontools 
 
# smartctl -H /dev/sda 
 
# smartctl -H /dev/nvme0n1 
 
Se il risultato e' PASSED: il disco e' sano. 
Se il risultato e' FAILED: fare subito un backup! Il disco puo' smettere di funzionare in 
qualsiasi momento. 
 
Dopo un FAILED, per capire qual e' il problema ispezionare tutti gli attributi: 
 
# smartctl -a /dev/sda 
 
Cercare nella colonna WHEN_FAILED i valori FAILING_NOW o In_the_past. 
Gli attributi piu' importanti da controllare: 
 
Attributo SMART Significato 
Reallocated_Sector_Ct Settori danneggiati rimappati. Idealmente 0 
Current_Pending_Sector Settori instabili in attesa di rimappatura 
Uncorrectable_Sector Errori non correggibili. Se > 0 il disco e' a rischio 
Power_On_Hours Ore totali di utilizzo del disco 
Temperature_Celsius Temperatura attuale del disco 
 
Memoria RAM danneggiata 
Con un settore di RAM danneggiato, free -h di solito non mostra nulla di anomalo. 
Il kernel esclude automaticamente le pagine difettose durante il boot — la RAM 
totale mostrata puo' essere leggermente inferiore a quella installata fisicamente, 
ma non appare un errore esplicito. 
 
I sintomi reali di RAM danneggiata sono: 
 
• crash casuali e imprevedibili del sistema, spesso senza un pattern chiaro 
• kernel panic — il sistema si blocca con un messaggio di errore e si riavvia o si spegne 
• processi che terminano in modo anomalo con errori di segmentation fault 
• dati corrotti in modo apparentemente casuale 
 

[Digitare qui] 
 
 
In casi gravi il server si spegne improvvisamente perche' il kernel scrive dati in una 
zona di memoria corrotta e il risultato e' imprevedibile. 
 
Per diagnosticare RAM difettosa il tool dedicato e' memtest86+, che gira fuori dal 
sistema operativo, dal menu di GRUB, e testa tutta la RAM in modo sistematico. 
 
Riepilogo degli strumenti 
 
Comando Categoria Cosa fa 
uptime Sistema Carico, uptime, load average 
free -h Memoria RAM e swap usata/libera 
dmesg Kernel Messaggi hardware dal boot 
journalctl Log Log centralizzati di tutto il sistema 
lsblk Disco Struttura dischi, partizioni e nomi dei device 
df -h Disco Spazio usato su ogni filesystem 
du -sh Disco Spazio occupato da una directory 
du --max-depth=1 -hx Disco Spazio per directory di primo livello, stesso 
filesystem 
smartctl -H Disco Salute S.M.A.R.T. del disco 
smartctl -a Disco Dettaglio completo degli attributi S.M.A.R.T. 
memtest86+ Memoria Test della RAM (si avvia da GRUB, fuori dal 
sistema operativo) 
 
 
Esercizio 
1. Verificare il carico del sistema con uptime. 
   Quanti core ha la VM? Il load average e' alto o basso rispetto al numero di core? 
 
2. Con free -h verificare quanta RAM e' disponibile. 
   Quanto usa il sistema al minimo? Quanto c'e' in buff/cache? 
 
3. Con dmesg | grep -iE "error|fail|warn" cercare problemi hardware. 
   Con journalctl -b -p err cercare errori nel boot corrente. 
 
4. Con lsblk identificare i dischi presenti nella VM e i loro nomi. 
   Quali partizioni ci sono? Dove sono montate? 
 
5. Con df -h trovare il filesystem piu' pieno. 
   Con du -sh /* trovare le directory piu' grandi. 
 
6. Installare smartmontools e verificare la salute del disco della VM. 
   Usare il nome del device trovato con lsblk. 
 


---

# networking linux doc

**File:** `networking linux doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3934.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

Networking in Linux — ITS Academy 
 
Networking in Linux 
Lezione — Linux Server | ITS Academy 
1. Introduzione 
La configurazione di rete è una competenza fondamentale per chi amministra un server 
Linux. In questa lezione vedremo come funziona lo stack di rete, come configurare 
interfacce, routing e risoluzione dei nomi, e come diagnosticare problemi di connettività. 
2. Concetti fondamentali 
Interfacce di rete 
Un'interfaccia di rete è il punto di contatto tra il sistema operativo e la rete fisica (o virtuale). 
In Linux le interfacce seguono una nomenclatura predittiva (introdotta con systemd/udev): 
 
Nome Tipo 
eth0, enp3s0, ens33 Ethernet fisica 
wlan0, wlp2s0 Wireless 
lo Loopback (127.0.0.1) 
virbr0, docker0 Bridge virtuali 
 
Il loopback è un'interfaccia speciale: tutto il traffico inviato a 127.0.0.1 rimane all'interno della 
macchina stessa. È usato da servizi che comunicano localmente (es. PHP → MySQL). 
Il modello TCP/IP a strati 
Strato Protocolli 
Applicazione HTTP, FTP, SSH, DNS 
Trasporto TCP (affidabile), UDP (veloce) 
Rete IP, ICMP, routing 
Collegamento Ethernet, ARP, MAC address 
 
3. Comandi essenziali 

Networking in Linux — ITS Academy 
Comando ip — visualizzare le interfacce 
Il comando ip sostituisce il vecchio ifconfig ed è lo strumento principale per la gestione della 
rete in Linux moderno. 
ip addr show           # mostra tutte le interfacce 
ip addr show enp3s0    # mostra solo una interfaccia 
ip addr add 192.168.1.100/24 dev enp3s0   # assegna IP temporaneo  
ip addr del 192.168.1.100/24 dev enp3s0   # rimuove un IP 
ip link set enp3s0 up  # attiva interfaccia 
ip link set enp3s0 down  # disattiva interfaccia 
Routing 
Il routing determina come i pacchetti raggiungono la destinazione. La tabella di routing dice 
al kernel quale gateway usare per raggiungere una determinata rete. 
ip route show           # mostra la tabella di routing 
ip route add default via 192.168.1.1        # default gateway  
ip route add 10.0.0.0/8 via 192.168.1.254  # rotta statica 
ip route del default via 192.168.1.1        # elimina rotta 
     Tutte le modifiche con ip sono temporanee: vengono perse al riavvio del sistema. 
4. Configurazione persistente 
Debian — /etc/network/interfaces 
auto enp3s0 
iface enp3s0 inet static 
    address 192.168.1.100 
    netmask 255.255.255.0 
    gateway 192.168.1.1 
    dns-nameservers 8.8.8.8 1.1.1.1 
Per applicare: 
systemctl restart networking 
Ubuntu moderno — Netplan (/etc/netplan/*.yaml) 
network: 
  version: 2 
  ethernets: 
    enp3s0: 
      addresses: [192.168.1.100/24] 
      routes: 
        - to: default 
          via: 192.168.1.1 
      nameservers: 
        addresses: [8.8.8.8, 1.1.1.1] 
Per applicare: 
netplan apply 
Best practice: come per MariaDB, preferire i file dedicati nelle directory .d/ invece di 
modificare i file di configurazione base. 

Networking in Linux — ITS Academy 
5. Risoluzione dei nomi (DNS) 
Quando si esegue ping google.com il sistema deve tradurre il nome in un indirizzo IP. 
Questo processo si chiama risoluzione DNS. 
Ordine di risoluzione — /etc/nsswitch.conf 
hosts: files dns 
Il sistema controlla prima /etc/hosts, poi interroga il server DNS configurato. 
/etc/hosts — mappature statiche 
127.0.0.1    localhost 
192.168.1.10 server-web.lan server-web 
192.168.1.20 db.lan 
Utile in laboratorio per simulare un DNS senza installarne uno. 
/etc/resolv.conf — server DNS 
nameserver 8.8.8.8 
nameserver 1.1.1.1 
search lan 
Attenzione: su sistemi con systemd-resolved, questo file è un symlink gestito 
automaticamente. 
6. Diagnostica di rete 
La sequenza logica per diagnosticare un problema di connettività parte sempre dal livello più 
basso: 
• Passo 1 — L'interfaccia è attiva? 
ip addr show    # verificare la presenza di UP e di un indirizzo IP  
• Passo 2 — Raggiungo il gateway? 
ping -c 4 192.168.1.1 
• Passo 3 — Raggiungo Internet per IP? 
ping -c 4 8.8.8.8 
• Passo 4 — Il DNS funziona? 
ping -c 4 google.com 
nslookup google.com 
dig google.com 
Altri strumenti 
Comando Utilizzo 
traceroute google.com Traccia il percorso dei pacchetti 
ss -tuln Connessioni attive e porte in ascolto 
ss -tulnp Come sopra + nome del processo 
tcpdump -i enp3s0 Cattura traffico su un'interfaccia 
tcpdump -i enp3s0 port 80 Cattura solo traffico sulla porta 80 
 

Networking in Linux — ITS Academy 
7. Porte e servizi 
Ogni servizio di rete ascolta su una porta. Le porte fino a 1023 sono privilegiate e richiedono 
i permessi di root. 
Porta Protocollo Servizio 
22 TCP SSH 
25 TCP SMTP 
53 TCP/UDP DNS 
80 TCP HTTP 
443 TCP HTTPS 
3306 TCP MySQL/MariaDB 
5432 TCP PostgreSQL 
 
ss -tulnp    # mostra porte in ascolto con nome del processo 
8. Esercizio pratico — Studio Fotografico Bianchi 
Il server Linux dello studio ha due interfacce di rete: 
• enp3s0 — collegata alla LAN interna (192.168.10.0/24) 
• enp4s0 — collegata al provider Internet (IP via DHCP) 
 
Obiettivi: 
• Assegnare a enp3s0 l'IP statico 192.168.10.1/24 in modo persistente 
• Aggiungere in /etc/hosts le voci per i client della LAN 
• Verificare la connettività verso i client con ping 
• Verificare le porte in ascolto con ss -tulnp 
• Usare traceroute per analizzare il percorso verso 8.8.8.8 
 
Domande di riflessione: 
• Perché è importante configurare l'IP in modo persistente? 
• Cosa succede se il gateway predefinito non è configurato correttamente? 
• Qual è la differenza pratica tra /etc/hosts e un server DNS? 
9. Riepilogo 
Concetto Comando / File chiave 
Visualizzare interfacce ip addr show 
Configurare IP (temporaneo) ip addr add IP/MASK dev IF 
Visualizzare routing ip route show 
Configurazione persistente /etc/network/interfaces o Netplan 
Risoluzione locale /etc/hosts 

Networking in Linux — ITS Academy 
Server DNS /etc/resolv.conf 
Diagnostica connettività ping, traceroute, ss 
Cattura traffico tcpdump 
 


---

# networking linux

**File:** `networking linux.pdf`
**Tipo:** `.pdf`
**Dimensione:** 445.1 KB
**Ultima modifica:** 02/07/2026 09:22

---

DOCENTE Wolfgang Cecchin
UNITA’ FORMATIVA Linux Server
ARGOMENTO Networking

Networking
in Linux
Configurazione, diagnostica e gestione della rete
Linux Server  |  ITS Academy

Agenda
Networking in Linux — ITS Academy
• 1.  Concetti fondamentali — stack TCP/IP e interfacce
• 2.  Il comando ip — visualizzare e configurare
• 3.  Routing e tabella di instradamento
• 4.  Configurazione persistente — interfaces e Netplan
• 5.  Risoluzione dei nomi — DNS, /etc/hosts, /etc/resolv.conf
• 6.  Diagnostica — ping, traceroute, ss, tcpdump
• 7.  Porte e servizi comuni
• 8.  Esercizio pratico — Studio Fotografico Bianchi

2. Concetti fondamentali — Stack TCP/IP
Networking in Linux — ITS Academy
Applicazione HTTP · FTP · SSH · DNS
Trasporto TCP (affidabile) · UDP (veloce)
Rete IP · ICMP · Routing
Collegamento Ethernet · ARP · MAC

Interfacce di rete — nomenclatura predittiva
Networking in Linux — ITS Academy
eth0 / enp3s0
Ethernet fisica
wlan0 / wlp2s0
Wireless
lo
Loopback — 127.0.0.1 (locale)
virbr0 / docker0
Bridge virtuale
⚑ Il loopback è usato da servizi che comunicano localmente — es. PHP → MySQL (127.0.0.1:3306)

3. Il comando ip — operazioni principali
Networking in Linux — ITS Academy
Sostituisce il vecchio ifconfig — strumento principale in Linux moderno
Visualizzare
ip addr show
ip addr show enp3s0
ip route show
ip link show
Modificare (temporaneo)
ip addr add 192.168.1.10/24 dev enp3s0
ip addr del 192.168.1.10/24 dev enp3s0
ip link set enp3s0 up
ip link set enp3s0 down
Routing
ip route add default via 192.168.1.1
ip route add 10.0.0.0/8 via 192.168.1.254
ip route del default via 192.168.1.1
Tutte le modifiche con ip sono temporanee — perse al riavvio!

4. Configurazione persistente
Networking in Linux — ITS Academy
Debian — /etc/network/interfaces
auto enp3s0
iface enp3s0 inet static
address 192.168.1.100
netmask 255.255.255.0
gateway 192.168.1.1
dns-nameservers 8.8.8.8
systemctl restart networking
Ubuntu — Netplan /etc/netplan/*.yaml
network:
version: 2
ethernets:
enp3s0:
addresses: [192.168.1.100/24]
routes:
- to: default
via: 192.168.1.1
netplan apply
Best practice: usare file dedicati nelle directory .d/ — non modificare i file di configurazione base (come per MariaDB)

5. Risoluzione dei nomi (DNS)
Networking in Linux — ITS Academy
Applicazione
(ping google.com) →
/etc/nsswitch.conf
ordine: files → dns →
/etc/hosts
mappature locali →
Server DNS
/etc/resolv.conf
/etc/hosts
127.0.0.1     localhost
192.168.1.10  server-web.lan
192.168.1.20  db.lan
/etc/resolv.conf
nameserver 8.8.8.8
nameserver 1.1.1.1
search lan
Con systemd-resolved: /etc/resolv.conf è un symlink gestito automaticamente — modificarlo direttamente potrebbe non avere effetto.

6. Diagnostica di rete — sequenza logica
Networking in Linux — ITS Academy
1 Interfaccia attiva? ip addr show
2 Raggiungo il gateway? ping -c 4 192.168.1.1
3 Internet raggiungibile (per IP)? ping -c 4 8.8.8.8
4 DNS funziona? dig google.com  /  nslookup google.com
Altri strumenti: traceroute / tracepath   |   ss -tuln / ss -tulnp   |   tcpdump -i enp3s0

7. Porte e servizi comuni
Networking in Linux — ITS Academy
ss -tulnp   # mostra porte in ascolto con nome del processo
Porta Protocollo Servizio
22 TCP SSH
25 TCP SMTP
53 TCP/UDP DNS
80 TCP HTTP
443 TCP HTTPS
3306 TCP MySQL / MariaDB
5432 TCP PostgreSQL

8. Esercizio pratico — Studio Fotografico Bianchi
Networking in Linux — ITS Academy
Scenario:
Il server Linux dello studio ha due interfacce: enp3s0 (LAN 192.168.10.0/24) e enp4s0 (Internet via DHCP)
Obiettivi:
• Assegnare a enp3s0 l'IP statico 192.168.10.1/24 in modo 
persistente
• Aggiungere in /etc/hosts le voci per i client della LAN
• Verificare la connettività con ping verso i client
• Verificare le porte in ascolto con ss -tulnp
• Usare traceroute per analizzare il percorso verso 8.8.8.8
Domande di riflessione:
• Perché è importante configurare l'IP in modo 
persistente?
• Cosa succede se il gateway predefinito non è 
configurato correttamente?
• Qual è la differenza pratica tra /etc/hosts e un 
server DNS?

Riepilogo
Visualizzare interfacce ip addr show
Configurare IP (temp.) ip addr add IP/MASK dev IF
Tabella di routing ip route show
Conf. persistente Debian /etc/network/interfaces
Conf. persistente Ubuntu /etc/netplan/*.yaml
Risoluzione locale /etc/hosts
Server DNS /etc/resolv.conf
Porte in ascolto ss -tuln / ss -tulnp
Cattura traffico tcpdump -i enp3s0


---

# panoramica guasti

**File:** `panoramica guasti.pdf`
**Tipo:** `.pdf`
**Dimensione:** 42.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

Panoramica dei guastiCausaGuastoLivelloMacchina# 10.0.0.11 → 10.0.0.1IP rete interna erratoRetedebian31 No regola porta 80HTTP bloccatoFirewalldebian32 /var/www/html → /wordpressnginx root sbagliataServiziodebian33 server_name + wp_optionsNome sito erratoApplicazionedebian34 enp0s8 DOWNInterfaccia spentaRetedebian45 No regola porta 3306MariaDB bloccatoFirewalldebian46 127.0.0.1 → 10.0.0.2bind-address erratoServiziodebian47


---

# Passaggi Ripasso Finale CSP

**File:** `Passaggi Ripasso Finale CSP.pdf`
**Tipo:** `.pdf`
**Dimensione:** 115.5 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte  ·  Linux Server PASSAGGI — StudioFoto Arcobaleno 
Pag. 1 
 
ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 
PASSAGGI 
Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 
Guida operativa passo-passo 
Durata: 2 ore  ·  Valutazione: 16 punti (1 per punto) — sufficienza a 10 
  

ITS ICT Piemonte  ·  Linux Server PASSAGGI — StudioFoto Arcobaleno 
Pag. 2 
Nota — Questa guida elenca la sequenza ordinata delle operazioni da svolgere, parte 
per parte. Indica il “come” procedurale; la sintassi esatta dei comandi e gli output sono 
nel documento Soluzione. 
 
Parte 1 — Utenti, gruppi e permessi  (~25 min) 
1. Imposta l'hostname con il comando dedicato di systemd, poi rileggilo per 
confermare che sia persistente. 
2. Crea il gruppo di lavoro, quindi crea i due utenti aggiungendoli al gruppo al 
momento della creazione (home + shell bash). 
3. Imposta una password per ciascun utente e verifica l'appartenenza ai gruppi. 
4. Crea la directory condivisa e assegnala al gruppo fotografi. 
5. Applica i permessi con i due bit speciali: SGID (eredità del gruppo) e Sticky bit 
(cancellazione solo dei propri file). 
6. Verifica i permessi risultanti con un listing della directory. 
Parte 2 — Rete  (~15 min) 
1. Apri il file di configurazione delle interfacce di Debian 
(/etc/network/interfaces). 
2. Lascia l'interfaccia NAT in DHCP; configura l'interfaccia Solo Host come statica 
con indirizzo e netmask richiesti. 
3. Riavvia il servizio di rete e verifica l'indirizzo assegnato. 
4. Aggiungi la riga di mappatura nome→IP nel file degli host. 
5. Verifica la risoluzione del nome con getent o ping. 
Parte 3 — Accesso remoto SSH  (~15 min) 
1. Sul client genera una coppia di chiavi (preferibilmente ed25519). 
2. Copia la chiave pubblica sul server nell'account its-usr (ssh-copy-id). 
3. Verifica l'accesso con chiave prima di disabilitare la password. 
4. Modifica sshd_config: nega il login di root e disattiva l'autenticazione via 
password (assicurandoti che la chiave pubblica sia abilitata). 
5. Controlla la sintassi della configurazione, ricarica il servizio e verificane lo stato. 
Parte 4 — Web server nginx + PHP  (~20 min) 
1. Aggiorna l'indice dei pacchetti e installa nginx insieme a php-fpm (mai il 
metapacchetto php, che trascinerebbe Apache). 
2. Crea la document root e la pagina info.php con la chiamata a phpinfo(). 
3. Crea un file di virtual host in sites-available con root, server_name e il blocco 
location per i file .php verso il socket di PHP-FPM. 
4. Abilita il sito con un link simbolico in sites-enabled. 
5. Controlla la sintassi di nginx, ricarica il servizio e verifica con curl che la pagina 
venga interpretata (HTML), non restituita come sorgente PHP. 

ITS ICT Piemonte  ·  Linux Server PASSAGGI — StudioFoto Arcobaleno 
Pag. 3 
Parte 5 — Database MariaDB  (~15 min) 
1. Installa il pacchetto server di MariaDB. 
2. Esegui lo script di hardening iniziale (password root, rimozione utenti anonimi e 
db di test). 
3. Entra nella console come amministratore e crea il database applicativo. 
4. Crea l'utente applicativo e assegnagli i privilegi solo sul database 
arcobaleno_db; ricarica i privilegi. 
5. Verifica effettuando il login con il nuovo utente e controllando i database 
visibili. 
Parte 6 — Processi e servizi  (~10 min) 
1. Abilita all'avvio e avvia i tre servizi in un solo comando, poi verifica che siano 
enabled e active. 
2. Lancia il processo sleep in background. 
3. Individua il PID con jobs oppure con ps. 
4. Termina il processo con il segnale standard (SIGTERM); ricorri a SIGKILL solo se 
non risponde. 
Parte 7 — Automazione (cron) e firewall (iptables)  (~15 min) 
1. Scrivi lo script: variabili per sorgente/destinazione, data nel nome dell'archivio 
(date +%F), creazione dell'archivio compresso con tar. 
2. Rendi lo script eseguibile e pianificalo nel crontab alle 02:30. 
3. Installa iptables e iptables-persistent. 
4. Inserisci PRIMA le regole di ACCEPT (loopback, connessioni stabilite, SSH, HTTP) 
e SOLO DOPO imposta la policy INPUT su DROP, per non perdere la sessione 
SSH in corso. 
5. Salva le regole per renderle persistenti al riavvio e verifica con un listing. 
Parte 8 — Diagnostica  (~5 min) 
1. Parti dal livello più basso e sali: prima la connettività di rete, poi il filtraggio del 
firewall, poi lo stato del servizio, infine l'applicazione. 
2. Per ogni livello esegui un controllo mirato e procedi al livello superiore solo 
quando quello inferiore è confermato funzionante. 


---

# presentazione grep sed find

**File:** `presentazione grep sed find.pdf`
**Tipo:** `.pdf`
**Dimensione:** 425.2 KB
**Ultima modifica:** 02/07/2026 09:27

---

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
Ricerca e manipolazione di file e testo in Linux
grep
Cerca nei file
sed
Modifica il testo
find
Cerca nel filesystem

In questa lezione
grep
• Cerca righe che contengono un 
pattern
• Opzioni: -i -r -n -v -l -c -E
• Ancore: ^ $ e regex estese
• Non modifica mai i file
sed
• Modifica il testo riga per riga
• Comando s/vecchio/nuovo/g
• Eliminare righe con /pattern/d
• Modifica in-place con -i
find
• Cerca per nome, tipo, proprietario
• Filtra per dimensione e data
• Permessi: tre formati di -perm
• Esegue azioni con -exec

grep — Cercare nei file
Sintassi
$ grep [opzioni] "pattern" file
Non modifica mai i file — solo cerca e mostra.
Opzioni principali
-i Case-insensitive (MAIUSCOLE = minuscole)
-r Ricorsiva nelle sottodirectory
-n Mostra il numero di riga
-v Inverte: righe che NON corrispondono
-l Solo nomi file con corrispondenze
-c Conta le righe corrispondenti
-E Abilita regex estese (ERE)
-o Stampa solo la parte corrispondente
Ancore nelle espressioni regolari
^
Riga che inizia con root
grep "^root"
$
Riga che finisce con bash
grep "bash$"
.
Qualsiasi carattere singolo
grep "er.ore"
|
OR logico (richiede -E)
grep -E "err|warn"

grep — Esempi pratici
Trova ERROR nel log
$ grep "ERROR" sistema.log
Cerca ERROR o WARNING (OR)
$ grep -E "ERROR|WARNING" sistema.log
Con numero di riga, case-insensitive
$ grep -ni "error" sistema.log
Righe che NON sono commenti
$ grep -v "^#" webserver.conf
Righe non vuote e non commentate
$ grep -v "^#" webserver.conf | grep -v "^$"
Conta i login falliti
$ grep -c "Failed password" sistema.log
File che contengono password (ricorsivo)
$ grep -rl "password" /etc/
Estrai tutti gli IP dal log
$ grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" sistema.log

sed — Modificare il testo
Sintassi
$ sed [opzioni] 'comando' file
Il comando di sostituzione  s/vecchio/nuovo/flag
$ sed 's/vecchio/nuovo/flag' file
(nessuno)
Sostituisce la prima occorrenza per riga
g
Tutte le occorrenze nella riga (global)
i
Case-insensitive
2
Solo la seconda occorrenza
Opzione  -i  (in-place)
Senza  -i  → output su stdout, file intatto
$ sed 's/old/new/' file.txt
Con  -i  → modifica diretta del file
$ sed -i 's/old/new/g' file.txt
ATTENZIONE: -i  modifica il file in modo irreversibile. Prima di usarla, verificare il risultato senza  -i.  Per creare una copia di backup automatica: sed -
i.bak 's/old/new/g' file

sed — Esempi pratici e workflow consigliato
Sostituire WARNING con ERROR (solo output)
$ sed 's/WARNING/ERROR/' webserver.conf
Tutte le occorrenze nella riga (flag g)
$ sed 's/server01/webserver.lan/g' sistema.log > 
mod.log
Eliminare le righe di commento dall'output
$ sed '/^#/d' webserver.conf
Eliminare le righe vuote
$ sed '/^$/d' file.txt
Mostrare solo le righe 1-10
$ sed -n '1,10p' sistema.log
Modifica in-place con backup
$ sed -i.bak 's/vecchio/nuovo/g' file.txt
Workflow consigliato: grep → sed
$ grep "old" file          # 1. verifico cosa troverò
$ sed 's/old/new/' file   # 2. controllo l'output senza -i
$ sed -i 's/old/new/' file # 3. applico la modifica

find — Cercare nel filesystem
Sintassi
$ find [percorso] [criteri] [azione]
-name "*.conf"
Nome (glob, case-sensitive)
-iname "hosts"
Nome case-insensitive
-type f / d / l
File, directory, link simbolico
-user mario
Proprietario dell'utente
-size +100M
Dimensione > 100 MiB
-mtime -1
Modificato nelle ultime 24 h
Esempi
$ find / -name "hosts" 2>/dev/null
$ find /var/log -type f -name "*.log"
$ find /home -type d -name "backup"
$ find /etc -mtime -1

find — Permessi: i tre formati di -perm
-perm NNNN
find . -perm 755
Corrispondenza esatta
Il file deve avere esattamente quei permessi e nessun altro. Raramente usato in pratica.
-perm -NNNN
find . -perm -111
Tutti i bit presenti
Tutti i bit indicati devono essere attivi, ma il file può averne anche altri.
-perm /NNNN
find . -perm /4000
Almeno un bit presente
Basta che sia attivo almeno uno dei bit indicati (OR logico). Il più usato per i permessi speciali.
Il formato  /NNNN  è quello più usato per cercare permessi speciali (SUID, SGID, Sticky bit).

find — Permessi speciali: SUID, SGID, Sticky bit
SUID 4000 Il file eseguibile viene eseguito con i permessi del proprietario (es. passwd → root).
SGID 2000 Su file: esegue con i permessi del gruppo. Su directory: i file creati ereditano il gruppo.
Sticky 1000 Su directory (es. /tmp): solo il proprietario può eliminare i propri file.
Esempi pratici
File con SUID (eseguiti come root)
$ find / -perm /4000 -type f 2>/dev/null
File con SGID
$ find / -perm /2000 -type f 2>/dev/null
Directory con sticky bit
$ find / -type d -perm /1000 2>/dev/null
Qualsiasi permesso speciale attivo
$ find / -perm /7000 2>/dev/null
Eseguibili da tutti (user + group + others)
$ find . -perm -111
Scrivibili da others (rischio sicurezza)
$ find /home -perm -002 -type f

find — Azioni: -exec, xargs e 2>/dev/null
-exec — eseguire un comando su ogni file trovato
$ find [percorso] [criteri] -exec comando {} \;
{} Segnaposto sostituito dal percorso di ogni file trovato \; Termina -exec. Il \ impedisce alla shell di interpretare il ;
Copiare i file di mario in /root/backup_mario/
$ find / -user mario -type f -exec cp {} /root/backup_mario/ \;
Listare i file SUID con dettagli
$ find / -perm /4000 -type f -exec ls -lh {} \; 2>/dev/null
Pipeline con xargs — alternativa più efficiente
$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1"
$ find /etc/ -type f -print0 | xargs -0 grep "pattern"  # nomi con spazi
2>/dev/null  scarta i messaggi "Permission denied" (stderr). Da aggiungere sempre con find / o su directory di sistema.

Riepilogo — Cheat Sheet
grep
grep "pat" file               → cerca pat nel file
grep -i "pat" file            → case-insensitive
grep -r "pat" dir/            → ricorsivo
grep -v "pat" file            → righe che NON corrispondono
grep -E "err|warn" file       → OR logico
grep -c "pat" file            → conta le righe
sed
sed 's/old/new/' file         → sostituzione (prima occ.)
sed 's/old/new/g' file        → sostituzione (tutte)
sed -i 's/old/new/g' file     → modifica in-place
sed '/^#/d' file              → elimina commenti
sed '/^$/d' file              → elimina righe vuote
sed -n '1,10p' file           → mostra righe 1-10
find
find / -name "file" 2>/dev/null   → cerca per nome
find / -type f -size +100M         → file > 100 MiB
find / -user mario -type f         → file di mario
find / -perm /4000 -type f         → file con SUID
find / -perm /7000 2>/dev/null     → tutti i perm. speciali
find /etc -exec grep -l "pat" {} \; → -exec

Esercizi
grep
• Mostrare le righe di sistema.log che 
contengono ERROR
• Cercare ERROR o WARNING con -E
• Contare i "Failed password" nel log
• Mostrare gli utenti con shell /bin/bash da 
utenti.txt
• Righe non vuote e non commentate da 
webserver.conf
sed
• Sostituire WARNING con ERROR solo a 
video
• Eliminare le righe di commento 
dall'output
• Sostituire server01 con webserver.lan → 
sistema_mod.log
find
• Cercare resolv.conf nel filesystem (con 
2>/dev/null)
• Trovare file SUID nel sistema
• Copiare i file di mario in 
/root/backup_mario/
• Trovare file > 100 MiB nel filesystem


---

# risoluzione problema rete Debian

**File:** `risoluzione problema rete Debian.txt`
**Tipo:** `.txt`
**Dimensione:** 0.4 KB
**Ultima modifica:** 02/07/2026 09:22

---

# risoluzione problema rete Debian 3
# tira su l'interfaccia a mano con l'IP tipico di VirtualBox NAT:

sudo ip link set enp0s3 up
sudo ip addr add 10.0.2.15/24 dev enp0s3
sudo ip route add default via 10.0.2.2
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

# verifica:

ping -c 2 8.8.8.8

# risoluzione permanente (basta reinstallare il client dhcp):
sudo apt install isc-dhcp-client -y

sudo systemctl restart networking



---

# shell avanzata doc

**File:** `shell avanzata doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 252.8 KB
**Ultima modifica:** 02/07/2026 09:22

---

 
 
  
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
In Linux, tutto è un file: file di testo, directory, dispositivi hardware, socket di rete, la tastiera, 
lo schermo. Il kernel gestisce tutto tramite la stessa astrazione. 
Quando un processo vuole comunicare con qualcosa — leggere dalla tastiera, scrivere sullo 
schermo, aprire un file — non lo fa direttamente. Chiede al kernel di aprire un canale, e il 
kernel gli restituisce un numero intero che rappresenta quel canale. Quel numero è il file 
descriptor (fd). 
Puoi immaginarlo come il numero di un tavolo al ristorante: il cameriere (kernel) sa a quale 
tavolo portare il cibo, tu (il processo) usi solo il numero — non ti preoccupi di dove si trova 
fisicamente il tavolo. 
 
 
processo → "voglio scrivere sul canale 1" → kernel → schermo 
processo → "voglio scrivere sul canale 1" → kernel → file.txt   ← dopo 
reindirizzamento 
 
Il processo scrive sempre sullo stesso numero. È il kernel che decide dove quel numero 
punta davvero. 
I tre canali aperti automaticamente 
Ogni processo, nel momento in cui viene avviato, riceve già tre file descriptor aperti, ereditati 
dalla shell: 
 
FD Nome Direzione Collegato a (default) 
0 stdin ingresso tastiera 
1 stdout uscita terminale 
2 stderr uscita errori terminale 
 
stdout e stderr puntano entrambi al terminale, ma sono canali separati. Questo è 
fondamentale: permette di mandare l'output normale da una parte e gli errori da un'altra, 
senza mescolarli. 
Perché si chiama "descriptor" e non "file" 
Il file descriptor non è il file — è solo un indice nella tabella dei file aperti del processo. Ogni 
processo ha la propria tabella. Modificare dove punta l'fd 1 di un processo non cambia nulla 
per gli altri processi. 

 
 
Il reindirizzamento (>, 2>, &>) non fa altro che cambiare la destinazione di questi indici prima 
che il processo parta. Il processo non sa nulla di questo: continua a scrivere su 1 e 2 come 
sempre. 
Reindirizzamento di stdout (1) 
 
# Salva l'elenco dei file di configurazione su file 
ls -l /etc > elenco.txt 
 
# Aggiunge in coda invece di sovrascrivere 
ls -l /var/www >> elenco.txt 
 
# Equivalente esplicito con fd 1 
ls -l /etc 1> elenco.txt 
 
# Caso pratico: salvare il risultato di una query MySQL su file 
mysql -u root -p fotodb -e "SELECT * FROM clienti;" > clienti.txt 
 
Reindirizzamento di stderr (2) 
 
# find genera errori su directory senza permessi — li separiamo 
find / -name "*.conf" > risultati.txt 2> errori.log 
 
# Cerca file PHP ignorando silenziosamente le directory protette 
find /var/www -name "*.php" 2> /dev/null 
 
# grep: solo i match su stdout, eventuali errori su file separato 
grep -r "password" /etc 2> /tmp/grep_errori.log 
 
Reindirizzare entrambi con 2>&1 
La sintassi si legge pezzo per pezzo: 
 
 
2  >  &1 
^  ^  ^^ 
│  │  │└─ il numero del file descriptor 1 (stdout) 
│  │  └── & significa "questo è un fd, non un nome file" 
│  └───── operatore di reindirizzamento 
└──────── il file descriptor 2 (stderr) 
 
Traduzione letterale: "punta fd 2 verso lo stesso posto dove punta fd 1". 
Il & davanti all'1 è necessario per disambiguare: senza, 2>1 significherebbe "scrivi stderr su 
un file chiamato letteralmente 1". 
 
Perché l'ordine conta 
La shell legge il reindirizzamento da sinistra a destra. 2>&1 significa "copia la destinazione 
attuale di fd 1" — non "tieni fd 2 sempre sincronizzato con fd 1". 
 
 
# CORRETTO: prima sposta stdout su file, poi aggancia stderr a stdout 
find / -name "*.conf" > tutto.log 2>&1 

 
 
 
# passo 1 — dopo > tutto.log:   fd1 → tutto.log,  fd2 → terminale 
# passo 2 — dopo 2>&1:          fd1 → tutto.log,  fd2 → tutto.log  ✓ 
 
 
# SBAGLIATO: 2>&1 viene letto prima, quando stdout punta ancora al terminale 
find / -name "*.conf" 2>&1 > tutto.log 
 
# passo 1 — dopo 2>&1:          fd1 → terminale,  fd2 → terminale  ← copia fd1 
com'è ora 
# passo 2 — dopo > tutto.log:   fd1 → tutto.log,  fd2 → terminale  ✗ stderr 
rimane sul terminale 
 
 
# Sintassi moderna equivalente (solo bash) 
find / -name "*.conf" &> tutto.log 
 
# Sintassi classica (funziona su sh, dash, bash — preferibile negli script) 
find / -name "*.conf" > tutto.log 2>&1 
 
Esempi pratici 
 
# Backup MySQL: output e errori nello stesso log 
mysqldump -u root -p fotodb > /var/log/backup.log 2>&1 
 
# Aggiornamento pacchetti silenzioso, tutto su log 
apt-get upgrade > /var/log/upgrade.log 2>&1 
 
# Esecuzione silenziosa — scarta tutto 
apt-get update &> /dev/null 
 
Reindirizzamento di stdin (0) 
 
# MySQL legge il dump da file invece che dalla tastiera 
mysql -u root -p fotodb < dump.sql 
 
# Invia il contenuto di un file come corpo di una mail 
mail -s "Report giornaliero" admin@studio.it < /var/log/backup.log 
 
/dev/null — il cestino 
 
# Esegui silenziosamente, nessun output 
apt-get update &> /dev/null 
 
2. Operatori di controllo 
; — esecuzione sequenziale (incondizionata) 
 
apt-get update ; apt-get upgrade 
# Il secondo gira sempre, anche se il primo fallisce 
 

 
 
# Backup e pulizia: la pulizia parte sempre, indipendentemente dal backup 
mysqldump -u root -p fotodb > backup.sql ; rm -f /tmp/export_temp.csv 
 
&& — AND logico 
Il secondo comando viene eseguito solo se il primo ha restituito codice 0. 
 
# Crea la directory e solo se riesce, entra dentro 
mkdir /var/www/nuovosito && cd /var/www/nuovosito 
 
# Installa nginx e solo se riesce, avvia il servizio 
apt-get install -y nginx && systemctl start nginx 
 
# Importa il dump solo se il backup è andato a buon fine 
mysqldump -u root -p fotodb > backup.sql && mysql -u root -p fotodb_test < 
backup.sql 
 
|| — OR logico 
Il secondo comando viene eseguito solo se il primo ha restituito codice diverso da 0. 
 
# Entra nella directory o, se non esiste, la crea 
cd /var/www/html || mkdir -p /var/www/html 
 
# Verifica connessione al DB o stampa errore e termina lo script 
mysql -u root -p -e "SELECT 1;" &>/dev/null || { echo "DB non raggiungibile"; 
exit 1; } 
 
Combinazione && e || 
 
# Simula un if/else in una riga 
ping -c1 8.8.8.8 &>/dev/null && echo "Rete OK" || echo "Rete non raggiungibile" 
 
# Verifica se nginx è attivo 
systemctl is-active nginx &>/dev/null && echo "nginx in esecuzione" || echo 
"nginx fermo" 
 
! — negazione del codice di uscita 
 
# Crea il file di config solo se non esiste già 
[ ! -f /etc/nginx/conf.d/studio.conf ] && cp /etc/nginx/conf.d/default.conf 
/etc/nginx/conf.d/studio.conf 
 
2b. $? — il codice di uscita 
Ogni comando restituisce un numero intero quando termina, chiamato exit code. È il valore 
che && e || controllano internamente. 
 
Valore Significato 
0 successo 

 
 
≠ 0 errore 
 
 
ls /etc 
echo $?        # → 0 
 
ls /cartella_inesistente 
echo $?        # → 2 
 
grep "root" /etc/passwd 
echo $?        # → 0  (trovato) 
 
grep "zzzz" /etc/passwd 
echo $?        # → 1  (nessun match — grep usa 1, non 2) 
 
mysql -u root -pwrong -e "SELECT 1;" &>/dev/null 
echo $?        # → 1  (autenticazione fallita) 
 
⚠  $? viene sovrascritto ad ogni comando, incluso echo. Va letto subito dopo il comando che 
interessa. 
Nei casi reali: salvarlo in una variabile 
 
mysqldump -u root -p fotodb > backup.sql 
ESITO=$? 
 
[ $ESITO -eq 0 ] && echo "Backup OK" || echo "Backup fallito (codice: $ESITO)" 
 
Exit code più comuni 
 
Codice Significato 
0 successo 
1 errore generico 
2 uso errato del comando 
127 comando non trovato 
130 interrotto con Ctrl+C 
 
3. Processi in background 
& — avvio in background 
 
# Il terminale torna subito disponibile 
php artisan queue:work & 
# [1] 4821  ← numero job e PID 
 
jobs — lista processi in background della sessione 

 
 
 
jobs 
# [1]+  Running    php artisan queue:work & 
# [2]-  Stopped    vim file.txt 
 
fg e bg 
 
fg          # porta in foreground il job corrente (+) 
fg %2       # porta in foreground il job numero 2 
 
bg          # riprende in background il job sospeso 
bg %2       # riprende in background il job 2 
 
Ctrl+Z — sospende il processo in foreground 
 
[Ctrl+Z] 
# [1]+  Stopped    ping google.com 
 
bg %1       # lo riprendi in background 
 
kill su job 
 
kill %1     # termina il job 1 (SIGTERM) 
kill -9 %1  # termina forzatamente (SIGKILL) 
 
I job in background sono legati alla sessione shell corrente: se chiudi il terminale, vengono 
terminati. 
4. nohup — processi persistenti 
nohup permette a un processo di sopravvivere alla chiusura del terminale, ignorando il 
segnale SIGHUP. 
 
# Avvio base — output automatico su nohup.out 
nohup php artisan queue:work & 
 
# Con log personalizzato 
nohup python3 script.py > /var/log/myscript.log 2>&1 & 
 
# Scartando tutto l'output 
nohup ./backup.sh &> /dev/null & 
 
Differenza chiave: & vs nohup & 
 
 comando & nohup comando & 
Terminale chiuso processo terminato processo continua 
Output sul terminale nohup.out (default) 

 
 
Segnale SIGHUP ricevuto ignorato 
 
Verificare che il processo stia girando 
 
ps aux | grep queue:work | grep -v grep 
 
5. Esercizio — Scenario: Studio fotografico 
Lo studio Luce & Scatto ti chiede di preparare uno script di manutenzione notturna per il 
proprio server Linux. Lo script deve: 
 
a) Creare la directory /var/log/studio/ se non esiste già, e interrompersi con un 
messaggio di errore se la creazione fallisce. 
b) Esportare la tabella sessioni del database fotodb su /tmp/sessioni_export.csv, 
salvando eventuali errori in /var/log/studio/errori.log. Verificare il codice di uscita e 
stampare un messaggio di esito. 
c) Eseguire find /var/www/fotografie -name "*.tmp" salvando i risultati su 
/var/log/studio/tmp_trovati.log e gli errori su /var/log/studio/errori.log (in aggiunta, non 
sovrascrivendo). 
d) Avviare lo script in background con nohup, in modo che continui a girare dopo il 
logout, con tutto l'output su /var/log/studio/manutenzione.log. 
e) Verificare con un solo comando che lo script sia effettivamente in esecuzione. 
Riepilogo 
 
Reindirizzamento: 
  >          stdout su file (sovrascrive) 
  >>         stdout su file (aggiunge) 
  2>         stderr su file 
  2>&1       stderr → dove punta stdout (ordine: prima >, poi 2>&1) 
  &>         stdout + stderr su file (solo bash) 
  <          stdin da file 
 
Operatori: 
  ;          esegui sempre in sequenza 
  &&         esegui solo se $? = 0 
  ||         esegui solo se $? ≠ 0 
  !          nega il codice di uscita 
 
$?: 
  0          successo 
  ≠ 0        errore (salvarlo subito in una variabile) 
 
Background: 
  cmd &      avvia in background 
  Ctrl+Z     sospendi in foreground 
  jobs       lista job sessione 
  fg %n      porta in foreground 
  bg %n      riprendi in background 
  kill %n    termina job 
 

 
 
nohup: 
  nohup cmd &                 persiste dopo logout 
  nohup cmd > log 2>&1 &      con log personalizzato 
 


---

# shell avanzata

**File:** `shell avanzata.pdf`
**Tipo:** `.pdf`
**Dimensione:** 492.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

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
tastiera, schermo, rete, dispositivi
Un processo non comunica direttamente
con l'hardware
Chiede al kernel di aprire un canale →
riceve un numero intero: il fd
Il reindirizzamento cambia dove
punta quel numero, non il processo
Analogia

I tre file descriptor standard
FD Nome Direzione Default
0 stdin ingresso ← tastiera
1 stdout uscita → terminale
2 stderr uscita → terminale
stdout e stderr puntano entrambi al terminale, ma sono canali separati — questo permette di 
separare output normale ed errori.

Reindirizzamento: stdout e stderr
stdout  (fd 1)
# sovrascrive
ls -l /etc > elenco.txt
# aggiunge in coda
ls -l /var/www >> elenco.txt
# equivalente esplicito
ls -l /etc 1> elenco.txt
stderr  (fd 2)
# separa errori dall'output
find / -name '*.conf' \
> risultati.txt 2> errori.log
# scarta gli errori
find /var/www -name '*.php' \
2> /dev/null
# grep: errori su file separato
grep -r 'password' /etc \
2> /tmp/errori.log
> sovrascrive   >> aggiunge   2> stderr   /dev/null cestino

Reindirizzare entrambi: 2>&1
2
fd 2 (stderr)
>
operatore
&
"questo è un 
fd"
1
fd 1 (stdout)
"Punta fd 2 verso lo stesso posto dove punta fd 1"
# Backup MySQL: tutto nello 
stesso log
mysqldump -u root -p fotodb \
> /var/log/backup.log 2>&1
# Scarta tutto (silenzioso)
apt-get update &> /dev/null
# &> equivale a > ... 2>&1
# ma funziona solo in bashSenza & davanti all'1: il comando 2>1 scriverebbe stderr su un file chiamato 
letteralmente "1"

2>&1 — l'ordine conta
La shell legge il reindirizzamento da sinistra a destra.
✓ CORRETTO
find / -name '*.conf' > tutto.log 2>&1
# passo 1 — > tutto.log:
#   fd1 → tutto.log
#   fd2 → terminale
# passo 2 — 2>&1:
#   fd2 → tutto.log  ✓
✗ SBAGLIATO
find / -name '*.conf' 2>&1 > tutto.log
# passo 1 — 2>&1:
#   fd2 → terminale  ← copia fd1 ora!
# passo 2 — > tutto.log:
#   fd1 → tutto.log
#   fd2 → terminale  ✗
Regola: prima sposta stdout con  >  poi aggancia stderr con  2>&1
Sintassi moderna (solo bash):   find / -name '*.conf' &> tutto.log

stdin (fd 0) e /dev/null
stdin  (fd 0) — leggere da file
# MySQL legge da file
# invece che dalla tastiera
mysql -u root -p fotodb < dump.sql
# Invia file come corpo mail
mail -s 'Report' \
admin@studio.it \
< /var/log/backup.log
/dev/null — il cestino
# Scarta solo stdout
apt-get update > /dev/null
# Scarta solo stderr
find / -name '*.conf' 2> /dev/null
# Scarta tutto
apt-get update &> /dev/null
Tutto quello che viene scritto in /dev/null scompare — nessun output, nessun errore visibile.

Operatori di controllo
;
Sempre in sequenza
Il secondo comando gira sempre, 
indipendentemente dall'esito del primo.
apt-get update ; apt-get upgrade
&&
Solo se successo
Il secondo comando gira solo se il primo ha 
restituito exit code 0.
mkdir /var/www/sito && cd /var/www/sito
||
Solo se fallimento
Il secondo comando gira solo se il primo ha 
restituito exit code ≠ 0.
cd /var/www/html || mkdir -p 
/var/www/html

Combinazioni e negazione !
&& e || insieme simulano un if/else in una riga:
# Rete raggiungibile?
ping -c1 8.8.8.8 &>/dev/null && echo 'Rete OK' || echo 'Rete KO'
# nginx è attivo?
systemctl is-active nginx &>/dev/null \
&& echo 'nginx in esecuzione' || echo 'nginx fermo'
# Importa dump solo se il backup ha avuto successo
mysqldump -u root -p fotodb > backup.sql \
&& mysql -u root -p fotodb_test < backup.sql
! — nega il codice di uscita
# Crea il file di config solo se NON esiste già
[ ! -f /etc/nginx/conf.d/studio.conf ] && cp default.conf studio.conf

$? — il codice di uscita
Ogni comando restituisce un numero quando termina. È il valore che && e || controllano.
0 successo
1 errore generico
2 uso errato del comando
127 comando non trovato
130 interrotto con Ctrl+C
ls /etc
echo $?        # → 0
ls /inesistente
echo $?        # → 2
grep 'root' /etc/passwd
echo $?        # → 0 (trovato)
grep 'zzzz' /etc/passwd
echo $?        # → 1 (non trovato)
$? viene sovrascritto ad ogni comando, incluso echo — salvarlo subito in una variabile.

$? nella pratica — salvarlo subito
Dopo il comando che ci interessa, assegniamo $? a una variabile prima che venga sovrascritto:
mysqldump -u root -p fotodb > backup.sql
ESITO=$?
[ $ESITO -eq 0 ] && echo 'Backup OK' \
|| echo "Backup fallito (codice: $ESITO)"
# Verifica connessione DB prima di procedere
mysql -u root -p -e 'SELECT 1;' &>/dev/null
ESITO=$?
[ $ESITO -ne 0 ] && { echo 'DB non raggiungibile'; exit 1; }
[ $ESITO -eq 0 ]  →  uguale a 0       [ $ESITO -ne 0 ]  →  diverso da 0

Processi in background
cmd &
Avvia in background
Il terminale è subito 
libero
[1] 4821  ← job e PID
jobs
Lista job della sessione
[1]+ Running  cmd &
[2]- Stopped  vim file.txt
fg %1
Porta in foreground
fg  →  job corrente (+)
fg %2  →  job numero 2 bg %1
Riprendi in background
bg  →  job corrente
bg %2  →  job numero 2
Ctrl+Z
Sospendi foreground
[1]+ Stopped  ping ...
bg %1  per riprendere kill %1
Termina job
SIGTERM (gentile)
kill -9 %1  →  SIGKILL
I job in background sono legati alla sessione corrente: chiudendo il terminale vengono terminati.

nohup — processi persistenti
nohup permette a un processo di sopravvivere alla chiusura del terminale, ignorando SIGHUP .
cmd & nohup cmd &
Terminale chiuso processo terminato processo continua
Output sul terminale nohup.out
Segnale SIGHUP ricevuto ignorato
# Output su nohup.out 
(default)
nohup php artisan queue:work &
# Con log personalizzato
nohup bash script.sh \
> /var/log/script.log 2>&1 &
# Verifica esecuzione
ps aux | grep script.sh | grep 
-v grepgrep -v grep filtra via la riga del grep stesso
(-v inverte il match: mostra le righe che NON contengono la stringa)

Esercizio
Studio fotografico Luce & Scatto
Preparare lo script manutenzione.sh:
a) Creare /var/log/studio/ o uscire con messaggio di errore
b) Esportare la tabella sessioni su CSV, log errori, verificare $?
c) Trovare file .tmp: output su log, errori in append su errori.log
d) Avviare con nohup, output su /var/log/studio/manutenzione.log
e) Verificare con un solo comando che lo script sia in esecuzione

Riepilogo
# Reindirizzamento
>      stdout su file (sovrascrive)
>>     stdout su file (aggiunge)
2>     stderr su file
2>&1   stderr → dove punta stdout
&>     stdout + stderr (solo bash)
<      stdin da file
# Operatori
;      esegui sempre in sequenza
&&     solo se $? = 0
||     solo se $? ≠ 0
!      nega il codice di uscita
# $?
0      successo
≠ 0    errore
ESITO=$?   # salvare subito
# Background
cmd &     avvia in background
Ctrl+Z    sospendi
jobs      lista job sessione
fg %n     porta in foreground
bg %n     riprendi in background
kill %n   termina job
# nohup
nohup cmd > log 2>&1 &


---

# Soluzione Ripasso Finale CSP

**File:** `Soluzione Ripasso Finale CSP.pdf`
**Tipo:** `.pdf`
**Dimensione:** 154.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte  ·  Linux Server SOLUZIONE — StudioFoto Arcobaleno 
Pag. 1 
 
ITS ICT Piemonte 
Corso Linux Server — CSP — Cloud Specialist 
SOLUZIONE 
Ripasso finale — Linux Server 
Scenario: StudioFoto Arcobaleno 
Comandi, configurazioni e verifiche 
Durata: 2 ore  ·  Valutazione: 16 punti (1 per punto) — sufficienza a 10 
  

ITS ICT Piemonte  ·  Linux Server SOLUZIONE — StudioFoto Arcobaleno 
Pag. 2 
Nota — Soluzione di riferimento. Le password sono segnaposto; in laboratorio usare 
credenziali coerenti con la policy del corso. Comandi verificati su Debian 12 (PHP 8.2).  
 
Parte 1 — Utenti, gruppi e permessi  (~25 min) 
Hostname persistente 
sudo hostnamectl set-hostname arcobaleno-srv 
hostnamectl                 # Static hostname: arcobaleno-srv 
 
Gruppo e utenti 
sudo groupadd fotografi 
sudo useradd -m -s /bin/bash -G fotografi anna 
sudo useradd -m -s /bin/bash -G fotografi luca 
sudo passwd anna   &&   sudo passwd luca 
id anna      # verifica gruppi (groups=...,fotografi) 
 
Directory condivisa + bit speciali 
sudo mkdir -p /srv/scatti 
sudo chgrp fotografi /srv/scatti 
sudo chmod 3770 /srv/scatti     # 2=SGID + 1=Sticky 
ls -ld /srv/scatti              # drwxrws--T  root fotografi 
 
Spiegazione bit speciali 
Nota — SGID (2) sulla directory: ogni nuovo file/sottocartella eredita automaticamente il 
gruppo fotografi invece del gruppo primario di chi scrive. Sticky bit (1): in una directory a 
scrittura condivisa, solo il proprietario del file (oltre a root e al proprietario della directory) 
può cancellarlo o rinominarlo. 
 
Parte 2 — Rete  (~15 min) 
/etc/network/interfaces 
# NAT - DHCP 
allow-hotplug enp0s3 
iface enp0s3 inet dhcp 
  
# Solo Host - IP statico 
auto enp0s8 
iface enp0s8 inet static 
    address 192.168.56.120 
    netmask 255.255.255.0 
 
Applica e verifica 
sudo systemctl restart networking 
ip a show enp0s8        # inet 192.168.56.120/24 

ITS ICT Piemonte  ·  Linux Server SOLUZIONE — StudioFoto Arcobaleno 
Pag. 3 
 
Record in /etc/hosts 
echo '10.0.0.2    db.arcobaleno.local' | sudo tee -a /etc/hosts 
getent hosts db.arcobaleno.local    # 10.0.0.2  db.arcobaleno.local 
 
Parte 3 — Accesso remoto SSH  (~15 min) 
Lato client: chiave e copia 
ssh-keygen -t ed25519 -C 'its-usr@arcobaleno' 
ssh-copy-id its-usr@192.168.56.120 
ssh its-usr@192.168.56.120     # prova: deve entrare senza password 
 
/etc/ssh/sshd_config 
PermitRootLogin no 
PasswordAuthentication no 
PubkeyAuthentication yes 
 
Test, ricarica, verifica 
sudo sshd -t                  # test sintassi (nessun output = OK) 
sudo systemctl reload ssh 
sudo systemctl status ssh     # active (running) 
 
Parte 4 — Web server nginx + PHP  (~20 min) 
Installazione 
sudo apt update 
sudo apt install -y nginx php-fpm   # Debian 12 -> php8.2-fpm 
 
Pagina info.php 
sudo mkdir -p /var/www/arcobaleno 
echo '<?php phpinfo();' | sudo tee /var/www/arcobaleno/info.php 
 
/etc/nginx/sites-available/arcobaleno 
server { 
    listen 80; 
    server_name arcobaleno.local; 
    root /var/www/arcobaleno; 
    index index.php info.php; 
    location / { try_files $uri $uri/ =404; } 
    location ~ \.php$ { 
        include snippets/fastcgi-php.conf; 
        fastcgi_pass unix:/run/php/php8.2-fpm.sock; 
    } 
} 

ITS ICT Piemonte  ·  Linux Server SOLUZIONE — StudioFoto Arcobaleno 
Pag. 4 
 
Abilita e verifica 
sudo ln -s /etc/nginx/sites-available/arcobaleno /etc/nginx/sites-enabled/ 
sudo nginx -t   &&   sudo systemctl reload nginx 
curl -s http://localhost/info.php | head   # HTML, non sorgente PHP 
 
Parte 5 — Database MariaDB  (~15 min) 
Installazione e hardening 
sudo apt install -y mariadb-server 
sudo mysql_secure_installation 
 
Database e utente (console come root) 
sudo mariadb 
CREATE DATABASE arcobaleno_db; 
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'PasswordSicura'; 
GRANT ALL PRIVILEGES ON arcobaleno_db.* TO 'wpuser'@'localhost'; 
FLUSH PRIVILEGES; 
EXIT; 
 
Verifica login applicativo 
mariadb -u wpuser -p -e 'SHOW DATABASES;' 
# deve mostrare solo: information_schema, arcobaleno_db 
 
Parte 6 — Processi e servizi  (~10 min) 
Stato e avvio automatico 
sudo systemctl enable --now nginx php8.2-fpm mariadb 
systemctl is-enabled nginx php8.2-fpm mariadb   # enabled x3 
systemctl status nginx php8.2-fpm mariadb --no-pager 
 
Processo in background e terminazione 
sleep 1000 & 
jobs -l            # mostra [1] <PID> 
ps aux | grep sleep 
kill <PID>         # SIGTERM (15); kill -9 <PID> solo se necessario 
 
Parte 7 — Automazione (cron) e firewall (iptables)  (~15 min) 
/usr/local/bin/backup-scatti.sh 
#!/bin/bash 
SRC="/srv/scatti" 
DEST="/var/backups" 

ITS ICT Piemonte  ·  Linux Server SOLUZIONE — StudioFoto Arcobaleno 
Pag. 5 
DATA=$(date +%F)                     # AAAA-MM-GG 
mkdir -p "$DEST" 
tar -czf "$DEST/scatti-$DATA.tar.gz" "$SRC" 
 
Esegui-bilità e cron 
sudo chmod +x /usr/local/bin/backup-scatti.sh 
sudo crontab -e 
# riga da aggiungere (min ora * * *): 
30 2 * * * /usr/local/bin/backup-scatti.sh 
 
iptables — installazione e regole 
sudo apt install -y iptables iptables-persistent 
sudo iptables -A INPUT -i lo -j ACCEPT 
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT 
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # SSH 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # HTTP 
sudo iptables -P INPUT DROP        # policy DROP DOPO gli ACCEPT 
sudo iptables -P FORWARD DROP 
 
Persistenza e verifica 
sudo netfilter-persistent save 
sudo iptables -L -n -v 
 
Parte 8 — Diagnostica  (~5 min) 
1. Rete 
ip a            # interfaccia su e con IP corretto? 
ip route        # gateway presente? 
ping 192.168.56.120 
 
2. Firewall 
sudo iptables -L -n -v     # la porta 80 e' permessa in INPUT? 
 
3. Servizio 
systemctl status nginx php8.2-fpm 
ss -tlnp | grep :80        # nginx in ascolto sulla 80? 
sudo nginx -t 
 
4. Applicazione 
curl -I http://localhost/ 
sudo tail /var/log/nginx/error.log 
# es. errore DB: verificare socket php-fpm e credenziali MariaDB 
 


---

# Soluzioni Esercitazione doc

**File:** `Soluzioni Esercitazione doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 138.7 KB
**Ultima modifica:** 02/07/2026 09:22

---

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 1 
 
SOLUZIONI 
Diagnostica e messa in sicurezza — Esercitazione WordPress 
Docente: Wolfgang Cecchin 
Panoramica dei guasti 
# Macchina Livello Guasto Causa 
1 debian3 Rete IP rete interna errato 10.0.0.11 invece di 10.0.0.1 
2 debian3 Firewall HTTP bloccato Policy DROP, no regola 
porta 80 
3 debian3 Servizio nginx root sbagliata /var/www/html invece di 
/var/www/wordpress 
4 debian3 Applicazione Nome sito errato server_name e 
wp_options da cambiare 
5 debian4 Rete Interfaccia intnet spenta enp0s8 DOWN, auto 
commentato 
6 debian4 Firewall MariaDB bloccato Policy DROP, no regola 
porta 3306 
7 debian4 Servizio bind-address errato 127.0.0.1 invece di 10.0.0.2 
  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 2 
DEBIAN3 — DIAGNOSI E SOLUZIONI 
 
Guasto 1 — IP rete interna errato 
Diagnosi 
ip a show enp0s9 
L'interfaccia mostra 10.0.0.11/24 invece di 10.0.0.1/24. Anche se il ping verso 10.0.0.2 funziona 
(stessa subnet), WordPress non riesce a connettersi al database perché l'utente MariaDB 
wpuser è autorizzato solo per connessioni dall'IP 10.0.0.1. 
Soluzione 
sudo nano /etc/network/interfaces 
 
# Modificare la riga: 
#   address 10.0.0.11 
# in: 
#   address 10.0.0.1 
Applicare: 
sudo systemctl restart networking 
Verifica: 
ip a show enp0s9 
# Deve mostrare 10.0.0.1/24 
Guasto 2 — Firewall blocca HTTP 
Diagnosi 
sudo iptables -L INPUT -n --line-numbers 
La policy è DROP. Le regole permettono solo loopback, ESTABLISHED/RELATED e SSH sulla 
porta 2222. Non c'è nessuna regola per la porta 80. 
Test di conferma: 
curl -I http://localhost 
# Funziona (loopback aperto) 
 
# Ma dal browser Windows: timeout 
# (la porta 80 e' bloccata dall'esterno) 
Soluzione 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT 
 
# Salvare per la persistenza: 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 3 
Verifica: 
sudo iptables -L INPUT -n --line-numbers 
# Deve mostrare la regola ACCEPT per dpt:80 
Guasto 3 — nginx root sbagliata 
Diagnosi 
sudo nginx -T | grep root 
Il virtual host punta a root /var/www/html invece di root /var/www/wordpress. nginx 
risponde, ma serve la pagina di default Debian. 
Soluzione 
sudo nano /etc/nginx/sites-available/wordpress 
 
# Modificare: 
#   root /var/www/html; 
# in: 
#   root /var/www/wordpress; 
Applicare: 
sudo nginx -t 
sudo systemctl reload nginx 
Guasto 4 — Nome sito errato (acme.local) 
Il sito è configurato per rispondere al nome "wordpress". Acme richiede che risponda a 
"acme.local". La modifica va fatta in due punti: nginx e il database WordPress.  
Passo 1 — nginx server_name 
sudo nano /etc/nginx/sites-available/wordpress 
 
# Modificare: 
#   server_name wordpress; 
# in: 
#   server_name acme.local; 
sudo nginx -t 
sudo systemctl reload nginx 
Passo 2 — URL nel database WordPress 
Da debian3, connettersi al database su debian4: 
mysql -h 10.0.0.2 -u wpuser -p wordpress 
Aggiornare i due campi: 
UPDATE wp_options SET option_value = 'http://acme.local' 

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 4 
WHERE option_name = 'siteurl'; 
 
UPDATE wp_options SET option_value = 'http://acme.local' 
WHERE option_name = 'home'; 
Verifica: 
SELECT option_name, option_value FROM wp_options 
WHERE option_name IN ('siteurl', 'home'); 
 
# Entrambi devono mostrare http://acme.local 
Nota: senza questo passaggio, WordPress continua a generare link e redirect verso il vecchio 
nome. Lo studente che corregge solo nginx ma non il database vedrà il sito caricarsi in 
modo anomalo. 
  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 5 
DEBIAN4 — DIAGNOSI E SOLUZIONI 
 
Nota: l'accesso iniziale a debian4 avviene esclusivamente dalla console VirtualBox.  
Guasto 5 — Interfaccia rete interna disattivata 
Diagnosi 
ip a show enp0s8 
# State: DOWN, nessun indirizzo IP 
 
cat /etc/network/interfaces 
# La riga 'auto enp0s8' e' commentata: #auto enp0s8 
L'interfaccia di rete interna è spenta e non si attiva al boot. 
Soluzione 
sudo nano /etc/network/interfaces 
 
# Decommentare la riga: 
#   #auto enp0s8 
# in: 
#   auto enp0s8 
Attivare: 
sudo ip link set enp0s8 up 
sudo systemctl restart networking 
Verifica: 
ip a show enp0s8 
# Deve mostrare 10.0.0.2/24 e state UP 
 
# Da debian3: 
ping -c 4 10.0.0.2 
# Deve rispondere 
Guasto 6 — Firewall blocca porta 3306 
Diagnosi 
sudo iptables -L INPUT -n --line-numbers 
Policy DROP, regole solo per loopback e ESTABLISHED/RELATED. Nessuna regola per la porta 
3306. 
Il ping da debian3 risponde, ma la connessione MariaDB va in timeout. 
Soluzione 
Aggiungere le regole per MariaDB e SSH, esclusivamente dalla rete interna:  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 6 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 3306 -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 2222 -j ACCEPT 
 
# Salvare: 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
Guasto 7 — MariaDB bind-address a localhost 
Diagnosi 
Anche con l'interfaccia attiva e il firewall aperto, da debian3: 
mysql -h 10.0.0.2 -u wpuser -p 
# Timeout o connessione rifiutata 
Su debian4: 
sudo ss -tulnp | grep 3306 
# Mostra 127.0.0.1:3306 — ascolta solo sulla loopback 
 
grep bind-address /etc/mysql/mariadb.conf.d/50-server.cnf 
# bind-address = 127.0.0.1 
MariaDB ascolta solo sulla loopback, non sull'interfaccia di rete interna. 
Soluzione 
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf 
 
# Modificare: 
#   bind-address = 127.0.0.1 
# in: 
#   bind-address = 10.0.0.2 
Riavviare: 
sudo systemctl restart mariadb 
Verifica: 
sudo ss -tulnp | grep 3306 
# Deve mostrare 10.0.0.2:3306 
 
# Da debian3: 
mysql -h 10.0.0.2 -u wpuser -p 
# Connessione riuscita 
  

ITS ICT Piemonte — Linux Server — SOLUZIONI 
Pagina 7 
VERIFICA FINALE 
 
Verifica dal PC Windows 
1. Aggiungere nel file C:\Windows\System32\drivers\etc\hosts: 
192.168.56.111  acme.local 
 
2. Aprire il browser su http://acme.local 
3. Il sito WordPress di Acme deve essere visibile e funzionante. 
Configurazione firewall completa 
debian3 — Ruleset finale 
sudo iptables -P INPUT DROP 
sudo iptables -P FORWARD DROP 
sudo iptables -P OUTPUT ACCEPT 
 
sudo iptables -A INPUT -i lo -j ACCEPT 
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 2222 -j ACCEPT 
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT 
 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
debian4 — Ruleset finale 
sudo iptables -P INPUT DROP 
sudo iptables -P FORWARD DROP 
sudo iptables -P OUTPUT ACCEPT 
 
sudo iptables -A INPUT -i lo -j ACCEPT 
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 2222 -j ACCEPT 
sudo iptables -A INPUT -i enp0s8 -p tcp --dport 3306 -j ACCEPT 
 
sudo iptables-save | sudo tee /etc/iptables/rules.v4 
 


---

# Soluzioni Esercitazione presentazione

**File:** `Soluzioni Esercitazione presentazione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 153.9 KB
**Ultima modifica:** 02/07/2026 09:22

---

SOLUZIONI
Diagnostica e messa in sicurezza
Esercitazione WordPress
Docente: Wolfgang Cecchin

Panoramica dei guasti
# Macchina Livello Guasto Causa
1 debian3 Rete IP rete interna errato 10.0.0.11 → 10.0.0.1
2 debian3 Firewall HTTP bloccato No regola porta 80
3 debian3 Servizio nginx root sbagliata /var/www/html → /wordpress
4 debian3 Applicazione Nome sito errato server_name + wp_options
5 debian4 Rete Interfaccia spenta enp0s8 DOWN
6 debian4 Firewall MariaDB bloccato No regola porta 3306
7 debian4 Servizio bind-address errato 127.0.0.1 → 10.0.0.2

debian3
Frontend — Diagnosi e soluzioni

debian3 — Guasto 1 Rete
IP rete interna errato
DIAGNOSI
ip a show enp0s9
# Mostra 10.0.0.11/24
# Dovrebbe essere 10.0.0.1/24
# Il ping verso 10.0.0.2 funziona
# (stessa subnet) ma WordPress
# non si collega al DB: wpuser
# autorizzato solo per 10.0.0.1
SOLUZIONE
sudo nano /etc/network/interfaces
# Cambiare:
#  address 10.0.0.11
# in:
#  address 10.0.0.1
sudo systemctl restart networking
# Verifica:
ip a show enp0s9
Subdolo: ping OK ma connessione DB fallisce — lo studente deve collegare IP e permessi MySQL.

debian3 — Guasto 2 Firewall
Firewall blocca HTTP
DIAGNOSI
sudo iptables -L INPUT -n --line-numbers
# Policy: DROP
# Regole: lo, ESTABLISHED, SSH:2222
# Manca: porta 80
# Conferma:
curl -I http://localhost   # OK
# Browser Windows: timeout
SOLUZIONE
sudo iptables -A INPUT \
-p tcp --dport 80 -j ACCEPT
# Salvare:
sudo iptables-save | \
sudo tee /etc/iptables/rules.v4
# Verifica:
sudo iptables -L INPUT -n \
--line-numbers
SSH funziona → lo studente pensa che la rete sia OK. Deve capire che il blocco è solo su HTTP.

debian3 — Guasto 3 Servizio
nginx root sbagliata
DIAGNOSI
sudo nginx -T | grep root
# Mostra: root /var/www/html
# Dovrebbe: root /var/www/wordpress
# nginx risponde ma serve la
# pagina di default Debian
# invece di WordPress
SOLUZIONE
sudo nano /etc/nginx/\
sites-available/wordpress
# Cambiare:
#  root /var/www/html;
# in:
#  root /var/www/wordpress;
sudo nginx -t
sudo systemctl reload nginx
Distinguere tra 'il servizio risponde' e 'il servizio risponde con il contenuto giusto'.

debian3 — Guasto 4 Applicazione
Nome sito errato → acme.local
Due modifiche necessarie: nginx + database WordPress
PASSO 1 — nginx server_name
# In sites-available/wordpress
# Cambiare:
#  server_name wordpress;
# in:
#  server_name acme.local;
sudo nginx -t
sudo systemctl reload nginx
PASSO 2 — URL nel database
mysql -h 10.0.0.2 -u wpuser
-p wordpress
UPDATE wp_options
SET option_value =
'http://acme.local'
WHERE option_name = 'siteurl';
UPDATE wp_options
SET option_value =
'http://acme.local'
WHERE option_name = 'home';
Senza il passo 2, WordPress fa redirect al vecchio nome anche con nginx corretto.

debian4
Backend — Diagnosi e soluzioni

debian4 — Guasto 5 Rete
Interfaccia rete interna spenta
DIAGNOSI
ip a show enp0s8
# State: DOWN, no IP
cat /etc/network/interfaces
# #auto enp0s8  (commentato!)
# Da debian3:
ping 10.0.0.2  # NESSUNA RISPOSTA
SOLUZIONE
sudo nano /etc/network/interfaces
# Decommentare:
#  #auto enp0s8
# in:
#  auto enp0s8
sudo ip link set enp0s8 up
sudo systemctl restart networking
# Verifica da debian3:
ping -c 4 10.0.0.2  # OK
Accesso solo via console VirtualBox — come andare fisicamente in sala server.

debian4 — Guasto 6 Firewall
Firewall blocca porta 3306
DIAGNOSI
sudo iptables -L INPUT -n \
--line-numbers
# Policy: DROP
# Regole: solo lo, ESTABLISHED
# No regola per 3306
# ping da debian3: OK
# ma mysql: TIMEOUT
SOLUZIONE
# MariaDB dalla rete interna
sudo iptables -A INPUT \
-i enp0s8 -p tcp \
--dport 3306 -j ACCEPT
# SSH dalla rete interna
sudo iptables -A INPUT \
-i enp0s8 -p tcp \
--dport 2222 -j ACCEPT
# Salvare:
sudo iptables-save | \
sudo tee /etc/iptables/rules.v4
Ping OK ma servizio KO → il 'qualcosa in mezzo' è il firewall.

debian4 — Guasto 7 Servizio
MariaDB bind-address a localhost
DIAGNOSI
sudo ss -tulnp | grep 3306
# 127.0.0.1:3306
# Ascolta SOLO su loopback!
grep bind-address \
/etc/mysql/mariadb.conf.d/\
50-server.cnf
# bind-address = 127.0.0.1
SOLUZIONE
sudo nano /etc/mysql/\
mariadb.conf.d/50-server.cnf
# Cambiare:
#  bind-address = 127.0.0.1
# in:
#  bind-address = 10.0.0.2
sudo systemctl restart mariadb
# Verifica:
sudo ss -tulnp | grep 3306
# Deve mostrare 10.0.0.2:3306
Il guasto più subdolo: rete OK + firewall OK ma servizio non raggiungibile. Serve ss -tulnp.

Verifica finale
192.168.56.111  acme.local
→ C:\Windows\System32\drivers\etc\hosts
Aprire http://acme.local nel browser
Il sito WordPress di Acme deve essere visibile e funzionante.
debian3 — Ruleset finale
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -m state ... -j ACCEPT
-A INPUT -i enp0s8 --dport 2222
-A INPUT --dport 80 -j ACCEPT
debian4 — Ruleset finale
-P INPUT DROP
-P FORWARD DROP
-P OUTPUT ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -m state ... -j ACCEPT
-A INPUT -i enp0s8 --dport 2222
-A INPUT -i enp0s8 --dport 3306


---

# soluzioni find

**File:** `soluzioni find.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3971.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

Soluzioni — find 
Ricerca base 
Es. 1  Cercare in tutto il filesystem un file di nome resolv.conf, sopprimendo gli errori.  
$ find / -name "resolv.conf" 2>/dev/null 
La ricerca parte dalla radice /. Il reindirizzamento 2>/dev/null scarta i messaggi "Permission 
denied" su stderr, lasciando l'output pulito. 
Es. 2  Trovare tutti i file con estensione .log nella directory /var/log. 
$ find /var/log -name "*.log" 
Il pattern *.log usa il glob * per qualsiasi prefisso. Le virgolette impediscono alla shell di 
espandere il glob prima di passarlo a find. 
Es. 3  Trovare tutte le directory che si chiamano backup a partire da /home.  
$ find /home -type d -name "backup" 
-type d limita la ricerca alle sole directory, escludendo file con lo stesso nome.  
Es. 4  Trovare i file di proprietà del tuo utente in /tmp. 
$ find /tmp -user $(whoami) 
La sostituzione di comando $(whoami) inserisce automaticamente il nome dell'utente corrente. 
In alternativa si può scrivere il nome esplicitamente: find /tmp -user mario. 
 
Ricerca per dimensione e data 
Es. 5  Trovare tutti i file regolari di dimensione superiore a 100 MiB nel filesystem.  
$ find / -type f -size +100M 2>/dev/null 
-type f esclude directory e link. +100M significa strettamente maggiore di 100 MiB. 2>/dev/null 
sopprime gli errori di accesso negato. 
Es. 6  Trovare i file in /etc modificati nelle ultime 24 ore. 
$ find /etc -mtime -1 
Il valore -1 con -mtime significa «modificati da meno di 1 giorno», ovvero nelle ultime 24 ore. Per 
ricerche più precise al minuto si può usare -mmin -60 (ultima ora). 
 
Permessi 
Es. 7  Trovare tutti i file nel sistema con il bit SUID attivo. 
$ find / -type f -perm /4000 2>/dev/null 
Il formato /4000 (slash) significa «almeno uno dei bit indicati è presente»: qui il bit SUID (4000). -
type f esclude le directory. 2>/dev/null rimuove i messaggi di accesso negato. 
 
⚠️  Sicurezza: I file SUID di proprietà di root vengono eseguiti con privilegi di 
amministratore. Censirli periodicamente è una buona pratica di hardening.  
 
Es. 8  Trovare le directory con lo sticky bit attivo (come /tmp). 
$ find / -type d -perm /1000 2>/dev/null 
Lo sticky bit su una directory (1000) impedisce agli utenti di eliminare i file altrui anche se hanno 
il permesso di scrittura sulla directory, come accade in /tmp. 
Es. 9  Trovare tutti i file con almeno uno dei permessi speciali attivi (SUID, SGID, Sticky).  

$ find / -perm /7000 2>/dev/null 
Il valore 7000 è la somma dei tre bit speciali: SUID (4000) + SGID (2000) + Sticky (1000). Con il 
formato / basta che sia attivo almeno uno dei tre. 
Es. 10  Trovare i file scrivibili da "others" in /home (potenziale rischio sicurezza).  
$ find /home -type f -perm -002 
Il formato -002 (trattino) significa «il bit 002 deve essere presente»: permesso di scrittura per 
others. Un file scrivibile da chiunque in /home è spesso un errore di configurazione da 
correggere. 
 
Azioni e pipeline 
Es. 11  Trovare i file *.conf in /etc modificati negli ultimi 7 giorni e visualizzarli con ls -lh. 
$ find /etc -name "*.conf" -mtime -7 -exec ls -lh {} \; 
Il {} viene sostituito dal percorso di ogni file trovato. Il \; termina il comando -exec: il backslash 
previene l'interpretazione del ; da parte della shell. 
Es. 12  Cercare in /etc/ tutti i file che contengono la stringa 127.0.0.1 usando find + xargs grep.  
$ find /etc/ -name '*' -type f | xargs grep "127.0.0.1" 
find produce la lista dei file; xargs la passa a grep come argomenti. È equivalente a grep -r 
"127.0.0.1" /etc/ ma il -type f di find garantisce di passare solo file regolari, evitando errori su 
directory e link. 
 
💡  Nomi con spazi: Se i percorsi possono contenere spazi, usare la variante sicura: find 
/etc/ -type f -print0 | xargs -0 grep "127.0.0.1" 
 
Es. 13  Trovare tutti i file di proprietà dell'utente mario e copiarli in /root/backup_mario/.  
$ find / -user mario -type f -exec cp {} /root/backup_mario/ \; 2>/dev/null 
Per ogni file trovato viene eseguito cp file /root/backup_mario/. La directory di destinazione 
deve esistere prima di lanciare il comando: mkdir -p /root/backup_mario/. 
Es. 14 (avanzato)  Trovare file chiamati student nel filesystem, escludendo /proc e /tmp, 
sopprimendo gli errori. 
$ find / -name "student" -type f ! -path '*/proc/*' ! -path '*/tmp/*' 2>/dev/null 
Il ! è l'operatore NOT: esclude i percorsi che corrispondono al pattern. */proc/* e */tmp/* 
escludono qualsiasi path che contenga quelle directory. È buona pratica escludere /proc e 
/sys nelle ricerche di sistema perché sono filesystem virtuali, non contengono file reali e 
generano molti falsi risultati. 


---

# soluzioni grep sed awk

**File:** `soluzioni grep sed awk.pdf`
**Tipo:** `.pdf`
**Dimensione:** 3887.4 KB
**Ultima modifica:** 02/07/2026 09:22

---

Soluzioni — grep, sed, awk 
File di riferimento: sistema.log  |  utenti.txt  |  webserver.conf  |  vendite.csv 
grep 
Es. 1  Mostrare tutte le righe di sistema.log che contengono la parola ERROR.  
$ grep "ERROR" sistema.log 
 
Es. 2  Mostrare le righe di sistema.log che contengono ERROR oppure WARNING.  
$ grep -E "ERROR|WARNING" sistema.log 
-E abilita le espressioni regolari estese; | è l'operatore OR. 
Es. 3  Contare quante volte appare "Failed password" nel file di log. 
$ grep -c "Failed password" sistema.log 
-c stampa il conteggio delle righe corrispondenti, non le righe stesse. 
Es. 4  In utenti.txt mostrare solo gli utenti la cui shell è /bin/bash. 
$ grep "/bin/bash$" utenti.txt 
Il $ ancora il pattern alla fine della riga: esclude eventuali righe che contengono /bin/bash nel 
mezzo del testo. 
Es. 5  In webserver.conf mostrare tutte le righe non vuote e non commentate.  
$ grep -v "^#" webserver.conf | grep -v "^$" 
Prima pipeline: esclude le righe che iniziano con #. Seconda: esclude le righe vuote (^$ = inizio 
riga immediatamente seguita da fine riga). 
 
sed 
Es. 6  In webserver.conf, sostituire WARNING con ERROR solo a video. 
$ sed 's/WARNING/ERROR/' webserver.conf 
Senza -i l'output va sullo stdout; il file originale non viene modificato. 
Es. 7  In webserver.conf, eliminare dall'output le righe di commento.  
$ sed '/^#/d' webserver.conf 
Il comando d (delete) elimina le righe che corrispondono al pattern. Anche qui senza -i: 
nessuna modifica al file. 
Es. 8  In sistema.log, sostituire server01 con webserver.lan e salvare in un nuovo file.  
$ sed 's/server01/webserver.lan/g' sistema.log > sistema_mod.log 
Il flag g sostituisce tutte le occorrenze per riga. Il reindirizzamento > salva l'output in 
sistema_mod.log senza toccare l'originale. 
 
awk 
Es. 9  Da utenti.txt, estrarre nome utente (campo 1) e home directory (campo 6).  
$ awk -F: '{print $1, $6}' utenti.txt 
-F: imposta i due punti come separatore di campo. 
Es. 10  Da vendite.csv, mostrare le righe della categoria "obiettivi" con prodotto e prezzo unitario.  
$ awk -F, '$3 == "obiettivi" {print $2, $5}' vendite.csv 
$3 è la categoria, $2 il prodotto, $5 il prezzo unitario. 

Es. 11  Da vendite.csv, calcolare il totale delle vendite per ogni venditore.  
$ awk -F, 'NR>1 {totale[$7] += $6} END {for (v in totale) print v, totale[v]}' 
vendite.csv 
NR>1 salta la riga di intestazione. $7 è il venditore, $6 il totale della vendita. L'array associativo 
totale[] accumula la somma per ciascun venditore; il blocco END stampa i risultati a fine 
elaborazione. 
 
Es. 12  (avanzato) Da sistema.log, estrarre tutti gli IP e contare quante volte appare ciascuno.  
$ grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" sistema.log | sort | uniq -c | sort -rn 
-o stampa solo la parte corrispondente (non l'intera riga). -E abilita le regex estese per il pattern 
dell'IP. sort | uniq -c conta le occorrenze; sort -rn ordina per frequenza decrescente. 
 
💡 Soluzione alternativa con solo awk: 
$ awk 'match($0,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/) {ip=substr($0,RSTART,RLENGTH); 
c[ip]++} END {for (ip in c) print c[ip], ip}' sistema.log | sort -rn 
 


---

# tabella libri

**File:** `tabella libri.sql`
**Tipo:** `.sql`
**Dimensione:** 0.3 KB
**Ultima modifica:** 02/07/2026 09:22

---

CREATE TABLE IF NOT EXISTS libri (
    id          INT             UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    titolo      VARCHAR(255)    NOT NULL,
    autore      VARCHAR(150)    NOT NULL,
    isbn        CHAR(13)        UNIQUE NOT NULL,
    pagine      SMALLINT        UNSIGNED NOT NULL,
    prezzo      DECIMAL(6,2)    UNSIGNED NOT NULL
);


---

# URL nel database WordPress

**File:** `URL nel database WordPress.txt`
**Tipo:** `.txt`
**Dimensione:** 0.7 KB
**Ultima modifica:** 02/07/2026 09:22

---

URL nel database WordPress

Da debian3, connettersi al database su debian4:
mysql -h 10.0.0.2 -u wpuser -p WordPress

Aggiornare i due campi:
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'siteurl';

UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'home';

Verifica:
SELECT option_name, option_value FROM wp_options
WHERE option_name IN ('siteurl', 'home');

# Entrambi devono mostrare http://acme.local
Nota: senza questo passaggio, WordPress continua a generare link e redirect verso il vecchio nome. Lo studente che corregge solo nginx ma non il database vedrà il sito caricarsi in modo anomalo.
 



---

# wordpress due macchine doc

**File:** `wordpress due macchine doc.pdf`
**Tipo:** `.pdf`
**Dimensione:** 4075.6 KB
**Ultima modifica:** 02/07/2026 09:22

---

WordPress su Architettura a Due 
Macchine 
Guida pratica per ITS Academy — Linux Server 
1. Architettura dell'esercitazione 
L'obiettivo è mettere in rete due macchine virtuali Debian in modo che: 
 
• debian1 esponga WordPress su nginx, accessibile dall'esterno 
• debian2 ospiti MariaDB, raggiungibile solo da debian1 tramite rete interna 
• L'accesso SSH a debian2 avvenga esclusivamente passando per debian1 
(ProxyJump) 
 
1.1 Schema di rete 
Macchina NIC 1 NIC 2 NIC 3 
debian1 NAT (internet) Solo Host (SSH da 
host) 
Rete interna 
intnet 
debian2 NAT (internet) Rete interna 
intnet 
— 
 
Macchina IP Solo Host IP Rete Interna 
debian1 192.168.56.110 10.0.0.1 
debian2 — 10.0.0.2 
 
2. Preparazione delle macchine virtuali in VirtualBox 
2.1 Clonare la macchina di base 
Partendo da una macchina Debian già configurata (debian1), clonare la VM in VirtualBox per 
ottenere debian2. Durante il clone, scegliere di rigenerare i MAC address. 
 
⚠️ Nota: Se il MAC address non viene rigenerato automaticamente, farlo manualmente 
dalle impostazioni di ogni scheda di rete: Impostazioni → Rete → Impostazioni avanzate → 
icona 🔄 
 
2.2 Configurazione NIC in VirtualBox 
Su debian2 
• NIC 1: NAT (tenere per apt) 

• NIC 2: Rete interna → nome: intnet 
 
Su debian1 
• NIC 1: NAT 
• NIC 2: Solo Host (accesso SSH dall'host) 
• NIC 3: Rete interna → nome: intnet (aggiungere una terza scheda) 
 
3. Configurazione hostname su debian2 
Dopo il clone, cambiare il nome della macchina su debian2: 
 
echo "debian2" | sudo tee /etc/hostname 
sudo sed -i 's/debian1/debian2/' /etc/hosts 
sudo hostnamectl set-hostname debian2 
 
Verificare: 
hostnamectl 
 
4. Configurazione della rete interna (intnet) 
4.1 Verificare le interfacce disponibili 
ip link show 
 
Macchina Interfaccia Ruolo 
debian1 enp0s3 NAT 
debian1 enp0s8 Solo Host 
debian1 enp0s9 Rete interna intnet 
debian2 enp0s3 NAT 
debian2 enp0s8 Rete interna intnet 
 
4.2 Configurare IP statico su debian1 
Aprire /etc/network/interfaces e aggiungere: 
 
# Internal network interface (intnet) 
# Static IP for private communication with debian2 
auto enp0s9 
iface enp0s9 inet static 
    address 10.0.0.1 
    netmask 255.255.255.0 
 
Attivare l'interfaccia: 

sudo ip addr add 10.0.0.1/24 dev enp0s9 
 
4.3 Configurare IP statico su debian2 
Aprire /etc/network/interfaces e aggiungere: 
 
# Internal network interface (intnet) 
# Static IP for private communication with debian1 
auto enp0s8 
iface enp0s8 inet static 
    address 10.0.0.2 
    netmask 255.255.255.0 
 
Attivare l'interfaccia: 
sudo ip addr add 10.0.0.2/24 dev enp0s8 
 
4.4 Verificare la connettività 
Da debian1: 
ping -c 4 10.0.0.2 
 
⚠️ Nota: Usare sempre sudo con i comandi ip addr add, altrimenti il comando viene 
ignorato silenziosamente. 
 
5. Configurazione MariaDB su debian2 
5.1 Installazione 
sudo apt update && sudo apt install mariadb-server -y 
 
5.2 Accesso iniziale 
sudo mysql 
 
5.3 Sicurezza di base 
-- Remove anonymous users 
DELETE FROM mysql.user WHERE User=''; 
 
-- Disallow root login remotely 
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', 
'127.0.0.1', '::1'); 
 
-- Remove test database 
DROP DATABASE IF EXISTS test; 

 
-- Apply changes 
FLUSH PRIVILEGES; 
 
5.4 Creazione database e utente WordPress 
-- Create the WordPress database 
CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE 
utf8mb4_unicode_ci; 
 
-- Create a dedicated user for WordPress 
-- Access is restricted to debian1's IP on the internal network 
CREATE USER 'wpuser'@'10.0.0.1' IDENTIFIED BY 'its2026'; 
 
-- Grant full privileges on the WordPress database only 
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'10.0.0.1'; 
 
-- Apply changes 
FLUSH PRIVILEGES; 
 
5.5 Configurazione bind-address 
Aprire il file di configurazione: 
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf 
 
Modificare la riga bind-address: 
# bind-address: the IP on which MariaDB listens for incoming connections  
# This is debian2's IP on the internal network (intnet) 
# NOTE: bind-address is NOT the IP of the client connecting to the 
database 
#       The client IP (debian1 = 10.0.0.1) is controlled by user 
privileges instead 
bind-address = 10.0.0.2 
 
Riavviare MariaDB: 
sudo systemctl restart mariadb 
 
Verificare che MariaDB ascolti sull'IP corretto: 
sudo ss -tlnp | grep 3306 
 
Output atteso: 
LISTEN 0  80  10.0.0.2:3306  0.0.0.0:*  users:(("mariadbd",...))  
 
5.6 Test connessione da debian1 
Installare il client MariaDB su debian1: 
sudo apt install mariadb-client -y 

 
Connettersi al database remoto: 
mysql -h 10.0.0.2 -u wpuser -pits2026 wordpress 
 
6. Installazione WordPress su debian1 
6.1 Installazione nginx e PHP 
sudo apt install nginx php8.4-fpm php8.4-mysql php8.4-curl php8.4-gd 
php8.4-mbstring php8.4-xml php8.4-xmlrpc php8.4-zip -y 
 
⚠️ Nota: Non usare il metapacchetto generico 'php' perché installa automaticamente 
Apache2, che va in conflitto con nginx sulla porta 80. 
 
Verificare che entrambi i servizi siano attivi: 
sudo systemctl status nginx 
sudo systemctl status php8.4-fpm 
 
6.2 Download e installazione WordPress 
cd /tmp && sudo wget https://wordpress.org/latest.tar.gz 
sudo tar -xzf /tmp/latest.tar.gz -C /tmp 
sudo mv /tmp/wordpress /var/www/wordpress 
sudo chown -R www-data:www-data /var/www/wordpress 
sudo find /var/www/wordpress -type d -exec chmod 755 {} \; 
sudo find /var/www/wordpress -type f -exec chmod 644 {} \; 
 
6.3 Configurazione /etc/hosts su debian1 
Aggiungere il nome wordpress a /etc/hosts: 
sudo nano /etc/hosts 
 
Aggiungere la riga: 
127.0.0.1   wordpress 
 
6.4 Configurazione nginx 
sudo nano /etc/nginx/sites-available/wordpress 
 
server { 
    listen 80; 
    server_name wordpress; 
 
    root /var/www/wordpress; 
    index index.php index.html; 
 

    # Log files 
    access_log /var/log/nginx/wordpress_access.log; 
    error_log /var/log/nginx/wordpress_error.log; 
 
    # Handle WordPress permalinks 
    location / { 
        try_files $uri $uri/ /index.php?$args; 
    } 
 
    # Pass PHP files to PHP-FPM 
    location ~ \.php$ { 
        include snippets/fastcgi-php.conf; 
        fastcgi_pass unix:/run/php/php8.4-fpm.sock; 
    } 
 
    # Deny access to hidden files 
    location ~ /\. { 
        deny all; 
    } 
} 
 
Abilitare il sito e ricaricare nginx: 
sudo ln -s /etc/nginx/sites-available/wordpress /etc/nginx/sites-
enabled/ 
sudo nginx -t 
sudo systemctl reload nginx 
 
6.5 Configurazione wp-config.php 
sudo cp /var/www/wordpress/wp-config-sample.php /var/www/wordpress/wp-
config.php 
sudo nano /var/www/wordpress/wp-config.php 
 
Modificare questi parametri: 
define( 'DB_NAME',     'wordpress' ); 
define( 'DB_USER',     'wpuser' ); 
define( 'DB_PASSWORD', 'its2026' ); 
define( 'DB_HOST',     '10.0.0.2' );  // debian2 internal IP 
 
7. Accesso SSH a debian2 tramite ProxyJump 
7.1 Comando diretto 
ssh -J its-usr@192.168.56.110 its-usr@10.0.0.2 
 
7.2 Configurazione ~/.ssh/config sull'host 

Aggiungere al file ~/.ssh/config sul proprio PC: 
Host debian1 
    HostName 192.168.56.110 
    User its-usr 
 
Host debian2 
    HostName 10.0.0.2 
    User its-usr 
    ProxyJump debian1 
 
Da questo momento è sufficiente: 
ssh debian2 
 
⚠️ Nota: ProxyJump non è un tunnel SSH. Con ProxyJump SSH apre una sessione su 
debian1 e da lì una nuova connessione SSH verso debian2. Il traffico è cifrato end-to-end. 
Un tunnel SSH (port forwarding) è una cosa diversa. 
 
8. Firewall su debian1 (ufw) 
Configurare ufw per accettare solo SSH (porta 22) e HTTP (porta 80). Tutto il resto in 
entrata viene bloccato. 
 
⚠️ Nota: Le regole 'deny incoming' bloccano solo il traffico in entrata su debian1. Le 
connessioni uscenti (verso MariaDB su debian2 e SSH verso debian2) non sono influenzate. 
 
8.1 Installazione e configurazione 
# Install ufw if not present 
sudo apt install ufw -y 
 
# Default policy: block all incoming, allow all outgoing 
sudo ufw default deny incoming 
sudo ufw default allow outgoing 
 
# Allow SSH 
sudo ufw allow 22/tcp 
 
# Allow HTTP 
sudo ufw allow 80/tcp 
 
# Enable firewall 
sudo ufw enable 
 
# Verify 
sudo ufw status verbose 
 

8.2 Traffico permesso 
Connessione Direzione su debian1 Permessa? 
SSH dall'esterno → debian1 
(porta 22) 
IN Sì 
HTTP dall'esterno → WordPress 
(porta 80) 
IN Sì 
debian1 → MariaDB su debian2 
(porta 3306) 
OUT Sì 
debian1 → SSH su debian2 (porta 
22) 
OUT Sì 
Qualsiasi altra connessione in 
entrata 
IN No — 
bloccata 
 
9. Riepilogo architettura finale 
Componente Macchina Dettaglio 
nginx + WordPress debian1 IP 192.168.56.110 (Solo 
Host) / 10.0.0.1 (intnet) 
PHP-FPM 8.4 debian1 Gestione script PHP 
MariaDB debian2 IP 10.0.0.2 (intnet) — non 
raggiungibile dall'esterno 
Utente DB debian2 wpuser@10.0.0.1 — solo da 
debian1 
SSH esterno debian1 Porta 22, IP 192.168.56.110 
SSH debian2 via debian1 ProxyJump: ssh -J debian1 
debian2 
 


---

# wordpress due macchine

**File:** `wordpress due macchine.pdf`
**Tipo:** `.pdf`
**Dimensione:** 368.8 KB
**Ultima modifica:** 02/07/2026 09:22

---

WordPress su Architettura
a Due Macchine
Guida pratica — Linux Server
ITS Academy

Obiettivo dell'esercitazione
• Mettere in rete due macchine Debian in VirtualBox
• debian1 → frontend: nginx + WordPress (accessibile dall'esterno)
• debian2 → backend: MariaDB (accessibile SOLO da debian1 via rete interna)
• Accesso SSH a debian2 solo tramite debian1 (ProxyJump)
• Scenario realistico: separazione frontend/backend come in produzione

Architettura e configurazione VirtualBox

Configurazione schede di rete (NIC)
Macchina NIC 1 NIC 2 NIC 3
debian1 NAT Solo Host → 
192.168.56.110
Rete interna intnet → 
10.0.0.1
debian2 NAT Rete interna intnet → 
10.0.0.2
—

Clone VM e cambio hostname
• Clonare debian1 in VirtualBox per ottenere debian2
• Durante il clone: rigenerare i MAC address (o farlo manualmente dopo)
• Cambiare hostname su debian2:
• → echo "debian2" | sudo tee /etc/hostname
• → sudo sed -i 's/debian1/debian2/' /etc/hosts
• → sudo hostnamectl set-hostname debian2
Il clone condivide il MAC address originale: rigenerarlo per evitare conflitti DHCP

Configurazione rete interna (intnet)

Interfacce di rete rilevate
Macchina Interfaccia Ruolo
debian1 enp0s3 NAT
debian1 enp0s8 Solo Host
debian1 enp0s9 Rete interna intnet
debian2 enp0s3 NAT
debian2 enp0s8 Rete interna intnet

Configurazione /etc/network/interfaces
# --- debian1: aggiungere in fondo ---
# Internal network interface (intnet)
# Static IP for private communication with debian2
auto enp0s9
iface enp0s9 inet static
address 10.0.0.1
netmask 255.255.255.0
# --- debian2: aggiungere in fondo ---
# Internal network interface (intnet)
# Static IP for private communication with debian1
auto enp0s8
iface enp0s8 inet static
address 10.0.0.2
netmask 255.255.255.0

Attivare le interfacce e testare
# Attivare su debian1 (usare SEMPRE sudo)
sudo ip addr add 10.0.0.1/24 dev enp0s9
# Attivare su debian2
sudo ip addr add 10.0.0.2/24 dev enp0s8
# Verificare la connettività (da debian1)
ping -c 4 10.0.0.2
# Output atteso: 0% packet loss

Configurazione MariaDB su debian2

Installazione e sicurezza di base
# Installazione
sudo apt update && sudo apt install mariadb-server -y
# Accesso
sudo mysql
-- Remove anonymous users
DELETE FROM mysql.user WHERE User='';
-- Disallow root login remotely
DELETE FROM mysql.user WHERE User='root'
AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
FLUSH PRIVILEGES;

Creazione database e utente WordPress
-- Create the WordPress database
CREATE DATABASE wordpress
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Create user restricted to debian1's IP only
CREATE USER 'wpuser'@'10.0.0.1' IDENTIFIED BY 'its2026';
-- Grant privileges only on wordpress DB
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'10.0.0.1';
FLUSH PRIVILEGES;

Configurazione bind-address in 50-server.cnf
# File: /etc/mysql/mariadb.conf.d/50-server.cnf
# bind-address: IP on which MariaDB listens
# This is debian2's IP on the internal network
# NOTE: NOT the client IP — that's controlled by user privileges
bind-address = 10.0.0.2
# Riavviare il servizio
sudo systemctl restart mariadb
# Verificare
sudo ss -tlnp | grep 3306
# Output atteso: LISTEN ... 10.0.0.2:3306

Installazione WordPress su debian1

Installazione nginx e PHP-FPM
# Installare nginx e PHP (NON usare 'php' generico:
# trascina Apache2 che va in conflitto con nginx)
sudo apt install nginx php8.4-fpm php8.4-mysql \
php8.4-curl php8.4-gd php8.4-mbstring \
php8.4-xml php8.4-xmlrpc php8.4-zip -y
# Verificare
sudo systemctl status nginx
sudo systemctl status php8.4-fpm

Download e installazione WordPress
# Download
cd /tmp && sudo wget https://wordpress.org/latest.tar.gz
sudo tar -xzf /tmp/latest.tar.gz -C /tmp
sudo mv /tmp/wordpress /var/www/wordpress
# Permessi
sudo chown -R www-data:www-data /var/www/wordpress
sudo find /var/www/wordpress -type d -exec chmod 755 {} \;
sudo find /var/www/wordpress -type f -exec chmod 644 {} \;
# Aggiungere a /etc/hosts su debian1:
# 127.0.0.1   wordpress

Configurazione nginx — sites-available/wordpress
server {
listen 80;
server_name wordpress;
root /var/www/wordpress;
index index.php index.html;
access_log /var/log/nginx/wordpress_access.log;
error_log  /var/log/nginx/wordpress_error.log;
location / {
try_files $uri $uri/ /index.php?$args;
}
location ~ \.php$ {
include snippets/fastcgi-php.conf;
fastcgi_pass unix:/run/php/php8.4-fpm.sock;
}
location ~ /\. { deny all; }
}

Configurazione wp-config.php
sudo cp /var/www/wordpress/wp-config-sample.php \
/var/www/wordpress/wp-config.php
# Modificare questi parametri:
define( 'DB_NAME',     'wordpress' );
define( 'DB_USER',     'wpuser' );
define( 'DB_PASSWORD', 'its2026' );
# DB_HOST = IP interno di debian2
define( 'DB_HOST',     '10.0.0.2' );

Accesso SSH tramite ProxyJump

SSH ProxyJump — accedere a debian2 dall'esterno
# Comando diretto
ssh -J its-usr@192.168.56.110 its-usr@10.0.0.2
# Oppure configurare ~/.ssh/config sul proprio PC:
Host debian1
HostName 192.168.56.110
User its-usr
Host debian2
HostName 10.0.0.2
User its-usr
ProxyJump debian1
# Da quel momento basta:
ssh debian2

Firewall su debian1 (ufw)

Configurazione firewall con ufw
# Installazione
sudo apt install ufw -y
# Politica default: blocca tutto in entrata, permetti in uscita
sudo ufw default deny incoming
sudo ufw default allow outgoing
# Permetti SSH (porta 22)
sudo ufw allow 22/tcp
# Permetti HTTP (porta 80)
sudo ufw allow 80/tcp
# Attivare e verificare
sudo ufw enable
sudo ufw status verbose

Traffico permesso dopo il firewall
Connessione Direzione Permessa?
SSH dall'esterno → debian1 (porta 
22)
IN Sì
HTTP → WordPress (porta 80) IN Sì
debian1 → MariaDB su debian2 
(3306)
OUT Sì
debian1 → SSH su debian2 (22) OUT Sì
Qualsiasi altra connessione in 
entrata
IN No — bloccata

ProxyJump vs Tunnel SSH — differenza
• ProxyJump: SSH si connette a debian1 e apre una NUOVA connessione SSH verso debian2
• Il traffico è cifrato end-to-end ma NON è un tunnel
• Tunnel SSH (port forwarding): fa forwarding di una porta remota sul PC locale
• → es: ssh -L 3306:10.0.0.2:3306 its-usr@192.168.56.110
• → utile per connettersi al DB con un client grafico dal proprio PC
• Per amministrare debian2 → usare ProxyJump
• Per accedere al DB da client grafico → usare tunnel SSH

Riepilogo architettura finale
Componente Macchina Dettaglio
nginx + WordPress debian1 192.168.56.110 (Solo Host) / 
10.0.0.1 (intnet)
PHP-FPM 8.4 debian1 Gestione script PHP
MariaDB debian2 10.0.0.2 — non raggiungibile 
dall'esterno
Utente DB debian2 wpuser@10.0.0.1 (solo da 
debian1)
SSH esterno debian1 Porta 22, IP 192.168.56.110
SSH debian2 via debian1 ProxyJump: ssh debian2

