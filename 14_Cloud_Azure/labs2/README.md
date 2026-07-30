# Automazione DevOps su Azure - Due Pipeline in Un Unico Repository

Questo progetto implementa l'automazione DevOps completa per le esercitazioni conclusive del corso Azure, trasformando in flusso automatico ciò che era stato fatto manualmente.

## Architettura

```
.
├── container/                 # Codice applicazione containerizzata
│   ├── app.py                # App Flask di esempio
│   ├── Dockerfile            # Build multi-stage
│   ├── requirements.txt      # Dipendenze Python
│   └── azure-pipelines.yml   # Pipeline A: build & push su ACR
├── function/                  # Codice Azure Function
│   ├── function_app.py       # HTTP trigger function
│   ├── host.json             # Configurazione Function
│   ├── requirements.txt      # Dipendenze Python
│   └── azure-pipelines.yml   # Pipeline B: deploy su Function App
├── pipelines/                 # Pipeline YAML aggiuntive (opzionali)
├── terraform/                 # Provisioning infrastructure as code
│   ├── main.tf               # Risorse principali
│   ├── variables.tf          # Variabili
│   ├── outputs.tf            # Output
│   └── providers.tf          # Provider Azure + azurerm
└── README.md                  # Questo file
```

## Flusso Automatico

A ogni `git push` su `main`:

| Path modificato | Pipeline attivata | Azione |
|-----------------|-------------------|--------|
| `container/**`  | Pipeline A (ACR)  | `az acr build` → immagine su ACR con tag `$(Build.BuildId)` e `latest` |
| `function/**`   | Pipeline B (Function) | `AzureFunctionApp@2` → deploy codice su Function App esistente |

**Nessun passaggio manuale** tra il push e il risultato in cloud.

## Prerequisiti (già provisionati via Terraform)

- **Azure DevOps Project** su ExtraNet con Azure Repos e Pipelines
- **Service Connection** basata su **Workload Identity Federation** (nessun segreto nei sorgenti)
- **Azure Container Registry (ACR)** - dalla esercitazione 26
- **Function App** su piano **Flex Consumption** - dalla esercitazione 23/25 (richiesto per Python 3.11+)

## Pipeline A - Container (ACR)

**File:** `container/azure-pipelines.yml`

Caratteristiche:
- Trigger filtrato su `container/**`
- Build delegata ad ACR (`az acr build`) - l'agent non serve Docker
- Due tag: `$(Build.BuildId)` (tracciabilità) + `latest` (comodità)
- Autenticazione via service connection (workload identity)

## Pipeline B - Function App

**File:** `function/azure-pipelines.yml`

Caratteristiche:
- Trigger filtrato su `function/**`
- Deploy del pacchetto codice su Function App **esistente** (non la ricrea)
- Piano **Flex Consumption** per supportare Python 3.11+
- Autenticazione via service connection (workload identity)

## Provisioning Terraform

Il modulo `terraform/` crea:
- Resource Group
- Azure Container Registry (SKU Basic/Standard)
- Function App su **Flex Consumption Plan** (Linux, Python 3.11+)
- Storage Account per Function App
- Log Analytics Workspace
- Service Principal + Federated Identity Credential per Workload Identity Federation
- Role Assignments: `AcrPush` su ACR, `Website Contributor` su Function App

## Verifica dal Vivo

Dopo ogni commit:
1. **ACR**: `az acr repository show-tags --name <acr> --repository <image> -o table` → mostra il nuovo tag `$(Build.BuildId)` e `latest` aggiornato
2. **Function**: `curl https://<function-app>.azurewebsites.net/api/<function>` → risponde con la nuova versione del codice

## Note Tecniche Chiave

| Argomento | Dettaglio |
|-----------|-----------|
| **Workload Identity Federation** | Nessun client secret nei sorgenti; token OIDC scambiato a runtime |
| **az acr build vs agent build** | Build in ACR = nessun Docker su agent, cache layer nativa, più veloce |
| **Python version** | Python 3.11+ non supportato su Consumption classico → serve **Flex Consumption** |
| **Permit service connection** | Alla prima run la pipeline si ferma "waiting for approval" → cliccare **View → Permit** |
| **Package path Function** | `package: '$(System.DefaultWorkingDirectory)/function'` per deployare la cartella corretta |

## Cosa Consegnare

PDF con screenshot che dimostrano:
- [ ] I due file `azure-pipelines.yml` (container/ e function/)
- [ ] Pipeline A verde + due tag immagine nel registry (build ID + latest)
- [ ] Pipeline B verde + Function risponde all'URL
- [ ] Prova "a ogni modifica": cambio una riga → push → risultato in cloud aggiornato
- [ ] Spiegazione (2 righe): perché pipeline come YAML nel repo e perché credenziali solo in service connection

## Avvio Rapido

```bash
# 1. Clona il repo su Azure Repos (ExtraNet)
git clone <url-repo>
cd <repo>

# 2. Inizializza Terraform (una volta)
cd terraform
terraform init
terraform apply   # provisiona ACR, Function App, Service Connection, ecc.

# 3. Configura le variabili nelle pipeline YAML:
#    - acrName, imageName, azureSubscription (nome service connection)
#    - functionAppName, azureSubscription

# 4. Push su main → parte la pipeline pertinente per path
git add .
git commit -m "Initial commit"
git push origin main
```

## Risorse Utili

- [az acr build](https://learn.microsoft.com/cli/azure/acr#az-acr-build)
- [AzureCLI@2 task](https://learn.microsoft.com/azure/devops/pipelines/tasks/reference/azure-cli-v2)
- [AzureFunctionApp@2 task](https://learn.microsoft.com/azure/devops/pipelines/tasks/reference/azure-function-app-v2)
- [CI/CD per Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-how-to-azure-devops)
- [Workload Identity Federation](https://learn.microsoft.com/azure/active-directory/workload-identities-workload-identity-federation)
- [Flex Consumption Plan](https://learn.microsoft.com/azure/azure-functions/flex-consumption-plan)