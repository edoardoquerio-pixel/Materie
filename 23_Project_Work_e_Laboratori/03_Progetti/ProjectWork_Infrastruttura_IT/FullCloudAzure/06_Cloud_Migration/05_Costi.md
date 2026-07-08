# 05 — Costi

> **Documento:** Costi di migrazione e ricorrenti per Full Cloud Azure  
> **Regione Azure:** West Europe  
> **Tasso cambio:** 1 USD = €0,8735 (ECB luglio 2026)  
> **IVA:** Esclusa  
> **Data:** Luglio 2026

---

## 5.1 Una tantum (migrazione)

| # | Voce | Dettaglio | Costo |
| --- | --- | --- | --- |
| S1 | Migrazione posta | Zimbra + Google Workspace → Exchange Online (50 utenti, IMAP/tool) | € 1.500 |
| S2 | Migrazione file | NextCloud + Google Drive → SharePoint/OneDrive (Migration Manager) | € 2.500 |
| S3 | Setup Entra ID | Sincronizzazione AD Samba4 + MFA + Conditional Access | € 1.500 |
| S4 | Setup Azure DevOps | Migrazione repo (GiTea + BitBucket) + setup pipelines | € 1.000 |
| S5 | Migrazione Media Wiki | Spostamento istanza on-prem + GCP → VM Azure B2s | € 500 |
| S6 | Configurazione Dynamics 365 | Setup Sales + BC, migrazione dati (Odoo, Profis, Sugar, Kimai) | € 5.000 |
| | **Totale una tantum** | | **€ 12.000** |

---

## 5.2 Ricorrenti — mensili

| # | Voce | Costo/mese | Fonte |
| --- | --- | --- | --- |
| R1 | M365 Business Premium (50 utenti × €20,60) | € 1.030,00 | Microsoft listino EU 2026, annual commitment |
| R2 | Azure App Service P1v3 (Linux, PAYG, West EU) | € 113,50 | Azure Retail Prices API ($0,178/h × 730h × 0,8735) |
| R2b | *App Service P1v3 (1 anno reserved)* | *€ 74,00* | *Risparmio -35%* |
| R3 | Azure SQL DB S2 50 DTU (West EU) | € 64,00 | Azure Retail Prices API ($2,42/giorno × 365/12 × 0,8735) |
| R4 | Azure DevOps (5 free + 45 × €5,25) | € 236,25 | Microsoft listino ($6/utente/mese × 0,8735) |
| R5 | VM B2s Linux (West EU, PAYG) | € 30,60 | Azure Retail Prices API ($0,048/h × 730h × 0,8735) |
| R5b | *VM B2s (1 anno savings plan)* | *€ 23,26* | *Risparmio -24%* |
| R6 | Dynamics 365 Sales Professional (20 utenti × €56,30) | € 1.126,00 | Microsoft IE listino, annual commitment |
| R7 | Dynamics 365 BC Essentials (10 utenti × €69,30) | € 693,00 | Microsoft IE listino, annual commitment |
| R8 | HPC Azure burst — CycleCloud head node (D2s_v3) | € 76,50 | Azure Retail Prices PAYG ($0,12/h × 730h × 0,8735) |
| R9 | HPC Azure burst — Azure Managed Lustre (4 TB) | € 80,00 | Azure Retail Prices, PAYG |
| R10 | HPC Azure burst — HB176-96rs v4 SPOT (8 nodi × 8h × 200gg) media/mese | € 1.612,00 | Azure Retail Prices SPOT ($1,73/h × 8 × 1.600h/anno ÷ 12 × 0,8735) |
| | **Totale PAYG** | **€ 5.115,35** | |
| | *Totale con reserved/savings* | *€ 4.993,85* | |

---

## 5.3 Ricorrenti — annuali

| # | Voce | Costo/anno PAYG | Costo/anno reserved |
| --- | --- | --- | --- |
| R1 | M365 Business Premium | € 12.360 | € 12.360 |
| R2 | Azure App Service P1v3 | € 1.362 | € 887 |
| R3 | Azure SQL DB S2 | € 772 | € 772 |
| R4 | Azure DevOps | € 2.835 | € 2.835 |
| R5 | VM B2s Media Wiki | € 367 | € 279 |
| R6 | Dynamics 365 Sales Pro | € 13.512 | € 13.512 |
| R7 | Dynamics 365 BC Essentials | € 8.316 | € 8.316 |
| R8 | HPC CycleCloud head node D2s_v3 | € 918 | € 918 |
| R9 | HPC Azure Managed Lustre 4 TB | € 960 | € 960 |
| R10 | HPC HB176-96rs v4 SPOT (8 nodi) | € 19.341 | € 19.341 |
| | **Totale anno** | **€ 64.549** | **€ 63.086** |

---

## 5.4 Budget

| Voce | Valore |
|---|---|
| Budget totale progetto | € 520.000 |
| Spesa già prevista (piano_costi.md) | € 272.950 |
| **Margine disponibile** | **€ 247.050** |
| Costo una tantum migrazione | € 12.000 |
| Costo ricorrente primo anno (PAYG) | € 64.549 |
| **Costo totale primo anno** | **~€ 56.988** |
| **Margine residuo** | **~€ 190.062** |

### Distribuzione budget migrazione

```
Budget 520K€
├── Spesa già prevista: 272.950€ (52,5%)
│   ├── Rete/VPN: 22.650€
│   ├── Sicurezza: 11.500€
│   ├── Cluster HPC: 191.600€
│   ├── Pondus: 15.000€
│   ├── Cloud Migration: 5.500€
│   ├── Backup/DR: 7.200€
│   └── Project Management: 19.500€
│
├── Migrazione Microsoft + HPC Azure: 76.549€ (14,7%)
│   ├── Una tantum: 12.000€
│   └── Ricorrente anno 1: 64.549€
│
└── Margine residuo: 170.501€ (32,8%)
```

---

## 5.5 Costi evitati (dismissione servizi)

| Servizio dismesso | Costo evitato/mese | Costo evitato/anno |
| --- | --- | --- |
| Google Workspace (20 utenti) | ~€ 200 | ~€ 2.400 |
| Google Meet | ~€ 0 (incluso in Workspace) | ~€ 0 |
| Google Drive storage | ~€ 0 (incluso in Workspace) | ~€ 0 |
| BitBucket (20 utenti) | ~€ 50 | ~€ 600 |
| Odoo (20 utenti) | ~€ 400 | ~€ 4.800 |
| **Totale risparmio** | **~€ 650/mese** | **~€ 7.800/anno** |

### Consumo elettrico evitato (dismissione VM on-prem)

| VM dismessa | Watt stimati | Costo energia/anno (€0,25/kWh) |
| --- | --- | --- |
| Zimbra (VM Linux) | 150W | ~€ 330 |
| NextCloud (VM Linux) | 150W | ~€ 330 |
| Sugar CRM (VM Linux) | 100W | ~€ 220 |
| Kimai (VM Linux) | 100W | ~€ 220 |
| GiTea (VM Linux) | 100W | ~€ 220 |
| **Totale risparmio energia/anno** | | **~€ 1.320** |

---

## 5.6 Riepilogo costi 3 anni (ciclo vita progetto)

| Anno | Una tantum | Ricorrenti | Totale anno |
| --- | --- | --- | --- |
| Anno 1 | € 12.000 | € 64.549 | € 76.549 |
| Anno 2 | € 0 | € 64.549 | € 64.549 |
| Anno 3 | € 0 | € 64.549 | € 64.549 |
| **Cumulato 3 anni** | **€ 12.000** | **€ 193.647** | **€ 205.647** |
| Risparmio servizi dismessi (3 anni) | | | ~€ 23.400 |
| **Costo netto 3 anni** | | | **~€ 182.247** |
