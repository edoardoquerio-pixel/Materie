# Progettazione Rete/VPN — Variante Full Cloud GCP

## REQUISITI

- Connettività sede Thema Consulting (Torino) verso Google Cloud
- Smart working per 10+ utenti/giorno su 50 dipendenti totali
- Accesso sicuro ai servizi cloud (Pondus pubblica, HPC, backup)
- Nessuna sede secondaria fisica (tutto converge su GCP)
- Shutdown massimo 7 giorni durante il cut-over
- Banda sufficiente per: 50 utenti (traffico collaborativo), HPC (upload/download risultati), Pondus (traffico pubblico)

## SOLUZIONE

### Architettura di rete

```
[FortiGate FG-60F] ---- Cloud VPN (tunnel IPsec) ---- [GCP VPC]
     Sede Thema                                       us-central1
         |                                                  |
    [Switch LAN]                                   [Subnet Servizi]
    ..........                                      ................
    40 postazioni fisse                              - Management (10.0.1.0/24)
    10+ smart worker                                - HPC (10.0.2.0/24)
                                                    - Pondus (10.0.3.0/24)
                                                    - Backup (10.0.4.0/24)
```

### Componenti

| Componente | Servizio GCP | Descrizione |
|---|---|---|
| **VPC** | Custom VPC | VPC nativo con subnet regionali in us-central1 |
| **Cloud VPN** | Classic VPN / HA VPN | Tunnel IPsec site-to-cloud tra FortiGate e GCP |
| **Client VPN** | Cloud VPN per utenti | Accesso remoto via IAP (Identity-Aware Proxy) + VPN client |
| **Firewall** | Cloud Firewall + Cloud Armor | Regole ingress/egress + WAF per Pondus pubblica |
| **NAT** | Cloud NAT | Uscita Internet per VM senza IP pubblico |
| **DNS** | Cloud DNS | Gestione zona DNS privata per servizi interni |

### Cloud VPN — LAN-to-LAN

- Tunnel IPsec (IKEv2) tra FortiGate FG-60F (sede Thema) e Cloud VPN Gateway GCP
- Throughput: fino a 3 Gbps per tunnel (HA VPN con 2 tunnel attivi)
- BGP dinamico (Cloud Router) per failover automatico
- Crittografia: AES-256, SHA-256, PFS (Perfect Forward Secrecy)

### VPN Client-to-LAN (Smart Working)

- Opzione 1: **Identity-Aware Proxy (IAP)** — accesso a VM e servizi senza VPN, basato su identità e contesto
- Opzione 2: **Cloud VPN per client** — tunnel IPsec client-to-cloud per accesso completo alla rete
- Raccomandata: IAP per servizi interni + Cloud VPN solo per utenti che necessitano accesso completo alla rete
- Utenti simultanei previsti: 10+ al giorno, fino a 20 in picco

### Cloud Firewall

| Rule | Source | Destination | Porte | Protocollo |
|---|---|---|---|---|
| Management | 10.0.0.0/24 (sede Thema) | Subnet Management | 22, 3389, 443 | TCP |
| HPC access | 10.0.0.0/24 | Subnet HPC | 22, custom HPC ports | TCP |
| Pondus public | 0.0.0.0/0 | Subnet Pondus | 443 | TCP |
| Backup | Subnet Backup | Cloud Storage API | 443 | TCP |
| Deny all | 0.0.0.0/0 | All subnets | Any | Any |

## DIMENSIONAMENTO

### Banda

| Tipologia traffico | Banda stimata | Note |
|---|---|---|
| Traffico collaborativo (50 utenti) | 500 Mbps | Posta, file, meet, web |
| HPC (upload/download) | 1 Gbps | Batch, non continuo |
| Pondus (pubblico) | 500 Mbps - 1 Gbps | Variabile, da dimensionare dopo go-live |
| Backup | 500 Mbps | Notturno, schedulato |
| **Totale link sede** | **1 Gbps** | Link dedicato con failover 4G/5G |

### Indirizzamento IP

| Subnet | CIDR | Ruolo |
|---|---|---|
| on-premises-link | 10.0.0.0/24 | Connettività sede Thema a GCP |
| management | 10.0.1.0/24 | VM amministrative, jump box, monitoring |
| hpc-cluster | 10.0.2.0/24 | Nodi HPC (istanze C2/H3) |
| pondus-app | 10.0.3.0/24 | Applicazione Pondus (Cloud Run / GKE) |
| backup-storage | 10.0.4.0/24 | Storage backup, Data Transfer |

## COSTI

| Voce | Servizio GCP | Costo mensile stimato | Costo annuale |
|---|---|---|---|
| Cloud VPN Gateway | HA VPN Gateway | ~$150 | ~$1.800 |
| Cloud Router | BGP session | ~$50 | ~$600 |
| Cloud NAT | NAT gateway (50 utenti) | ~$70 | ~$840 |
| Cloud Armor | WAF + DDoS protection | ~$100 | ~$1.200 |
| Cloud DNS | Zona privata + query | ~$10 | ~$120 |
| Connettività sede | Fibra 1 Gbps dedicata | ~€500 | ~€6.000 |
| Failover 4G/5G | Backup link | ~€80 | ~€960 |
| **Totale annuo** | | | **~€11.520** |

*Note: costi GCP basati su listino pubblico 2026. Connettività sede stimata su operatori italiani business.*
