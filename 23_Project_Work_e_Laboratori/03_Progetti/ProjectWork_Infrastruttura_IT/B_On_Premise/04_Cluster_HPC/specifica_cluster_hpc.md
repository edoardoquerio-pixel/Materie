# Specifica Cluster HPC — Variante On-Premise

## REQUISITI

- 8 nodi esistenti Thema (HW proprietario, InfiniBand) + 8 nuovi nodi da acquistare
- 2 CPU per nodo, ≥24 core per CPU, clock rate elevato
- 8 GB RAM per core
- NO GPU
- Scratch: ≥1,6 TB per nodo (SSD NVMe locale)
- OS: Linux (Ubuntu 24.04 LTS / Rocky Linux 9)
- Rete: Ethernet + InfiniBand (100/200 Gbps)
- NO virtualizzazione, NO container per nodi di calcolo
- Raffreddamento: problema — condizionamento già al limite
- Spazio rack: saturo — necessaria espansione
- Budget: ~€250k

## SOLUZIONE

### Architettura

```
[Front-end VM Linux] ---- [Ethernet 10 GbE] ---- [Storage NFS]
        |
[Switch InfiniBand 200 Gbps]
        |
[Nodi calcolo × 16] ---- [Disco locale SSD NVMe 1,6 TB]
  8 esistenti + 8 nuovi

[Switch Ethernet 25 GbE] ---- [Rete aziendale / Internet]
```

### Specifica nodi di calcolo

| Parametro | Valore |
|---|---|
| **Processore** | 2× AMD EPYC 9474F (48 core, 3,6 GHz base, 4,1 GHz boost) |
| **Core totali per nodo** | 96 |
| **RAM** | 768 GB (12× 64 GB DDR5-4800 ECC) — 8 GB/core |
| **Storage scratch** | 2× 800 GB SSD NVMe U.2 (1,6 TB totali, RAID 0 per performance) |
| **Rete InfiniBand** | 1× ConnectX-7 HDR (200 Gbps) o equivalente |
| **Rete Ethernet** | 1× 25 GbE (amministrazione + storage) |
| **Form factor** | 2U rack |
| **Alimentazione** | 2× 1600W PSU ridondanti |

### Nodi esistenti

| Parametro | Note |
|---|---|
| **Nodi** | 8 nodi HW proprietario Thema |
| **Rete** | InfiniBand proprietario |
| **Compatibilità** | Da verificare con integrazione nuovi nodi |
| **Fine vita** | Valutare sostituzione graduale (2-3 anni) |

### Rete

| Componente | Specifica | Q.tà |
|---|---|---|
| **Switch InfiniBand** | NVIDIA QM9700 (40 porte HDR 200 Gbps) | 1 |
| **Switch Ethernet** | NVIDIA Spectrum-3 SN4600 (32 porte 25 GbE) | 1 |
| **Front-end** | VM Linux (8 vCPU, 32 GB RAM, 100 GB SSD) | 1 |
| **Storage condiviso NFS** | Server 2U, 32 core, 128 GB RAM, 10 TB SSD | 1 |

### Raffreddamento

| Problema | Soluzione proposta |
|---|---|
| Condizionamento al limite | Nuovo armadio rack con raffreddamento dedicato (InRow DX o Chiller) |
| Posizionamento | Armadio aggiuntivo in sala server esistente (se spazio) o in co-location |
| Consumo 8 nuovi nodi | ~6-8 kW aggiuntivi (da piano elettrico) |
| UPS | Upgrade per carico aggiuntivo: +5 kVA |

## DIMENSIONAMENTO

| Elemento | Specifica | Costo stimato |
|---|---|---|
| 8 nodi calcolo AMD EPYC 9474F | 96 core, 768 GB, 1,6 TB NVMe | ~€180.000 |
| Switch InfiniBand QM9700 | 40 porte HDR 200 Gbps | ~€25.000 |
| Switch Ethernet 25 GbE | 32 porte | ~€8.000 |
| Cavi InfiniBand + Ethernet | 16× HDR + cablaggio | ~€4.000 |
| Storage NFS condiviso | 10 TB SSD | ~€12.000 |
| Raffreddamento (armadio dedicato) | InRow DX 12 kW | ~€15.000 |
| Armadio rack 42U + PDU | Nuovo armadio | ~€3.000 |
| Installazione e configurazione | 10 gg/uomo | ~€5.000 |
| **Totale** | | **~€252.000** |

## COSTI OPERATIVI ANNUALI

| Voce | Costo annuo |
|---|---|
| Energia elettrica (8 nodi + rete, ~8 kW × 8760h × €0,20/kWh) | ~€14.000 |
| Raffreddamento dedicato | ~€3.000 |
| Manutenzione HW (garanzia estesa anno 2-3) | ~€5.000 |
| Canone InfiniBand (sottoscrizione) | ~€2.000 |
| **Totale annuo** | **~€24.000** |

## Confronto: Cluster esistente + nuovi nodi

| Metric | Attuale (8 nodi) | Dopo upgrade (16 nodi) |
|---|---|---|
| Core totali | Variabile (HW proprietario) | 96 × 8 + esistenti |
| RAM totale | Variabile | 6.144 GB (nuovi) + esistenti |
| Interconnessione | InfiniBand proprietario | InfiniBand HDR 200 Gbps |
| Storage scratch | HD locale | NVMe SSD 1,6 TB per nodo |
| Consumo | ~5-8 kW | ~11-16 kW |
| Spazio rack | 16U | 16U + 2U switch = 18U aggiuntivi |
