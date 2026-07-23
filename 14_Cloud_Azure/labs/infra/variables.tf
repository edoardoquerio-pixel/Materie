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
