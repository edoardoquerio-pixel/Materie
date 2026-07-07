# Project Work e Laboratori — Memoria Completa del Progetto

> **Materia:** 23_Project_Work_e_Laboratori
> **Ultimo aggiornamento:** 07/06/2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027 (BF 2025-27)
> **Docente:** Luca Robaldo — Unità Formativa "Learning by project"

---

## Indice

1. [Panoramica Generale](#1-panoramica-generale)
2. [Scenario Aziendale](#2-scenario-aziendale)
3. [Assessment AS-IS](#3-assessment-as-is)
4. [Decisioni di Convergenza (Gap Analysis)](#4-decisioni-di-convergenza-gap-analysis)
5. [Architettura TO-BE per Area](#5-architettura-to-be-per-area)
6. [Budget e Costi](#6-budget-e-costi)
7. [ProjectWork_Infrastruttura_IT — Varianti](#7-projectwork_infrastruttura_it--varianti)
8. [Gruppi di Lavoro](#8-gruppi-di-lavoro)
9. [Stato Avanzamento e Prossimi Step](#9-stato-avanzamento-e-prossimi-step)
10. [Riferimenti Incrociati](#10-riferimenti-incrociati)

---

## 1. Panoramica Generale

### File rilevanti

| File | Percorso |
| --- | --- |
| Traccia progetto | `00_Note/01_Cloud_Specialist_-_BF_2025-27_-_Learning_by_project_-_Progetto.md` (e PDF in `01_Materiale/`) |
| Gruppi di lavoro | `00_Note/02_Gruppi_di_lavoro.md` |
| Appunti strutturati | `00_Note_STRUTTURATE.md` |

### Due progetti distinti

Nella directory `03_Progetti/` coesistono due progetti paralleli:

| Progetto | Percorso | Stato |
| --- | --- | --- |
| **TP_Group** | `03_Progetti/TP_Group/` | **Attivo** — 9 aree complete, agenti specializzati |
| **ProjectWork_Infrastruttura_IT** | `03_Progetti/ProjectWork_Infrastruttura_IT/` | **Bozza** — 3 varianti architetturali (GCP, On-Prem, Ibrido) + variante D (Azure) |

> **Nota importante:** TP_Group e ProjectWork_Infrastruttura_IT sono progetti separati sviluppati indipendentemente, non sovrapponibili. TP_Group è più avanzato e strutturato con agenti dedicati.

---

## 2. Scenario Aziendale

### TP Group — Fusione Thema Consulting + Pro Studio

| Dato | Thema Consulting | Pro Studio |
| --- | --- | --- |
| **Settore** | Progettazione strutturale automotive | Progettazione aerospace |
| **Anno fondazione** | Fine anni '90 | 2023 |
| **Personale** | 30 dipendenti/collaboratori | 20 dipendenti |
| **Sede** | Centro Torino (di proprietà) | Condominio uffici Torino (affitto) |
| **Destino sede** | Mantenuta (max 40 postazioni) | **Da dismettere** |
| **Modello IT** | On-premise prevalente | Full cloud |

### Vincoli chiave

- **Budget totale progetto:** 520.000 € + IVA
- **Costi risorse:** sistemista €500/giorno, PM €650/giorno (entrambi extra budget — coprono IT interno per 3 anni)
- **Smart working:** minimo 10 dipendenti/giorno in remoto via VPN
- **Finestra manutenzione:** massimo 7 giorni consecutivi
- **Ciclo di vita:** 3 anni
- **Conformità richiesta:** ISO/IEC 27001 (business continuity, disaster recovery, sicurezza accessi)
- **Postazioni sede:** max 40 (con 50 dipendenti → smart working strutturale per almeno 10)

### Referente cliente

| Dato | Valore |
| --- | --- |
| Ruolo | Solution Architect |
| Priorità dichiarate | Produttività operativa, business continuity |
| Tempi migrazione | 9-12 mesi |
| Preferenze tecnologiche | NO Google Workspace (confermato: mantenere ecosistema Thema: MS365, Zimbra, NextCloud, GiTea) |

---

## 3. Assessment AS-IS

### 3.1 Thema Consulting — Infrastruttura on-premise

**Datacenter:**
- 2 armadi rack saturi (non espandibili)
- 2 host VMWare
- SAN NetApp 24 TB
- NAS QNAP 32 TB (backup on-premise)
- UPS autonomia ~10 minuti
- Condizionamento al limite

**Cluster HPC:**
- 8 nodi fisici Linux con Infiniband proprietario
- 1 front-end VM Linux
- Nessuna GPU
- Utilizzo: simulazioni crash test (solo interno)

**Pondus:**
- Web application C# su MS IIS + MS SQL Server
- HW dedicato: 1 CPU Xeon Silver 4110, 64 GB RAM, 1,2 TB HDD
- Servizio attivo dal 2015 per clienti automotive/aerospace

**Servizi self-hosted su VM Linux:**
| Servizio | Prodotto | Piattaforma |
| --- | --- | --- |
| Posta/Calendario | Zimbra | VM Linux |
| Office | MS365 + LibreOffice | Desktop + cloud |
| Videoconferenza | MS Teams | Cloud |
| Autenticazione | AD Samba4 | VM Linux |
| File Server | NextCloud | VM Linux |
| Sviluppo/Versioning | GiTea | Self hosted |
| Contabilità | Profis | Windows Server |
| CRM | Sugar CRM | VM Linux |
| Timesheet | Kimai | VM Linux |
| Documentazione | Media Wiki | VM Linux |

### 3.2 Pro Studio — Full cloud (GCP)

| Servizio | Prodotto | Piattaforma |
| --- | --- | --- |
| Posta/Calendario | Google Workspace | SaaS |
| Office | Google Workspace | SaaS |
| Videoconferenza | Google Meet | SaaS |
| Autenticazione | Google Authenticator | SaaS |
| File Server | Google Drive | SaaS |
| Sviluppo/Versioning | Bit Bucket | SaaS |
| Contabilità | Odoo | SaaS |
| CRM | Odoo | SaaS |
| Timesheet | Odoo | SaaS |
| Documentazione | Media Wiki | IaaS (GCP) |

### 3.3 Criticità emerse

| ID | Criticità | Impatto | Priorità |
| --- | --- | --- | --- |
| C1 | Datacenter saturo (2 rack) | Alto | Critica |
| C2 | UPS autonomia 10' | Alto | Alta |
| C3 | Condizionamento al limite | Alto | Alta |
| C4 | Sede Pro Studio da dismettere | Alto | Critica |
| C5 | Due domini di autenticazione | Medio | Media |
| C6 | Backup non delocalizzato | Medio | Media |
| C7 | Nessuna ridondanza connettività | Medio | Media |
| C8 | Piattaforme office eterogenee | Basso | Bassa |
| C9 | Assenza MFA strutturato | Medio | Media |
| C10 | Versioning non unificato | Basso | Bassa |

---

## 4. Decisioni di Convergenza (Gap Analysis)

### Decisioni definitive (intervista cliente 18/06/2026)

| Servizio | Thema | Pro Studio | Decisione TO-BE |
| --- | --- | --- | --- |
| **Posta/Calendario** | Zimbra | Google Workspace | **Zimbra** (unificata) |
| **Office** | MS365 / LibreOffice | Google Workspace | **MS365** per tutti 50 utenti |
| **Videoconferenza** | MS Teams | Google Meet | **MS Teams** |
| **Autenticazione** | AD Samba4 | Google Authenticator | **AD Samba4 + MFA** |
| **File Server** | NextCloud | Google Drive | **NextCloud** |
| **Versioning** | GiTea | Bit Bucket | **GiTea** |
| **Contabilità** | Profis | Odoo | **Profis** (mantenuto) |
| **CRM** | Sugar CRM | Odoo | **Odoo** |
| **Timesheet** | Kimai | Odoo | **Odoo** |
| **Documentazione** | Media Wiki (on-prem) | Media Wiki (GCP) | **Media Wiki** unico on-prem |

### Mappa migrazioni

```
Google Workspace → Zimbra (posta)
Google Workspace → MS365 (office)
Google Meet → MS Teams (videoconferenza)
Google Drive → NextCloud (file server)
Bit Bucket → GiTea (versioning)
Sugar CRM → Odoo (CRM)
Kimai → Odoo (timesheet)
Media Wiki GCP → Media Wiki on-prem (unificato)
```

---

## 5. Architettura TO-BE per Area

### 5.1 Rete e VPN

| Componente | Specifica | Costo |
| --- | --- | --- |
| Firewall HA | 2× Fortigate FG-100F | € 9.000 |
| Switch Core L3 | 2 unità stack (Cisco CBS350-24P-4G) | € 2.400 |
| Switch Accesso L2 | 2 unità 48 porte (Cisco CBS250-48P) | € 1.800 |
| Access Point WiFi 6 | 3× UniFi U6 Pro | € 450 |
| Cablaggio | Patch panel, connettori | € 1.500 |
| **Totale HW rete** | | **€ 15.150** |
| ISP doppio link | 2× fibra 1 Gbps | € 240/mese |

**VLAN:**
| VLAN | Scopo | Subnet |
| --- | --- | --- |
| 10 | Uffici | 10.10.10.0/24 |
| 20 | Management | 10.10.20.0/24 |
| 30 | WiFi guest | 10.10.30.0/24 |
| 40 | Datacenter | 10.10.40.0/24 |
| 50 | Pondus | 10.10.50.0/24 |
| 60 | Backup | 10.10.60.0/24 |
| 70 | HPC Ethernet | 10.10.70.0/24 |
| 80 | HPC Infiniband | 192.168.100.0/24 |
| 90 | VPN LAN to LAN | 10.10.90.0/24 |
| 100 | VPN Hybrid Cloud | 10.10.100.0/24 |

**VPN:**
| Tipo | Protocollo | Utilizzo |
| --- | --- | --- |
| LAN to LAN | IPsec IKEv2 AES-256-GCM | Sede ↔ DR |
| Client to LAN | WireGuard ChaCha20 | 50 utenti remoti |
| Hybrid Cloud | IPsec IKEv2 AES-256-GCM | Sede ↔ GCP |

### 5.2 Sicurezza ISO 27001

**Cifratura at-rest:**
- SAN NetApp: NSE AES-256 (nativo)
- NAS QNAP: AES-256 volume
- VM VMWare: vSphere encryption AES-256
- 40 laptop Windows: BitLocker AES-256-XTS
- 10 laptop Linux: LUKS AES-256-XTS
- HPC scratch: LUKS
- DB Pondus: TDE AES-256
- Backup GCP: CSEK AES-256

**IAM:**
- Identity Provider: AD Samba4 (primario)
- MFA: FortiToken (push OTP)
- SSO: SAML 2.0 per Google Workspace
- Sincronizzazione: Google Cloud Directory Sync (GCDS)
- Password policy: 12+ caratteri, scadenza 90 giorni

**Costi sicurezza:** € 17.500

### 5.3 Cluster HPC

**Specifica nuovo nodo (AMD EPYC):**
| Componente | Specifica |
| --- | --- |
| CPU | 2× AMD EPYC 9654 (96 core × 2 = 192 core/nodo) |
| RAM | 1.536 GB DDR5-4800 ECC |
| Scratch | 1× SSD NVMe U.2 1,6 TB |
| HCA Infiniband | NVIDIA ConnectX-7 NDR200 (200 Gbps) |
| NIC Ethernet | Intel E810-2CQDA2 2×25 GbE |
| OS | Rocky Linux 9 |
| Costo per nodo | ~€ 20.060 |
| **Totale 8 nodi** | **~€ 160.500** |

**Rete Infiniband:**
| Componente | Costo |
| --- | --- |
| Switch QM9790 NDR200 (36 porte) | € 25.000 |
| Cavi DAC 17× | € 2.550 |

**Stack SW:** Slurm (scheduler), Lustre (filesystem parallelo), Rocky Linux 9

**Logistica:** Co-location hosting (risolve saturazione datacenter)
- Co-location: € 1.300/mese (1° anno: € 9.600 in offerta)
- Costo totale HPC (3 anni): **€ 303.470** (on-premise/hosting)
- Ottimizzabile a **€ 219.620** con CPU AMD EPYC 9334 + switch HDR100

### 5.4 Pondus App

**Architettura TO-BE:** Migrazione da HW fisico a VM HA su VMWare (confermato dal cliente: self-hosted → online)

| Componente | Specifica | Costo |
| --- | --- | --- |
| Web IIS (2 VM) | 4 vCPU, 16 GB RAM, 80 GB SSD | Incluso in VMWare |
| DB MS SQL (2 VM) | 8 vCPU, 32 GB RAM, 500+100 GB SSD | Incluso in VMWare |
| HA | AlwaysOn Availability Group + NLB | — |
| WAF | Fortigate Web Application Firewall | Incluso |
| Autenticazione | AD Samba4 + MFA admin; JWT clienti | — |
| Backup DB | Completo giornaliero + log shipping orario | — |
| Costi licenze | Windows Server + MS SQL Server | € 4.800 |
| Sistemista migrazione | 20 giorni | € 10.000 |
| **Totale Pondus** | | **€ 15.000** |

### 5.5 Cloud Migration (Ibrido)

| Servizio | Azione | Tempistica |
| --- | --- | --- |
| VPN GCP + GCDS | Configurazione | Settimane 1-2 |
| Identità (AD ↔ Google Workspace) | SSO SAML | Settimane 2-3 |
| Media Wiki | Migrazione GCP → on-prem | Settimane 3-4 |
| Google Drive → NextCloud | Trasferimento rclone | Settimane 4-6 |
| Bit Bucket → GiTea | Migrazione repo | Settimana 5 |
| Sugar CRM + Kimai → Odoo | Esportazione/import | Settimane 5-6 |
| Dismissione Google Workspace | Finale | Settimane 6-8 |
| **Costo migrazione cloud** | | **€ 10.500** |

**Costi IAM:** € 4.500 (FortiAuthenticator + FortiToken + sistemista)

### 5.6 Backup e Disaster Recovery

**Regola 3-2-1:**
- 3 copie: produzione + NAS QNAP + GCS
- 2 supporti: disco (NAS) + cloud (GCS)
- 1 off-site: GCS Nearline

**Storage backup:**
| Storage | Capacità | Retention | Costo |
| --- | --- | --- | --- |
| NAS QNAP (nuovo) | 40 TB | 30gg + 12 mesi | € 4.000 |
| GCS Nearline | 10 TB iniziali | 90gg + 3 anni | € 150/mese |
| SAN NetApp | 24 TB | 7gg + 4 sett. | Incluso |

**RPO/RTO target:**
| Sistema | RPO | RTO | Priorità |
| --- | --- | --- | --- |
| Pondus | 1 ora | 4 ore | Critica |
| AD Samba4 | 24 ore | 4 ore | Alta |
| File server | 24 ore | 8 ore | Media |
| HPC | 7 giorni | 48 ore | Bassa |

**DR:** Opzione B — Cloud DR su GCP (€ 600/mese)
**Test:** Mensile (singolo sistema), Trimestrale (failover Pondus), Annuale (DR completo)

### 5.7 Project Management

**Milestone:**
| M# | Milestone | Periodo |
| --- | --- | --- |
| M1 | Assessment completato | Mese 1-2 |
| M2 | Rete e VPN operative | Mese 2-4 |
| M3 | Sicurezza implementata | Mese 3-6 |
| M4 | HPC potenziato | Mese 4-8 |
| M5 | Pondus migrato e HA | Mese 6-9 |
| M6 | Cloud integrato | Mese 5-9 |
| M7 | Backup e DR pronti | Mese 6-9 |
| M8 | Offerta consegnata | Mese 8-12 |
| M9 | Smart working operativo | Mese 2 |
| M10 | Chiusura progetto | Mese 9-12 |

**RASCI:** 9 aree, 11 ruoli (PM, Sistemista, Security Officer, HPC Engineer, App Architect, Cloud Specialist, Backup Engineer, Bid Manager, Referente Thema, Referente Pro Studio, Direzione)

**Rischi:** 22 rischi (4 alti, 13 medi, 5 bassi) — R01, R02, R05, R08, R14, R16 sono critici (livello 6)

---

## 6. Budget e Costi

### Riepilogo per Dominio (TP_Group)

| Dominio | Una tantum | Ricorrente/mese |
| --- | --- | --- |
| Rete e VPN | € 22.650 | € 240 |
| Sicurezza ISO 27001 | € 11.500 | € 200 |
| Cluster HPC | € 191.600 | € 800 |
| Pondus | € 15.000 | € 0 |
| Cloud Migration | € 5.500 | € 300 |
| Backup e DR | € 7.200 | € 210 |
| Project Management | € 19.500 | € 0 |
| **Totale** | **€ 272.950** | **€ 1.750** |

> **Budget:** € 520.000 — **Margine:** € 247.050 ✅

### Costi ricorrenti (3 anni)

| Anno | Una tantum | Ricorrenti | Totale anno | Cumulato |
| --- | --- | --- | --- | --- |
| 1 | € 272.950 | € 21.000 | € 293.950 | € 293.950 |
| 2 | € 0 | € 21.000 | € 21.000 | € 314.950 |
| 3 | € 0 | € 21.000 | € 21.000 | € 335.950 |

### KANBAN — Carichi di lavoro

| Area | Backlog | Todo | In Progress | Done |
| --- | --- | --- | --- | --- |
| Rete / VPN | 2 | 1 | — | — |
| Sicurezza ISO 27001 | — | 2 | — | — |
| Cluster HPC | — | 1 | — | — |
| App Pondus | 1 | 1 | — | — |
| Cloud Migration | — | 2 | — | — |
| Backup / DR | — | 1 | — | — |
| Offerta documenti | — | 1 | 1 | — |
| Project Management | — | — | 1 | — |
| Architettura / Assessment | — | — | 1 | — |
| Logistica | — | 1 | — | — |

---

## 7. ProjectWork_Infrastruttura_IT — Varianti

### Panoramica

Progetto separato che esplora 3 varianti architetturali + 1 variante aggiuntiva (Azure). **Non sovrapponibile a TP_Group** — sviluppato indipendentemente.

| Variante | Descrizione | Budget 3 anni |
| --- | --- | --- |
| **A — Full Cloud GCP** | Tutta l'infrastruttura su Google Cloud | ~€ 549.720 |
| **B — On-Premise** | Infrastruttura on-premise con co-location | ~€ 601.100 |
| **C — Ibrido** | On-premise (HPC) + Cloud (servizi, DR) | ~€ 674.900 |
| **D — Full Cloud Azure** | Tutta l'infrastruttura su Microsoft Azure | ~€ 570.756 |

### Confronto chiave

| Criterio | A — GCP | B — On-Prem | C — Ibrido | D — Azure |
| --- | --- | --- | --- | --- |
| HPC | Istanze C2 (no InfiniBand) | 16 nodi InfiniBand 200G | 16 nodi + burst GCP | **InfiniBand NDR 400G** |
| Pondus | Cloud Run + Cloud SQL | Server on-prem + Docker | Cloud Run + Cloud SQL | **AKS Windows + Azure SQL** |
| Posta | Google Workspace | Zimbra + Workspace | Google Workspace | **M365 già presente** |
| DR | Auto multi-regione | Manuale (RTO 10h) | Misto | **Auto West/North Europe** |
| Costo 3 anni | **~€549.720** | **~€601.100** | **~€674.900** | **~€570.756** |

### Raccomandazione finale (da matrice confronto)

Variante **C — Ibrida** per miglior rapporto costo/beneficio (mantiene InfiniBand per HPC e sfrutta cloud per DR).
**OPPURE** Variante **D — Azure** se il cliente preferisce ecosistema Microsoft (M365 già presente).

### Piano di test (solo variante D)

24 test case coprenti: Rete/VPN (4), HPC (4), Pondus (4), Migrazione (4), Backup/DR (4), Sicurezza (4).

### Stato ProjectWork_Infrastruttura_IT

- **Stato:** Bozza / Incompleto
- **Assessment:** Completato (Thema + Pro Studio + Gap Analysis)
- **Project Management:** Project Charter, WBS, Gantt, RASCI, Risk (presenti)
- **Variante D (Azure):** Offerta economica dettagliata, piano migrazione, piano test
- **Altre varianti (GCP, On-Prem, Ibrido):** Struttura scheletro (solo alcune aree compilate)
- **Directory `.omo/drafts/`:** Presente ma vuota (bozze temporanee)

---

## 8. Gruppi di Lavoro

### Gruppo 1 — Digital Horizon Lab
Christian Cavagnero, Katherinne Huancayo Ramos, Christopher Mancini, Francesco Montaperto, Salvatore Scaringella

### Gruppo 2 — H2C (Hybrid to Cloud)
Daniele Buscemi, Andrea Chiandoni, Vito Nicolò Ingargiola, Simone Liguori, Alessandro Pistone

### Gruppo 3 — Sprout
Loris Angione, Barbara Cucchiara, Ivan Jaures Kouankeu Nya, Anis Ravera, Andrea Sassi

### Gruppo 4 — Forty Group
Rita Cignarelli, Luciano Stanziani, Mario Mogavero, **Edoardo Querio Gianetto**, Lorenzo Sasso, Luca Tarallo

### Gruppo 5 — 5 Stack
Lorenzo Airoldi, Gabriele Mattiolo, Emanuele Sole, Jacopo Franco Santiago Merlo, Yassine Suriano

---

## 9. Stato Avanzamento e Prossimi Step

### TP_Group — Stato attuale

| Area | Stato | Note |
| --- | --- | --- |
| **01_Assessment** | ✅ Completo | AS-IS, Gap Analysis, Report Thema + Pro Studio |
| **02_Rete_VPN** | ✅ Completo | Progetto rete, VPN, schema (Mermaid) |
| **03_Sicurezza_ISO27001** | ✅ Completo | Requisiti ISO, politica cifratura, matrice rischi |
| **04_Cluster_HPC** | ✅ Completo | Progetto cluster, confronto costi |
| **05_Pondus_App** | ✅ Completo | Architettura TO-BE, piano migrazione |
| **06_Cloud_Migration** | ✅ Completo | Strategia ibrida, piano migrazione + full cloud, integrazione identità |
| **07_Backup_DR** | ✅ Completo | Architettura backup, piano DR, procedure restore |
| **08_Offerta_Documenti** | ✅ Completo | Offerta, quotazione, checklist (manca presentazione azienda) |
| **09_Project_Management** | ✅ Completo | Charter, WBS, Gantt, RASCI, costi, rischi, template |
| **KANBAN** | 🟡 In aggiornamento | Backlog con task aperti |

### Item aperti (da KANBAN)

- [ ] Valutare upgrade Firewall Fortigate FG-60F (risolto: sostituzione con FG-100F HA)
- [ ] Definire subnetting IP completo (completato: 10 VLAN definite)
- [ ] Scegliere 2° ISP per ridondanza connettività (da decidere TIM vs WindTre)
- [ ] Valutare hosting vs on-premise per Pondus (deciso: migrazione a VM HA)
- [ ] Definire piano di test funzionali per ogni area (da redigere)
- [ ] Redigere presentazione azienda proponente (manca in offerta §3)
- [ ] Compilare template report di avanzamento (template pronto, da popolare)

### ProjectWork_Infrastruttura_IT — Stato

- Assessment e PM: completi
- Variante D (Azure): offerta economica + piano migrazione + piano test
- Varianti A/B/C: struttura scheletro (aree non compilate)
- Directory .omo/drafts/: vuota

---

## 10. Riferimenti Incrociati

### TP_Group — Struttura agenti

| Ordine | Agente | Cartella | Dipende da |
| --- | --- | --- | --- |
| 1 | Assessment Analyst | `01_Assessment/` | — |
| 2 | Network & VPN Engineer | `02_Rete_VPN/` | 1 |
| 3 | Security & Compliance Officer | `03_Sicurezza_ISO27001/` | 1, 2 |
| 4 | HPC Architect | `04_Cluster_HPC/` | 1 |
| 5 | Application Architect (Pondus) | `05_Pondus_App/` | 1, 3 |
| 6 | Cloud Migration Specialist | `06_Cloud_Migration/` | 1, 2 |
| 7 | Backup & DR Engineer | `07_Backup_DR/` | 1, 3, 6 |
| 8 | Bid Manager (Offerta) | `08_Offerta_Documenti/` | tutti |
| 9 | Project Manager | `09_Project_Management/` | tutti |

### Regole progetto TP_Group

- Lavorare SOLO dentro `23_Project_Work_e_Laboratori`
- Lingua: italiano
- Formato: Markdown con tabelle `| --- |`
- Scelte tecniche motivate per: erogazione, tipologia server, OS, open source vs commerciale, noleggio vs proprietà, gestione interna vs outsourcing
- Costi IVA esclusa
- Budget: € 520k

### ProjectWork_Infrastruttura_IT — Note

- README.md alla root del progetto fornisce la guida alla navigazione
- Variante D (Azure) è la più avanzata tra le varianti
- Non ci sono dipendenze con TP_Group
- Le domande "da chiedere al cliente" sono lasciate come assunzioni
