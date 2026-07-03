# 15_Cloud_GCP

## 📋 Panoramica

Cloud computing su Google Cloud Platform. Suite di servizi cloud con punti di forza in data analytics, AI/ML, Kubernetes (GKE), networking globale (Andromeda) e serverless.

> ⚠️ **Nessun materiale didattico presente** in `01_Materiale/`. Questa nota è un placeholder da integrare.

## 📚 Indice degli argomenti (attesi dal syllabus)

### 1. Fondamenti GCP
- Regions, Zones, Global resources
- Gerarchia risorse: Organization → Folder → Project → Resources
- GCP Console, Cloud Shell, Cloud SDK (gcloud), Client Libraries

### 2. Identità e Sicurezza
- **Cloud IAM**: Roles (primitive/predefined/custom), Service Accounts, Policy
- **Cloud KMS**: Key management, CMEK, CSEK
- **Security Command Center**: Remediation e vulnerability scanning
- **VPC Service Controls**: Perimeter security

### 3. Compute
- **Compute Engine**: VM, machine types, sole-tenant nodes, preemptible/spot
- **GKE (Google Kubernetes Engine)**: Managed K8s, Autopilot vs Standard, Workload Identity
- **Cloud Run**: Container serverless (Knative-based)
- **Cloud Functions**: Function-as-a-Service (Gen 1 e Gen 2)
- **App Engine**: PaaS tradizionale (standard/flexible)

### 4. Storage e Database
- **Cloud Storage**: Bucket, classi (Standard, Nearline, Coldline, Archive), object versioning
- **Cloud SQL**: MySQL, PostgreSQL, SQL Server managed
- **Cloud Spanner**: DB relazionale orizzontalmente scalabile
- **Firestore / Bigtable**: NoSQL document/wide-column
- **BigQuery**: Data warehouse serverless (SQL analytics su petabyte)

### 5. Networking
- **VPC**: Subnet mode (auto/custom), firewall rules, Cloud NAT
- **Cloud Interconnect / VPN**: Hybrid connectivity
- **Cloud CDN**: Content delivery
- **Cloud DNS**: Managed DNS
- **Cloud Load Balancing**: Multi-region, anycast IP

### 6. AI/ML e Dati
- **Vertex AI**: ML piattaforma unificata (AutoML, custom training, predictions)
- **Dataflow**: Stream/batch processing (Apache Beam)
- **Dataproc**: Managed Hadoop/Spark
- **Pub/Sub**: Messaggistica asincrona

## ⚡ Punti Chiave

- GCP è leader in **data analytics e AI/ML** (BigQuery, Vertex AI)
- **GKE** è il managed Kubernetes più maturo dei tre cloud
- **Cloud Run** esegue container serverless con fatturazione al secondo
- La gerarchia **Organization → Folder → Project → Resources** è unica di GCP
- **BigQuery** separa storage e compute — paga per storage e query eseguite

## 📎 Risorse Collegate

- **02_Esercizi/**: —
- **03_Progetti/**: —
- **Materie collegate**: `23_Project_Work_e_Laboratori`, `14_Cloud_Azure`, `13_Cloud_AWS`, `20_Data_Analytics_Visualization`
