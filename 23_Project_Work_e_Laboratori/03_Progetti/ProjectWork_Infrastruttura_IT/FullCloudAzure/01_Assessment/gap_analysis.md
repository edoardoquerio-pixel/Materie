# Gap Analysis — Full Cloud Azure vs. Requisiti ISO/IEC 27001

## Contesto

La variante **Full Cloud Azure** prevede la migrazione di tutti i servizi (escluso HPC) sull'ecosistema Microsoft. Questa gap analysis valuta lo scostamento tra lo stato AS-IS e i requisiti ISO 27001 alla luce della migrazione.

## Gap Analysis

| # | Requisito ISO 27001 | Stato AS-IS | Target Full Cloud Azure | Gap residuo | Priorità |
|---|---|---|---|---|---|
| 1 | **Business continuity — Ridondanza sistemi** | Thema: SAN singola, NAS singolo, FortiGate singolo. Pro Studio: dipendenza unico cloud provider (GCP) | Azure garantisce ridondanza intrinsica (Azure SQL HA, App Service multi-istanza, M365 ridondante). AD Samba4 on-prem rimane SPOF per identità fino a completa migrazione Entra ID | **Basso** — Azure risolve la maggior parte dei SPOF. AD Samba4 richiede HA o dismissione rapida | **Media** |
| 2 | **Business continuity — Ridondanza connettività** | Thema: singolo ISP. Pro Studio: connettività condominiale | FortiGate FG-100F con dual WAN (2 ISP). VPN Azure Gateway ridondante (active-standby) | **Basso** — risolto con nuovo firewall e 2° ISP | **Bassa** |
| 3 | **Disaster recovery — Delocalizzazione backup** | Thema: backup su NAS QNAP on-prem (stessa sede). Pro Studio: backup GCP single-region | Azure Backup: backup su storage geo-ridondante (RA-GRS). Azure Site Recovery: replica in paired region (West Europe → North Europe) | **Nullo** — requisito soddisfatto da Azure nativamente | **Bassa** |
| 4 | **Disaster recovery — Fruibilità servizi** | Pondus su HW dedicato on-prem — nessun DR | Pondus su Azure App Service: slot di staging, backup automatici, possibilità multi-regione | **Basso** — App Service fornisce alta disponibilità. Per DR cross-regione serve piano aggiuntivo | **Media** |
| 5 | **Cifratura storage** | Thema: nessuna cifratura a riposo documentata. Pro Studio: GCP cifrato default | Azure: cifratura lato server AES-256 su tutti i servizi (Azure SQL, Managed Disks, Blob Storage). M365: cifratura at-rest e in-transit | **Nullo** — risolto dalla piattaforma | **Bassa** |
| 6 | **Protocolli sicuri** | Servizi Thema: non documentata adozione TLS sistematica | Azure: HTTPS di default su tutti gli endpoint. M365: TLS 1.2+ | **Nullo** — risolto dalla piattaforma | **Bassa** |
| 7 | **VPN LAN-to-LAN** | Nessuna VPN attiva tra Thema e Pro Studio | VPN IPsec IKEv2 tra sede Torino (FortiGate FG-100F) e Azure VPN Gateway | **Nullo** — progettato e incluso nel piano | **Bassa** |
| 8 | **VPN Client-to-LAN** | Thema: non documentata VPN client diffusa. Pro Studio: nessuna VPN | WireGuard su FortiGate FG-100F per i 50 utenti + Azure VPN Client per risorse Azure | **Basso** — da configurare e distribuire | **Media** |
| 9 | **VPN Hybrid Cloud** | Thema: nessuna VPN verso cloud. Pro Studio: accesso GCP via Internet | VPN IPsec Sede → Azure per accesso risorse IaaS. Azure Private Link per PaaS | **Nullo** — risolto | **Bassa** |
| 10 | **MFA** | Thema: solo password AD. Pro Studio: Google Authenticator | **Entra ID P1** + Conditional Access + Microsoft Authenticator per tutti i 50 utenti | **Nullo** — risolto | **Bassa** |
| 11 | **UPS** | Thema: UPS 10 minuti, nessun generatore | **Non applicabile** — datacenter virtualizzato su Azure. Solo connettività di sede richiede UPS per apparati di rete | **Nullo** — il cloud elimina il rischio | **Bassa** |
| 12 | **Condizionamento** | Thema: raffreddamento al limite | **Non applicabile** — cloud elimina carico termico del datacenter. Solo HPC on-prem rimane | **Basso** — HPC on-prem richiede ancora raffreddamento adeguato | **Media** |
| 13 | **Hardening server** | Server Thema autogestiti, nessun benchmark | **Azure Policy** + **Defender for Cloud** per valutazione continua della conformità. VM MediaWiki: Azure Update Management | **Basso** — policy e automazione Azure risolvono il gap | **Bassa** |
| 14 | **IAM** | Thema: AD Samba4 senza policy formale. Pro Studio: Google Workspace con ruoli base | **Entra ID P1** con RBAC, PIM (Privileged Identity Management), revisione accessi trimestrale | **Basso** — Entra ID fornisce strumenti nativi | **Bassa** |

## Riepilogo Gap

| Priorità | Conteggio | # Riferimento |
|---|---|---|
| **Media** | 3 | 1, 4, 8 |
| **Bassa** | 11 | 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14 |
| **Totale** | **14** | |

## Valutazione sintetica

La migrazione Full Cloud Azure **riduce drasticamente il numero di gap** rispetto allo scenario on-premise:

- **8 gap eliminati completamente** (cifratura, protocolli sicuri, VPN, MFA, UPS, condizionamento backup)
- **3 gap ridotti a impatto medio/basso** (ridondanza AD, DR Pondus, VPN client)
- **3 gap da monitorare** (HPC on-prem, connettività, hardening VM)
