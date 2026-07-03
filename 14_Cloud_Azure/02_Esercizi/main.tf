terraform {
    required_version = ">= 1.6.0"

    required_providers {
        azurerm = {
            source  = "hashicorp/azurerm"
            version = "~> 4.0"
            }
    }


    backend "local" {
        path = "terraform.tfstate"
    }
}

provider "azurerm" {
    features {}
}
# unica risorsa: un Resource Group.
resource "azurerm_resource_group" "rg" {
    name     = var.resource_group_name
    location = var.location
}

resource "azurerm_virtual_network" "vn" {
    name                = "vnet-minimal"
    resource_group_name = azurerm_resource_group.rg.name
    location            = azurerm_resource_group.rg.location
    address_space       = ["10.0.0.0/16"]
}
