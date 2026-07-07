# Project Work e Laboratori — Appunti Strutturati

> **Corso:** ITS ICT Cloud Specialist 2025-2027
> **Materia:** 23_Project_Work_e_Laboratori
> **Ultimo aggiornamento:** 07/06/2026

---

## 📊 Indice dei Progetti

| Progetto | Percorso | Stato | Budget | Agenti |
| --- | --- | --- | --- | --- |
| **TP_Group** | `03_Progetti/TP_Group/` | ✅ Completo (9 aree) | € 520.000 | 9 specializzati |
| **ProjectWork_Infrastruttura_IT** | `03_Progetti/ProjectWork_Infrastruttura_IT/` | 🟡 Bozza (solo D completa) | € 520.000 + € 181k extra | 4 varianti |

---

## 📄 01 — TP_Group (Progetto Attivo)

### Scenario
Fusione Thema Consulting (30p, on-prem Torino) + Pro Studio (20p, full cloud GCP) → TP Group (50p, sede unica Torino, max 40 postazioni, conformità ISO 27001)

### 9 Aree + Deliverable

| # | Area | File chiave | Agente |
| --- | --- | --- | --- |
| 01 | **Assessment** | `assessment_as_is.md`, `gap_analysis.md`, 2 report aziendali | Assessment Analyst |
| 02 | **Rete e VPN** | `progetto_rete.md`, `progetto_vpn.md`, `schema_rete.md` | Network & VPN Engineer |
| 03 | **Sicurezza ISO 27001** | `requisiti_iso27001.md`, `politica_cifratura_accessi.md`, `matrice_rischi.md` | Security Officer |
| 04 | **Cluster HPC** | `progetto_cluster.md`, `confronto_costi_hpc.md` | HPC Architect |
| 05 | **Pondus App** | `architettura_pondus.md`, `piano_migrazione_pondus.md` | Application Architect |
| 06 | **Cloud Migration** | `strategia_cloud_ibrida.md`, `piano_migrazione_cloud.md`, `integrazione_identita.md` | Cloud Specialist |
| 07 | **Backup e DR** | `architettura_backup.md`, `piano_disaster_recovery.md`, `procedure_restore.md` | Backup & DR Engineer |
| 08 | **Offerta** | `offerta_tecnico_economica.md`, `quotazione_economica.md`, `checklist_completezza.md` | Bid Manager |
| 09 | **Project Management** | `project_charter.md`, `wbs.md`, `gantt.md`, `matrice_rasci.md`, `piano_costi.md`, `registro_rischi.md`, `template_report_avanzamento.md` | Project Manager |

### Costi TP_Group (€ 272.950 una tantum)

| Area | Una tantum | % |
| --- | --- | --- |
| Cluster HPC | € 191.600 | 70% |
| PM | € 19.500 | 7% |
| Rete | € 22.650 | 8% |
| Pondus | € 15.000 | 6% |
| Sicurezza | € 11.500 | 4% |
| Backup | € 7.200 | 3% |
| Cloud | € 5.500 | 2% |

### Decisioni cliente (18/06/2026)

| Decisione | Valore |
| --- | --- |
| Posta unificata | Zimbra (NO Google Workspace) |
| Office | MS365 per 50 utenti |
| File server | NextCloud (NO Google Drive) |
| CRM/TS | Odoo (migrazione da SugarCRM e Kimai) |
| Versioning | GiTea (migrazione da BitBucket) |
| Pondus | Da self-hosted a online |
| Tempi | 9-12 mesi migrazione, 3 anni ciclo vita |
| Smart working | Min 10 persone/giorno in remoto |
| Finestra manutenzione | Max 7 giorni |

---

## 📄 02 — ProjectWork_Infrastruttura_IT

### 4 Varianti Architetturali

| Variante | Target | Costo 3 anni | HPC | Posta |
| --- | --- | --- | --- | --- |
| **A — Full Cloud GCP** | Google Cloud | ~€ 549.720 | C2 (no IB) | Google Workspace |
| **B — On-Premise** | Infrastruttura fisica | ~€ 601.100 | 16 nodi IB 200G | Zimbra |
| **C — Ibrido** | On-prem + Cloud | ~€ 674.900 | 16 nodi + burst GCP | Workspace |
| **D — Full Cloud Azure** | Microsoft Azure | ~€ 570.756 | HB176-96rs IB 400G | M365 (già presente) |

### Stato avanzamento varianti

| Variante | Assessment | Rete | HPC | Pondus | Cloud | Backup | Sicurezza | Offerta | PM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A (GCP) | ✅ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ✅ |
| B (On-Prem) | ✅ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ✅ |
| C (Ibrido) | ✅ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ✅ |
| D (Azure) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Piano di test (Variante D)
24 test case (Rete 4, HPC 4, Pondus 4, Migrazione 4, DR 4, Sicurezza 4)

---

## 📄 03 — Gruppi di Lavoro

| Gruppo | Nome | Membri |
| --- | --- | --- |
| 1 | Digital Horizon Lab | Cavagnero, Huancayo Ramos, Mancini, Montaperto, Scaringella |
| 2 | H2C (Hybrid to Cloud) | Buscemi, Chiandoni, Ingargiola, Liguori, Pistone |
| 3 | Sprout | Angione, Cucchiara, Kouankeu Nya, Ravera, Sassi |
| 4 | **Forty Group** | Cignarelli, Stanziani, Mogavero, **Querio Gianetto**, Sasso, Tarallo |
| 5 | 5 Stack | Airoldi, Mattiolo, Sole, Santiago Merlo, Suriano |

---

## 📄 04 — To Do (prossimi passi)

- [ ] Compilare §3 "Presentazione azienda proponente" in offerta tecnico/economica
- [ ] Definire 2° ISP per ridondanza (TIM / WindTre / altri)
- [ ] Redigere piano di test funzionali per TP_Group (per ogni area)
- [ ] Compilare template report di avanzamento
- [ ] Completare varianti A/B/C di ProjectWork_Infrastruttura_IT
- [ ] Verificare consistenza budget tra TP_Group e varianti
- [ ] Validare incrociata tra agenti (dipendenze — vedere KANBAN.md)
- [ ] Rivedere offerta alla luce dell'intervista cliente del 18/06/2026

---

## 📄 05 — Note operative

- **Formato documenti:** Markdown con tabelle
- **Lingua:** Italiano (terminologia tecnica in inglese)
- **Costi:** Sempre IVA esclusa
- **Costi risorse:** Sistemista €500/gg e PM €650/gg sono EXTRA budget (coprono IT interno 3 anni)
- **Remote principale:** `github.com/edoardoquerio-pixel/Materie.git` branch `main`
- **Legenda KANBAN:** 🔴 Alta | 🟡 Media | 🟢 Bassa
