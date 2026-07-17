# Cloud Azure — Note Complete

## 1. Azure Core Services

**Compute:**
- **Azure VMs**: IaaS, Windows/Linux, scale sets, availability sets/zones
- **App Services**: PaaS per web app, auto-scale, slot deployment
- **Azure Functions**: serverless, event-driven, trigger (HTTP, Timer, Blob, Queue)
- **AKS (Azure Kubernetes Service)**: managed K8s, node pools, auto-scaling
- **Container Instances**: container senza orchestrazione

**Storage:**
- **Blob Storage**: oggetti non strutturati (hot/cool/archive tier)
- **Disk Storage**: SSD/HDD managed disks per VM
- **Azure Files**: SMB shares, cloud o ibrido
- **Azure SQL Database**: managed SQL Server, DTU/vCore, elastic pool

**Networking:**
- **VNet**: reti virtuali, subnet, peering
- **Load Balancer**: Layer 4 (pubblico/interno)
- **Application Gateway**: Layer 7, WAF, SSL termination, URL routing
- **VPN Gateway**: site-to-site, point-to-site
- **Azure DNS**: hosting domini, zone private
- **CDN / Front Door**: caching + global routing
- **Traffic Manager**: DNS-based routing

## 2. Azure Functions v2 (Python)

```python
import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="hello", methods=["GET"], auth_level=func.AuthLevel.FUNCTION)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")
    logging.info(f"HTTP trigger: name={name}")
    return func.HttpResponse(f"Hello {name}!")
```

- **local.settings.json**: configurazione locale, connessioni
- **host.json**: trigger globali, timeout, binding
- **Bindings**: input/output dichiarativi (Blob, Queue, Cosmos DB, SQL)
- **Durable Functions**: orchestrazione, fan-out/fan-in

## 3. Identity & Security

- **Entra ID (Azure AD)**: tenant, utenti, gruppi, applicazioni
- **RBAC**: ruoli (Owner, Contributor, Reader) + custom roles
- **Managed Identities**: identity automatiche per servizi Azure
- **Key Vault**: segreti, chiavi, certificati
- **NSG/ASG**: filtri traffico subnet/NIC per applicazione
- **Azure Policy**: governance, compliance, tagging

## 4. AI & ML

- **Azure AI Services**: Vision, Language, Speech, Decision
- **Azure Machine Learning**: workspace, pipeline, AutoML, endpoint
- **Cognitive Search**: AI-powered search, indexing, enrichment

## 5. Management & Monitoring

- **Azure Portal**: GUI management
- **Azure CLI**: `az group create`, `az vm create`, `az functionapp`
- **Azure PowerShell**: `Az` module cmdlet
- **ARM/Bicep**: Infrastructure as Code
- **Azure Monitor**: metrics, logs, alerts
- **Application Insights**: APM, telemetry, distributed tracing

## 6. Reti su Azure

- **VNet peering**: connessione VNet (stessa region o cross-region)
- **Azure Bastion**: RDP/SSH senza IP pubblico (via Azure Portal)
- **Private Link / Private Endpoint**: connessione privata a servizi Azure
- **ExpressRoute**: connessione dedicata on-prem → Azure
- **Azure Firewall**: stato completo, FQDN filtering, threat intel
- **Hub & Spoke**: topologia rete centralizzata

## 7. Cost Management

- **TCO Calculator**: stima risparmio migrazione
- **Pricing Calculator**: preventivi servizi
- **Reserved Instances**: sconto 1-3 anni, 40-70%
- **Azure Hybrid Benefit**: licenze Windows Server/SQL esistenti
- **Budget + Alerts**: monitoraggio spesa
- **FinOps**: tagging, right-sizing, auto-shutdown
