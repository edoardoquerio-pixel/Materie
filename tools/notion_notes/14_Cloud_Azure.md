# [14] Cloud Azure

## 📋 Panoramica

Materia dedicata a Microsoft Azure con copertura completa: architettura, identità/governance, reti virtuali, compute (VM, App Service, Functions, Container/AKS), storage, AI/Foundry e security/BC/DR. 18 moduli progressivi con slide.

**Tecnologie**: Microsoft Azure, Entra ID, Virtual Network, VM, App Service, Functions, AKS, Blob Storage, AI Foundry, Defender, Key Vault, Backup/DR

---

## 📚 Indice degli argomenti

### 1. Introduzione ad Azure

- **Cos'è il cloud computing**: IaaS, PaaS, SaaS
- **Modelli di deployment**: pubblico, privato, ibrido
- **Regioni e zone di disponibilità**: replicazione geografica, residenza dati
- **SLA**: 99.9% → 99.999% a seconda della configurazione

### 2. Architettura e Strumenti di Accesso (2-3)

- **Azure Portal**: GUI web
- **Azure CLI / PowerShell**: automazione e scripting
- **Azure Resource Manager (ARM)**: API unificata per provisioning
- **Azure Arc**: gestione risorse on-premise e multi-cloud
- **Blueprint**: template di conformità

### 3. Identity e Governance (4-5)

- **Microsoft Entra ID** (ex Azure AD): directory tenant, SSO, MFA
- **RBAC** (Role-Based Access Control): ruoli, scope, azioni consentite
- **Policy**: regole di governance per risorse
- **Management Groups**: gerarchia di sottoscrizioni
- **Privileged Identity Management (PIM)**: accesso JIT a ruoli privilegiati

### 4. Reti su Azure (6-8)

- **Virtual Network (VNet)**: isolamento rete, addressing, subnets
- **Peering VNet**: connessione tra VNet (stessa regione o cross-region)
- **VPN Gateway**: sito-sito, punto-sito
- **Azure DNS**: risoluzione nomi
- **Load Balancer**: pubblico/interno, livello 4
- **Application Gateway**: WAF, routing livello 7
- **Azure Front Door / Traffic Manager**: routing globale

### 5. Compute: VM, App Service, Functions (9-12)

- **Virtual Machines**: IaaS, immagini, scaling set, dischi (managed/unmanaged)
- **App Service**: PaaS per web app, auto-scaling, slot deployment
- **Azure Functions**: serverless, trigger (HTTP, timer, queue), Durable Functions
- **Container Instances / AKS**: container PaaS / Kubernetes orchestrato
- **Opzioni scaling**: verticale (VM più grande) vs orizzontale (più istanze)

### 6. Storage e Dati (13-14, 16)

- **Blob Storage**: dati non strutturati (hot/cool/archive tier)
- **File Storage**: condivisioni SMB, Azure File Sync
- **Disk Storage**: SSD/HDD managed per VM
- **Sicurezza storage**: crittografia lato server/ client, SAS tokens, firewall
- **Database gestiti**:
  - **Azure SQL**: SQL Server managed
  - **Cosmos DB**: NoSQL globale, multi-model (document, graph, key-value, column-family)
  - **Data Integration**: Data Factory, Synapse Analytics

### 7. AI su Azure (15)

- **Azure AI Foundry**: portale per modelli AI (OpenAI, vision, speech)
- **AI Services**: Vision, Language, Speech, Decision
- **GitHub Copilot**: AI pair programmer (parte del modulo)
- **Cognitive Search**: ricerca semantica con AI enrichment

### 8. Security, Reliability, BC/DR (17-18)

- **Microsoft Defender for Cloud**: security posture, vulnerability assessment
- **Key Vault**: gestione di secret, chiavi, certificati
- **Azure Backup**: backup di VM, file, database
- **Disaster Recovery**: Site Recovery per failover regionale
- **Business Continuity**: RPO, RTO, SLA planning

---

## ⚡ Punti Chiave

1. **Tutto in Azure è un Resource Group**: raggruppa risorse per ciclo di vita
2. **RBAC è il metodo primario di autorizzazione**: minimo privilegio sempre
3. **Reti**: VNet sono isolate di default — peering per connetterle
4. **Costi**: Prestare attenzione ai tier di storage, VM dimensionamento, egress
5. **Sicurezza**: Key Vault per secret, Defender per posture, MFA sempre
6. **Backup non è DR**: backup protegge da cancellazione, DR da disastro regionale

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Laboratori Azure
- **03_Progetti/** — Progetti con Azure Functions v2 (Python)
