# Consegna Esercitazione doc

Fonte: `Consegna Esercitazione doc.pdf`

ITS ICT Piemonte — Linux Server 

ESERCITAZIONE 
Diagnostica e messa in sicurezza di un'infrastruttura WordPress 

Docente: Wolfgang Cecchin 

Scenario 

L'azienda Acme S.r.l. ha commissionato a un fornitore esterno la realizzazione del proprio sito 
web WordPress, ospitato su un'infrastruttura a due macchine virtuali Debian: 

Macchina 

Ruolo 

Rete 

debian3 

Frontend — nginx + WordPress + PHPFPM 

Solo Host + rete interna 

debian4 

Backend — MariaDB 

Solo rete interna 

Le due macchine comunicano attraverso una rete interna privata (intnet, rete 10.0.0.0/24). Il 
sito WordPress su debian3 si collega al database MariaDB su debian4 tramite questa rete. 

Al momento della consegna, l'azienda Acme scopre che il sito non funziona e che 
l'infrastruttura presenta diversi problemi di configurazione. L'azienda vi incarica di intervenire. 

Informazioni di accesso 

Dettagli 

debian3 

debian4 

Username 

Password 

SSH dalla macchina Windows, porta 2222, autenticazione con 
username e password 

Non raggiungibile via SSH. Accesso esclusivamente dalla console 
VirtualBox (equivalente all'accesso fisico in sala server) 

its-usr 

Its2026 

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

Pagina 1 

 
 
 
ITS ICT Piemonte — Linux Server 

Per visualizzare il sito dal browser Windows, aggiungere una riga nel file 
C:\Windows\System32\drivers\etc\hosts: 

192.168.56.111 acme.local 

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

Pagina 2