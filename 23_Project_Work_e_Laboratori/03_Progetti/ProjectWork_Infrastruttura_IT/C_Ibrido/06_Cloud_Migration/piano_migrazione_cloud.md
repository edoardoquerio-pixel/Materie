# Piano Migrazione Cloud — Variante Ibrida

## REQUISITI

- HPC rimane on-premise (16 nodi)
- Servizi collaborativi e gestionali migrati su GCP/Workspace
- Pondus migrato su GCP
- Identità: ibrida (Samba4 AD on-prem + Google Workspace)
- Backup: on-prem (HPC) + cloud (servizi migrati)
- DR: cloud per servizi critici (Pondus), on-prem con replica off-site

## SOLUZIONE

### Matrice servizi: On-prem vs Cloud

| Servizio | Location | Motivo |
|---|---|---|
| **HPC** | On-prem | InfiniBand critico, latenza |
| **Pondus** | GCP (Cloud Run + SQL) | Pubblicazione online, scalabilità |
| **Posta** | Google Workspace | Unificazione con Pro Studio |
| **AD** | On-prem (Samba4) + sync GCP | Autenticazione HPC |
| **File** | Google Drive (collab) + NextCloud on-prem (HPC data) | Ibrido per latenza |
| **Contabilità** | Odoo (SaaS) | Sostituzione Profis |
| **CRM** | Odoo (SaaS) | Unificazione |
| **Backup** | On-prem (NAS, HPC) + GCP (servizi cloud) | 3-2-1 rule |

### Ordine migrazione

1. **Posta e identità** (Settimane 1-3): Workspace + GCDS sync
2. **File collaborativi** (Settimane 3-5): Drive per ufficio, NextCloud per HPC
3. **Gestionale** (Settimane 4-8): Profis→Odoo, SugarCRM→Odoo, Kimai→Odoo
4. **Pondus** (Settimane 6-10): Cloud Run + Cloud SQL, cut-over con 2gg shutdown
5. **Backup DR** (Settimane 8-10): Configurazione backup cloud + replica off-site

### Integrazione identità

```
[Samba4 AD on-prem] ←── LDAP ──→ [HPC cluster]
       |
[GCDS sync] ────────────────→ [Google Workspace]
       |
[Identity Platform] ←── LDAPS ──→ [Pondus on Cloud Run]
```

## COSTI

| Voce | Una tantum | Annuale |
|---|---|---|
| Google Workspace (50 utenti Business) | — | ~€7.200 |
| Odoo Enterprise (50 utenti) | — | ~€14.940 |
| GCDS + Identity Platform | — | ~€600 |
| GCP servizi (Pondus, backup, networking) | — | ~€35.000 |
| **Totale ricorrente** | — | **~€57.740/anno** |
