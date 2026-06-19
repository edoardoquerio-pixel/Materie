# Architettura Backup e DR — Variante Ibrida

## REQUISITI

- 3-2-1 rule con copertura sia on-prem che cloud
- RPO servizi critici: ≤1 ora (Pondus cloud), ≤4 ore (HPC on-prem)
- RTO servizi critici: ≤15 min (Pondus), ≤10 ore (disastro HPC)
- Backup on-prem: HPC + AD + dati non migrati
- Backup cloud: Pondus + servizi migrati
- DR: failover cloud automatico per Pondus, restore manual per HPC

## SOLUZIONE

### Architettura duale

```
[Sede Thema — On-prem]                    [GCP]
       |                                       |
[NAS QNAP 32 TB]                       [Cloud Storage]
  - HPC dati progetto                     - Pondus backup
  - AD snapshot                           - Cloud SQL backup
  - HPC config                            - File collaborativi
       |                                       |
[Replica off-site]                      [Multi-regione]
  - NAS secondario (co-location)           - europe-west4 DR
```

### Backup per servizio

| Servizio | Location | Metodo | RPO | Retention |
|---|---|---|---|---|
| **HPC (dati progetto)** | On-prem | rsync → NAS QNAP | 24 ore | 90 giorni |
| **HPC (config)** | On-prem | Snapshot → NAS | 7 giorni | 30 giorni |
| **Pondus (DB)** | Cloud | Cloud SQL PITR | 1 ora | 30 giorni |
| **Pondus (app)** | Cloud | Container registry | Ad ogni deploy | 10 versioni |
| **AD (Samba4)** | On-prem | Veeam → NAS | 24 ore | 30 giorni |
| **File HPC** | On-prem | rsync → NAS | 24 ore | 90 giorni |
| **File collab** | Cloud | Versioning GDrive | Continuo | 90 giorni |
| **VM servizi** | On-prem | Veeam → NAS | 24 ore | 14 giorni |

### DR Strategy

| Scenario | Azione | RTO |
|---|---|---|
| **Guasto HPC on-prem** | Ripristino da backup su nodi spare + job re-schedule | 4 ore |
| **Guasto Pondus cloud** | Cloud SQL failover + Cloud Run multi-regione | 15 min |
| **Disastro sede Thema** | Attivazione servizi cloud (Pondus + DR), restore AD in co-location | 10 ore |
| **Disastro GCP regione** | Backup su europe-west4 attivato | 2 ore |
| **Perdita dati** | Restore da backup (NAS / Cloud Storage) | Variabile (2-10 ore) |

## COSTI

| Voce | Una tantum | Annuale |
|---|---|---|
| NAS QNAP secondario (co-location) | ~€3.000 | — |
| Veeam Backup Standard | ~€1.200 | ~€600 |
| Cloud Storage backup | — | ~$2.000 |
| Cloud SQL backup storage | — | ~$600 |
| GCP DR (istanze standby minime) | — | ~$6.000 |
| **Totale** | **~€4.200** | **~€9.200** |
