# Architettura Backup — Full Cloud Azure

## Schema generale

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AZURE WEST EUROPE                             │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────┐       │
│  │                Recovery Services Vault                     │       │
│  │                   bvault-tpgroup-westeu                     │       │
│  │                                                             │       │
│  │  ┌────────────────────┐  ┌──────────────────────────┐      │       │
│  │  │ Azure Backup        │  │ Azure Site Recovery      │      │       │
│  │  │                     │  │                          │      │       │
│  │  │ • VM MediaWiki      │  │ • Replica VM MediaWiki   │      │       │
│  │  │   (daily, 30gg)     │  │   → North Europe         │      │       │
│  │  │ • Azure SQL DB      │  │                          │      │       │
│  │  │   (PITR 7gg + mens) │  └──────────────────────────┘      │       │
│  │  │ • File shares       │                                     │       │
│  │  │   (Azure Files)     │  ┌──────────────────────────┐      │       │
│  │  └────────────────────┘  │ Azure Backup (HPC on-prem)│      │       │
│  │                          │ • Dati job HPC            │      │       │
│  │  ┌────────────────────┐  │ • Config front-end        │      │       │
│  │  │ Microsoft 365       │  │ → Blob Storage (RA-GRS)  │      │       │
│  │  │ Backup (opzionale)  │  └──────────────────────────┘      │       │
│  │  │ • SharePoint        │                                     │       │
│  │  │ • Exchange Online   │                                     │       │
│  │  │ • OneDrive          │                                     │       │
│  │  │ → 1 anno retention │                                     │       │
│  │  └────────────────────┘                                     │       │
│  └──────────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
```

## Backup per servizio

| Servizio | Metodo | RPO | Retention | Costo/mese |
|---|---|---|---|---|
| **VM MediaWiki** | Azure Backup (daily, agent) | 24 ore | 30 giorni | ~€ 15 |
| **Azure SQL DB (Pondus)** | PITR automatico | 5 min | 7 giorni (+ long-term mensile 1 anno) | Incluso |
| **App Service Pondus** | Backup filesystem + Blob | 24 ore | 7 giorni | ~€ 5 |
| **M365 (posta, file, Teams)** | M365 Backup (opzionale) | 12 ore | 1 anno | ~€ 60/mese (50 utenti) |
| **M365 (retention nativa)** | Litigation hold + retention policy | — | 30-90 giorni | Incluso |
| **HPC on-prem (dati job)** | Azure Backup (MARS agent) | 24 ore | 90 giorni | ~€ 20 |
| **AD Samba4** | Backup nativo Samba4 + Azure Blob | 24 ore | 30 giorni | ~€ 5 |
| **Dynamics 365** | Export periodico + backup nativo | 24 ore | 30 giorni (export) | Incluso |
| **Azure DevOps** | Backup nativo Microsoft | Continuo | Illimitato (Microsoft managed) | Incluso |

## Storage Backup

| Tipo | Ridondanza | Utilizzo |
|---|---|---|
| Recovery Vault (RA-GRS) | Geo-ridondante (West EU + North EU) | VM, SQL, file shares |
| Blob Storage (RA-GRS) | Geo-ridondante | HPC data, AD backup |
| M365 Backup | Microsoft managed | M365 data |

## Costi totali backup

| Voce | Costo/mese |
|---|---|
| Azure Backup (VM + SQL + files) | ~€ 40 |
| Blob Storage RA-GRS (HPC, AD) | ~€ 15 |
| M365 Backup (50 utenti, opzionale) | ~€ 60 |
| **Totale backup** | **~€ 115/mese** |
