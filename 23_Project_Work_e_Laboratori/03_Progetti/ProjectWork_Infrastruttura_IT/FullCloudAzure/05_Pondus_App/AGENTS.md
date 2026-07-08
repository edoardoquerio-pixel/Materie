# Agente: Application Architect (Pondus) — Full Cloud Azure

## Ruolo

Progettazione della migrazione dell'applicazione Pondus da HW fisico on-prem ad Azure App Service + Azure SQL Database.

## Dipende da

- `01_Assessment/` (dati AS-IS Pondus)
- `03_Sicurezza_ISO27001/` (policy sicurezza)

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `architettura_pondus.md` | Architettura target su Azure PaaS |
| 02 | `piano_migrazione_pondus.md` | Piano di migrazione e rollback |

## Decisioni chiave Full Cloud Azure

- Runtime: **Azure App Service P1v3** (Linux container o Windows)
- Database: **Azure SQL Database S2** (50 DTU, 250 GB)
- Deployment: **Azure DevOps Pipelines** con staging slot
- Autenticazione: **Entra ID** (Easy Auth) per accesso clienti + JWT per API esterne
- Backup automatico: Azure SQL PITR + App Service backup
