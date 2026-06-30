# Gap Analysis — Stato AS-IS vs. Requisiti ISO/IEC 27001

## Introduzione

La norma **ISO/IEC 27001** definisce i requisiti per un Sistema di Gestione della
Sicurezza delle Informazioni (Information Security Management System — ISMS).
All'interno del perimetro di certificazione di TP Group, i requisiti prioritari
individuati dal cliente riguardano tre macro-aree: **Business continuity**,
**Disaster recovery** e **Sicurezza degli accessi ai dati**.

La presente gap analysis confronta lo stato AS-IS delle due realtà conflue in
TP Group — Thema Consulting (infrastruttura on-premise) e Pro Studio
(infrastruttura cloud-native) — con i requisiti ISO 27001 dichiarati dal cliente,
al fine di identificare le lacune da colmare nelle successive fasi di
progettazione delle soluzioni (Varianti A/B/C).

Per ogni requisito vengono analizzati: lo stato attuale di Thema Consulting,
lo stato attuale di Pro Studio, il gap identificato e una priorità
(Alta / Media / Bassa) assegnata in base all'impatto sulla conformità e
sulla continuità operativa.

---

## Tabella Gap Analysis

| # | Requisito ISO 27001 | Stato Thema Consulting | Stato Pro Studio | Gap Identificato | Priorità |
|---|---|---|---|---|---|
| 1 | **Business continuity — Ridondanza sistemi strategici**: i sistemi critici devono essere protetti da guasti hardware con componenti ridondanti | Singola SAN NetApp (24 TB) senza replica; singolo NAS QNAP (32 TB); singolo firewall FortiGate FG-60F; singolo front-end HPC (VM Linux); armadi rack saturi senza possibilità di espansione. | Nessuna infrastruttura on-premise; dipendenza esclusiva da un unico cloud provider (GCP). | Assenza totale di ridondanza per storage primario (SAN), storage backup (NAS), firewall perimetrale e front-end HPC. L'infrastruttura on-premise di Thema è a punto singolo di guasto (SPOF) su tutti i componenti critici. Pro Studio non ha ridondanza cross-provider. | **Alta** |
| 2 | **Business continuity — Ridondanza connettività**: la connettività WAN deve essere garantita anche in caso di guasto del link primario | Singola connessione Internet (via FortiGate); nessun link di backup o failover documentato. | Connettività inclusa nel contratto di locazione condominiale; non documentata presenza di link di backup. | Entrambe le sedi dipendono da un unico circuito Internet; in caso di guasto del provider o dell'infrastruttura di accesso, l'intera connettività viene meno, bloccando l'operatività e l'accesso ai servizi cloud/remoti. | **Alta** |
| 3 | **Disaster recovery — Delocalizzazione salvataggi dati**: i backup devono essere conservati in sito geograficamente distinto dalla sede primaria | Backup su NAS QNAP collocato nello stesso datacenter della sede di Torino (nessuna copia off-site). | Backup su Cloud Storage GCP (single-region, non documentata replica multi-regione). | Thema non dispone di alcuna copia off-site: un evento distruttivo nella sede (incendio, allagamento, furto) comprometterebbe sia i dati primari che le copie di backup. Pro Studio utilizza storage GCP ma non è documentata una configurazione multi-regione o una seconda destinazione. | **Alta** |
| 4 | **Disaster recovery — Fruibilità servizi clienti**: i servizi erogati ai clienti devono rimanere accessibili anche in scenari di disastro | Applicazione Pondus erogata on-premise su HW dedicato (CPU Xeon Silver 4110, 64 GB RAM); servizio accessibile ai clienti via Internet. Nessun sito di DR, nessuna replica dell'applicazione. | Servizi SaaS (Odoo, BitBucket, Google Workspace) intrinsecamente resilienti per natura cloud, ma nessun piano di DR formale documentato. | Pondus è completamente esposta: un guasto hardware, un problema software o un evento nella sede di Torino comporta l'interruzione del servizio per i clienti automotive e aerospace. Non esistono infrastruttura di failover, replica dati caldi o procedure di ripristino documentate. | **Alta** |
| 5 | **Sicurezza accessi — Cifratura sistemi di memorizzazione**: tutti i sistemi di storage (primario, backup, endpoint) devono essere cifrati a riposo | SAN NetApp, NAS QNAP, server HPC e VM: non è documentata l'adozione di crittografia a riposo (at-rest encryption). Laptop aziendali: non documentata policy di full-disk encryption. | Google Drive: cifratura lato server (AES-256) di default. VM MediaWiki su GCP: dischi persistenti crittografati di default. | Thema non adotta crittografia a riposo su storage SAN, NAS, server fisici e VM. I dati sensibili (simulazioni, dati clienti, documentazione tecnica) sono potenzialmente leggibili in chiaro in caso di accesso fisico non autorizzato o smarrimento/furto dei supporti. | **Alta** |
| 6 | **Sicurezza accessi — Protocolli sicuri**: le applicazioni di rete devono utilizzare protocolli crittografati (HTTPS, SSH, SFTP, ecc.) | Servizi web self-hosted (NextCloud, MediaWiki, Zimbra webmail, Pondus, GiTea, SugarCRM, Kimai, Profis): l'utilizzo di TLS/HTTPS non è esplicitamente documentato. | Servizi SaaS cloud-native: accesso via HTTPS di default (GDPR compliance). | Thema: non è verificata l'adozione sistematica di TLS per tutti i servizi web. Potrebbero persistere servizi esposti su protocolli in chiaro (HTTP, FTP, Telnet) o configurazioni TLS datate (TLS 1.0/1.1, certificati scaduti). | **Media** |
| 7 | **Sicurezza accessi — VPN LAN-to-LAN**: le comunicazioni tra sedi devono avvenire su tunnel crittografati | FortiGate FG-60F: supporta VPN IPsec, ma non è documentata alcuna VPN LAN-to-LAN attiva verso Pro Studio. | Nessuna infrastruttura VPN: i dipendenti accedono ai servizi esclusivamente via Internet pubblico. | Nessuna connettività VPN LAN-to-LAN tra le due sedi. Il traffico tra i servizi on-premise di Thema e quelli cloud di Pro Studio transita su Internet senza crittografia di livello rete. Necessario tunnel IPsec per l'integrazione delle reti post-fusione. | **Alta** |
| 8 | **Sicurezza accessi — VPN Client-to-LAN**: i dipendenti in mobilità o smart working devono connettersi in modo sicuro alla rete aziendale | FortiGate FG-60F: probabilmente abilitato a VPN client (SSL-VPN o IPsec), ma non documentata una soluzione di client VPN distribuita a tutti i dipendenti. | Nessuna VPN configurata; accesso ai servizi via Internet pubblico con solo 2FA (Google Authenticator). | Manca una soluzione di client VPN standardizzata e obbligatoria per l'accesso da remoto alle risorse on-premise di Thema. Post-fusione, 50 dipendenti necessiteranno di accesso remoto sicuro alla rete aziendale unificata. | **Alta** |
| 9 | **Sicurezza accessi — VPN Hybrid Cloud**: la connettività tra datacenter on-premise e cloud pubblici deve essere protetta da tunnel crittografati | Nessuna connessione VPN verso cloud pubblici (GCP, AWS, Azure) documentata. | MediaWiki self-hosted su GCP: accesso via Internet senza VPN o Cloud Interconnect dedicato. | Assenza di connettività VPN hybrid cloud tra l'infrastruttura on-premise di Thema e i servizi su GCP di Pro Studio. Per la strategia hybrid cloud post-fusione è necessario un tunnel IPsec o Cloud VPN verso GCP. | **Media** |
| 10 | **Sicurezza accessi — Autenticazione Multi-Fattore (MFA)**: l'accesso ai sistemi critici deve essere protetto da autenticazione a più fattori | Samba4 Active Directory: autenticazione a singolo fattore (username + password). Nessuna integrazione con provider MFA esterno. | Google Authenticator: 2FA implementato e attivo per gli account Google Workspace. | Thema non dispone di MFA per l'accesso ai sistemi on-premise (AD Samba4, servizi self-hosted, accesso amministrativo). I 30 dipendenti Thema + i nuovi ingressi Pro Studio richiederanno una soluzione MFA unificata integrata con l'AD. | **Alta** |
| 11 | **Business continuity — Gruppo di continuità (UPS)**: l'alimentazione dei sistemi critici deve essere garantita per un tempo sufficiente allo spegnimento ordinato o all'attivazione del generatore | UPS presente: autonomia ~10 minuti. Nessun generatore elettrico di backup documentato. | N/A (nessuna infrastruttura on-premise). | L'autonomia UPS di 10 minuti è insufficiente per garantire continuità operativa in caso di blackout prolungato o per completare uno shutdown ordinato di cluster HPC e sistemi di storage. La sede storica impedisce l'installazione di un gruppo elettrogeno. | **Media** |
| 12 | **Business continuity — Condizionamento**: la temperatura del datacenter deve essere controllata per prevenire guasti da surriscaldamento | Sistema di raffreddamento al limite del carico termico attuale; difficilmente potenziabile per vincoli strutturali dell'edificio storico. | N/A (nessuna infrastruttura on-premise). | Il condizionamento esistente non ha margine per ulteriori carichi termici (es. espansione HPC +8 nodi). Un guasto del sistema di raffreddamento può causare il fermo del datacenter per surriscaldamento in pochi minuti. | **Media** |
| 13 | **Sicurezza accessi — Hardening server e VM**: i sistemi devono essere configurati secondo benchmark di sicurezza (minimizzazione, patch, logging) | Server e VM Linux autogestiti su VMWare; non documentata l'adozione di benchmark di sicurezza (CIS benchmark, hardening guide) né un processo formalizzato di patch management. | VM MediaWiki su GCP: gestita dal cliente; sicurezza dell'hypervisor e dell'infrastruttura GCP a carico del provider. | Manca un processo formalizzato di hardening e vulnerability scanning per i sistemi on-premise di Thema. L'assenza di un security baseline incrementa la superficie d'attacco sfruttabile. | **Media** |
| 14 | **Sicurezza accessi — Gestione identità e accessi (IAM)**: definizione di ruoli, privilegi minimi e revisione periodica degli accessi | Samba4 AD: gestione centralizzata utenti ma non documentata una policy di segregazione dei ruoli o di revisione periodica degli accessi. | Google Workspace: gestione identità cloud, ruoli e permessi granellari; Google Authenticator per 2FA. | Thema: manca una policy formale di Identity and Access Management (principio del minimo privilegio, revisione accessi, account audit). Post-fusione sarà necessario unificare le identità tra Samba4 AD e Google Workspace. | **Bassa** |

---

## Riepilogo Gap

| Priorità | Conteggio | # Riferimento |
|---|---|---|
| **Alta** | 8 | 1, 2, 3, 4, 5, 7, 8, 10 |
| **Media** | 5 | 6, 9, 11, 12, 13 |
| **Bassa** | 1 | 14 |
| **Totale** | **14** | |

### Distribuzione per area requisito

| Area ISO 27001 | Gap identificati | Di cui priorità Alta |
|---|---|---|
| Business continuity (ridondanza sistemi + connettività + UPS + condizionamento) | 4 | 2 |
| Disaster recovery (delocalizzazione + fruibilità servizi) | 2 | 2 |
| Sicurezza accessi (cifratura, protocolli, VPN, MFA, IAM, hardening) | 8 | 4 |
| **Totale** | **14** | **8** |

---

*Documento redatto a scopo di assessment — TP Group srl — Versione 1.0*
