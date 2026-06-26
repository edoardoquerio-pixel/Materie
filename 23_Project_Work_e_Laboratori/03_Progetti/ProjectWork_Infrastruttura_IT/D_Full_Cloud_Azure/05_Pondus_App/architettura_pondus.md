# Architettura Pondus — Variante Full Cloud Azure

## REQUISITI

- Stato attuale: Web application C#/.NET su IIS + MS SQL Server, HW dedicato (Xeon Silver 4110, 64 GB RAM, 1,2 TB HDD), attiva dal 2015
- Clientela: automotive (auto sportive) e aerospace — cerchia ristretta
- Obiettivo: potenziamento funzionale, pubblicazione online con abbonamento, distribuzione a utenza più ampia
- Target: containerizzato su Azure, esposizione pubblica con dominio HTTPS
- DB: migrazione ad Azure SQL con Azure Hybrid Benefit (riuso licenza SQL on-prem)
- Scalabilità orizzontale, multi-tenancy, sito e-commerce per abbonamenti
- **Vincolo tecnico**: dipendenze Windows legacy (IIS, librerie Win32) — container Linux non sufficiente

## SOLUZIONE

### Architettura target

```
[Azure Application Gateway v2 (WAF)] ---- [Azure Kubernetes Service (AKS)] ----- [Azure Cache for Redis]
         |                                         |   Windows nodepool   |           (caching)
     [Dominio + HTTPS]                         [Container .NET 8 su    ]              |
                                                 Windows nanoserver]                   |
         |                                         |                    [Azure SQL Managed Instance (BC)]
     [Azure CDN]                              [Azure Container Registry]         + Failover Group
                                                (immagini Windows)           West Europe ←→ North Europe
```

### Perché AKS con Windows nodepool

Pondus è un'applicazione C#/.NET con dipendenze Windows legacy (IIS, possibili librerie Win32, configurazioni di sistema). **Azure Container Apps non supporta Windows containers** — supporta solo container Linux. L'unica piattaforma Azure container che supporta Windows containers è **Azure Kubernetes Service (AKS) con Windows nodepool**.

Vantaggi della scelta AKS Windows:

| Aspetto | AKS Windows | Container Apps Linux (scartata) |
|---|---|---|
| **Supporto Windows container** | ✅ Sì | ❌ No (solo Linux) |
| **Dockerfile Windows base** | ✅ `nanoserver` o `windowsservercore` | ❌ N/A |
| **Compatibilità codice esistente** | ✅ Minimo refactoring (IIS→Kestrel) | ❌ Richiede rewrite per Linux |
| **Costo** | ~€8.160/anno (D4s_v3 nodepool) | ~€3.000/anno (più economico ma incompatibile) |
| **Scalabilità** | Fino a 1000 pod per cluster | Fino a 100 repliche per revision |
| **Aggiornamenti** | Gestiti da Azure (nodepool upgrade) | Automatici (serverless) |

### Componenti

| Componente | Servizio Azure | Ruolo |
|---|---|---|---|
| **Applicazione** | AKS + Windows nodepool (Standard_D4s_v3) | Monolito .NET 8 su Windows nanoserver (HPA scala repliche) |
| **Cache** | Azure Cache for Redis Standard C1 | Caching query DB, sessioni utente, riduce latenza |
| **Registry** | Azure Container Registry (ACR) | Immagini container Windows |
| **Database** | Azure SQL Managed Instance (Business Critical) | DB relazionale, SSD locale (<1 ms), Active Geo-Replication automatica, Failover Group WE↔NE |
| **Load Balancer** | Azure Application Gateway v2 | Terminazione TLS, WAF, routing, cookie-based affinity |
| **Storage** | Azure Blob Storage | File statici, upload materiali |
| **CDN** | Azure CDN (Microsoft) | Asset statici a bassa latenza globale |
| **Autenticazione** | Microsoft Entra ID + Azure AD B2C | Abbonamenti, gestione utenti, MFA |
| **API** | Azure API Management | API gateway per integrazioni esterne |

### Strategia di containerizzazione

| Aspetto | Scelta |
|---|---|
| **Runtime** | .NET 8 su **Windows container (nanoserver-ltsc2022)** |
| **Base image** | `mcr.microsoft.com/dotnet/aspnet:8.0-nanoserver-ltsc2022` |
| **Registry** | Azure Container Registry (ACR) — supporta immagini Windows |
| **Orchestrazione** | **Azure Kubernetes Service (AKS)** — cluster con Windows nodepool |
| **Node pool Windows** | Standard_D4s_v3 (4 vCPU, 16 GB RAM) — 1 nodo, auto-scaling 1-3 |
| **Build** | Dockerfile multi-stage + ACR Tasks (supporto Windows build agent) |
| **Scaling** | HPA (Horizontal Pod Autoscaler): CPU >70% trigger, min 2 pod, max 20 |
| **Architettura** | **Monolito** (non microservizi). HPA scala repliche identiche dell'intera applicazione. Per carichi >500 utenti concorrenti, valutare refactoring in microservizi separati |

> **Nota sull'architettura**: Pondus rimane un'applicazione **monolitica**. La scalabilità orizzontale è garantita dall'HPA che replica l'intero pod. Questo è sufficiente per l'utenza iniziale (decine di utenti) e per la crescita prevista. Non ci sono microservizi separati — ogni replica esegue l'intera applicazione C#.NET. Per utenze superiori a 500 utenti concorrenti, si consiglia un refactoring in microservizi (pondus-api, pondus-calc, pondus-billing).

#### Dockerfile esempio

```dockerfile
# Stage 1: Build
FROM mcr.microsoft.com/dotnet/sdk:8.0-nanoserver-ltsc2022 AS build
WORKDIR /src
COPY Pondus.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app

# Stage 2: Runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0-nanoserver-ltsc2022 AS runtime
WORKDIR /app
COPY --from=build /app .
EXPOSE 8080
ENTRYPOINT ["dotnet", "Pondus.dll"]
```

### Migrazione DB con Azure Hybrid Benefit

| Passaggio | Dettaglio |
|---|---|
| **Source** | MS SQL Server on-premise (Xeon Silver 4110, 64 GB RAM) |
| **Target** | Azure SQL Managed Instance — **Business Critical** (16 vCPU, 64 GB RAM, SSD locale <1 ms I/O latency) |
| **Failover Group** | Automatico: West Europe (primario) ↔ North Europe (secondario). RPO ~5 secondi, RTO ~1 minuto |
| **Tool** | Azure Database Migration Service (DMS) — CDC per migrazione a zero downtime |
| **Hybrid Benefit** | La licenza SQL Server on-premise esistente viene applicata su **entrambe** le istanze (primaria + secondaria failover) → **risparmio ~55%** su ciascuna |
| **Retention backup (PITR)** | **35 giorni** — massima finestra di recupero ISO 27001 compliant |
| **Dimensione DB** | Stima: ~200 GB (dati storici + configurazioni) |

> **Azure Hybrid Benefit**: Poiché Thema possiede già licenze SQL Server on-premise (Software Assurance), queste possono essere riutilizzate su Azure SQL con uno sconto del ~55% rispetto al prezzo con licenza inclusa.

### Pubblicazione online e abbonamenti

- **Sito vetrina**: landing page con descrizione servizio, case study, contatti
- **Area clienti**: login con abbonamento mensile (Azure AD B2C + Stripe)
- **E-commerce**: pagamento ricorrente per abbonamenti (Stripe + Azure Functions webhook)
- **Dominio**: acquisto tramite registrar esterno, certificato TLS via Azure App Service Managed Certificate
- **API pubblica**: endpoint REST documentati (OpenAPI) tramite Azure API Management

## DIMENSIONAMENTO

| Risorsa | Specifica |
|---|---|
| **AKS cluster** | 1 Windows nodepool (Standard_D4s_v3) |
| **Windows nodepool RAM** | 16 GB per nodo |
| **Concorrenza** | 200 richieste concorrenti per pod (configurazione Kestrel). Utenza target: poche decine, scalabile |
| **Redis Cache** | Azure Cache for Redis Standard C1 (1 GB cache, 250 connessioni concorrenti, <1 ms latenza) |
| **Azure SQL Managed Instance** | Business Critical, 16 vCPU, 64 GB RAM, 500 GB storage, SSD locale, Failover Group WE↔NE automatico, PITR retention 35 giorni |
| **Blob Storage** | 100 GB, Hot tier |
| **CDN** | Azure CDN Standard (Microsoft) |
| **ACR** | Basic SKU, 10 GB storage |

## COSTI

| Voce | Servizio | Costo mensile | Costo annuale |
|---|---|---|---|---|
| Windows nodepool | 1 × Standard_D4s_v3 (Windows license inclusa) | ~€680 | ~€8.160 |
| Redis Cache | Standard C1 (1 GB) | ~€75 | ~€900 |
| Azure SQL MI (primario) | Business Critical 16 vCPU, 200 GB (Hybrid Benefit -55%) | ~€1.658 | ~€19.896 |
| Azure SQL MI (failover secondario) | Business Critical 16 vCPU, replica WE→NE (Hybrid Benefit -55%) | ~€1.658 | ~€19.896 |
| Application Gateway v2 | WAF_v2, TLS termination | ~€120 | ~€1.440 |
| Azure CDN | 100 GB/mese | ~€8 | ~€96 |
| Azure AD B2C | 50k utenti mensili | ~€30 | ~€360 |
| Dominio + certificato | Dominio .com + TLS managed | ~€15 | ~€180 |
| Azure Container Registry | Basic SKU | ~€6 | ~€72 |
| Stripe commissioni | 2,9% + €0,30 per transazione | Variabile | Variabile |
| **Totale annuo** | | | **~€51.000** |

> **Nota**: Il costo annivo di ~€51.000 riflette il passaggio a **Business Critical** con **Failover Group automatico** (West Europe ↔ North Europe), che garantisce RPO ~5 secondi e RTO ~1 minuto. La replica secondaria di failover raddoppia il costo SQL ma è necessaria per la continuità operativa richiesta da ISO 27001. **Azure Cache for Redis** (~€900/anno) riduce la latenza delle query frequenti e allevia il carico sul DB. Azure Hybrid Benefit (-55%) si applica a entrambe le istanze SQL (primaria e secondaria).

## Piano di migrazione

| Fase | Durata | Attività |
|---|---|---|
| 1. Assessment | 1 settimana | Analisi codice C#, dipendenze Windows legacy, compatibilità container nanoserver |
| 2. Refactoring IIS→Kestrel | 2 settimane | Adattamento IIS → Kestrel, configurazione Dockerfile Windows, test build ACR |
| 3. Setup AKS cluster + Redis | 1 settimana | Creazione cluster AKS, configurazione Windows nodepool, deploy Redis Cache C1, installazione ingress controller |
| 4. Migrazione DB | 2 settimane | Azure DMS setup + migrate + Hybrid Benefit activation + Failover Group WE↔NE + PITR 35gg |
| 5. Deploy su AKS staging | 1 settimana | Deploy container Windows su AKS staging, integrazione Redis, test funzionali, HPA tuning |
| 6. Deploy Produzione | 3 giorni | Cut-over DNS, attivazione HTTPS via App Gateway, verifica failover group |
| 7. Attivazione abbonamenti | 1 settimana | Integrazione Stripe + B2C, test pagamento, go-live sito |
