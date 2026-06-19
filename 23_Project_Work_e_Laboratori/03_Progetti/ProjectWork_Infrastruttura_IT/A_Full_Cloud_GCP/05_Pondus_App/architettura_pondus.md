# Architettura Pondus — Variante Full Cloud GCP

## REQUISITI

- Stato attuale: Web application C#/.NET su IIS + MS SQL Server, HW dedicato (Xeon Silver 4110, 64 GB RAM, 1,2 TB HDD), attiva dal 2015
- Clientela: automotive (auto sportive) e aerospace — cerchia ristretta
- Obiettivo: potenziamento funzionale, pubblicazione online con abbonamento, distribuzione a utenza più ampia
- Target: containerizzato su Google Cloud, esposizione pubblica con dominio HTTPS
- DB: migrazione a Cloud SQL (SQL Server) o AlloyDB
- Scalabilità orizzontale, multi-tenancy, sito e-commerce per abbonamenti

## SOLUZIONE

### Architettura target

```
[Cloud Load Balancer] ---- [Cloud Run / GKE] ---- [Cloud SQL (SQL Server)]
         |                          |                        |
    [Dominio + HTTPS]          [Container C#]           [DB Persistente]
         |                          |
    [Cloud Armor (WAF)]        [Cloud Storage]
                                  (File statici)
```

### Componenti

| Componente | Servizio GCP | Ruolo |
|---|---|---|
| **Applicazione** | Cloud Run (container Linux/Windows) | Esecuzione containerizzata C#/.NET |
| **Database** | Cloud SQL per SQL Server | DB relazionale, backup automatici, replica multi-zona |
| **Load Balancer** | External HTTPS LB | Terminazione TLS, routing, scaling |
| **Storage** | Cloud Storage | File statici, upload materiali |
| **CDN** | Cloud CDN | Asset statici a bassa latenza |
| **Autenticazione** | Firebase Auth / Identity Platform | Abbonamenti, gestione utenti |
| **API** | Apigee / Cloud Endpoints | API management per integrazioni esterne |

### Strategia di containerizzazione

| Aspetto | Scelta |
|---|---|
| **Runtime** | .NET 8 su container Linux (Windows Server Core se dipendenze legacy) |
| **Registry** | Artifact Registry |
| **Orchestrazione** | Cloud Run (serverless) per semplicità; GKE solo se necessario per controllo granulare |
| **Build** | Cloud Build + Dockerfile multi-stage |
| **Scaling** | Cloud Run: 0-100 istanze automatico (min 1 per evitare cold start) |

### Migrazione DB

| Passaggio | Dettaglio |
|---|---|
| **Source** | MS SQL Server on-premise (Xeon Silver 4110, 64 GB RAM) |
| **Target** | Cloud SQL for SQL Server (Standard tier, 16 vCPU, 64 GB RAM) |
| **Tool** | Database Migration Service (DMS) — CDC per migrazione a zero downtime |
| **Schema** | Valutare compatibilità: SQL Server 2019 on-prem → SQL Server 2022 su Cloud SQL |
| **Dimensione DB** | Stima: 50-200 GB (dati storici + configurazioni) |

### Pubblicazione online e abbonamenti

- **Sito vetrina**: landing page con descrizione servizio, case study, contatti
- **Area clienti**: login con abbonamento mensile (Firebase Auth + Stripe)
- **E-commerce**: pagamento ricorrente per abbonamenti (Stripe + Cloud Functions webhook)
- **Dominio**: acquisto tramite Cloud Domains o registrar esterno, certificato TLS via Google-managed SSL
- **API pubblica**: endpoint REST documentati (OpenAPI) per integrazione clienti

## DIMENSIONAMENTO

| Risorsa | Specifica |
|---|---|
| **Cloud Run CPU** | 4 vCPU per istanza (min 1, max 20) |
| **Cloud Run RAM** | 8 GB per istanza |
| **Concorrenza** | 80 richieste concorrenti per istanza |
| **Cloud SQL** | 16 vCPU, 64 GB RAM, SSD 500 GB, replica multi-zona |
| **Storage** | 100 GB Cloud Storage Standard |
| **Banda** | 500 Mbps (CDN per asset statici) |

## COSTI

| Voce | Servizio | Costo mensile | Costo annuale |
|---|---|---|---|
| Cloud Run | 4 vCPU, 8 GB RAM, 500k richieste/giorno | ~$300 | ~$3.600 |
| Cloud SQL SQL Server | 16 vCPU, 64 GB, 500 GB SSD | ~$1.500 | ~$18.000 |
| Cloud Load Balancer | HTTPS LB + SSL | ~$50 | ~$600 |
| Cloud Armor | WAF | ~$100 | ~$1.200 |
| Cloud CDN | 100 GB/mese | ~$10 | ~$120 |
| Dominio + certificato | Dominio .com + SSL managed | ~$15 | ~$180 |
| Stripe commissioni | 2,9% + €0,30 per transazione | Variabile | Variabile |
| **Totale** | | **~$1.975** | **~$23.700** |

*Costi Cloud SQL SQL Server includono licenza (costo maggiorato rispetto a MySQL/PostgreSQL). Valutare alternativa: AlloyDB (compatibile PostgreSQL) per ridurre costi licenza.*

## Piano di migrazione

| Fase | Durata | Attività |
|---|---|---|
| 1. Assessment | 1 settimana | Analisi codice C#, dipendenze legacy, compatibilità container |
| 2. Refactoring | 3 settimane | Adattamento IIS → Kestrel, configurazione container, Dockerfile |
| 3. Migrazione DB | 2 settimane | DMS setup + migrate + verifica integrità |
| 4. Deploy Staging | 1 settimana | Deploy su Cloud Run staging, test funzionali |
| 5. Deploy Produzione | 3 giorni | Cut-over DNS, attivazione HTTPS, verifica |
| 6. Attivazione abbonamenti | 1 settimana | Integrazione Stripe, test pagamento, go-live sito |
