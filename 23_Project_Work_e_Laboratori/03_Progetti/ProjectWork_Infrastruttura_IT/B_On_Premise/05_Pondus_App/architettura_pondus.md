# Architettura Pondus — Variante On-Premise

## REQUISITI

- Upgrade HW: server attuale (Xeon Silver 4110, 64 GB RAM, 1,2 TB HDD) datato (2015)
- Containerizzazione per scalabilità orizzontale e gestione moderna
- DB: MS SQL Server on-premise (upgrade licenza o passaggio a Standard)
- Esposizione pubblica: sito web e-commerce per abbonamenti mensili
- Backup su NAS QNAP esistente
- Integrazione con AD Samba4 per autenticazione

## SOLUZIONE

### Architettura target

```
[Clienti] ---- HTTPS ---- [Reverse Proxy (nginx/IIS ARR)]
                                |
                    [Load Balancer (HAProxy)]
                          /              \
              [Pondus Instance 1]    [Pondus Instance 2]
                    |                       |
              [MS SQL Server]       [NAS QNAP (Backup)]
                    |
              [Samba4 AD (auth)]
```

### Upgrade HW

| Componente | Attuale | Target |
|---|---|---|
| **Server** | Xeon Silver 4110, 64 GB | 2× Xeon Silver 4510, 128 GB RAM |
| **Storage** | 1,2 TB HDD | 2× 960 GB SSD NVMe (RAID 1) + 4 TB HDD (dati) |
| **Form factor** | Tower | 2U rack |
| **Alimentazione** | Singola | Doppia PSU ridondante |

### Containerizzazione

| Aspetto | Scelta |
|---|---|
| **Container engine** | Docker Engine su Linux (o Windows Server Core con Docker) |
| **Orchestrazione** | Docker Compose (singolo host) o Swarm (multi-host futuro) |
| **Reverse proxy** | nginx (terminazione TLS, routing) |
| **Registry** | GitLab Container Registry o Harbor self-hosted |
| **Build CI/CD** | GitLab CI / Jenkins (su VM esistente) |

### Database

| Aspetto | Scelta |
|---|---|
| **DBMS** | MS SQL Server 2022 Standard |
| **Licenza** | Licenza perpetua (stima: ~€4.000 una tantum) o subscription (~€150/mese) |
| **Storage** | SSD NVMe RAID 1 per log + HDD per dati |
| **Backup** | Backup su NAS QNAP (giornaliero, retention 30 giorni) |
| **HA** | Sempre-on availability group (se budget lo consente) |

### Esposizione pubblica e abbonamenti

- **Dominio**: pondus.tp-group.it (certificato Let's Encrypt / SSL commerciale)
- **Reverse proxy**: nginx con TLS 1.3
- **E-commerce**: integrazione con Stripe per abbonamenti
- **Autenticazione**: LDAP su Samba4 AD + MFA con Google Authenticator (via RADIUS)
- **API pubblica**: REST API su endpoint /api/v1/

## DIMENSIONAMENTO

| Risorsa | Specifica |
|---|---|
| **CPU** | 2× Xeon Silver 4510 (24 core totali) |
| **RAM** | 128 GB |
| **Storage SSD** | 2 TB (RAID 1) |
| **Storage HDD** | 4 TB (dati + log) |
| **Banda** | 500 Mbps |

## COSTI

| Voce | Costo una tantum | Costo annuale |
|---|---|---|
| Server HW (2× Xeon Silver 4510, 128 GB, SSD + HDD) | ~€6.000 | — |
| Licenza MS SQL Server 2022 Standard | ~€4.000 | — |
| Software assurance MS SQL (opzionale) | — | ~€1.000 |
| Container platform (Docker Engine) | Gratuito | — |
| nginx / HAProxy | Gratuito (open source) | — |
| Certificato SSL commerciale | ~€200 | ~€200 |
| Integrazione Stripe (commissioni) | — | Variabile (2,9% + €0,30) |
| Manutenzione annua HW | — | ~€500 |
| Energia elettrica | — | ~€600 |
| **Totale** | **~€10.200** | **~€2.300/anno** |
