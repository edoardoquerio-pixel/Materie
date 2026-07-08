# Piano Costi — Full Cloud Azure

## Budget

| Voce | Budget |
|---|---|
| Budget totale progetto | € 520.000 |
| Investimento iniziale (una tantum) | € 82.200 |
| Servizi cloud anno 1 | € 64.253 |
| **Totale anno 1** | **€ 146.453** |
| **Margine residuo** | **~€ 391.302** |

## Costi per area

| Area | Una tantum | Ricorrente/anno |
|---|---|---|
| **Rete / VPN** | | |
| FortiGate FG-100F HA cluster | € 7.000 | — |
| Switch L3 48 porte PoE+ (×2) | € 2.400 | — |
| Switch accesso 24 porte (×3) | € 1.200 | — |
| Access Point WiFi 6 (×4) | € 1.000 | — |
| UPS rack 1500 VA (×2) | € 1.200 | — |
| Cablaggio strutturato cat.6A | € 6.000 | — |
| 2° ISP FTTH 1 Gbps | — | € 4.200 |
| *Subtotale* | *€ 18.800* | *€ 4.200* |
| **Sicurezza** | | |
| Licenze/configurazione ISO 27001 | € 8.000 | — |
| Audit iniziale sicurezza | € 3.500 | — |
| *Subtotale* | *€ 11.500* | *€ 0* |
| **Cluster HPC** | | |
| Rinnovo licenze cluster on-prem (3 anni) | € 10.000 | — |
| Potenziamento InfiniBand | € 6.000 | — |
| Azure CycleCloud HB176-96rs v4 SPOT (8 nodi × 8h × 200gg) | — | € 19.341 |
| Azure CycleCloud head node D2s_v3 (24/7 PAYG) | — | € 918 |
| Azure Managed Lustre 4 TB | — | € 960 |
| *Subtotale (senza ER)* | *€ 16.000* | *€ 21.219* |
| *Subtotale (con ER)* | *€ 16.000* | *€ 24.819* |
| **Pondus su Azure** | | |
| Analisi compatibilità codice | € 2.000 | — |
| Adattamento codice (se necessario) | € 10.000 (media) | — |
| Setup Azure App + SQL | € 1.500 | — |
| Test e validazione | € 2.000 | — |
| Azure App Service P1v3 | — | € 1.362 |
| Azure SQL DB S2 | — | € 772 |
| *Subtotale* | *€ 15.500* | *€ 2.134* |
| **Cloud Migration (M1-M11)** | | |
| Migrazione posta | € 1.500 | — |
| Migrazione file | € 2.500 | — |
| Setup Entra ID + MFA | € 1.500 | — |
| Setup Azure DevOps | € 1.000 | — |
| Migrazione MediaWiki | € 500 | — |
| Configurazione Dynamics 365 | € 5.000 | — |
| M365 Business Premium (50 utenti) | — | € 12.360 |
| Dynamics 365 Sales Pro (20 utenti) | — | € 13.512 |
| Dynamics 365 BC Essentials (10 utenti) | — | € 8.316 |
| Azure DevOps (45 utenti) | — | € 2.835 |
| VM B2s MediaWiki | — | € 367 |
| Azure VPN Gateway | — | € 1.170 |
| *Subtotale* | *€ 12.000* | *€ 38.560* |
| **Backup / DR** | | |
| Configurazione Azure Backup | € 3.500 | — |
| Configurazione Azure Site Recovery | € 2.000 | — |
| Test DR | € 1.700 | — |
| Azure Backup (VM + SQL + files) | — | € 480 |
| Blob Storage RA-GRS (HPC, AD) | — | € 180 |
| M365 Backup (opzionale) | — | € 720 |
| Azure Site Recovery | — | € 360 |
| *Subtotale* | *€ 7.200* | *€ 1.740* |
| **Project Management** | | |
| PM (17 giorni × €650) — extra budget | — | € 11.050 |
| Sistemista (55 giorni × €500) — extra budget | — | € 27.500 |
| *Subtotale (extra budget)* | *€ 0* | *€ 38.550* |
| **Formazione** | | |
| Formazione utenti base (M365, Dynamics, Teams, amministratori) | € 3.000 | — |
| Formazione nuova infrastruttura TP_Group (7 moduli: rete, Azure, DevOps, HPC, backup, sicurezza) | € 4.000 | — |
| Documentazione | € 2.000 | — |
| *Subtotale* | *€ 9.000* | *€ 0* |

## Riepilogo

| Categoria | Una tantum | Ricorrente/anno |
|---|---|---|
| Infrastruttura e servizi (A) | € 90.000 | € 58.669 |
| Risorse interne (B) — extra budget | € 0 | € 38.550 |
| **Totale A + B anno 1** | **€ 90.000** | **€ 97.219** |
| Budget disponibile | € 520.000 | |
| **Margine residuo** | | **~€ 332.781** |
