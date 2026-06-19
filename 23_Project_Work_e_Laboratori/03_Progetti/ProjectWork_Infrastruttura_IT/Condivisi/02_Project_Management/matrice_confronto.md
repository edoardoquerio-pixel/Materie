# Matrice di Confronto — Varianti A / B / C

## Confronto Architetturale

| Criterio | A — Full Cloud GCP | B — On-Premise | C — Ibrido |
|---|---|---|---|
| **HPC** | Istanze C2 su GCP (no InfiniBand) | 16 nodi on-prem (InfiniBand 200 Gbps) | 16 nodi on-prem (InfiniBand) + burst GCP |
| **Pondus** | Cloud Run + Cloud SQL | Server on-prem + Docker | Cloud Run + Cloud SQL |
| **Posta/Collab** | Google Workspace | Zimbra + Workspace (ibrido) | Google Workspace |
| **Identità** | GCDS → Workspace | Samba4 AD | Samba4 AD + GCDS sync |
| **File server** | Google Drive + Cloud Storage | NextCloud on-prem + NAS | Drive (collab) + NextCloud (HPC) |
| **Backup** | Cloud Storage multi-regione | NAS QNAP + replica co-location | NAS QNAP (HPC) + Cloud Storage (servizi) |
| **DR** | Failover automatico GCP multi-regione | Manuale (co-location, RTO 10h) | Cloud automatico (Pondus) + manuale (HPC) |
| **Sicurezza** | GCP compliance nativa | On-prem hardening + co-location | Mista: GCP compliance + on-prem |

## Confronto Performance HPC

| Criterio | A — Full Cloud | B — On-Premise | C — Ibrido |
|---|---|---|---|
| **Interconnessione** | 100 Gbps Ethernet (gVNIC) | InfiniBand 200 Gbps | InfiniBand 200 Gbps |
| **Latenza MPI** | ~10-50 μs | < 2 μs | < 2 μs |
| **Scratch** | 3 TB Local SSD | 1,6 TB NVMe | 1,6 TB NVMe |
| **Burst** | Fino a 16 istanze extra | N/A | Fino a 16 istanze GCP |
| **Performance crash test** | Buona (non InfiniBand) | **Eccellente** | **Eccellente** |

## Confronto DR

| Criterio | A — Full Cloud | B — On-Premise | C — Ibrido |
|---|---|---|---|
| **RPO servizi critici** | ≤1 ora | ≤4 ore | ≤1 ora (Pondus) / ≤24 ore (HPC) |
| **RTO servizi critici** | ≤15 min | ≤10 ore | ≤15 min (Pondus) / ≤4 ore (HPC) |
| **Failover automatico** | ✅ Sì | ❌ No (manuale) | ✅ Parziale (Pondus sì, HPC no) |
| **Test DR** | Semestrale (scriptabile) | Semestrale (manuale) | Semestrale (misto) |

## Confronto Costi (3 anni)

| Voce | A — Full Cloud | B — On-Premise | C — Ibrido |
|---|---|---|---|
| Una tantum (HW + setup) | €22.800 | €306.800 | €285.800 |
| Ricorrente anno 1 | ~€152.640 | ~€98.100 | ~€129.700 |
| Ricorrente anno 2-3 | ~€305.280 | ~€196.200 | ~€259.400 |
| **Totale 3 anni** | **~€480.720** | **~€601.100** | **~€674.900** |
| Extra manodopera | €69.000 | Incluso | Incluso |
| **Totale complessivo** | **~€549.720** | **~€601.100** | **~€674.900** |
| **Delta budget (€701k)** | **+€151.280** | **+€99.900** | **+€26.100** |

## SWOT per Variante

| Variante | Punti di forza | Punti di debolezza |
|---|---|---|
| **A — Full Cloud** | Costo più basso, DR automatico, scalabilità, zero gestione HW | No InfiniBand nativo, dipendenza cloud provider, migrazione complessa |
| **B — On-Premise** | InfiniBand HPC, controllo totale, costi prevedibili | Costo HW elevato (~€307k), DR manuale, gestione HW interna, vincoli sede |
| **C — Ibrido** | InfiniBand HPC + DR cloud automatico, flessibilità, migrazione graduale | Complessità architetturale, doppia gestione (on-prem + cloud), costo intermedio |

## Raccomandazione

| Scenario | Variante consigliata |
|---|---|
| **Cliente vuole InfiniBand per HPC** | B (On-Premise) o C (Ibrido) |
| **Cliente vuole DR automatico e costo minimo** | A (Full Cloud GCP) |
| **Cliente vuole flessibilità e migrazione graduale** | C (Ibrido) |
| **Cliente ha vincoli edificio storico** | A (Full Cloud) o C (HPC in co-location) |
| **Budget minimo** | A (Full Cloud) |
| **Massima performance HPC** | B (On-Premise) |

**Raccomandazione finale**: Variante **C — Ibrida** per il miglior rapporto
costo/beneficio. Mantiene InfiniBand per HPC (requisito critico) e sfrutta
il cloud per DR automatico, scalabilità dei servizi e riduzione costi HW.
