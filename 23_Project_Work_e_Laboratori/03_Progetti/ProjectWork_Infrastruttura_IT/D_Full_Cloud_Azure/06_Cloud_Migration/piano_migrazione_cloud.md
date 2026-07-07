# Piano Migrazione Cloud — Variante Full Cloud Azure

## REQUISITI

- Migrare TUTTI i servizi Thema Consulting da on-premise a Microsoft Azure / M365
- Unificare i servizi cloud di Pro Studio (Google Workspace → M365, GCP → Azure)
- Tempo totale: 12 settimane attive
- Shutdown massimo: 7 giorni consecutivi (cut-over)
- Zero perdita dati durante la migrazione
- Coesistenza on-premise + cloud durante la migrazione graduale

## Mappatura Servizi

| Servizio | Stato Attuale (Thema) | Stato Attuale (Pro Studio) | Target Azure | Priorità |
|---|---|---|---|---|
| **Posta/Calendario** | Zimbra (VM Linux) | Google Workspace | **M365 Exchange** (unificato) — M365 già presente! | Alta |
| **Directory/Identità** | Samba4 AD (VM Linux) | Google Workspace | **Microsoft Entra ID Connect** (sync da Samba4) | Alta |
| **File server** | NextCloud (VM Linux) | Google Drive | **SharePoint Online / OneDrive for Business** | Alta |
| **Sviluppo/Versioning** | GiTea (VM Linux) | BitBucket (SaaS) | **Azure DevOps** (Basic: ~€6/user/mese × 5 utenti = ~€360/anno) | Media |
| **Contabilità** | Profis (Server Windows) | Odoo (SaaS) | **Odoo** (unificato) — migrazione dati contabili (~€3.000 una tantum) | Media |
| **CRM** | SugarCRM (VM Linux) | Odoo (SaaS) | **Odoo** (unificato) | Media |
| **Time Sheet** | Kimai (VM Linux) | Odoo (SaaS) | **Odoo** (unificato) | Bassa |
| **Documentazione** | MediaWiki (VM Linux) | MediaWiki (VM GCP) | **SharePoint** o **Azure App Service** | Bassa |
| **HPC** | 8 nodi on-prem (InfiniBand, Linux) | N/A | **Hybrid: 8 on-prem + Azure HBv4 burst** (CycleCloud, 8 nodi SPOT, Lustre condiviso) | Alta |
| **Pondus** | C# IIS + MS SQL on-prem | N/A | **Azure Container Apps + Azure SQL** | Alta |
| **Backup** | NAS QNAP 32 TB | GCP Cloud Storage | **Azure Backup + Blob Storage GRS** | Alta |

> **Vantaggio chiave**: M365 è già attivo per Thema (30 licenze). Non serve migrare la posta Zimbra a Workspace come su GCP — si estende semplicemente M365 a 50 utenti. Pro Studio (20 utenti su Google Workspace) va migrato a M365 una tantum.
>
> **Aggiornamento M365**: Thema ha attualmente 30 licenze **Business Basic** (~€6/utente/mese). Per i requisiti di sicurezza ISO 27001 (MFA, DLP, Information Protection) è necessario l'upgrade a **Business Premium** (~€22/utente/mese). Pro Studio (20 utenti) attiverà direttamente Business Premium.
> - Costo M365 totale: 50 × €22 × 12 = **€13.200/anno**
> - Delta upgrade 30 utenti Basic→Premium: €16 × 30 × 12 = **€5.760/anno**

## Strategia di migrazione

### Approccio: Graduale con finestra cut-over

Fasi:
1. **Migranti early** (Settimane 1-4): servizi cloud-native, dati non critici, test con utenti pilota
2. **Migranti core** (Settimane 5-8): servizi collaborativi (M365), identità (Entra ID), file server (SharePoint)
3. **Migranti critici** (Settimane 9-10): HPC burst (CycleCloud + HBv4 SPOT + Lustre), Pondus (Container Apps + Azure SQL), backup (Azure Backup)
4. **Cut-over finale** (Settimana 11): shutdown 7 giorni, disconnessione finale on-premise
5. **Post-migrazione** (Settimana 12+): stabilizzazione, verifica, dismissione HW on-premise

### Ordine di migrazione

```mermaid
gantt
    title Ordine Migrazione Azure
    dateFormat YYYY-MM-DD
    section Collaborazione
        Estensione M365 (Zimbra→Exchange)      :c1, 7d
        Migrazione identità (Samba4→Entra ID)    :c2, after c1, 5d
        Migrazione file (NextCloud→SharePoint)   :c3, after c1, 5d
        Migrazione Workspace→M365 (Pro Studio)   :c4, after c1, 5d
    section Gestionale
        Migrazione contabilità (Profis→Odoo)     :g1, after c3, 7d
        Verifica quadratura contabile            :g1a, after g1, 5d
        Migrazione CRM (SugarCRM→Odoo)           :g2, after c3, 5d
        Migrazione time sheet (Kimai→Odoo)       :g3, after c3, 3d
    section Tecnico
        Migrazione Git (GiTea→Azure DevOps)      :t1, 3d
        Migrazione Wiki (MediaWiki→SharePoint)   :t2, 3d
    section Cut-over
        Setup HPC burst (CycleCloud+HBv4+Lustre)  :h1, 5d
        Migrazione Pondus (IIS→AKS Windows)      :p1, after h1, 5d
        Cut-over finale                          :co, after p1, 3d
```

### Criteri di cut-over

- **Shutdown finestra**: max 7 giorni consecutivi
- **Attività nella finestra**: spegnimento VM on-premise, verifica DNS, test integrazione, rollback pronti
- **Rollback**: snapshot Azure pre-cut-over, riconnessione on-premise se fallimento critico
- **Go/no-go**: decisione 24 ore prima basata su test di integrazione

## Migrazione Profis → Odoo

Profis (Server Windows, Thema) è il sistema contabile attuale. Pro Studio utilizza già Odoo (SaaS). La migrazione unifica la contabilità su Odoo.

### Fasi migrazione

| Fase | Durata | Attività | Note |
|---|---|---|---|
| 1. Analisi dati contabili | 1 settimana | Inventario dati Profis (clienti, fornitori, conti, prima nota), mappatura su schema Odoo | Identificare eventuali personalizzazioni Profis |
| 2. Migrazione dati | 2 settimane | Export dati da Profis, trasformazione ETL, import su Odoo | Validazione campioni intermedi |
| 3. Verifica quadratura | 1 settimana | Bilancio di verifica, riconciliazione saldi, controllo partite aperte | Con responsabile amministrativo |
| **Totale** | **4 settimane** | | |

### Costi migrazione

| Voce | Costo |
|---|---|
| Giorni sistemista (6 gg × €500/gg) | €3.000 |
| Piattaforma Odoo (già attiva per Pro Studio) | €0 (costi esistenti) |
| **Totale migrazione Profis→Odoo** | **€3.000 una tantum** |

> La migrazione Profis→Odoo è pianificata nella finestra "Migranti core" (settimane 5-8), parallelamente alla migrazione CRM (SugarCRM→Odoo).

## Integrazione Identità

### Scenario target: Microsoft Entra ID (Hybrid Identity)

```
[Samba4 AD] ---- Microsoft Entra ID Connect ---- [Microsoft Entra ID]
   Thema                                           (Tenant TP Group)
     |                                                    |
[Utenti on-prem]                                  [Utenti cloud M365]
     |                                                    |
     +---------------- Entra ID (unificato) ----------------+
                          |
                    [Azure RBAC]
                    [Azure SQL Auth]
                    [Azure DevOps Auth]
```

Entra ID Connect sincronizza Samba4 AD con Microsoft Entra ID:
- **Password hash sync**: autenticazione utenti su M365 con credenziali AD
- **Password writeback**: cambio password da cloud → on-prem
- **Group sync**: gruppi di sicurezza AD sincronizzati su Azure per RBAC

## Costi migrazione

| Voce                                                  | Costo stimato                 | Note |
|---|---|---|---|
| Azure Data Box                                        | ~€300                         | Trasferimento dati massivi (se >5 TB) |
| Azure DMS                                             | Gratuito                      | Database Migration Service per SQL |
| Azure Migrate                                         | Gratuito                      | Assessment e migrazione VM            |
| Migrazione Profis→Odoo                                | ~€3.000                       | 6 gg sistemista (€500/gg) |
| Azure DevOps Basic (5 utenti × ~€6/mese × 12 mesi)    | ~€360/anno                    | Sostituzione GiTea |
| Giorni/uomo sistemista                                | 40gg × €500 = €20.000         | Incluso in extra manodopera |
| **Totale migrazione**                                 | **~€23.660**                  |                                         |

*I costi di migrazione sono inclusi nella voce "Extra manodopera" del budget complessivo.*
