# Progettazione Rete/VPN — Variante Full Cloud Azure

## REQUISITI

- Connettività sede Thema Consulting (Torino) verso Microsoft Azure
- Smart working per 10+ utenti/giorno su 50 dipendenti totali
- Accesso sicuro ai servizi cloud (Pondus pubblica, HPC, backup)
- Nessuna sede secondaria fisica (tutto converge su Azure)
- Shutdown massimo 7 giorni durante il cut-over
- Banda sufficiente per: 50 utenti (traffico collaborativo), HPC (upload/download risultati), Pondus (traffico pubblico)

## SOLUZIONE

### Architettura di rete

```
[FortiGate FG-60F] ---- Azure VPN Gateway (IPsec IKEv2) ---- [Azure VNet]
     Sede Thema                                               West Europe
         |                                                         |
    [Switch LAN]                                           [Subnet Servizi]
    ..........                                               ................
    40 postazioni fisse                                      - Management (10.0.1.0/24)
    10+ smart worker                                         - HPC (10.0.2.0/24)
                                                             - Pondus (10.0.3.0/24)
                                                             - Backup (10.0.4.0/24)
                                                             - GatewaySubnet (10.0.0.0/24)
```

### Componenti

| Componente | Servizio Azure | Descrizione |
|---|---|---|
| **VNet** | Azure Virtual Network | VNet in West Europe con subnet per servizi |
| **VPN Site-to-Site** | Azure VPN Gateway (Active-Active) | Tunnel IPsec IKEv2 tra FortiGate e Azure |
| **Client VPN** | Azure Point-to-Site VPN + Azure Bastion | Accesso remoto per smart working + admin |
| **Firewall** | Azure Network Security Groups (NSG) + Application Gateway WAF | Regole ingress/egress + WAF per Pondus |
| **NAT** | Azure NAT Gateway | Uscita Internet per VM senza IP pubblico |
| **DNS** | Azure DNS | Gestione zona DNS privata per servizi interni |

### VPN LAN-to-LAN

- Tunnel IPsec (IKEv2) tra FortiGate FG-60F (sede Thema) e Azure VPN Gateway
- Modalità Active-Active: 2 tunnel contemporanei per throughput aggregato fino a 10 Gbps
- BGP dinamico via Azure Route Server per failover automatico
- Crittografia: AES-256, SHA-256, Perfect Forward Secrecy (PFS)
- Throughput per tunnel: fino a 5 Gbps (VPN Gateway VpnGw3)

### VPN Client-to-LAN (Smart Working)

- **Azure Point-to-Site VPN**: tunnel IPsec/IKEv2 client-to-cloud per accesso completo alla rete aziendale
- **Azure Bastion**: accesso RDP/SSH via browser alle VM senza esporre IP pubblici
- Raccomandata: Bastion per amministratori + Point-to-Site VPN per utenti che necessitano accesso completo
- Utenti simultanei previsti: 10+ al giorno, fino a 20 in picco

### Network Security Groups (NSG)

| Rule | Source | Destination | Porte | Protocollo |
|---|---|---|---|---|
| Management | 10.0.0.0/24 (sede Thema) | Subnet Management | 22, 3389, 443 | TCP |
| HPC access | 10.0.0.0/24 | Subnet HPC | 22, custom HPC ports | TCP |
| Pondus public | 0.0.0.0/0 | Subnet Pondus (via App GW) | 443 | TCP |
| Backup | Subnet Backup | Azure Storage | 443 | TCP |
| Deny all | 0.0.0.0/0 | All subnets | Any | Any |

## DIMENSIONAMENTO

### Banda

| Tipologia traffico | Banda stimata | Note |
|---|---|---|
| Traffico collaborativo (50 utenti) | 500 Mbps | Posta, file, Teams, web |
| HPC (upload/download) | 1 Gbps | Batch, non continuo |
| Pondus (pubblico) | 500 Mbps - 1 Gbps | Variabile, da dimensionare dopo go-live |
| Backup | 500 Mbps | Notturno, schedulato |
| **Totale link sede** | **1 Gbps** | Link dedicato con failover 4G/5G |

### Indirizzamento IP

| Subnet | CIDR | Ruolo |
|---|---|---|
| GatewaySubnet | 10.0.0.0/24 | Azure VPN Gateway |
| management | 10.0.1.0/24 | VM amministrative, jump box, monitoring |
| hpc-cluster | 10.0.2.0/24 | Nodi HPC (HBv4) |
| pondus-app | 10.0.3.0/24 | Applicazione Pondus (Container Apps) |
| backup-storage | 10.0.4.0/24 | Storage backup, Private Endpoint |

## COSTI

| Voce | Servizio Azure | Costo mensile stimato | Costo annuale |
|---|---|---|---|
| Azure VPN Gateway | Active-Active (VpnGw3) | ~€220 | ~€2.640 |
| Azure NAT Gateway | NAT gateway (50 utenti) | ~€65 | ~€780 |
| Azure WAF | Application Gateway v2 (WAF_v2) | ~€130 | ~€1.560 |
| Azure Bastion | Basic tier | ~€140 | ~€1.680 |
| Azure DNS | Zona privata + query | ~€8 | ~€96 |
| Connettività sede | Fibra 1 Gbps dedicata | ~€500 | ~€6.000 |
| Failover 4G/5G | Backup link | ~€80 | ~€960 |
| **Totale annuo** | | | **~€13.716** |

*Note: costi Azure basati su listino pubblico 2026 (cambio $1 = €0,95). Connettività sede stimata su operatori italiani business. M365 già presente — nessun costo aggiuntivo per posta e collaborazione.*
