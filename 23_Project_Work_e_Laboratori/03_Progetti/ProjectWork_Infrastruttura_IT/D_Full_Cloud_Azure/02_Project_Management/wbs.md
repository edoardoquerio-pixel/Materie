# WBS — Work Breakdown Structure

## Progetto: Integrazione Infrastruttura IT TP Group (Thema Consulting + Pro Studio)

| Campo | Valore |
|---|---|
| **Documento** | WBS — Work Breakdown Structure |
| **Versione** | 1.0 |
| **Data** | Giugno 2026 |
| **Redatto da** | PM (Project Manager) |
| **Durata progetto** | 12 settimane attive |
| **Risorse** | Sistemista (€500/gg) + Project Manager (€650/gg) |
| **Budget manodopera** | ~€181.000 |

---

## Struttura WBS

Le attività sono codificate con numerazione gerarchica a 3 livelli.  
La stima effort è espressa in **giorni uomo (gg)**.

---

### 1.0 Project Management (18 gg)

#### 1.1 Pianificazione di progetto (5 gg)
- 1.1.1 Definizione WBS, cronoprogramma e milestone (2 gg)
- 1.1.2 Piano di comunicazione e reporting (1,5 gg)
- 1.1.3 Piano di qualità, risk management e RASCI (1,5 gg)

#### 1.2 Coordinamento e controllo (9 gg)
- 1.2.1 Riunioni di coordinamento settimanali (4 gg)
- 1.2.2 Monitoraggio avanzamento e gestione deliverable (3 gg)
- 1.2.3 Gestione variazioni, rischi e issue tracking (2 gg)

#### 1.3 Chiusura di progetto (4 gg)
- 1.3.1 Consuntivazione finale e lesson learned (2 gg)
- 1.3.2 Certificazione consegne e verbale di collaudo (1,5 gg)
- 1.3.3 Chiusura amministrativa e archiviazione documenti (0,5 gg)

---

### 2.0 Assessment e Analisi (18 gg)

#### 2.1 Assessment infrastruttura esistente (9 gg)
- 2.1.1 Rilevazione rete locale Thema Consulting (2 gg)
- 2.1.2 Rilevazione server fisici, virtualizzazione e Samba4 AD (2 gg)
- 2.1.3 Rilevazione storage (SAN NetApp), backup (NAS QNAP) e DR (2 gg)
- 2.1.4 Rilevazione servizi cloud Pro Studio (GCP, Workspace, Odoo, MediaWiki) (2 gg)
- 2.1.5 Rilevazione applicazione Pondus (C#, MS SQL, IIS) (1 gg)

#### 2.2 Analisi dei requisiti (5 gg)
- 2.2.1 Requisiti di connettività (VPN LAN-to-LAN, Client-to-LAN, hybrid cloud) (1,5 gg)
- 2.2.2 Requisiti cluster HPC (espansione +8 nodi, InfiniBand) (1,5 gg)
- 2.2.3 Requisiti sicurezza e conformità ISO/IEC 27001 (1 gg)
- 2.2.4 Requisiti business continuity e disaster recovery (1 gg)

#### 2.3 Gap analysis (4 gg)
- 2.3.1 Confronto stato attuale vs architettura target (2 gg)
- 2.3.2 Stima effort, risorse e costi necessari (1 gg)
- 2.3.3 Analisi rischi preliminare e mitigazioni (1 gg)

---

### 3.0 Progettazione (22 gg)

#### 3.1 Progettazione architettura di rete (6 gg)
- 3.1.1 Progettazione topologia rete convergente (2 gg)
- 3.1.2 Schema IP, subnetting e VLAN (1,5 gg)
- 3.1.3 Progettazione VPN (LAN-to-LAN, Client-to-LAN, hybrid cloud) (2 gg)
- 3.1.4 Progettazione ridondanza collegamenti e failover (0,5 gg)

#### 3.2 Progettazione cluster HPC (6 gg)
- 3.2.1 Specifica tecnica nodi di calcolo (CPU, RAM, scratch) (2 gg)
- 3.2.2 Architettura rete InfiniBand 100/200 Gbps (2 gg)
- 3.2.3 Schema storage scratch per nodo e condivisione dati (1 gg)
- 3.2.4 Piano di espansione in fasi (fase 1: +4 nodi, fase 2: +4 nodi) (1 gg)

#### 3.3 Progettazione sicurezza e conformità (6 gg)
- 3.3.1 Piano di adeguamento ISO/IEC 27001 — gap analysis formale (2 gg)
- 3.3.2 Policy di sicurezza: accessi, crittografia, protocolli sicuri (1,5 gg)
- 3.3.3 Piano di disaster recovery: RPO/RTO, delocalizzazione, failover (1,5 gg)
- 3.3.4 Matrice crittografia per sistema (dati a riposo, in transito) (1 gg)

#### 3.4 Progettazione migrazione cloud ibrido (4 gg)
- 3.4.1 Definizione strategia hybrid cloud (on-premise + GCP) (1,5 gg)
- 3.4.2 Architettura servizi cloud: identità, backup, networking (1,5 gg)
- 3.4.3 Piano di migrazione servizi e cronologia delle fasi (1 gg)

---

### 4.0 Approvvigionamento HW/SW (10 gg)

#### 4.1 Definizione specifiche e capitolati (3 gg)
- 4.1.1 Capitolato tecnico nodi HPC (CPU, RAM, storage, InfiniBand) (1 gg)
- 4.1.2 Capitolato apparati di rete attivi (switch, firewall, transceiver) (1 gg)
- 4.1.3 Capitolato storage backup e server aggiuntivi (1 gg)

#### 4.2 Richiesta preventivi e selezione fornitori (4 gg)
- 4.2.1 Richiesta offerte a fornitori qualificati (1 gg)
- 4.2.2 Valutazione tecnico-economica delle offerte pervenute (1,5 gg)
- 4.2.3 Negoziazione e aggiudicazione fornitori (1,5 gg)

#### 4.3 Gestione ordini e logistica (3 gg)
- 4.3.1 Emissione ordini e contratti di fornitura (1 gg)
- 4.3.2 Coordinamento trasporto e ricevimento merci (1 gg)
- 4.3.3 Verifica conformità materiali e documentazione fornitori (1 gg)

---

### 5.0 Configurazione e Implementazione (36 gg)

#### 5.1 Configurazione rete e VPN (10 gg)
- 5.1.1 Configurazione firewall Fortigate (regole, NAT, VPN) (2 gg)
- 5.1.2 Configurazione switch di rete, VLAN e trunking (2 gg)
- 5.1.3 Configurazione VPN LAN-to-LAN (sede Thema ↔ cloud Pro Studio) (2,5 gg)
- 5.1.4 Configurazione VPN Client-to-LAN (remoti e collaboratori) (1,5 gg)
- 5.1.5 Configurazione hybrid cloud connectivity (GCP VPN interconnect) (2 gg)

#### 5.2 Configurazione server e virtualizzazione (6 gg)
- 5.2.1 Setup hypervisor e nodi di virtualizzazione (2 gg)
- 5.2.2 Configurazione Active Directory Samba4 integrato (2 gg)
- 5.2.3 Configurazione servizi di base (DNS, DHCP, NTP, certificati) (2 gg)

#### 5.3 Implementazione cluster HPC (10 gg)
- 5.3.1 Rack, cablaggio e installazione fisica nodi HPC (2 gg)
- 5.3.2 Installazione e configurazione rete InfiniBand (switch, schede HCA, driver) (2,5 gg)
- 5.3.3 Installazione e configurazione OS Linux (nodi compute + front-end) (2 gg)
- 5.3.4 Configurazione scheduler job (SLURM) e gestione code (2 gg)
- 5.3.5 Benchmark performance iniziali e validazione (1,5 gg)

#### 5.4 Configurazione storage e backup (5 gg)
- 5.4.1 Configurazione storage primario SAN NetApp (LUN, volumes, export) (1,5 gg)
- 5.4.2 Configurazione NAS QNAP per backup on-premise (1 gg)
- 5.4.3 Configurazione backup su cloud GCP (Veeam / native tool) (1,5 gg)
- 5.4.4 Configurazione policy di retention, scheduling e alerting (1 gg)

#### 5.5 Implementazione sicurezza e hardening (5 gg)
- 5.5.1 Configurazione crittografia dati a riposo (storage, server, DB) (1,5 gg)
- 5.5.2 Configurazione protocolli sicuri (TLS 1.3, SSH key-only, HTTPS) (1,5 gg)
- 5.5.3 Hardening server Linux e Windows (baseline CIS) (1 gg)
- 5.5.4 Implementazione logging centralizzato e monitoring (1 gg)

---

### 6.0 Migrazione (15 gg)

#### 6.1 Migrazione servizi cloud (6 gg)
- 6.1.1 Migrazione posta elettronica e Google Workspace (2 gg)
- 6.1.2 Migrazione file server e dati condivisi (Google Drive → NAS/SAN) (2 gg)
- 6.1.3 Migrazione Odoo e riconfigurazione connettività SaaS (2 gg)

#### 6.2 Migrazione identità e accessi (4 gg)
- 6.2.1 Integrazione Active Directory Samba4 con Google Workspace (sync) (1,5 gg)
- 6.2.2 Migrazione utenti, gruppi e policy di accesso (1 gg)
- 6.2.3 Configurazione SSO e autenticazione multifattore (MFA) (1,5 gg)

#### 6.3 Trasferimento dati e riconfigurazione client (5 gg)
- 6.3.1 Migrazione dati applicativi da sistemi legacy a nuovi storage (2 gg)
- 6.3.2 Riconfigurazione postazioni di lavoro e Profili utente (1,5 gg)
- 6.3.3 Verifica continuità servizi durante la migrazione (cut-over) (1,5 gg)

---

### 7.0 Test e Collaudo (15 gg)

#### 7.1 Test di connettività e rete (4 gg)
- 7.1.1 Test connettività LAN, VLAN e routing (1 gg)
- 7.1.2 Test VPN LAN-to-LAN, Client-to-LAN e hybrid cloud (1,5 gg)
- 7.1.3 Test ridondanza collegamenti e failover automatico (1 gg)
- 7.1.4 Test di latenza e throughput su circuiti critici (0,5 gg)

#### 7.2 Test cluster HPC (3 gg)
- 7.2.1 Test performance di calcolo (benchmark HPL/HPG) (1 gg)
- 7.2.2 Test latenza e banda InfiniBand (1 gg)
- 7.2.3 Test scheduling SLURM e gestione job multipli (1 gg)

#### 7.3 Test applicazione Pondus (3 gg)
- 7.3.1 Test funzionali applicazione C# su IIS (1 gg)
- 7.3.2 Test di carico e performance DB (MS SQL) (1 gg)
- 7.3.3 Test integrazione Pondus con infrastruttura aggiornata (1 gg)

#### 7.4 Test sicurezza e disaster recovery (3 gg)
- 7.4.1 Vulnerability assessment e penetration test (1,5 gg)
- 7.4.2 Test disaster recovery: ripristino da backup e failover sito (1 gg)
- 7.4.3 Test policy di accesso, autenticazione e crittografia (0,5 gg)

#### 7.5 Collaudo finale e accettazione (2 gg)
- 7.5.1 Verifica conformità a requisiti e specifiche progettuali (1 gg)
- 7.5.2 Collaudo congiunto con committenza e verbale di accettazione (1 gg)

---

### 8.0 Formazione e Documentazione (10 gg)

#### 8.1 Formazione del personale (6 gg)
- 8.1.1 Formazione amministratori di sistema su nuova infrastruttura (2 gg)
- 8.1.2 Formazione utenti finali su nuovi servizi e strumenti (2 gg)
- 8.1.3 Formazione su procedure di sicurezza, backup e DR (1 gg)
- 8.1.4 Formazione su applicazione Pondus potenziata (1 gg)

#### 8.2 Documentazione tecnica e operativa (4 gg)
- 8.2.1 Documentazione architettura finale e schemi rete (1 gg)
- 8.2.2 Procedure operative (runbook) per amministrazione ordinaria (1,5 gg)
- 8.2.3 Manuali utente e guide rapide per servizi finali (1 gg)
- 8.2.4 Documentazione as-built e consuntivo tecnico (0,5 gg)

---

### 9.0 Avvio e Supporto (12 gg)

#### 9.1 Avvio in produzione (4 gg)
- 9.1.1 Go-live: attivazione progressiva dei servizi (1,5 gg)
- 9.1.2 Verifica operatività generale e monitoraggio intensivo (1,5 gg)
- 9.1.3 Stabilizzazione e correzioni rapide post-avvio (1 gg)

#### 9.2 Supporto post-avvio (6 gg)
- 9.2.1 Supporto helpdesk prima settimana (3 gg)
- 9.2.2 Supporto helpdesk seconda settimana (2 gg)
- 9.2.3 Risoluzione anomalie residue e interventi correttivi (1 gg)

#### 9.3 Passaggio in garanzia (2 gg)
- 9.3.1 Consegna documentazione finale e closure report (1 gg)
- 9.3.2 Passaggio di consegne formale a supporto interno e service desk (1 gg)

---

## Riepilogo effort per fase

| Codice | Fase | Giorni uomo (gg) |
|:---:|---|---|
| 1.0 | Project Management | 18 |
| 2.0 | Assessment e Analisi | 18 |
| 3.0 | Progettazione | 22 |
| 4.0 | Approvvigionamento HW/SW | 10 |
| 5.0 | Configurazione e Implementazione | 36 |
| 6.0 | Migrazione | 15 |
| 7.0 | Test e Collaudo | 15 |
| 8.0 | Formazione e Documentazione | 10 |
| 9.0 | Avvio e Supporto | 12 |
| | **Totale** | **156** |

---

## Note

- **156 giorni uomo** complessivi, distribuiti su **12 settimane** di calendario con risorse PM e Sistemista in parallelo.
- Il costo manodopera stimato è di circa **€181.000** (156 gg × costo medio ponderato PM/sistemista ~€1.160/gg).
- La fase 5 (Configurazione e Implementazione) è la più onerosa (36 gg, 23% del totale), seguita dalla fase 3 (Progettazione, 22 gg, 14%).
- Le attività di Project Management (18 gg) sono distribuite sull'intera durata del progetto.
- Le fasi 4 (Approvvigionamento) e 5 (Implementazione) possono sovrapporsi parzialmente per ottimizzare i tempi.
