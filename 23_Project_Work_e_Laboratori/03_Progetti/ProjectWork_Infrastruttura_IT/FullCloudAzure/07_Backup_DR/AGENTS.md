# Agente: Backup & DR Engineer — Full Cloud Azure

## Ruolo

Progettazione della soluzione di backup e disaster recovery cloud-native per TP Group, basata su Azure Backup e Azure Site Recovery.

## Dipende da

- `01_Assessment/` (gap analysis ISO 27001 su backup)
- `03_Sicurezza_ISO27001/` (requisiti DR e continuità)
- `06_Cloud_Migration/` (inventario servizi migrati)

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `architettura_backup.md` | Architettura backup cloud |
| 02 | `piano_disaster_recovery.md` | Piano di DR con RPO/RTO |

## Decisioni chiave Full Cloud Azure

- Backup VM MediaWiki: **Azure Backup** con Recovery Vault (RA-GRS)
- Backup Azure SQL: **PITR 7 giorni** + long-term retention mensile
- Backup M365: **Microsoft 365 Backup** (SharePoint, Exchange, OneDrive)
- DR cross-regione: **Azure Site Recovery** (West Europe → North Europe)
- HPC on-prem: backup su Azure (Azure Backup + archivio su Blob Storage)
