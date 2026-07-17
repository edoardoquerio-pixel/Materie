# Fondamenti ICT — Note Complete

## 1. Hardware del Calcolatore

**Architettura di Von Neumann:**
- CPU (Control Unit + ALU + Registri) ← Bus → Memoria (RAM/ROM) ← Bus → I/O
- Ciclo macchina: Fetch → Decode → Execute → Store

**Componenti:**
| Componente | Funzione | Esempi |
|------------|----------|--------|
| CPU | Esecuzione istruzioni | Intel Core i7, AMD Ryzen |
| RAM | Memoria volatile dati temporanei | DDR4, DDR5 |
| ROM/SSD | Memoria persistente | NVMe, SATA SSD |
| Scheda Madre | Interconnessione componenti | Chipset, socket, slot |
| Bus di sistema | Trasferimento dati | PCIe, SATA, USB |

## 2. Rappresentazione dei Dati

**Sistemi numerici:**
- Binario (base 2): 0, 1
- Ottale (base 8): 0-7
- Decimale (base 10): 0-9
- Esadecimale (base 16): 0-9, A-F

**Conversioni:**
- Bin→Dec: somma potenze di 2
- Dec→Bin: divisioni successive per 2
- Hex↔Bin: ogni cifra hex = 4 bit

**Unità di misura:**
1 byte = 8 bit
1 KB = 1024 byte
1 MB = 1024 KB
1 GB = 1024 MB
1 TB = 1024 GB

## 3. Software

**Categorie:**
- **Sistema Operativo**: gestione risorse HW (Windows, Linux, macOS)
- **Applicativo**: compiti specifici (browser, Office, DB)
- **Middleware**: strato tra OS e applicazioni

**Funzioni del SO:**
- Gestione processi (scheduling)
- Gestione memoria (paginazione, segmentazione)
- File system (organizzazione dati su disco)
- I/O management (driver, interrupt)
- Sicurezza (permessi, utenti)

## 4. Reti — Fondamenti

**Topologie:** Stella (switch), Anello, Bus, Maglia, Albero

**Modello OSI (7 livelli):**
1. Fisico — cavi, segnali, bit
2. Data Link — frame, MAC, switch
3. Rete — pacchetti, IP, routing
4. Trasporto — segmenti, TCP/UDP
5. Sessione — dialogo, RPC
6. Presentazione — crittografia, codifica
7. Applicazione — HTTP, FTP, SMTP

**Modello TCP/IP (4 livelli):**
- Network Access → Internet → Transport → Application
- Basato su RFC 1122, standard de-facto di Internet

## 5. Architetture dei Calcolatori

**CISC vs RISC:**
| CISC | RISC |
|------|------|
| Istruzioni complesse | Istruzioni semplici |
| Microprogrammato | Pipeline hardware |
| x86/64 (Intel, AMD) | ARM, RISC-V |

**Multiprocessing:**
- SMP (Symmetric Multi-Processing): CPU uguali condividono bus
- NUMA (Non-Uniform Memory Access): CPU con memoria locale

## 6. Storage

**Gerarchia di memoria:**
Registri → Cache L1/L2/L3 → RAM → SSD → HDD → Nastro
(Più veloce, più piccolo, più costoso → Più lento, più grande, più economico)

**RAID:**
- RAID 0: striping (performance, nessuna ridondanza)
- RAID 1: mirroring (ridondanza, 50% capacità)
- RAID 5: striping + parità distribuita (1 disco tolleranza)
- RAID 6: doppia parità (2 dischi tolleranza)
- RAID 10: mirroring + striping (performance + ridondanza)

## 7. Virtualizzazione (cenni)

**Hypervisor Type-1 (bare-metal):** VMware ESXi, KVM, Hyper-V
**Hypervisor Type-2 (hosted):** VirtualBox, VMware Workstation
**Container:** Docker, LXC (kernel condiviso, isolation via namespaces/cgroups)
