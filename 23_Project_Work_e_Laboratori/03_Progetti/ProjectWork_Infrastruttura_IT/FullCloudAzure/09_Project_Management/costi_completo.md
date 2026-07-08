# Costi Completi — Full Cloud Azure

> **Scope:** tutti i costi del progetto, estratti da specifica_cluster_hpc.md, 05_Costi.md, offerta_tecnico_economica.md, quotazione_economica.md, piano_costi.md, piano_economico.md, attivita_sede_remoto.md
>
> **Cambio:** 1 USD = €0,8735 (ECB July 2026)
> **Regione:** West Europe
> **Ultima verifica:** Prezzi HPC verificati via Azure Retail Prices API (luglio 2026)

---

## 1. Investimento iniziale — Una tantum

### 1.1 Rete / VPN

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 1 | FortiGate FG-100F HA cluster (FortiCare 3 anni) | 2 | € 3.500 | **€ 7.000** |
| 2 | Switch Core L3 48 porte PoE+ | 2 | € 1.200 | **€ 2.400** |
| 3 | Switch accesso 24 porte PoE+ | 3 | € 400 | **€ 1.200** |
| 4 | Access Point WiFi 6 triband | 4 | € 250 | **€ 1.000** |
| 5 | UPS rack 1500 VA | 2 | € 600 | **€ 1.200** |
| 6 | Cablaggio strutturato cat.6A | 1 | — | **€ 6.000** |
| 7 | Accessori (SFP+ ×20, PDU rack, passacavi, console) | 1 | — | **€ 1.200** |
| 8 | Smaltimento RAEE apparati obsoleti | 1 | — | **€ 300** |
| | **Subtotale Rete** | | | **€ 20.500** |

### 1.2 Sicurezza

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 9 | Licenze/configurazione ISO 27001 | 1 | — | **€ 8.000** |
| 10 | Audit iniziale sicurezza | 1 | — | **€ 3.500** |
| | **Subtotale Sicurezza** | | | **€ 11.500** |

### 1.3 Cluster HPC (on-prem upgrade)

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 11 | Rinnovo licenze/supporto cluster on-prem (3 anni) | 1 | — | **€ 10.000** |
| 12 | Potenziamento rete InfiniBand (cavi, switch) | 1 | — | **€ 6.000** |
| | **Subtotale HPC on-prem** | | | **€ 16.000** |

### 1.4 Pondus su Azure (setup)

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 13 | Analisi compatibilità codice | 1 | — | **€ 2.000** |
| 14 | Adattamento codice (se necessario, media stimata) | 1 | — | **€ 10.000** |
| 15 | Setup Azure App + SQL | 1 | — | **€ 1.500** |
| 16 | Test e validazione | 1 | — | **€ 2.000** |
| | **Subtotale Pondus setup** | | | **€ 15.500** |

### 1.5 Cloud Migration (servizi professionali)

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 17 | Migrazione posta (Zimbra + GWS → Exchange Online) | 1 | — | **€ 1.500** |
| 18 | Migrazione file (NextCloud + Drive → SharePoint/OneDrive) | 1 | — | **€ 2.500** |
| 19 | Setup Entra ID + MFA + Conditional Access | 1 | — | **€ 1.500** |
| 20 | Setup Azure DevOps (repo + pipelines) | 1 | — | **€ 1.000** |
| 21 | Migrazione MediaWiki (on-prem + GCP → VM B2s) | 1 | — | **€ 500** |
| 22 | Configurazione Dynamics 365 (Sales + BC, migrazione dati) | 1 | — | **€ 5.000** |
| | **Subtotale Migration setup** | | | **€ 12.000** |

### 1.6 Backup / DR (setup)

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 23 | Configurazione Azure Backup | 1 | — | **€ 3.500** |
| 24 | Configurazione Azure Site Recovery | 1 | — | **€ 2.000** |
| 25 | Test DR | 1 | — | **€ 1.700** |
| | **Subtotale Backup/DR setup** | | | **€ 7.200** |

### 1.7 Formazione

#### Fase 1 — Formazione utenti (base, già pianificata)

| # | Modulo | Durata | Destinatari | Q.tà | €/cad | Totale |
|:-:|--------|:------:|-------------|:----:|:-----:|:------:|
| 26 | M365 base (posta, calendario, Office Online) | 4h | 50 utenti | 1 | — | **€ 3.000** |
| | *(include: Teams 2h, Dynamics Sales 4h per 20 utenti CRM, Dynamics BC 8h per 10 utenti ERP)* | | | | | |

#### Fase 2 — Formazione utilizzo nuova infrastruttura (dipendenti TP_Group)

| # | Modulo | Durata | Destinatari | Q.tà | €/cad | Totale |
|:-:|--------|:------:|-------------|:----:|:-----:|:------:|
| 27 | SharePoint/OneDrive: sincronia, condivisione, collaborazione | 2h | 50 utenti standard | 1 | € 400 | **€ 400** |
| 28 | Rete aziendale: FortiGate HA, VLAN, VPN WireGuard | 4h | IT staff (5-6) | 1 | € 600 | **€ 600** |
| 29 | Azure administration: portale, costi, monitoraggio | 4h | IT staff | 1 | € 600 | **€ 600** |
| 30 | Azure DevOps: repos, pipelines, CI/CD | 4h | Dev team (5-8) | 1 | € 600 | **€ 600** |
| 31 | HPC ibrido: CycleCloud, job submission, Lustre | 4h | HPC team (3-4) | 1 | € 600 | **€ 600** |
| 32 | Backup e DR: Azure Backup, Site Recovery, restore procedure | 4h | IT staff | 1 | € 600 | **€ 600** |
| 33 | Procedure sicurezza: ISO 27001, incident response, access review | 4h | IT staff + referenti | 1 | € 600 | **€ 600** |
| | **Subtotale Fase 2** | **26h** | | | | **€ 4.000** |

#### Documentazione

| # | Voce | Q.tà | €/cad | Totale |
|:-:|------|:----:|:-----:|:------:|
| 34 | Documentazione progetto (manuali utente, procedure, as-built) | 1 | — | **€ 2.000** |
| | **Subtotale Documentazione** | | | **€ 2.000** |

| | **Totale Formazione** | | | | **€ 9.000** |
| | *di cui Fase 1 (utenti base)* | | | | *€ 3.000* |
| | *di cui Fase 2 (nuova infrastruttura)* | | | | *€ 4.000* |
| | *di cui Documentazione* | | | | *€ 2.000* |

> **Totale investimento iniziale (costo acquisto):** **€ 91.700**
> **Totale investimento iniziale (prezzo vendita con ricarico 15%):** **~€ 86.225** (esclusi €10.000 adattamento Pondus e €9.000 formazione non ricaricati)

---

## 2. Costi cloud ricorrenti — Mensili

| # | Servizio | Dettaglio | €/mese | €/anno | Note |
|:-:|---------|-----------|:------:|:------:|------|
| 28 | M365 Business Premium | 50 utenti × €20,60 | € 1.030,00 | **€ 12.360** | Annual commitment |
| 29 | Dynamics 365 Sales Professional | 20 utenti × €56,30 | € 1.126,00 | **€ 13.512** | Annual commitment |
| 30 | Dynamics 365 BC Essentials | 10 utenti × €69,30 | € 693,00 | **€ 8.316** | Annual commitment |
| 31 | Azure App Service P1v3 (Linux) | PAYG | € 113,50 | **€ 1.362** | Reserved: €74/mese (-35%) |
| 32 | Azure SQL DB S2 50 DTU | — | € 64,00 | **€ 772** | |
| 33 | Azure DevOps | 5 free + 45 utenti × €5,25 | € 236,25 | **€ 2.835** | |
| 34 | VM B2s Linux (MediaWiki) | PAYG | € 30,60 | **€ 367** | Savings plan: €23,26 (-24%) |
| 35 | Azure VPN Gateway VpnGw1AZ | PAYG | € 97,50 | **€ 1.170** | |
| 36 | Azure Backup (VM + SQL + files) | — | € 40,00 | **€ 480** | |
| 37 | Blob Storage RA-GRS (HPC, AD) | — | € 15,00 | **€ 180** | |
| 38 | M365 Backup | Opzionale | € 60,00 | **€ 720** | |
| 39 | Azure Site Recovery | — | € 30,00 | **€ 360** | |
| 40 | **HPC HB176-96rs v4 SPOT** | 8 nodi × 8h × 200gg | € 1.612,00 | **€ 19.341** | Verificato API |
| 41 | **HPC CycleCloud head node D2s_v3** | 24/7 PAYG | € 76,50 | **€ 918** | |
| 42 | **HPC Azure Managed Lustre 4 TB** | ~€0,20/GB/mese | € 80,00 | **€ 960** | Prezzo non verificato via API |
| | | | | | |
| | **Totale cloud mensile** | | **~€ 5.304** | | |
| | **Totale cloud annuo** | | | **~€ 63.653** | |

### Dettaglio HPC SPOT — Verifica API

| Voce | Valore |
|------|--------|
| SKU | Standard_HB176-96rs_v4 (Linux) |
| Tipo prezzo | SPOT (consumption) |
| Prezzo API | $1,729728/h (West Europe, luglio 2026) |
| Prezzo in € | € 1,51/h ($1,73 × 0,8735) |
| Ore/giorno | 8 |
| Giorni/anno | 200 |
| Costo 1 nodo/anno | € 1,51 × 8 × 200 = **€ 2.418** |
| Costo 8 nodi/anno | € 2.418 × 8 = **€ 19.341** |
| Media/mese (÷12) | **€ 1.612** |

> **Nota:** Prezzo originale documentato era €1,46/h ($1,34/h × conversion). API mostra $1,73/h → +18%. Conseguenza: costo passato da €2.144 a **€19.341/anno** (9×).

---

## 3. Costi ricorrenti — Infrastruttura on-prem

| # | Voce | €/mese | €/anno |
|:-:|------|:------:|:------:|
| 43 | 2° ISP FTTH 1 Gbps | € 350 | **€ 4.200** |
| | | | |

---

## 4. Manodopera (extra budget — fuori dai ricorrenti cloud)

| # | Ruolo | Giorni | €/gg | In sede | Da remoto | Totale |
|:-:|-------|:------:|:----:|:------:|:---------:|:------:|
| 44 | Sistemista senior | 55 | € 500 | 15 gg (€ 7.500) | 40 gg (€ 20.000) | **€ 27.500** |
| 45 | Project Manager | 17 | € 650 | 0 gg | 17 gg (€ 11.050) | **€ 11.050** |
| 46 | Consulente Dynamics | 10 | € 600 | 0 gg | 10 gg (€ 6.000) | **€ 6.000** |
| | **Totale** | **82 gg** | | **15 gg** | **67 gg** | **€ 44.550** |

### Costo del lavoro (azienda)

| # | Ruolo | Costo/gg | Tariffa/gg | Margine/gg | Margine % |
|:-:|-------|:--------:|:----------:|:----------:|:---------:|
| 47 | Sistemista senior | ~€ 280 | € 500 | € 220 | 44% |
| 48 | Project Manager | ~€ 350 | € 650 | € 300 | 46% |
| 49 | Consulente Dynamics | ~€ 320 | € 600 | € 280 | 47% |

---

## 5. Trasferta

| # | Voce | Calcolo | Importo |
|:-:|------|---------|:-------:|
| 50 | Maggiorazione 25% su giorni in sede | 15 gg × €500 × 25% = €7.500 × 25% | **€ 1.875** |
| 51 | Attrezzatura trasferta (crimpatore, etichettatrice, continuity tester) | Una tantum | **€ 300** |
| | **Totale trasferta** | | **€ 2.175** |

---

## 6. Costi evitati (dismissione servizi legacy)

| # | Servizio | Risparmio/mese | Risparmio/anno |
|:-:|---------|:--------------:|:--------------:|
| 52 | Google Workspace (20 utenti) | ~€ 200 | **~€ 2.400** |
| 53 | Odoo SaaS (20 utenti) | ~€ 400 | **~€ 4.800** |
| 54 | BitBucket (20 utenti) | ~€ 50 | **~€ 660** |
| 55 | Manutenzione NAS QNAP + SAN NetApp | ~€ 375 | **~€ 4.500** |
| 56 | Elettricità datacenter (5 VM dismesse) | ~€ 110 | **~€ 1.320** |
| 57 | Licenze MS SQL Server | ~€ 167 | **~€ 2.000** |
| | **Totale risparmio** | **~€ 1.302/mese** | **~€ 15.680/anno** |
| | **Risparmio 3 anni** | | **~€ 47.040** |

---

## 7. Riepilogo budget — Anno 1

| Componente | Costo acquisto (azienda) | Prezzo vendita (cliente) |
|-----------|:-----------------------:|:-----------------------:|
| Forniture una tantum | € 85.500 | € 86.825 (*) |
| Manodopera (costo/tariffa) | € 24.550 | € 44.550 |
| Trasferta | € 2.175 | € 2.175 |
| Cloud ricorrenti (pass-through) | € 67.853 | € 67.853 |
| **Totale anno 1** | **€ 112.225** | **€ 201.403** |

| Budget | Valore |
|--------|:------:|
| Budget totale progetto | **€ 520.000** |
| Uscita cliente anno 1 | **€ 201.403** |
| Uscita cliente anno 2 (solo cloud) | **€ 67.853** |
| Uscita cliente anno 3 (solo cloud) | **€ 67.853** |
| **Cumulato 3 anni** | **€ 337.109** |
| **Margine residuo su budget** | **~€ 182.891 (35,2%)** |

(*) Prezzo vendita forniture: ricarico 15% su €75.500 (esclusi €10.000 adattamento Pondus e €9.000 formazione)

---

## 8. Piano di pagamento — Milestone

| # | Milestone | Condizione | % | Importo |
|:-:|----------|-----------|:-:|:-------:|
| M0 | Acconto avvio progetto | Contratto + ordine apparati rete | 19,4% | **€ 25.000** |
| M1 | Foundation completata | VNet, VPN, FortiGate HA, Entra ID, tenant M365 | 15,5% | **€ 20.000** |
| M2 | Infrastruttura on-prem pronta | Cablaggio, apparati, VLAN, WiFi, 2° ISP | 15,5% | **€ 20.000** |
| M3 | Posta + File migrati | 50 caselle Exchange, SharePoint/OneDrive | 10,9% | **€ 14.000** |
| M4 | Dynamics 365 attivo | Sales + BC, dati migrati, test pilota | 13,2% | **€ 17.000** |
| M5 | DevOps + MediaWiki + HPC burst | Repos, Wiki su Azure, CycleCloud, Lustre, test | 13,2% | **€ 17.000** |
| M6 | Test e accettazione | Test, formazione Fase 1 + Fase 2, documentazione | 10,9% | **€ 14.600** |
| M7 | Saldo finale | Dismissione VM, report, collaudo | 4,5% | **€ 5.950** |
| | **Totale** | | **100%** | **€ 133.550** |

---

## 9. Riepilogo 3 anni (cumulato)

| Anno | Una tantum | Cloud ricorrenti | Manodopera extra | **Totale cliente** |
|:---:|:----------:|:----------------:|:----------------:|:------------------:|
| 1 | € 86.825 | € 67.853 | € 44.550 | **€ 201.403** |
| 2 | € 0 | € 67.853 | € 13.250 | **€ 67.853** |
| 3 | € 0 | € 67.853 | € 13.250 | **€ 67.853** |
| | | | **Cumulato** | **€ 337.109** |
| | | | Budget | **€ 520.000** |
| | | | **Margine** | **~€ 182.891** |

---

## 10. Costi evitati (potenziali risparmi in sede)

| # | Voce | Risparmio | Condizione |
|:-:|------|:---------:|-----------|
| 58 | Switch core L3 48p (×2) | € 2.400 | Se switch esistenti sufficienti |
| 59 | Switch accesso 24p (×3) | € 1.200 | Se switch PoE+ già presenti |
| 60 | Cablaggio cat.6A | € 6.000 | Se cablaggio esistente adeguato |
| 61 | Potenziamento InfiniBand | € 6.000 | Se fabbrica HDR on-prem funzionante |
| 62 | M365 Backup | € 720/anno | Se retention nativa M365 sufficiente |
| | **Risparmio max** | **~€ 15.600 una tantum + € 720/anno** | |

---

## Indice delle fonti

| Costi | File principale | Linee |
|-------|----------------|:-----:|
| HPC dettaglio | `04_Cluster_HPC/specifica_cluster_hpc.md` | L80-116 |
| Cloud ricorrenti + migration | `06_Cloud_Migration/05_Costi.md` | L15-131 |
| Offerta economica | `08_Offerta_Documenti/offerta_tecnico_economica.md` | L88-146 |
| Quotazione per area | `08_Offerta_Documenti/quotazione_economica.md` | L9-68 |
| Budget per area + risorse | `09_Project_Management/piano_costi.md` | L7-86 |
| Conto economico azienda | `09_Project_Management/piano_economico.md` | L24-277 |
| Check forniture | `09_Project_Management/attivita_sede_remoto.md` | L26-127 |

---

*Generato il 07/07/2026 — Prezzi Azure verificati via API Retail Prices (West Europe, Linux, Consumption)*
