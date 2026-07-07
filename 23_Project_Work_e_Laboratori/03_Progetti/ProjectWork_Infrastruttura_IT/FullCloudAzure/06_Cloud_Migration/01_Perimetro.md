# 01 — Perimetro del Progetto

> **Documento:** Perimetro della migrazione TP Group verso Full Cloud Azure + Ecosistema Microsoft  
> **Data:** Luglio 2026  
> **Regione Azure:** West Europe

---

## Incluso

| # | Area | Servizio AS-IS (Thema) | Servizio AS-IS (Pro Studio) | Target TO-BE |
| --- | --- | --- | --- | --- |
| M1 | Posta e calendario | Zimbra (VM Linux) | Google Workspace | **Exchange Online** |
| M2 | Suite office | MS365 + LibreOffice | Google Workspace | **M365 Business Premium** |
| M3 | Videoconferenza / IM | MS Teams | Google Meet | **MS Teams** |
| M4 | Identità e accessi | AD Samba4 (VM Linux) | Google Authenticator | **Entra ID P1 + MFA + Conditional Access** |
| M5 | File server e storage | NextCloud (VM Linux) | Google Drive | **SharePoint Online + OneDrive** |
| M6 | CRM | Sugar CRM (VM Linux) | Odoo (SaaS) | **Dynamics 365 Sales Professional** |
| M7 | ERP / Contabilità | Profis (Windows VM) | Odoo (SaaS) | **Dynamics 365 Business Central Essentials** |
| M8 | Timesheet | Kimai (VM Linux) | Odoo (SaaS) | **Dynamics 365 Business Central** |
| M9 | Versioning / Sviluppo | GiTea (self-hosted) | BitBucket (SaaS) | **Azure DevOps Repos** |
| M10 | CI/CD | Assente | Assente | **Azure DevOps Pipelines** |
| M11 | Documentazione | Media Wiki (on-prem) | Media Wiki (GCP) | **Media Wiki su VM Azure B2s** |
| M12 | App clienti | Pondus (HW fisico, C# + MS SQL) | — | **Azure App Service (code) + Azure SQL Database** |

---

## Escluso

| Servizio | Motivazione |
|---|---|
| **Cluster HPC** (8 nodi on-prem) | Percorso separato: mantiene on-prem + Azure CycleCloud (HB176-96rs v4 burst) per overflow |
| **Infrastruttura rete on-prem** (Fortigate, switch, cablaggio) | Gestita dal piano Rete/VPN (area 02) |
| **Potenziamento UPS e condizionamento** | Gestito dal piano sicurezza sede (area 03) |
| **Laptop e postazioni utente** | Di proprietà TP Group, fuori fornitura |
| **Arredi e infrastruttura fisica** | Rack, cablaggio edificio, UPS condizionamento |

---

## Vincoli

| Vincolo | Valore |
|---|---|
| Budget totale progetto | € 520.000 + IVA |
| Finestra manutenzione max | 7 giorni consecutivi |
| Smart working strutturale | Minimo 10 dipendenti/giorno in remoto |
| Ciclo di vita | 3 anni |
| Costi risorse (sistemista €500/gg, PM €650/gg) | Extra budget |
| Conformità | ISO/IEC 27001 (business continuity, DR, sicurezza accessi) |

---

## Criteri di successo

| KPI | Target |
|---|---|
| Posta: invio/ricezione interno+esterno | &lt; 5 secondi |
| File: upload/download SharePoint/OneDrive 100 MB | &lt; 10 secondi |
| MFA: accesso condizionale Entra ID | Blocco/permesso corretto per policy |
| Dynamics: creazione opportunità CRM | &lt; 3 secondi |
| Dynamics: creazione fattura BC | &lt; 5 secondi |
| Azure DevOps: clone + push repo | &lt; 30 secondi |
| Media Wiki: lettura/scrittura articoli | &lt; 3 secondi |
| Downtime migrazione posta | 0 (migrazione graduale per utente) |
| Dati migrati (posta, file, DB) | 100%, verificato con checksum |
