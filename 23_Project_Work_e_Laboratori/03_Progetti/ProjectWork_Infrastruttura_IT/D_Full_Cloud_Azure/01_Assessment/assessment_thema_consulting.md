# Assessment AS-IS — Thema Consulting

## 1. Profilo Aziendale

Thema Consulting srl nasce alla fine degli anni '90 dall'idea di tre ingegneri
progettisti, attivi da circa un decennio nel settore della progettazione
meccanica. L'azienda si occupa prevalentemente di **progettazione strutturale
in ambito automotive**, con simulazioni di crash test e analisi agli elementi
finiti (FEA). La sede è di proprietà, situata in un edificio storico del centro
di Torino.

Il personale è composto da **30 persone** (tra dipendenti e collaboratori).
Gli uffici possono ospitare fino a **40 postazioni di lavoro** fisse, ciascuna
composta da scrivania con connessione LAN e monitor esterno a cui collegare il
proprio laptop aziendale. Ogni dipendente dispone di un laptop aziendale.
Non sono richieste soluzioni VDI.

---

## 2. Datacenter

### 2.1 Infrastruttura fisica

| Elemento | Descrizione |
|---|---|
| **Armadi rack** | 2 armadi rack, entrambi saturi — non è possibile installare ulteriore hardware |
| **Virtualizzazione** | 2 host fisici con VMWare |
| **Storage SAN** | 1 SAN NetApp (24 TB totali) on premise |
| **UPS** | Gruppo di continuità in grado di sopperire a interruzioni di corrente fino a 10 minuti |
| **Condizionamento** | Sistema di raffreddamento al limite per l'attuale carico termico, difficilmente potenziabile a causa dei vincoli strutturali dell'edificio storico |

**Stima costi annui presunti:**
- Elettricità datacenter (server, storage, condizionamento): ~6.000–8.000 €/anno
- Manutenzione SAN NetApp (contratto assistenza): ~3.500–5.000 €/anno
- Canone assistenza VMWare (2 host): ~2.000–3.000 €/anno

### 2.2 Backup

| Elemento | Descrizione |
|---|---|
| **Dispositivo** | NAS QNAP dedicato, 32 TB totali |
| **Tipologia** | Backup su disco locale on premise |
| **Ubicazione** | Stessa sede del datacenter (nessuna delocalizzazione) |

**Stima costi annui presunti:**
- Manutenzione / sostituzione HDD NAS: ~500–800 €/anno
- Energia elettrica NAS: ~200–400 €/anno

---

## 3. Rete e Connettività

### 3.1 Firewall e perimetrale

| Elemento | Descrizione |
|---|---|
| **Firewall** | 1 x FortiGate FG-60F |
| **Ruolo** | Protezione perimetrale della rete aziendale, gestione connettività Internet e VPN |

**Stima costi annui presunti:**
- Canone FortiGate (sottoscrizione servizi di sicurezza, aggiornamenti firmware): ~600–900 €/anno

### 3.2 Rete locale

La rete LAN interna serve le 40 postazioni degli uffici tramite connettività
Ethernet cablata (ciascuna postazione dispone di presa LAN a muro). Non sono
disponibili dettagli sulla topologia di rete (switch, cablaggio, VLAN).

---

## 4. Cluster HPC

| Elemento | Descrizione |
|---|---|
| **Nodi di calcolo** | 8 nodi fisici dedicati al calcolo HPC |
| **Hardware** | Soluzioni HW proprietarie, schede InfiniBand per interconnessione |
| **Sistema operativo** | Linux |
| **Front-end** | 1 macchina virtuale Linux che funge da nodo di accesso (Front-end) |
| **Utilizzo** | Esclusivo riservato al personale interno dell'azienda |
| **Scopo** | Simulazioni strutturali (crash test), analisi FEM, calcolo parallelo |

Il cluster HPC è l'unico sistema in grado di eseguire le simulazioni di
calcolo strutturale richieste dai clienti automotive e aerospace. L'hardware
è caratterizzato da soluzioni proprietarie, inclusi i controller e le schede
di interconnessione InfiniBand.

**Stima costi annui presunti:**
- Elettricità 8 nodi HPC + Front-end (consumo medio ~5–8 kW): ~8.000–12.000 €/anno
- Raffreddamento quota HPC: ~3.000–5.000 €/anno
- Manutenzione hardware (ricambi, assistenza): ~3.000–5.000 €/anno

---

## 5. Applicazione Pondus

| Elemento | Descrizione |
|---|---|
| **Tipologia** | Web application per ottimizzazione pesi materiali |
| **Stack tecnologico** | C# / .NET, MS IIS (Web server), MS SQL Server (DB server) |
| **HW dedicato** | 1 CPU Xeon Silver 4110, 64 GB RAM, 1,2 TB HDD (fisico dedicato) |
| **Anno attivazione** | 2015 |
| **Clientela** | Cerchia ristretta di clienti in ambito automotive (auto sportive) e aerospace |
| **Servizio** | Ottimizzazione dei pesi dei materiali per la scelta di componenti speciali |

Il servizio Pondus è erogato on premise ed è accessibile da remoto ai clienti
attuali tramite la connettività Internet della sede.

**Stima costi annui presunti:**
- Licenza MS SQL Server Standard: ~1.500–2.500 €/anno (o costo una tantum già ammortizzato)
- Manutenzione HW dedicato: ~500–800 €/anno
- Elettricità: ~300–500 €/anno

---

## 6. Servizi di Infrastruttura (Virtual Machines)

La quasi totalità dei servizi aziendali è ospitata su macchine virtuali Linux
in esecuzione sui due host VMWare. Di seguito il dettaglio per servizio.

### 6.1 Posta elettronica e calendario

| Elemento | Descrizione |
|---|---|
| **Software** | Zimbra |
| **Piattaforma** | VM Linux su infrastruttura VMWare |
| **Dominio** | Gestione posta elettronica e calendari per tutti i dipendenti |

**Stima costi annui presunti:**
- Elettricità / risorse VM (quota parte): ~200–400 €/anno
- Manutenzione / amministrazione (tempo sistemista interno): ~1.000–2.000 €/anno

### 6.2 Autenticazione e identità

| Elemento | Descrizione |
|---|---|
| **Software** | Samba4 in configurazione Active Directory |
| **Piattaforma** | VM Linux |
| **Ruolo** | Gestione utenti, autenticazione centralizzata, policy di dominio |

**Stima costi annui presunti:**
- Quota parte risorse VM: ~100–200 €/anno

### 6.3 File server e condivisione documenti

| Elemento | Descrizione |
|---|---|
| **Software** | NextCloud |
| **Piattaforma** | VM Linux |
| **Ruolo** | Condivisione file, sincronizzazione tra dispositivi, accesso remoto ai documenti |

**Stima costi annui presunti:**
- Quota parte risorse VM + storage: ~300–500 €/anno

### 6.4 Sviluppo software e versioning

| Elemento | Descrizione |
|---|---|
| **Software** | GiTea (self hosted) |
| **Piattaforma** | VM Linux |
| **Ruolo** | Repository Git per il versionamento del codice sorgente interno |

**Stima costi annui presunti:**
- Quota parte risorse VM: ~100–200 €/anno

### 6.5 Documentazione tecnica e wiki

| Elemento | Descrizione |
|---|---|
| **Software** | MediaWiki (self hosted) |
| **Piattaforma** | VM Linux |
| **Ruolo** | Documentazione tecnica interna, knowledge base aziendale |

**Stima costi annui presunti:**
- Quota parte risorse VM: ~100–200 €/anno

---

## 7. Applicazioni gestionali

### 7.1 Contabilità (Profis)

| Elemento | Descrizione |
|---|---|
| **Software** | Profis |
| **Piattaforma** | Server Windows on premise |
| **Ruolo** | Gestione contabilità aziendale |

**Stima costi annui presunti:**
- Canone assistenza / licenza Profis: ~1.500–2.500 €/anno
- Quota parte manutenzione HW / VM: ~300–500 €/anno

### 7.2 CRM (SugarCRM)

| Elemento | Descrizione |
|---|---|
| **Software** | SugarCRM (self hosted) |
| **Piattaforma** | VM Linux |
| **Ruolo** | Gestione relazioni con i clienti |

**Stima costi annui presunti:**
- Quota parte risorse VM: ~100–200 €/anno

### 7.3 Time sheet (Kimai)

| Elemento | Descrizione |
|---|---|
| **Software** | Kimai (self hosted) |
| **Piattaforma** | VM Linux |
| **Ruolo** | Rilevazione e gestione ore lavorate |

**Stima costi annui presunti:**
- Quota parte risorse VM: ~100–200 €/anno

---

## 8. Produttività e collaborazione

### 8.1 Suite per ufficio

| Elemento | Descrizione |
|---|---|
| **Software** | Microsoft 365 (licenze) + LibreOffice (alternativa open source) |
| **Ruolo** | Elaborazione documenti, fogli di calcolo, presentazioni |

**Stima costi annui presunti:**
- Licenze Microsoft 365 Business (stima 30 utenti): ~3.600–4.800 €/anno

### 8.2 Videoconferenza e messaggistica istantanea

| Elemento | Descrizione |
|---|---|
| **Software** | Microsoft Teams |
| **Ruolo** | Comunicazione interna, riunioni virtuali, collaborazione da remoto |

**Stima costi annui presunti:**
- Incluse nelle licenze Microsoft 365 (nessun costo aggiuntivo stimato)

---

## 9. Sede

| Elemento | Descrizione |
|---|---|
| **Ubicazione** | Centro di Torino, edificio storico |
| **Proprietà** | Di proprietà dell'azienda |
| **Vincoli** | Le caratteristiche strutturali dell'edificio storico limitano le opzioni di ampliamento del datacenter e il potenziamento del condizionamento |

Non sono disponibili costi di gestione della sede (affitto non applicabile in
quanto di proprietà; utenze e manutenzione ordinaria a carico dell'azienda).

---

## 10. Stima Costi Operativi Attuali (riepilogo annuale)

La tabella seguente riporta una stima dei costi operativi ricorrenti per
l'infrastruttura IT di Thema Consulting allo stato attuale. Le cifre sono
da intendersi come ordini di grandezza basati su hardware, software e
utenze identificati; non includono il costo del personale IT interno.

| Categoria | Voce | Stima costo annuo |
|---|---|---|
| **Datacenter** | Energia elettrica server, storage e condizionamento | 6.000–8.000 € |
| | Manutenzione SAN NetApp | 3.500–5.000 € |
| | Canone assistenza VMWare (2 host) | 2.000–3.000 € |
| **Backup** | Manutenzione NAS QNAP | 500–800 € |
| | Energia elettrica NAS | 200–400 € |
| **Rete** | Sottoscrizione FortiGate | 600–900 € |
| **Cluster HPC** | Energia elettrica 8 nodi + Front-end | 8.000–12.000 € |
| | Raffreddamento quota HPC | 3.000–5.000 € |
| | Manutenzione hardware HPC | 3.000–5.000 € |
| **Pondus** | Manutenzione HW dedicato | 500–800 € |
| | Licenza MS SQL Server (ammortamento o SaaS) | 1.500–2.500 € |
| | Energia elettrica HW Pondus | 300–500 € |
| **Software gestionali** | Canone assistenza Profis | 1.500–2.500 € |
| | Manutenzione VM servizi (Zimbra, Samba4, NextCloud, GiTea, MediaWiki, SugarCRM, Kimai) | 2.000–4.000 € |
| **Produttività** | Licenze Microsoft 365 Business (30 utenti) | 3.600–4.800 € |
| **TOTALE STIMATO** | | **36.700–53.200 €/anno** |

*Nota: le stime non includono il costo del personale IT interno (sistemista),
costi di connettività Internet, manutenzione della rete LAN (switch, cablaggio),
né eventuali canoni per servizi cloud accessori. I costi energia sono stimati
su un costo medio di ~0,20–0,25 €/kWh per utenza business in Italia.*
