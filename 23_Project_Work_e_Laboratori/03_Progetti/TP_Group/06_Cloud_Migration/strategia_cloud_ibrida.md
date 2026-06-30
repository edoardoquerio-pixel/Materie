# Strategia Cloud Ibrida TP Group

> **NOTA:** Le decisioni di convergenza sono state aggiornate in base all'intervista cliente del 18/06/2026. Il cliente ha scelto di mantenere l'ecosistema Thema (MS365, Zimbra, NextCloud, GiTea) e di adottare Odoo per CRM/TimeSheet.

## Visione architetturale

TP Group adotta un modello **ibrido** dove l'infrastruttura on-premise (Thema) viene integrata con i servizi cloud esistenti (Pro Studio) tramite tunnel VPN IPsec dedicato.

```mermaid
graph TB
    subgraph ONPREM["On-Premise — Sede Torino"]
        AD[AD Samba4<br/>Autenticazione]
        ZIMBRA[Zimbra<br/>Posta]
        PROFIS[Profis<br/>Contabilità]
        PONDUS[Pondus<br/>App clienti]
        HPC[Cluster HPC]
        NEXTCLOUD[NextCloud<br/>File server]
        SUGAR[Sugar CRM<br/>CRM]
        KIMAI[Kimai<br/>Time Sheet]
        MEDIAWIKI[Media Wiki<br/>Documentazione]
    end

    subgraph CLOUD["Cloud — GCP / SaaS"]
        GW[Cloud VPN Gateway]
        MW[Media Wiki<br/>(migrato da GCP)]
        GC_BACKUP[Backup<br/>delocalizzato]
    end

    subgraph SAAS["SaaS esterni"]
        ODOO[Odoo<br/>Contabilità/CRM/TS]
        MS365[MS365<br/>Office]
        BITBUCKET[Bit Bucket<br/>(da sostituire)]
        MEET[Google Meet<br/>Videoconferenza]
    end

    AD ---|LDAP sync| GW
    GW ---|IPsec VPN| ONPREM
    ONPREM --- SAAS
```

## Mappatura servizi: decisioni di convergenza

| Servizio | Thema | Pro Studio | Decisione TO-BE | Motivazione |
| --- | --- | --- | --- | --- |
| **Posta / Calendario** | Zimbra | Google Workspace | Migrare a **Zimbra** (unificata) | Cliente sceglie ecosistema Thema. Google Workspace dismesso. |
| **Office** | MS365 / LibreOffice | Google Workspace | **MS365 per tutti 50 utenti** | Cliente sceglie MS365. Google Workspace dismesso. |
| **Videoconferenza** | MS Teams | Google Meet | Mantenere **MS Teams** | Coerenza con MS365. |
| **Autenticazione** | AD Samba4 | Google authenticator | **AD Samba4 + MFA** con bridge verso Workspace | AD è il punto di controllo centrale; MFA via FortiToken |
| **File server** | NextCloud | Google Drive | Mantenere **NextCloud** (migrare dati Drive) | Dati sensibili on-premise, controllo GDPR |
| **Sviluppo versioning** | GiTea | Bit Bucket | Unificare su **GiTea** | Self-hosted, nessun costo SaaS, controllo completo |
| **Contabilità** | Profis | Odoo | Mantenere **Profis** | Dati contabili on-premise, compliance |
| **CRM** | Sugar CRM | Odoo | **Odoo** unifica CRM + Time Sheet | SaaS, minore gestione interna, già in uso da Pro Studio |
| **Time Sheet** | Kimai | Odoo | **Odoo** unifica CRM + Time Sheet | SaaS, già in uso |
| **Documentazione** | Media Wiki | Media Wiki | **Media Wiki unico** su VM on-premise | Centralizzare, migrare da GCP |
| **Backup** | NAS locale | GCP | **Ibrido**: NAS locale + GCP off-site | Delocalizzazione ISO 27001 |

## Schema connettività ibrida

```
Sede Torino                    GCP
┌──────────────┐         ┌──────────────┐
│  Fortigate   │◄─IPsec──│  Cloud VPN   │
│  FG-100F     │────────►│  Gateway     │
│  10.10.0.0/16│         │  10.30.0.0/16│
└──────┬───────┘         └──────┬───────┘
       │                        │
       ▼                        ▼
  NextCloud                Media Wiki (fino a migrazione)
  Profis                   Backup storage
  GiTea
  Pondus
```

## Gestione identità (IAM)

**Modello TO-BE:** AD Samba4 come Identity Provider primario

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  AD Samba4  │────►│  Google      │◄────│  FortiAuth   │
│  (master)   │     │  Cloud       │     │  + MFA       │
│             │     │  Directory   │     │              │
│  utenti,    │     │  Sync (GCDS) │     │  OTP push    │
│  gruppi,    │     │              │     │  app         │
│  policy     │     │  SSO SAML    │     │              │
└─────────────┘     └──────────────┘     └──────────────┘
                          │
                          ▼
                   ┌──────────────┐
                   │  Google      │
                   │  Workspace   │
                   │  (posta,     │
                   │  calendar,   │
                   │  meet)       │
                   └──────────────┘
```

**Componenti:**
- **AD Samba4**: fonte autoritativa per tutti gli utenti TP Group (50)
- **Google Cloud Directory Sync (GCDS)**: sincronizza AD → Google Workspace
- **SAML/SSO**: Google Workspace federato con AD per autenticazione
- **MFA**: FortiToken (push) su VPN + accesso a risorse sensibili

## Note dall'intervista cliente

- **Referente:** Solution Architect
- **Priorità:** Produttività, business continuity
- **Smart working:** Minimo 10 dipendenti/giorno in remoto via VPN
- **Finestra manutenzione:** Massimo 7 giorni
- **Ciclo di vita:** 3 anni
- **Budget risorse:** €500/gg sistemista e €650/gg PM sono EXTRA budget (per IT interno, coprono i 3 anni successivi)
