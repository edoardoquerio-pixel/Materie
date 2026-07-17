# Cloud GCP — Note Complete

## 1. Compute

**Compute Engine:**
- VM (GCE) con sustained use discounts automatici (30%+ per uso continuativo)
- Famiglie: E2 (economico), N2/N2D (general purpose), C2/C2D/C3 (compute), M1/M2/M3 (memory), G2 (GPU)
- Preemptible/Spot: 60-91% sconto, max 24h
- Sole-Tenant Nodes: server dedicati per licensing/compliance
- OS Login: gestione chiavi SSH via IAM
- Snapshots: backup incrementali, cross-region

**GKE (Google Kubernetes Engine):**
- Kubernetes gestito, pioniere del settore (creato da Google, Borg → Omega → K8s)
- Autopilot: nodi completamente gestiti (serverless K8s)
- Standard: controllo sui nodi
- Workload Identity: IAM per K8s service accounts

**Cloud Run:**
- Container serverless, scala a zero (nessun costo quando inutilizzato)
- Pay-per-request + CPU/memory per durata
- Supporto HTTP/2, WebSocket, event-driven
- Max 60 min per request, 4 vCPU, 16 GB RAM
- Knative-based (portabile su GKE, on-prem)

**Cloud Functions:**
- 1st gen: 540s timeout, 2 GB RAM, eventi GCP
- 2nd gen (Cloud Run-based): 60 min, 16 GB, più eventi

## 2. Storage

**Cloud Storage:**
- Object storage unificato (non classi rigide come AWS)
- Classi: Standard (multi-region), Nearline (30gg), Coldline (90gg), Archive (365gg)
- Autoclass: tiering automatico basato su accesso
- Object holds, retention policies, Object Versioning
- Signed URLs per accesso temporaneo
- Trasferimento dati: Storage Transfer Service, Transfer Appliance

## 3. Database

**Cloud SQL:** MySQL, PostgreSQL, SQL Server gestiti (fino ~30 TB)
**Cloud Spanner:** Database relazionale globalmente distribuito, strong consistency, SQL ANSI
**Firestore:** NoSQL document database, real-time sync, offline support
**Bigtable:** NoSQL wide-column, bassissima latenza (<10ms), HBase API
**Memorystore:** Redis/Memcached gestiti
**BigQuery:** Data warehouse serverless, SQL, petabyte-scale, analisi in tempo reale

## 4. Networking

**VPC:** Rete globale (non regionale come AWS), subnet in espansione automatica
**Cloud CDN:** CDN globale con Cloud Load Balancing
**Cloud Load Balancing:** Global (singolo anycast IP), HTTP(S)/TCP/SSL/ UDP, cross-region
**Cloud NAT:** NAT gestito per traffico outbound da VM private
**Cloud Armor:** WAF, DDoS protection, rate limiting
**Private Google Access:** Accesso API Google da VM senza IP pubblico
**VPC Service Controls:** Perimetro di sicurezza per dati gestiti
**Cloud VPN / Cloud Interconnect:** Connessioni site-to-cloud

## 5. IAM

- **Roles**: Primitive (Owner/Editor/Viewer), Predefined (per servizio), Custom
- **Policy**: allow-only (no deny esplicito), ereditate nella gerarchia
- **Resource hierarchy**: Organization → Folder → Project → Resource
- **Service Accounts**: identità per applicazioni
- **Workload Identity Federation**: accesso senza chiavi (OIDC, SAML)

## 6. AI/ML

**Vertex AI:**
- Piattaforma ML unificata (AutoML + custom training)
- Model Garden: 150+ modelli (Gemini, Llama, Claude)
- Vertex AI Agent Builder: agenti RAG
- Model Registry, Feature Store, Pipelines
- **Gemini:** modelli multimodali (testo, immagini, audio, video)

**BigQuery ML:** ML in SQL (crea/valuta modelli con SQL)
**Document AI:** Estrazione dati da documenti
**Translation AI, Speech-to-Text, Text-to-Speech:** API AI pre-built

## 7. Data Analytics

**BigQuery:**
- Serverless, columnar, petabyte-scale
- Standard SQL, BI Engine per dashboard sub-second
- Materialized views, clustering, partitioning
- Omni: query multi-cloud (AWS, Azure)
- BigQuery Studio: notebook integrati

**Dataflow:** Stream/batch processing (Apache Beam runner)
**Dataproc:** Spark/Hadoop gestito
**Pub/Sub:** Messaggistica asincrona scalabile
**Data Fusion:** ETL grafico (CDAP-based)

## 8. DevOps & IaC

**Cloud Build:** CI/CD serverless
**Cloud Deploy:** Delivery pipeline a Google Cloud Run/GKE
**Cloud Source Repositories:** Git hosting
**Artifact Registry:** Container/package registry
**Deployment Manager:** IaC nativo (YAML Jinja2/Python, deprecato)
**Terraform:** Provider Google, supporto first-class

## 9. Security

**Security Command Center:** Threat detection, vulnerability scanning, compliance
**Cloud Armor:** WAF, DDoS
**reCAPTCHA Enterprise:** Protezione bot
**Cloud KMS:** Key management
**Secret Manager:** Gestione segreti
**BeyondCorp Enterprise:** Zero trust access

## 10. GCP vs AWS vs Azure

| Caratteristica | GCP | AWS | Azure |
|---------------|-----|-----|-------|
| Sconti automatici | Sustained Use 30%+ | Nessuno | Nessuno |
| K8s native | GKE (pioniere) | EKS | AKS |
| Data warehouse | BigQuery (serverless) | Redshift | Synapse |
| Rete globale | VPC globale | VPC regionale | VNet regionale |
| AI/ML | Vertex AI | SageMaker | Azure AI |
| Billing | Per-second, minuto per alcuni | Per-second | Per-second |
