# Requisiti Sicurezza ISO 27001 — Variante On-Premise

## Premessa

La presente sezione documenta l'adeguamento tecnico della Variante On-Premise ai
requisiti ISO/IEC 27001 specificati dal cliente. Trattandosi di architettura on-premise,
la responsabilità della conformità è interamente in capo al fornitore/proponente e al
cliente TP Group, senza la delega al cloud provider.

## Business Continuity

### Ridondanza sistemi strategici

| Sistema | Strategia | Dettaglio |
|---|---|---|
| **Firewall** | FortiGate 100F attivo + spare configurato | Warm spare per sostituzione rapida |
| **Switch** | Stack con MCLAG (Multi-Chassis Link Aggregation) | Nessun SPOF sul networking |
| **Storage** | NAS QNAP RAID 6 (2 disk fault tolerance) | Tolleranza 2 dischi guasti |
| **VM host** | 2 host VMWare esistenti (HA cluster) | Failover automatico VM |
| **Cluster HPC** | Nodi ridondanti: job scheduler riavvia su nodi vivi | Guasto singolo nodo tollerato |
| **UPS** | 2 UPS (sede + co-location) | Autonomia 30+ minuti |
| **Co-location** | Raffreddamento + UPS + generatore | SLA 99,99% datacenter |

### Ridondanza connettività

| Elemento | Configurazione |
|---|---|
| **Link primario** | Fibra 1 Gbps business ISP1 |
| **Link backup** | 4G/5G FortiExtender (100 Mbps, failover < 30s) |
| **Co-location link** | Cross-connect dedicato 1 Gbps |
| **VPN** | Tunnel IPsec tra sede e co-location (BGP failover) |

## Disaster Recovery

| Requisito | Implementazione |
|---|---|
| Delocalizzazione backup | NAS secondario 32 TB in co-location (replica notturna) |
| Fruibilità servizi clienti | Pondus ripristinabile in co-location (RTO 10h) |
| Procedure di restore | Runbook DR documentato, test semestrale |
| RPO servizi critici | ≤4 ore (Pondus: backup ogni 4h su NAS + replica) |
| RTO servizi critici | ≤10 ore (disastro totale) / ≤2 ore (guasto HW) |

## Sicurezza Accessi

### Cifratura dati

| Stato | Dettaglio |
|---|---|
| **Dati in transito** | TLS 1.3 su servizi web (Pondus, NextCloud, Zimbra); IPSec su VPN; SSH per accesso server |
| **Dati a riposo (server)** | LUKS (Linux) o BitLocker (Windows) su tutti i server |
| **Dati a riposo (NAS)** | Cifratura nativa NAS QNAP (AES-256) |
| **Dati a riposo (laptop)** | BitLocker policy obbligatoria per tutti i laptop aziendali |
| **Backup off-site** | Backup cifrati (AES-256) prima della replica |

### Protocolli sicuri

| Servizio | Protocollo | Note |
|---|---|---|
| Web (Pondus, NextCloud, Wiki) | HTTPS (TLS 1.3) | Certificati Let's Encrypt / commerciali |
| Posta (Zimbra) | SMTP TLS, IMAPS | Porte 587/993 |
| SSH | SSH key-only | Disabilitato accesso password |
| VPN (LAN-to-LAN) | IPsec IKEv2 | AES-256, SHA-256, PFS |
| VPN (Client-to-LAN) | SSL-VPN (FortiClient) | FortiGate SSL-VPN |
| DB (MS SQL) | TLS 1.2+ | Connessioni cifrate |
| Backup replica | AES-256 su tunnel IPsec | Veeam encryption + tunnel |

### VPN

| Tipo | Configurazione |
|---|---|
| **LAN-to-LAN** | IPsec attivo tra FortiGate 100F (sede) e FortiGate (co-location) |
| **Client-to-LAN** | FortiClient SSL-VPN per smart working (10+ licenze) |
| **Hybrid Cloud** | N/A (variante 100% on-prem) |

### Autenticazione Multi-Fattore (MFA)

- **FortiGate admin**: MFA via FortiToken mobile (o Google Authenticator via RADIUS)
- **VPN accesso**: MFA obbligatorio per tutti gli utenti VPN (FortiToken)
- **Servizi web (Pondus)**: MFA via Google Authenticator + LDAP su Samba4 AD
- **Server accesso**: SSH key + MFA (modulo pam_google_authenticator)
- **Samba4 AD**: password policy (min 12 caratteri, scadenza 90gg) + MFA per admin

### Identity and Access Management (IAM)

| Principio | Implementazione |
|---|---|
| **Minimo privilegio** | Ruoli AD (Domain Admin, Server Admin, User, Guest) |
| **Separazione ruoli** | Admin IT ≠ Utente standard ≠ Ospite |
| **Resource hierarchy** | OU in AD per reparto (Engineering, Administration, Management) |
| **Audit logging** | Syslog centralizzato (VM Graylog o ELK) + Windows Event Log |
| **Revisione periodica** | Report trimestrale account e permessi |

### Hardening server

| Sistema | Benchmark |
|---|---|
| **Linux server** | CIS Benchmark per Ubuntu/Rocky Linux |
| **Windows server** | CIS Benchmark per Windows Server 2022 |
| **VMware** | VMware Security Hardening Guide |
| **FortiGate** | Fortinet Security Configuration Guide |
| **NAS QNAP** | QNAP security advisor |

## Bozza Policy di Sicurezza

### Principi generali

1. Accesso basato sul minimo privilegio
2. Cifratura end-to-end (dati in transito e a riposo)
3. MFA obbligatorio per accessi amministrativi e remoti
4. Patch management entro 7 giorni (critico) / 30 giorni (standard)
5. Backup obbligatorio per tutti i sistemi (verifica settimanale)
6. Incident response entro 1 ora dalla rilevazione

### Ruoli

| Ruolo | Responsabilità |
|---|---|
| **Security Officer** | Policy, audit, incident response |
| **System Admin** | Patch, hardening, backup, monitoring |
| **Network Admin** | Firewall, VPN, VLAN, accessi rete |
| **Application Owner** | Sicurezza applicativa, utenti, permessi |
| **Utenti** | MFA, password policy, segnalazione incidenti |

## Adeguamento ISO 27001 — Checklist

| Controllo ISO 27001 (Annex A) | Stato Variante B | Evidenza |
|---|---|---|
| A.5.1 — Policy di sicurezza | ✅ Policy bozza inclusa | Presente documento |
| A.6.1 — Organizzazione interna | ✅ Ruoli definiti | Matrice ruoli |
| A.9.1 — Controllo accessi | ✅ AD + MFA | Samba4 AD + FortiToken |
| A.10.1 — Controlli crittografici | ✅ Cifratura attiva | LUKS, BitLocker, TLS 1.3, IPSec |
| A.11.1 — Sicurezza fisica | 🟡 Da rafforzare (co-location) | Sede Thema non datacenter class |
| A.11.2 — Apparecchiature | 🟡 UPS insufficiente | Upgrade UPS pianificato |
| A.12.3 — Backup | ✅ Backup NAS + co-location | 3-2-1 rule rispettata |
| A.12.6 — Vulnerability management | 🟡 Da formalizzare | Patch policy definita ma non automatizzata |
| A.13.1 — Sicurezza rete | ✅ VLAN, VPN, firewall | Segmentazione completa |
| A.13.2 — Trasferimento informazioni | ✅ VPN cifrata | IPsec + TLS |
| A.14.1 — Sicurezza applicativa | 🟡 Da completare | Security review pianificato |
| A.17.1 — Continuità servizi | ✅ DR co-location | RPO 4h, RTO 10h |
| A.18.1 — Conformità GDPR | 🟡 DPA clienti da formalizzare | In corso |

✅ = Coperto / 🟡 = Parzialmente coperto

## Costi sicurezza

| Voce | Costo una tantum | Costo annuale |
|---|---|---|
| FortiToken mobile (50 utenti) | — | ~€500 |
| Certificati SSL (Let's Encrypt gratis / commerciali) | — | ~€200 |
| Graylog / ELK (VM monitoring, open source) | — | ~€500 (VM quota) |
| Vulnerability scanner (OpenVAS / Nessus) | — | ~€1.000 (Nessus Pro) |
| Formazione sicurezza (2 sessioni/anno) | — | ~€2.000 |
| **Totale** | — | **~€4.200/anno** |
