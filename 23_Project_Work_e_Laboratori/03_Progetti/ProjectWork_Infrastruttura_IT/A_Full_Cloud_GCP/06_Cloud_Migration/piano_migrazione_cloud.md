# Piano Migrazione Cloud — Variante Full Cloud GCP

## REQUISITI

- Migrare TUTTI i servizi Thema Consulting da on-premise a Google Cloud
- Integrare servizi cloud di Pro Studio (già su GCP/Workspace)
- Tempo totale: 12 settimane attive
- Shutdown massimo: 7 giorni consecutivi (cut-over)
- Zero perdita dati durante la migrazione
- Coesistenza on-premise + cloud durante la migrazione graduale

## Mappatura Servizi

| Servizio | Stato Attuale (Thema) | Stato Attuale (Pro Studio) | Target GCP | Priorità |
|---|---|---|---|---|
| **Posta/Calendario** | Zimbra (VM Linux) | Google Workspace | Google Workspace (unificato) | Alta |
| **Directory/Identità** | Samba4 AD (VM Linux) | Google Workspace | Google Cloud Directory Sync + Workspace | Alta |
| **File server** | NextCloud (VM Linux) | Google Drive | Google Drive + Cloud Storage | Alta |
| **Sviluppo/Versioning** | GiTea (VM Linux) | BitBucket (SaaS) | BitBucket (unificato) | Media |
| **Contabilità** | Profis (Server Windows) | Odoo (SaaS) | Odoo (unificato) | Media |
| **CRM** | SugarCRM (VM Linux) | Odoo (SaaS) | Odoo (unificato) | Media |
| **Time Sheet** | Kimai (VM Linux) | Odoo (SaaS) | Odoo (unificato) | Bassa |
| **Documentazione** | MediaWiki (VM Linux) | MediaWiki (VM GCP) | MediaWiki su GCP o migrazione a Cloud Wiki | Bassa |
| **HPC** | 8 nodi on-premise | N/A (su sistemi clienti) | Istanze C2/H3 su GCP | Alta |
| **Pondus** | C# IIS + MS SQL on-prem | N/A | Cloud Run + Cloud SQL | Alta |
| **Backup** | NAS QNAP 32 TB | GCP Cloud Storage | Cloud Storage (unificato) | Alta |

## Strategia di migrazione

### Approccio: Graduale con finestra cut-over

Fasi:
1. **Migranti early** (Settimane 1-4): servizi cloud-native, dati non critici, test con utenti pilota
2. **Migranti core** (Settimane 5-8): servizi collaborativi, identità, file server
3. **Migranti critici** (Settimane 9-10): HPC, Pondus, backup (richiedono cut-over pianificato)
4. **Cut-over finale** (Settimana 11): shutdown 7 giorni, disconnessione finale on-premise
5. **Post-migrazione** (Settimana 12+): stabilizzazione, verifica, dismissione HW on-premise

### Ordine di migrazione

```mermaid
gantt
    title Ordine Migrazione GCP
    dateFormat YYYY-MM-DD
    section Collaborazione
        Migrazione posta (Zimbra→Workspace)       :c1, 7d
        Migrazione identità (Samba4→GCDS)          :c2, after c1, 5d
        Migrazione file (NextCloud→Drive)          :c3, after c1, 5d
    section Gestionale
        Migrazione contabilità (Profis→Odoo)       :g1, after c3, 7d
        Migrazione CRM (SugarCRM→Odoo)             :g2, after c3, 5d
        Migrazione time sheet (Kimai→Odoo)         :g3, after c3, 3d
    section Tecnico
        Migrazione Git (GiTea→BitBucket)           :t1, 3d
        Migrazione Wiki (MediaWiki→GCP)            :t2, 3d
    section Cut-over
        Migrazione HPC (on-prem→GCP)               :h1, 5d
        Migrazione Pondus (IIS→Cloud Run)          :p1, after h1, 5d
        Cut-over finale                            :co, after p1, 3d
```

### Criteri di cut-over

- **Shutdown finestra**: max 7 giorni consecutivi
- **Attività nella finestra**: spegnimento VM on-premise, verifica DNS, test integrazione, rollback pronti
- **Rollback**: snapshot GCP pre-cut-over, riconnessione on-premise se fallimento critico
- **Go/no-go**: decisione 24 ore prima basata su test di integrazione

## Integrazione Identità

### Scenario target: Hybrid Identity

```
[Samba4 AD] ---- GCDS (Google Cloud Directory Sync) ---- [Google Workspace]
   Thema                                                      Pro Studio
     |                                                            |
[Utenti on-prem]                                          [Utenti cloud]
     |                                                            |
     +---------------- Google Workspace (unificato) ----------------+
                          |                       |
                    [Autenticazione]         [App Password per legacy]
```

### Passaggi

1. Configurare GCDS per sincronizzare Samba4 AD → Google Workspace
2. Mantenere Samba4 AD come source of truth per utenti Thema
3. Unificare domini: tema-consulting.it + pro-studio.it → tp-group.it
4. Google Authenticator come MFA unificato per tutti gli utenti
5. Dismissione Samba4 AD solo dopo migrazione completa (fase post)

## Rischi e Mitigazioni

| Rischio | Probabilità | Impatto | Mitigazione |
|---|---|---|---|
| Volume dati supera stime | Media | Alto | Assessment preliminare con tool di discovery GCP |
| Downtime non pianificato durante migrazione DB | Bassa | Alto | CDC (Change Data Capture) per migrazione zero-downtime |
| Incompatibilità applicazioni legacy con cloud | Media | Alto | Test di compatibilità preventivi su ambiente staging GCP |
| Resistenza utenti al cambiamento (Zimbra→Workspace) | Alta | Medio | Formazione anticipata, periodo di coesistenza |
| Tempi consegna HW per connettività sede | Media | Medio | Ordine anticipato (lead time 8-16 settimane) |
| Coesistenza Samba4 AD ↔ Workspace problematica | Media | Alto | Test pilota con gruppo ristretto di utenti |

## Costi migrazione

| Voce | Costo stimato |
|---|---|
| Assessment e discovery | Incluso in budget manodopera |
| Formazione utenti (2 sessioni) | Incluso in budget manodopera |
| Google Workspace (50 utenti, Business Standard) | ~€600/mese (~€7.200/anno) |
| GCDS (gratuito) | €0 |
| BitBucket (50 utenti, Standard) | ~$150/mese (~$1.800/anno) |
| Odoo Enterprise (50 utenti) | ~€1.245/mese (~€14.940/anno) |
| Servizi GCP (HPC, Pondus, backup) | Vedi documenti specifici |
| **Totale costi ricorrenti** | **~€25.000/anno** |

*Nota: la migrazione da Profis a Odoo richiede export dati contabili e riconciliazione manuale — costo una tantum stimato 5-8 gg/uomo.*
