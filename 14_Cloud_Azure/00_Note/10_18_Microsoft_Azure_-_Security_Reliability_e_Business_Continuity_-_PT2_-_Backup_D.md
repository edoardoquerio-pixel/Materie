# 18) Microsoft Azure - Security, Reliability e Business Continuity - PT2 - Backup, Disaster Recovery

**File:** `18) Microsoft Azure - Security, Reliability e Business Continuity - PT2 - Backup, Disaster Recovery.pptx`
**Tipo:** `.pptx`
**Dimensione:** 79.9 KB
**Ultima modifica:** 02/07/2026 09:24

---

DOCENTE
Federico Laurianti
UNITÀ FORMATIVA
Microsoft Azure (100 ore)
ARGOMENTO
Security, Reliability e Business Continuity - PT2: Backup, Disaster Recovery e Compliance (4 ore)

---

Backup, Disaster Recovery e Compliance
Far sopravvivere dato e servizio a un guasto, e saperlo dimostrare

---

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

---

Il backup non è solo una copia
•  Fare backup non significa automaticamente poter ripartire bene.
•  Conta cosa proteggi, con quale frequenza e quanto velocemente recuperi.
•  Backup e continuità del servizio vanno letti insieme.
•  Se non sai cosa vuoi recuperare prima, la policy resta astratta.
•  Il punto è progettare il recupero, non solo salvare dati.

---

La logica 3-2-1 nel cloud
•  La regola 3-2-1: più copie, su supporti/livelli diversi, con una separazione reale.
•  Nel cloud la separazione non è solo fisica: può essere logica, operativa, di accesso.
•  Serve a ridurre il rischio di perdita unica o compromissione comune.
•  Va adattata al workload, non applicata come slogan.

---

Retention operativa e storica
Tipo
Scopo
Operativa
recupero veloce dopo errore o incidente comune
Storica
conservazione lunga per audit, analisi o obblighi
•  Le due retention non coincidono quasi mai.
•  Confonderle porta a costi inutili o recuperi insufficienti.

---

Recovery Services Vault e separazione
•  Il Recovery Services Vault è il contenitore Azure per backup e punti di ripristino.
•  Tiene insieme policy di backup, retention e gli elementi protetti.
•  Vault separation: non tutto deve stare nello stesso contenitore operativo.
•  Separare ambienti/workload riduce il blast radius di errori o compromissioni.
•  Anche i permessi diventano più leggibili e meno pericolosi.

---

Restore test e runbook
•  Un backup non testato è solo una promessa.
•  I restore test verificano tempi, dipendenze e integrità del recupero.
•  I runbook evitano di improvvisare durante un incidente.
•  Quando il ripristino coinvolge più servizi, la procedura conta quanto il dato.
•  Qui si vede la differenza tra protezione dichiarata e protezione reale.

---

Dal backup alla continuità: HA vs DR
•  Alta disponibilità (HA) e Disaster Recovery (DR) non sono la stessa cosa.
•  HA: riduce interruzioni locali o limitate (un nodo, un guasto circoscritto).
•  DR: prepara il servizio a eventi gravi e meno frequenti (perdita di una region).
•  Se i due piani si confondono, anche il design resta ambiguo.
•  Distinguere continuità locale da recupero su scala ampia.

---

Availability Set, Zone e Region
Livello
Idea chiave
Availability Set
separazione da fault e update domain (stesso datacenter)
Availability Zone
distribuzione su zone distinte nella stessa region
Region
separazione geografica per eventi più ampi
•  Ogni livello aumenta resilienza, ma anche costo e complessità.
•  La scelta dipende da rischio atteso e criticità del servizio.

---

RPO e RTO
•  RPO (Recovery Point Objective): quanta perdita di dati puoi tollerare.
•  RTO (Recovery Time Objective): in quanto tempo devi tornare operativo.
•  Sono i due numeri guida per decidere architettura e investimento.
•  Senza questi riferimenti, parlare di DR (Disaster Recovery) resta troppo vago.
•  Prima si definisce il requisito, poi si sceglie la tecnologia.

---

Azure Site Recovery
•  Azure Site Recovery (ASR) supporta replica e failover controllato.
•  Porta i workload verso un sito secondario o una region alternativa.
•  Non basta attivarlo: va allineato a dipendenze applicative e dati.
•  È uno strumento, non il piano completo.
•  Il valore emerge quando entra in una strategia coerente.

---

Il failover è una sequenza
•  Un failover serio non sposta solo macchine: muove un servizio intero.
•  Vanno considerati ordine di avvio, dipendenze, DNS, dati e verifiche finali.
•  Se manca una dipendenza critica, il sito secondario non serve davvero.
•  Per questo il piano va scritto, provato e aggiornato.
•  La resilienza dipende dalla sequenza, non solo dalla replica.

---

Scegliere il livello giusto
•  Non ogni servizio richiede architetture multi-region complesse.
•  Per alcuni workload basta alta disponibilità locale ben progettata.
•  Per altri servono replica geografica e piani di ripartenza dettagliati.
•  Il design corretto nasce dall'impatto del fermo sul business.
•  Affidabilità e costo vanno bilanciati con lucidità.

---

Compliance: non basta la checklist
•  La compliance non è spuntare un elenco di controlli: è dimostrare che l'ambiente segue regole e vincoli.
•  In cloud conta la raccolta continua delle evidenze: se la prova manca, anche un buon controllo è difficile da sostenere.
•  È il punto dove governance e operatività si incontrano.

---

Regulatory Compliance in Azure
•  Regulatory Compliance (in Defender for Cloud / Azure Policy) legge requisiti e stato dei controlli.
•  Mostra dove sono i gap e quali evidenze sono disponibili, raggruppati per area (rete, identity, dati…).
•  Non sostituisce il lavoro del team: rende visibile il quadro.
•  Uno standard senza lettura operativa resta teorico.

---

Audit e tracciabilità
•  Audit = ricostruire chi ha fatto cosa e quando.
•  Activity Log e log diagnostici, raccolti in un workspace e interrogabili via Application Insights.
•  Servono quando qualcosa sfugge a design e postura: sono la base del postmortem.
•  Le evidenze vanno conservate in modo coerente e consultabile nel tempo.

---

Sicurezza applicativa: il punto centralizzato
•  La sicurezza è anche come pubblichi l'applicazione, non solo la piattaforma.
•  Un gateway centralizzato come API Management concentra più controlli:
      ○  autenticazione/autorizzazione di chi chiama (subscription key, token/JWT)
      ○  protezione dagli attacchi e rate limiting
      ○  TLS, cifratura e certificati gestiti sul gateway
•  WAF ed endpoint gestiti completano il perimetro: sicuro dentro ma esposto male fuori = fragile.

---

Private Link e pubblicazione controllata
•  Private Link riduce l'esposizione pubblica dei servizi critici (già visto nella lezione di rete).
•  Raggiungi alcune risorse via percorsi privati, senza passare da Internet.
•  Ha molto senso per dati e backend sensibili.
•  Principio: pubblicare meno, controllare meglio.

---

Da portare a casa
•  Il backup serve a ripartire: 3-2-1, retention operativa/storica, vault separation, restore test.
•  HA (alta disponibilità) ≠ DR (Disaster Recovery); RPO/RTO guidano architettura e spesa.
•  Il failover è una sequenza, abilitata da strumenti come ASR (Azure Site Recovery).
•  Compliance = dimostrare la conformità; audit/log = poter fare il postmortem.
•  Sicurezza applicativa con APIM e Private Link: pubblicare meno, controllare meglio.
