# Piano: Project Work — Offerta Infrastruttura IT TP Group

## TL;DR

> **Quick Summary**: Sviluppare il progetto completo di offerta tecnico/economica per l'integrazione IT di TP Group (fusione Thema Consulting + Pro Studio), in 3 varianti architetturali parallele: Full Cloud (GCP), On-Premise e Ibrido. Prodotto finale: full package di documentazione tecnica, project management e offerta economica in formato Markdown.
>
> **Deliverables**:
> - Documenti condivisi (Assessment AS-IS, Project Charter, WBS, Gantt, RASCI, Risk Register)
> - 3 set di documenti tecnici (Rete/VPN, HPC, Pondus, Cloud Migration, Backup/DR, Sicurezza ISO 27001) — uno per variante
> - 3 Offerte Tecnico/Economiche complete (una per variante)
> - Matrice di confronto tra varianti
>
> **Estimated Effort**: XL (35+ task, 3 varianti parallele)
> **Parallel Execution**: YES — 4 waves principali + 4 final reviews
> **Critical Path**: Task 1 → 2-4 → 7 → 8 → 14/21/28 → 29-31 → 32 → F1-F4

---

## Context

### Original Request
Sviluppare il piano per il project work "CSP - BF 2025-27 - Learning by project" — offerta tecnico/economica per l'infrastruttura IT di TP Group, basata sui documenti cliente (estratto_progetto.md, Domande_Project_Edoardo_FORMATTED.xlsx, SOLUZIONE.docx).

### Interview Summary
**Key Discussions**:
- **Directory**: `23_Project_Work_e_Laboratori/03_Progetti/ProjectWork_Infrastruttura_IT/`
- **Da zero**: Ignorare completamente i file esistenti in `TP_Group/` — progetto autonomo
- **3 varianti in parallelo**: Full Cloud (GCP) + On-Premise + Ibrido
- **Full package**: Assessment + Documenti tecnici + PM + Offerta economica
- **Formato**: Solo Markdown (.md)
- **Ruolo**: Fornitore/Proponente
- **Domande cliente aperte**: Lasciate in sospeso (HPC definitivo, connettività sede, retention dati)

**Research Findings**:
- Scenario completo in `01_Materiale/estratto_progetto.md` (9 pagine): assessment, vincoli, budget 520k€, requisiti ISO 27001, criteri valutazione
- Domande/risposte cliente estratte da Excel + Word (budget aggiornato €580k on-prem / €525k cloud, extra €181k manodopera, 12 settimane, 7gg shutdown, 3 anni ciclo vita)
- Strategia suggerita dal Word SOLUZIONE.docx: "principalmente cloud" ma l'utente ha chiesto 3 varianti complete

### Path Note (importante)
Tutti i file sorgente (`01_Materiale/`) sono in `23_Project_Work_e_Laboratori/01_Materiale/` dalla root del workspace. I References nei task usano path relativi a questa directory. L'esecutore deve anteporre `23_Project_Work_e_Laboratori/` dove necessario.

### Metis Review
**Identified Gaps** (addressed):
- **Struttura a matrice**: Documenti condivisi (AS-IS, PM) + 3 cartelle variante —riduce duplicazione, garantisce coerenza
- **Budget integrity check**: Ogni variante deve quadrare entro 520k€ o dichiarare scostamento
- **Matrice di confronto**: Necessaria tabella riepilogativa per confrontare le 3 varianti
- **Guardrail ISO 27001**: Specificare se "allineamento" o "certificazione"
- **Scope creep prevention**: Banditi runbook operativi, analisi legale, piani formazione, benchmark competitor

---

## Work Objectives

### Core Objective
Produrre il pacchetto completo di documentazione tecnica, project management e offerta economica per il progetto di integrazione IT di TP Group, in 3 varianti architetturali confrontabili.

### Concrete Deliverables
- **Documenti Condivisi** (1 set):
  - Assessment AS-IS (Thema + Pro Studio + Gap Analysis)
  - Project Charter
  - WBS, Gantt, Matrice RASCI, Registro Rischi
- **Documenti Variante** (3 set identici per struttura, diversi per contenuto):
  - Progettazione Rete/VPN
  - Specifica Cluster HPC
  - Architettura Pondus & Migrazione
  - Piano Cloud Migration
  - Architettura Backup/DR
  - Requisiti Sicurezza ISO 27001
  - Offerta Tecnico/Economica
- **Matrice di Confronto** (trasversale alle 3 varianti)

### Definition of Done
- [ ] Ogni documento esiste in formato `.md` nella directory corretta
- [ ] Ogni documento segue la struttura: REQUISITI → SOLUZIONE → DIMENSIONAMENTO → COSTI
- [ ] Ogni variante è autocoerente (dati, numeri, scelte tecniche non contraddittori)
- [ ] Budget integrity: somma voci economiche ≤ 520k€ (o scostamento motivato)
- [ ] Matrice di confronto completata con costi/rischi/performance/compliance per tutte 3 le varianti
- [ ] I vincoli ISO 27001 sono coperti in ogni variante

### Must Have
- Assessment AS-IS completo (Thema + Pro Studio) — documento condiviso, scritto UNA volta
- 3 varianti complete e confrontabili (stessa struttura, metriche, profondità)
- Offerta Tecnico/Economica con tutte le 10 sezioni richieste dal capitolato
- WBS (minimo 3 livelli) + Gantt con milestone verificabili
- Matrice di confronto con: Costo totale, Rischio, Compliance ISO, Performance HPC, Scalabilità, Tempo, Complessità
- Ogni sezione tecnica segue format: REQUISITI → SOLUZIONE → DIMENSIONAMENTO → COSTI
- Vincoli temporali (12 settimane attive, 7gg shutdown) riflessi nel Gantt

### Must NOT Have (Guardrails)
- **NON** leggere/copiare file dalla cartella `TP_Group/` esistente
- **NON** includere runbook operativi, script di deploy, comandi specifici
- **NON** includere analisi legale, contrattuale o fiscale
- **NON** includere piani di formazione o change management dettagliato
- **NON** includere benchmark competitor o analisi di mercato
- **NON** tradurre in inglese — solo italiano
- **NON** lasciare placeholder generici ("[DA DEFINIRE]", "[COSTO]", "[NOME]")
- **NON** superare la profondità di dettaglio richiesta (design document, non implementation spec)

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — Tutta la verifica è agent-executed.
> Trattandosi di documentazione progettuale e non codice, la verifica si concentra su: coerenza interna, completezza strutturale, budget integrity e vincoli temporali.

### Test Decision
- **Infrastructure exists**: NO (non è un progetto software)
- **Automated tests**: NONE (documentazione progettuale)
- **Verification method**: Agent-executed QA tramite lettura file, grep incrociato, e validazione strutturale

### QA Policy
Ogni task produce documenti `.md` verificabili con:
- **Bash (grep/glob)**: Verifica esistenza file, coerenza dati (es. conteggio dipendenti), assenza placeholder
- **Bash (script Python)**: Validazione incrociata budget (somma voci ≤ 520k€), date Gantt (≤ 12 settimane)
- **Read**: Lettura sezioni per verifica format REQUISITI→SOLUZIONE→DIMENSIONAMENTO→COSTI
- Evidenza salvata in `.omo/evidence/task-{N}/{scenario-slug}.txt`

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — foundation + shared docs):
├── Task 1: Scaffolding directory structure + README
├── Task 2: Assessment AS-IS Thema Consulting
├── Task 3: Assessment AS-IS Pro Studio
├── Task 4: Gap Analysis
├── Task 5: Project Charter
├── Task 6: WBS (Work Breakdown Structure)
└── Task 7: Gantt di progetto

Wave 2 (After Wave 1 — Variante A: Full Cloud GCP, MAX PARALLEL):
├── Task 8:  A — Progettazione Rete/VPN (Full Cloud GCP)
├── Task 9:  A — Specifica Cluster HPC (Full Cloud GCP)
├── Task 10: A — Architettura Pondus & Migrazione (Full Cloud GCP)
├── Task 11: A — Piano Cloud Migration (Full Cloud GCP)
├── Task 12: A — Architettura Backup/DR (Full Cloud GCP)
└── Task 13: A — Requisiti Sicurezza ISO 27001 (Full Cloud GCP)

Wave 2b (Wave 1 + parallel to Wave 2 — Variante B: On-Premise):
├── Task 14: B — Progettazione Rete/VPN (On-Premise)
├── Task 15: B — Specifica Cluster HPC (On-Premise)
├── Task 16: B — Architettura Pondus & Migrazione (On-Premise)
├── Task 17: B — Piano Upgrade Infrastruttura (On-Premise)
├── Task 18: B — Architettura Backup/DR (On-Premise)
└── Task 19: B — Requisiti Sicurezza ISO 27001 (On-Premise)

Wave 2c (Wave 1 + parallel to Waves 2/2b — Variante C: Ibrido):
├── Task 20: C — Progettazione Rete/VPN (Ibrido)
├── Task 21: C — Specifica Cluster HPC (Ibrido)
├── Task 22: C — Architettura Pondus & Migrazione (Ibrido)
├── Task 23: C — Strategia Cloud Ibrida (Ibrido)
├── Task 24: C — Architettura Backup/DR (Ibrido)
└── Task 25: C — Requisiti Sicurezza ISO 27001 (Ibrido)

Wave 3 (After Waves 2/2b/2c — Offerte + Confronto):
├── Task 26: A — Offerta Tecnico/Economica (Full Cloud GCP)
├── Task 27: B — Offerta Tecnico/Economica (On-Premise)
├── Task 28: C — Offerta Tecnico/Economica (Ibrido)
├── Task 29: Matrice di Confronto tra Varianti
├── Task 30: Registro Rischi
├── Task 31: Matrice RASCI
└── Task 32: Template Report di Avanzamento

Wave FINAL (After ALL tasks — 4 parallel reviews):
├── Task F1: Plan Compliance Audit (oracle)
├── Task F2: Coerenza e Budget Integrity (unspecified-high)
├── Task F3: Completezza Documentale (unspecified-high)
└── Task F4: Scope Fidelity Check (deep)
```

### Dependency Matrix (abbreviated)

| Task | Blocked By | Blocks |
|------|-----------|--------|
| 1 (scaffolding) | - | 2,3,5,6,7 |
| 2,3,4 (assessment) | 1 | 5,8-25 |
| 5,6,7 (PM base) | 1 | 26-32 |
| 8-13 (Var A docs) | 1,2,3,4 | 26 |
| 14-19 (Var B docs) | 1,2,3,4 | 27 |
| 20-25 (Var C docs) | 1,2,3,4 | 28 |
| 26-28 (Offerte) | 5-25 | 29 |
| 29-32 (PM finali) | 5,6,7,26-28 | F1-F4 |
| F1-F4 (Review) | 1-32 | user ok |

### Agent Dispatch Summary

| Wave | Agents | Tasks |
|------|--------|-------|
| 1 | 7 | T1 → `quick`, T2-T4 → `unspecified-high`, T5-T7 → `unspecified-high` |
| 2 | 6 | T8-T13 → `unspecified-high` (1 agent per task se parallelo) |
| 2b | 6 | T14-T19 → `unspecified-high` |
| 2c | 6 | T20-T25 → `unspecified-high` |
| 3 | 7 | T26-T28 → `unspecified-high`, T29 → `unspecified-high`, T30-T32 → `unspecified-high` |
| FINAL | 4 | F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep` |

---

## TODOs

- [x] 1. Scaffolding — struttura directory e README

  **What to do**:
  - Creare la struttura a matrice del progetto:
    ```
    03_Progetti/ProjectWork_Infrastruttura_IT/
    ├── README.md
    ├── Condivisi/
    │   ├── 01_Assessment/
    │   └── 02_Project_Management/
    ├── A_Full_Cloud_GCP/
    │   ├── 03_Rete_VPN/
    │   ├── 04_Cluster_HPC/
    │   ├── 05_Pondus_App/
    │   ├── 06_Cloud_Migration/
    │   ├── 07_Backup_DR/
    │   ├── 08_Sicurezza_ISO27001/
    │   └── 09_Offerta/
    ├── B_On_Premise/
    │   └── ... stessa struttura ...
    └── C_Ibrido/
        └── ... stessa struttura ...
    ```
  - Creare README.md con: panoramica progetto, scenario, struttura directory, istruzioni di navigazione
  - Aggiungere un file `.gitkeep` in ogni directory vuota

  **Must NOT do**:
  - Non creare file nella directory `TP_Group/`
  - Non includere template generici

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: NO (foundation)
  - **Parallel Group**: Wave 1
  - **Blocks**: Tasks 2-7
  - **Blocked By**: None (start immediately)

  **References**:
  - `01_Materiale/estratto_progetto.md` — Scenario completo e requisiti
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — Dati cliente
  - `01_Materiale/SOLUZIONE.docx` — Linee guida soluzione

  **Acceptance Criteria**:
  - [ ] Directory `03_Progetti/ProjectWork_Infrastruttura_IT/` creata con sottodirectory come da struttura
  - [ ] README.md presente con panoramica e struttura
  - [ ] Ogni sottodirectory ha `.gitkeep`

  **QA Scenarios**:
  ```
  Scenario: Verifica struttura directory
    Tool: Bash (Get-ChildItem)
    Steps:
      1. Get-ChildItem -Recurse -Directory "23_Project_Work_e_Laboratori/03_Progetti/ProjectWork_Infrastruttura_IT/"
    Expected Result: La struttura a matrice completa con Condivisi/, A_Full_Cloud_GCP/, B_On_Premise/, C_Ibrido/ e sottodirectory
    Evidence: .omo/evidence/task-1/directory-structure.txt
  ```

- [x] 2. Assessment AS-IS — Thema Consulting

  **What to do**:
  - Documentare lo stato attuale dell'infrastruttura IT di Thema Consulting:
    - Datacenter: 2 host VMWare + SAN NetApp 24TB, rack saturi, UPS 10', condizionamento al limite
    - Rete: Firewall Fortigate FG-60F
    - Cluster HPC: 8 nodi fisici + Infiniband + Front-end VM Linux
    - Server: Zimbra (VM Linux), MS365/LibreOffice, MS Teams, Samba4 AD (VM Linux), NextCloud (VM Linux), GiTea, Profis (Server Windows), SugarCRM (VM Linux), Kimai (VM Linux), MediaWiki (VM Linux)
    - Pondus: Web C# (IIS + MS SQL), HW Xeon Silver 4110, 64GB RAM, 1.2TB HDD
    - Personale: 30 persone, 40 postazioni, laptop aziendali
  - Usare i dati da `estratto_progetto.md` e dal file Excel
  - Scrivere in italiano tecnico
  - Stima costi operativi attuali (energia, manutenzione, licenze)

  **Must NOT do**:
  - Non includere valutazioni o giudizi (solo fatti)
  - Non includere soluzioni proposte (saranno nelle varianti)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 3)
  - **Parallel Group**: Wave 1 (with Task 3)
  - **Blocks**: Tasks 8-25 (documenti tecnici varianti)
  - **Blocked By**: Task 1

  **References**:
  - `01_Materiale/estratto_progetto.md:42-52` — Descrizione Thema Consulting (personale, sede, datacenter)
  - `01_Materiale/estratto_progetto.md:66-75` — Assessment tabella infrastruttura
  - `01_Materiale/estratto_progetto.md:80-93` — Tabella servizi/sistemi Thema
  - Excel "Analisi Cliente" — Budget, vincoli, strumenti AS-IS

  **Acceptance Criteria**:
  - [ ] File `Condivisi/01_Assessment/assessment_thema_consulting.md` creato
  - [ ] Copre: datacenter, rete, HPC, server/servizi, personale, costi
  - [ ] Dati coerenti con documento originale (30 persone, 40 postazioni, etc.)

  **QA Scenarios**:
  ```
  Scenario: Verifica completezza assessment Thema
    Tool: Bash (grep per dati chiave)
    Steps:
      1. grep "30" Condivisi/01_Assessment/assessment_thema_consulting.md
      2. grep "Fortigate\|HPC\|Pondus\|Samba4\|Zimbra" Condivisi/01_Assessment/assessment_thema_consulting.md
      3. grep -c "REQUISITI\|SOLUZIONE\|DIMENSIONAMENTO\|COSTI" Condivisi/01_Assessment/assessment_thema_consulting.md
    Expected Result: File contiene tutti gli elementi chiave dell'infrastruttura Thema
    Evidence: .omo/evidence/task-2/thema-assessment-check.txt
  ```

- [x] 3. Assessment AS-IS — Pro Studio

  **What to do**:
  - Documentare lo stato attuale di Pro Studio:
    - Nessuna infrastruttura on-premise
    - Google Workspace (posta, calendar, office, drive, meet, authenticator)
    - Bit Bucket (SaaS, versioning)
    - Odoo (SaaS: contabilità, CRM, time sheet)
    - Media Wiki (self-hosted su GCP)
    - Backup su GCP
    - Personale: 20 dipendenti
  - Usare dati da `estratto_progetto.md` e file Excel

  **Must NOT do**:
  - Stesse limitazioni di Task 2

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Task 2)
  - **Blocks**: Tasks 8-25
  - **Blocked By**: Task 1

  **References**:
  - `01_Materiale/estratto_progetto.md:55-62` — Descrizione Pro Studio
  - `01_Materiale/estratto_progetto.md:66-75` — Assessment tabella
  - `01_Materiale/estratto_progetto.md:80-93` — Tabella servizi Pro Studio

  **Acceptance Criteria**:
  - [ ] File `Condivisi/01_Assessment/assessment_prostudio.md` creato
  - [ ] Copre: servizi cloud, personale, costi, dipendenze

  **QA Scenarios**:
  ```
  Scenario: Verifica completezza assessment Pro Studio
    Tool: Bash (grep)
    Steps:
      1. grep "20\|GCP\|Workspace\|Odoo\|MediaWiki" Condivisi/01_Assessment/assessment_prostudio.md
    Expected Result: Dati core di Pro Studio presenti
    Evidence: .omo/evidence/task-3/prostudio-assessment-check.txt
  ```

- [x] 4. Gap Analysis — stato attuale vs requisiti ISO 27001

  **What to do**:
  - Confrontare lo stato AS-IS (Thema + Pro Studio) con i requisiti ISO/IEC 27001:
    - Business continuity: ridondanza sistemi, connettività
    - DR: delocalizzazione backup, fruibilità servizi clienti
    - Sicurezza accessi: cifratura, protocolli sicuri, VPN
    - MFA
  - Identificare gap organizzativi e tecnologici
  - Tabella: Requisito | Stato Attuale | Gap | Priorità (Alta/Media/Bassa)

  **Must NOT do**:
  - Non proporre soluzioni (saranno nelle varianti)
  - Non fare analisi legale

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (after Tasks 2,3)
  - **Blocks**: Tasks 8-25 (documenti sicurezza)
  - **Blocked By**: Tasks 2,3

  **References**:
  - `01_Materiale/estratto_progetto.md:103-118` — Vincoli ISO 27001
  - `SOLUZIONE.docx` — Requisiti ISO da applicare
  - Tasks 2,3 (assessment)

  **Acceptance Criteria**:
  - [ ] File `Condivisi/01_Assessment/gap_analysis.md` creato
  - [ ] Tabella gap analysis completa per ogni requisito ISO 27001

  **QA Scenarios**:
  ```
  Scenario: Verifica gap analysis
    Tool: Bash (grep)
    Steps:
      1. grep -c "Alta\|Media\|Bassa" Condivisi/01_Assessment/gap_analysis.md
    Expected Result: ≥5 gap identificati e classificati
    Evidence: .omo/evidence/task-4/gap-analysis-check.txt
  ```

- [x] 5. Project Charter

  **What to do**:
  - Creare il Project Charter per il progetto di integrazione TP Group:
    - Nome progetto: "Integrazione IT TP Group"
    - Sponsor/Cliente: TP Group srl (Andrei+ — Solution Architect)
    - Ruolo: Fornitore/Proponente
    - Business case: Fusione Thema Consulting + Pro Studio, necessità integrazione IT
    - Obiettivi: Convergenza servizi, ISO 27001, potenziamento HPC/Pondus, smart working
    - Budget: 520.000€ + IVA (+ 181.000€ extra manodopera)
    - Tempistica: 12 settimane attive (9-12 mesi totali), shutdown max 7gg
    - Team: Sistemista (€500/gg) + PM (€650/gg)
    - Stakeholder: Dirigenza TP Group, Dipendenti (50), Clienti automotive/aerospace
    - Rischi preliminari: Datacenter saturo, condizionamento limite, finestra migrazione stretta

  **Must NOT do**:
  - Non includere dettagli implementativi

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 6,7)
  - **Blocks**: Tasks 26-32 (PM finali)
  - **Blocked By**: Task 1

  **References**:
  - `01_Materiale/estratto_progetto.md` — Scenario completo
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — Budget, tempistiche, vincoli
  - `01_Materiale/SOLUZIONE.docx` — Budget dettagliato, tempistica 12 settimane

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/project_charter.md` creato
  - [ ] Copre: obiettivi, budget, tempistica, stakeholder, rischi preliminari

  **QA Scenarios**:
  ```
  Scenario: Verifica Project Charter
    Tool: Bash (grep)
    Steps:
      1. grep -i "budget\|520\|obiettivi\|tempistica\|stakeholder\|rischi" Condivisi/02_Project_Management/project_charter.md
    Expected Result: Tutte le sezioni core presenti
    Evidence: .omo/evidence/task-5/charter-check.txt
  ```

- [x] 6. WBS (Work Breakdown Structure)

  **What to do**:
  - Creare WBS a 3+ livelli per il progetto:
    - Livello 1: Fasi (Assessment, Progettazione, Approvvigionamento, Implementazione, Test, Migrazione, Chiusura)
    - Livello 2: Attività principali
    - Livello 3: Sotto-attività
  - Stimare effort (giorni uomo) per ogni attività
  - Assegnare responsabilità di massima

  **Must NOT do**:
  - Non includere dettagli operativi (runbook)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5,7)
  - **Blocks**: Tasks 30-32
  - **Blocked By**: Task 1

  **References**:
  - Task 5 (Project Charter) — Obiettivi e vincoli
  - `01_Materiale/estratto_progetto.md:152-178` — Requisiti offerta (attività richieste)

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/wbs.md` creato
  - [ ] Minimo 3 livelli di profondità
  - [ ] Stima effort per ogni attività

  **QA Scenarios**:
  ```
  Scenario: Verifica WBS
    Tool: Bash
    Steps:
      1. wc -l Condivisi/02_Project_Management/wbs.md
      2. grep -c "Livello\|1\.\|2\.\|3\." Condivisi/02_Project_Management/wbs.md
    Expected Result: WBS con ≥3 livelli e minimo 15 voci
    Evidence: .omo/evidence/task-6/wbs-check.txt
  ```

- [x] 7. Gantt di Progetto

  **What to do**:
  - Creare diagramma Gantt testuale (Mermaid) per il progetto:
    - Durata: 12 settimane attive
    - Milestone: Fine Assessment (Settimana 2), Fine Progettazione (Settimana 5), Ordine HW (Settimana 3), Inizio Implementazione (Settimana 6), Migrazione (Settimana 10-11), Go-Live (Settimana 12)
    - Shutdown massimo: 7 giorni consecutivi (Settimana 11)
    - Dipendenze tra attività (da WBS)
    - Risorse: Sistemista + PM
    - Gantt in formato Mermaid (```mermaid gantt ... ```) e tabella di sintesi

  **Must NOT do**:
  - Non usare software esterni (solo Mermaid markdown)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 5,6)
  - **Blocks**: Tasks 30-32
  - **Blocked By**: Task 1

  **References**:
  - Task 6 (WBS) — Attività e stime
  - `01_Materiale/SOLUZIONE.docx` — Tempistica: "12 settimane", "shutdown 7 giorni"
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — "Tempistica implementazione: 9/12 mesi"

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/gantt.md` creato
  - [ ] Gantt in formato Mermaid
  - [ ] Milestone "Migrazione completata" entro 12 settimane
  - [ ] Shutdown massimo 7 giorni

  **QA Scenarios**:
  ```
  Scenario: Verifica Gantt
    Tool: Bash (grep e verifica Mermaid)
    Steps:
      1. grep "mermaid\|gantt" Condivisi/02_Project_Management/gantt.md
      2. grep -c "milestone\|milestone" Condivisi/02_Project_Management/gantt.md
      3. grep "12\|settimana\|week" Condivisi/02_Project_Management/gantt.md
    Expected Result: Gantt presente con sintassi Mermaid valida e milestone
    Evidence: .omo/evidence/task-7/gantt-check.txt
  ```

- [x] 8. [A] Progettazione Rete/VPN — Full Cloud GCP

  **What to do**:
  - Progettare la rete per la variante Full Cloud GCP:
    - Architettura: tutto su Google Cloud (VPC nativo)
    - Connettività sede Thema: Cloud VPN (LAN-to-LAN) tunnel tra Fortigate FG-60F e GCP
    - Smart working: Client-to-LAN via Cloud VPN (10+ utenti remoti/giorno)
    - Hybrid Cloud: non applicabile (tutto su cloud)
    - Topologia: VPC con subnet per servizi (HPC, Pondus, backup, management)
    - Schema IP/subnetting
    - Firewall rules (Cloud Armor + firewall rules GCP)
    - Dimensionamento banda: 50 utenti, HPC traffico dati, Pondus pubblico
    - Costi: Cloud VPN, Cloud NAT, Cloud Armor
  - Formato: REQUISITI → SOLUZIONE → DIMENSIONAMENTO → COSTI

  **Must NOT do**:
  - Non includere comandi di configurazione specifici

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 9-13)
  - **Blocks**: Task 26 (Offerta A)
  - **Blocked By**: Tasks 1,2,3,4

  **References**:
  - `01_Materiale/estratto_progetto.md:115-118` — Requisiti VPN
  - `01_Materiale/SOLUZIONE.docx` — VPN via GCP
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — Smart working 10+/gg, laptop + VPN

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/03_Rete_VPN/progetto_rete_vpn.md` creato
  - [ ] Include: topologia, subnet, VPN, cloud firewall, costi
  - [ ] Segue format REQUISITI → SOLUZIONE → DIMENSIONAMENTO → COSTI

  **QA Scenarios**:
  ```
  Scenario: Verifica documento rete Full Cloud
    Tool: Bash (grep)
    Steps:
      1. grep -i "Cloud VPN\|VPC\|subnet\|firewall\|COSTI" A_Full_Cloud_GCP/03_Rete_VPN/progetto_rete_vpn.md
    Expected Result: Tutti gli elementi chiave di progettazione rete presenti
    Evidence: .omo/evidence/task-8/variant-a-rete-check.txt
  ```

- [x] 9. [A] Specifica Cluster HPC — Full Cloud GCP

  **What to do**:
  - Progettare il cluster HPC su GCP per la variante Full Cloud:
    - Istanze HPC su GCP (es. C2/H3 high-mem instances)
    - 8 nodi attuali on-prem → da considerare fine vita / migrazione a cloud?
    - 8 nuovi nodi su cloud: 2 CPU, ≥24 core, 8GB RAM/core, NO GPU, Linux
    - Rete: Ethernet (VPC) + valutazione se Infiniband è disponibile su GCP (GCP non offre Infiniband nativo — alternativa: cluster su GCP con reti ad alta velocità)
    - Scratch: ≥1,6 TB per nodo (dischi persistenti o local SSD)
    - Front-end: VM Linux
    - Nessuna virtualizzazione/container per nodi calcolo
    - Stima costi: istanze HPC on-demand vs committed use discounts (3 anni)
    - Considerazioni: performance simulazioni crash test, latenza rete
  - Nota: GCP non offre Infiniband nativo — documentare come requisito da valutare con cliente

  **Must NOT do**:
  - Non includere comandi gcloud

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: none needed

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 8,10-13)

  **References**:
  - `01_Materiale/estratto_progetto.md:126-133` — Requisiti HPC
  - `01_Materiale/SOLUZIONE.docx` — Specifiche HPC (ricerca componenti)

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/04_Cluster_HPC/specifica_cluster_hpc.md` creato
  - [ ] Include: tipologia istanze, dimensionamento, storage, costi
  - [ ] Nota su Infiniband su GCP documentata

  **QA Scenarios**:
  ```
  Scenario: Verifica specifica HPC cloud
    Tool: Bash (grep)
    Steps:
      1. grep -i "istanza\|core\|RAM\|scratch\|costo\|CPU" A_Full_Cloud_GCP/04_Cluster_HPC/specifica_cluster_hpc.md
    Expected Result: Specifiche tecniche complete
    Evidence: .omo/evidence/task-9/variant-a-hpc-check.txt
  ```

- [x] 10. [A] Architettura Pondus & Migrazione — Full Cloud GCP

  **What to do**:
  - Progettare la migrazione di Pondus su cloud:
    - Stato attuale: C# Web App su IIS + MS SQL, HW Xeon Silver 4110/64GB/1.2TB
    - Target: Containerizzato su Google Cloud Run o GKE
    - DB: MS SQL → Cloud SQL (SQL Server) o AlloyDB
    - Refactoring: da IIS a container Linux/Windows, C# compatibile
    - Pubblicazione online: esposizione pubblica con dominio + HTTPS (Cloud LB)
    - Abbonamento: sito web e-commerce per abbonamenti mensili
    - Stima costi: Cloud Run/GKE + Cloud SQL + Cloud LB + networking
    - Upgrade funzionale: scalabilità orizzontale, multi-tenancy

  **Must NOT do**:
  - Non scrivere codice C# o Dockerfile
  - Non includere dettagli implementativi di refactoring

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 8,9,11-13)

  **References**:
  - `01_Materiale/estratto_progetto.md:52` — Pondus come servizio
  - `01_Materiale/estratto_progetto.md:92` — Specifiche HW Pondus
  - `01_Materiale/estratto_progetto.md:126-127` — Obiettivo potenziamento Pondus
  - `01_Materiale/SOLUZIONE.docx` — "Containerizzare e scalare orizzontalmente", "pubblicazione online"

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/05_Pondus_App/architettura_pondus.md` creato
  - [ ] Include: stato attuale, target cloud, migrazione DB, pubblicazione online, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica architettura Pondus
    Tool: Bash (grep)
    Steps:
      1. grep -i "container\|Cloud Run\|GKE\|SQL\|migrazione\|abbonamento" A_Full_Cloud_GCP/05_Pondus_App/architettura_pondus.md
    Expected Result: Strategia cloud per Pondus completa
    Evidence: .omo/evidence/task-10/variant-a-pondus-check.txt
  ```

- [x] 11. [A] Piano Cloud Migration — Full Cloud GCP

  **What to do**:
  - Pianificare la migrazione completa su GCP:
    - Servizi da migrare: Posta (Zimbra → MS365/Workspace), AD (Samba4 → Google Cloud Directory Sync o MS365 AD), File (NextCloud → Drive/Cloud Storage), Sviluppo (GiTea → BitBucket), Contabilità (Profis → Odoo), CRM (SugarCRM → Odoo), TimeSheet (Kimai → Odoo), Documentazione (MediaWiki)
    - Strategia: Big Bang o Graduale? Consigliata: graduale per servizi non critici, finestra unica per migrazione cut-off
    - Ordine migrazione: Servizi collaborativi → Dati → Applicazioni critiche (Pondus)
    - Integrazione identità: Samba4 AD ↔ GCP / MS365 (federation)
    - Dismissione servizi Thema non più necessari
    - Stima tempi: 12 settimane totali, 7gg shutdown per cut-over
    - Rischi: Coesistenza durante migrazione, volume dati, downtime

  **Must NOT do**:
  - Non includere configurazioni tecniche specifiche

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 8-10,12,13)

  **References**:
  - `01_Materiale/estratto_progetto.md:80-93` — Tabella servizi
  - `01_Materiale/SOLUZIONE.docx` — "Trasferire tutto su Google Cloud", "servizi self-hosted più difficili"
  - Task 2,3 (assessment AS-IS)

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/06_Cloud_Migration/piano_migrazione_cloud.md` creato
  - [ ] Include: mappatura servizi, ordine migrazione, integrazione identità, costi, rischi

  **QA Scenarios**:
  ```
  Scenario: Verifica piano migrazione cloud
    Tool: Bash (grep)
    Steps:
      1. grep -i "migrazione\|Zimbra\|Samba4\|NextCloud\|GiTea\|Odoo\|tempistica\|rischi" A_Full_Cloud_GCP/06_Cloud_Migration/piano_migrazione_cloud.md
    Expected Result: Copertura completa servizi e piano
    Evidence: .omo/evidence/task-11/variant-a-migration-check.txt
  ```

- [x] 12. [A] Architettura Backup/DR — Full Cloud GCP

  **What to do**:
  - Progettare backup e DR su GCP:
    - Strategia nativa cloud: backup automatici GCP
    - 3-2-1 rule: 3 copie, 2 media, 1 off-site (multi-regione GCP)
    - RPO/RTO target: da definire con SLA cliente (suggerito: RPO 4h, RTO 8h per servizi critici)
    - Copertura: VM, database (Cloud SQL), file storage (Cloud Storage), Pondus
    - DR: GCP multi-regione (europe-west1 + europe-west4) per failover automatico
    - Procedure di restore
    - Costi: Cloud Storage (Nearline/Coldline), Cloud SQL backup

  **Must NOT do**:
  - Non includere comandi gcloud

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 8-11,13)

  **References**:
  - `01_Materiale/estratto_progetto.md:109-111` — Requisiti DR (delocalizzazione, fruibilità)
  - `01_Materiale/SOLUZIONE.docx` — "Delocalizzazione dati (funzionalità cloud provider)"

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/07_Backup_DR/architettura_backup_dr.md` creato
  - [ ] Include: strategia, RPO/RTO, copertura, costi, procedure restore

  **QA Scenarios**:
  ```
  Scenario: Verifica backup/DR cloud
    Tool: Bash (grep)
    Steps:
      1. grep -i "RPO\|RTO\|backup\|DR\|restore\|multi-regione\|costo" A_Full_Cloud_GCP/07_Backup_DR/architettura_backup_dr.md
    Expected Result: Strategia DR completa su GCP
    Evidence: .omo/evidence/task-12/variant-a-backup-check.txt
  ```

- [x] 13. [A] Requisiti Sicurezza ISO 27001 — Full Cloud GCP

  **What to do**:
  - Documentare la conformità ISO 27001 per variante Full Cloud:
    - Business continuity: ridondanza GCP multi-regione, Cloud Load Balancing, managed services
    - DR: backup automatici, multi-regione failover
    - Sicurezza accessi: Cloud IAM, cifratura dati at rest/in transit (GCP default), Cloud VPN, MFA (Google Authenticator)
    - Protocolli sicuri: HTTPS, TLS 1.3, SSH
    - Accesso remoto: Cloud VPN (LAN-to-LAN, Client-to-LAN)
    - Policy di sicurezza: bozza (principi, ruoli, responsabilità)
    - NOTE: La certificazione ISO 27001 formale richiede audit esterno — questo documento copre l'adeguamento tecnico

  **Must NOT do**:
  - Non includere procedure organizzative complete (solo bozza policy)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 8-12)

  **References**:
  - `01_Materiale/estratto_progetto.md:103-118` — Vincoli ISO 27001
  - `01_Materiale/SOLUZIONE.docx` — Requisiti ISO specifici
  - Task 4 (Gap Analysis)

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md` creato
  - [ ] Copre: business continuity, DR, sicurezza accessi, protocolli, MFA, VPN
  - [ ] Include bozza policy

  **QA Scenarios**:
  ```
  Scenario: Verifica requisiti sicurezza ISO
    Tool: Bash (grep)
    Steps:
      1. grep -i "ISO 27001\|business continuity\|DR\|cifratura\|MFA\|VPN\|policy" A_Full_Cloud_GCP/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md
    Expected Result: Tutti i requisiti ISO 27001 coperti
    Evidence: .omo/evidence/task-13/variant-a-security-check.txt
  ```

- [x] 14. [B] Progettazione Rete/VPN — On-Premise

  **What to do**:
  - Progettare la rete per la variante On-Premise:
    - Upgrade firewall Fortigate FG-60F (valutare modello superiore per 50 utenti + VPN)
    - VPN LAN-to-LAN: Fortigate ↔ sede secondaria/co-location
    - VPN Client-to-LAN: FortiClient VPN per smart working (10+ utenti)
    - Rete interna: switches, cablaggio (edificio storico — valutare WiFi 6 per flessibilità postazioni)
    - Schema IP/subnetting: VLAN separazione servizi (HPC, Pondus, server, management, ospiti)
    - Ridondanza connettività: link principale + backup (4G/5G o secondo provider)
    - Upgrade infrastruttura di rete: PoE per AP WiFi, switch aggregazione
    - Costi: Fortigate upgrade, switch, AP, cablaggio, licenze
  - Nota: datacenter saturo — valutare armadio rack aggiuntivo o micro-datacenter

  **Must NOT do**:
  - Non includere configurazioni CLI Fortigate

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 15-19)

  **References**:
  - `01_Materiale/estratto_progetto.md:71` — Firewall Fortigate FG-60F
  - `01_Materiale/estratto_progetto.md:115-118` — Requisiti VPN
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — Datacenter saturo, co-location €250k

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/03_Rete_VPN/progetto_rete_vpn.md` creato
  - [ ] Include: upgrade Fortigate, VPN, VLAN, WiFi, ridondanza, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica rete On-Premise
    Tool: Bash (grep)
    Steps:
      1. grep -i "Fortigate\|VPN\|VLAN\|WiFi\|ridondanza\|costo\|upgrade" B_On_Premise/03_Rete_VPN/progetto_rete_vpn.md
    Expected Result: Architettura di rete on-prem completa
    Evidence: .omo/evidence/task-14/variant-b-rete-check.txt
  ```

- [x] 15. [B] Specifica Cluster HPC — On-Premise

  **What to do**:
  - Progettare il potenziamento HPC on-premise:
    - 8 nodi esistenti + 8 nuovi nodi on-prem
    - Specifica nuovi nodi: 2 CPU ≥24 core, 8GB RAM/core, NO GPU, Linux
    - Rete: Ethernet + Infiniband 100/200 Gbps
    - Scratch: 1,6 TB per nodo (SSD NVMe)
    - Front-end VM Linux (esistente + upgrade se necessario)
    - Raffreddamento: valutare soluzione per +8 nodi (condizionamento già al limite → serving costoso)
    - Spazio rack: saturo → necessaria espansione (co-location o armadio aggiuntivo)
    - Budget stimato: ~€200-250k per 8 nodi + Infiniband + storage
    - Consumo elettrico: stimare kW aggiuntivi

  **Must NOT do**:
  - Non specificare marche precise (solo tipologia)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 14,16-19)

  **References**:
  - `01_Materiale/estratto_progetto.md:126-133` — Requisiti HPC
  - `01_Materiale/SOLUZIONE.docx` — Specifiche HPC, ricerca componenti

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/04_Cluster_HPC/specifica_cluster_hpc.md` creato
  - [ ] Include: specifica nodi, rete, storage, raffreddamento, spazio, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica HPC On-Premise
    Tool: Bash (grep)
    Steps:
      1. grep -i "core\|RAM\|Infiniband\|scratch\|Linux\|raffreddamento\|costo\|rack" B_On_Premise/04_Cluster_HPC/specifica_cluster_hpc.md
    Expected Result: Specifica HPC completa e dimensionata
    Evidence: .omo/evidence/task-15/variant-b-hpc-check.txt
  ```

- [x] 16. [B] Architettura Pondus — On-Premise

  **What to do**:
  - Progettare il potenziamento di Pondus on-premise:
    - Upgrade HW: nuovo server (o upgrade Xeon Silver 4110)
    - Containerizzazione: Docker Swarm o Kubernetes on-prem (Perché on-prem)
    - DB: MS SQL on-prem (upgrade licenza o passaggio a SQL Server Standard)
    - Esposizione pubblica: pubblicazione online con sito web e-commerce
    - Scalabilità orizzontale: load balancing con più istanze
    - Backup: integrazione con NAS QNAP esistente
    - Costi: HW server, licenze MS, container platform

  **Must NOT do**:
  - Non includere dettagli implementativi

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 14,15,17-19)

  **References**:
  - `01_Materiale/estratto_progetto.md:52,92,126-127` — Descrizione Pondus
  - `01_Materiale/SOLUZIONE.docx` — "Containerizzare"

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/05_Pondus_App/architettura_pondus.md` creato
  - [ ] Include: upgrade HW/SW, containerizzazione, esposizione, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica Pondus On-Premise
    Tool: Bash (grep)
    Steps:
      1. grep -i "upgrade\|server\|container\|MS SQL\|pubblicazione\|costo" B_On_Premise/05_Pondus_App/architettura_pondus.md
    Expected Result: Architettura Pondus on-prem completa
    Evidence: .omo/evidence/task-16/variant-b-pondus-check.txt
  ```

- [x] 17. [B] Piano Upgrade Infrastruttura — On-Premise

  **What to do**:
  - Pianificare l'upgrade dell'infrastruttura on-premise:
    - Co-location: valutare spazio in datacenter esterno per espansione (budget ~€250k dal Excel)
    - Oppure: micro-datacenter in sede (armadio rack aggiuntivo + condizionamento dedicato)
    - Upgrade condizionamento esistente (se possibile)
    - UPS: upgrade per nuovi carichi HPC
    - Gruppo di continuità per nuovi armadi
    - Tempistica: acquisto HW (8-16 settimane lead time), installazione (2-4 settimane), test (1-2 settimane)

  **Must NOT do**:
  - Non includere dettagli impiantistici (elettricità, HVAC engineering)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 14-16,18,19)

  **References**:
  - `01_Materiale/estratto_progetto.md:47,73-75` — Limiti datacenter
  - Excel — Opzioni co-location €250k / cloud €220k

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/06_Cloud_Migration/piano_upgrade_infrastruttura.md` creato

  **QA Scenarios**:
  ```
  Scenario: Verifica upgrade infrastruttura
    Tool: Bash (grep)
    Steps:
      1. grep -i "co-location\|rack\|condizionamento\|UPS\|tempistica\|costo" B_On_Premise/06_Cloud_Migration/piano_upgrade_infrastruttura.md
    Expected Result: Piano upgrade completo
    Evidence: .omo/evidence/task-17/variant-b-upgrade-check.txt
  ```

- [x] 18. [B] Architettura Backup/DR — On-Premise

  **What to do**:
  - Progettare backup e DR on-premise:
    - Backup locale: NAS QNAP 32TB esistente + espansione
    - 3-2-1 rule: copia locale (NAS) + copia off-site (sede secondaria o cloud)
    - DR: sito secondario (co-location) per failover servizi critici (Pondus, AD)
    - RPO/RTO: RPO 4h, RTO 24h per servizi critici (tempi più lunghi senza cloud)
    - Backup HPC: dati progetto su NAS + tape library?
    - Procedure di restore
    - Costi: NAS espansione, nastro, connectivity sito secondario

  **Must NOT do**:
  - Non specificare marche

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 14-17,19)

  **References**:
  - `01_Materiale/estratto_progetto.md:69` — NAS QNAP 32TB
  - `01_Materiale/estratto_progetto.md:109-111` — Requisiti DR

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/07_Backup_DR/architettura_backup_dr.md` creato

  **QA Scenarios**:
  ```
  Scenario: Verifica backup/DR On-Premise
    Tool: Bash (grep)
    Steps:
      1. grep -i "NAS\|RPO\|RTO\|sito secondario\|off-site\|restore\|costo" B_On_Premise/07_Backup_DR/architettura_backup_dr.md
    Expected Result: Strategia DR on-prem completa
    Evidence: .omo/evidence/task-18/variant-b-backup-check.txt
  ```

- [x] 19. [B] Requisiti Sicurezza ISO 27001 — On-Premise

  **What to do**:
  - Documentare conformità ISO 27001 per variante On-Premise:
    - Business continuity: ridondanza HW (server gemelli), NAS RAID, gruppo continuità, link backup
    - DR: backup su nastro + sito secondario, procedure documentate
    - Sicurezza accessi: cifratura dischi (BitLocker/LUKS), protocolli (HTTPS, TLS, SSH), VPN (FortiClient + FortiGate), MFA
    - Accesso remoto: VPN Client-to-LAN + eventuale VDI (solo per manutenzione)
    - Policy di sicurezza: bozza
    - Considerazioni: nessun DR nativo cloud — serve investimento in sito secondario

  **Must NOT do**:
  - Non includere procedure HR o organizzative

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 14-18)

  **References**:
  - `01_Materiale/estratto_progetto.md:103-118` — Vincoli ISO 27001
  - Task 4 (Gap Analysis)

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md` creato

  **QA Scenarios**:
  ```
  Scenario: Verifica sicurezza On-Premise
    Tool: Bash (grep)
    Steps:
      1. grep -i "ISO 27001\|cifratura\|VPN\|MFA\|business continuity\|policy" B_On_Premise/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md
    Expected Result: Tutti i requisiti ISO coperti
    Evidence: .omo/evidence/task-19/variant-b-security-check.txt
  ```

- [x] 20. [C] Progettazione Rete/VPN — Ibrido

  **What to do**:
  - Progettare la rete ibrida (on-prem + GCP):
    - On-prem: Fortigate FG-60F (upgrade) per connettività sede + VPN
    - Cloud: Cloud VPN su GCP per hybrid connectivity
    - VPN LAN-to-LAN: Fortigate ↔ GCP (tunnel IPsec)
    - VPN Client-to-LAN: FortiClient o Cloud VPN per 10+ utenti remoti
    - Hybrid Cloud: connettività dedicata (Partner Interconnect o Cloud VPN) tra sede Thema e GCP
    - VLAN: separazione traffico on-prem (HPC, server, management) e cloud (servizi migrati)
    - Schema IP/subnetting: on-prem + GCP VPC con peering
    - Ridondanza: link principale + backup (secondo ISP o 4G/5G)
    - Costi: Fortigate upgrade, Cloud VPN, interconnect, switches

  **Must NOT do**:
  - Non includere configurazioni CLI

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 21-25)

  **References**:
  - `01_Materiale/estratto_progetto.md:115-118` — VPN requisiti
  - Task 8 (rete Full Cloud) + Task 14 (rete On-Prem) — Pattern da ibridare

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/03_Rete_VPN/progetto_rete_vpn.md` creato
  - [ ] Include: connettività on-prem + cloud, VPN, hybrid, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica rete ibrida
    Tool: Bash (grep)
    Steps:
      1. grep -i "Fortigate\|Cloud VPN\|IPsec\|VLAN\|hybrid\|interconnect\|costo" C_Ibrido/03_Rete_VPN/progetto_rete_vpn.md
    Expected Result: Architettura di rete ibrida completa
    Evidence: .omo/evidence/task-20/variant-c-rete-check.txt
  ```

- [x] 21. [C] Specifica Cluster HPC — Ibrido

  **What to do**:
  - Progettare HPC ibrido (on-prem + cloud):
    - 8 nodi esistenti: restano on-prem (investimento già ammortizzato)
    - 8 nuovi nodi: su GCP (istanze HPC C2/H3) o su co-location
    - Rete: nodi on-prem con Infiniband locale, nodi cloud con Ethernet GCP
    - Collegamento: Hybrid Cloud per job HPC distribuiti (valutare latenza)
    - Front-end: VM Linux unificata (on-prem + cloud)
    - Scratch: 1,6 TB per nodo (on-prem SSD, cloud persistent disk)
    - Nessuna virtualizzazione/container per nodi calcolo
    - Vantaggio: flessibilità (picchi di calcolo su cloud, carico base on-prem)
    - Costi: nodi on-prem (solo esercizio) + istanze cloud

  **Must NOT do**:
  - Non specificare marche

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 20,22-25)

  **References**:
  - `01_Materiale/estratto_progetto.md:126-133` — Requisiti HPC
  - Task 9 (HPC Full Cloud) + Task 15 (HPC On-Prem)

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/04_Cluster_HPC/specifica_cluster_hpc.md` creato
  - [ ] Include: nodi on-prem + cloud, rete, storage, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica HPC ibrido
    Tool: Bash (grep)
    Steps:
      1. grep -i "on-prem\|cloud\|Infiniband\|ibrido\|core\|RAM\|scratch\|costo" C_Ibrido/04_Cluster_HPC/specifica_cluster_hpc.md
    Expected Result: Specifica HPC ibrida completa
    Evidence: .omo/evidence/task-21/variant-c-hpc-check.txt
  ```

- [x] 22. [C] Architettura Pondus & Migrazione — Ibrido

  **What to do**:
  - Progettare Pondus in architettura ibrida:
    - Opzione 1: Containerizzato on-prem (Docker Swarm/K8s), DB MS SQL on-prem, esposizione via reverse proxy
    - Opzione 2: Containerizzato su GCP (Cloud Run), DB su Cloud SQL, ma retaining altri servizi on-prem
    - Consigliata: Opzione 2 (Pondus su cloud per scalabilità pubblica, resto on-prem)
    - Pubblicazione online: Cloud LB + dominio + abbonamenti
    - Integrazione: Pondus su GCP ←→ dati HPC on-prem (API)
    - Costi: Cloud Run + Cloud SQL + networking + licenze

  **Must NOT do**:
  - Non scrivere codice

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 20,21,23-25)

  **References**:
  - Task 10 + Task 16 — Pattern Pondus
  - `01_Materiale/SOLUZIONE.docx` — Containerizzazione e pubblicazione

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/05_Pondus_App/architettura_pondus.md` creato

  **QA Scenarios**:
  ```
  Scenario: Verifica Pondus ibrido
    Tool: Bash (grep)
    Steps:
      1. grep -i "container\|cloud\|on-prem\|ibrido\|pubblicazione\|abbonamento\|costo" C_Ibrido/05_Pondus_App/architettura_pondus.md
    Expected Result: Architettura Pondus ibrida completa
    Evidence: .omo/evidence/task-22/variant-c-pondus-check.txt
  ```

- [x] 23. [C] Strategia Cloud Ibrida

  **What to do**:
  - Documentare la strategia di integrazione ibrida:
    - Cosa resta on-prem: HPC (nodi esistenti), Pondus? (dipende da scelta), connettività sede
    - Cosa va su cloud: servizi collaborativi (MS365, Odoo), DR/backup, carichi HPC aggiuntivi, Pondus (se Opzione 2)
    - Integrazione identità: Samba4 AD ↔ MS365 / GCP (federation)
    - Migrazione graduale: prima servizi non critici → poi servizi cloud-native → poi valutazione HPC cloud
    - Coesistenza: gli utenti devono poter accedere a servizi on-prem e cloud durante migrazione
    - Tempistica: 12 settimane per migrazione servizi collaborativi, HPC cloud scalabile indipendentemente
    - Costi: GCP (servizi cloud) + on-prem (esercizio)

  **Must NOT do**:
  - Non creare duplicazione con altri task

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 20-22,24,25)

  **References**:
  - Task 11 + Task 17 — Pattern migrazione
  - `01_Materiale/SOLUZIONE.docx` — "Inizialmente ibrido"

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/06_Cloud_Migration/strategia_cloud_ibrida.md` creato
  - [ ] Include: cosa on-prem vs cloud, identità, tempistica, costi

  **QA Scenarios**:
  ```
  Scenario: Verifica strategia ibrida
    Tool: Bash (grep)
    Steps:
      1. grep -i "on-prem\|cloud\|ibrido\|identità\|migrazione\|tempistica\|costo" C_Ibrido/06_Cloud_Migration/strategia_cloud_ibrida.md
    Expected Result: Strategia ibrida completa
    Evidence: .omo/evidence/task-23/variant-c-strategy-check.txt
  ```

- [x] 24. [C] Architettura Backup/DR — Ibrido

  **What to do**:
  - Progettare backup e DR ibrido:
    - On-prem: NAS QNAP 32TB per backup locale (HPC, server, servizi critici on-prem)
    - Cloud: GCP Cloud Storage come destinazione off-site (delocalizzazione ISO 27001)
    - 3-2-1 rule: 1 primario (NAS), 1 secondario (GCP), 1 off-site (GCP multi-regione)
    - RPO/RTO: RPO 1h (cloud) / 4h (on-prem), RTO 4h (cloud) / 24h (on-prem)
    - DR: failover servizi cloud su GCP, servizi on-prem con procedure manuali
    - Vantaggio: delocalizzazione nativa via GCP senza investire in sito secondario fisico
    - Costi: NAS (già esistente) + Cloud Storage (Nearline ~€0.01/GB)

  **Must NOT do**:
  - Non includere comandi gsutil

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 20-23,25)

  **References**:
  - Task 12 + Task 18 — Pattern backup
  - `01_Materiale/estratto_progetto.md:69` — NAS QNAP 32TB

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/07_Backup_DR/architettura_backup_dr.md` creato

  **QA Scenarios**:
  ```
  Scenario: Verifica backup/DR ibrido
    Tool: Bash (grep)
    Steps:
      1. grep -i "backup\|RPO\|RTO\|off-site\|GCP\|Cloud Storage\|DR\|costo" C_Ibrido/07_Backup_DR/architettura_backup_dr.md
    Expected Result: Strategia DR ibrida completa
    Evidence: .omo/evidence/task-24/variant-c-backup-check.txt
  ```

- [x] 25. [C] Requisiti Sicurezza ISO 27001 — Ibrido

  **What to do**:
  - Documentare conformità ISO 27001 per variante Ibrida:
    - Business continuity: on-prem (ridondanza HW, NAS, UPS) + cloud (GCP multi-regione)
    - DR: backup on-prem (NAS) + cloud (GCP Storage) — doppia copia off-site
    - Sicurezza accessi: cifratura (on-prem LUKS/BitLocker + GCP default encryption), protocolli sicuri, VPN (Fortigate + Cloud VPN), MFA
    - Hybrid access: SSO tra Samba4 AD e GCP/MS365
    - Policy di sicurezza: bozza
    - Vantaggio: il cloud fornisce DR nativo e delocalizzazione senza ulteriori investimenti

  **Must NOT do**:
  - Non includere procedure HR

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 20-24)

  **References**:
  - Task 13 + Task 19 — Pattern sicurezza
  - Task 4 (Gap Analysis)

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md` creato

  **QA Scenarios**:
  ```
  Scenario: Verifica sicurezza ibrida
    Tool: Bash (grep)
    Steps:
      1. grep -i "ISO 27001\|business continuity\|DR\|cifratura\|MFA\|VPN\|SSO\|policy" C_Ibrido/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md
    Expected Result: Tutti i requisiti ISO coperti
    Evidence: .omo/evidence/task-25/variant-c-security-check.txt
  ```

- [x] 26. [A] Offerta Tecnico/Economica — Full Cloud GCP

  **What to do**:
  - Redigere il documento di offerta per la variante Full Cloud GCP, seguendo le 10 sezioni del capitolato:
    1. **Pagina introduttiva**: Nome progetto, data, versione, riferimento cliente (TP Group)
    2. **Indice**: Struttura completa del documento
    3. **Presentazione azienda proponente**: Chi siamo, servizi, storicità, team proposto
    4. **Introduzione**: Cosa prevede l'offerta (soluzione Full Cloud GCP)
    5. **Assunzioni**: Accesso remoto ai sistemi, connettività, cooperazione cliente
    6. **Descrizione fornitura HW**: Attrezzatura necessaria (minima — tutto su cloud)
    7. **Attività richieste**: Installazione, configurazione, test funzionali, migrazione, esclusioni
    8. **Documentazione**: Documenti che verranno prodotti
    9. **Termini e condizioni**: Supporto 3 anni, SLA, garanzie
    10. **Quotazione economica**: Tabella costi dettagliata per macro-voce
  - Budget target: €525.000 + IVA (budget cloud)
  - Extra manodopera: €181.000 (sistemista + PM per 3 anni)
  - Includere note e esclusioni esplicite
  - Riferimenti a documenti tecnici della variante (task 8-13)

  **Must NOT do**:
  - Non lasciare placeholder "[DA DEFINIRE]"
  - Non includere voci di costo senza giustificazione

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 27,28)
  - **Blocks**: Task 29 (Matrice di Confronto)
  - **Blocked By**: Tasks 8-13, Task 5

  **References**:
  - `01_Materiale/estratto_progetto.md:152-178` — Requisiti compilazione offerta
  - `01_Materiale/estratto_progetto.md:137-148` — Budget e costi risorse
  - Tasks 8-13 (documenti tecnici Variante A)
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — Budget, extra-budget

  **Acceptance Criteria**:
  - [ ] File `A_Full_Cloud_GCP/09_Offerta/offerta_tecnico_economica.md` creato
  - [ ] Segue struttura 10-sezioni del capitolato
  - [ ] Quotazione economica con somma verificabile (≤ €525k + €181k o scostamento motivato)
  - [ ] Include esclusioni esplicite

  **QA Scenarios**:
  ```
  Scenario: Verifica offerta Variante A
    Tool: Bash (grep + lettura)
    Steps:
      1. grep -c "^#\|^##\|^###" A_Full_Cloud_GCP/09_Offerta/offerta_tecnico_economica.md
      2. grep -i "quotazione\|€\|budget\|totale\|esclusioni" A_Full_Cloud_GCP/09_Offerta/offerta_tecnico_economica.md
    Expected Result: Offerta completa con tutte le sezioni e quotazione
    Evidence: .omo/evidence/task-26/offer-a-check.txt
  ```

- [x] 27. [B] Offerta Tecnico/Economica — On-Premise

  **What to do**:
  - Stessa struttura della Task 26, ma per variante On-Premise
  - Budget target: €580.000 + IVA (budget on-prem)
  - Include costi HW (server HPC, Fortigate, switch, NAS, cablaggio)
  - Include costi co-location (~€250k dal Excel) se necessaria
  - Extra manodopera: €181.000
  - Riferimenti a documenti tecnici Variante B (task 14-19)

  **Must NOT do**:
  - Stesse limitazioni task 26

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 26,28)

  **References**:
  - Task 14-19 (Variante B), Task 26 (struttura offerta)
  - `01_Materiale/estratto_progetto.md:152-178` — Sezioni offerta

  **Acceptance Criteria**:
  - [ ] File `B_On_Premise/09_Offerta/offerta_tecnico_economica.md` creato
  - [ ] Struttura 10 sezioni, quotazione verificabile ≤ €580k

  **QA Scenarios**:
  ```
  Scenario: Verifica offerta Variante B
    Tool: Bash (grep)
    Steps:
      1. grep -c "^#\|^##\|^###" B_On_Premise/09_Offerta/offerta_tecnico_economica.md
      2. grep -i "quotazione\|€\|budget\|co-location\|esclusioni" B_On_Premise/09_Offerta/offerta_tecnico_economica.md
    Expected Result: Offerta completa con costi on-prem
    Evidence: .omo/evidence/task-27/offer-b-check.txt
  ```

- [x] 28. [C] Offerta Tecnico/Economica — Ibrido

  **What to do**:
  - Stessa struttura della Task 26, ma per variante Ibrida
  - Budget target: €525.000-580.000 + IVA (dipende dal mix)
  - Include costi on-prem selezionati + costi cloud (GCP)
  - Extra manodopera: €181.000
  - Riferimenti a documenti tecnici Variante C (task 20-25)

  **Must NOT do**:
  - Stesse limitazioni task 26

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 26,27)

  **References**:
  - Task 20-25 (Variante C), Task 26 (struttura)

  **Acceptance Criteria**:
  - [ ] File `C_Ibrido/09_Offerta/offerta_tecnico_economica.md` creato
  - [ ] Struttura 10 sezioni

  **QA Scenarios**:
  ```
  Scenario: Verifica offerta Variante C
    Tool: Bash (grep)
    Steps:
      1. grep -c "^#\|^##\|^###" C_Ibrido/09_Offerta/offerta_tecnico_economica.md
      2. grep -i "quotazione\|€\|budget\|ibrido\|esclusioni" C_Ibrido/09_Offerta/offerta_tecnico_economica.md
    Expected Result: Offerta completa con costi ibridi
    Evidence: .omo/evidence/task-28/offer-c-check.txt
  ```

- [x] 29. Matrice di Confronto tra Varianti

  **What to do**:
  - Creare documento di confronto tra le 3 varianti:
    - Tabella comparativa con:
      | Criterio | A — Full Cloud GCP | B — On-Premise | C — Ibrido |
      |---|---|---|---|
      | Costo totale | €X | €X | €X |
      | Rischio complessivo | B/M/A | B/M/A | B/M/A |
      | Compliance ISO 27001 | Completa | Parziale | Completa |
      | Performance HPC | Buona (dipende latenza) | Massima (rete locale) | Buona (ibrida) |
      | Scalabilità | Massima | Limitata da HW | Alta |
      | Smart Working | Nativo | VPN | VPN + Cloud |
      | Tempo implementazione | 8-10 settimane | 12-16 settimane | 10-12 settimane |
      | Complessità | Bassa | Alta | Media |
      | Costi ricorrenti (3 anni) | €180k (GCP) | €50k (energia/manut) | €100-150k |
    - Analisi qualitativa: pro/contro per ogni variante
    - Raccomandazione motivata (basata su costi, rischi, compliance, scalabilità)
    - Grafico radar testuale

  **Must NOT do**:
  - Non essere di parte — presentare dati oggettivi

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: NO (dipende dalle offerte)
  - **Blocks**: F1-F4
  - **Blocked By**: Tasks 26,27,28

  **References**:
  - Tasks 26,27,28 (offerte) — Dati economici
  - Tutti i task tecnici (8-25) — Dati tecnici

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/matrice_confronto.md` creato
  - [ ] Include: tabella comparativa, analisi pro/contro, raccomandazione
  - [ ] Dati coerenti con le offerte (26,27,28)

  **QA Scenarios**:
  ```
  Scenario: Verifica matrice di confronto
    Tool: Bash (grep + Python per validazione)
    Steps:
      1. grep -c "Variante A\|Variante B\|Variante C\|Full Cloud\|On-Premise\|Ibrido" Condivisi/02_Project_Management/matrice_confronto.md
      2. python -c "validare che costi matrice == costi offerte"
    Expected Result: Matrice completa con tutte le varianti e dati coerenti
    Evidence: .omo/evidence/task-29/comparison-matrix-check.txt
  ```

- [x] 30. Registro Rischi

  **What to do**:
  - Creare il Risk Register per il progetto:
    - Identificare rischi per area (tecnici, organizzativi, economici, temporali)
    - Per ogni rischio: Descrizione | Probabilità (1-5) | Impatto (1-5) | Punteggio | Mitigazione | Contingenza | Responsabile
    - Rischi specifici: datacenter saturo, condizionamento limite, tempi consegna HW, downtime migrazione, resistenza al cambiamento, complessità integrazione AD/cloud
    - Aggiornare per ogni variante dove applicabile

  **Must NOT do**:
  - Non includere rischi non pertinenti (legali, di mercato)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 31,32)
  - **Blocked By**: Tasks 5,6,7

  **References**:
  - Task 5 (Project Charter) — Rischi preliminari
  - `01_Materiale/estratto_progetto.md` — Vincoli e criticità
  - `01_Materiale/Domande_Project_Edoardo_FORMATTED.xlsx` — Vincoli cliente (7gg shutdown, etc.)

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/registro_rischi.md` creato
  - [ ] ≥10 rischi identificati con probabilità, impatto, mitigazione

  **QA Scenarios**:
  ```
  Scenario: Verifica risk register
    Tool: Bash (grep)
    Steps:
      1. grep -c "Probabilità\|Impatto\|Punteggio\|Mitigazione" Condivisi/02_Project_Management/registro_rischi.md
    Expected Result: Risk register completo con ≥10 rischi
    Evidence: .omo/evidence/task-30/risk-register-check.txt
  ```

- [x] 31. Matrice RASCI

  **What to do**:
  - Creare matrice RASCI per il progetto:
    - Attività (da WBS): Assessment, Progettazione, Approvvigionamento, Configurazione, Migrazione, Test, Formazione base, Supporto
    - Ruoli: PM, Sistemista, Cliente (TP Group), Dirigenza, Fornitori HW/SW
    - Per ogni attività: R (Responsible), A (Accountable), S (Support), C (Consulted), I (Informed)
    - In formato tabella markdown

  **Must NOT do**:
  - Non includere ruoli non previsti

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 30,32)

  **References**:
  - Task 6 (WBS) — Attività
  - Task 5 (Project Charter) — Ruoli

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/matrice_rasci.md` creato
  - [ ] Copre tutte le attività principali e ruoli chiave

  **QA Scenarios**:
  ```
  Scenario: Verifica RASCI
    Tool: Bash (grep)
    Steps:
      1. grep "R\|A\|S\|C\|I" Condivisi/02_Project_Management/matrice_rasci.md
    Expected Result: Matrice RASCI completa
    Evidence: .omo/evidence/task-31/rasci-check.txt
  ```

- [x] 32. Template Report di Avanzamento

  **What to do**:
  - Creare template per report di avanzamento settimanale:
    - Sezioni: Stato complessivo (RAG status), Attività completate, Attività in corso, Prossime attività, Problemi/bloccanti, Rischi aggiornati, KPI (budget speso, % completamento, scostamenti)
    - Istruzioni compilazione
    - Formato markdown pronto per l'uso

  **Must NOT do**:
  - Non includere contenuti specifici (solo template vuoto)

  **Recommended Agent Profile**:
  - **Category**: `quick`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with Tasks 30,31)

  **References**:
  - Task 30 (Risk Register) — Rischi da riportare

  **Acceptance Criteria**:
  - [ ] File `Condivisi/02_Project_Management/template_report_avanzamento.md` creato
  - [ ] Include sezioni complete per report settimanale

  **QA Scenarios**:
  ```
  Scenario: Verifica template report
    Tool: Bash (grep)
    Steps:
      1. grep -i "stato\|completate\|corso\|prossime\|problemi\|KPI" Condivisi/02_Project_Management/template_report_avanzamento.md
    Expected Result: Template report completo
    Evidence: .omo/evidence/task-32/report-template-check.txt
  ```

---

## Final Verification Wave

> 4 review agent in PARALLEL. Tutti devono APPROVARE.
> Attendere OK esplicito dell'utente prima di completare.

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, grep content). For each "Must NOT Have": search codebase for forbidden patterns — reject with file:line if found. Check:
  - [ ] Assessment AS-IS completato (Thema + Pro Studio)
  - [ ] 3 varianti complete (A, B, C) con 6-7 documenti tecnici ciascuna
  - [ ] 3 offerte economico/tecniche con 10 sezioni
  - [ ] WBS ≥3 livelli, Gantt ≤12 settimane, shutdown ≤7gg
  - [ ] Matrice di confronto presente
  - [ ] Budget integrity: ogni variante ≤ budget dichiarato
  - [ ] Zero placeholder ("DA DEFINIRE", "[COSTO]", "[NOME]")
  - [ ] Zero riferimenti a file TP_Group/
  - [ ] Ogni sezione tecnica segue format REQUISITI→SOLUZIONE→DIMENSIONAMENTO→COSTI
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Coerenza e Budget Integrity** — `unspecified-high`
  Verify cross-document consistency and budget integrity:
  - [ ] I dati core sono coerenti tra tutti i documenti (50 dipendenti, 40 postazioni, 10+ remoto, 520k€ budget)
  - [ ] Budget: per ogni offerta, somma voci economiche == budget dichiarato (con scostamento massimo del 5% o motivato)
  - [ ] Gantt rispetta: 12 settimane attive, shutdown 7gg, milestone verificabili
  - [ ] WBS + Gantt coincidono (stesse attività, stesse durate)
  - [ ] Risk Register usa stessi rischi/esiti delle offerte
  - [ ] Matrice confronto usa stessi dati delle offerte
  - [ ] Nome TP Group scritto correttamente dappertutto (non "TPGroup", "TP_Group", etc.)
  Output: `Budget [N/N check] | Coerenza [N/N] | VERDICT`

- [x] F3. **Completezza Documentale** — `unspecified-high`
  Verify EVERY expected file exists and has meaningful content:
  - [ ] Condivisi/01_Assessment/assessment_thema_consulting.md
  - [ ] Condivisi/01_Assessment/assessment_prostudio.md
  - [ ] Condivisi/01_Assessment/gap_analysis.md
  - [ ] Condivisi/02_Project_Management/project_charter.md
  - [ ] Condivisi/02_Project_Management/wbs.md
  - [ ] Condivisi/02_Project_Management/gantt.md
  - [ ] Condivisi/02_Project_Management/matrice_rasci.md
  - [ ] Condivisi/02_Project_Management/registro_rischi.md
  - [ ] Condivisi/02_Project_Management/template_report_avanzamento.md
  - [ ] Condivisi/02_Project_Management/matrice_confronto.md
  - [ ] A_Full_Cloud_GCP/03_Rete_VPN/progetto_rete_vpn.md
  - [ ] A_Full_Cloud_GCP/04_Cluster_HPC/specifica_cluster_hpc.md
  - [ ] A_Full_Cloud_GCP/05_Pondus_App/architettura_pondus.md
  - [ ] A_Full_Cloud_GCP/06_Cloud_Migration/piano_migrazione_cloud.md
  - [ ] A_Full_Cloud_GCP/07_Backup_DR/architettura_backup_dr.md
  - [ ] A_Full_Cloud_GCP/08_Sicurezza_ISO27001/requisiti_sicurezza_iso27001.md
  - [ ] A_Full_Cloud_GCP/09_Offerta/offerta_tecnico_economica.md
  - ... stessi 7 file per B_On_Premise/ e C_Ibrido/
  - [ ] README.md nella root del progetto
  - [ ] Ogni file ha contenuto sostanziale (≥500 caratteri, non placeholder)
  - [ ] Ogni file formattato correttamente in markdown
  Output: `Files [N/N presenti] | Content [N/N validi] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual file content. Verify 1:1:
  - [ ] Ogni requisito del capitolato (estratto_progetto.md:152-178) è coperto nell'offerta
  - [ ] Ogni vincolo ISO 27001 (estratto_progetto.md:103-118) è coperto nei documenti sicurezza
  - [ ] Niente è stato costruito oltre lo scope (no runbook, no analisi legale, no formazione)
  - [ ] I 3 documenti di assessment coprono TUTTI i servizi della tabella (estratto_progetto.md:80-93)
  - [ ] Ogni variante è TECNICAMENTE plausibile (soluzioni realistiche, non fantascienza)
  - [ ] C'è contaminazione tra varianti? (Task 8 parla di roba di Task 9?)
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

- **Wave 1**: `docs(assessment): add AS-IS assessment for Thema and Pro Studio`
- **Wave 2**: `docs(variant-a): add full cloud GCP architecture documents`
- **Wave 2b**: `docs(variant-b): add on-premise architecture documents`
- **Wave 2c**: `docs(variant-c): add hybrid architecture documents`
- **Wave 3**: `docs(offer): add technical-economic offers and comparison matrix`
- **Wave Final**: `docs(review): final verification and consistency fixes`

---

## Success Criteria

### Verification Commands
```bash
# Verifica struttura directory
Get-ChildItem -Recurse -Directory "23_Project_Work_e_Laboratori/03_Progetti/ProjectWork_Infrastruttura_IT/"
# Verifica conteggio file markdown
Get-ChildItem -Recurse -Filter "*.md" "23_Project_Work_e_Laboratori/03_Progetti/ProjectWork_Infrastruttura_IT/"
# Verifica assenza placeholder
grep -r "DA DEFINIRE\|COSTO\|NOME" "23_Project_Work_e_Laboratori/03_Progetti/ProjectWork_Infrastruttura_IT/"
```

### Final Checklist
- [ ] Assessment AS-IS completato per Thema Consulting e Pro Studio
- [ ] 3 varianti architetturali complete e confrontabili
- [ ] 3 offerte tecnico/economiche (10 sezioni ciascuna)
- [ ] PM docs: Project Charter, WBS, Gantt, RASCI, Risk Register
- [ ] Matrice di confronto con costi/rischi/performance/compliance
- [ ] Budget integrity: ogni variante ≤ 520k€ o scostamento motivato
- [ ] Gantt rispetta 12 settimane attive, 7gg shutdown
- [ ] Zero placeholder ("DA DEFINIRE", "[COSTO]") nei documenti
- [ ] Zero riferimenti a file TP_Group/ esistenti
