# Mappatura agenti per le directory del workspace "Materie"

Questo file descrive quale agente usare (suggerito) per ogni area/modulo della cartella `Materie` e come invocarlo per attività comuni.

## Gerarchia di routing

```
SISYPHUS
  ├── CONSULTANTI DIRETTI: oracle · metis · momus · librarian · explore
  ├── coding-orchestrator → coding-coach-its · dotnet-api-tutor · dotnet-style-matcher
  │                         database-sql-coach · exam-prep-its
  ├── infra-orchestrator  → cloud-lab-tutor · linux-sysadmin-lab · network-security-trainer · iot-edge-lab
  ├── tp-orchestrator     → 9 agenti TP Group
  └── content-orchestrator → english-tech-mentor · project-work-mentor · data-analytics-coach
```

## Routing dinamico basato sul prompt

Analizza la richiesta e invoca l'orchestratore di dominio appropriato con `@nome-orchestratore`.
L'orchestratore si occuperà di delegare al subagente specializzato corretto.

Mappa contenuto → orchestratore/agente:

| Cosa chiede l'utente | Instrada a | Che fa |
|---|---|---|
| Programmazione generale, C/C++, Python, JS/TS, algoritmi, Git, AI, fondamenti ICT | `@coding-orchestrator` | Scompone e delega al tutor specializzato |
| C#, .NET, ASP.NET, API REST in .NET, EF, WPF, MAUI, LINQ | `@coding-orchestrator` | Instrada a dotnet-api-tutor o dotnet-style-matcher |
| SQL, NoSQL, modellazione dati, query, indici, MongoDB, Redis | `@coding-orchestrator` | Instrada a database-sql-coach |
| Piani di studio, quiz, simulazioni esame, ripasso | `@coding-orchestrator` | Instrada a exam-prep-its |
| AWS, Azure, GCP, Docker, Kubernetes, deployment cloud | `@infra-orchestrator` | Instrada a cloud-lab-tutor |
| Linux server, shell scripting, hardening, troubleshooting sistemistico | `@infra-orchestrator` | Instrada a linux-sysadmin-lab |
| Reti, firewall, crittografia, OWASP, troubleshooting di rete | `@infra-orchestrator` | Instrada a network-security-trainer |
| IoT, sensori, MQTT, telemetria, edge computing | `@infra-orchestrator` | Instrada a iot-edge-lab |
| Architettura TP Group, fusione Thema+Pro Studio | `@tp-orchestrator` | Scompone nei 9 agenti TP Group |
| Rete/VPN TP Group, Fortigate | `@tp-orchestrator` | Instrada a tp-network-engineer |
| Sicurezza ISO 27001, DR, crittografia (progetto TP) | `@tp-orchestrator` | Instrada a tp-security-compliance |
| Cluster HPC, Infiniband, nodi calcolo | `@tp-orchestrator` | Instrada a tp-hpc-engineer |
| App Pondus, C#/MS SQL/IIS | `@tp-orchestrator` | Instrada a tp-pondus-dev |
| Strategia cloud ibrida, GCP, Workspace (progetto TP) | `@tp-orchestrator` | Instrada a tp-cloud-strategist |
| Backup e DR (progetto TP) | `@tp-orchestrator` | Instrada a tp-backup-dr |
| Offerta tecnico/economica (progetto TP) | `@tp-orchestrator` | Instrada a tp-offerta-docs |
| Project management TP Group, Gantt, budget | `@tp-orchestrator` | Instrada a tp-project-manager |
| Inglese tecnico, traduzioni, CV/LinkedIn EN, terminologia IT | `@content-orchestrator` | Instrada a english-tech-mentor |
| Project work, documentazione, stage, CV, processi, SharePoint | `@content-orchestrator` | Instrada a project-work-mentor |
| Analisi dati, visualizzazioni, dashboard, pandas, Power BI | `@content-orchestrator` | Instrada a data-analytics-coach |
| Esplorazione veloce del codice, "trova", "dov'è", struttura progetto | `@explore` | Ricerca diretta (modello leggero) |
| Consulenza architetturale, debugging complesso, tradeoff | `@oracle` | Consulenza read-only |
| Analisi ambiguità, pre-pianificazione | `@metis` | Analisi pre-implementazione |
| Review piani, qualità, completezza | `@momus` | Plan critic |

## Regole di routing

1. **Default: passa dall'orchestratore.** Non chiamare mai direttamente un agente foglia se esiste un orchestratore per quel dominio.
2. **Eccezioni: chiamata diretta consentita solo per:**
   - `@explore` — ricerca rapida, è un modello leggero, bypassare l'orchestratore è più veloce
   - `@oracle` / `@metis` / `@momus` / `@librarian` — sono consultivi, non hanno orchestratore
   - Urgenza o richiesta esplicita dell'utente (es. "chiama direttamente tp-pondus-dev")
3. **Contesto misto** (es. "query SQL in C#"): instrada all'orchestratore del dominio principale.
4. **Richiesta ambigua o generica**: usa `@coding-orchestrator` (copre la maggior parte dei casi base).
5. **Non aggiungere commenti "ho invocato X"** nella risposta.
6. **Quando invochi un subagent (orchestratore o diretto), passa sempre contesto completo**: directory, file rilevanti, obiettivo, vincoli.

## Mappatura directory -> contesto (informativa)

Le directory servono solo per capire il contesto del progetto. Il routing effettivo si basa sul prompt.

- `00_Amministrazione_Corso` -> project-work-mentor
- `01_Inglese_Tecnico` -> english-tech-mentor
- `02_Orientamento_e_Soft_Skills` -> project-work-mentor
- `03_Parita_e_Non_Discriminazione` -> project-work-mentor
- `04_Sicurezza_sul_Lavoro` -> project-work-mentor
- `05_Fondamenti_ICT` -> coding-coach-its
- `06_Reti_e_Sicurezza_Informatica` -> network-security-trainer
- `07_Version_Control_Git` -> coding-coach-its / explore
- `08_Basi_di_Dati_SQL_NoSQL` -> database-sql-coach
- `09_Programmazione_C_CPP` -> coding-coach-its
- `10_Programmazione_Python` -> coding-coach-its
- `11_Programmazione_DotNet_CSharp` -> dotnet-api-tutor / dotnet-style-matcher
- `12_RESTful_API` -> dotnet-api-tutor / coding-coach-its
- `13_Cloud_AWS` -> cloud-lab-tutor
- `14_Cloud_Azure` -> cloud-lab-tutor
- `15_Cloud_GCP` -> cloud-lab-tutor
- `16_Linux_Server_e_Amministrazione` -> linux-sysadmin-lab
- `17_Container_Docker_Kubernetes` -> cloud-lab-tutor
- `18_Microsoft_365_SharePoint` -> project-work-mentor
- `19_Virtualizzazione` -> project-work-mentor
- `20_Data_Analytics_Visualization` -> data-analytics-coach
- `21_Internet_of_Things` -> iot-edge-lab
- `22_AI_e_Prompt_Engineering` -> coding-coach-its
- `23_Project_Work_e_Laboratori` -> project-work-mentor
- `24_Stage_Professionale` -> project-work-mentor
- `tools/` -> explore