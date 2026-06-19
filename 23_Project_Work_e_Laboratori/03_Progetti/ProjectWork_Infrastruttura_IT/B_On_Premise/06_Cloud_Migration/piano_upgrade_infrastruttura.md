# Piano Upgrade Infrastruttura — Variante On-Premise

## REQUISITI

- Datacenter attuale saturo (2 rack, nessuno spazio per espansione)
- Condizionamento al limite termico (difficilmente potenziabile in edificio storico)
- UPS autonomia 10 minuti (insufficiente per spegnimento ordinato cluster HPC)
- Necessità: +8 nodi HPC + nuovo server Pondus + nuova rete (switch, firewall)
- Budget stimato: ~€250k (co-location) o espansione on-site
- Lead time HW: 8-16 settimane

## SOLUZIONE

### Opzione A: Co-location (raccomandata)

Affittare spazio in datacenter professionale (Torino/Milano) per ospitare l'espansione.

| Vantaggio | Dettaglio |
|---|---|
| Raffreddamento professionale | Nessun vincolo edificio storico |
| Alimentazione ridondata | UPS + generatore, SLA 99,99% |
| Connettività multipla | Peering diretto, più ISP, BGP |
| Crescita futura | Possibilità espansione senza vincoli fisici |
| Security fisica | Controllo accessi, videosorveglianza, badge |

| Svantaggio | Dettaglio |
|---|---|
| Costo ricorrente | Canone mensile co-location |
| Latenza aggiuntiva | ~1-3 ms rispetto a sede locale |
| Connettività necessaria | VPN LAN-to-LAN tra sede e co-location |

### Opzione B: Espansione on-site (se sede lo permette)

- Nuovo armadio rack 42U in sala server (se spazio disponibile)
- Raffreddamento InRow DX dedicato (12 kW)
- UPS aggiuntivo o upgrade esistente
- Nuovo circuito elettrico dedicato

## Confronto opzioni

| Criterio | Co-location | Espansione on-site |
|---|---|---|
| Costo iniziale | ~€10.000 (set-up) | ~€25.000 (armadio, raffreddamento, UPS, elettrico) |
| Costo annuo | ~€12.000-€18.000 | ~€3.000 (energia + manutenzione) |
| Capacità raffreddamento | Illimitata (SLA datacenter) | 12 kW (nuovo InRow) |
| Crescita futura | Alta (espansione rapida) | Bassa (vincoli edificio storico) |
| Sicurezza fisica | Professionale | Base (sede aziendale) |
| Connettività | Multi-ISP, BGP | Singolo ISP + backup 4G |
| Latenza | +1-3 ms | 0 ms (locale) |
| **Scelta** | **✅ Raccomandata** | Solo se budget non disponibile |

## Piano di implementazione

### Fase 1: Co-location setup (Settimane 1-6)

| Attività | Durata | Dipendenza |
|---|---|---|
| Valutazione provider co-location (TO/MI) | 1 settimana | — |
| Contratto e ordine spazio/link | 1 settimana | Scelta provider |
| Acquisto armadio + raffreddamento InRow | 2 settimane | Budget approvato |
| Installazione rack, PDU, raffreddamento | 1 settimana | Consegna HW |
| Connettività inter-data center | 1 settimana | Installazione rack |
| VPN LAN-to-LAN sede ↔ co-location | 1 settimana | Connettività attiva |

### Fase 2: HW placement (Settimane 7-12)

| Attività | Durata | Dipendenza |
|---|---|---|
| Consegna nodi HPC (lead time 8-16 settimane) | — | Ordine in Fase 1 |
| Rack e cablaggio nodi HPC in co-location | 1 settimana | Consegna |
| Configurazione InfiniBand + Ethernet | 1 settimana | Rack completato |
| Collocazione server Pondus in co-location | 1 giorno | — |
| Test connettività HPC + Pondus | 1 settimana | Configurazione |

## DIMENSIONAMENTO SPAZIO

| Equipaggiamento | Spazio | Consumo | Raffreddamento |
|---|---|---|---|
| 8 nuovi nodi HPC (2U × 8) | 16U | ~6-8 kW | InRow DX 12 kW |
| Switch InfiniBand (1U) | 1U | ~0,5 kW | Incluso |
| Switch Ethernet (1U) | 1U | ~0,3 kW | Incluso |
| Storage NFS (2U) | 2U | ~0,5 kW | Incluso |
| Server Pondus (2U) | 2U | ~0,3 kW | Incluso |
| **Totale** | **22U** | **~8-10 kW** | **Coperto** |

## COSTI

| Voce | Una tantum | Annuale |
|---|---|---|
| **Co-location** | | |
| Set-up co-location (installazione, cross-connect) | ~€5.000 | — |
| Canone mensile spazio 22U + 4 kW | — | ~€15.000 |
| Connettività extra (cross-connect 1 Gbps) | — | ~€3.000 |
| **Espansione on-site alternativa** | | |
| Armadio rack 42U + PDU | ~€2.500 | — |
| Raffreddamento InRow DX 12 kW | ~€15.000 | ~€1.000 |
| UPS 5 kVA aggiuntivo | ~€4.000 | ~€200 |
| Impianto elettrico dedicato | ~€5.000 | — |
| **Totale co-location** | **~€5.000** | **~€18.000/anno** |
| **Totale on-site** | **~€26.500** | **~€1.200/anno** |
