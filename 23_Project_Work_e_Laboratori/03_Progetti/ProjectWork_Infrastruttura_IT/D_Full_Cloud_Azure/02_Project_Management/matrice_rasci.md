# Matrice RASCI — Integrazione IT TP Group

## Legenda

| Codice | Significato |
|---|---|
| **R** | Responsible (esegue) |
| **A** | Accountable (approva) |
| **S** | Support (supporta) |
| **C** | Consulted (consultato) |
| **I** | Informed (informato) |

## Attori

| Codice | Ruolo |
|---|---|
| **PM** | Project Manager (fornitore) |
| **SA** | System Admin (fornitore) |
| **NA** | Network Admin (fornitore) |
| **SO** | Security Officer (fornitore) |
| **CL** | Cliente TP Group (Andrei+) |
| **DR** | Direzione TP Group |
| **UT** | Utenti finali |

## Matrice

| Attività | PM | SA | NA | SO | CL | DR | UT |
|---|---|---|---|---|---|---|---|
| **Assessment** | | | | | | | |
| Assessment infrastruttura | A | R | R | C | C | I | I |
| Gap analysis ISO 27001 | A | S | S | R | C | I | — |
| Analisi requisiti | A | S | S | C | R | C | I |
| **Progettazione** | | | | | | | |
| Architettura rete/VPN | A | S | R | C | C | I | — |
| Specifica HPC | A | R | S | C | C | I | — |
| Architettura Pondus | A | R | S | C | C | I | — |
| Piano migrazione | A | R | S | S | C | C | I |
| Piano sicurezza | A | S | S | R | C | I | — |
| **Approvvigionamento** | | | | | | | |
| Specifiche acquisto HW | A | R | S | C | C | I | — |
| Selezione fornitori | A | S | S | — | R | C | — |
| Emissione ordini | R | — | — | — | A | I | — |
| **Implementazione** | | | | | | | |
| Configurazione rete | A | — | R | S | I | I | — |
| Setup cluster HPC | A | R | S | — | I | I | — |
| Configurazione backup/DR | A | R | — | S | I | I | — |
| Deploy Pondus | A | R | S | S | I | I | — |
| Configurazione sicurezza | A | S | S | R | I | I | — |
| **Migrazione** | | | | | | | |
| Migrazione posta | A | R | — | — | C | I | I |
| Migrazione dati | A | R | S | — | C | I | I |
| Cut-over (shutdown 7gg) | A | R | R | S | C | I | I |
| **Test e collaudo** | | | | | | | |
| Test unitari | A | R | R | S | I | — | — |
| Test integrazione | A | R | R | R | C | I | — |
| Collaudo congiunto | A | S | S | S | R | C | — |
| UAT (User Acceptance Test) | A | S | — | — | C | I | R |
| **Formazione** | | | | | | | |
| Formazione admin | A | R | R | S | I | — | — |
| Formazione utenti | A | S | — | S | I | I | R |
| Documentazione | A | R | R | S | C | I | — |
| **Avvio e supporto** | | | | | | | |
| Go-live | A | R | R | S | C | I | I |
| Supporto post-go-live | A | R | R | S | I | I | S |
| Passaggio di consegne | A | R | R | S | R | C | — |

## Regole di governance

1. **Ogni attività ha UN solo Accountable (A)** — il PM per la maggior parte, il CL per approve HW, la DR per decisioni strategiche
2. **Il PM è Accountable di default** per tutte le attività di progetto salvo diversa indicazione
3. **Il Cliente (CL)** è Consulted per decisioni tecniche e Accountable per approvazione ordini
4. **La Direzione (DR)** è Consulted per decisioni strategiche e Informed su avanzamento
5. **Gli Utenti (UT)** sono Responsible solo per UAT e formazione; Informed per migrazioni
