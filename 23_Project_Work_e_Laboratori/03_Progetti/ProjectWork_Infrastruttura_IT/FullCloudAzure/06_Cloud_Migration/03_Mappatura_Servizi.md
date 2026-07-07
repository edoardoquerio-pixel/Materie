# 03 — Mappatura Servizi AS-IS → TO-BE

> **Documento:** Mappatura completa di ogni servizio TP Group, stato attuale e target Microsoft/Azure  
> **Data:** Luglio 2026

---

## M1 — Posta / Calendario

| Dato | Valore |
|---|---|
| **Servizio** | Posta elettronica e calendario |
| **Thema (AS-IS)** | Zimbra su VM Linux (self-hosted) |
| **Pro Studio (AS-IS)** | Google Workspace (GMail + Calendar) |
| **Target TO-BE** | **Exchange Online** |
| **Incluso in** | M365 Business Premium |
| **Utenti** | 50 |
| **Migrazione** | IMAP sync o tool migrazione Microsoft (nativo Exchange Online) |
| **Rollback** | Zimbra in sola lettura 7 giorni |

---

## M2 — Suite Office / Produttività

| Dato | Valore |
|---|---|
| **Servizio** | Office, documenti, fogli di calcolo, presentazioni |
| **Thema (AS-IS)** | MS365 + LibreOffice |
| **Pro Studio (AS-IS)** | Google Workspace (Docs, Sheets, Slides) |
| **Target TO-BE** | **M365 Business Premium** (Office 365 desktop + web) |
| **Incluso in** | M365 Business Premium |
| **Utenti** | 50 |
| **Migrazione** | Google Workspace dismesso; migrazione documenti via SharePoint |

---

## M3 — Videoconferenza / IM

| Dato | Valore |
|---|---|
| **Servizio** | Videoconferenza, messaggistica istantanea, riunioni |
| **Thema (AS-IS)** | MS Teams |
| **Pro Studio (AS-IS)** | Google Meet |
| **Target TO-BE** | **MS Teams** (mantenuto) |
| **Incluso in** | M365 Business Premium |
| **Utenti** | 50 |
| **Migrazione** | Google Meet dismesso; migrazione a Teams già in atto |

---

## M4 — Autenticazione / Identity

| Dato | Valore |
|---|---|
| **Servizio** | Directory utenti, autenticazione, MFA |
| **Thema (AS-IS)** | Active Directory su Samba4 (VM Linux) |
| **Pro Studio (AS-IS)** | Google Authenticator (2FA personale, nessuna directory) |
| **Target TO-BE** | **Entra ID P1** + MFA + Conditional Access |
| **Incluso in** | M365 Business Premium |
| **Utenti** | 50 |
| **Strumento sync** | Entra Connect Sync (AD Samba4 → Entra ID) |
| **MFA** | Microsoft Authenticator + Conditional Access policy |
| **Rollback** | Samba4 mantenuto durante sync; disattivabile dopo verifica |

---

## M5 — File Server / Storage

| Dato | Valore |
|---|---|
| **Servizio** | File server, storage documenti, condivisione file |
| **Thema (AS-IS)** | NextCloud su VM Linux (self-hosted) |
| **Pro Studio (AS-IS)** | Google Drive |
| **Target TO-BE** | **SharePoint Online + OneDrive** |
| **Incluso in** | M365 Business Premium |
| **Utenti** | 50 |
| **Storage** | 1 TB/utente (OneDrive) + siti SharePoint dipartimentali |
| **Migrazione** | Microsoft Migration Manager o strumento di terze parti |
| **Rollback** | NextCloud in sola lettura 7 giorni |

---

## M6 — CRM

| Dato | Valore |
|---|---|
| **Servizio** | Customer Relationship Management |
| **Thema (AS-IS)** | Sugar CRM su VM Linux (self-hosted) |
| **Pro Studio (AS-IS)** | Odoo CRM (SaaS) |
| **Target TO-BE** | **Dynamics 365 Sales Professional** |
| **Utenti** | 20 licenze |
| **Moduli** | Pipeline vendita, opportunità, contatti, attività |
| **Migrazione** | Esportazione dati Sugar + Odoo → import Dynamics |
| **Rollback** | Mantenere Sugar + Odoo attivi per 2 settimane |

---

## M7 — ERP / Contabilità

| Dato | Valore |
|---|---|
| **Servizio** | Contabilità generale, fatturazione, ciclo attivo/passivo |
| **Thema (AS-IS)** | Profis su Windows VM (on-prem) |
| **Pro Studio (AS-IS)** | Odoo contabilità (SaaS) |
| **Target TO-BE** | **Dynamics 365 Business Central Essentials** |
| **Utenti** | 10 licenze |
| **Moduli** | Contabilità generale, IVA, clienti/fornitori, fatturazione |
| **Migrazione** | Pianificazione con consulente Dynamics dedicato |
| **Rollback** | Profis in cold storage 30 giorni; Odoo mantenuto 2 settimane |
| **Complessità** | Alta — dati contabili critici |

---

## M8 — Timesheet

| Dato | Valore |
|---|---|
| **Servizio** | Rilevazione ore lavoro, timesheet progetti |
| **Thema (AS-IS)** | Kimai su VM Linux (self-hosted) |
| **Pro Studio (AS-IS)** | Odoo timesheet (SaaS) |
| **Target TO-BE** | **Dynamics 365 Business Central** (incluso in BC) |
| **Utenti** | 10 (stessi di BC) |
| **Migrazione** | Esportazione dati Kimai + Odoo → Dynamics BC |

---

## M9 — Versioning / Sviluppo

| Dato | Valore |
|---|---|
| **Servizio** | Repository Git, versioning codice sorgente |
| **Thema (AS-IS)** | GiTea su VM Linux (self-hosted) |
| **Pro Studio (AS-IS)** | BitBucket (SaaS) |
| **Target TO-BE** | **Azure DevOps Repos** |
| **Utenti** | 50 (pieno accesso) |
| **Migrazione** | `git clone --mirror` + push su Azure Repos (history preservata) |
| **Rollback** | GiTea + BitBucket in sola lettura 7 giorni |

---

## M10 — CI/CD

| Dato | Valore |
|---|---|
| **Servizio** | Integrazione continua, deploy automatico |
| **Thema (AS-IS)** | Assente |
| **Pro Studio (AS-IS)** | Assente |
| **Target TO-BE** | **Azure DevOps Pipelines** |
| **Agent** | Self-hosted agent per accesso rete on-prem (HPC, servizi) |
| **Pipelines** | Build + test + deploy per Pondus e progetti interni |

---

## M11 — Documentazione

| Dato | Valore |
|---|---|
| **Servizio** | Wiki aziendale, documentazione tecnica |
| **Thema (AS-IS)** | Media Wiki su VM Linux (on-prem) |
| **Pro Studio (AS-IS)** | Media Wiki su GCP (IaaS) |
| **Target TO-BE** | **Media Wiki su VM Azure B2s** (West Europe) |
| **Motivazione eccezione** | Personalizzazioni esistenti non facilmente migrabili a SharePoint |
| **SKU** | B2s (2 vCPU, 4 GB RAM), 30 GB managed disk |
| **Migrazione** | Unificare contenuti on-prem + GCP nella nuova VM |
| **Backup** | Azure Backup settimanale + snapshot giornaliero |
| **Rollback** | Puntare DNS all'istanza on-prem originale |

---

## M12 — Applicazione Clienti (Pondus)

| Dato | Valore |
|---|---|
| **Servizio** | Web app ottimizzazione pesi materiali (automotive/aerospace) |
| **Thema (AS-IS)** | C# su MS IIS + MS SQL su HW fisico dedicato (Xeon Silver 4110, 64 GB, 1,2 TB HDD) |
| **Pro Studio (AS-IS)** | — |
| **Target TO-BE** | **Azure App Service (code) P1v3** + **Azure SQL Database S2** |
| **Regione** | West Europe |
| **Runtime** | ASP.NET Core (da verificare compatibilità codice C# legacy) |
| **Deployment** | Azure DevOps Pipelines + staging slot |
| **Autenticazione** | Entra ID (Easy Auth) o JWT per clienti esterni |
| **Percorso** | Separato dal presente piano migrazione servizi |
