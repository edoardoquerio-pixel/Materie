# Progetto Rete — Sede Unificata TP Group

## Topologia LAN

```
┌─────────────────────────────────────────────────────────┐
│                    Sede Torino (Thema)                    │
│                                                          │
│   Internet ──── FortiGate FG-100F (HA cluster)           │
│                    │                                     │
│              ┌─────┴─────┐                               │
│              │  Switch    │                               │
│              │  Core L3   │                               │
│              └─────┬─────┘                               │
│                    │                                     │
│         ┌──────────┼──────────┐                          │
│         ▼          ▼          ▼                          │
│   Postazioni    HPC      Server                          │
│   LAN 40 pz    cluster   AD Samba4                       │
│   (VLAN 10)    (VLAN 20) (VLAN 30)                      │
│                                                          │
│   WiFi AP ──── VLAN 40 (ospiti/collaboratori)            │
└─────────────────────────────────────────────────────────┘
```

## Specifiche tecniche

| Componente | Specifica | Q.tà | Costo unit. | Totale |
|---|---|---|---|---|
| FortiGate FG-100F (HA cluster) | 2 appliance + FortiCare 3 anni | 2 | € 3.500 | € 7.000 |
| Switch Core L3 48 porte PoE+ | Gestito, VLAN, QoS, stackable | 2 | € 1.200 | € 2.400 |
| Switch accesso 24 porte PoE+ | Per postazioni | 3 | € 400 | € 1.200 |
| Access Point WiFi 6 | Triband, gestito da FortiGate | 4 | € 250 | € 1.000 |
| UPS rack 1500 VA | Per apparati di rete | 2 | € 600 | € 1.200 |
| Cablaggio strutturato cat.6A | Postazioni, patch panel, percorsi | 1 | € 6.000 | € 6.000 |
| 2° ISP (FTTH 1 Gbps) | Ridondanza connettività | 12 mesi | € 350/mese | € 4.200 |
| **Totale** | | | | **€ 23.000** |

## VLAN

| VLAN | ID | Scopo |
|---|---|---|
| LAN-dipendenti | 10 | 40 postazioni fisse |
| HPC-cluster | 20 | 8+8 nodi calcolo + front-end |
| Server-infra | 30 | AD Samba4, stampanti |
| WiFi-dipendenti | 40 | Accesso wireless dipendenti |
| WiFi-ospiti | 50 | Rete ospiti (isolata) |
| VPN-remoti | 60 | Accesso client VPN remoti |
| MGMT | 99 | Amministrazione apparati |

## Routing

- **BGP** per route advertisement tra FortiGate e Azure VPN Gateway
- **Static route** per subnet on-prem non propagabili
- **Default route** 0.0.0.0/0 → FortiGate WAN primaria (fallback su 2° ISP via SD-WAN)
