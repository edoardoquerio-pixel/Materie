# Piano di Migrazione Pondus — On-Prem → Azure PaaS

## Fasi

### Fase 0 — Analisi (Settimane 1-2)

| # | Attività | Responsabile | Durata |
|---|---|---|---|
| P0.1 | Analisi compatibilità codice C# (.NET Framework → .NET 8/10) | Sviluppatore | 3 giorni |
| P0.2 | Verifica dipendenze (librerie IIS, COM, componenti legacy) | Sviluppatore | 2 giorni |
| P0.3 | Verifica compatibilità MS SQL → Azure SQL (database compatibility level) | Sistemista | 1 giorno |
| P0.4 | Decisione: App Service Windows vs Linux vs VM IaaS | Team | 1 giorno |

### Fase 1 — Preparazione (Settimane 3-4)

| # | Attività | Responsabile | Durata |
|---|---|---|---|
| P1.1 | Provisioning Azure App Service Plan P1v3 (Windows) | Sistemista | 1 ora |
| P1.2 | Provisioning Azure SQL Database S2 | Sistemista | 1 ora |
| P1.3 | Esportazione database MS SQL → bacpac | Sistemista | 1 giorno |
| P1.4 | Import bacpac su Azure SQL | Sistemista | 1 giorno |
| P1.5 | Deploy codice Pondus su slot STAGING | Sviluppatore | 2 giorni |
| P1.6 | Configurazione Entra ID Easy Auth | Sistemista | 1 giorno |
| P1.7 | Setup Azure DevOps pipeline (build + deploy) | Sviluppatore | 2 giorni |

### Fase 2 — Migrazione (Settimana 5)

| # | Attività | Responsabile | Durata |
|---|---|---|---|
| P2.1 | Test funzionali su STAGING | Sviluppatore + Utenti pilota | 3 giorni |
| P2.2 | Migrazione dati finali (delta) | Sistemista | 4 ore |
| P2.3 | Swap slot STAGING → PROD | Sistemista | 15 min |
| P2.4 | Configurazione DNS (pondus.tpgroup.it → App Service) | Sistemista | 1 ora |
| P2.5 | Abilitazione backup automatico (SQL PITR + App Service) | Sistemista | 1 ora |

### Fase 3 — Rollback (se necessario)

| # | Attività | Tempo |
|---|---|---|
| P3.1 | Swap PROD → STAGING (ritorno a versione precedente) | 15 min |
| P3.2 | Puntamento DNS a IP on-prem originale | 1 ora |
| P3.3 | Ripristino DB da bacpac locale | 2 ore |

## CI/CD Pipeline (Azure DevOps)

```yaml
trigger:
  branches:
    include:
      - main
      - develop

stages:
  - stage: Build
    jobs:
      - job: Build
        pool:
          vmImage: 'windows-latest'
        steps:
          - task: DotNetCoreCLI@2
            inputs:
              command: 'restore'
          - task: DotNetCoreCLI@2
            inputs:
              command: 'build'
          - task: DotNetCoreCLI@2
            inputs:
              command: 'publish'
              publishWebProjects: true
          - task: PublishBuildArtifacts@1

  - stage: Deploy_STAGING
    jobs:
      - deployment: Deploy
        environment: 'staging'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureWebApp@1
                  inputs:
                    azureSubscription: 'Azure-TPGroup'
                    appName: 'app-tpgroup-pondus-westeu'
                    slotName: 'staging'
                    package: '$(Build.ArtifactStagingDirectory)/**/*.zip'

  - stage: Deploy_PROD
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: Deploy
        environment: 'production'
        strategy:
          runOnce:
            deploy:
              steps:
                - task: AzureAppServiceManage@0
                  inputs:
                    action: 'Swap Slots'
                    appName: 'app-tpgroup-pondus-westeu'
                    sourceSlot: 'staging'
                    destinationSlot: 'production'
```

## Costi aggiuntivi migrazione Pondus

| Voce | Una tantum | Note |
|---|---|---|
| Analisi compatibilità codice | € 2.000 | 4 giorni sviluppatore |
| Adattamento codice per Azure (se necessario) | € 5.000 – 15.000 | Variabile in base a modifiche necessarie |
| Setup iniziale Azure + DevOps | € 1.500 | Sistemista |
| Test + validazione | € 2.000 | Test utenti pilota |
| **Range costo migrazione** | **€ 8.500 – 20.500** | |
