# Integrazione Architettura Pondus — Business Critical, Redis, Failover Automatico

## TL;DR

> **Quick Summary**: Aggiornare l'architettura Pondus e tutti i documenti downstream con le decisioni prese: Azure SQL Managed Instance Business Critical con Failover Group automatico, Redis Cache come layer intermedio, retention backup 35 giorni, chiarimento monolito vs microservizi.
>
> **Deliverables**:
> - `architettura_pondus.md` aggiornato con nuova architettura Redis + BC + failover
> - `offerta_tecnico_economica.md` costi allineati
> - `REPORT_COMPARATIVO_VARIANTI.md` sezioni 5, 9.2, 9.3, 10, 11 aggiornate
> - `matrice_confronto.md` costi Pondus allineati
> - `README.md` totale 3 anni aggiornato (se necessario)
>
> **Estimated Effort**: Short
> **Parallel Execution**: YES — Wave 1 (3 parallel docs)
> **Critical Path**: architettura_pondus.md → offerta/report/matrice/readme

---

## Context

### Original Request
Domande dell'utente su microservizi, scalabilità, e robustezza DB di Pondus. Risposte dell'utente (Q1-Q10):
- Monolito su AKS con HPA (non microservizi)
- Azure SQL MI → **Business Critical** 16 vCPU
- Calcoli in **C#** (non in SQL)
- **Failover automatico** (Failover Group, West Europe ↔ North Europe)
- **Redis Cache** come layer di caching tra AKS e SQL
- Retention backup: **35 giorni**
- DB size: ~200 GB
- Utenti: poche decine (con scalabilità futura)

### Interview Summary
**Key Discussions**:
- L'architettura attuale è un monolito containerizzato, non microservizi — OK per il carico attuale, HPA garantisce scalabilità
- Business Critical + failover group aumenta il costo SQL da ~€14.400/anno a ~€39.792/anno (+€25.392/anno)
- Redis Cache aggiunge ~€900/anno
- Nuovo totale Pondus ~€51.000/anno (+€26.292 vs vecchio)
- **Impatto budget**: da ~€410.880/3y a **~€489.756/3y** (+€78.876). Margine: **+€211.244** (70% budget)

---

## Work Objectives

### Core Objective
Allineare l'architettura Pondus e tutti i documenti derivati alle decisioni dell'utente su tier DB, caching, failover e scalabilità.

### Concrete Deliverables
- [ ] `D_Full_Cloud_Azure/05_Pondus_App/architettura_pondus.md` aggiornato
- [ ] `D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md` costi allineati
- [ ] `REPORT_COMPARATIVO_VARIANTI.md` sezioni interessate aggiornate
- [ ] `Condivisi/02_Project_Management/matrice_confronto.md` aggiornata
- [ ] `README.md` eventuale aggiornamento costo totale

### Must Have
- Diagramma architetturale con Redis + Business Critical + Failover Group
- Costi SQL calcolati correttamente (BC + HB + failover secondary)
- Redis Cache aggiunto a componenti, dimensionamento e costi
- Chiarimento esplicito: monolito, non microservizi
- Retention backup 35 giorni documentata
- Tutti i documenti downstream allineati allo stesso costo

### Must NOT Have (Guardrails)
- Non introdurre microservizi (resta monolito)
- Non modificare l'infrastruttura HPC o rete
- Non cambiare dimensionamento nodo AKS (resta D4s_v3)

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: NO (documenti markdown)
- **Automated tests**: None
- **Agent-Executed QA**: Verifica grep per coerenza costi cross-document

### QA Policy
Ogni task verifica che:
1. I costi siano coerenti tra architettura pondus → offerta → report comparativo → matrice
2. Il diagramma architetturale includa Redis + BC + failover
3. Non ci siano riferimenti a General Purpose o vecchi costi SQL

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (3 task in parallelo):
├── Task 1: architettura_pondus.md — diagramma, componenti, dimensionamento, costi
├── Task 2: offerta_tecnico_economica.md — costi SQL, Redis, totale 3 anni
└── Task 3: REPORT_COMPARATIVO_VARIANTI.md — sezioni 5, 9.2, 9.3, 10, 11

Wave 2 (2 task in parallelo):
├── Task 4: matrice_confronto.md — costi dettaglio Pondus
└── Task 5: README.md — totale Variante D (se cambiato)

Wave FINAL:
├── Task F1: Verifica coerenza cross-document (grep)
└── Task F2: Presentazione riepilogo modifiche
```

---

## TODOs

- [ ] 1. Aggiornare architettura_pondus.md

  **What to do**:
  - Sostituire diagramma architetturale: aggiungere Redis Cache layer tra AKS e SQL, aggiornare SQL a "Azure SQL MI Business Critical + Failover Group West Europe ↔ North Europe"
  - Tabella Componenti: aggiungere riga Redis Cache, aggiornare SQL a Business Critical con Active Geo-Replication automatica
  - Tabella Strategia containerizzazione: aggiungere nota "Monolito (non microservizi) — HPA scala repliche"
  - Sezione Migrazione DB: aggiornare target a Business Critical 16 vCPU, aggiungere setup Failover Group, retention PITR 35 giorni
  - Tabella Dimensionamento: aggiungere Redis Cache Standard C1, storage 200 GB, retention 35 giorni
  - Tabella Costi: 
    - SQL: 1 riga Primary BC ~€1.658/mese + 1 riga Secondary failover ~€1.658/mese
    - Redis: Standard C1 ~€75/mese
    - Ricalcolare totale annuo (~€51.000)
  - Aggiornare nota sotto costi per riflettere BC + failover + Redis

  **Must NOT do**:
  - Non modificare dimensionamento AKS (D4s_v3 invariato)
  - Non introdurre microservizi

  **Recommended Agent Profile**:
  - Category: `unspecified-high`
    - Reason: Modifica strutturale di un documento tecnico con impatto sui costi

  **Acceptance Criteria**:
  - [ ] Diagramma mostra Redis Cache tra AKS e SQL
  - [ ] SQL specificato come Business Critical con Failover Group
  - [ ] Costi SQL: ~€39.792/anno (primario + secondario con HB)
  - [ ] Redis: ~€900/anno
  - [ ] Totale annuo Pondus aggiornato (~€51.000)
  - [ ] Retention backup: 35 giorni

  **QA Scenarios**:
  ```
  Scenario: Verifica costi SQL
    Tool: grep
    Preconditions: File aggiornato
    Steps:
      1. grep "Business Critical\|€39.792\|€1.658" architettura_pondus.md
    Expected Result: Tutti e 3 i pattern trovati
    Evidence: .omo/evidence/task-1-sql-cost.txt

  Scenario: Verifica Redis presente
    Tool: grep
    Steps:
      1. grep -i "redis\|Redis Cache" architettura_pondus.md
    Expected Result: Redis presente in diagramma, componenti, dimensionamento e costi
    Evidence: .omo/evidence/task-1-redis.txt

  Scenario: Verifica nessun riferimento a General Purpose
    Tool: grep
    Steps:
      1. grep -i "General Purpose" architettura_pondus.md
    Expected Result: 0 occorrenze (tranne eventuale nota di confronto)
    Evidence: .omo/evidence/task-1-no-gp.txt
  ```

  **Commit**: YES
  - Message: `docs(pondus): upgrade SQL to Business Critical, add Redis + Failover Group`
  - Files: `D_Full_Cloud_Azure/05_Pondus_App/architettura_pondus.md`

- [ ] 2. Aggiornare offerta_tecnico_economica.md

  **What to do**:
  - Nella sezione "Dettaglio costi ricorrenti": aggiornare riga SQL da ~€14.400 a ~€39.792 (BC + failover)
  - Aggiungere riga "Azure Cache for Redis" ~€900/anno
  - Ricalcolare totale ricorrente anno 1 e anno 2-3
  - Ricalcolare totale complessivo 3 anni
  - Aggiornare margine residuo
  - Nella sezione "Modifiche rispetto a preventivo precedente": aggiungere delta SQL e Redis

  **Must NOT do**:
  - Non modificare altri costi (HPC, M365, Odoo, etc.)

  **Acceptance Criteria**:
  - [ ] SQL cost: ~€39.792/anno
  - [ ] Redis cost: ~€900/anno
  - [ ] Nuovo totale 3 anni calcolato correttamente
  - [ ] Margine aggiornato

  **QA Scenarios**:
  ```
  Scenario: Verifica costi SQL e Redis in offerta
    Tool: grep
    Steps:
      1. grep "€39.792\|€900\|Redis" offerta_tecnico_economica.md
    Expected Result: Entrambi i costi presenti
    Evidence: .omo/evidence/task-2-offerta-costs.txt
  ```

  **Commit**: YES (con task 3)
  - Message: `docs(offerta): aggiorna costi SQL BC e Redis`
  - Files: `D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md`

- [ ] 3. Aggiornare REPORT_COMPARATIVO_VARIANTI.md

  **What to do**:
  - Sezione 5 (Confronto Pondus): aggiornare costo annuo D, delta vs GCP
  - Sezione 9.2: aggiornare riga SQL e Redis, ricalcolare totale D
  - Sezione 9.3: aggiornare ricorrente e totale 3 anni D
  - Sezione 10 (SWOT): aggiornare costi e punti di forza/debolezza
  - Sezione 11 (Raccomandazione): aggiornare budget residuo

  **Acceptance Criteria**:
  - [ ] Costo annuo Pondus D aggiornato
  - [ ] Costo annuo Variante D aggiornato
  - [ ] Totale 3 anni Variante D aggiornato
  - [ ] Margine budget aggiornato

  **QA Scenarios**:
  ```
  Scenario: Verifica coerenza costi report
    Tool: grep
    Steps:
      1. grep "~€" REPORT_COMPARATIVO_VARIANTI.md | head -20
    Expected Result: Costi allineati con offerta
    Evidence: .omo/evidence/task-3-report-costs.txt
  ```

  **Commit**: YES (con task 2)
  - Message: `docs(report): aggiorna costi Pondus BC + Redis`
  - Files: `REPORT_COMPARATIVO_VARIANTI.md`

- [ ] 4. Aggiornare matrice_confronto.md

  **What to do**:
  - Nella sezione Confronto Costi: aggiornare totale Variante D
  - Nella sezione Dettaglio Costi Variante D: aggiornare SQL e Redis
  - Nella sezione SWOT e Raccomandazione: aggiornare se necessario

  **Acceptance Criteria**:
  - [ ] Dettaglio costi Pondus D aggiornato
  - [ ] Totale 3 anni D aggiornato

  **QA Scenarios**:
  ```
  Scenario: Verifica costi matrice
    Tool: grep
    Steps:
      1. grep "~€" Condivisi/02_Project_Management/matrice_confronto.md | head -15
    Expected Result: Totale 3 anni D allineato
    Evidence: .omo/evidence/task-4-matrice-costs.txt
  ```

  **Commit**: YES (con task 5)
  - Message: `docs(matrice): aggiorna costi Pondus Variante D`
  - Files: `Condivisi/02_Project_Management/matrice_confronto.md`

- [ ] 5. Aggiornare README.md (se necessario)

  **What to do**:
  - Se il totale 3 anni Variante D cambia, aggiornare la riga nella tabella varianti

  **Acceptance Criteria**:
  - [ ] Costo Variante D in README aggiornato se cambiato

  **Commit**: YES (con task 4)
  - Message: `docs(readme): aggiorna costo Variante D`
  - Files: `README.md`

---

## Final Verification Wave

- [ ] F1. **Cross-Document Consistency Check**
  Grep tutti i file per verificare che:
  - Costo SQL BC + failover: ~€39.792/anno in tutti i documenti
  - Redis Cache: ~€900/anno in tutti i documenti
  - Totale 3 anni Variante D identico in offerta, report, matrice, readme
  - Nessun riferimento residuo a General Purpose o vecchi costi SQL
  - Output: `Documenti [N/N consistenti] | Costi [N/N match] | VERDICT`

---

## Commit Strategy

- **1**: `docs(pondus): upgrade SQL to Business Critical, add Redis + Failover Group`
- **2-3**: `docs(offerta+report): aggiorna costi Pondus BC e Redis`
- **4-5**: `docs(matrice+readme): aggiorna costi Pondus Variante D`

---

## Success Criteria

### Verification Commands
```bash
# Verifica SQL BC in tutti i documenti
grep -r "Business Critical\|€39.792" D_Full_Cloud_Azure/05_Pondus_App/ REPORT_COMPARATIVO_VARIANTI.md Condivisi/02_Project_Management/matrice_confronto.md

# Verifica Redis in tutti i documenti
grep -ri "redis" D_Full_Cloud_Azure/05_Pondus_App/ REPORT_COMPARATIVO_VARIANTI.md

# Verifica nessun General Purpose residuo
grep -ri "General Purpose" D_Full_Cloud_Azure/05_Pondus_App/

# Verifica totale 3 anni allineato
grep -r "~€" D_Full_Cloud_Azure/09_Offerta/offerta_tecnico_economica.md REPORT_COMPARATIVO_VARIANTI.md | grep "410\|489\|490"
```

### Final Checklist
- [ ] Diagramma pondus include Redis → BC → Failover Group
- [ ] Costo SQL aggiornato (~€39.792/anno)
- [ ] Redis aggiunto (~€900/anno)
- [ ] Retention backup 35 giorni documentata
- [ ] Tutti i documenti downstream allineati
- [ ] Nessun riferimento a General Purpose residuo
- [ ] Monolito (non microservizi) chiaramente documentato
