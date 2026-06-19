# Progettazione Rete/VPN — Variante Ibrida

## REQUISITI

- On-prem: FortiGate 100F (upgrade) per rete sede, VPN, HPC
- Cloud: Cloud VPN su GCP per servizi migrati
- VPN LAN-to-LAN: FortiGate ↔ GCP (tunnel IPsec)
- VPN Client-to-LAN: FortiClient + Cloud VPN IAP per smart working
- Hybrid Cloud: connettività dedicata tra sede Thema e GCP
- VLAN: separazione traffico on-prem (HPC, server, management) e cloud (servizi migrati)
- Ridondanza connettività: link primario + backup 4G/5G

## SOLUZIONE

### Architettura

```
[Sede Thema (on-prem)]                          [GCP]
       |                                             |
[FortiGate 100F] ---- HA VPN (IPsec) ---- [Cloud VPN Gateway]
       |                                             |
  [VLAN On-prem]                               [VPC GCP]
  - HPC (10.0.10.0/24)                        - Services (10.1.1.0/24)
  - Server (10.0.20.0/24)                     - Managed (10.1.2.0/24)
  - Backup (10.0.30.0/24)                     - Backup (10.1.3.0/24)
       |                                             |
  [Smart worker] ──── FortiClient VPN / IAP ──────┘
```

### Componenti

| Componente | On-prem | Cloud |
|---|---|---|
| **Firewall** | FortiGate 100F (upgrade) | Cloud Firewall rules |
| **VPN LAN-to-LAN** | IPsec tunnel to GCP | HA VPN Gateway |
| **VPN Client-to-LAN** | FortiClient SSL-VPN | IAP + Cloud VPN |
| **Rete interna** | VLAN con tagging 802.1Q | VPC nativo |
| **DNS** | BIND (on-prem) | Cloud DNS (forwarder) |
| **Routing** | BGP dinamico (FortiGate) | Cloud Router |

### Hybrid Cloud Connectivity

| Opzione | Costo | Latenza | Throughput | Raccomandazione |
|---|---|---|---|---|
| **Cloud VPN (IPsec)** | €0 (solo egress) | +5-10 ms | 3 Gbps | **Default** |
| **Partner Interconnect** | ~€200/mese + cross-connect | +1-3 ms | 10-100 Gbps | Se latenza critica |

### Subnetting

| Rete | CIDR | Location | Ruolo |
|---|---|---|---|
| On-prem HPC | 10.0.10.0/24 | Sede Thema | Cluster HPC |
| On-prem server | 10.0.20.0/24 | Sede Thema | VM servizi |
| On-prem backup | 10.0.30.0/24 | Sede Thema | NAS backup |
| GCP services | 10.1.1.0/24 | GCP us-central1 | Pondus, servizi migrati |
| GCP managed | 10.1.2.0/24 | GCP us-central1 | AD, jump box |
| GCP backup | 10.1.3.0/24 | GCP us-central1 | Backup cloud |

## DIMENSIONAMENTO

| Link | Banda | Costo |
|---|---|---|
| Sede → Internet | 1 Gbps (fibra) | ~€500/mese |
| Sede → GCP (VPN) | 1 Gbps (condiviso) | Incluso |
| Backup 4G/5G | 100 Mbps | ~€80/mese |
| GCP egress | 5 TB/mese stimato | ~$250/mese |

## COSTI

| Voce | Una tantum | Annuale |
|---|---|---|
| FortiGate 100F + UTM | ~€3.500 | ~€900 |
| Cloud VPN Gateway (HA) | — | ~$1.800 |
| Cloud Router + BGP | — | ~$600 |
| Fibra 1 Gbps + 4G backup | — | ~€6.960 |
| **Totale** | **~€3.500** | **~€10.260** |
