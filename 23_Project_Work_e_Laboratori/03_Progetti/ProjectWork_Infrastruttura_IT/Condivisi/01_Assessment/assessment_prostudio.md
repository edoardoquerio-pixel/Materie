# Assessment AS-IS — Pro Studio srl

## Panoramica

Pro Studio srl nasce nel 2023 come startup composta da giovani ingegneri progettisti che operano nel settore aerospace. L'azienda conta 20 dipendenti con sede a Torino. Dal punto di vista dell'infrastruttura IT, Pro Studio ha adottato fin dalla fondazione un modello completamente cloud-native, senza possesso di alcuna infrastruttura IT on-premise. Il calcolo strutturale, attività core dell'ingegneria aerospaziale, viene sottomesso direttamente sui sistemi dei clienti finali, eliminando la necessità di un cluster di calcolo interno.

---

## Sede

La sede di Pro Studio è un ufficio di rappresentanza in affitto presso un condominio uffici. Il contratto di locazione include tutte le facilities necessarie al funzionamento:

- **Energia elettrica**: fornita tramite contratto condominiale, inclusa nella locazione.
- **Riscaldamento e condizionamento**: gestiti centralmente dall'edificio, inclusi nella locazione.
- **Connettività**: accesso Internet incluso, gestito tramite infrastruttura condominiale.

L'azienda non sostiene costi diretti per questi servizi, in quanto compresi nel canone di locazione. Non sono presenti sale server, rack, UPS o sistemi di condizionamento dedicati.

---

## Personale

L'organico è composto da **20 dipendenti**, tutti con sede a Torino. Ogni dipendente dispone di un laptop aziendale assegnato. Non sono richieste soluzioni VDI (Virtual Desktop Infrastructure). La mobilità dei dipendenti è gestita tramite l'accesso ai servizi cloud da qualsiasi postazione.

---

## Infrastruttura IT

Pro Studio non possiede infrastruttura IT interna. L'intero stack tecnologico è basato su servizi cloud e SaaS (Software as a Service), senza server fisici o virtuali on-premise.

| Componente | Stato |
|---|---|
| Server on-premise | Nessuno |
| Virtualizzazione | Nessuna |
| Firewall hardware | N/A (affidato alla connettività condominiale) |
| Storage locale | N/A (tutti i dati su cloud) |
| UPS | N/A |
| Condizionamento dedicato | N/A |

Non sono presenti sistemi di backup locale, NAS, SAN o apparati di rete dedicati.

---

## Servizi e Sistemi

### Posta e Calendario — Google Workspace

La piattaforma di posta elettronica e calendario è Google Workspace. Tutti i 20 dipendenti dispongono di account con dominio aziendale, con accesso via web e tramite client mobili.

### Office e Produttività — Google Workspace

La suite di produttività (documenti, fogli di calcolo, presentazioni) è interamente basata su Google Workspace (Google Docs, Sheets, Slides). Non sono installate suite office tradizionali on-premise.

### Videoconferenza e IM — Google Meet

Le comunicazioni interne ed esterne via video e messaggistica istantanea sono gestite tramite Google Meet, integrato nell'ecosistema Google Workspace.

### Autenticazione — Google Authenticator

Il sistema di autenticazione a due fattori (2FA) è implementato tramite Google Authenticator. L'identità degli utenti è gestita esclusivamente tramite Google Workspace. Non esiste un directory server Active Directory o LDAP on-premise.

### File Server — Google Drive

La condivisione e l'archiviazione dei file aziendali avviene tramite Google Drive. Non esistono file server on-premise, NAS o soluzioni di storage locale. I dati sono accessibili da qualsiasi dispositivo tramite connessione Internet.

### Sviluppo e Versioning — BitBucket (SaaS)

La gestione del codice sorgente e il versionamento sono affidati a BitBucket, piattaforma SaaS di Atlassian. Non sono presenti server Git interni o soluzioni self-hosted. I repository ospitano il codice relativo ai progetti di ingegneria e alle eventuali personalizzazioni software.

### Contabilità — Odoo (SaaS)

Il sistema contabile è Odoo, utilizzato in modalità SaaS (cloud). La piattaforma gestisce la contabilità generale, la fatturazione e la gestione finanziaria dell'azienda. Non sono presenti server contabili on-premise.

### CRM — Odoo (SaaS)

La gestione delle relazioni con i clienti (Customer Relationship Management) è gestita tramite il modulo CRM di Odoo in modalità SaaS. Il sistema traccia le interazioni con i clienti, le opportunità di vendita e il pipeline commerciale.

### Time Sheet — Odoo (SaaS)

La rilevazione delle ore lavorative del personale è gestita tramite il modulo Time Sheet di Odoo in modalità SaaS. Ogni dipendente registra le proprie ore di lavoro direttamente sulla piattaforma.

### Documentazione — MediaWiki (self-hosted su GCP)

La documentazione tecnica e aziendale è gestita tramite MediaWiki, installato su una macchina virtuale self-hosted su Google Cloud Platform (GCP). Si tratta dell'unico servizio che non fa uso di una piattaforma SaaS, pur rimanendo in ambiente cloud. La VM ospita il software MediaWiki e il relativo database.

### Backup — GCP

Le politiche di backup sono implementate su Google Cloud Platform. I dati critici — inclusi i file presenti su Google Drive, i repository BitBucket e il database MediaWiki — vengono salvati su storage GCP. Non esiste backup su supporti locali o in sede secondaria.

---

## Stima Costi Operativi Attuali

La seguente tabella riporta una stima dei costi operativi mensili e annuali sostenuti da Pro Studio per i servizi IT. Le stime sono basate sui listini pubblici dei fornitori al 2026.

| Servizio | Tipologia | Costo mensile stimato | Costo annuale stimato |
|---|---|---|---|
| Google Workspace Business (20 utenti × ~€12) | SaaS | ~€240 | ~€2.880 |
| BitBucket (20 utenti, Standard: ~$3/user/mese) | SaaS | ~$60 (~€55) | ~$720 (~€660) |
| Odoo Enterprise (20 utenti: ~€24,90/user/mese) | SaaS | ~€498 | ~€5.976 |
| MediaWiki su GCP (VM e2-small + storage) | Cloud IaaS | ~€25 | ~€300 |
| Backup su GCP (storage ~500 GB) | Cloud Storage | ~€15 | ~€180 |
| **Totale stimato** | | **~€833** | **~€9.996** |

**Note sulla stima dei costi:**

- Google Workspace: il costo Business Starter (~€6/user/mese) o Business Standard (~€12/user/mese) dipende dal piano sottoscritto. La stima considera il piano Business Standard con archiviazione illimitata e maggiori funzionalità.
- BitBucket: per team fino a 5 utenti il piano è gratuito. Oltre i 5 utenti è richiesto il piano Standard a $3/user/mese.
- Odoo: la versione Enterprise include i moduli Contabilità, CRM e Time Sheet. Il costo indicato è per utente/mese per la suite completa.
- MediaWiki su GCP: una VM e2-small (2 vCPU, 2 GB RAM) con storage persistente da 50 GB è sufficiente per l'hosting del wiki. Il costo può variare in base al traffico e allo spazio disco utilizzato.
- Backup su GCP: stimato su circa 500 GB di dati in Cloud Storage (classe Standard), con costi di rete e operazioni trascurabili per volumi ridotti.

I costi di connettività (Internet) e le facilities (elettricità, riscaldamento) sono inclusi nel canone di locazione della sede e non sono pertanto quantificabili separatamente come spesa IT diretta.

---

*Documento redatto a scopo di assessment — TP Group srl — Versione 1.0*
