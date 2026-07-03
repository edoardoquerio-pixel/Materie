# Lezione 14

Fonte: `14) Microsoft Azure - Storage, Data Integration - Protezione dati e file service.pptx`

### Slide 1

DOCENTE

Federico Laurianti

UNITÀ FORMATIVA

Microsoft Azure (100 ore)

ARGOMENTO

Storage, Data & Integration: protezione dati, file service e backup (4 ore)

---

### Slide 2

Storage, protezione dati e file service (4 ore)

•  Lifecycle, tiering e retention per governare costo e ciclo di vita del dato
•  Versioning, soft delete e immutabilita per protezione operativa e compliance
•  Azure Files con identita centralizzate e permessi a due livelli
•  Backup e recovery per continuita operativa verificabile

---

### Slide 3

Blob tiering: Hot, Cool, Archive

Tier

Uso tipico

Hot

dati letti spesso

Cool

dati letti saltuariamente

Archive

dati rari, conservazione lunga

•  Il tier influenza costo di storage e costo/tempo di accesso
•  Non esiste tier migliore in assoluto: dipende dal comportamento del dato
•  La scelta corretta parte da frequenza reale di lettura

---

### Slide 4

Lifecycle management e retention

•  Le regole lifecycle automatizzano spostamento e cancellazione blob
•  Condizioni comuni: età del dato, prefisso, tipo di contenuto
•  Vantaggio: meno operazioni manuali e costo più stabile nel tempo
•  Retention va allineata a esigenze operative e vincoli normativi
•  Lifecycle è una policy continua, non una attività una tantum

---

### Slide 5

Versioning, soft delete e immutabilita

•  Versioning: mantiene storico delle modifiche ai blob
•  Soft delete: recupera cancellazioni accidentali in finestra definita
•  Immutabilita (WORM): blocca modifica/cancellazione per un periodo
•  Versioning e soft delete coprono errori operativi
•  WORM copre integrita forte, audit e requisiti di compliance

---

### Slide 6

Protezione e costo: combinare le leve

Esigenza

Leva principale

ridurre costo nel tempo

lifecycle + tiering

recuperare errori utente

versioning + soft delete

garantire integrita legale

immutabilita WORM

•  Non si attiva tutto per default: si sceglie in base al rischio
•  La soluzione giusta e una combinazione coerente di controlli

---

### Slide 7

Azure Files: quando usarlo

•  Azure Files fornisce file share SMB gestite nello Storage Account
•  Utile per workload che si aspettano condivisioni file classiche
•  Adatto a directory condivise, profili utente e applicazioni lift-and-shift
•  Se serve modello object/API, spesso e preferibile Blob Storage
•  La scelta dipende dal modo in cui l'app legge e scrive i dati

---

### Slide 8

Identita centralizzate per Azure Files

•  Accesso integrabile con identita directory (AD DS o Entra in scenari compatibili)
•  Si riducono account locali e credenziali statiche
•  Gruppi e ruoli semplificano concessione e revoca accessi
•  Il controllo accessi diventa uniforme e tracciabile nel tempo
•  Obiettivo: governance chiara tra utenti, gruppi e risorse

---

### Slide 9

Permessi: livello share e livello NTFS

•  Permessi share: definiscono chi puo accedere alla condivisione
•  Permessi NTFS: definiscono cosa puo fare dentro file e cartelle
•  Accesso effettivo = intersezione dei due livelli
•  Errore tipico: un livello corretto e l'altro errato
•  Verifica sempre entrambe le dimensioni prima del go-live

---

### Slide 10

Backup, recovery e continuita operativa

•  Recovery Services Vault centralizza policy e operazioni di restore
•  Backup senza test di restore non garantisce recupero reale
•  RPO: perdita dati accettabile, RTO: tempo massimo di ripristino
•  Policy e retention devono essere coerenti con criticita servizio
•  Continuita operativa = tecnologia + procedure verificate

---

### Slide 11

Scenario integrato: scelta guidata

Domanda

Scelta tecnica

dati poco letti ma da tenere

lifecycle verso Cool/Archive

rischio sovrascrittura/cancellazione

versioning + soft delete

requisito legale di integrita

immutabilita WORM

app che richiede file share SMB

Azure Files

requisito di recupero servizio

backup con Vault + test restore

•  Una architettura robusta nasce da esigenze esplicite e priorita chiare

---

### Slide 12

Traccia tecnica di lavoro

•  Definire un caso d'uso con requisiti storage, protezione e recupero
•  Progettare policy lifecycle e strategia di protezione del dato
•  Progettare file share con identita centralizzate e permessi a due livelli
•  Definire backup, retention e piano di test restore
•  Documentare evidenze operative e motivazioni architetturali

---

### Slide 13

Criteri di qualita della soluzione

•  Scelta corretta tra blob policy e file share in base al contesto d'uso
•  Livelli coerenti di protezione: operativo, integrita, recovery
•  Motivazioni tecniche chiare e leggibili anche per interlocutori non tecnici
•  Decisioni architetturali validate con verifiche pratiche