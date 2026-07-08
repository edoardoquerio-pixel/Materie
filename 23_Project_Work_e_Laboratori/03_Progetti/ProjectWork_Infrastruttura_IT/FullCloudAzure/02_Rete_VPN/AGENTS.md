# Agente: Network & VPN Engineer — Full Cloud Azure

## Ruolo

Progettazione della connettività di rete per la sede unificata TP Group, tunnel VPN verso Azure, accesso remoto per smart working e integrazione cloud.

## Dipende da

- `01_Assessment/` (dati AS-IS Thema e Pro Studio)

## Deliverable

| # | File | Contenuto |
|---|---|---|
| 01 | `progetto_rete.md` | Progetto rete LAN sede unificata |
| 02 | `progetto_vpn.md` | VPN Sede→Azure e VPN client remoti |
| 03 | `schema_rete.md` | Schema topologia di rete |

## Decisioni chiave Full Cloud Azure

- Upgrade firewall: **FortiGate FG-60F → FG-100F** in HA cluster (50 utenti + VPN)
- VPN Sede→Azure: **IPsec IKEv2** verso Azure VPN Gateway VpnGw1AZ
- VPN client: **WireGuard** su FortiGate + Azure VPN Client
- 2° ISP per ridondanza connettività
- DNS: domini TP Group puntati a M365/Azure
