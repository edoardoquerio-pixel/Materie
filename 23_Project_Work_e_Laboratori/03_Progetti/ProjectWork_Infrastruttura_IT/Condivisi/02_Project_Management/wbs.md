# WBS — Work Breakdown Structure

## Progetto: Integrazione Infrastruttura IT TP Group (Thema Consulting + Pro Studio) — Variante D (Full Cloud Azure)

| Campo | Valore |
|---|---|
| **Documento** | WBS — Work Breakdown Structure |
| **Versione** | 2.0 (Variante D) |
| **Data** | Giugno 2026 |
| **Redatto da** | PM (Project Manager) |
| **Durata progetto** | 12 settimane attive |
| **Risorse** | Sistemista (€500/gg) + Project Manager (€650/gg) + Sviluppatore .NET (€450/gg) |
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
- 2.2.1 Requisiti di connettività (VPN LAN-to-LAN, Client-to-LAN) (1,5 gg)
- 2.2.2 Requisiti cluster HPC (8 nodi HB96-96rs v4, InfiniBand NDR) (1,5 gg)
- 2.2.3 Requisiti sicurezza e conformità ISO/IEC 27001 (1 gg)
- 2.2.4 Requisiti business continuity e disaster recovery (1 gg)

#### 2.3 Gap analysis (4 gg)
- 2.3.1 Confronto stato attuale vs architettura target Azure (2 gg)
- 2.3.2 Stima effort, risorse e costi necessari (1 gg)
- 2.3.3 Analisi rischi preliminare e mitigazioni (1 gg)

---

### 3.0 Progettazione (22 gg)

#### 3.1 Progettazione architettura di rete (6 gg)
- 3.1.1 Progettazione topologia rete convergente su Azure VNet (2 gg)
- 3.1.2 Schema IP, subnetting e VNet peering (1,5 gg)
- 3.1.3 Progettazione VPN (LAN-to-LAN, Client-to-LAN) su Azure VPN Gateway (2 gg)
- 3.1.4 Progettazione ridondanza collegamenti e failover (0,5 gg)

#### 3.2 Progettazione cluster HPC (6 gg)
- 3.2.1 Specifica tecnica nodi HB96-96rs v4 (CPU, RAM 8 GB/core, scratch NVMe) (2 gg)
- 3.2.2 Architettura rete InfiniBand NDR 400 Gbps su Azure (2 gg)
- 3.2.3 Schema storage: Managed Lustre + Blob + egress data (1 gg)
- 3.2.4 Piano di espansione (Scenario B — 8 nodi, dismissione on-prem) (1 gg)

#### 3.3 Progettazione sicurezza e conformità (6 gg)
- 3.3.1 Piano di adeguamento ISO/IEC 27001 — gap analysis formale (2 gg)
- 3.3.2 Policy di sicurezza: accessi, crittografia, protocolli sicuri (1,5 gg)
- 3.3.3 Piano di disaster recovery: RPO/RTO, delocalizzazione, failover (1,5 gg)
- 3.3.4 Matrice crittografia per sistema (dati a riposo, in transito) (1 gg)

#### 3.4 Progettazione migrazione Azure (4 gg)
- 3.4.1 Definizione strategia migrazione: all-in Azure (1,5 gg)
- 3.4.2 Architettura servizi Azure: tenant, landing zone, subscription, RBAC (1,5 gg)
- 3.4.3 Piano di migrazione servizi e cronologia delle fasi (1 gg)

---

### 4.0 Setup Azure Tenant e Licenze (8 gg)

#### 4.1 Setup tenant Azure e landing zone (3 gg)
- 4.1.1 Creazione tenant Microsoft Entra ID, subscription e management group (1 gg)
- 4.1.2 Configurazione Azure Policy (ISO 27001 built-in initiative) (1 gg)
- 4.1.3 Configurazione RBAC, PIM e Conditional Access (1 gg)

#### 4.2 Attivazione licenze e servizi M365 (3 gg)
- 4.2.1 Upgrade licenze Thema Business Basic → Business Premium (1 gg)
- 4.2.2 Onboarding 20 utenti Pro Studio su M365 (Google Workspace → M365) (1,5 gg)
- 4.2.3 Configurazione Microsoft Purview (DLP, Information Protection) (0,5 gg)

#### 4.3 Setup Azure DevOps e BitBucket (2 gg)
- 4.3.1 Creazione organizzazione Azure DevOps, progetti e repo migration (1 gg)
- 4.3.2 Configurazione CI/CD pipeline per Pondus (1 gg)

---

### 5.0 Configurazione e Implementazione (36 gg)

#### 5.1 Configurazione rete e VPN su Azure (10 gg)
- 5.1.1 Deploy Azure VNet, subnet, NSG e routing (2 gg)
- 5.1.2 Configurazione Azure VPN Gateway (Active-Active, IPsec IKEv2) (2,5 gg)
- 5.1.3 Configurazione VPN LAN-to-LAN (FortiGate sede ↔ Azure) (2,5 gg)
- 5.1.4 Configurazione VPN Point-to-Site (remoti e collaboratori) + Azure Bastion (1,5 gg)
- 5.1.5 Configurazione Azure Front Door / Traffic Manager per DR (1,5 gg)

#### 5.2 Setup identità Entra ID Connect (6 gg)
- 5.2.1 Installazione e configurazione Microsoft Entra ID Connect (sync Samba4 AD) (2 gg)
- 5.2.2 Configurazione password hash sync e password writeback (1,5 gg)
- 5.2.3 Configurazione Conditional Access, MFA e PIM (2 gg)
- 5.2.4 Test autenticazione e group sync (0,5 gg)

#### 5.3 Deploy cluster HPC Azure HB96 (10 gg)
- 5.3.1 Deploy Azure CycleCloud e configurazione Slurm (2 gg)
- 5.3.2 Creazione nodi HB96-96rs v4 (3 Reserved + 5 Spot) con image Rocky Linux (2,5 gg)
- 5.3.3 Configurazione InfiniBand NDR (ConnectX-7, SR-IOV) e MPI (2 gg)
- 5.3.4 Configurazione Azure Managed Lustre (10 TB) e mount su nodi (1,5 gg)
- 5.3.5 Benchmark performance iniziali (HPL, OSU MPI) e validazione (2 gg)

#### 5.4 Deploy Pondus su AKS Windows (5 gg)
- 5.4.1 Creazione cluster AKS con Windows nodepool (1 gg)
- 5.4.2 Configurazione Azure Container Registry per immagini Windows (0,5 gg)
- 5.4.3 Deploy container Windows Pondus su AKS (2,5 gg)
- 5.4.4 Configurazione HPA, ingress controller e Application Gateway (1 gg)

#### 5.5 Configurazione backup e DR (5 gg)
- 5.5.1 Configurazione Azure Backup (VM HBv4 ogni 4 ore, Azure Files giornaliero) (1,5 gg)
- 5.5.2 Configurazione Azure Blob Storage GRS (soft delete, versioning, lifecycle) (1 gg)
- 5.5.3 Configurazione Azure SQL Active Geo-Replication (failover automatico) (1 gg)
- 5.5.4 Configurazione Azure Site Recovery per VM (drill) (0,5 gg)
- 5.5.5 Test DR iniziale e validazione RPO/RTO (1 gg)

---

### 6.0 Migrazione (18 gg)

#### 6.1 Migrazione servizi collaborativi su M365 (5 gg)
- 6.1.1 Migrazione posta Zimbra → M365 Exchange (2 gg)
- 6.1.2 Migrazione file NextCloud → SharePoint Online / OneDrive (1,5 gg)
- 6.1.3 Migrazione Google Workspace Pro Studio → M365 (posta, Drive, calendar) (1,5 gg)

#### 6.2 Migrazione identità su Entra ID (4 gg)
- 6.2.1 Configurazione Microsoft Entra ID Connect (sync da Samba4 AD) (1,5 gg)
- 6.2.2 Migrazione utenti, gruppi e policy di accesso (1 gg)
- 6.2.3 Configurazione SSO e autenticazione multifattore (MFA) (1,5 gg)

#### 6.3 Migrazione applicazioni e dati (5 gg)
- 6.3.1 Migrazione DB Pondus su Azure SQL Managed Instance (2 gg)
- 6.3.2 Migrazione GiTea → Azure DevOps (repo, wiki) (1,5 gg)
- 6.3.3 Migrazione MediaWiki → SharePoint / Azure App Service (1,5 gg)

#### 6.4 Migrazione Profis → Odoo (4 gg)
- 6.4.1 Export dati contabili da Profis e trasformazione ETL (2 gg)
- 6.4.2 Import su Odoo e verifica quadratura contabile (2 gg)

---

### 7.0 Test e Collaudo (15 gg)

#### 7.1 Test di connettività e rete (4 gg)
- 7.1.1 Test connettività VNet, subnet e NSG (1 gg)
- 7.1.2 Test VPN LAN-to-LAN e Client-to-LAN (1,5 gg)
- 7.1.3 Test Azure Bastion e accesso admin (0,5 gg)
- 7.1.4 Test ridondanza e failover connettività (1 gg)

#### 7.2 Test cluster HPC (3 gg)
- 7.2.1 Test performance di calcolo (benchmark HPL — atteso ~36 TFLOPS) (1 gg)
- 7.2.2 Test latenza e banda InfiniBand NDR (<2 μs, >380 Gbps) (1 gg)
- 7.2.3 Test scheduling Slurm e gestione job con nodi Spot (1 gg)

#### 7.3 Test applicazione Pondus su AKS (3 gg)
- 7.3.1 Test funzionali applicazione C# su Windows container (1 gg)
- 7.3.2 Test di carico e performance DB (Azure SQL) (1 gg)
- 7.3.3 Test integrazione Pondus con AKS e scaling automatico (1 gg)

#### 7.4 Test sicurezza e disaster recovery (3 gg)
- 7.4.1 Vulnerability assessment e penetration test (1,5 gg)
- 7.4.2 Test disaster recovery: ripristino backup, failover SQL, Site Recovery drill (1 gg)
- 7.4.3 Test policy di accesso, MFA e Conditional Access (0,5 gg)

#### 7.5 Collaudo finale e accettazione (2 gg)
- 7.5.1 Verifica conformità a requisiti e specifiche progettuali (1 gg)
- 7.5.2 Collaudo congiunto con committenza e verbale di accettazione (1 gg)

---

### 8.0 Formazione e Documentazione (10 gg)

#### 8.1 Formazione del personale (6 gg)
- 8.1.1 Formazione amministratori su Azure, Entra ID e M365 (2 gg)
- 8.1.2 Formazione utenti finali su M365 (posta, SharePoint, Teams) (2 gg)
- 8.1.3 Formazione su procedure di sicurezza, backup e DR (1 gg)
- 8.1.4 Formazione su applicazione Pondus potenziata (1 gg)

#### 8.2 Documentazione tecnica e operativa (4 gg)
- 8.2.1 Documentazione architettura Azure finale e schemi rete (1 gg)
- 8.2.2 Procedure operative (runbook) per amministrazione Azure (1,5 gg)
- 8.2.3 Manuali utente e guide rapide per servizi finali (1 gg)
- 8.2.4 Documentazione as-built e consuntivo tecnico (0,5 gg)

---

### 9.0 Avvio e Supporto (12 gg)

#### 9.1 Avvio in produzione (4 gg)
- 9.1.1 Go-live: attivazione progressiva dei servizi Azure (1,5 gg)
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
| 4.0 | Setup Azure Tenant e Licenze | 8 |
| 5.0 | Configurazione e Implementazione | 36 |
| 6.0 | Migrazione | 18 |
| 7.0 | Test e Collaudo | 15 |
| 8.0 | Formazione e Documentazione | 10 |
| 9.0 | Avvio e Supporto | 12 |
| | **Totale** | **157** |

---

## Note

- **157 giorni uomo** complessivi, distribuiti su **12 settimane** di calendario con risorse PM e Sistemista in parallelo.
- Il costo manodopera stimato è di circa **€181.000** (157 gg × costo medio ponderato).
- **Variazioni rispetto alla WBS v1.0 (pre-variante D)**:
  - Rimosse: fase 4 "Approvvigionamento HW/SW" (sostituita da "Setup Azure Tenant"), attività 5.1.5 (hybrid cloud GCP), attività 5.2 (virtualizzazione on-prem)
  - Modificate: 2.2.1 (rimosso hybrid cloud), 3.1.1-3.1.4 (indirizzate su Azure VNet), 3.4 (da "cloud ibrido" a "migrazione Azure")
  - Aggiunte: 5.3 (deploy HPC HB96), 5.4 (deploy Pondus AKS), 5.5 (backup/DR su Azure), 6.4 (migrazione Profis→Odoo)
- La fase 5 (Configurazione e Implementazione) è la più onerosa (36 gg, 23% del totale), seguita dalla fase 3 (Progettazione, 22 gg, 14%).
- Le attività di Project Management (18 gg) sono distribuite sull'intera durata del progetto.
- Nessuna attività GCP, hybrid cloud connectivity o Google Workspace GCDS rimane nella WBS.
