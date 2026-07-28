# Task 5: Deployment Scripts

## Context
This is the fifth task in an Azure E2E lab project. Tasks 1-4 created all application code. This task creates deployment helper scripts.

**Working directory:** `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\labs`

## What to do

### Step 1: Write `scripts/deploy-acr.sh`

```bash
#!/bin/bash
# Build and push frontend image to Azure Container Registry
# Usage: ./scripts/deploy-acr.sh <resource-group> <acr-name>

set -euo pipefail

RG="${1:?Usage: $0 <resource-group> <acr-name>}"
ACR="${2:?Usage: $0 <resource-group> <acr-name>}"

echo "=== Logging into ACR ==="
az acr login -n "$ACR"

echo "=== Building and pushing image (cloud build) ==="
az acr build -r "$ACR" -t frontend:v1 ../frontend/

echo "=== Done! Image pushed to ${ACR}.azurecr.io/frontend:v1 ==="
```

### Step 2: Write `scripts/deploy-frontend.sh`

```bash
#!/bin/bash
# Deploy frontend to App Service for Containers
# Usage: ./scripts/deploy-frontend.sh <resource-group> <app-name> <acr-name>

set -euo pipefail

RG="${1:?Usage: $0 <resource-group> <app-name> <acr-name>}"
APP="${2:?Usage: $0 <resource-group> <app-name> <acr-name>}"
ACR="${3:?Usage: $0 <resource-group> <app-name> <acr-name>}"

echo "=== Updating App Service to pull new image ==="
az webapp config container set \
  -g "$RG" \
  -n "$APP" \
  --docker-custom-image-name "${ACR}.azurecr.io/frontend:v1" \
  --docker-registry-server-url "https://${ACR}.azurecr.io" \
  --docker-registry-server-user "$(az acr credential show -n "$ACR" --query username -o tsv)" \
  --docker-registry-server-password "$(az acr credential show -n "$ACR" --query 'passwords[0].value' -o tsv)"

echo "=== Restarting App Service ==="
az webapp restart -g "$RG" -n "$APP"

echo "=== Done! Frontend deployed at: https://${APP}.azurewebsites.net ==="
```

### Step 3: Write `scripts/setup-queue.sh`

```bash
#!/bin/bash
# Create the Storage Queue for decoupled processing
# Usage: ./scripts/setup-queue.sh <storage-account-name>

set -euo pipefail

SA="${1:?Usage: $0 <storage-account-name>}"

echo "=== Creating queue 'richieste-da-elaborare' ==="
az storage queue create \
  --name "richieste-da-elaborare" \
  --account-name "$SA" \
  --auth-mode login

echo "=== Done! Queue created in storage account ${SA} ==="
```

### Step 4: Make scripts executable
```bash
chmod +x /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs/scripts/*.sh
```

### Step 5: Commit
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add scripts/
git commit -m "feat(scripts): add deployment scripts for ACR, frontend, and queue"
```

## Report
Write your report to: `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\.superpowers\sdd\task-5-report.md`

Include: status (DONE/BLOCKED/NEEDS_CONTEXT), files created/modified, any concerns.
