# Lezione 18

## Panoramica
Security, Reliability e Business Continuity - PT2: Backup, Disaster Recovery e Compliance (4 ore)

## Argomenti trattati
Azure, Cloud, Reti, API REST, Sicurezza

---
## Appunti

### Slide 1
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
Security, Reliability e Business Continuity - PT2: Backup, Disaster Recovery e Compliance (4 ore)
### Slide 2
Backup, Disaster Recovery e Compliance
Far sopravvivere dato e servizio a un guasto, e saperlo dimostrare
### Slide 3
Argomenti (4 ore)
•  Il backup non è solo una copia: progettare il recupero
•  La logica 3-2-1 applicata al cloud
•  Retention operativa e storica
•  Recovery Services Vault e separazione dei vault
•  Restore test e runbook: protezione reale vs dichiarata
•  Alta disponibilità vs Disaster Recovery
•  Availability Set / Zone / Region, RPO/RTO (Recovery Point/Time Objective), Azure Site Recovery
•  Il failover come sequenza, non solo replica
•  Compliance e audit: dimostrare la conformità e poter fare il postmortem
•  Sicurezza applicativa (API Management) e Private Link
### Slide 4
Il backup non è solo una copia
•  Fare backup non significa automaticamente poter ripartire bene.
•  Conta cosa proteggi, con quale frequenza e quanto velocemente recuperi.
•  Backup e continuità del servizio vanno letti insieme.
•  Se non sai cosa vuoi recuperare prima, la policy resta astratta.
•  Il punto è progettare il recupero, non solo salvare dati.
### Slide 5
La logica 3-2-1 nel cloud
•  La regola 3-2-1: più copie, su supporti/livelli diversi, con una separazione reale.
•  Nel cloud la separazione non è solo fisica: può essere logica, operativa, di accesso.
•  Serve a ridurre il rischio di perdita unica o compromissione comune.
•  Va adattata al workload, non applicata come slogan.
### Slide 6
Retention operativa e storica
recupero veloce dopo errore o incidente comune
conservazione lunga per audit, analisi o obblighi
•  Le due retention non coincidono quasi mai.
•  Confonderle porta a costi inutili o recuperi insufficienti.
### Slide 7
Recovery Services Vault e separazione
•  Il Recovery Services Vault è il contenitore Azure per backup e punti di ripristino.
•  Tiene insieme policy di backup, retention e gli elementi protetti.
•  Vault separation: non tutto deve stare nello stesso contenitore operativo.
•  Separare ambienti/workload riduce il blast radius di errori o compromissioni.
•  Anche i permessi diventano più leggibili e meno pericolosi.
### Slide 8
Restore test e runbook
•  Un backup non testato è solo una promessa.
•  I restore test verificano tempi, dipendenze e integrità del recupero.
•  I runbook evitano di improvvisare durante un incidente.
•  Quando il ripristino coinvolge più servizi, la procedura conta quanto il dato.
•  Qui si vede la differenza tra protezione dichiarata e protezione reale.
### Slide 9
Dal backup alla continuità: HA vs DR
•  Alta disponibilità (HA) e Disaster Recovery (DR) non sono la stessa cosa.
•  HA: riduce interruzioni locali o limitate (un nodo, un guasto circoscritto).
•  DR: prepara il servizio a eventi gravi e meno frequenti (perdita di una region).
•  Se i due piani si confondono, anche il design resta ambiguo.
•  Distinguere continuità locale da recupero su scala ampia.
### Slide 10
Availability Set, Zone e Region
Availability Set
separazione da fault e update domain (stesso datacenter)
Availability Zone
distribuzione su zone distinte nella stessa region
separazione geografica per eventi più ampi
•  Ogni livello aumenta resilienza, ma anche costo e complessità.
•  La scelta dipende da rischio atteso e criticità del servizio.
### Slide 11
•  RPO (Recovery Point Objective): quanta perdita di dati puoi tollerare.
•  RTO (Recovery Time Objective): in quanto tempo devi tornare operativo.
•  Sono i due numeri guida per decidere architettura e investimento.
•  Senza questi riferimenti, parlare di DR (Disaster Recovery) resta troppo vago.
•  Prima si definisce il requisito, poi si sceglie la tecnologia.
### Slide 12
Azure Site Recovery
•  Azure Site Recovery (ASR) supporta replica e failover controllato.
•  Porta i workload verso un sito secondario o una region alternativa.
•  Non basta attivarlo: va allineato a dipendenze applicative e dati.

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 018_18_Microsoft_Azure_-_Security_Reliability_e_Business_Continuity_-_PT2_-_Backup_D.md*
