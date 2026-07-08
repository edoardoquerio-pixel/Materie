# Architettura Pondus su Azure — Full Cloud Azure

## Architettura

```
CLIENTI                               AZURE WEST EUROPE
   │                              ┌──────────────────────────────────────┐
   │                              │        Resource Group                │
   │  HTTPS ──────────────────────►   rg-tpgroup-pondus-westeu           │
   │  pondus.tpgroup.it           │                                      │
   │                              │  ┌────────────────────────────────┐  │
   │                              │  │  App Service P1v3 (Linux/Win)  │  │
   │                              │  │  ┌─────────┐  ┌─────────────┐ │  │
   │                              │  │  │ PROD   │  │  STAGING    │ │  │
   │                              │  │  │ Slot   │  │  Slot       │ │  │
   │                              │  │  └────┬────┘  └──────┬──────┘ │  │
   │                              │  └───────┼──────────────┼─────────┘  │
   │                              │          │              │            │
   │                              │          ▼              ▼            │
   │                              │  ┌────────────────────────────────┐  │
   │                              │  │  Azure SQL Database S2         │  │
   │                              │  │  (50 DTU, 250 GB)              │  │
   │                              │  │  ┌──────────┐ ┌────────────┐  │  │
   │                              │  │  │ PROD DB  │ │  STAGING   │  │  │
   │                              │  │  │          │ │  DB        │  │  │
   │                              │  │  └──────────┘ └────────────┘  │  │
   │                              │  └────────────────────────────────┘  │
   │                              │                                      │
   │                              │  ┌────────────────────────────────┐  │
   │                              │  │  Azure Backup Vault             │  │
   │                              │  │  - SQL PITR (7 giorni)          │  │
   │                              │  │  - Long-term (mensile, 1 anno)  │  │
   │                              │  └────────────────────────────────┘  │
   │                              │                                      │
   │                              │  ┌────────────────────────────────┐  │
   │                              │  │  App Service Backup            │  │
   │                              │  │  - Filesystem (daily)          │  │
   │                              │  │  - Blob storage (7 giorni)     │  │
   │                              │  └────────────────────────────────┘  │
   └──────────────────────────────┴──────────────────────────────────────┘

ADMIN / SVILUPPATORI
   │
   ├──► Azure DevOps ─► CI/CD Pipeline ─► Staging ─► Swap ─► PROD
   │
   └──► Entra ID ─► Easy Auth ─► App Service
```

## Componenti e SKU

| Componente | SKU | Dettaglio | Costo/mese |
|---|---|---|---|
| App Service Plan | **P1v3** (Linux/Windows) | 2 vCPU, 8 GB RAM, 250 GB storage | € 113,50 |
| App Service (PROD) | Incluso nel plan | 1 slot deployment (PROD) | — |
| App Service (STAGING) | Incluso nel plan | 1 slot deployment (STAGING) | — |
| Azure SQL Database | **S2** (50 DTU) | 250 GB storage, PITR 7 giorni | € 64,00 |
| Azure SQL (STAGING) | **S0** (10 DTU) | Solo durante migrazione | € 18,00 |
| Azure Backup | Incluso | SQL PITR + long-term retention | € 0 (incluso in SQL) |
| **Totale** | | | **€ 195,50** |

## Stack tecnologico

| Layer | AS-IS (on-prem) | TO-BE (Azure) |
|---|---|---|
| Web server | MS IIS | Azure App Service (container Windows/Linux) |
| Runtime | .NET Framework (C#) | .NET 8/10 (da verificare compatibilità) |
| Database | MS SQL Server (HW dedicato) | Azure SQL Database S2 |
| Autenticazione | Form authentication | Entra ID Easy Auth + JWT |
| Deployment | Manuale (copia file IIS) | Azure DevOps Pipelines |
| Backup | Backup file system manuale | Azure SQL PITR + App Service backup |
| Storage files | HDD locale 1,2 TB | Azure Files (condiviso tra slot) |

**Nota**: Il codice C# legacy (probabilmente ASP.NET WebForms) richiede una analisi di compatibilità con Azure App Service Windows. In caso di incompatibilità, si valuta:
1. **App Service Windows** (compatibile con .NET Framework)
2. **VM Windows** (IaaS) come alternativa di ripiego
