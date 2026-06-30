# Architettura Backup e DR — Variante Full Cloud Azure

## REQUISITI

- 3-2-1 rule: 3 copie, 2 media differenti, 1 copia off-site
- RPO (Recovery Point Objective): ≤4 ore per servizi critici
- RTO (Recovery Time Objective): ≤8 ore per servizi critici, ≤24 ore per servizi non critici
- Delocalizzazione: backup in regione Azure secondaria (North Europe)
- Business continuity: failover automatico cross-regione
- Copertura: VM, database, file storage, applicazioni (Pondus), HPC
- Fruibilità servizi clienti anche in caso di disastro

## SOLUZIONE

### Strategia generale

```
[Produzione West Europe]      [Backup/Ripristino North Europe]
         |                                 |
    [Servizi Azure]                   [Azure Blob Storage GRS]
         |                                 |
    [Backup automatici]            [Copia Geo-Redondante]
         |                                 |
    [Snapshot / Dump]              [Replica asincrona cross-regione]
```

### Backup per servizio

| Servizio | Metodo | Frequenza | Retention | Destinazione |
|---|---|---|---|---|
| **Azure SQL Managed Instance** | Backup automatico PITR | Giornaliero + point-in-time (5 min) | 35 giorni | GRS (Blob storage) |
| **Azure Container Apps (Pondus)** | Immagine container in ACR | Ad ogni deploy | Ultime 10 versioni | ZRS (replica intra-regione) |
| **VM HBv4 (HPC)** | Azure Backup (snapshot VSS) | Ogni 4 ore | 14 giorni | GRS (Recovery Services Vault) |
| **Azure Blob Storage** | Soft delete + versioning + lifecycle | Continuo (versioning) | 90 giorni hot, poi cool, poi archive | GRS nativo |
| **Azure Files** | Azure Backup snapshot | Giornaliero | 30 giorni | GRS |
| **Microsoft 365** | Microsoft 365 Backup | Continuo | Retention policy legale | Nativo Microsoft |
| **Azure DevOps / BitBucket** | Git repository backup | Giornaliero | 30 giorni | Azure Blob Storage |

### Disaster Recovery

#### Scenario: Disastro regione West Europe

| Fase | Azione | Tempo stimato |
|---|---|---|
| **1. Rilevamento** | Azure Monitor + Traffic Manager endpoint monitoring | 1 minuto |
| **2. Failover DNS** | Azure Traffic Manager (routing priority) o Front Door | 1 minuto |
| **3. Attivazione DB** | Azure SQL Active Geo-Replication → promo a primario in North Europe | 10-30 secondi |
| **4. Attivazione Pondus** | Azure Container Apps multi-regione — traffico reindirizzato a North Europe | 5 minuti |
| **5. Attivazione HPC** | Azure Site Recovery — failover VM HBv4 in North Europe | 30-60 minuti |
| **6. Verifica** | Smoke test su servizi critici | 30 minuti |
| **Totale RTO** | | **~1-2 ore** |

#### Procedure di Disaster Recovery

```
A. Disastro parziale (perdita singolo servizio)
   1. Identificare servizio degradato via Azure Monitor
   2. Ripristinare da backup più recente (se guasto dati)
   3. Oppure: aumentare repliche Container Apps (se guasto compute)

B. Disastro totale regione
   1. Attivare runbook DR
   2. Promuovere Azure SQL replica in North Europe a primario
   3. Puntare Traffic Manager su nuovo endpoint
   4. Riavviare carichi HPC in North Europe via Site Recovery
   5. Verificare integrità dati
   6. Comunicare ripristino al cliente

C. Test DR (semestrale)
   1. Eseguire failover simulato con Azure Site Recovery drill
   2. Verificare RPO/RTO reali
   3. Documentare gap e correzioni
   4. Report alla direzione
```

### RPO/RTO target

| Servizio | RPO | RTO | Note |
|---|---|---|---|
| Azure SQL (Pondus) | ≤1 ora (PITR) / 0 (Active Geo-Replication) | ≤30 sec (failover automatico) | Active Geo-Replication in modalità automatica |
| Azure Container Apps (Pondus) | ≤1 deploy | ≤5 min (multi-regione) | Traffic Manager per failover automatico |
| VM HBv4 (HPC) | ≤4 ore (Azure Backup ogni 4 ore) | ≤60 min (Site Recovery) | Site Recovery replica VM |
| Azure Blob Storage | 0 (versioning continuo) | ≤15 min | GRS con failover automatico |
| M365 | 0 (continuo) | ≤15 min | Microsoft gestisce il failover |

## COSTI

| Voce | Servizio Azure | Costo mensile stimato | Costo annuale |
|---|---|---|---|
| Azure Backup (VM + file) | Recovery Services Vault | ~€120 | ~€1.440 |
| Azure Blob Storage GRS | 20 TB, Hot tier | ~€240 | ~€2.880 |
| Azure Site Recovery | Replica VM HBv4 | ~€150 | ~€1.800 |
| SQL backup storage | Backup storage Azure SQL | ~€80 | ~€960 |
| Azure Traffic Manager / Front Door | Failover automatico multi-regione | ~€35 | ~€420 |
| **Totale annuo** | | | **~€7.500** |

*Costi basati su listino Azure 2026. GRS = Geo-Redundant Storage, replica automatica a regione accoppiata (West Europe ↔ North Europe). I costi di backup SQL sono inclusi nel prezzo dell'istanza Managed Instance.*
