# Ottimizzazioni da Applicare al Progetto Azure E2E Lab

## Data: 2026-07-27

## Sommario
Questo documento contiene tutte le modifiche necessarie per ottimizzare il progetto secondo i requisiti dei lab 23, 24 e 25.

---

## 1. PRIORITÀ ALTA - Sicurezza: Spostare Connection Strings in Key Vault

### File: infra/main.tf

#### 1.1 Aggiungere il segreto storage nel Key Vault (dopo riga 194)

```hcl
resource "azurerm_key_vault_secret" "storage_conn" {
  name         = "storage-conn"
  value        = azurerm_storage_account.main.primary_connection_string
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.deployer]
}
```

#### 1.2 Modificare gli app_settings della Function App (righe 152-157)

RIMUOVERE:
```hcl
  app_settings = {
    COSMOS_CONNECTION_STRING = azurerm_cosmosdb_account.main.primary_sql_connection_string
    QUEUE_STORAGE_CONNECTION = azurerm_storage_account.main.primary_connection_string
    AzureWebJobsStorage      = azurerm_storage_account.main.primary_connection_string
    FUNCTIONS_WORKER_RUNTIME = "python"
  }
```

SOSTITUIRE CON:
```hcl
  app_settings = {
    COSMOS_CONNECTION_STRING = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.main.vault_uri}secrets/${azurerm_key_vault_secret.cosmos_conn.name}/)"
    QUEUE_STORAGE_CONNECTION = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.main.vault_uri}secrets/${azurerm_key_vault_secret.storage_conn.name}/)"
    AzureWebJobsStorage      = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.main.vault_uri}secrets/${azurerm_key_vault_secret.storage_conn.name}/)"
    FUNCTIONS_WORKER_RUNTIME = "python"
  }

  depends_on = [
    azurerm_key_vault_access_policy.function_app,
    azurerm_key_vault_secret.cosmos_conn,
    azurerm_key_vault_secret.storage_conn
  ]
```

---

## 2. PRIORITÀ ALTA - Sicurezza: Restringere CORS

### File: infra/main.tf (righe 147-149)

RIMUOVERE:
```hcl
    cors {
      allowed_origins = ["*"]
    }
```

SOSTITUIRE CON:
```hcl
    cors {
      allowed_origins = ["https://${azurerm_linux_web_app.frontend.default_hostname}"]
    }
```

---

## 3. PRIORITÀ ALTA - Configurazione: Aggiungere Always On

### File: infra/main.tf (dopo riga 138, dentro site_config)

AGGIUNGERE dopo site_config:
```hcl
  site_config {
    always_on = true

    application_stack {
      python_version = "3.11"
    }
```

---

## 4. PRIORITÀ MEDIA - Sicurezza: Disabilitare Admin ACR e usare Managed Identity

### File: infra/main.tf

#### 4.1 Modificare ACR (riga 83)

RIMUOVERE:
```hcl
  admin_enabled       = true
```

SOSTITUIRE CON:
```hcl
  admin_enabled       = false
```

#### 4.2 Aggiungere Managed Identity al Frontend Web App (dopo riga 102)

AGGIUNGERE:
```hcl
  identity {
    type = "SystemAssigned"
  }
```

#### 4.3 Modificare site_config del Frontend (righe 104-110)

RIMUOVERE:
```hcl
  site_config {
    application_stack {
      docker_image_name   = "frontend:v1"
      docker_registry_url = "https://${azurerm_container_registry.main.login_server}"
      docker_registry_username = azurerm_container_registry.main.admin_username
      docker_registry_password = azurerm_container_registry.main.admin_password
    }
  }
```

SOSTITUIRE CON:
```hcl
  site_config {
    application_stack {
      docker_image_name   = "frontend:v1"
      docker_registry_url = "https://${azurerm_container_registry.main.login_server}"
    }

    acr_use_managed_identity_credentials = true
  }
```

#### 4.4 Aggiungere Role Assignment per ACR Pull (alla fine del file)

AGGIUNGERE:
```hcl
resource "azurerm_role_assignment" "acr_pull_frontend" {
  scope                = azurerm_container_registry.main.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_linux_web_app.frontend.identity[0].principal_id

  depends_on = [azurerm_linux_web_app.frontend]
}
```

---

## 5. PRIORITÀ MEDIA - Dipendenze: Aggiornare requirements.txt

### File: backend/requirements.txt

CONTENUTO ATTUALE:
```
azure-functions
```

SOSTITUIRE CON:
```
azure-functions
azure-cosmos
azure-storage-queue
```

---

## 6. PRIORITÀ MEDIA - Gestione Errori: Migliorare function Riepilogo

### File: backend/function_app.py (righe 200-231)

SOSTITUIRE la funzione riepilogo con versione che include try-catch per gestione errori robusta.

---

## Ordine di Applicazione delle Modifiche

1. Aggiornare backend/requirements.txt (punto 5)
2. Aggiungere gestione errori in backend/function_app.py (punto 6)
3. Modificare infra/main.tf (punti 1-4)

---

## Verifica Post-Applicazione

Dopo aver applicato le modifiche:

1. Terraform Plan
   cd infra && terraform plan -out=tfplan

2. Terraform Apply
   terraform apply tfplan

3. Verificare Key Vault References
   - Portale Azure → Function App → Environment Variables
   - Le tre variabili devono mostrare stato "Resolved"

4. Testare il Frontend
   - Inviare richiesta sincrona (201)
   - Inviare richiesta asincrona (202)
   - Verificare dati su Cosmos DB

5. Verificare il Timer
   - Attendere 2 minuti
   - Controllare container riepiloghi su Cosmos DB

6. Verificare Application Insights
   - Query: requests | where timestamp > ago(1h)
   - Query: traces | where timestamp > ago(1h) and message contains "Riepilogo"

---

## Checklist Finale

- [ ] Connection strings spostate in Key Vault
- [ ] CORS ristretto al frontend specifico
- [ ] Always On attivato per piano B1
- [ ] Admin ACR disabilitato
- [ ] Managed Identity configurata per frontend
- [ ] Role assignment AcrPull assegnato
- [ ] requirements.txt aggiornato
- [ ] Gestione errori aggiunta
- [ ] Terraform plan eseguito
- [ ] Terraform apply completato
- [ ] Key Vault references risolti
- [ ] Frontend funzionante
- [ ] Timer scatta ogni 2 minuti
- [ ] Log visibili in Application Insights

---

## Note Importanti

Dopo terraform apply:

1. Riavviare la Function App:
   az functionapp restart -g <resource-group-name> -n funcapp-e2e07171436

2. Attendere 2 minuti per propagazione permessi

3. Se errori 500: normale nei primi minuti durante propagazione

---

## Benefici delle Ottimizzazioni

SICUREZZA:
- Connection strings non più in chiaro
- CORS ristretto
- ACR senza admin credentials

CONFORMITÀ LAB 24:
- Application Insights collegato
- Key Vault con segreti
- Managed Identity configurata
- Key Vault References attivi

CONFORMITÀ LAB 25:
- Timer con Always On
- Gestione errori robusta

BEST PRACTICES AZURE:
- Uso Managed Identity
- Secrets centralizzati in Key Vault
- Piano B1 ottimizzato
