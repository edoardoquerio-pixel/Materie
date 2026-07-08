# 02 — Architettura TO-BE

> **Documento:** Architettura target Full Cloud Azure + Ecosistema Microsoft per TP Group  
> **Data:** Luglio 2026  
> **Regione Azure:** West Europe

---

## Schema architetturale

```mermaid
graph TB
    subgraph M365["M365 Business Premium — 50 utenti"]
        EXO[Exchange Online<br/>Posta + Calendario]
        TEAMS[MS Teams<br/>Videoconferenza + IM]
        SPO[SharePoint Online<br/>+ OneDrive<br/>File server]
        ENTRA[Entra ID P1<br/>MFA + Conditional Access]
        DEF[Defender for Office 365]
    end

    subgraph AZURE["Azure West Europe"]
        subgraph PAAS["PaaS"]
            ASP[App Service P1v3<br/>Pondus Web App]
            SQL[Azure SQL DB S2<br/>Pondus Database]
            DEVOP[Azure DevOps<br/>Repos + Pipelines]
        end
        subgraph IaaS["IaaS"]
            VM[VM B2s<br/>Media Wiki<br/>Documentazione]
        end
    end

    subgraph D365["Dynamics 365"]
        SALES[Dynamics 365<br/>Sales Professional<br/>20 utenti]
        BC[Dynamics 365<br/>Business Central<br/>10 utenti<br/>ERP + Timesheet]
    end

    CLIENTI[Clienti Pondus] --> ASP
    UTENTI[Utenti TP Group<br/>50 persone] --> EXO
    UTENTI --> TEAMS
    UTENTI --> SPO
    UTENTI --> D365
    UTENTI --> DEVOP
    ADMIN[Amministratori] --> ENTRA
    ENTRA --> EXO
    ENTRA --> SPO
    ENTRA --> D365
    ENTRA --> DEVOP
    ASP --> SQL
```

---

## Layer architetturale

### Layer 1 — Identità e Accesso (Entra ID)

| Componente | Descrizione |
|---|---|
| **Entra ID P1** | Identity provider unico per tutti i 50 utenti |
| **Entra Connect Sync** | Sincronizzazione da AD Samba4 esistente verso Entra ID |
| **MFA** | Conditional Access con MFA su tutte le app critiche |
| **Conditional Access** | Policy per location, device compliance, risk |

### Layer 2 — Produttività (M365 Business Premium)

| Componente | Descrizione |
|---|---|
| **Exchange Online** | Posta, calendario, contatti, 50 GB per utente |
| **SharePoint Online** | Siti dipartimentali e di progetto |
| **OneDrive** | Storage personale, 1 TB per utente |
| **MS Teams** | Chat, videoconferenza, canali per progetto |
| **Defender for Office 365** | Protezione phishing, malware, attachment sicuri |

### Layer 3 — Applicazioni Line of Business (Dynamics 365)

| Componente | Utenti | Descrizione |
|---|---|---|
| **Dynamics 365 Sales Professional** | 20 | CRM: pipeline vendita, opportunità, contatti |
| **Dynamics 365 Business Central Essentials** | 10 | ERP: contabilità, fatturazione, ciclo attivo/passivo |
| **Dynamics 365 Business Central** (incluso) | 10 | Timesheet, gestione progetti, integrazione ERP |

### Layer 4 — Applicazione Clienti (Azure PaaS)

| Componente | SKU | Descrizione |
|---|---|---|
| **Azure App Service P1v3** | Linux, 2 vCPU, 8 GB RAM | Pondus Web App (C#) |
| **Azure SQL Database S2** | 50 DTU, 250 GB storage | Pondus Database |

### Layer 5 — DevOps (Azure)

| Componente | Descrizione |
|---|---|
| **Azure DevOps Repos** | Repository Git centralizzato (da GiTea + BitBucket) |
| **Azure DevOps Pipelines** | CI/CD per Pondus e progetti interni |
| **Azure Artifacts** | Pacchetti NuGet/npm privati (se necessario) |

### Layer 6 — Documentazione (Azure IaaS)

| Componente | SKU | Descrizione |
|---|---|---|
| **VM B2s** | West Europe, 2 vCPU, 4 GB RAM | Media Wiki unificato, 30 GB managed disk |

---

## VNet e subnet

Rete virtuale Azure per servizi IaaS e integrazione VNet con App Service:

| Risorsa | Valore |
|---|---|
| Resource Group | `rg-tpgroup-migration-westeu` |
| VNet | `vnet-tpgroup-westeu` — 10.30.0.0/16 |
| Subnet Media Wiki | `snet-mediawiki-westeu` — 10.30.1.0/24 |
| Subnet App Service VNet integration | `snet-appsvc-westeu` — 10.30.2.0/24 |
| Subnet VPN Gateway | `snet-gateway-westeu` — 10.30.254.0/24 |
| VPN Gateway | VpnGw1AZ, active-standby |
