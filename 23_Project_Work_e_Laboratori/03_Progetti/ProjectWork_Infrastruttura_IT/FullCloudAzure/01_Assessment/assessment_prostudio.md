# Assessment AS-IS — Pro Studio srl (Full Cloud Azure)

## 1. Profilo Aziendale

Pro Studio srl (2023) — 20 giovani ingegneri progettisti settore aerospace. Sede Torino in affitto (condominio uffici) con facilities incluse. Modello completamente **cloud-native**, nessuna infrastruttura on-premise.

## 2. Servizi AS-IS (Pro Studio)

| Servizio | Piattaforma AS-IS | Target Full Cloud Azure |
|---|---|---|
| Posta/Calendario | Google Workspace (GMail + Calendar) | **Exchange Online** |
| Suite office | Google Workspace (Docs, Sheets, Slides) | **M365 Business Premium** |
| Videoconferenza | Google Meet | **MS Teams** |
| Identità | Google Authenticator (2FA, nessuna directory) | **Entra ID P1 + MFA** |
| File storage | Google Drive | **SharePoint Online + OneDrive** |
| CRM | Odoo CRM (SaaS) | **Dynamics 365 Sales Pro** |
| Contabilità | Odoo (SaaS) | **Dynamics 365 BC Essentials** |
| Timesheet | Odoo Timesheet (SaaS) | **Dynamics 365 BC** |
| Versioning | BitBucket (SaaS) | **Azure DevOps Repos** |
| Documentazione | MediaWiki su GCP (IaaS) | **MediaWiki su VM Azure B2s** |

## 3. Infrastruttura IT

| Componente | Stato |
|---|---|
| Server on-premise | Nessuno |
| Virtualizzazione | N/A |
| Firewall hardware | N/A (affidato a connettività condominiale) |
| Storage locale | N/A (tutti i dati su cloud) |
| Backup | GCP Cloud Storage (single-region) |

## 4. Stima Costi Annui Pro Studio

| Servizio | Costo/anno stimato |
|---|---|
| Google Workspace (20 utenti × €12/mese) | ~€ 2.880 |
| BitBucket (20 utenti × $3/mese) | ~€ 660 |
| Odoo Enterprise (20 utenti × €24,90/mese) | ~€ 5.976 |
| MediaWiki su GCP (VM e2-small) | ~€ 300 |
| Backup GCP storage | ~€ 180 |
| **Totale annuo stimato** | **~€ 9.996** |

## 5. Impatto migrazione Full Cloud Azure

| Elemento | Azione |
|---|---|
| Google Workspace | Dismissione completa — migrazione a M365 |
| Google Drive | Dati migrati a SharePoint/OneDrive |
| BitBucket | Repos migrati ad Azure DevOps |
| Odoo | Dati esportati verso Dynamics 365 |
| VM MediaWiki su GCP | Migrata a VM Azure B2s |
| Account Google | Mantenuti solo per utenti che necessitano accesso storico |
