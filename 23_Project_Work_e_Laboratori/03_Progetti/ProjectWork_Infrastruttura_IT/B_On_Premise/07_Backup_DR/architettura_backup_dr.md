# Architettura Backup e DR — Variante On-Premise

## REQUISITI

- 3-2-1 rule: 3 copie su 2 media, 1 copia off-site
- RPO ≤4 ore per servizi critici, RTO ≤24 ore
- Backup locale su NAS QNAP 32 TB esistente (da espandere)
- Backup off-site su co-location (sede secondaria)
- DR: servizi critici (Pondus, AD) recuperabili da co-location
- Backup HPC: dati progetto su NAS + storage co-location

## SOLUZIONE

### Architettura backup

```
[Produzione — Sede Thema]               [Co-location / DR]
         |                                      |
[NAS QNAP 32 TB]                        [NAS secondario 32 TB]
    Backup locale                             |
    (giornaliero)                  [Replica off-site notturna]
         |                                      |
[Server / VM / DB]              [DR failover (Pondus, AD)]
    Backup agent
    (Veeam / rsync)
```

### Backup per servizio

| Servizio | Metodo | Frequenza | Retention | Destinazione |
|---|---|---|---|---|
| **VM server (Veeam)** | Agente backup Veeam su VM | Giornaliero | 14 giorni | NAS QNAP + co-location |
| **MS SQL (Pondus)** | Backup nativo SQL + Veeam | Ogni 4 ore | 7 giorni (PITR) + 30 giorni (full) | NAS + co-location |
| **File server (NextCloud)** | rsync + snapshot NAS | Giornaliero | 30 giorni | NAS QNAP |
| **HPC dati progetto** | rsync da scratch a NAS | Settimanale (post-job) | 90 giorni | NAS QNAP |
| **Active Directory** | Backup Veeam + export | Giornaliero | 30 giorni | NAS + co-location |
| **Posta (Zimbra)** | Zimbra backup + Veeam | Giornaliero | 14 giorni | NAS QNAP |
| **Configurazioni firewall/switch** | Config backup automatico | Ad ogni modifica | Ultime 5 versioni | NAS QNAP |
| **Documenti (MediaWiki)** | Dump DB + file | Settimanale | 90 giorni | NAS + co-location |

### Replica off-site

- **Metodo**: Veeam Backup & Replication (o rsync crittografato)
- **Destinazione**: NAS secondario 32 TB in co-location
- **Frequenza**: notturna (finestra: 22:00-06:00)
- **Crittografia**: AES-256 in transito (IPsec tra sedi)
- **Banda**: 500 Mbps dedicata per replica off-site

### Disaster Recovery

#### Scenario: Disastro sede Thema (incendio, allagamento, furto)

| Fase | Azione | Tempo |
|---|---|---|
| **1. Attivazione DR** | Team IT avvia runbook DR | 1 ora |
| **2. Provisioning HW** | Server in co-location (spare) accesi | 2 ore |
| **3. Restore AD** | Avvio Samba4 AD da backup su NAS co-location | 2 ore |
| **4. Restore Pondus** | MS SQL + applicazione da backup | 3 ore |
| **5. DNS cut-over** | Puntamento DNS su IP co-location | 1 ora |
| **6. Verifica** | Smoke test servizi | 2 ore |
| **RTO totale** | | **~10 ore** |

#### Scenario: Guasto HW singolo (es. server Pondus)

| Fase | Azione | Tempo |
|---|---|---|
| 1. Spare server in sede (pre-configurato) | Accensione | 30 min |
| 2. Restore ultimo backup | NAS QNAP → spare server | 1 ora |
| 3. Test funzionale | Verifica servizio | 30 min |
| **RTO** | | **~2 ore** |

### RPO/RTO target

| Servizio | RPO | RTO | Dipendenza |
|---|---|---|---|
| Pondus (DB + app) | 4 ore | 2 ore (guasto HW) / 10 ore (disastro) | NAS QNAP + spare |
| File server | 24 ore | 4 ore | NAS QNAP |
| HPC dati | 7 giorni | 24 ore | NAS + backup |
| Posta | 24 ore | 4 ore | Veeam restore |
| AD | 24 ore | 2 ore | NAS + spare |
| Sito aziendale | 24 ore | 4 ore | General purpose |

## DIMENSIONAMENTO

| Storage | Capacità | Ruolo |
|---|---|---|
| NAS QNAP primario (esistente) | 32 TB | Backup locale servizi |
| NAS secondario (co-location) | 32 TB | Replica off-site |
| Espansione NAS primario (se necessario) | +16 TB | Capacità aggiuntiva |

## COSTI

| Voce | Una tantum | Annuale |
|---|---|---|
| NAS QNAP secondario 32 TB (co-location) | ~€3.000 | — |
| Veeam Backup & Replication (server + VM) | ~€1.200 | ~€600 (maintenance) |
| Espansione NAS primario +16 TB (opzionale) | ~€800 | — |
| Dischi HDD per spare (hot spare kit) | ~€500 | — |
| Banda replicate off-site (quota ISP) | — | Già inclusa in connettività |
| **Totale** | **~€5.500** | **~€600/anno** |

*Veeam: licenza standard per backup VM + agent su SQL. Alternativa open source: Bacula o XtraBackup (costo €0).*
