# Cloud AWS — Note Complete

## 1. Compute

**EC2 (Elastic Compute Cloud):**
- VM con oltre 750 tipi di istanza
- Famiglie: A (arm), T (burst), M (general purpose), C (compute), R/X (memory), P/G (GPU)
- Acquisto: On-Demand, Reserved (1-3y, 72% sconto), Spot (90% sconto, interrompibili), Savings Plans
- EBS: volumi block storage (gp3, io2, st1, sc1)

**Lambda (Serverless):**
- Fino a 15 minuti di esecuzione, 10 GB RAM
- Trigger: S3, DynamoDB, API Gateway, SQS, EventBridge
- Pay-per-invocation + durata (1ms granularità)

**ECS / EKS:**
- ECS: container orchestrator AWS-native
- EKS: Kubernetes gestito (control plane AWS, nodi cliente)
- Fargate: serverless container (no nodi da gestire)

## 2. Storage

**S3 (Simple Storage Service):**
- Object storage, 99.999999999% durabilità (11 9's)
- Classi: Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier (minuti/ore), Glacier Deep Archive (12h)
- Versioning, Lifecycle Policies, Cross-Region Replication
- S3 Select / S3 Object Lambda

**EFS:** File system NFS gestito, multi-AZ
**FSx:** File system gestiti (Windows FS, Lustre per HPC)

## 3. Database

**RDS:** MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora
**Aurora:** Compatibile MySQL/PostgreSQL, throughput 5x MySQL, storage auto-scaling
**DynamoDB:** NoSQL key-value/document, single-digit ms latency, autoscaling, DAX cache
**Redshift:** Data warehouse petabyte-scale, columnar storage, concurrency scaling
**ElastiCache:** Redis / Memcached gestiti

## 4. Networking

**VPC:** Virtual Private Cloud, subnet (public/private), route tables, Internet Gateway, NAT Gateway
**Security Groups:** stateful firewall a livello di istanza
**NACL:** stateless firewall a livello di subnet
**Route 53:** DNS gestito, routing policies (simple, weighted, latency, failover, geolocation)
**CloudFront:** CDN globale, edge locations, Lambda@Edge
**ELB:** ALB (HTTP/HTTPS), NLB (TCP/UDP), GLB (GWLB)

## 5. IAM (Identity and Access Management)

**Componenti:**
- Users: identità per persone
- Groups: insieme di utenti con stessi permessi
- Roles: identità per servizi AWS (assumibile)
- Policies: JSON che definisce permessi (Allow/Deny, Effect + Action + Resource)
- **Least privilege**: concedere solo i permessi necessari

**Best practices:**
- Root account solo per operazioni critiche
- MFA obbligatorio
- IAM Roles per EC2 (non access keys sulle istanze)
- Policy conditions per restrizioni contestuali (IP, tempo, SSL)

## 6. Serverless & Application Integration

**API Gateway:** API REST/HTTP/WebSocket, throttle, caching, auth (Cognito, Lambda authorizer)
**SQS:** Code di messaggi (Standard: at-least-once, FIFO: exactly-once)
**SNS:** Pub/sub messaging, push a email/SMS/HTTP/Lambda/SQS
**Step Functions:** Workflow visuali, stati (Task, Choice, Parallel, Map, Wait)
**EventBridge:** Event bus per eventi SaaS e AWS services

## 7. Infrastruttura come Codice

**CloudFormation:** Template JSON/YAML, stack, change sets, drift detection
**CDK (Cloud Development Kit):** Infrastruttura in TypeScript/Python/Java/C#/.NET
**Elastic Beanstalk:** PaaS per deploy automatico (auto-scaling, health monitoring)

## 8. Well-Architected Framework

1. **Operational Excellence**: operations as code, documentazione, game days
2. **Security**: IAM, encryption at rest/in transit, detective controls
3. **Reliability**: backup, DR, fault tolerance, auto-scaling
4. **Performance Efficiency**: right-size, serverless first, caching
5. **Cost Optimization**: Reserved/Spot, lifecycle policies, FinOps
6. **Sustainability**: efficienza energetica, riduzione impatto

## 9. Servizi di Supporto

| Servizio | Funzione |
|----------|----------|
| CloudWatch | Metriche, log, alarm, dashboard |
| CloudTrail | Audit API calls, governance |
| Trusted Advisor | Best practice recommendations |
| Config | Resource compliance, configuration history |
| Systems Manager | Patch management, automation, parameter store |
| KMS | Gestione chiavi crittografia |
| WAF & Shield | Web application firewall, DDoS protection |
