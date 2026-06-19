# Progettazione Rete/VPN — Variante On-Premise

## REQUISITI

- Connettività sede Thema (Torino) per 50 dipendenti (40 postazioni fisse + 10+ smart working)
- VPN LAN-to-LAN: sede Thema ↔ co-location / sede secondaria
- VPN Client-to-LAN: smart working per 10+ utenti/giorno
- Rete interna: VLAN per separazione servizi (HPC, Pondus, server, management, guest)
- Ridondanza connettività: link primario + backup (4G/5G o secondo ISP)
- Upgrade firewall FortiGate FG-60F (modello sottodimensionato per 50 utenti + VPN)
- Datacenter saturo: valutare armadio aggiuntivo o co-location

## SOLUZIONE

### Topologia di rete

```
[FortiGate 100F] ---- Link primario 1 Gbps ---- [ISP1]
      |                   Link backup 4G/5G ---- [ISP2]
      |
[Switch Aggregazione] ---- [Switch Accesso × 4]
      |                           |
[VLAN Servizi]             [40 postazioni fisse]
  - HPC (VLAN 10)
  - Pondus (VLAN 20)
  - Server (VLAN 30)
  - Management (VLAN 40)
  - Guest/WiFi (VLAN 50)
  - VoIP (VLAN 60)
```

### Componenti di rete

| Componente | Modello/Soluzione | Q.tà | Ruolo |
|---|---|---|---|
| **Firewall** | FortiGate 100F (upgrade da FG-60F) | 1 | Perimetro, VPN, IPS, filtering |
| **Switch aggregazione** | FortiSwitch 424D-POE o equivalente | 1 | Aggregazione VLAN, PoE per AP |
| **Switch accesso** | FortiSwitch 108F-POE | 4 | Accesso postazioni fisse |
| **Access Point WiFi** | FortiAP 231F (WiFi 6) | 4 | Copertura uffici 40 postazioni |
| **Link primario** | Fibra 1 Gbps dedicata | 1 | ISP business primario |
| **Link backup** | 4G/5G LTE (FortiExtender) | 1 | Failover automatico |
| **UPS** | APC Smart-UPS 3000 VA | 2 | Alimentazione rete + server |

### VLAN e subnetting

| VLAN | CIDR | Ruolo | Accesso |
|---|---|---|---|
| Native | 10.0.0.0/24 | Management apparati | Admin only |
| HPC | 10.0.10.0/24 | Cluster HPC (16 nodi + front-end) | Sviluppo HPC |
| Pondus | 10.0.20.0/24 | Applicazione Pondus + DB | DevOps |
| Server | 10.0.30.0/24 | VM servizi (Zimbra, AD, etc.) | Admin sistemisti |
| Management | 10.0.40.0/24 | Backup, monitoring, jump box | Admin |
| Guest/WiFi | 10.0.50.0/24 | Rete ospiti (Internet only) | Tutti + ospiti |
| VoIP | 10.0.60.0/24 | Telefonia IP | Ufficio |

### VPN

| Tipo | Configurazione |
|---|---|
| **LAN-to-LAN (sede ↔ co-location)** | IPsec tunnel tra FortiGate 100F e FortiGate/VPN node in co-location. IKEv2, AES-256, SHA-256, PFS |
| **Client-to-LAN (smart working)** | FortiClient VPN (SSL-VPN o IPsec). 10+ licenze concurrent. Autenticazione: AD Samba4 + MFA (Google Authenticator via RADIUS) |
| **Hybrid Cloud** | N/A (variante 100% on-premise) |

### Ridondanza connettività

| Scenario | Azione |
|---|---|
| **Guasto link primario** | FortiGate failover automatico su 4G/5G (< 30 secondi) |
| **Guasto ISP** | BGP failover su secondo ISP (se disponibile) |
| **Guasto FortiGate** | Spare FortiGate 100F configurato (warm spare) |
| **Guasto switch aggregazione** | Stack switch con ridondanza (MCLAG) |

## DIMENSIONAMENTO

| Traffico | Banda | Note |
|---|---|---|
| Collaborativo (50 utenti) | 500 Mbps | Posta, file, videochiamate |
| HPC (transfer) | 1 Gbps | Upload/download risultati simulazioni |
| Pondus (pubblico) | 500 Mbps | Traffico clienti esterni |
| Backup | 500 Mbps | Notturno, schedulato |
| **Link primario** | **1 Gbps** | Fibra dedicata business |
| **Backup** | **100 Mbps** | 4G/5G LTE |

## COSTI

| Voce | Costo una tantum | Costo annuale |
|---|---|---|
| FortiGate 100F | ~€3.500 | ~€900 (sottoscrizione UTM) |
| FortiSwitch 424D-POE | ~€1.200 | ~€200 (garanzia) |
| FortiSwitch 108F-POE × 4 | ~€2.400 | ~€400 (garanzia) |
| FortiAP 231F × 4 | ~€1.600 | ~€200 (garanzia) |
| FortiExtender 4G/5G | ~€600 | ~€480 (SIM dati) |
| UPS APC 3000 VA × 2 | ~€2.000 | ~€200 (batterie) |
| Fibra 1 Gbps business | — | ~€6.000 |
| Cablaggio e installazione | ~€3.000 | — |
| **Totale** | **~€14.300** | **~€8.380/anno** |
