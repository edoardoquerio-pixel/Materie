variable "resource_group_name" {
  description = "Nome del Resource Group"
  type        = string
  default     = "rg-azure-e2e-lab"
}

variable "location" {
  description = "Regione Azure per tutte le risorse"
  type        = string
  default     = "polandcentral"
}

variable "suffix" {
  description = "Suffisso univoco per i nomi delle risorse (se vuoto viene generato randomicamente)"
  type        = string
  default     = ""
}

variable "python_version" {
  description = "Versione Python per Azure Functions"
  type        = string
  default     = "3.12"
}

variable "frontend_image_tag" {
  description = "Tag per l immagine Docker del frontend"
  type        = string
  default     = "v1"
}

variable "function_app_sku" {
  description = "SKU per il piano App Service della Function App (B1 richiesto per Always On + Timer)"
  type        = string
  default     = "B1"
}

variable "frontend_sku" {
  description = "SKU per il piano App Service del frontend"
  type        = string
  default     = "B1"
}

variable "cosmos_serverless" {
  description = "Abilita modalita serverless per Cosmos DB"
  type        = bool
  default     = true
}
