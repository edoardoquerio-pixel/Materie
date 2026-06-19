# Requisiti Sicurezza ISO 27001 — Variante Ibrida

## Premessa

Nella variante ibrida, la sicurezza è suddivisa tra:
- **On-prem**: responsabilità del fornitore/cliente (HPC, AD, rete sede)
- **Cloud GCP**: compliance nativa GCP (SOC 2, ISO 27001)
- **Integrazione**: connettività ibrida protetta, identità federata

## Business Continuity

### Ridondanza

| Sistema | On-prem | Cloud GCP |
|---|---|---|
| **HPC** | 16 nodi + spare parts | N/A (on-prem) |
| **Pondus** | N/A (cloud) | Multi-regione attivo/passivo |
| **AD** | Samba4 + replica in co-location | GCDS sync workspace |
| **Storage** | NAS QNAP RAID 6 | Cloud Storage multi-regione |
| **Connettività** | Fibra + 4G/5G | HA VPN + Cloud Interconnect |

## Disaster Recovery

| Requisito | Implementazione |
|---|---|
| Delocalizzazione backup | On-prem: NAS co-location / Cloud: multi-regione GCP |
| Fruibilità servizi clienti | Pondus su GCP con failover automatico |
| RPO Pondus | ≤1 ora (PITR Cloud SQL) |
| RTO Pondus | ≤15 min (failover automatico) |
| RPO HPC | ≤24 ore (backup su NAS QNAP) |
| RTO HPC | ≤4 ore (restore nodi on-prem) |

## Sicurezza Accessi

| Area | On-prem | Cloud GCP |
|---|---|---|
| **Cifratura dati a riposo** | LUKS/BitLocker server, NAS AES-256 | AES-256 default GCP |
| **Cifratura dati in transito** | TLS, IPsec, SSH | TLS 1.3, gRPC |
| **VPN** | FortiGate IPsec + FortiClient | Cloud VPN + IAP |
| **MFA** | FortiToken (VPN, admin) | Google 2FA (Workspace, Cloud Console) |
| **IAM** | Samba4 AD ruoli | Cloud IAM + Identity Platform |
| **Audit** | Syslog centralizzato (ELK) | Cloud Audit Logs |
| **Patch management** | CIS benchmark, patch 7/30gg | Managed services (patch automatico) |

### Autenticazione ibrida

```
[Utente] ── LDAP/MFA ──→ [Samba4 AD on-prem]
    │                            │
    │                    [LDAPS + GCDS]
    │                            │
    └──── OAuth 2.0 ──────────→ [Google Workspace / Cloud Run]
```

## Adeguamento ISO 27001

| Controllo | On-prem | Cloud | Gap? |
|---|---|---|---|
| A.5 — Policy | ✅ Bozza | ✅ GCP compliance | 🟡 Unificare policy |
| A.6 — Organizzazione | ✅ Ruoli | ✅ Ruoli IAM | ✅ |
| A.9 — Accesso | ✅ AD + MFA | ✅ IAM + 2FA | ✅ |
| A.10 — Crittografia | ✅ LUKS, TLS | ✅ AES-256, TLS 1.3 | ✅ |
| A.12 — Backup | ✅ NAS + co-location | ✅ Cloud SQL PITR | ✅ |
| A.13 — Rete | ✅ VLAN, VPN | ✅ VPC, Cloud VPN | ✅ |
| A.17 — Continuità | 🟡 DR manuale HPC | ✅ DR automatico Pondus | 🟡 HPC DR da migliorare |

✅ = Coperto / 🟡 = Parzialmente coperto

## Costi sicurezza

| Voce | Annuale |
|---|---|
| FortiToken (50 utenti) | ~€500 |
| Security Command Center Standard | Gratuito |
| Cloud Audit Logs retention | ~$600 |
| Certificati SSL | ~€200 |
| Vulnerability scanning (OpenVAS) | Gratuito |
| Formazione sicurezza | ~€2.000 |
| **Totale** | **~€3.300/anno** |
