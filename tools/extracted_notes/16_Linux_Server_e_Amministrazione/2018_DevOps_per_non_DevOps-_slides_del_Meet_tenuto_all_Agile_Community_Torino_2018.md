# DevOps per non DevOps- slides del Meet tenuto all'Agile Community Torino, 2018

Fonte: `DevOps per non DevOps- slides del Meet tenuto all'Agile Community Torino, 2018.pdf`

+Agile meetup | 5 Dicembre: 
INTRODUZIONE A DEVOPS 
PER NON DEVOPS

IN COLLABORAZIONE CON

© 2018 DropletBENVENUTI! 
Siamo 

WOLFGANG CECCHIN 

SOCIO FONDATORE DI DROPLET* 

MARCO BOZZOLAN, 

GESTORE SISTEMI DROPLET*

*DROPLET SI OCCUPA DI 

e-commerce 
e digital 
experience 
dal 2003.

© 2018 Droplet 2 
 
SUMMARY: 

COME ARRIVIAMO A DEVOPS?, 

WOLFGANG CECCHIN 

DEVOPS DEMO, 

MARCO BOZZOLAN 

CONSIDERAZIONI FINALI 

© 2018 Droplet 3 
 
DEVOPS:  

Quali sono gli 

SCENARI ?

© 2018 Droplet 4 
SCENARI… 

DEV OPS

:
-
(

© 2018 Droplet 5DEV

WORSE SCENARIO 

OPS

© 2018 Droplet 6N
E
V
E

WORSE SCENARIO 

DEV

VS.

OPS

VS.
VS.
Mr. BUSINESS

© 2018 Droplet 7MA 
COME ARRIVIAMO A 
DEVOPS?, 

© 2018 Droplet 8FACCIAMO UN 

REWIND 

RIAVVOLGIAMO IL NASTRO… 

© 2018 Droplet 
 
 
 
 
…E FACCIAMO 
QUALCHE 
PASSO 
INDIETRO…

© 2018 Droplet© 2018 DropletMMM… 
LO ABBIAMO RIAVVOLTO 
TROPPO :-)

© 2018 DropletRIAVVOLGIAMO IL NASTRO: 

OK, FERMIAMOCI UN PÒ PRIMA E PARLIAMO DI “STORIA” E DI 

OPERATIONS 

© 2018 Droplet 
RIAVVOLGIAMO IL NASTRO: 
OPS 

L’ETÀ DEL FERRO 

PRIMA DEL 2001 D.C. 

© 2018 Droplet 14 
ETÀ “DEL FERRO” 

“BARE METAL” 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 15 
OPS 

ETÀ DEL FERRO 

“BARE METAL” 

AMBIENTI: 
• Dev; 

• CQ (AKA “Test", “System Test”, “Pre-prod”, “Gold”, 

“Staging”); 

• Produzione.

© 2018 Droplet 16 
OPS 

ETÀ DEL FERRO 

“BARE METAL” 

RIDONDANZA E SCALING: 
• Raid (ridondanza sui dischi); 

• Macchine di backup (cloni); 

• Cluster; 

• …

© 2018 Droplet 17 
OPS 

ETÀ DEL FERRO 

“BARE METAL” 

E SE QUALCOSA SI SPACCA? 
Repeat again and again:

:
-
(

Assemblaggio hardware; 

• Installazione sistema operativo; 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 18 
RIAVVOLGIAMO IL NASTRO: 
OPS 

L’ETÀ DEL FERRO 

PRIMA DEL 2001 D.C. 

L’ETÀ DELLE 
VIRTUAL MACHINES 

DAL 2001 D.C. 

© 2018 Droplet 19 
ETÀ DELLE VIRTUAL 
MACHINES 

OPS 

L’INFRASTRUTTURA

© 2018 Droplet 20 
 ETÀ DEL FERRO 

“BARE METAL” 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 21 
ETÀ DELLE VIRTUAL 
MACHINES 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; +allocazione risorse; 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 22 
OPS 

ETÀ DELLE VIRTUAL 
MACHINES 

VANTAGGI: 
• Le VM si clonano (CQ, Dev, PROD) e si spostano; 

• Le risorse delle VM si possono aumentare con pochi click.

© 2018 Droplet 23 
OPS 

ETÀ DELLE VIRTUAL 
MACHINES 

SVANTAGGI: 
• Devono essere allocate delle risorse hardware ad hoc.

© 2018 Droplet 24 
OPS 

ETÀ DELLE VIRTUAL 
MACHINES 

PRODOTTI PRINCIPALI: 
• VMWare ESX(i) Server; 

• KVM; 

• Oracle Virtual Box; 

• Menzione speciale: Vagrant (2010); 

© 2018 Droplet 25 
RIAVVOLGIAMO IL NASTRO: 
OPS 

L’ETÀ DEL FERRO 

PRIMA DEL 2001 D.C. 

L’ETÀ DELLE VIRTUAL MACHINES 

DAL DEL 2001 D.C. 

L’ETÀ DEI  
CONTAINER 

DAL 2008 D.C. 

© 2018 Droplet 26 
 
 
ETÀ DEI CONTAINER 

OPS 

COSA CAMBIA?

© 2018 Droplet 27 
 ETÀ DELLE VIRTUAL 
MACHINES 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; +allocazione risorse 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 28 
ETÀ DEI CONTAINER 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; +allocazione risorse 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 29 
ETÀ DEI CONTAINER 

OPS 

VANTAGGI: 
• I container si clonano (Dev, CQ, PROD) e si spostano; 

• Le risorse si possono aumentare con pochi click; 

• L’allocazione delle risorse è dinamica; 

• Non devo occuparmi del sistema operativo sottostante; 

• Ospitano “piccole porzioni” di software.

© 2018 Droplet 30 
ETÀ DEI CONTAINER 

OPS 

MA… 
• Devo occuparmi del software all’interno del Container.

© 2018 Droplet 31 
ETÀ DEI CONTAINER 

OPS 

PRODUTTORI: 
• Linux LXC (2008); 

• Docker (2013).

ORCHESTRATORI DI CONTAINER: 
• OpenStack; 

• Kubernetes.

© 2018 Droplet 32 
RIAVVOLGIAMO IL NASTRO: 
OPS 

L’ETÀ DEL FERRO 
PRIMA DEL 2001 D.C. 

L’ETÀ DELLE VIRTUAL MACHINES 
DAL DEL 2001 D.C. 

L’ETÀ DEI CONTAINERS 
DAL DEL 2008 D.C. 

CONFIGURATION 
MANAGEMENT SYSTEM 
DAL 2006 D.C. (CIRCA) 

© 2018 Droplet 33 
 
 
 
 ETÀ DEI CONTAINER 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; +allocazione risorse 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 34 
CONFIGURATION 
MANAGEMENT SYSTEM 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; +allocazione risorse; 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 35 
CONFIGURATION 
MANAGEMENT SYSTEM 

OPS 

VENDORS:  

• Puppet; 

• Ansible; 

• Chef; 

• Terraform; 

• Salt;

• Cloudformation.

© 2018 Droplet 36 
RIAVVOLGIAMO IL NASTRO: 
OPS 

L’ETÀ DEL FERRO 
PRIMA DEL 2001 D.C. 

L’ETÀ DELLE VIRTUAL MACHINES 
DAL DEL 2001 D.C. 

L’ETÀ DEI CONTAINERS 
DAL DEL 2008 D.C. 

L’ETÀ DEL CMS 
DAL DEL 2006 D.C. 

L’ETA DEL CLOUD 

DAL 2006 D.C. 

© 2018 Droplet 37 
 
 
 
 
 CONFIGURATION 
MANAGEMENT SYSTEM 

OPS 

OPERAZIONI SUI SERVER: 
• Assemblaggio hardware; 

• Installazione sistema operativo; +allocazione risorse; 

• Installazione e conﬁgurazione software accessori (utenti, librerie); 

• Installazione e conﬁgurazione del software sviluppato.

© 2018 Droplet 38 
ETÀ DEL CLOUD 

OPS 

CHE COSA RIMANE DA FARE?

© 2018 Droplet 39 
ETÀ DEL CLOUD 

OPS 

NON VOGLIAMO PIÙ DIPENDERE DAL FERRO; 

VOGLIAMO FARE TUTTO QUELLO CHE 
ABBIAMO DETTO FINORA, 
MAN MANO CHE NE ABBIAMO BISOGNO: 

VOGLIAMO AMBIENTI CLOUD “SCALABILI”.

© 2018 Droplet 40 
 
ETÀ DEL CLOUD 

OPS 

VENDORS: 

• Amazon AWS - EC2: Elastic Compute Cloud; 

• Google Cloud Platform; 

• Microsoft Azure; 

• SoftLayer.

© 2018 Droplet 41 
OPS 

ETÀ DEL CLOUD 

EVERYTHING AS SERVICE (EASS) 

• SaaS (Software as Service); 

• PaaS (Platform as Service); 

• IaaS (Infrastructure as Service).

© 2018 Droplet 42 
RIAVVOLGIAMO IL NASTRO: 
OPS 

L’ETÀ DEL FERRO 
PRIMA DEL 2001 D.C. 

L’ETÀ DELLE VIRTUAL MACHINES 
DAL DEL 2001 D.C. 

L’ETÀ DEI CONTAINERS 
DAL DEL 2008 D.C. 

L’ETÀ DEL CMS 
DAL DEL 2006 D.C. 

L’ETÀ DEL CLOUD 
DAL DEL 2015 D.C. 

SERVERLESS 

© 2018 Droplet 43 
 
 
 
 
 
SERVERLESS (LAMBDA) 

OPS 

VOGLIAMO CHE IL CODICE SI ATTIVI IN BASE A 
DETERMINATI EVENTI 

OVVERO 

VOGLIAMO PAGARE SOLO QUELLO CHE USIAMO 
VERAMENTE.

© 2018 Droplet 44 
 
 
SERVERLESS (LAMBDA) 

OPS 

VENDORS: 
VENDORS: 

• Amazon Lambda; 
• Amazon Lambda; 

• Google Cloud Functions; 
• Google Cloud Functions; 

• Azure Functions.
• Azure Functions.

© 2018 Droplet 45 
RIAVVOLGIAMO IL NASTRO: 

OK, ORA L’ALTRA FACCIA DELLA MEDAGLIA. PARLIAMO DI 

DEVELOPERS 

© 2018 Droplet 
RIAVVOLGIAMO IL NASTRO: 
DEV 

BEST PRACTICES: 
• VERSIONAMENTO DEL CODICE.

© 2018 Droplet 47DEV 

BEST PRACTICES 

VERSIONAMENTO DEL CODICE 

VANTAGGI: 
• Se sbaglio, posso ritornare facilmente alla versione precedente; 

• Sviluppo in team: risoluzione dei conﬂitti; 

• Tracking: so chi ha inserito una speciﬁca modiﬁca e perché; 

• Communicate in code.

© 2018 Droplet 48 
DEV 

BEST PRACTICES 

VERSIONAMENTO DEL CODICE 

PRODOTTI: 

GESTORI: 

• CVS; 

• Apache SVN (dal 2000); 

• Mercurial; 

• Git.

MICROSOFT GITHUB, 
GITLAB, 
RHODECODE, 
ATLASSIAN BITBUCKET.

© 2018 Droplet 49 
 
 
RIAVVOLGIAMO IL NASTRO: 
DEV 

- BEST PRACTICES 
- VERSIONAMENTO DEL CODICE 

SVILUPPO BASATO 
SUI TEST 

© 2018 Droplet 50 
 
SVILUPPO BASATO SUI 
TEST 

DEV 

KENT BECK,  
EXTREME PROGRAMMING 
EXPLAINED, 
1999.

© 2018 Droplet 51 
DEV 

SVILUPPO BASATO 
SUI TEST 

• Scrivo il test; 

• Eseguo il test, che non deve passare; 

• Scrivo il codice; 

• Eseguo il test, che passa; 

• Modiﬁco il codice.

© 2018 Droplet 52DEV 

SVILUPPO BASATO SUI 
TEST 

METODOLOGIE DI TEST: 

TIPI DI TEST: 

• Acceptance Test Driven Development; 

• Test Driven Development; 

• Behaviour Driven Development. 

• Acceptance Tests; 

• Unit Testing; 

• Functional Tests / Integration 

Tests.

© 2018 Droplet 53 
DEV 

SVILUPPO BASATO SUI 
TEST 

STRUMENTI OPER UNIT TESTING: 
• JUnit; 

• PHPUnit; 

• Nose; 

• Live Unit Testing.

© 2018 Droplet 54 
SVILUPPO BASATO SUI 
TEST 

DEV 

SOFTWARE: 
• Jenkins; 

• Travis CI; 

• GoCD; 

• Concourse.

© 2018 Droplet 55 
RIAVVOLGIAMO IL NASTRO: 
DEV 

- BEST PRACTICES 
- VERSIONAMENTO DEL CODICE 
- SVILUPPO BASATO SUI TEST 

SVILUPPO BASATO 
SUI MISCROSERVIZI 

© 2018 Droplet 56 
 
SVILUPPO BASATO SUI 
MICROSERVIZI 

DEV 

AJAX (2005) E 
JQUERY (2006)

E poi… 

Angular,js 
React.js 
Vue.js

© 2018 Droplet 57 
 
SVILUPPO BASATO SUI 
MICROSERVIZI 

PROGRAMMAZIONE FUNZIONALE E LAMBDA 
(REACTIVE MANIFESTO - 2014) 

DEV 

© 2018 Droplet 58 
RIAVVOLGIAMO IL NASTRO: 
DEV 

- VERSIONAMENTO DEL CODICE 
- SVILUPPO BASATO SUI TEST 
- SVILUPPO BASATO SUI MICROSERVIZI 

MENO DOCUMENTAZIONE, 
PIÙ CODICE 

© 2018 Droplet 59 
 
LA DOCUMENTAZIONE 
DEVE MORIRE 

DEV 

ROBERT MARTIN,  
CLEAN CODE, 
2004.

© 2018 Droplet 60 
DEVOPS? 

FINALMENTE!

© 2018 Droplet 
UN NUOVO SCENARIO 

© 2018 Droplet 62DEVOPS? 

AUTOMATION: CONTINUOS INTEGRATION + CONTINUOS DELIVERY

© 2018 Droplet 63 
 
DEVOPS? 

WITH TOOLS

© 2018 Droplet 64 
DEVOPS? 

AUTOMATION: CONTINUOUS INTEGRATION + CONTINUOUS DELIVERY

© 2018 Droplet 65 
 
DEVOPS? 

• Plan: Dev + Ops. Si ipotizza un piano e si scelgono le metriche. 

• Create: Sviluppo basato sui test; 

• Verify: Test automatici; 

• Package: Artifacts; 

• Release: Deploy in Sviluppo o in Produzione; 

• Conﬁgure: Conﬁguration Management System; 

• Monitor: KPI Systems + Business,

© 2018 Droplet 66 
DEVOPS 

MONITORING? 

INSPECT AND ADAPT 

DASHBOARD DI PERFORMANCES 
Sistemi (Prometheus, Collectd, Graphite) 
+ Business 
+ Analytics.

© 2018 Droplet 67 
 
PIPELINES 

LE PIPELINES CONSENTONO DI 
AUTOMATIZZARE I PROCESSI 
DEVOPS.

DEVOPS 

© 2018 Droplet 68 
DEVOPS

IT’S DEMO TIME!

CON MARCO 

NOW LIVE!

© 2018 Droplet 69DEVOPS 

COSA VEDREMO OGGI?? 

• Plan; 

• Create: Source control - Git + Rhodecode; 

• Verify: Test automatici - Jenkins; 

• Package: Container; 

• Release: Deploy in Sviluppo o in Produzione - Jenkins; 

• Conﬁgure: Infrastruttura come codice - Ansible; 

• Monitor.

© 2018 Droplet 70 
CAVEAT! 

© 2018 DropletCAVEAT! 

•DevOps non è un’etichetta;

© 2018 Droplet 72CAVEAT! 

•DevOps non è un’etichetta; 

•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management;

© 2018 Droplet 73CAVEAT! 

•DevOps non è un’etichetta; 

•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 

•DevOps non è un insieme di strumenti;

© 2018 Droplet 74CAVEAT! 

•DevOps non è un’etichetta; 

•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 

•DevOps non è un insieme di strumenti; 

•DevOps non è una bacchetta magica;

© 2018 Droplet 75CAVEAT! 

•DevOps non è un’etichetta; 

•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 

•DevOps non è un insieme di strumenti; 

•DevOps non è una bacchetta magica; 

•DevOps non è DevOps(TM);

© 2018 Droplet 76CAVEAT! 

•DevOps non è un’etichetta; 

•DevOps non si può calare dall'alto, 
né far emergere dal basso senza appoggio dal management; 

•DevOps non è un insieme di strumenti; 

•DevOps non è una bacchetta magica; 

•DevOps non è DevOps(TM); 

•DevOps non “ﬁnisce”.

© 2018 Droplet 77DEVOPS? 

BONUS TRACK 

© 2018 Droplet 
COME PORTARE 
DEVOPS 
IN AZIENDA

DEVOPS 

MA ABBIAMO SEMPRE 

FATTO COSI’ PERCHE’ADESSO 

DOBBIAMO CAMBIARE? 

QUANDO L’AMBIENTE 
“REMA NATURALMENTE CONTRO” 

© 2018 Droplet 79 
UNA 
MEZZA 
IDEA 
L’AVREI!

© 2018 Droplet 80MMM.. 
NON ANCORA 
BRUCE… 
PROVIAMO CON 
LARMAN

© 2018 Droplet 81“Culture follows 

structure

- Craig Larman -

© 2018 Droplet 82DEVOPS 

LA STRUTTURA DETERMINA LA 
CULTURA

QUARTA LEGGE DI LARMAN: 

Larman’s Laws of Organizational Behavior observes that… 

1.Organizations are implicitly optimized to avoid changing the status quo middle- and ﬁrstlevel manager and single-specialist positions & power structures. 

2.As a corollary to (1), any change initiative will be reduced to redeﬁning or overloading the 
new terminology to mean basically the same as status quo. 

3.As a corollary to (1), any change initiative will be derided as “purist”, “theoretical”, and 
“needing pragmatic customization for local concerns”—which deﬂects from addressing 
weaknesses and manager/specialist status quo. 

4.Culture follows structure. 

Craig Larman

© 2018 Droplet 83LA STRUTTURA 
DETERMINA LA CULTURA
QUARTA LEGGE DI LARMAN: 

DEVOPS 

The systems-thinking thought-leader John Seddon explains 

this way: 

“culture follows structure” 

Attempting to change an organization’s culture is a folly, it always fails. Peoples’ 
behavior (the culture) is a product of the system; when you change the system 
peoples’ behavior changes. 

© 2018 Droplet 84 
CAMBIA GLI STRUMENTI 
CHE HAI IN MANO

DEVOPS 

Stewart Brand lo riassunse nel modo migliore: 

«Puoi provare a cambiare la testa della gente, ma stai solo 
perdendo tempo. Cambia gli strumenti che hanno in mano, 
e cambierai il mondo». 

Alessandro Baricco, The Game, 2018. 

Steward Brand, The Next Whole Earth Catalog: Access to 
Tools, 1968 

© 2018 Droplet 85 
© 2018 Droplet 86“GRAZIE*
“

*un grazie speciale a CORVALLIS per l’ospitalità

© 2018 Droplet 87