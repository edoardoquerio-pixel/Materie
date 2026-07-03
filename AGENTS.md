# AGENTS.md — Materie (ITS ICT Cloud Specialist)

## Cosa è questo repository

Ecosystem didattico del corso **ITS ICT Cloud Specialist** (Piemonte). Contiene materiali, esercizi e progetti di 22 materie. Su questo si innesta **Zara Agent** (`aldok10/zara-agent-opc`), un framework AI engineering partner MCP-based che fornisce CI/CD, test, e tooling — i due layer convivono nello stesso repo ma servono scopi diversi.

- **Remote principale:** `github.com/edoardoquerio-pixel/Materie.git` (branch `main`)
- **Submodule:** `17_Container_Docker_Kubernetes/` → `github.com/edoardoquerio-pixel/ITS-ICT_Containers.git` (branch `master`)
- **Git**: `git submodule update --init --recursive` dopo il clone

---

## Struttura

### Materie (22 aree numerate)

Ogni materia segue la convenzione:

```
NN_Nome_Materia/
├── 01_Materiale/    # PDF, PPT, codice di esempio, risorse
├── 02_Esercizi/     # Esercizi e soluzioni
└── 03_Progetti/     # Progetti completi
```

| # | Materia | Tecnologie principali |
|---|---------|----------------------|
| 05 | Fondamenti ICT | — |
| 06 | Reti e Sicurezza Informatica | Python (matplotlib, multiprocessing) |
| 07 | Version Control Git | — |
| 08 | Basi di Dati SQL/NoSQL | SQL (SQL Server, SQLite), .bak, .sql |
| 09 | Programmazione C/CPP | C (CMake), struct, allocazione dinamica |
| 10 | Programmazione Python | Python (type hints, pathlib, CLI) |
| 11 | Programmazione DotNet C# | C# .NET 10 (console, WinForms, ADO.NET) |
| 12 | RESTful API | Node.js/Express (ESM), SQLite, Swagger |
| 13 | Cloud AWS | — |
| 14 | Cloud Azure | Python (Azure Functions v2) |
| 15 | Cloud GCP | — |
| 16 | Linux Server e Amministrazione | SQL, shell |
| 17 | Container Docker Kubernetes | Docker, K8s (submodule esterno) |
| 18 | Microsoft 365 SharePoint | — |
| 19 | Virtualizzazione | Docker, Terraform (HCL) |
| 20 | Data Analytics & Visualization | Python (pandas, matplotlib), Jupyter |
| 21 | Internet of Things | — |
| 22 | AI e Prompt Engineering | — |
| 23 | Project Work e Laboratori | **TP_Group** (project work enterprise) |
| — | tools/ | PowerShell (FAD downloader) |

### Zara Agent overlay

```
tests/                         # Test suite (Zara Agent, NON delle materie)
  *.test.mjs                   #   Unit test (Node --test)
  test_structure.bats          #   Struttura repo (richiede bats)
  test_prompts.bats            #   Prompt validation
.github/
  workflows/ci.yml             #   CI: lint JSON/.mjs/shell + test matrix (3 OS × 2 Node)
  workflows/release.yml        #   Release: su tag v*, crea GitHub Release
  workflows/security.yml       #   Security: CodeQL, TruffleHog, npm audit, dependency-review
  copilot-instructions.md      #   Istruzioni workspace Copilot
  AGENTS.md                    #   Lista 11 agenti workspace
  AI_README.md                 #   Riepilogo Zara Agent (leggibile da AI)
  instructions/                #   Regole per Python, SQL, Cloud labs
agents/                        #   11 agent definitions (.agent.md)
prompts/                       #   11 .prompt.md per generazione esercizi/lab
```

---

## Comandi essenziali

### C# (.NET)
```bash
# Creare nuovo progetto console
dotnet new console -n NomeProgetto
# Build + run
dotnet run --project NomeProgetto/NomeProgetto.csproj
# Tutti i progetti in una cartella
for d in */; do dotnet run --project "$d${d%/}.csproj"; done
```

### Node.js (REST API)
```bash
cd 12_RESTful_API/03_Progetti/libreriaonline
npm install
npm start              # via nodemon
# oppure
node server.js
```

### Python
```bash
python -m pip install -r requirements.txt   # se presente
python nome_script.py
```

### Docker / K8s (submodule)
```bash
cd 17_Container_Docker_Kubernetes
docker-compose up -d                                   # lab 17
kubectl apply -f labs/18-Kubernetes/deployment.yaml    # lab 18+
```

### FAD Downloader (solo Windows PowerShell 5.1+)
```bash
cd tools
copy .env.example .env        # inserire credenziali
.\download-all.bat             # scarica tutti i corsi
```

### Zara Agent — CI (solo GitHub, locale non funziona senza node_modules)
```bash
npm install --ignore-scripts
node --experimental-sqlite --test tests/*.test.mjs
bats tests/test_structure.bats    # richiede bats-core installato
```

---

## Pattern di codice osservati

### C# .NET 10
- **`.csproj`**: SDK-style con `<TargetFramework>net10.0</TargetFramework>`, `<ImplicitUsings>enable</ImplicitUsings>`, `<Nullable>enable</Nullable>`
- **`.slnx`**: Formato XML (`<Solution><Project Path="..."/></Solution>`), NON il vecchio `.sln`
- **Entry point**: Due pattern compresenti — top-level statements (C# 10+, senza `class Program`) e classico `namespace X { class Program { static void Main } }`
- **Console**: `Console.Write`/`Console.ReadLine`, string interpolation (`$"..."`)
- **OOP**: Object initializer, `override ToString()`, enum/classi separati, `switch`

### Node.js Express
- **ESM**: `import`/`export`, `"type": "module"` in package.json
- **Routing**: `express.Router()`, path prefix `/api/v1` o `/api/v2`
- **Body**: `body-parser` con `json()`
- **Storage**: Da array in memoria (v1) a SQLite con `sqlite3` (v2)
- **Swagger**: `swagger-ui-express` + `swagger.json` (OpenAPI 2.0)

### Python
- **Type hints**: `list[int]`, `-> bool`, `-> None` (anche con `from __future__ import annotations`)
- **Path**: `pathlib.Path` per path
- **CLI guard**: `if __name__ == "__main__":`
- **Error handling**: Eccezioni specifiche, validazione input con loop
- **Muliprocessing**: `multiprocessing.Pool` per CPU-bound

### C (09_Programmazione_C_CPP)
- **CMake**: `CMakeLists.txt` con `add_executable`
- **Header guard**: `#ifndef NOME_H / #define NOME_H`
- **Struct**: `typedef struct` per modellazione dati
- **CLI**: Menu-driven con `do { switch } while()`, input via `fgets`/`sscanf`

---

## Testing

> **⚠ I test in `tests/` appartengono a Zara Agent, NON alle materie.**

- **Unit test**: Node.js built-in runner — `node --experimental-sqlite --test tests/*.test.mjs`
- **Structure test**: `bats tests/test_structure.bats` (verifica esistenza dir/file Zara Agent, fallirà se mancano `docs/`, `examples/`, `scripts/` etc.)
- **CI matrix**: 3 OS (ubuntu, windows, macos) × 2 Node (22, 24), non-blocking
- **Per le materie**: Non esiste test automation — il codice sono esercizi didattici

---

## Gotcha e avvertenze

1. **README.md fuorviante**: Quello alla root non descrive il progetto Materie ma il submodule Docker/K8s. Ignorarlo come overview generale.
2. **Due progetti in uno**: `tests/`, `.github/workflows/`, `.github/ISSUE_TEMPLATE/` appartengono a **Zara Agent**, non al corso. Non crearne di nuovi per le materie.
3. **No `package.json` locale**: Esiste su GitHub (usato dalla CI) ma non in questo workspace locale. `npm install` fallirà.
4. **`.slnx` ≠ `.sln`**: Le soluzioni C# usano il nuovo formato XML `.slnx`, non il vecchio `.sln`. Non confonderli.
5. **`net10.0`**: Tutti i progetti C# targettano .NET 10. Verificare che il runtime sia installato (`dotnet --list-sdks`).
6. **FAD downloader richiede credenziali**: Copiare `.env.example` in `.env` e inserire username/password del portale FAD ITS ICT. Non committare `.env`.
7. **Submodule Docker/K8s**: `17_Container_Docker_Kubernetes/` è un git submodule. Dopo il clone fare `git submodule update --init --recursive`.
8. **Structure tests falliranno localmente**: `bats tests/test_structure.bats` richiede `docs/`, `examples/`, `scripts/`, `LICENSE`, `CONTRIBUTING.md` etc. — file Zara Agent non presenti in questo checkout.
9. **Commenti in italiano, codice in inglese**: I commenti didattici sono in italiano, nomi di variabili/funzioni in inglese (tranne C# dove nomi classe sono in italiano se didattici).
10. **Nessun orm/odm**: I progetti .NET e Node.js usano SQL diretto (ADO.NET, `sqlite3`), non Entity Framework o Prisma.

---

## Project Work (23_Project_Work_e_Laboratori)

**TP_Group** è un project work enterprise simulato (Thema Consulting + Pro Studio merger):
- 9 agent specializzati (Assessment, Network, Security, HPC, App, Cloud, Backup, Bid, PM)
- Budget: 520k€ + IVA
- KANBAN.md con task organizzati per delivery order
- Deliverable tracking con dipendenze
- Agenti specifici in `TP_Group/agents/`

---

## Convenzioni GitHub

- **Branch**: `main` (protezione su push diretto)
- **Tags**: `v*` triggerano release workflow
- **PR**: Usare template in `.github/PULL_REQUEST_TEMPLATE.md`
- **Issue**: Template per bug, feature, question in `.github/ISSUE_TEMPLATE/`
- **Dependabot**: Aggiornamenti npm settimanali, GitHub Actions mensili
- **`.github/instructions/`**: Regole Copilot per Python, SQL, Cloud labs (applicate automaticamente da GitHub Copilot/OpenCode)
