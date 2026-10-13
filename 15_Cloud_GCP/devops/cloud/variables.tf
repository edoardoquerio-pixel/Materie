variable "project_id" {
  description = "ID del progetto GCP in cui creare le risorse."
  type        = string
}

variable "region" {
  description = "Regione GCP per le risorse e il bucket dei documenti."
  type        = string
  default     = "europe-west6"
}

variable "resource_prefix" {
  description = "Prefisso da anteporre al nome delle risorse."
  type        = string

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9-]{0,51}[a-z0-9]$", var.resource_prefix))
    error_message = "Il prefisso deve contenere da 2 a 53 caratteri minuscoli, numeri o trattini e iniziare e terminare con una lettera o un numero."
  }
}
