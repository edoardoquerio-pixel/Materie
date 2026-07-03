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
