# Architettura Backup e DR — Variante Full Cloud GCP

## REQUISITI

- 3-2-1 rule: 3 copie, 2 media differenti, 1 copia off-site
- RPO (Recovery Point Objective): ≤4 ore per servizi critici
- RTO (Recovery Time Objective): ≤8 ore per servizi critici, ≤24 ore per servizi non critici
- Delocalizzazione: backup in regione GCP secondaria
- Business continuity: failover automatico multi-regione
- Copertura: VM, database, file storage, applicazioni (Pondus), HPC
- Fruibilità servizi clienti anche in caso di disastro

## SOLUZIONE

### Strategia generale

```
[Produzione us-central1]      [Backup/Ripristino europe-west4]
         |                                 |
    [Servizi GCP]                    [Cloud Storage]
         |                                 |
    [Backup automatici]        [Copia multi-regione]
         |                                 |
    [Snapshot / Dump]            [Replica asincrona]
```

### Backup per servizio

| Servizio | Metodo | Frequenza | Retention | Destinazione |
|---|---|---|---|---|
| **Cloud SQL (SQL Server)** | Backup automatico managed | Giornaliero + point-in-time | 30 giorni | Multi-regione |
| **Cloud Run (Pondus)** | Immagine container in Artifact Registry | Ad ogni deploy | Ultime 10 versioni | Multi-regione |
| **VM Compute Engine** | Snapshot disco | Giornaliero | 14 giorni | Multi-regione |
| **Cloud Storage** | Object versioning + lifecycle | Continuo (versioning) | 90 giorni + archive | Multi-regione |
| **HPC (C2 istanze)** | Snapshot + dati su Cloud Storage | Settimanale | 30 giorni | Multi-regione |
| **Google Workspace** | Google Vault (retention policy) | Continuo | Secondo policy legale | Nativo Google |
| **BitBucket** | Git repository backup | Giornaliero | 30 giorni | Cloud Storage |
| **Odoo** | Backup automatico SaaS | Giornaliero | 14 giorni (nativo) + extra su Cloud Storage |

### Disaster Recovery

#### Scenario: Disastro regione us-central1

| Fase | Azione | Tempo stimato |
|---|---|---|
| **1. Rilevamento** | Monitoring GCP (Uptime Check) rileva indisponibilità | 1 minuto |
| **2. Failover DNS** | Cloud DNS con routing basato su health check | 5 minuti |
| **3. Attivazione DB** | Cloud SQL replica di failover in europe-west4 → promo a primario | 10-30 minuti |
| **4. Attivazione Pondus** | Cloud Run multi-regione — traffico reindirizzato a europe-west4 | 5 minuti |
| **5. Attivazione HPC** | Riavvio istanze C2 in europe-west4 da snapshot | 30-60 minuti |
| **6. Verifica** | Smoke test su servizi critici | 30 minuti |
| **Totale RTO** | | **~1-2 ore** |

#### Procedure di Disaster Recovery

```
A. Disastro parziale (perdita singolo servizio)
   1. Identificare servizio degradato via Cloud Monitoring
   2. Ripristinare da backup più recente (se guasto dati)
   3. Oppure: aumentare repliche (se guasto compute)
   
B. Disastro totale regione
   1. Attivare runbook DR
   2. Promuovere Cloud SQL replica in europe-west4 a primario
   3. Puntare Cloud DNS su nuovo indirizzo
   4. Riavviare carichi HPC in europe-west4
   5. Verificare integrità dati
   6. Comunicare ripristino al cliente

C. Test DR (semestrale)
   1. Eseguire failover simulato in ambiente di staging
   2. Verificare RPO/RTO reali
   3. Documentare gap e correzioni
   4. Report alla direzione
```

### RPO/RTO target

| Servizio | RPO | RTO | Note |
|---|---|---|---|
| Cloud SQL (Pondus DB) | 1 ora | 15 min | Backup PITR + replica |
| Cloud Run (Pondus) | 0 (immagine deploy) | 5 min | Multi-regione attivo |
| VM Compute Engine | 24 ore (snapshot) | 2 ore | Avvio da snapshot |
| Cloud Storage | 0 (versioning) | 1 min | Sempre disponibile |
| HPC dati | 24 ore (snapshot) | 4 ore | Riavvio con snapshot |
| Google Workspace | Nativo | 1 ora | Google Vault |
| **Servizi clienti (Pondus)** | **1 ora** | **15 min** | **Priorità massima** |

## DIMENSIONAMENTO

| Componente | Capacità | Costo mensile |
|---|---|---|
| Cloud Storage (backup primario) | 5 TB Standard | ~$100 |
| Cloud Storage (archive a 90gg) | 10 TB Archive | ~$60 |
| Snapshot Compute Engine | 2 TB | ~$80 |
| Cloud SQL backup storage | 500 GB | ~$50 |
| Artifact Registry | 20 GB | ~$2 |
| Network egress DR test | 500 GB/mese | ~$50 |
| **Totale backup** | | **~$342/mese** |

## COSTI

| Voce | Costo mensile | Costo annuale |
|---|---|---|
| Cloud Storage backup | ~$160 | ~$1.920 |
| Snapshot Compute Engine | ~$80 | ~$960 |
| Cloud SQL backup storage | ~$50 | ~$600 |
| Artifact Registry | ~$2 | ~$24 |
| Data transfer (DR test) | ~$50 | ~$600 |
| **Totale backup** | **~$342** | **~$4.104** |
| **Costo DR (istanze standby)** | **~$500** | **~$6.000** |
| **Totale complessivo** | **~$842** | **~$10.104** |

*DR istanze standby: VM minime in europe-west4 per failover rapido (non scalate).*
*Opzione cost-saving: usare snapshot al posto di istanze standby per HPC (RTO 4h invece di 1h).*
