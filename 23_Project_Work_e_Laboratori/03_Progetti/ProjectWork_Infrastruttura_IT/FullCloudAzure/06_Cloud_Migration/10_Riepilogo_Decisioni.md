# 10 — Riepilogo Decisioni

> **Documento:** Riepilogo decisioni e budget della migrazione Full Cloud Azure  
> **Data:** Luglio 2026

---

## Decisioni di progetto

| Decisione | Valore |
|---|---|
| Target migrazione | Ecosistema Microsoft (M365 + Azure + Dynamics) |
| Regione Azure | **West Europe** (tutti i servizi) |
| Runtime Pondus | **Azure App Service (code) + Azure SQL Database** |
| Unica eccezione Microsoft | **Media Wiki su VM Azure** (documentazione — personalizzazioni non migrabili) |
| CI/CD | **Azure DevOps** (Repos + Pipelines) |
| Esclusi dal perimetro | **HPC** (on-prem), **Pondus** (percorso separato) |

---

## Mappatura servizi

| # | Servizio | AS-IS | TO-BE | Piattaforma |
| --- | --- | --- | --- | --- |
| M1 | Posta/Calendario | Zimbra + Google Workspace | **Exchange Online** | M365 BP |
| M2 | Suite Office | MS365 + LibreOffice + Google Workspace | **M365 Business Premium** | M365 BP |
| M3 | Videoconferenza | MS Teams + Google Meet | **MS Teams** | M365 BP |
| M4 | Identità | AD Samba4 + Google Auth | **Entra ID P1 + MFA + CA** | M365 BP |
| M5 | File server | NextCloud + Google Drive | **SharePoint Online + OneDrive** | M365 BP |
| M6 | CRM | Sugar CRM + Odoo | **Dynamics 365 Sales Pro** | Dynamics |
| M7 | ERP | Profis + Odoo | **Dynamics 365 BC Essentials** | Dynamics |
| M8 | Timesheet | Kimai + Odoo | **Dynamics 365 BC** | Dynamics |
| M9 | Versioning | GiTea + BitBucket | **Azure DevOps Repos** | Azure |
| M10 | CI/CD | Assente | **Azure DevOps Pipelines** | Azure |
| M11 | Documentazione | Media Wiki (on-prem + GCP) | **Media Wiki su VM Azure B2s** | Azure IaaS |
| M12 | App clienti | Pondus (HW fisico) | **App Service P1v3 + Azure SQL S2** | Azure PaaS |

---

## Riepilogo costi

| Voce | Importo |
|---|---|
| Una tantum migrazione | € 12.000 |
| Ricorrenti primo anno (PAYG) | € 39.524 |
| Ricorrenti anno 2 e 3 (ciascuno) | € 39.524 |
| **Costo totale 3 anni** | **€ 130.572** |
| Risparmio dismissione servizi (3 anni) | ~€ 23.400 |
| **Costo netto 3 anni** | **~€ 107.172** |
| Costi risorse (extra budget, migrazione 55gg + PM 17gg) | € 38.550 |

---

## Budget

| Voce | Valore |
|---|---|
| Budget totale progetto | € 520.000 |
| Spesa già prevista (piano_costi.md) | € 272.950 |
| **Margine disponibile** | **€ 247.050** |
| Costo migrazione primo anno (una tantum + ricorrenti) | ~€ 51.524 |
| **Margine residuo** | **~€ 195.526** |

```
Budget 520.000€
╔══════════════════════════════════════════════════╗
║  Già previsto:   272.950€ (52,5%)               ║
║  ┌──────────────────────────────────────────────╢
║  │ Rete/VPN:     22.650€                        ║
║  │ Sicurezza:    11.500€                        ║
║  │ HPC:         191.600€                        ║
║  │ Pondus:       15.000€                        ║
║  │ Cloud Migr:    5.500€                        ║
║  │ Backup/DR:     7.200€                        ║
║  │ PM:           19.500€                        ║
║  └──────────────────────────────────────────────╢
║                                                  ║
║  Migrazione Microsoft:  51.524€ (9,9%)          ║
║  ┌──────────────────────────────────────────────╢
║  │ Una tantum:        12.000€                   ║
║  │ Ricorrente anno 1: 39.524€                   ║
║  └──────────────────────────────────────────────╢
║                                                  ║
║  Margine residuo:    195.526€ (37,6%)           ║
╚══════════════════════════════════════════════════╝
```

---

## Roadmap

| Fase | Durata | Settimane |
| --- | --- | --- |
| F0 — Foundation | 2 settimane | 1-2 |
| F1 — Posta | 3 settimane | 3-5 |
| F2 — File | 2 settimane | 3-4 |
| F3 — Dynamics 365 | 5 settimane | 4-8 |
| F4 — Azure DevOps | 2 settimane | 5-6 |
| F5 — Media Wiki | 1 settimana | 5 |
| F6 — Test | 2 settimane | 8-9 |
| F7 — Dismissione | 1 settimana | 10 |
| **Durata totale** | **10 settimane** | |

---

## Criteri di successo

| KPI | Target |
|---|---|
| Posta: invio/ricezione | &lt; 5 sec |
| File: upload 100 MB | &lt; 10 sec |
| MFA: policy corretta | Blocco/permesso giusto |
| Dynamics CRM: creazione opportunità | &lt; 3 sec |
| Dynamics BC: creazione fattura | &lt; 5 sec |
| Azure DevOps: clone + push | &lt; 30 sec |
| Media Wiki: navigazione | &lt; 3 sec |
| Migrazione dati | 100%, verificato |
| Downtime posta | 0 (migrazione graduale) |
