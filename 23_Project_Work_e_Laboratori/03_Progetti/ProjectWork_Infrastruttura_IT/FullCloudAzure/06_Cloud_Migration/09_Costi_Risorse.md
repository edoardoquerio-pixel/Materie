# 09 — Costi Risorse (Extra Budget)

> **Documento:** Costi del personale IT interno per la migrazione Full Cloud Azure  
> **Data:** Luglio 2026

---

## Premessa

Come da intervista cliente (18/06/2026), i costi di **sistemista (€500/giorno)** e **Project Manager (€650/giorno)** sono considerati **extra budget** e coprono il personale IT interno per i 3 anni successivi al progetto. Non vanno inclusi nel budget totale di €520.000.

---

## Stima giorni per fase

| Fase | Sistemista (gg) | PM (gg) | Note |
| --- | --- | --- | --- |
| F0 — Foundation | 10 | 2 | Setup tenant, sync AD, VNet |
| F1 — Posta | 8 | 2 | Migrazione 50 caselle |
| F2 — File | 6 | 1 | Migrazione dati |
| F3 — Dynamics | 5 | 3 | Supporto a consulente Dynamics |
| F4 — Azure DevOps | 4 | 1 | Migrazione repo, setup pipelines |
| F5 — Media Wiki | 2 | 1 | Setup VM e migrazione contenuti |
| F6 — Test | 5 | 3 | Esecuzione test |
| F7 — Dismissione | 5 | 2 | Spegnimento legacy, report |
| Supporto post-migrazione (2 settimane) | 10 | 2 | Assistenza post go-live |
| **Totale** | **55 gg** | **17 gg** | |

---

## Costo totale risorse

| Ruolo | Giorni | Costo/giorno | Totale |
| --- | --- | --- | --- |
| Sistemista senior | 55 | € 500 | € 27.500 |
| Project Manager | 17 | € 650 | € 11.050 |
| **Totale risorse** | **72 gg** | | **€ 38.550** |

### Costi su 3 anni (ciclo vita progetto)

| Anno | Sistemista (gg) | PM (gg) | Costo annuale |
| --- | --- | --- | --- |
| Anno 1 (migrazione + supporto) | 55 | 17 | € 38.550 |
| Anno 2 (manutenzione ordinaria) | 20 | 5 | € 13.250 |
| Anno 3 (manutenzione ordinaria) | 20 | 5 | € 13.250 |
| **Cumulato 3 anni** | **95 gg** | **27 gg** | **€ 65.050** |

---

## Riepilogo budget + risorse

| Voce | Budget | Extra budget |
| --- | --- | --- |
| Budget totale progetto | € 520.000 | — |
| Spesa già prevista (piano_costi.md) | € 272.950 | — |
| Migrazione Microsoft (una tantum + anno 1) | ~€ 51.524 | — |
| **Sistemista (55 gg)** | — | € 27.500 |
| **PM (17 gg)** | — | € 11.050 |
| **Totale risorse migrazione** | — | **€ 38.550** |
| **Margine residuo** | **~€ 195.526** | — |
