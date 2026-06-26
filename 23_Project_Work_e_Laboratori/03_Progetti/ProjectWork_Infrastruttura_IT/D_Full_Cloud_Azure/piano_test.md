# Piano di Test — Variante D (Full Cloud Azure)

> **Documento:** Piano di Test per la Variante D — infrastruttura TP Group su Microsoft Azure
> **Versione:** 1.0
> **Stato:** Bozza

## Premessa

### Scopo
Il presente piano di test definisce le procedure di verifica per accertare il corretto funzionamento dell'infrastruttura TP Group sulla Variante D (Full Cloud Azure), in conformità con i requisiti tecnici e i criteri di accettazione del progetto.

### Ambito
Il piano copre le seguenti aree tecnologiche:
- Rete e VPN (connettività tra sede Thema e Azure)
- Cluster HPC (Azure HB96-96rs v4 su InfiniBand NDR)
- Applicazione Pondus (AKS con Windows nodepool)
- Migrazione servizi (Profis→Odoo, M365, GiTea→Azure DevOps)
- Backup e Disaster Recovery
- Sicurezza e conformità ISO 27001

### Criteri di successo
- Tutti i test case critici superati con esito Pass
- Massimo 2 test case con esito Blocked (non bloccanti per il go-live)
- RPO/RTO verificati e conformi ai target definiti
- Rollback plan documentato e testato per ogni area critica

---

## Test Case

### 1. Rete e VPN

| ID | Area | Descrizione | Precondizioni | Passi | Risultato Atteso | Responsabile |
|---|---|---|---|---|---|---|
| TC-RETE-01 | VPN Site-to-Site | Verificare connettività IPsec tra FortiGate sede e Azure VPN Gateway | FortiGate configurato, tunnel IPsec IKEv2 stabilito | 1. Verificare stato tunnel su FortiGate: `diagnose vpn tunnel list`<br>2. Ping verso Azure VM da LAN sede<br>3. Ping verso gateway sede da Azure VM | Tunnel UP, ping RTT <5 ms, perdita 0% | Sistemista rete |
| TC-RETE-02 | P2S VPN | Verificare accesso remoto da client VPN | Azure Point-to-Site configurato, certificato client installato | 1. Connettere client OpenVPN/IKEv2 a Azure VPN Gateway<br>2. Eseguire ping verso Azure VM interna<br>3. Verificare risoluzione DNS interna | Connessione stabilita, accesso a risorse Azure | Sistemista rete |
| TC-RETE-03 | Azure Bastion | Verificare accesso admin via Bastion (senza IP pubblico) | Azure Bastion deployato, VM senza IP pubblico | 1. Accedere a VM via portale Azure → Bastion<br>2. Eseguire comando SSH/RDP<br>3. Verificare che VM non abbia IP pubblico | Accesso riuscito, VM senza IP pubblico | Sistemista rete |
| TC-RETE-04 | NSG Rules | Verificare regole NSG bloccano traffico non autorizzato | NSG configurato su subnet | 1. Tentare SSH su VM da IP esterno non autorizzato<br>2. Verificare log NSG (Azure Network Watcher) | Connessione rifiutata, log NSG registra il tentativo | Sistemista rete |

### 2. Cluster HPC (Azure HB96-96rs v4)

| ID | Area | Descrizione | Precondizioni | Passi | Risultato Atteso | Responsabile |
|---|---|---|---|---|---|---|
| TC-HPC-01 | Benchmark HPL | Verificare performance HPL (LINPACK) sui nodi HB96 | Cluster CycleCloud/Slurm deployato, 8 nodi HB96 attivi | 1. Eseguire HPL benchmark su 8 nodi (768 core)<br>2. Confrontare risultato con baseline atteso (~36 TFLOPS) | Performance ≥80% del teorico (~28,8 TFLOPS) | HPC Engineer |
| TC-HPC-02 | Latenza MPI | Verificare latenza MPI OSU benchmark | InfiniBand NDR funzionante su tutti i nodi | 1. Eseguire OSU MPI latency benchmark tra 2 nodi<br>2. Eseguire OSU MPI bandwidth benchmark | Latenza <2 μs, banda >380 Gbps | HPC Engineer |
| TC-HPC-03 | Slurm Scheduling | Verificare scheduling job su Slurm | Slurm controller operativo, partizioni configurate | 1. Inviare job di test: `sbatch -N 8 test_job.sh`<br>2. Verificare allocazione nodi: `squeue` e `sinfo`<br>3. Verificare output job | Job completato su 8 nodi, output corretto | HPC Engineer |
| TC-HPC-04 | Spot Recovery | Verificare recupero job da terminazione Spot | Nodi Spot attivi, job checkpointabile | 1. Simulare terminazione nodo Spot (Azure CLI stop)<br>2. Verificare che Slurm riavvii job da checkpoint<br>3. Verificare integrità risultati | Job ripreso da checkpoint senza perdita | HPC Engineer |

### 3. Pondus su AKS (Windows Container)

| ID | Area | Descrizione | Precondizioni | Passi | Risultato Atteso | Responsabile |
|---|---|---|---|---|---|---|
| TC-PONDUS-01 | Deploy Windows Container | Verificare deploy container Windows su AKS | AKS cluster con Windows nodepool, ACR con immagine Windows | 1. Eseguire `kubectl apply -f pondus-deployment.yaml`<br>2. Verificare stato pod: `kubectl get pods -o wide`<br>3. Verificare OS del nodo: Windows | Pod in stato Running su nodo Windows | Sviluppatore Pondus |
| TC-PONDUS-02 | Funzionalità C# | Verificare funzionamento endpoint applicazione | Applicazione Pondus deployata su AKS | 1. Eseguire GET su endpoint API Pondus<br>2. Verificare risposta JSON<br>3. Eseguire operazione CRUD su entità | Risposta 200 OK, dati coerenti | Sviluppatore Pondus |
| TC-PONDUS-03 | Connettività DB | Verificare connettività Pondus ad Azure SQL | Azure SQL MI accessibile da AKS | 1. Connettersi al pod: `kubectl exec -it pondus-pod -- /bin/bash`<br>2. Eseguire query di test: `SELECT 1`<br>3. Verificare operazioni CRUD su DB | Connessione DB riuscita, query restituiscono risultati | Sviluppatore Pondus |
| TC-PONDUS-04 | HTTPS/TLS | Verificare terminazione TLS su Application Gateway | Certificato TLS configurato su App Gateway | 1. Eseguire `curl -v https://pondus.tpgroup.it`<br>2. Verificare catena certificato<br>3. Verificare assenza errori TLS | Certificato valido, HTTPS 200 OK | Sistemista |

### 4. Migrazione

| ID | Area | Descrizione | Precondizioni | Passi | Risultato Atteso | Responsabile |
|---|---|---|---|---|---|---|
| TC-MIG-01 | Integrità dati post-migrazione | Verificare integrità dati dopo migrazione DB | Migrazione DMS completata | 1. Confrontare row count tabella per tabella tra source e target<br>2. Verificare checksum su campioni<br>3. Eseguire query di quadratura | Row count identico, checksum corrispondente | Sistemista DB |
| TC-MIG-02 | Rollback test | Verificare procedura di rollback | Snapshot pre-migrazione disponibile | 1. Eseguire rollback simulato: ripristino da snapshot<br>2. Verificare servizio funzionante su source<br>3. Verificare assenza perdita dati | Rollback completato in <30 min, zero perdita dati | Sistemista |
| TC-MIG-03 | Profis→Odoo quadratura | Verificare quadratura contabile post-migrazione | Import Odoo completato | 1. Estrarre bilancio di verifica da Odoo<br>2. Confrontare con bilancio pre-migrazione Profis<br>3. Verificare partite aperte clienti/fornitori | Bilancio corrispondente, saldi invariati | Responsabile amministrativo |
| TC-MIG-04 | M365 funzionalità | Verificare posta e collaborazione su M365 | Utenti migrati a M365 Premium | 1. Inviare email tra utente Thema e Pro Studio<br>2. Condividere documento SharePoint<br>3. Verificare MFA attivo | Posta funzionante, condivisione OK, MFA obbligatorio | Sistemista |

### 5. Backup e Disaster Recovery

| ID | Area | Descrizione | Precondizioni | Passi | Risultato Atteso | Responsabile |
|---|---|---|---|---|---|---|
| TC-DR-01 | File Restore | Verificare ripristino file da Azure Backup | Backup VM HBv4 eseguito (≤4 ore) | 1. Eliminare file su Azure Files<br>2. Avviare restore da Recovery Services Vault<br>3. Verificare file ripristinato | File ripristinato con dati intatti | Sistemista |
| TC-DR-02 | SQL Failover | Verificare failover Azure SQL Active Geo-Replication | Replica configurata West Europe → North Europe | 1. Simulare disconnessione DB primario (blocco NSG)<br>2. Verificare failover automatico a secondario<br>3. Verificare app Pondus riconnessa | Failover <30 secondi, app funzionante | Sistemista DB |
| TC-DR-03 | Site Recovery Drill | Verificare failover VM HBv4 con Azure Site Recovery | Site Recovery configurato, drill pianificato | 1. Eseguire failover simulato (Site Recovery drill)<br>2. Verificare VM partite in North Europe<br>3. Verificare rete e connettività | VM in esecuzione su regione DR, RPO/RTO rispettati | Sistemista HPC |
| TC-DR-04 | Verifica RPO/RTO | Misurare RPO/RTO reali | Test DR in corso | 1. Registrare timestamp ultimo backup prima del failover<br>2. Calcolare RPO: differenza tra failover e ultimo backup<br>3. Calcolare RTO: tempo da failover a servizio attivo | RPO ≤4 ore HPC, RTO ≤60 min HPC | PM / Sistemista |

### 6. Sicurezza

| ID | Area | Descrizione | Precondizioni | Passi | Risultato Atteso | Responsabile |
|---|---|---|---|---|---|---|
| TC-SEC-01 | MFA Enforcement | Verificare MFA obbligatorio per tutti gli utenti | Conditional Access policy configurata | 1. Tentare login con utente senza MFA registrato<br>2. Verificare prompt MFA<br>3. Verificare log Entra ID: `Sign-ins` | Accesso bloccato senza MFA, log registra mancata MFA | Security Team |
| TC-SEC-02 | Azure Policy Compliance | Verificare conformità Azure Policy ISO 27001 | Azure Policy initiative ISO 27001 assegnata | 1. Aprire Azure Policy → Compliance<br>2. Verificare risorse non conformi<br>3. Remediate risorse non conformi | Compliance score ≥80% | Security Team |
| TC-SEC-03 | Vulnerability Scan | Verificare scansione vulnerabilità su VM HBv4 | Azure Defender per VM attivo | 1. Eseguire vulnerability scan su VM HBv4<br>2. Esportare report vulnerabilità<br>3. Verificare assenza vulnerabilità Critical/High non note | Nessuna vulnerabilità Critical/High non mitigata | Security Team |
| TC-SEC-04 | Access Review | Verificare accessi privilegiati con PIM | PIM configurato per ruoli Azure | 1. Verificare attivazioni JIT degli ultimi 30 giorni<br>2. Verificare audit log PIM<br>3. Confermare nessun ruolo permanente | Tutti gli accessi admin sono JIT con audit | Security Team |

---

## Template Report di Test

```
REPORT TEST — Variante D (Full Cloud Azure)
═════════════════════════════════════════════

Test ID:        TC-XXXX-XX
Data test:      __/__/____
Tester:         ____________________________
Ambiente:       [Staging / Produzione]

ESITO:          [Pass / Fail / Blocked / N/A]

Evidenze:
  - Screenshot: allegato
  - Log: allegato
  - Output comando: allegato

Note:
____________________________________________________________

Anomalie riscontrate:
1. ________________________________________________________
2. ________________________________________________________

Firma tester:   _______________________
Firma PM:       _______________________
```

---

## Riepilogo Test Case

| Area | ID Range | Test Case Count |
|---|---|---|
| Rete e VPN | TC-RETE-01 ÷ TC-RETE-04 | 4 |
| Cluster HPC | TC-HPC-01 ÷ TC-HPC-04 | 4 |
| Pondus su AKS | TC-PONDUS-01 ÷ TC-PONDUS-04 | 4 |
| Migrazione | TC-MIG-01 ÷ TC-MIG-04 | 4 |
| Backup e DR | TC-DR-01 ÷ TC-DR-04 | 4 |
| Sicurezza | TC-SEC-01 ÷ TC-SEC-04 | 4 |
| **Totale** | | **24** |
