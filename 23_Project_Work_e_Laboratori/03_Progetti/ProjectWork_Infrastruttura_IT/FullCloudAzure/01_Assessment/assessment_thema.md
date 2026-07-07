# Assessment AS-IS — Thema Consulting (Full Cloud Azure)

## 1. Profilo Aziendale

Thema Consulting srl, fondata negli anni '90, opera nella progettazione strutturale in ambito automotive con simulazioni crash test e analisi FEM. La sede è di proprietà in centro Torino (edificio storico). Personale: **30 persone** (dipendenti + collaboratori), con possibilità di ospitare fino a **40 postazioni**.

## 2. Infrastruttura Datacenter

| Elemento | Stato AS-IS | Impatto Full Cloud Azure |
|---|---|---|
| Armadi rack | 2 rack saturi — nessuna espansione possibile | ✅ Si dismettono tutti i servizi (escluso HPC) |
| Virtualizzazione | 2 host VMWare | ✅ Dismissione dopo migrazione servizi |
| Storage SAN | 1 SAN NetApp 24 TB on-prem | ✅ Dismissione — dati su Azure/SharePoint |
| UPS | Autonomia 10 minuti, nessun generatore | ✅ Rischio eliminato con cloud |
| Condizionamento | Al limite del carico termico | ✅ Rischio eliminato con cloud |

## 3. Servizi AS-IS (Thema)

| Servizio | Piattaforma | Target Full Cloud Azure |
|---|---|---|
| Posta | Zimbra (VM Linux) | **Exchange Online** |
| Suite office | MS365 + LibreOffice | **M365 Business Premium** |
| Videoconferenza | MS Teams | **MS Teams** (mantenuto) |
| Identità | AD Samba4 (VM Linux) | **Entra ID P1** (sync) |
| File server | NextCloud (VM Linux) | **SharePoint Online + OneDrive** |
| CRM | SugarCRM (VM Linux) | **Dynamics 365 Sales Pro** |
| Contabilità | Profis (Windows VM) | **Dynamics 365 BC Essentials** |
| Timesheet | Kimai (VM Linux) | **Dynamics 365 BC** |
| Versioning | GiTea (VM Linux) | **Azure DevOps Repos** |
| Documentazione | MediaWiki (VM Linux) | **MediaWiki su VM Azure B2s** |
| App clienti | Pondus (HW fisico, C# + MS SQL) | **Azure App Service + Azure SQL** |

## 4. Cluster HPC

| Elemento | Valore |
|---|---|
| Nodi correnti | 8 nodi fisici on-prem con InfiniBand |
| Nuovi nodi | 8 nodi Azure CycleCloud (HB176-48rs) |
| Connettività | VPN Sede → Azure per cluster ibrido |

## 5. Stima Costi Annui Thema (on-prem)

| Voce | Costo/anno stimato |
|---|---|
| Elettricità datacenter | € 6.000 – 8.000 |
| Manutenzione SAN NetApp | € 3.500 – 5.000 |
| Canone VMWare | € 2.000 – 3.000 |
| Canone FortiGate FG-60F | € 600 – 900 |
| Manutenzione NAS QNAP | € 500 – 800 |
| Licenze MS SQL Server | € 1.500 – 2.500 |
| Manutenzione HW Pondus | € 500 – 800 |
| **Totale annuo stimato** | **~€ 16.500** |
