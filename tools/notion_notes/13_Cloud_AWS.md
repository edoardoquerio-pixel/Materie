# 13_Cloud_AWS

## 📋 Panoramica

Cloud computing su Amazon Web Services. Piattaforma cloud leader di mercato con oltre 200 servizi tra compute, storage, database, networking, AI/ML e sicurezza.

> ⚠️ **Nessun materiale didattico presente** in `01_Materiale/`. Questa nota è un placeholder da integrare.

## 📚 Indice degli argomenti (attesi dal syllabus)

### 1. Fondamenti AWS
- Global infrastructure: Regions, AZs, Edge Locations
- AWS Management Console, CLI, SDK
- IAM: Users, Groups, Roles, Policies (JSON)

### 2. Compute
- **EC2**: Tipi di istanza, AMI, security groups, EBS, ELB, Auto Scaling
- **Lambda**: Serverless, trigger, runtime, billing per invocazione
- **ECS / EKS**: Container orchestration (Fargate vs EC2)

### 3. Storage
- **S3**: Bucket, classi storage, lifecycle, versioning, replication
- **EBS**: Volumi, snapshot, encryption
- **EFS**: File system condiviso NFS

### 4. Database
- **RDS**: MySQL, PostgreSQL, MariaDB, SQL Server, Oracle
- **DynamoDB**: NoSQL key-value/document
- **ElastiCache**: Redis, Memcached

### 5. Networking
- **VPC**: Subnet, route tables, Internet Gateway, NAT Gateway
- **Security Groups vs NACL**
- **CloudFront**: CDN
- **Route 53**: DNS

### 6. Sicurezza e Monitoring
- **CloudWatch**: Logs, metrics, alarms
- **CloudTrail**: Audit API calls
- **AWS Shield / WAF**: Protezione DDoS e firewall applicativo
- **KMS**: Key management, encryption

## ⚡ Punti Chiave

- AWS ha il **market share maggiore** nel cloud (≈32% Q1 2025)
- **IAM** è il fondamento della sicurezza — seguire il principio del minimo privilegio
- **S3** è storage object, non file system (consistenza read-after-write)
- **Lambda** si paga per invocazione e durata (arrotondato a 1ms)
- Tutti i servizi possono essere gestiti via **Infrastructure as Code** (CloudFormation/Terraform)

## 📎 Risorse Collegate

- **02_Esercizi/**: —
- **03_Progetti/**: —
- **Materie collegate**: `23_Project_Work_e_Laboratori`, `19_Virtualizzazione`, `14_Cloud_Azure`, `15_Cloud_GCP`
