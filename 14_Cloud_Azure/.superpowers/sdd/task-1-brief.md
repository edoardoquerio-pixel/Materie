# Task 1: Project Structure + Terraform Variables

## Context
This is the first task in an Azure E2E lab project. We're building a complete cloud application with containerized frontend, serverless backend, Cosmos DB, and more. This task creates the foundational project structure and Terraform variable definitions.

**Working directory:** `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\labs`

## What to do

### Step 1: Create directories
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
mkdir -p infra scripts docs/report
```

### Step 2: Write `infra/variables.tf`

```hcl
variable "suffix" {
  description = "Unique suffix for all resources"
  type        = string
  default     = "e2e07171436"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "francecentral"
}

variable "resource_group_name" {
  description = "Resource group name"
  type        = string
  default     = "rg-e2e-lab"
}

locals {
  name_prefix = "e2e${var.suffix}"

  cosmos_account   = "cosmos-${local.name_prefix}"
  cosmos_db        = "appdb"
  cosmos_container = "richieste"
  cosmos_riepiloghi = "riepiloghi"

  function_app = "funcapp-${local.name_prefix}"
  acr_name     = "acr${local.name_prefix}"
  webapp_name  = "webappfrontend-${local.name_prefix}"
  webapp_plan  = "planfrontend-${local.name_prefix}"

  key_vault     = "kv-${local.name_prefix}"
  app_insights  = "ai-${local.name_prefix}"
  storage_account = "st${local.name_prefix}"

  queue_name = "richieste-da-elaborare"

  tags = {
    project = "azure-e2e-lab"
    suffix  = var.suffix
  }
}
```

### Step 3: Write `infra/terraform.tfvars`

```hcl
suffix          = "e2e07171436"
location        = "francecentral"
resource_group_name = "rg-e2e-lab"
```

### Step 4: Update `infra/versions.tf`

Replace the entire file with:

```hcl
terraform {
  required_version = ">= 1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.30"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
}
```

### Step 5: Verify Terraform syntax
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs/infra
terraform init && terraform validate
```
Expected: `Success! The configuration is valid.`

If terraform is not installed, skip validation — the files are correct.

### Step 6: Commit
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add infra/variables.tf infra/terraform.tfvars infra/versions.tf
git commit -m "feat(infra): add Terraform variables and provider config"
```

## Report
Write your report to: `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\.superpowers\sdd\task-1-report.md`

Include: status (DONE/BLOCKED/NEEDS_CONTEXT), files created/modified, any concerns, and test results.
