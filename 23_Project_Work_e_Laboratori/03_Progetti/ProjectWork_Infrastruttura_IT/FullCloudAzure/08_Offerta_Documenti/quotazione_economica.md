# Quotazione Economica — Variante Full Cloud Azure

## Riepilogo costi

```
Budget 520.000€
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  INVESTIMENTO INIZIALE (una tantum):          78.200€         ║
║  ┌──────────────────────────────────────────────────────────╢
║  │ Rete/VPN:        23.000€                                 ║
║  │ Sicurezza:       11.500€                                 ║
║  │ HPC:             16.000€                                 ║
║  │ Pondus:           8.500€                                 ║
║  │ Cloud Migration: 12.000€                                 ║
║  │ Backup/DR:        7.200€                                 ║
║  └──────────────────────────────────────────────────────────╢
║                                                              ║
║  SERVIZI CLOUD ANNO 1 (ricorrenti):           45.178€         ║
║  ┌──────────────────────────────────────────────────────────╢
║  │ M365 Business Premium:       12.360€/anno                 ║
║  │ Dynamics 365 Sales + BC:     21.828€/anno                 ║
║  │ Azure (App, SQL, VM, DevOps): 5.336€/anno                 ║
║  │ VPN Gateway:                  1.170€/anno                 ║
║  │ Backup + DR:                  1.380€/anno                 ║
║  │ HPC CycleCloud:               3.464€/anno (SPOT + head)   ║
║  └──────────────────────────────────────────────────────────╢
║                                                              ║
║  TOTALE ANNO 1:                             123.738€          ║
║                                                              ║
║  MARGINE RESIDUO:                           ~396.262€         ║
║                                                              ║
║  COSTI RISORSE (extra budget):               38.550€          ║
║  (sistemista 55gg + PM 17gg)                                 ║
╚══════════════════════════════════════════════════════════════╝
```

## Dettaglio costi per area

| Area | Una tantum | Ricorrente/anno | 3 anni |
|---|---|---|---|
| Rete / VPN | € 23.000 | € 4.200 (2° ISP) | € 35.600 |
| Sicurezza ISO 27001 | € 11.500 | € 0 | € 11.500 |
| Cluster HPC ibrido | € 16.000 | € 3.464 (Azure CycleCloud SPOT + head node) | € 26.392 |
| Pondus su Azure | € 8.500 | € 2.134 (App + SQL) | € 14.902 |
| Cloud Migration (M1-M11) | € 12.000 | € 35.740 (M365 + Dynamics + Azure) | € 119.220 |
| Backup / DR | € 7.200 | € 1.380 | € 11.340 |
| **Totale** | **€ 78.200** | **€ 45.538** | **€ 214.814** |

## Costi extra budget (risorse interne)

| Ruolo | Giorni (anno 1) | Costo/giorno | Totale |
|---|---|---|---|
| Sistemista senior | 55 | € 500 | € 27.500 |
| Project Manager | 17 | € 650 | € 11.050 |
| **Totale risorse** | **72 gg** | | **€ 38.550** |
| Anno 2 (manutenzione) | 20gg + 5gg | | € 13.250 |
| Anno 3 (manutenzione) | 20gg + 5gg | | € 13.250 |
| **Cumulato 3 anni risorse** | | | **€ 65.050** |

## Confronto: Full Cloud Azure vs piano base (ibrido)

| Voce | Piano base (ibrido) | Full Cloud Azure | Delta |
|---|---|---|---|
| Nuovi nodi HPC fisici | € 192.000 | € 16.000 (on-prem upgrade) | **-€ 176.000** |
| Infrastruttura on-prem (UPS, condiz.) | € 15.000 | € 0 | **-€ 15.000** |
| Servizi cloud | € 51.524/anno | € 45.538/anno | **-€ 5.986/anno** |
| Margine residuo anno 1 | ~€ 195.526 | ~€ 396.262 | **+€ 200.736** |

La variante Full Cloud Azure libera **~€ 201.000 aggiuntivi** rispetto al piano ibrido, grazie all'eliminazione dell'acquisto di nuovi nodi HPC fisici. I costi burst Azure includono il CycleCloud head node dedicato (Standard_D2s_v3, 24/7) e istanze SPOT per i nodi di calcolo (8 nodi, stessi core totali della configurazione precedente).
