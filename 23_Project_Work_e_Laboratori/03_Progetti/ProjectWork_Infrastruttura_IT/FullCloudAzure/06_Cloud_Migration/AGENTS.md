# Agente: Cloud Migration Specialist — Full Cloud Azure

## Ruolo

Specialista migrazione responsabile della transizione dei servizi TP Group dall'ecosistema attuale verso Full Cloud Azure + Ecosistema Microsoft.

## Input

- `../01_Assessment/assessment_as_is.md`
- `../01_Assessment/gap_analysis.md`
- `../05_Pondus_App/architettura_pondus.md`
- `../05_Pondus_App/piano_migrazione_pondus.md`
- `../03_Sicurezza_ISO27001/`

## Decisioni chiave

| Decisione | Valore |
|---|---|
| Target | Ecosistema Microsoft (M365 + Azure + Dynamics) |
| Regione Azure | West Europe |
| Runtime Pondus | Azure App Service (code) + Azure SQL Database |
| Unica eccezione | Media Wiki su VM Azure (documentazione) |
| CI/CD | Azure DevOps (Repos + Pipelines) |
| Esclusi | HPC (on-prem), Pondus (percorso separato) |

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `01_Perimetro.md` | Perimetro del progetto, inclusi/esclusi |
| 02 | `02_Architettura_TO_BE.md` | Architettura TO-BE con schema |
| 03 | `03_Mappatura_Servizi.md` | Mappatura AS-IS → TO-BE per ogni servizio (M1-M12) |
| 04 | `04_Schema_Connettivita.md` | Schema connettività rete e identità |
| 05 | `05_Costi.md` | Costi una tantum, ricorrenti, budget, costi evitati |
| 06 | `06_Roadmap_Migrazione.md` | Roadmap con fasi, attività, rollback |
| 07 | `07_Rischi_Mitigazioni.md` | Rischi, probabilità, impatto, mitigazioni |
| 08 | `08_Cronoprogramma.md` | Cronoprogramma con tempi e deliverable |
| 09 | `09_Costi_Risorse.md` | Costi risorse sistemista e PM (extra budget) |
| 10 | `10_Riepilogo_Decisioni.md` | Riepilogo decisioni e budget |

## Dipendenze

- 01_Assessment (dati AS-IS)
- 03_Sicurezza_ISO27001 (policy)
- 05_Pondus_App (architettura applicativa)
- 06_Cloud_Migration (strategia cloud preesistente)
- 08_Offerta_Documenti (quotazione finale)
- 09_Project_Management (WBS, Gantt)
