variable "resource_group_name" {
  description = "Nome del Resource Group"
  type        = string
  default     = "collaboration1"
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
