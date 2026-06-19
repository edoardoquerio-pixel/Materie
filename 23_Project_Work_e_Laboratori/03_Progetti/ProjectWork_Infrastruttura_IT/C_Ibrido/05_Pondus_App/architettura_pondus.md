# Architettura Pondus — Variante Ibrida

## REQUISITI

- Migrazione Pondus su GCP (Cloud Run + Cloud SQL)
- DB MS SQL → Cloud SQL (SQL Server)
- Esposizione pubblica HTTPS
- Containerizzazione C#/.NET
- Abbonamento e-commerce
- Integrazione AD Samba4 on-prem (autenticazione)

## SOLUZIONE

### Architettura ibrida

Ibrida per Pondus significa: applicazione su cloud, autenticazione ibrida
(AD on-prem + Identity Platform), backup on-prem + cloud.

```
[Clienti] ---- HTTPS ---- [Cloud LB GCP]
                                |
                      [Cloud Run (Pondus)]
                                |
                    [Cloud SQL (SQL Server)]
                                |
              [Identity Platform + Samba4 AD]
                    (federation)
```

### Componenti

| Componente | Servizio | Location |
|---|---|---|
| **Applicazione** | Cloud Run (C#/.NET container) | GCP |
| **Database** | Cloud SQL SQL Server | GCP |
| **Autenticazione** | Identity Platform + Samba4 AD (LDAPS) | Cloud + on-prem |
| **File statici** | Cloud Storage | GCP |
| **Backup DB** | Cloud SQL backup + NAS QNAP | GCP + on-prem |
| **Monitoring** | Cloud Monitoring + Grafana on-prem | Cloud + on-prem |

## DIMENSIONAMENTO

| Risorsa | Specifica |
|---|---|
| Cloud Run | 4 vCPU, 8 GB RAM, 0-50 istanze |
| Cloud SQL | 16 vCPU, 64 GB RAM, 500 GB SSD |
| Storage | 100 GB Cloud Storage |
| Backup on-prem | 200 GB su NAS QNAP |

## COSTI

| Voce | Costo mensile | Costo annuale |
|---|---|---|
| Cloud Run | ~$300 | ~$3.600 |
| Cloud SQL SQL Server | ~$1.500 | ~$18.000 |
| Cloud Load Balancer | ~$50 | ~$600 |
| Cloud Armor WAF | ~$100 | ~$1.200 |
| Identity Platform | ~$50 | ~$600 |
| **Totale** | **~$2.000** | **~$24.000** |
