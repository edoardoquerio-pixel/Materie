# Piano di Correzione — Variante D (Full Cloud Azure) — Allineamento Requisiti

## TL;DR

> **Quick Summary**: Correggere 16 gap identificati tra requisiti e soluzioni nella Variante D (Full Cloud Azure) del progetto TP Group. Modifiche critiche: SKU HPC da HB176 a HB96 (8 GB/core), Pondus da Linux container ad AKS Windows, ridimensionamento nodi HPC a 8, ricalcolo budget, riscrittura WBS/Gantt per Variante D, aggiornamento registro rischi.
>
> **Deliverables**: 9 documenti modificati + 1 nuovo documento
> - `04_Cluster_HPC/specifica_cluster_hpc.md` — Riscritto (SKU, nodi, costi)
> - `05_Pondus_App/architettura_pondus.md` — Riscritto (AKS Windows)
> - `06_Cloud_Migration/piano_migrazione_cloud.md` — Aggiornato (Profis→Odoo, M365, GiTea)
> - `07_Backup_DR/architettura_backup_dr.md` — Ritoccato (RPO HPC)
> - `08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md` — Integrato (policy org.)
> - `09_Offerta/offerta_tecnico_economica.md` — Riscritto (budget corretto)
> - `Condivisi/02_Project_Management/wbs.md` — Riscritto per Variante D
> - `Condivisi/02_Project_Management/gantt.md` — Riscritto per Variante D
> - `Condivisi/02_Project_Management/registro_rischi.md` — Aggiornato
> - `D_Full_Cloud_Azure/piano_test.md` — **Nuovo documento**
> - `REPORT_COMPARATIVO_VARIANTI.md` — Allineato
>
> **Estimated Effort**: Medium (10 documenti, 1 nuovo)
> **Parallel Execution**: YES — 3 waves
> **Critical Path**: Task 1 → Task 4 → Task 5 → Task 8 → Task 10

---

## Context

### Original Request
Analisi approfondita di tutti i requisiti del progetto TP Group (Variante D), confronto con le soluzioni adottate, identificazione gap, proposta modifiche e generazione piano di lavoro per applicare le correzioni.

### Interview Summary
**Key Discussions**:
- **HPC SKU**: Da HB176-96rs v4 (4,36 GB/core, viola requisito ≥8 GB/core) → **HB96-96rs v4** (96 core, 768 GB = 8 GB/core esatti)
- **Nodi HPC**: Da 5 nodi proposti → **8 nodi HB96** (Scenario B, sostituzione completa on-prem). Scenario A (16 nodi totali) scartato per costi + vincoli edificio.
- **Pondus**: Da Container Apps Linux → **AKS con Windows nodepool** (dipendenze Windows legacy)
- **M365**: Thema ha Business Basic. Upgrade a **Business Premium** incluso nel budget.
- **Profis**: Migrazione a **Odoo** unificato
- **Vincolo no VM**: SR-IOV accettabile come bare-metal ✅
- **Budget**: €374.520 → ~€470.220, ancora dentro €701k (+€230.780 margine)

### Research Findings
- **Azure HB96-96rs v4**: 96 core, 768 GB RAM, 8 GB/core, InfiniBand NDR 400 Gbps. Costo on-demand ~$3,60/h (vs $7,20 di HB176)
- **Azure Container Apps**: NON supporta Windows containers → obbligatorio AKS o App Service Windows
- **AKS Windows nodepool**: Minimo 1 nodo Windows, ~€400-500/mese per 2 vCPU
- **M365 Premium**: €22/utente/mese. Delta Basic→Premium: €16/utente/mese × 30 utenti = €5.760/anno
- **Azure egress**: ~€0,087/GB dopo 10 GB gratis. HPC stima 100-500 GB/mese → ~€1.500/anno

### Metis Review
**Identified Gaps** (addressed):
- Nessun gap aggiuntivo identificato da Metis. Analisi completa.

---

## Work Objectives

### Core Objective
Allineare la documentazione della Variante D (Full Cloud Azure) ai requisiti originali del progetto, correggendo i 16 gap identificati nell'analisi.

### Concrete Deliverables
1. Specifica HPC riscritta con HB96, 8 nodi, costi aggiornati
2. Architettura Pondus riscritta con AKS Windows, costi aggiornati
3. Piano migrazione aggiornato (Profis→Odoo, M365 upgrade, GiTea)
4. Budget offerta ricalcolato con tutte le modifiche
5. WBS riscritta per Variante D (no attività legacy GCP/hybrid)
6. Gantt con milestone allineati alla Variante D
7. Registro rischi aggiornato (rischi Azure-specific)
8. Nuovo Piano di Test specifico Variante D
9. Backup/DR — allineamento RPO HPC
10. Sicurezza — integrate policy organizzative ISO 27001
11. Report comparativo — allineamento costi D aggiornati

### Definition of Done
- [ ] Tutti i documenti elencati sono stati aggiornati/creati
- [ ] Ogni documento segue lo schema REQUISITI→SOLUZIONE→DIMENSIONAMENTO→COSTI
- [ ] Budget complessivo Variante D ricalcolato e coerente tra tutti i documenti
- [ ] WBS e Gantt non contengono più attività legacy (GCP, hybrid cloud)
- [ ] Registro rischi non contiene più R12 (vendor lock-in GCP)
- [ ] Costi HPC, Pondus, M365, egress, Managed Lustre sono allineati

### Must Have
- SKU HPC corretto da HB176 a HB96-96rs v4 (8 GB/core)
- 8 nodi HPC (non 5)
- Pondus su AKS Windows (non Container Apps Linux)
- Upgrade M365 Basic→Premium incluso nel budget
- Costi egress HPC inclusi nel budget
- Profis→Odoo come attività di migrazione
- WBS senza attività GCP/hybrid

### Must NOT Have (Guardrails)
- Non modificare la struttura architetturale generale della Variante D
- Non modificare le sezioni rete/VPN, backup/DR (già OK)
- Non aggiungere provider cloud aggiuntivi (resta single-cloud Azure)
- Non riaprire la discussione Variante A/C vs D
- Non modificare i costi di Odoo, BitBucket (invariati)

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** — ALL verification via document review e command-line checks.

### Test Decision
- **Infrastructure exists**: NO (markdown docs)
- **Automated tests**: None (document review)
- **Agent-Executed QA**: Each task verified by reading the output document and checking against requirements

### QA Policy
Every task MUST include verification steps (see TODO template).
Evidence saved to `.omo/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Document verification**: Read output file, compare against task requirements, check consistency with other documents
- **Cross-document consistency**: Verify budget figures match across offerta, HPC, Pondus docs
- **WBS/Gantt consistency**: Verify Gantt activities match WBS tasks, no orphan activities

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Foundation - core technical docs, MAX PARALLEL):
├── Task 1: HPC spec — rewrite SKU/nodi/costi [deep]
├── Task 2: Pondus arch — AKS Windows [deep]
├── Task 3: Migration plan — Profis→Odoo, M365, GiTea [deep]
├── Task 4: Backup/DR — RPO allineamento [quick]
├── Task 5: Security — policy organizzative [unspecified-high]
└── Task 6: Nuovo Piano di Test [unspecified-high]

Wave 2 (Budget + PM docs):
├── Task 7: Offerta economica — budget ricalcolato [deep]
├── Task 8: WBS — riscritta per Variante D [unspecified-high]
├── Task 9: Gantt — milestone allineati [unspecified-high]
└── Task 10: Registro rischi — aggiornato [quick]

Wave 3 (Cross-document consistency):
├── Task 11: Report comparativo — costi allineati [quick]
├── Task F1: Plan compliance audit [oracle]
├── Task F2: Cross-document consistency check [unspecified-high]
└── Task F3: Scope fidelity check [deep]

Critical Path: Task 1 → Task 7 → Task 11 → F1-F3 → user okay
Parallel Speedup: ~60% faster than sequential
Max Concurrent: 6 (Wave 1)
```

---

## TODOs

> **FORMAT**: Task labels use bare numbers: `1.`, `2.`, `3.`
> Final Verification Wave labels use `F1.`, `F2.`, etc.

- [ ] 1. **HPC Spec — Rewrite SKU, node count, costs**

  **What to do**:
  - Modify `D_Full_Cloud_Azure/04_Cluster_HPC/specifica_cluster_hpc.md`:
    - CHANGE SKU from HB176-96rs v4 to **HB96-96rs v4** (96 core, 768 GB RAM, 8 GB/core)
    - CHANGE node count from 5 to **8** nodes
    - Keep Front-end (Standard_D8s_v5), Managed Lustre (10 TB), Blob Storage (20 TB)
    - RECALCULATE all costs:
      - Compute: 8 HB96, 12h×220gg, 3 Reserved + 5 Spot = ~$XX/h → ~€YY/anno
      - Managed Lustre: $18.000/anno (~€17.000/anno)
      - Egress data: ~€1.500/anno
    - UPDATE benchmark performance table for HB96 (96 core vs 176)
    - REMOVE comparison tables that reference HB176 (keep ones comparing Azure vs GCP vs AWS)
    - ADD "Scenario A vs B" comparison table (16 total nodes vs 8 HB96)
    - ADD "Egress cost" section
    - UPDATE "3 anni costo totale" with new figures
    - Maintain existing structure: REQUISITI → SOLUZIONE → DIMENSIONAMENTO → COSTI

  **Must NOT do**:
  - Non modificare l'architettura InfiniBand (resta NDR 400)
  - Non modificare lo stack software (Slurm, Rocky Linux, OpenMPI)
  - Non eliminare il confronto con GCP/AWS

  **Recommended Agent Profile**:
  - **Category**: `deep` — goal-oriented autonomous work on a complex document
  - **Skills**: none needed (markdown document editing)
  - **Skills Evaluated but Omitted**:
    - `git-master`: Not git-specific

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5, 6)
  - **Blocks**: Task 7 (Offerta), Task 8 (WBS), Task 9 (Gantt)
  - **Blocked By**: None (can start immediately)

  **References**:
  - `D_Full_Cloud_Azure/04_Cluster_HPC/specifica_cluster_hpc.md` — Documento completo da riscrivere
  - `D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md` — Budget attuale per allineamento costi
  - `Condivisi/02_Project_Management/matrice_confronto.md` — Tabella confronto provider HPC
  - Azure HBv4 pricing: `https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/` (HB96-96rs v4)

  **Acceptance Criteria**:
  - [ ] SKU cambiato da HB176 a HB96-96rs v4 in tutto il documento
  - [ ] Nodi passati da 5 a 8
  - [ ] 8 GB/core verificato (768 GB / 96 core = 8 GB/core)
  - [ ] Costi ricalcolati con 8 HB96 (3 Reserved + 5 Spot, 12h×220gg)
  - [ ] Sezione egress cost aggiunta
  - [ ] Confronto Scenario A vs B presente
  - [ ] Budget HPC 3 anni aggiornato

  **QA Scenarios**:
  ```
  Scenario: Verifica SKU e RAM/core
    Tool: Bash (grep + calcolo)
    Preconditions: File modificato
    Steps:
      1. grep "HB96-96rs" specifica_cluster_hpc.md → trova riferimenti
      2. grep "768 GB / 96 core" o calcolo simile → verifica 8 GB/core
    Expected Result: SKU HB96 presente, 8 GB/core confermato
    Evidence: .omo/evidence/task-1-sku-check.txt

  Scenario: Verifica 8 nodi in tutto il documento
    Tool: Bash (grep)
    Steps:
      1. grep -c "8 nodi\|8× HB96\|8 nodi HB" specifica_cluster_hpc.md → almeno 3 occorrenze
    Expected Result: 8 nodi menzionato in sezioni chiave
    Evidence: .omo/evidence/task-1-nodes-check.txt

  Scenario: Verifica costi allineati
    Tool: Bash (grep)
    Steps:
      1. grep "€\|costo" specifica_cluster_hpc.md | head -10
    Expected Result: Costi espressi in EUR, coerenti con scenario realistico
    Evidence: .omo/evidence/task-1-costs-check.txt
  ```
  **Evidence to Capture**:
  - [ ] Output dei comandi grep per SKU, nodi, costi

  **Commit**: YES
  - Message: `fix(hpc): change SKU to HB96, 8 nodes, recalculate costs`
  - Files: `D_Full_Cloud_Azure/04_Cluster_HPC/specifica_cluster_hpc.md`

---

- [ ] 2. **Pondus Architecture — Rewrite for AKS Windows**

  **What to do**:
  - Modify `D_Full_Cloud_Azure/05_Pondus_App/architettura_pondus.md`:
    - CHANGE platform from "Azure Container Apps (Linux container)" to **"Azure Kubernetes Service (AKS) con Windows nodepool"**
    - UPDATE architecture diagram text (remove Container Apps, add AKS + Windows nodepool)
    - ADD Windows container considerations:
      - Dockerfile Windows base image (mcr.microsoft.com/dotnet/aspnet:8.0-nanoserver-1809)
      - AKS cluster with at least 1 Windows node pool
      - Azure Container Registry for Windows images
    - UPDATE component table:
      - Runtime: .NET 8 su Windows container (nanoserver)
      - Orchestrazione: AKS (Azure Kubernetes Service)
      - Registry: Azure Container Registry (invariato)
    - RECALCULATE costs:
      - AKS control plane: ~€75/mese
      - Windows nodepool (2 vCPU, 8 GB): ~€350-450/mese
      - Azure SQL Managed Instance: invariato (Hybrid Benefit)
      - Application Gateway v2 WAF: invariato
    - UPDATE "Piano di migrazione" section (adattare fasi per AKS)
    - Keep all existing sections (authentication, CDN, API Management, pubblicazione)

  **Must NOT do**:
  - Non modificare Azure SQL Managed Instance (resta invariato)
  - Non modificare Azure AD B2C / Entra ID
  - Non eliminare Azure Hybrid Benefit

  **Recommended Agent Profile**:
  - **Category**: `deep` — technical architecture document requiring domain knowledge
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5, 6)
  - **Blocks**: Task 7 (Offerta)
  - **Blocked By**: None

  **References**:
  - `D_Full_Cloud_Azure/05_Pondus_App/architettura_pondus.md` — Documento da riscrivere
  - Azure AKS Windows nodepool docs: `https://learn.microsoft.com/en-us/azure/aks/windows-faq`
  - AKS pricing: `https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/`
  - Windows Server pricing on Azure: `https://azure.microsoft.com/en-us/pricing/details/virtual-machines/windows/`

  **Acceptance Criteria**:
  - [ ] Container Apps Linux completamente sostituito da AKS Windows
  - [ ] Architettura diagramma aggiornato (testualmente)
  - [ ] Costi AKS Windows calcolati e inseriti
  - [ ] Piano di migrazione adattato per AKS
  - [ ] Nessun riferimento a Container Apps Linux rimasto

  **QA Scenarios**:
  ```
  Scenario: Verifica AKS Windows
    Tool: Bash (grep)
    Steps:
      1. grep -i "aks\|windows.*container\|windows.*nodepool" architettura_pondus.md → almeno 3 occorrenze
      2. grep -i "container apps\|container.*linux" architettura_pondus.md → 0 occorrenze
    Expected Result: AKS Windows presente, Container Apps Linux assente
    Evidence: .omo/evidence/task-2-aks-windows-check.txt

  Scenario: Verifica costi Pondus
    Tool: Bash (grep)
    Steps:
      1. grep "€\|costo\|Totale annuo" architettura_pondus.md
    Expected Result: Costi AKS Windows più alti di Container Apps Linux (~€4.500-6.500/anno)
    Evidence: .omo/evidence/task-2-costs-check.txt
  ```

  **Evidence to Capture**:
  - [ ] grep output per AKS/Container Apps
  - [ ] Costi aggiornati

  **Commit**: YES
  - Message: `fix(pondus): migrate from Container Apps Linux to AKS Windows`
  - Files: `D_Full_Cloud_Azure/05_Pondus_App/architettura_pondus.md`

---

- [ ] 3. **Migration Plan — Add Profis→Odoo, update M365, add GiTea→Azure DevOps costs**

  **What to do**:
  - Modify `D_Full_Cloud_Azure/06_Cloud_Migration/piano_migrazione_cloud.md`:
    - UPDATE "Mappatura Servizi" table:
      - Profis: "Odoo (unificato)" — aggiungi riga con migrazione dati contabili
      - GiTea→Azure DevOps: aggiungi costo licenze DevOps (~€30/mese per 5 utenti base)
    - ADD section "Migrazione Profis → Odoo":
      - Analisi dati contabili (1 settimana)
      - Migrazione dati (2 settimane)
      - Verifica quadratura contabile (1 settimana)
      - Costo stimato: ~€3.000 una tantum (6 gg sistemista)
    - UPDATE "M365" section:
      - Thema: 30 licenze Business Basic → upgrade a Business Premium
      - Pro Studio: 20 utenti Google Workspace → M365 Business Premium
      - Costo M365: 50 × €22 × 12 = €13.200/anno
      - Delta upgrade 30 utenti Basic→Premium: €16 × 30 × 12 = €5.760/anno
    - UPDATE Gantt di migrazione (sezione mermaid):
      - Aggiungere "Migrazione Profis→Odoo" dopo migrazione collaborazione
    - UPDATE "Costi migrazione" tabella:
      - Aggiungere €3.000 per migrazione Odoo
      - Aggiungere nota sui costi Azure DevOps (~€360/anno)
    - MAINTAIN existing structure: REQUISITI → MAPPATURA → STRATEGIA → COSTI

  **Must NOT do**:
  - Non modificare la strategia di migrazione principale (graduale con cut-over)
  - Non modificare Entra ID Connect (OK)
  - Non toccare migrazione HPC e Pondus (gestite da Task 1 e 2)

  **Recommended Agent Profile**:
  - **Category**: `deep` — requires understanding of business application migration
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4, 5, 6)
  - **Blocks**: Task 7 (Offerta)
  - **Blocked By**: None

  **References**:
  - `D_Full_Cloud_Azure/06_Cloud_Migration/piano_migrazione_cloud.md` — Documento da aggiornare
  - `Condivisi/01_Assessment/assessment_thema_consulting.md` — Sezione 7.1 Profis
  - `Condivisi/01_Assessment/assessment_prostudio.md` — Sezione Odoo
  - Azure DevOps pricing: `https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/`

  **Acceptance Criteria**:
  - [ ] Profis→Odoo aggiunto come attività di migrazione con costi
  - [ ] M365 upgrade da Basic a Premium documentato con costi
  - [ ] GiTea→Azure DevOps: costo incluso
  - [ ] Costo migrazione Odoo (€3.000) aggiunto a "Costi migrazione"
  - [ ] Gantt mermaid aggiornato

  **QA Scenarios**:
  ```
  Scenario: Verifica Profis→Odoo
    Tool: Bash (grep)
    Steps:
      1. grep -i "profis\|Odoo.*migrazione\|migrazione.*contab" piano_migrazione_cloud.md
    Expected Result: Sezione migrazione Profis→Odoo presente
    Evidence: .omo/evidence/task-3-profis-odoo.txt

  Scenario: Verifica M365 upgrade
    Tool: Bash (grep)
    Steps:
      1. grep -i "basic.*premium\|upgrade.*m365\|€13\.200" piano_migrazione_cloud.md
    Expected Result: Costo M365 Premium aggiornato
    Evidence: .omo/evidence/task-3-m365-upgrade.txt
  ```

  **Evidence to Capture**:
  - [ ] grep output per Profis/Odoo
  - [ ] Costi M365 aggiornati

  **Commit**: YES
  - Message: `fix(migration): add Profis→Odoo, update M365 costs, add GiTea→DevOps`
  - Files: `D_Full_Cloud_Azure/06_Cloud_Migration/piano_migrazione_cloud.md`

---

- [ ] 4. **Backup/DR — Align RPO for HPC**

  **What to do**:
  - Modify `D_Full_Cloud_Azure/07_Backup_DR/architettura_backup_dr.md`:
    - IDENTIFY RPO inconsistency: "Requisiti" section says RPO ≤4 ore, "RPO/RPO target" table says RPO ≤24 ore for HPC
    - RESOLVE: change HPC RPO to ≤4 ore (align with general requirements)
    - UPDATE "Backup per servizio" table: VM HBv4 backup frequency from "Giornaliero" to "Ogni 4 ore"
    - UPDATE Azure Backup Recovery Services Vault cost (more frequent backups = slightly higher cost)
    - UPDATE "RPO/RTO target" table: HPC RPO from ≤24 ore to ≤4 ore
    - VERIFY consistency with all other mentions of RPO in the document

  **Must NOT do**:
  - Non modificare RPO/RTO degli altri servizi (SQL, Container Apps, Blob, M365)
  - Non modificare l'architettura DR generale (resta West Europe → North Europe)

  **Recommended Agent Profile**:
  - **Category**: `quick` — small targeted fix
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 5, 6)
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `D_Full_Cloud_Azure/07_Backup_DR/architettura_backup_dr.md` — Documento da correggere
  - `Condivisi/01_Assessment/gap_analysis.md` — Gap #4: RPO servizi critici
  - Azure Backup pricing: `https://azure.microsoft.com/en-us/pricing/details/backup/`

  **Acceptance Criteria**:
  - [ ] HPC RPO cambiato da ≤24 ore a ≤4 ore (o "ogni 4 ore")
  - [ ] Backup VM HBv4 frequency updated to "Ogni 4 ore"
  - [ ] RPO consistent in tutte le sezioni del documento
  - [ ] Costo Azure Backup aggiornato se necessario

  **QA Scenarios**:
  ```
  Scenario: Verifica RPO HPC
    Tool: Bash (grep)
    Steps:
      1. grep -n "RPO\|24 ore\|4 ore\|ogni 4" architettura_backup_dr.md
    Expected Result: Nessun "RPO ≤24 ore" per HPC, sostituito con "≤4 ore" o "ogni 4 ore"
    Evidence: .omo/evidence/task-4-rpo-hpc.txt
  ```

  **Evidence to Capture**:
  - [ ] grep output RPO/HPC

  **Commit**: YES (group with Task 10)
  - Message: `fix(backup): align HPC RPO from 24h to 4h per requirements`
  - Files: `D_Full_Cloud_Azure/07_Backup_DR/architettura_backup_dr.md`

---

- [ ] 5. **Security — Add organizational ISO 27001 policies**

  **What to do**:
  - Modify `D_Full_Cloud_Azure/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md`:
    - ADD section "Procedure Organizzative ISO 27001" (non-technical controls):
      - **A.5 — Policy di sicurezza**: Bozza di Information Security Policy (principi, scope, responsabilità)
      - **A.6 — Organizzazione interna**: Ruoli e responsabilità di sicurezza, comitato di sicurezza
      - **A.16 — Incident Management**: Procedura di gestione incidenti (rilevamento, escalation, containment, recovery, lessons learned)
      - **A.12 — Operations**: Vulnerability management process (scansione mensile, remediation 30gg)
      - **A.18 — Compliance**: Review annuale della conformità, audit trail
    - UPDATE "Bozza Policy di Sicurezza" section to reference these new procedures
    - ADD draft templates for:
      - Incident Response Plan (template)
      - Vulnerability Management Procedure (template)
      - Access Review Procedure (template)
    - MAINTAIN existing technical controls (cifratura, MFA, VPN, Defender, Azure Policy)

  **Must NOT do**:
  - Non eliminare le sezioni tecniche esistenti
  - Non trasformare in documento legale (resta bozza tecnica)
  - Non aggiungere policy HR o GDPR non richieste

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high` — requires understanding of ISO 27001 organizational controls
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4, 6)
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `D_Full_Cloud_Azure/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md` — Documento da integrare
  - `Condivisi/01_Assessment/gap_analysis.md` — Gap #1, #5, #10, #13 (aree organizzative)
  - ISO 27001:2022 Annex A controls (A.5, A.6, A.16)

  **Acceptance Criteria**:
  - [ ] Sezione "Procedure Organizzative ISO 27001" aggiunta
  - [ ] A.5 Policy: bozza presente
  - [ ] A.6 Organizzazione: ruoli e responsabilità definiti
  - [ ] A.16 Incident Management: procedura presente
  - [ ] Vulnerability management process documentato
  - [ ] Template Incident Response, Vulnerability Management, Access Review inclusi

  **QA Scenarios**:
  ```
  Scenario: Verifica sezione organizzativa
    Tool: Bash (grep)
    Steps:
      1. grep -n "Procedure Organizzative\|A\.5\|A\.6\|A\.16\|Incident\|Vulnerability\|Access Review" requisiti_sicurezza_iso27001.md
    Expected Result: Sezioni organizzative presenti
    Evidence: .omo/evidence/task-5-org-policies.txt
  ```

  **Evidence to Capture**:
  - [ ] grep output sezioni organizzative

  **Commit**: YES
  - Message: `fix(security): add organizational ISO 27001 policies and procedures`
  - Files: `D_Full_Cloud_Azure/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md`

---

- [ ] 6. **New Document — Create Piano di Test for Variante D**

  **What to do**:
  - CREATE new file `D_Full_Cloud_Azure/piano_test.md`:
    - Header: "Piano di Test — Variante D (Full Cloud Azure)"
    - Premessa: scopo, ambito, criteri di successo
    - TEST per area:
      - **Rete/VPN**: connettività VPN Site-to-Site, P2S VPN, Bastion access, NSG rules
      - **HPC**: benchmark HPL, latenza MPI OSU, scheduling Slurm, nodi Spot recovery
      - **Pondus su AKS**: deploy Windows container, funzionalità C#, connettività DB, HTTPS
      - **Migrazione**: verifica integrità dati post-migrazione, rollback test
      - **Backup/DR**: restore file, failover SQL, Site Recovery drill, RPO/RTO verification
      - **Sicurezza**: MFA enforcement, Azure Policy compliance, vulnerability scan
    - Tabella: Test Case ID, Area, Descrizione, Precondizioni, Passi, Risultato Atteso, Responsabile
    - Template per report di test (esito, evidenze, note)

  **Must NOT do**:
  - Non duplicare i QA scenarios già presenti nei task del piano (sono per l'executor)
  - Non creare test UI/UX (non applicabile a documenti)
  - Non includere test non verificabili

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high` — test planning document
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 3, 4, 5)
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `Condivisi/02_Project_Management/wbs.md` — Sezione 7.0 Test e Collaudo
  - `Condivisi/02_Project_Management/gantt.md` — Timeline test
  - All technical documents for test coverage

  **Acceptance Criteria**:
  - [ ] File `piano_test.md` creato in `D_Full_Cloud_Azure/`
  - [ ] Copertura: Rete, HPC, Pondus, Migrazione, Backup/DR, Sicurezza
  - [ ] Almeno 3 test case per area (18+ totali)
  - [ ] Template report test incluso
  - [ ] Ogni test case ha: ID, descrizione, precondizioni, passi, risultato atteso

  **QA Scenarios**:
  ```
  Scenario: Verifica esistenza e copertura
    Tool: Bash
    Steps:
      1. Test-Path "D_Full_Cloud_Azure/piano_test.md" → True
      2. grep -c "Test Case" piano_test.md → ≥18
      3. grep -i "rete\|hpc\|pondus\|migrazione\|backup\|sicurezza" piano_test.md
    Expected Result: File presente, ≥18 test case, tutte le aree coperte
    Evidence: .omo/evidence/task-6-test-plan.txt
  ```

  **Evidence to Capture**:
  - [ ] Test-Path result
  - [ ] Test case count
  - [ ] Coverage per area

  **Commit**: YES
  - Message: `feat(test): create Piano di Test for Variante D`
  - Files: `D_Full_Cloud_Azure/piano_test.md`

---

- [ ] 7. **Offerta Economica — Recalculate full budget with all corrections**

  **What to do**:
  - Modify `D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md`:
    - UPDATE "Riepilogo Variante" HPC: da "5 nodi (3 Reserved + 2 spot)" a **"8 nodi (3 Reserved + 5 spot)"**
    - UPDATE "Costi una tantum":
      - Aggiungi "Migrazione Profis→Odoo: €3.000"
      - Totale una tantum: €22.300 → **€25.300**
    - UPDATE "Costi HW/SW/Cloud (primo anno)":
      - Compute HPC: da ~€28.700 a **~€55.000** (8 HB96, 3R+5S, 12h×220gg)
      - Azure Managed Lustre: da ~€8.100 a **~€17.000** (allineamento costo reale)
      - Pondus (Container Apps→AKS Windows): da ~€3.000 a **~€6.500**
      - M365 Business Premium: da ~€10.200 a **~€13.200** (50 × €22 × 12)
      - Aggiungi "Egress data HPC: ~€1.500"
      - Totale ricorrente anno 1: da ~€92.740 a **~€120.740**
    - UPDATE "Riepilogo Budget 3 Anni":
      - Ricorrente anno 1: ~€120.740
      - Ricorrente anno 2-3: ~€241.480
      - Totale 3 anni: **~€387.520** (senza extra manodopera)
    - UPDATE "Extra manodopera":
      - Aggiungi 6 gg per migrazione Odoo: +€3.000
      - Totale extra: ~€74.000 → **~€77.000**
    - UPDATE "Totale complessivo 3 anni": da ~€374.520 a **~€464.520**
    - UPDATE "Margine residuo": da +€326.480 a **+€236.480** ✅
    - UPDATE "Confronto con Budget Cliente" table
    - UPDATE "Risparmi rispetto a GCP" (sezioni non cambiate, OK)
    - VERIFY all totals are consistent

  **Must NOT do**:
  - Non modificare i costi invariati (Odoo, BitBucket, networking base, backup base, sicurezza base)
  - Non modificare il formato del documento

  **Recommended Agent Profile**:
  - **Category**: `deep` — careful budget recalculation with multiple interdependent figures
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2 (sequential after Task 1, 2, 3)
  - **Blocks**: Task 11 (Report comparativo)
  - **Blocked By**: Task 1 (HPC costs), Task 2 (Pondus costs), Task 3 (Migration costs)

  **References**:
  - `D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md` — Documento da riscrivere
  - Task 1 output: HPC costs recalculated
  - Task 2 output: Pondus AKS Windows costs
  - Task 3 output: Migration costs (Odoo, M365, GiTea)
  - Azure HB96 pricing: ~$3,60/h on-demand, ~$1,44/h 3Y Reserved, ~$0,73/h Spot
  - M365 Business Premium: €22/user/month

  **Acceptance Criteria**:
  - [ ] Compute HPC: 8 HB96, 3R+5S, 12h×220gg = ~€55.000/anno
  - [ ] Managed Lustre: €17.000/anno (non più €8.100)
  - [ ] Pondus: €6.500/anno (non più €3.000)
  - [ ] M365: €13.200/anno (non più €10.200)
  - [ ] Egress: €1.500/anno aggiunto
  - [ ] Una tantum: €25.300 (aggiunto Odoo migration €3.000)
  - [ ] Extra manodopera: €77.000 (aggiunto +€3.000)
  - [ ] Totale 3 anni: ~€464.520
  - [ ] Margine residuo: +€236.480 ✅ (dentro budget €701k)
  - [ ] Tutti i totali sono aritmeticamente corretti

  **QA Scenarios**:
  ```
  Scenario: Verifica aritmetica budget
    Tool: Bash (calcolo manuale)
    Steps:
      1. grep "~€" offerta_tecnico_economica.md | head -20
      2. Sommare voci "Costi HW/SW/Cloud (primo anno)" → deve dare ~€120.740
      3. Sommare una tantum + anno 1 + anno 2-3 + extra → deve dare ~€464.520
    Expected Result: Totali aritmeticamente corretti
    Evidence: .omo/evidence/task-7-budget-calc.txt

  Scenario: Verifica budget entro margine
    Tool: Bash (calcolo)
    Steps:
      1. Calcolare 701000 - 464520 = 236480
    Expected Result: Margine ≥ €0
    Evidence: .omo/evidence/task-7-budget-margin.txt
  ```

  **Evidence to Capture**:
  - [ ] Output verifica aritmetica
  - [ ] Margine residuo

  **Commit**: YES
  - Message: `fix(budget): recalculate all costs for HB96, AKS Windows, M365 Premium`
  - Files: `D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md`

---

- [ ] 8. **WBS — Rewrite for Variante D (remove legacy, add Azure-specific)**

  **What to do**:
  - Modify `Condivisi/02_Project_Management/wbs.md`:
    - REVIEW all sections for Variante D compatibility
    - REMOVE or REPLACE these activities (no longer needed):
      - `3.4 Progettazione migrazione cloud ibrido` → Sostituire con "Progettazione migrazione Azure"
      - `5.1.5 Configurazione hybrid cloud connectivity (GCP VPN interconnect)` → Rimuovere
      - `5.2 Configurazione server e virtualizzazione` → Non più necessario (full cloud)
      - `6.2.1 Integrazione AD Samba4 con Google Workspace (GCDS sync)` → Sostituire con Entra ID Connect
    - ADD these activities:
      - `3.4 Progettazione migrazione Azure`: setup tenant, landing zone, subscription
      - `3.5 Progettazione identità Entra ID`: sync Samba4→Entra ID, Conditional Access
      - `5.1 Setup Azure tenant e landing zone`: subscription, RBAC, Azure Policy
      - `5.2 Configurazione Entra ID Connect`: sync da Samba4 AD, password hash sync
      - `5.3 Deploy cluster HPC Azure HBv4`: CycleCloud, Slurm, test benchmarks
      - `5.4 Deploy Pondus su AKS Windows`: AKS cluster, Windows nodepool, container registry
      - `5.5 Configurazione backup M365`: Microsoft 365 Backup setup
      - `6.4 Migrazione Profis→Odoo`: export dati, migrazione, verifica quadratura
    - UPDATE "Riepilogo effort per fase": ricalcolare gg/uomo
    - VERIFY total effort is still realistic (~156 gg/uomo, può variare)

  **Must NOT do**:
  - Non eliminare le fasi di Project Management, Assessment, Test, Formazione (rimangono valide)
  - Non modificare la struttura gerarchica a 3 livelli

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high` — WBS restructuring
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Task 9)
  - **Blocks**: None
  - **Blocked By**: None (can use existing WBS as base)

  **References**:
  - `Condivisi/02_Project_Management/wbs.md` — Documento da riscrivere
  - `D_Full_Cloud_Azure/06_Cloud_Migration/piano_migrazione_cloud.md` — Migration activities
  - `D_Full_Cloud_Azure/04_Cluster_HPC/specifica_cluster_hpc.md` — HPC deployment
  - `D_Full_Cloud_Azure/05_Pondus_App/architettura_pondus.md` — Pondus on AKS

  **Acceptance Criteria**:
  - [ ] Tutte le attività legacy (GCP, hybrid cloud, GCDS) rimosse
  - [ ] Aggiunte attività: setup tenant, Entra ID, HPC HBv4, AKS Windows, backup M365, Profis→Odoo
  - [ ] Fase 3.4 rinominata da "migrazione cloud ibrido" a "migrazione Azure"
  - [ ] Riepilogo effort aggiornato
  - [ ] Nessuna attività GCP o GCDS rimasta

  **QA Scenarios**:
  ```
  Scenario: Verifica rimozione legacy
    Tool: Bash (grep)
    Steps:
      1. grep -i "gcp\|gcds\|hybrid cloud\|google workspace" wbs.md
    Expected Result: 0 occorrenze di attività legacy GCP
    Evidence: .omo/evidence/task-8-wbs-legacy-removed.txt

  Scenario: Verifica nuove attività
    Tool: Bash (grep)
    Steps:
      1. grep -i "entra id\|aks windows\|hbv4\|hb96\|profis.*odo" wbs.md
    Expected Result: Nuove attività presenti
    Evidence: .omo/evidence/task-8-wbs-new.txt
  ```

  **Evidence to Capture**:
  - [ ] grep legacy activities (should be 0)
  - [ ] grep new activities (should be present)

  **Commit**: YES
  - Message: `fix(wbs): rewrite for Variante D, remove legacy GCP/hybrid activities`
  - Files: `Condivisi/02_Project_Management/wbs.md`

---

- [ ] 9. **Gantt — Align milestones to Variante D**

  **What to do**:
  - Modify `Condivisi/02_Project_Management/gantt.md`:
    - REVIEW and UPDATE all sections for Variante D compatibility
    - UPDATE "Diagramma Gantt (Mermaid)" section:
      - Section "Assessment": OK (invariato)
      - Section "Progettazione": da "Progettazione architettura" a **"Progettazione Azure"**
      - Section "Approvvigionamento": da "Ordine e attesa HW" a **"Setup Azure tenant + licenses"** (no HW da aspettare)
      - Section "Migrazione": aggiornare per includere migrazione Odoo, M365, HPC, Pondus
    - UPDATE "Tabella Riepilogativa":
      - "Ordine e attesa HW" (42 gg) → da rimuovere o sostituire con "Setup tenant e licenze" (14 gg)
      - Dipendenze da aggiornare
    - MILESTONE:
      - M3 "Ordine HW Effettuato" → da rimuovere
      - M4 "Consegna HW" → da rimuovere  
      - Aggiungere M3 "Tenant Azure operativo"
      - Aggiungere M4 "Entra ID Connect attivo"
      - Aggiungere M5 "Cluster HPC deployato"
    - UPDATE "Note": rimuovere riferimenti a consegna HW, aggiornare per full cloud
    - MAINTAIN same overall duration (12 settimane) and timeline structure

  **Must NOT do**:
  - Non ridurre la durata complessiva (12 settimane)
  - Non eliminare la finestra di shutdown (7 giorni max)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high` — project timeline restructuring
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Task 8)
  - **Blocks**: None
  - **Blocked By**: Task 8 (WBS) — logical dependency (Gantt derives from WBS)

  **References**:
  - `Condivisi/02_Project_Management/gantt.md` — Documento da riscrivere
  - Task 8 output: Updated WBS
  - `D_Full_Cloud_Azure/06_Cloud_Migration/piano_migrazione_cloud.md` — Migration timeline

  **Acceptance Criteria**:
  - [ ] "Ordine e attesa HW" rimosso o sostituito
  - [ ] Milestone HW rimosse, milestone Azure aggiunte
  - [ ] Durata 12 settimane invariata
  - [ ] Shutdown 7 giorni mantenuto
  - [ ] Mermaid diagram funzionante (sintassi valida)

  **QA Scenarios**:
  ```
  Scenario: Verifica milestone HW rimosse
    Tool: Bash (grep)
    Steps:
      1. grep -i "consegna hw\|ordine hw\|attesa hw" gantt.md
    Expected Result: 0 occorrenze
    Evidence: .omo/evidence/task-9-gantt-legacy.txt

  Scenario: Verifica nuove milestone
    Tool: Bash (grep)
    Steps:
      1. grep -i "tenant azure\|entra id\|cluster hpc deploy" gantt.md
    Expected Result: Nuove milestone presenti
    Evidence: .omo/evidence/task-9-gantt-new.txt
  ```

  **Evidence to Capture**:
  - [ ] grep legacy milestones (0)
  - [ ] grep new milestones (present)

  **Commit**: YES
  - Message: `fix(gantt): align milestones to Variante D, remove HW procurement`
  - Files: `Condivisi/02_Project_Management/gantt.md`

---

- [ ] 10. **Risk Register — Update for Variante D**

  **What to do**:
  - Modify `Condivisi/02_Project_Management/registro_rischi.md`:
    - REMOVE R12 "Vendor lock-in GCP" — non più applicabile
    - ADD new risk: **Vendor lock-in Azure** (sostituisce R12)
      - Probabilità: Media (3), Impatto: Alto (4), Punteggio: 12
      - Mitigazione: Architettura containerizzata (Pondus su AKS), DB SQL standard, codice portabile
    - ADD new risk: **Azure cost escalation HPC** (rischio economico su 3 anni)
      - Probabilità: Media (3), Impatto: Alto (4), Punteggio: 12
      - Mitigazione: Reserved Instances 3 anni bloccano prezzo, alert di spesa, budget Azure
    - ADD new risk: **Egress cost imprevisti HPC**
      - Probabilità: Alta (4), Impatto: Medio (3), Punteggio: 12
      - Mitigazione: Monitoraggio traffico, alert su soglia, compressione risultati prima del download
    - ADD new risk: **Compatibilità Windows container Pondus**
      - Probabilità: Bassa (2), Impatto: Alto (4), Punteggio: 8
      - Mitigazione: Test di compatibilità pre-migrazione, fallback su VM Windows IIS
    - UPDATE "Top 5 rischi critici" with new risks
    - UPDATE "Matrice dei rischi" text diagram

  **Must NOT do**:
  - Non modificare i rischi R1-R11 che restano validi
  - Non modificare la struttura del registro

  **Recommended Agent Profile**:
  - **Category**: `quick` — targeted updates
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Task 8, 9)
  - **Blocks**: None
  - **Blocked By**: None

  **References**:
  - `Condivisi/02_Project_Management/registro_rischi.md` — Documento da aggiornare
  - `REPORT_COMPARATIVO_VARIANTI.md` — SWOT analysis for Variante D (vendor lock-in risk)
  - Task 1 output: HPC cost structure
  - Task 2 output: Pondus AKS Windows compatibility

  **Acceptance Criteria**:
  - [ ] R12 "Vendor lock-in GCP" rimosso
  - [ ] Nuovo rischio "Vendor lock-in Azure" presente (al posto di R12)
  - [ ] Nuovo rischio "Azure cost escalation HPC" presente
  - [ ] Nuovo rischio "Egress cost imprevisti HPC" presente
  - [ ] Nuovo rischio "Compatibilità Windows container Pondus" presente
  - [ ] Top 5 rischi critici aggiornato

  **QA Scenarios**:
  ```
  Scenario: Verifica R12 e nuovi rischi
    Tool: Bash (grep)
    Steps:
      1. grep "vendor lock-in GCP\|R12" registro_rischi.md → 0 occorrenze
      2. grep -i "vendor lock-in Azure\|cost escalation\|egress\|compatibilità.*windows.*pondus" registro_rischi.md
    Expected Result: GCP risk rimosso, Azure risks presenti
    Evidence: .omo/evidence/task-10-risk-register.txt
  ```

  **Evidence to Capture**:
  - [ ] grep R12 (should be 0)
  - [ ] grep new risks (should be present)

  **Commit**: YES (group with Task 4)
  - Message: `fix(risks): update risk register for Variante D, replace GCP with Azure risks`
  - Files: `Condivisi/02_Project_Management/registro_rischi.md`

---

- [ ] 11. **Report Comparativo — Align cost figures**

  **What to do**:
  - Modify `REPORT_COMPARATIVO_VARIANTI.md`:
    - UPDATE Section 9 "Confronto Economico":
      - Variante D costi aggiornati con nuovo budget (Task 7 output)
      - Ricalcolare delta vs Variante A e C
      - Ricalcolare "Risparmio Variante D vs A"
    - UPDATE Section 9.2 "Costi Ricorrenti Annuali":
      - Compute HPC: da ~€28.700 a **~€55.000**
      - Managed Lustre: da ~€8.100 a **~€17.000**
      - Pondus: da ~€17.400 a **~€20.900** (AKS Windows)
      - M365: da €10.200 a **€13.200**
      - Aggiungere "Egress data HPC: ~€1.500"
    - UPDATE Section 9.3 "Riepilogo 3 Anni":
      - Una tantum: da €22.300 a **€25.300**
      - Extra manodopera: da €74.000 a **€77.000**
      - Ricorrente anno 1: da ~€92.740 a **~€120.740**
      - Totale 3 anni: da ~€374.520 a **~€464.520**
    - UPDATE Section 1 "Executive Summary":
      - Costo totale 3 anni Variante D: ~€464.520
      - Delta budget: +€236.480
    - VERIFY all cross-document consistency

  **Must NOT do**:
  - Non modificare le sezioni di confronto tecnico (HPC performance, DR, sicurezza)
  - Non modificare le varianti A e C
  - Non modificare la SWOT analysis

  **Recommended Agent Profile**:
  - **Category**: `quick` — targeted cost alignment
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 3 (after Task 7)
  - **Blocks**: None
  - **Blocked By**: Task 7 (Offerta costs)

  **References**:
  - `REPORT_COMPARATIVO_VARIANTI.md` — Documento da aggiornare
  - Task 7 output: Updated offer budget

  **Acceptance Criteria**:
  - [ ] Costi Variante D allineati con offerta (Task 7)
  - [ ] Executive summary aggiornato (~€464.520, margine +€236.480)
  - [ ] Tabella costi ricorrenti aggiornata
  - [ ] Riepilogo 3 anni coerente
  - [ ] Delta vs A e C ricalcolati

  **QA Scenarios**:
  ```
  Scenario: Verifica costi allineati con offerta
    Tool: Bash (grep + confronto)
    Steps:
      1. grep "Totale 3 anni\|~€" REPORT_COMPARATIVO_VARIANTI.md | grep "D — Full"
      2. Confrontare con offerta_tecnico_economica.md
    Expected Result: Costi Variante D corrispondono tra i due documenti
    Evidence: .omo/evidence/task-11-report-comparativo.txt
  ```

  **Evidence to Capture**:
  - [ ] Costi Variante D da report comparativo
  - [ ] Verifica corrispondenza con offerta

  **Commit**: YES
  - Message: `fix(report): align Variante D costs with updated budget`
  - Files: `REPORT_COMPARATIVO_VARIANTI.md`

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 3 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
>
> **Do NOT auto-proceed after verification.**

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. Verify each "Must Have" is implemented. Check each "Must NOT Have" for forbidden patterns. Compare deliverables against plan tasks.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Cross-Document Consistency Check** — `unspecified-high`
  Read all modified documents and verify budget figures match across:
  - Offerta (Task 7) vs Report Comparativo (Task 11)
  - Offerta (Task 7) vs HPC Spec (Task 1)
  - Offerta (Task 7) vs Pondus (Task 2)
  - WBS (Task 8) vs Gantt (Task 9) — no orphan activities
  - Report any figure discrepancies
  Output: `Figures [N/N consistent] | WBS↔Gantt [CLEAN/issues] | VERDICT`

- [ ] F3. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual diff (git log/diff). Verify 1:1 — everything in spec was built (no missing), nothing beyond spec was built (no creep). Check "Must NOT do" compliance.
  Output: `Tasks [N/N compliant] | Scope creep [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

- **Task 1**: `fix(hpc): change SKU to HB96, 8 nodes, recalculate costs`
- **Task 2**: `fix(pondus): migrate from Container Apps Linux to AKS Windows`
- **Task 3**: `fix(migration): add Profis→Odoo, update M365 costs, add GiTea→DevOps`
- **Task 4+10**: `fix(backup): align RPO; fix(risks): update risk register for Variante D`
- **Task 5**: `fix(security): add organizational ISO 27001 policies and procedures`
- **Task 6**: `feat(test): create Piano di Test for Variante D`
- **Task 7**: `fix(budget): recalculate all costs for HB96, AKS Windows, M365 Premium`
- **Task 8**: `fix(wbs): rewrite for Variante D, remove legacy GCP/hybrid activities`
- **Task 9**: `fix(gantt): align milestones to Variante D, remove HW procurement`
- **Task 11**: `fix(report): align Variante D costs with updated budget`

---

## Success Criteria

### Verification Commands
```bash
# Verifica SKU HPC su tutti i documenti
grep -r "HB176\|HB96" D_Full_Cloud_Azure/ --include="*.md"
# Dovrebbe mostrare solo HB96

# Verifica nessun riferimento GCP legacy in WBS
grep -r -i "gcp\|gcds\|hybrid cloud connectivity" Condivisi/02_Project_Management/wbs.md
# Dovrebbe essere vuoto

# Verifica nessun Container Apps Linux in Pondus
grep -r -i "container apps" D_Full_Cloud_Azure/05_Pondus_App/ --include="*.md"
# Dovrebbe essere vuoto (sostituito da AKS)

# Verifica M365 cost allineati
grep "€13.200\|€10.200" Condivisi/02_Project_Management/matrice_confronto.md
# Dovrebbe mostrare €13.200 (non €10.200)

# Verifica R12 rimosso da risk register
grep "R12" Condivisi/02_Project_Management/registro_rischi.md
# Dovrebbe essere vuoto (R12 sostituito)
```

### Final Checklist
- [ ] Tutti i 9 documenti esistenti modificati
- [ ] 1 nuovo documento creato (piano_test.md)
- [ ] SKU HPC: HB96-96rs v4 in tutti i documenti
- [ ] Nodi HPC: 8 in tutti i documenti
- [ ] Pondus: AKS Windows (no Container Apps Linux)
- [ ] M365: Business Premium (€13.200/anno)
- [ ] Costi allineati tra offerta, report comparativo, documenti tecnici
- [ ] WBS: nessuna attività GCP/hybrid
- [ ] Gantt: nessuna milestone HW
- [ ] Rischi: R12 rimosso, nuovi rischi Azure presenti
- [ ] Budget totale 3 anni: ~€464.520 (entro €701.000)
- [ ] Margine residuo: +€236.480 ✅

