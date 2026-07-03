# 23_Project_Work_e_Laboratori

## 📋 Panoramica

Project work enterprise simulato **(TP_Group)** — convergenza e potenziamento servizi IT dopo la fusione tra Thema Consulting e Pro Studio. Assegnato a 9 gruppi di lavoro con budget 520k€ + IVA. Docente: Luca Robaldo. Copre assessment, progettazione, offerta tecnico/economica su infrastruttura IT integrata.

## 📚 Indice degli argomenti

### 1. Scenario di Riferimento
- **Thema Consulting** (Torino, 30 persone): Data center on-prem con 2 host VMware, SAN NetApp 24TB, cluster HPC 8 nodi (crash test automotive), servizio Pondus (ottimizzazione pesi), Fortigate FG-60F
- **Pro Studio srl** (Torino, 20 persone): Senza infrastruttura IT propria, servizi cloud, calcolo strutturale su sistemi clienti, sede in affitto
- **Unione → TP Group**: Integrazione e convergenza dei sistemi informativi

### 2. Assessment — Stato dell'Arte
- **Datacenter Thema**: 2 rack saturi, hypervisor VMware, NAS QNAP 32TB per backup
- **Virtualizzazione**: 2 host VMware on-prem (Thema) / nessuno (Pro Studio)
- **Backup**: On-prem su NAS QNAP (Thema) / on GCP (Pro Studio)
- **Firewall**: Fortigate FG-60F (Thema) / cloud (Pro Studio)
- **HPC**: 8 nodi fisici Linux con Infiniband + 1 frontend VM (Thema)
- **UPS e Condizionamento**: Presenti in Thema, assenti in Pro Studio

### 3. Vincoli e Requisiti
- **Vincoli tecnologici**: Sistemi esistenti da integrare, HPC da preservare
- **Vincoli logistici**: Due sedi, personale distribuito
- **Obiettivi**: Convergenza infrastrutture, disaster recovery, scalabilità, sicurezza
- **Budget**: 520.000€ + IVA

### 4. Offerta Tecnico/Economica
- **Requisiti**: Documento di offerta tecnico/economica
- **Criteri di valutazione**: Qualità tecnica, costi, timeline, innovazione
- **Costi indicativi risorse**: Stima costi HW, SW, servizi cloud, consulenza

### 5. Organizzazione del Lavoro
- **9 gruppi di lavoro**: Ogni gruppo si occupa di un'area specifica (rete, security, HPC, app, cloud, backup, ecc.)
- **Agents**: 9 agenti specializzati in `TP_Group/agents/` (Assessment, Network, Security, HPC, App, Cloud, Backup, Bid, PM)
- **KANBAN.md**: Task organizzati per delivery order
- **Deliverable tracking**: Dipendenze e milestone tra gruppi

### 6. Aree di Intervento
- **Assessment**: Mappatura attuale infrastrutture Thema + Pro Studio
- **Network**: Interconnessione sedi, VPN, VLAN, routing
- **Security**: Firewall perimetrale, segmentazione, IAM, compliance
- **HPC**: Cluster computing on-prem/cloud, job scheduling
- **App**: Migrazione/refactoring applicazioni, Pondus
- **Cloud**: IaaS/PaaS su cloud provider, hybrid cloud
- **Backup/DR**: BC/DR strategy, backup centralizzato, off-site
- **Bid**: Offerta economica, giustificativi di prezzo
- **PM**: Project management, risk management, reporting

## ⚡ Punti Chiave

- Budget **520k€ + IVA** — va motivata ogni voce di spesa
- **Assessment iniziale** è fondamentale per capire punto di partenza
- La fusione richiede **convergenza** non solo tecnica ma anche organizzativa
- L'**HPC** (8 nodi Infiniband) è asset critico per Thema — va preservato e possibilmente esteso
- **Pro Studio** è cloud-native — la convergenza richiederà decisioni su hybrid cloud
- Gruppi di lavoro **inter-dipendenti** — il PM deve coordinare le consegne
- I **9 agenti specializzati** coprono tutti gli aspetti tecnici ed economici

## 📎 Risorse Collegate

- **TP_Group/**: KANBAN.md, agents/, deliverable tracking
- **02_Esercizi/**: —
- **03_Progetti/**: —
- **Materie collegate**: Tutte le materie tecniche (project work trasversale)
