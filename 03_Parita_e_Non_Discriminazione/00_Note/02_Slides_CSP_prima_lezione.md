# Slides CSP prima lezione

**File:** `Slides CSP prima lezione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 437.9 KB
**Ultima modifica:** 02/07/2026 09:11

---

Chi è il Tecnico Superiore System
Administration - Cloud Specialist?
È il professionista responsabile della progettazione, configurazione e manutenzione di infrastrutture
IT complesse, con un focus specifico sugli ambienti Cloud.
Le sue competenze includono:
●Gestione Infrastrutturale:Amministrazione di server (Linux/Windows), reti virtuali e storage.
●Continuità Operativa:Implementazione di strategie di Backup e Disaster Recovery per garantire che i
servizi non si fermino mai.
●Sicurezza e Monitoraggio:Protezione dei sistemi da intrusioni e gestione dei log per la tracciabilità degli
accessi.
● Automazione e Scalabilità:Utilizzo di strumenti per gestire le risorse in modo elastico in base al carico di
lavoro.

Il "Luogo" del Dato e la Sovranità Digitale
●Il paradosso della nuvola:I dati sono virtuali, ma i server sono fisici. Se i dati
sono a Dublino, rispondo alla legge irlandese o italiana?
●Trasferimento transfrontaliero:Conoscere le norme è fondamentale per
decidere in qualeRegionoData Centerconfigurare l'infrastruttura. Una errata
scelta può mettere l’azienda in difficoltà.
● Il rischio del CLOUD Act:Comprendere come le autorità (nazionali ed estere)
possono richiedere l'accesso ai dati che tu amministri.

Non tutto ciò che è installabile è lecito
●La trappola dell'Open Source:"Open" non significa "senza regole". Bisogna
capire le licenze (GPL, Apache, MIT) per evitare che l'azienda perda la proprietà
del p roprio software.
●Software Asset Management:Imparare a gestire le licenze in ambienti
virtualizzati (es. come contare le licenze Windows o Oracle su core virtuali).
●Responsabilità del contenuto:Se un utente carica materiale protetto da
copyright sul tuo storage S3, chi è responsabile? Tu, in quanto amministratore, devi
conoscere le procedure diNotice and Take Down.

Sicurezza Tecnica vs. Conformità Legale
1.GDPR e Privacy:La legge impone la "Data Protection by Design". Voi siete quelli
che devono trasformare l'articolo di legge in una regola di firewall o in unapolicydi
crittografia.
2.Tracciabilità e Log:Sapere cosa conservare e per quanto tempo non è una scelta
tecnica, è un obbligo giuridico.
3. Cyber-resilienza (Direttiva NIS2):Le nuove norme europee impongono standard
minimi di sicurezza per le infrastrutture critiche. Lo specialista Cloud è il primo
responsabile dell'attuazione di questi standard.

Perché questo corso nel tuo curriculum?
Per parlare il linguaggio dell’azienda:Le aziende non cercano chi sa solo "montare
macchine", ma chi sa dialogare con l'ufficio legale e il DPO (Data Protection Officer).
Per proteggersi dai rischi professionali:Conoscere la propria responsabilità penale e
civile come amministratore di sistema è la prima forma di assicurazione professionale.
Valore di Mercato:Un Cloud Specialist che certifica lacompliancedei sistemiè pagato
significativamente di piùrispetto a chi esegue solo comandi da terminale.

Persone fisiche e persone giuridiche
Persona fisica:
Essere umano titolare di diritti e obblighi
Persona giuridica
Ente/società riconosciuta dall’ordinamento.
Nel mondo IT :
software house, sviluppatori, azienda, eventuale cliente, utenti, startup

Società di persone e società di capitali


La Startup
Temporaneità: È una fase iniziale (avviamento) che punta a trasformarsi in una grande
impresa.
Tecnologia: Spesso si basa su tecnologie avanzate (es. IT , digitale).
Innovazione: Introduce novità (di prodotto, processo, modello di business) nel mercato.
Scalabilità: Può crescere esponenzialmente con risorse relativamente limitate.
Replicabilità: Il modello di business può essere replicato in altre situazioni o mercati.
https://www.mimit.gov.it/it/startup-innovative

Il CLOUD Act
ll CLOUD Act trae origine dall’Electronic Communications Privacy Act (ECPA) e dallo Stored
Communications Act (SCA). Queste leggi sono state scritte per un’era pre-cloud e non hanno
chiarito se le richieste dei giudici statunitensi - fatte per ragioni di giustizia o di sicurezza nazionale
- potessero raggiungere i dati memorizzati all’estero.
La questione è diventata decisiva nel caso “Microsoft Ireland”:
●Nel 2013, i pubblici ministeri statunitensi hanno richiesto tramite un mandato SCA e-mail
memorizzate nel data center di Dublino di Microsoft
●Microsoft ha rifiutato, sostenendo che la SCA riguarda solo i dati contenuti all'interno dei
confini degli Stati Uniti
●Nel 2016, una corte d'appello degli Stati Uniti ha dato ragione a Microsoft, stabilendo che il
governo non poteva forzare la divulgazione dei dati memorizzati all'estero
●

Per risolvere il problema “Microsoft Ireland”, il Congresso ha approvato il CLOUD
Act il 23 marzo 2018, che modifica le precedenti leggi in materia in tre modi
chiave:
●Portata extraterritoriale:le autorità statunitensi possono chiedere dati ai
fornitori statunitensi, indipendentemente da dove sono archiviati i dati
●Procedura “Comity” (rispetto reciproco):la legge ha creato un
meccanismo legale che consente ai fornitori di contestare gli ordini di
divulgazione se sono in conflitto con le leggi straniere (es GDPR UE)
●Accordi esecutivi:accordi diretti, governo-governo, che rendono le richieste
di dati transfrontaliere più veloci e più prevedibili.

Fattore Significato
La posizione dei dati
non equivale alla
sicurezza dei dati
L'archiviazione dei dati nell'UE (o in qualsiasi regione non statunitense) non garantisce
la protezione se il fornitore, o un'affiliata controllata dagli Stati Uniti, può accedervi. La
giurisdizione seguechi controlla i dati, nondove si trova.
La portata del
venditore è
importante
Se utilizzi piattaforme cloud, SaaS o di comunicazione basate negli Stati Uniti, devi
sapere che le richieste legali statunitensi valide possono raggiungere i tuoi dati,
indipendentemente dalla posizione di archiviazione.
Conflitti di diritto
operativi
Le organizzazioni dell'UE possono affrontare situazioni in cui il GDPR e la legge CLOUD
si scontrano, andando oltre la protezione del mdello “comity”. Mentre le sfide “comity”
consentono un respingimento limitato, la maggior parte dei casi richiede un’escalation
strutturata e una consulenza legale.
Strategie di
mitigazione
Invece di concentrarsi solo su dove sono ospitati i dati, pensa a chi può accedervi o
decifrarli. Le opzioni includono: utilizzo di fornitori solo dell'UE, chiavi di crittografia
gestite dal cliente, controlli di accesso rigorosi per ridurre l'esposizione dei dati.

3. L'incendio del Data Center OVH a Strasburgo (2021)
●Il fatto:Un enorme incendio ha distrutto uno dei data center di OVHcloud,
causando la perdita definitiva di dati per migliaia di aziende che non avevano un
piano di disaster recovery attivo o contrattualizzato.
●Implicazioni per il Cloud Specialist:Il caso ha sollevato questioni legali enormi
sullaresponsabilità contrattuale. Chi è responsabile se il backup non è incluso
nel contratto base? Lo specialist deve saper leggere le clausole di limitazione della
responsabilità del provider.
●Fonte:Report tecnici di OVHcloud Newsroom
Lavoro di gruppo: debate tra le posizioni di OVHCloud, azienda che ha perso i dati, cloud specialist
