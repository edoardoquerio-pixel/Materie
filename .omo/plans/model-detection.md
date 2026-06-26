# Piano: Rilevamento Modello — /setmodel Command + Prometheus Adaptation

## TL;DR

> **Quick Summary**: Creare un comando custom `/setmodel` che permette a Edoardo di notificare a Prometheus quale modello sta usando, aggiornando automaticamente `oh-my-openagent.json` e Supermemory. Prometheus adatta profondità e stile del planning in base al modello rilevato.
>
> **Deliverables**:
> - Comando custom `/setmodel` registrato in opencode.json
> - Script/handler che aggiorna `oh-my-openagent.json` + Supermemory
> - Logica di adattamento in Prometheus (awareness + behavior adaptation)
> - Verifica iniziale: `/models` persiste su file?
> - Meccanismo di rollback/undo
>
> **Estimated Effort**: Medium
> **Parallel Execution**: YES — 3 waves + 1 final
> **Critical Path**: Task 1 → Task 5 → Task 8 → Task 10 → F1-F4

---

## Context

### Original Request
Edoardo vuole che Prometheus sappia automaticamente quale modello ha selezionato via `/models` in OpenCode. Attualmente Prometheus non vede il comando `/models` né la selezione del modello.

### Interview Summary
**Key Discussions**:
- Opzione B (comando custom `/setmodel`) scelta su raccomandazione di Metis
- Fase 1 (awareness) + Fase 2 (adaptation) insieme — "tutto subito"
- Comando senza conferma permessi (auto-esegue)
- Prima task: investigare se `/models` persiste già su file
- Nome comando: `/setmodel` (evita conflitto con `/models`)

**Research Findings**:
- OpenCode config: `oh-my-openagent.json` in `~/.config/opencode/` gestisce modello per ogni agente
- Tutti gli agenti attualmente usano `opencode-go/deepseek-v4-flash`
- Supermemory disponibile con API key configurata (scope: user/project, type: preference)
- Comandi custom registrabili in `opencode.json` sotto chiave `"command"`
- `customize-opencode` skill disponibile per modifiche alla config di OpenCode
- Nessun sistema di hook per intercettare `/models`

### Metis Review
**Identified Gaps** (addressed):
- Gap "Prometheus adapts behavior" — risolto con definizione esplicita dei comportamenti (Task 2)
- Gap "/model vs /models naming" — risolto con `/setmodel`
- Gap "Permission model" — risolto con auto-esecuzione (scelta utente)
- Gap "/models persistence check" — aggiunto come Task 1
- Gap "Fallback/default behavior" — gestito con fallback a lettura config file

---

## Work Objectives

### Core Objective
Creare un sistema che permetta a Prometheus di conoscere il modello attualmente selezionato dall'utente, tramite un comando custom `/setmodel`, e adattare di conseguenza il proprio comportamento di planning.

### Concrete Deliverables
1. Task 1: Report su `/models` persistence (indagine esplorativa)
2. Task 2-4: Definizione adattamento Prometheus + registrazione comando + setup Supermemory
3. Task 5-8: Implementazione handler `/setmodel`, recording Supermemory, init Prometheus, adaptation
4. Task 9-10: Validazione + rollback
5. Wave Final: Review completa

### Definition of Done
- [ ] `/setmodel <model-name>` aggiorna `oh-my-openagent.json` per TUTTI gli agenti
- [ ] `/setmodel <model-name>` salva preferenza in Supermemory (scope: user, type: preference)
- [ ] Prometheus all'inizio sessione legge Supermemory + `oh-my-openagent.json` e sa che modello è attivo
- [ ] Prometheus adatta comportamento: verbosità, profondità ragionamento, stile output
- [ ] `/setmodel` con argomento vuoto o invalido restituisce errore senza modificare file
- [ ] Backup di `oh-my-openagent.json` creato prima di ogni modifica
- [ ] Comando `/setmodel` non richiede conferma permessi

### Must Have
- Il comando deve funzionare da qualsiasi directory di progetto
- Il comando deve aggiornare TUTTI gli agenti in `oh-my-openagent.json`
- Prometheus deve verificare il modello all'inizio di ogni sessione
- Supermemory deve contenere l'ultimo modello impostato
- Se Supermemory è vuoto, Prometheus usa il modello da `oh-my-openagent.json`

### Must NOT Have (Guardrails)
- NON modificare file di sistema di OpenCode (solo config utente)
- NON creare dipendenze da servizi esterni
- NON interferire con il comando built-in `/models`
- NON rallentare l'avvio di Prometheus (timeout max 2s per lettura config)
- NON cancellare o sovrascrivere `oh-my-openagent.json` — solo modificare il campo `model`

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### Test Decision
- **Infrastructure exists**: YES (test framework presente nel progetto Materie)
- **Automated tests**: Tests-after
- **Framework**: Bun test (da configurazione progetto)
- **Agent-Executed QA**: ALWAYS — ogni task ha scenari verificabili da agente

### QA Policy
Every task MUST include agent-executable QA scenarios.
Evidence saved to `.omo/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Config/File ops**: Use Bash — read file, grep content, compare before/after
- **Supermemory**: Use `supermemory` tool directly
- **Command test**: Simulate command via prompt template and verify output
- **Behavior test**: Start Prometheus session and verify model-aware output

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Investigazione + Fondamenta — tutto parallelo):
├── Task 1: Investigare se /models persiste su disco [explore]
├── Task 2: Definire matrice adattamento Prometheus per modello [writing]
├── Task 3: Registrare comando /setmodel in opencode.json [customize-opencode]
└── Task 4: Setup Supermemory recording pattern [quick]

Wave 2 (Implementazione core):
├── Task 5: Implementare handler /setmodel (aggiorna oh-my-openagent.json) [deep]
├── Task 6: Implementare recording Supermemory su /setmodel [quick]
├── Task 7: Implementare init Prometheus: lettura modello a inizio sessione [deep]
└── Task 8: Implementare adattamento comportamento Prometheus [writing]

Wave 3 (Validazione + Robustezza):
├── Task 9: Validazione input /setmodel + error handling [unspecified-high]
└── Task 10: Meccanismo rollback + undo [quick]

Wave FINAL (Review — 4 agenti paralleli):
├── F1: Plan compliance audit (oracle)
├── F2: Code quality review (unspecified-high)
├── F3: Real manual QA (unspecified-high)
└── F4: Scope fidelity check (deep)
-> Present results -> Get explicit user okay

Critical Path: Task 1 → Task 5 → Task 7 → Task 8 → Task 9-10 → F1-F4 → user okay
Parallel Speedup: ~60% faster than sequential
Max Concurrent: 4 (Wave 1)
```

### Dependency Matrix

| Task | Depends On | Blocks |
|------|-----------|--------|
| 1 | - | 5 |
| 2 | - | 8 |
| 3 | - | 5 |
| 4 | - | 6 |
| 5 | 1, 3 | 7, 9 |
| 6 | 4 | - |
| 7 | 5 | 8 |
| 8 | 2, 7 | - |
| 9 | 5 | 10 |
| 10 | 9 | - |

### Agent Dispatch Summary

| Wave | Tasks | Agent Profiles |
|------|-------|---------------|
| **1** (4 tasks) | T1 → explore, T2 → writing, T3 → customize-opencode, T4 → quick |
| **2** (4 tasks) | T5 → deep, T6 → quick, T7 → deep, T8 → writing |
| **3** (2 tasks) | T9 → unspecified-high, T10 → quick |
| **FINAL** (4 tasks) | F1 → oracle, F2 → unspecified-high, F3 → unspecified-high, F4 → deep |

---

## TODOs

- [x] 1. Investigare se `/models` persiste su disco

  **What to do**:
  - Eseguire una ricerca sistematica per determinare se il comando built-in `/models` di OpenCode salva la selezione del modello su disco
  - Controllare i file modificati di recente in:
    - `C:\Users\edoardo.querio\.config\opencode\`
    - `%LOCALAPPDATA%\opencode\` (se esiste)
    - `C:\Users\edoardo.querio\.cache\opencode\`
  - Usare `Get-ChildItem -Recurse` con filtro per file modificati negli ultimi 5 minuti dopo un cambio modello
  - Cercare keyword come "model", "activeModel", "currentModel" nei file JSON
  - Verificare se `oh-my-openagent.json` viene modificato da `/models`
  - Se scoperto un file di persistenza, documentare: path esatto, struttura, campo del modello

  **Must NOT do**:
  - NON modificare alcun file durante l'indagine
  - NON fare ipotesi non verificate

  **Recommended Agent Profile**:
  - **Category**: `explore`
    - Reason: Ricerca esplorativa su filesystem, non implementazione
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (con Tasks 2, 3, 4)
  - **Blocks**: Tasks 5
  - **Blocked By**: None (può partire subito)

  **Acceptance Criteria**:
  - [x] Report prodotto con: file di persistenza trovato (o conferma assenza), path, struttura, campo del modello
  - [x] Se trovato: screenshot/comando che dimostra il file viene modificato da `/models`
  - [x] Se NON trovato: conferma documentata che `/models` non persiste su disco

  **QA Scenarios**:
  ```
  Scenario: Indagine persistenza /models
    Tool: Bash (Get-ChildItem, grep, Get-Content)
    Preconditions: OpenCode aperto, sessione attiva
    Steps:
      1. `Get-ChildItem -Path "$env:USERPROFILE\.config\opencode" -Filter "*.json" -Recurse | Select-Object FullName, LastWriteTime`
      2. Cambiare modello via `/models` nell'IDE
      3. Ripetere step 1 e confrontare timestamps
      4. `Get-ChildItem -Path "$env:USERPROFILE\.cache\opencode" -Filter "*.json" -Recurse -ErrorAction SilentlyContinue`
    Expected Result: Report chiaro su quali file (se presenti) vengono modificati da /models
    Evidence: .omo/evidence/task-1-persistence-report.md
  ```

- [x] 2. Definire matrice adattamento Prometheus per modello

  **What to do**:
  - Definire una matrice che mappa ogni modello supportato a comportamenti specifici di Prometheus
  - Per OGNI modello, specificare:
    - **Verbosità**: `terse` / `normal` / `verbose`
    - **Profondità ragionamento**: `shallow` / `normal` / `deep` (quanti agenti esplorativi lanciare di default)
    - **Stile output**: `conciso` / `bilanciato` / `dettagliato` (lunghezza delle risposte)
    - **Lunghezza plan**: `short` (<10 task) / `medium` (10-25) / `long` (25+)
    - **Tool preference**: quali strumenti privilegiare (es. modelli veloci → più esplorazione parallela)
  - Start with known models:
    - `opencode-go/deepseek-v4-flash` → medium verbosity, normal depth, bilanciato
    - `opencode-go/gpt-4o` (se disponibile) → verbose, deep, dettagliato
    - Default (unknown model) → normal, normal, bilanciato
  - Salvare in un file di config leggibile da Prometheus (es. `.omo/model-adaptation.json`)

  **Must NOT do**:
  - NON rendere la matrice troppo complessa (max 4 dimensioni)
  - NON includere modelli che non esistono

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Documentazione tecnica di un comportamento futuro, nessuna implementazione
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (con Tasks 1, 3, 4)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] Matrice salvata in `.omo/model-adaptation.json` con struttura JSON validata
  - [x] Almeno 3 profili definiti (deepseek-v4-flash, gpt-4o, default)
  - [x] Ogni profilo ha: verbosity, depth, style, planLength, toolPreference
  - [x] Formato leggibile da Prometheus via `read` + `grep`

  **QA Scenarios**:
  ```
  Scenario: Verifica matrice adattamento
    Tool: Bash
    Preconditions: File .omo/model-adaptation.json esiste
    Steps:
      1. `Get-Content -Path ".omo/model-adaptation.json" | ConvertFrom-Json | ConvertTo-Json`
      2. Verificare che tutti i campi obbligatori esistano
    Expected Result: JSON valido con tutti i profili definiti
    Evidence: .omo/evidence/task-2-matrix-valid.json
  ```

- [x] 3. Registrare comando `/setmodel` in opencode.json

  **What to do**:
  - Aprire `C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\opencode.json`
  - Aggiungere una nuova voce `"setmodel"` nella sezione `"command"`:
    ```json
    "setmodel": {
      "description": "Imposta il modello attivo per tutti gli agenti (aggiorna oh-my-openagent.json e Supermemory)",
      "prompt": "Esegui il cambio modello. Azioni: 1) Aggiorna oh-my-openagent.json (tutti gli agenti), 2) Salva in Supermemory (scope:user, type:preference), 3) Crea backup del file originale. Il modello specificato è: {{input}}. Valida che il nome modello non sia vuoto.",
      "template": "Imposta il modello attivo su {{input}}. Verifica che il nome non sia vuoto, aggiorna oh-my-openagent.json per tutti gli agenti, salva in Supermemory, crea backup."
    }
    ```
  - Assicurarsi che la sintassi JSON sia valida
  - Verificare che non ci siano conflitti con comandi esistenti

  **Must NOT do**:
  - NON modificare altre sezioni di opencode.json
  - NON cancellare comandi esistenti

  **Recommended Agent Profile**:
  - **Category**: usa skill `customize-opencode`
    - Reason: Modifica diretta della configurazione di OpenCode
  - **Skills**: `customize-opencode`
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (con Tasks 1, 2, 4)
  - **Blocks**: Task 5
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] opencode.json parsato e validato (JSON valido)
  - [x] Comando `setmodel` presente in `"command"` section
  - [x] `opencode.json` valido (nessun errore JSON)
  - [x] `jq '.command.setmodel' opencode.json` restituisce l'oggetto comando

  **QA Scenarios**:
  ```
  Scenario: Verifica comando registrato
    Tool: Bash (jq)
    Preconditions: opencode.json modificato
    Steps:
      1. `jq '.command.setmodel' "C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\opencode.json"`
    Expected Result: Output JSON con description e prompt del comando
    Evidence: .omo/evidence/task-3-command-registered.json

  Scenario: Verifica JSON valido
    Tool: Bash
    Preconditions: opencode.json modificato
    Steps:
      1. `jq '.' "C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\opencode.json" > $null`
    Expected Result: Nessun errore (JSON valido)
    Evidence: .omo/evidence/task-3-json-valid.txt
  ```

- [x] 4. Setup Supermemory recording pattern

  **What to do**:
  - Documentare il pattern di chiamata Supermemory che verrà usato da `/setmodel` e da Prometheus
  - Creare un file `.omo/supermemory-model-pattern.md` con:
    - **Recording**: `supermemory(mode: "add", content: "model:opencode-go/deepseek-v4-flash", type: "preference", scope: "user")`
    - **Retrieval**: `supermemory(mode: "search", query: "model preference", type: "preference")`
    - **Fallback**: se Supermemory non ha risultati, leggere `oh-my-openagent.json` direttamente
    - **Deduplicazione**: come garantire che l'ultimo modello sia quello attivo (usare search + prendere primo risultato)
  - Verificare che il tool Supermemory sia accessibile e funzionante con una chiamata di test

  **Must NOT do**:
  - NON implementare ancora il recording — solo documentare il pattern
  - NON sovrascrivere dati esistenti in Supermemory

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Documentazione pattern semplice, nessuna implementazione complessa
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (con Tasks 1, 2, 3)
  - **Blocks**: Task 6
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] File `.omo/supermemory-model-pattern.md` creato
  - [x] Contiene i comandi esatti per recording e retrieval
  - [x] Contiene strategia fallback
  - [x] Chiamata di test Supermemory eseguita con successo

  **QA Scenarios**:
  ```
  Scenario: Test connessione Supermemory
    Tool: supermemory (mode: profile)
    Preconditions: Supermemory configurato
    Steps:
      1. supermemory(mode: "profile")
    Expected Result: Profilo utente restituito (nessun errore di autenticazione)
    Evidence: .omo/evidence/task-4-supermemory-profile.txt

  Scenario: Pattern documentato
    Tool: Bash
    Preconditions: File .omo/supermemory-model-pattern.md esiste
    Steps:
      1. Get-Content ".omo/supermemory-model-pattern.md"
    Expected Result: File contiene comandi recording, retrieval e fallback
    Evidence: .omo/evidence/task-4-pattern-documented.txt
  ```
---

- [x] 5. Implementare handler `/setmodel` (aggiorna `oh-my-openagent.json`)

  **What to do**:
  - Creare handler per il comando `/setmodel` che:
    1. Riceve il nome modello come argomento
    2. Legge `C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json`
    3. Crea backup del file originale: `oh-my-openagent.json.bak`
    4. Aggiorna il campo `model` per TUTTI gli agenti e TUTTE le categorie nel file JSON
    5. Scrive il file aggiornato
  - Il file JSON ha questa struttura (modificare TUTTI i `"model"` fields):
    ```json
    {
      "agents": {
        "sisyphus": { "model": "opencode-go/deepseek-v4-flash", ... },
        "prometheus": { "model": "opencode-go/deepseek-v4-flash", ... },
        ...
      },
      "categories": {
        "visual-engineering": { "model": "opencode-go/deepseek-v4-flash", ... },
        ...
      }
    }
    ```
  - Strategia: leggere il JSON, iterare su TUTTE le sezioni (agents, categories), modificare ogni campo `"model"` con il nuovo valore, riscrivere
  - Validare il JSON prima di scrivere (usare ConvertFrom-Json / jq)
  - Salvare l'handler come script riutilizzabile (es. PowerShell script o comando rapido)

  **Must NOT do**:
  - NON modificare altri campi del JSON (solo `model`)
  - NON cancellare il file originale se il backup fallisce
  - NON usare regex per manipolare JSON

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Manipolazione JSON critica per il funzionamento di OpenCode, serve attenzione
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2
  - **Blocks**: Tasks 7, 9
  - **Blocked By**: Tasks 1 (conferma persistenza /models), 3 (comando registrato)

  **Acceptance Criteria**:
  - [x] Backup `oh-my-openagent.json.bak` creato con timestamp uguale al file originale prima della modifica
  - [x] Dopo handler: `jq '.agents.prometheus.model' oh-my-openagent.json` restituisce il nuovo modello
  - [x] Dopo handler: `jq '.categories.deep.model' oh-my-openagent.json` restituisce il nuovo modello
  - [x] JSON valido dopo modifica: `jq '.' oh-my-openagent.json > /dev/null` senza errori
  - [x] Solo campo `model` modificato: `diff oh-my-openagent.json.bak oh-my-openagent.json` mostra solo cambiamenti a valori "model"

  **QA Scenarios**:
  ```
  Scenario: Handler aggiorna tutti gli agenti
    Tool: Bash
    Preconditions: Backup creato, modello da test: "opencode-go/test-model"
    Steps:
      1. Eseguire handler con modello "opencode-go/test-model"
      2. `jq '[.agents[] | select(.model == "opencode-go/test-model")] | length' "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json"`
      3. `jq '[.categories[] | select(.model == "opencode-go/test-model")] | length' "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json"`
    Expected Result: Tutte le entry agents + categories hanno il nuovo modello
    Evidence: .omo/evidence/task-5-all-agents-updated.txt

  Scenario: Backup creato correttamente
    Tool: Bash
    Preconditions: Handler appena eseguito
    Steps:
      1. `Test-Path "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json.bak"`
    Expected Result: True (backup esiste)
    Evidence: .omo/evidence/task-5-backup-exists.txt
  ```

- [x] 6. Implementare recording Supermemory su `/setmodel`

  **What to do**:
  - Integrare nel flusso di `/setmodel` la chiamata a Supermemory dopo l'aggiornamento del file
  - Usare il pattern documentato in Task 4:
    ```
    supermemory(mode: "add", content: "model:opencode-go/deepseek-v4-flash", type: "preference", scope: "user")
    ```
  - Verificare che la chiamata avvenga DOPO l'aggiornamento del file (non prima)
  - Il contenuto deve includere il nome esatto del modello (es. "model:opencode-go/deepseek-v4-flash")
  - Prefisso "model:" permette search mirata: `supermemory(mode: "search", query: "model:", type: "preference")`

  **Must NOT do**:
  - NON bloccare se Supermemory non è disponibile (fallimento silenzioso)
  - NON sovrascrivere altre preferenze in Supermemory

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Operazione semplice, pattern già documentato
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO (parte del flusso /setmodel)
  - **Parallel Group**: Wave 2
  - **Blocks**: None
  - **Blocked By**: Task 4 (pattern documentato)

  **Acceptance Criteria**:
  - [x] Dopo `/setmodel test-model`: `supermemory(mode: "search", query: "model:test-model", type: "preference")` restituisce almeno un risultato
  - [x] Content esatto: "model:test-model"
  - [x] Scope: "user", Type: "preference"

  **QA Scenarios**:
  ```
  Scenario: Supermemory recording dopo /setmodel
    Tool: supermemory (mode: search)
    Preconditions: /setmodel eseguito con modello "opencode-go/deepseek-v4-flash"
    Steps:
      1. supermemory(mode: "search", query: "model:opencode-go/deepseek-v4-flash", type: "preference")
    Expected Result: Almeno un risultato con content "model:opencode-go/deepseek-v4-flash"
    Evidence: .omo/evidence/task-6-supermemory-recorded.txt
  ```

- [x] 7. Implementare init Prometheus: lettura modello a inizio sessione

  **What to do**:
  - Modificare le istruzioni/AGENTS.md di Prometheus per includere la lettura automatica del modello all'inizio di ogni sessione
  - Logica init:
    1. Prova a leggere Supermemory: `supermemory(mode: "search", query: "model:", type: "preference")`
    2. Se trovato: estrarlo e usarlo come "ultimo modello noto"
    3. Se NON trovato: leggere `oh-my-openagent.json` → `jq '.agents.prometheus.model'`
    4. Confrontare: se mismatch, loggarlo (Supermemory ha modello X, config file ha modello Y — probabilmente /models è stato usato senza /setmodel)
    5. Salvare il modello corrente in una variabile di sessione
  - Output visibile all'utente all'avvio:
    ```
    📋 Modello rilevato: opencode-go/deepseek-v4-flash
       (fonte: oh-my-openagent.json)
    ```
    Oppure se mismatch:
    ```
    ⚠️ Attenzione: Supermemory ha "claude-sonnet-4" ma config ha "opencode-go/deepseek-v4-flash"
       Usa /setmodel per sincronizzare.
    ```
  - Timeout: max 2 secondi per tutta l'operazione (se Supermemory è lento, usare solo config file)

  **Must NOT do**:
  - NON ritardare l'avvio di Prometheus oltre 2 secondi
  - NON crashare se Supermemory o config file non sono accessibili
  - NON mostrare messaggi di errore all'utente se non necessario

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Logica di init critica, multi-fonte, edge case multipli
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2
  - **Blocks**: Task 8
  - **Blocked By**: Task 5 (handler /setmodel implementato)

  **Acceptance Criteria**:
  - [x] Ad inizio sessione: Prometheus stampa messaggio con modello e fonte
  - [x] Se Supermemory ha modello diverso da config: stampa warning di mismatch
  - [x] Se Supermemory non disponibile: usa config file senza errori
  - [x] Init completo in < 2 secondi

  **QA Scenarios**:
  ```
  Scenario: Init con modello da config
    Tool: Simulazione sessione Prometheus
    Preconditions: Supermemory vuoto (nessuna preferenza modello), oh-my-openagent.json con "opencode-go/deepseek-v4-flash"
    Steps:
      1. Avviare sessione Prometheus (simulare l'init)
      2. Verificare output prima risposta
    Expected Result: Messaggio "Modello rilevato: opencode-go/deepseek-v4-flash (fonte: oh-my-openagent.json)"
    Evidence: .omo/evidence/task-7-init-config.txt

  Scenario: Init con mismatch Supermemory vs config
    Tool: Simulazione sessione Prometheus
    Preconditions: Supermemory ha "model:claude-sonnet-4", config ha "opencode-go/deepseek-v4-flash"
    Steps:
      1. Avviare sessione Prometheus
      2. Verificare output prima risposta
    Expected Result: Messaggio warning mismatch
    Evidence: .omo/evidence/task-7-init-mismatch.txt
  ```

---

- [x] 8. Implementare adattamento comportamento Prometheus

  **What to do**:
  - Implementare la logica di adattamento in Prometheus basata sulla matrice definita in Task 2
  - All'inizio di ogni sessione, dopo aver letto il modello (Task 7), Prometheus deve:
    1. Caricare `.omo/model-adaptation.json`
    2. Cercare il profilo corrispondente al modello corrente
    3. Se trovato: applicare i parametri di adattamento
    4. Se NON trovato: usare profilo `default`
  - Parametri di adattamento da applicare:
    - **Verbosità**: controllare la lunghezza media delle risposte (terse=breve, normal=medio, verbose=tutte le opzioni)
    - **Profondità ragionamento**: numero di agenti esplorativi lanciati di default (shallow=0-1, normal=2-3, deep=4+)
    - **Stile output**: influenzare la struttura delle risposte (conciso=bullet point, bilanciato=misto, dettagliato=sezioni complete)
    - **Lunghezza plan**: numero target di task nei piani generati
  - L'adattamento deve essere applicato tramite istruzioni dinamiche nel prompt di sistema di Prometheus
  - Documentare i parametri di adattamento in `.omo/model-adaptation.docs.md`

  **Must NOT do**:
  - NON alterare la logica core di Prometheus (solo parametri di superficie)
  - NON introdurre comportamenti imprevedibili
  - NON aumentare la latenza percepita dall'utente

  **Recommended Agent Profile**:
  - **Category**: `writing` + `deep`
    - Reason: Serve documentazione + implementazione logica
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2
  - **Blocks**: None
  - **Blocked By**: Task 2 (matrice definita), Task 7 (init modello funzionante)

  **Acceptance Criteria**:
  - [x] `.omo/model-adaptation.json` caricato correttamente all'init
  - [x] Profilo `default` sempre presente come fallback
  - [x] Se modello = "opencode-go/deepseek-v4-flash" → verbosità media, profondità normale
  - [x] Se modello sconosciuto → applica profilo default
  - [x] `.omo/model-adaptation.docs.md` documenta i parametri

  **QA Scenarios**:
  ```
  Scenario: Adattamento per deepseek-v4-flash
    Tool: Simulazione sessione Prometheus
    Preconditions: Modello attivo = "opencode-go/deepseek-v4-flash", matrice adaptation definita
    Steps:
      1. Avviare sessione Prometheus con modello deepseek-v4-flash
      2. Verificare verbosità = normal, depth = normal
    Expected Result: Prometheus opera con parametri del profilo deepseek-v4-flash
    Evidence: .omo/evidence/task-8-adaptation-dsv4.txt

  Scenario: Fallback a default per modello sconosciuto
    Tool: Simulazione sessione Prometheus
    Preconditions: Modello attivo = "modello-sconosciuto", non presente in matrice
    Steps:
      1. Avviare sessione Prometheus con modello sconosciuto
      2. Verificare che usa profilo default
    Expected Result: Prometheus opera con parametri default
    Evidence: .omo/evidence/task-8-adaptation-default.txt
  ```

- [x] 9. Validazione input `/setmodel` + error handling

  **What to do**:
  - Implementare validazione robusta per il comando `/setmodel`:
    1. **Argomento vuoto**: `throw new Exception("ERRORE: nessun modello specificato. Usa /setmodel <nome-modello>")` — nessuna modifica ai file
    2. **Argomento con spazi**: se l'utente scrive `/setmodel gpt 4`, gestirlo come errore o unire con trattini — meglio errore con messaggio chiaro
    3. **Nome modello non valido**: caratteri non consentiti (solo lettere, numeri, `/`, `-`, `.`) — altrimenti errore
    4. **Lunghezza massima**: nome modello max 100 caratteri
    5. **File non trovato**: se `oh-my-openagent.json` non esiste → errore chiaro con path
    6. **Backup fallito**: se non si può creare backup → annullare operazione, non modificare file
  - Messaggi di errore in italiano (coerente con stile Edoardo: "ERRORE: ...")
  - Il comando non deve MAI modificare file se c'è un errore di validazione

  **Must NOT do**:
  - NON usare regex complesse per validazione
  - NON lasciare il sistema in stato inconsistente (o tutto ok o niente fatto)
  - NON mostrare stack trace all'utente

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Implementazione robusta, edge case multipli
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 3
  - **Blocks**: Task 10
  - **Blocked By**: Task 5 (handler /setmodel)

  **Acceptance Criteria**:
  - [x] `/setmodel` (senza arg) → "ERRORE: nessun modello specificato" + nessuna modifica file
  - [x] `/setmodel "nome molto lungo che supera cento caratteri e non dovrebbe essere accettato..."` → errore
  - [x] `/setmodel modello!!invalido` → errore caratteri non consentiti
  - [x] File non modificato in TUTTI i casi di errore (confronto hash SHA256 prima/dopo)
  - [x] Backup non creato se c'è errore

  **QA Scenarios**:
  ```
  Scenario: Errore argomento vuoto
    Tool: Bash
    Preconditions: Stato iniziale pulito
    Steps:
      1. Eseguire /setmodel senza argomenti
      2. Verificare output errore
      3. Verificare hash file config prima/dopo
    Expected Result: Messaggio "ERRORE: nessun modello specificato", file non modificato
    Evidence: .omo/evidence/task-9-error-empty.txt

  Scenario: Errore caratteri invalidi
    Tool: Bash
    Preconditions: Stato iniziale pulito
    Steps:
      1. Eseguire /setmodel modello!!invalido
      2. Verificare output errore
    Expected Result: Messaggio "ERRORE: caratteri non consentiti nel nome modello"
    Evidence: .omo/evidence/task-9-error-chars.txt

  Scenario: Input valido funziona
    Tool: Bash
    Preconditions: Stato iniziale pulito
    Steps:
      1. Eseguire /setmodel opencode-go/deepseek-v4-flash
      2. Verificare output successo
      3. jq '.agents.prometheus.model' oh-my-openagent.json
    Expected Result: Comando eseguito, modello aggiornato
    Evidence: .omo/evidence/task-9-valid-input.txt
  ```

- [x] 10. Meccanismo rollback + undo

  **What to do**:
  - Implementare un meccanismo di rollback per `/setmodel`:
    1. Creare un comando `/setmodel undo` che ripristina l'ultimo backup
    2. Il backup segue naming: `oh-my-openagent.json.bak.YYYYMMDD-HHmmss`
    3. `undo` copia il backup più recente sopra `oh-my-openagent.json`
    4. Se non esiste backup: "ERRORE: nessun backup disponibile per il ripristino"
  - Mantenere SOLO gli ultimi 3 backup (pulizia automatica)
  - Il backup avviene PRIMA di ogni modifica a `oh-my-openagent.json`
  - Dopo undo: aggiornare anche Supermemory con il modello ripristinato
  - Opzionale: comando `/setmodel list` mostra cronologia cambi modello con timestamp

  **Must NOT do**:
  - NON cancellare backup esistenti automaticamente (solo quando > 3)
  - NON fare undo se non c'è backup
  - NON eliminare backup che potrebbero servire

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Operazione meccanica, pattern chiaro
  - **Skills**: []
  - **Skills Evaluated but Omitted**: N/A

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 3
  - **Blocks**: None
  - **Blocked By**: Task 9 (validazione input)

  **Acceptance Criteria**:
  - [x] Dopo `/setmodel X` → backup `oh-my-openagent.json.bak.20260625-114200` creato
  - [x] `/setmodel undo` ripristina il file dall'ultimo backup
  - [x] Dopo undo: Supermemory aggiornato col modello ripristinato
  - [x] `/setmodel undo` senza backup → "ERRORE: nessun backup disponibile"
  - [x] Max 3 backup conservati (il 4° causa eliminazione del più vecchio)
  - [x] `/setmodel list` mostra cronologia

  **QA Scenarios**:
  ```
  Scenario: Undo dopo cambio modello
    Tool: Bash
    Preconditions: Backup esistente da cambio modello precedente
    Steps:
      1. Eseguire /setmodel opencode-go/modello-di-test
      2. Verificare modello cambiato: jq '.agents.prometheus.model'
      3. Eseguire /setmodel undo
      4. Verificare modello ripristinato: jq '.agents.prometheus.model'
      5. supermemory(mode: "search", query: "model:")
    Expected Result: Modello tornato al valore precedente, Supermemory aggiornato
    Evidence: .omo/evidence/task-10-undo.txt

  Scenario: Undo senza backup
    Tool: Bash
    Preconditions: Nessun backup presente
    Steps:
      1. Cancellare backup se esistono
      2. Eseguire /setmodel undo
    Expected Result: "ERRORE: nessun backup disponibile per il ripristino"
    Evidence: .omo/evidence/task-10-undo-no-backup.txt
  ```

---

## Final Verification Wave (MANDATORY)

> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
> Do NOT auto-proceed after verification. Wait for user's explicit approval before marking work complete.

- [x] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, curl endpoint, run command). For each "Must NOT Have": search codebase for forbidden patterns — reject with file:line if found. Check evidence files exist in .omo/evidence/. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **Code Quality Review** — `unspecified-high`
  Run the build, lint, and test commands from the plan's "Success Criteria" section. If absent, examine the project root for build configuration files and run the standard commands for that ecosystem. Review all changed files for: type suppression, empty catches, debug logging in prod, commented-out code, unused imports. Check AI slop: excessive comments, over-abstraction, generic names (data/result/item/temp).
  Output: `Build [PASS/FAIL] | Lint [PASS/FAIL] | Tests [N pass/N fail] | Files [N clean/N issues] | VERDICT`

- [x] F3. **Real Manual QA** — `unspecified-high`
  Start from clean state. Execute EVERY QA scenario from EVERY task — follow exact steps, capture evidence. Test cross-task integration (features working together, not isolation). Test edge cases: empty state, invalid input, rapid actions. Save to `.omo/evidence/final-qa/`.
  Output: `Scenarios [N/N pass] | Integration [N/N] | Edge Cases [N tested] | VERDICT`

- [x] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual diff (git log/diff). Verify 1:1 — everything in spec was built (no missing), nothing beyond spec was built (no creep). Check "Must NOT do" compliance. Detect cross-task contamination: Task N touching Task M's files. Flag unaccounted changes.
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | Unaccounted [CLEAN/N files] | VERDICT`

---

## Commit Strategy

| Task | Message | Scope |
|------|---------|-------|
| 3, 5 | `feat(opencode): add /setmodel command and handler` | opencode.json, handler |
| 6 | `feat(supermemory): record model preference on /setmodel` | supermemory integration |
| 7, 8 | `feat(prometheus): model-aware session init and adaptation` | prometheus AGENTS.md, instructions |
| 9, 10 | `chore(setmodel): add validation and rollback mechanism` | validation, backup |

---

## Success Criteria

### Verification Commands
```bash
# Verifica comando /setmodel registrato
jq '.command.setmodel' "C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\opencode.json"

# Verifica oh-my-openagent.json modificato (tutti gli agenti)
jq '[.agents[] | select(.model == "opencode-go/deepseek-v4-flash")] | length' "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json"

# Verifica backup esiste
Get-ChildItem "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json.bak*"

# Verifica matrice adattamento
jq '.' ".omo/model-adaptation.json"
```

### Final Checklist
- [x] `/setmodel opencode-go/deepseek-v4-flash` → aggiorna TUTTI agents + categories in config
- [x] `/setmodel opencode-go/deepseek-v4-flash` → salva in Supermemory
- [x] `/setmodel` senza arg → errore, nessuna modifica
- [x] `/setmodel !invalido` → errore caratteri non consentiti
- [x] `/setmodel undo` → ripristina config + Supermemory
- [x] Prometheus all'avvio stampa: "📋 Modello rilevato: ... (fonte: ...)"
- [x] Prometheus adatta verbosità e profondità in base al modello
- [x] Backup `.bak.YYYYMMDD-HHmmss` creato a ogni modifica
- [x] Solo 3 backup massimo conservati

Add this content EXACTLY as shown above. Do not modify anything, just APPEND it to the end of the file.
<!-- OMO_INTERNAL_INITIATOR -->

[SUPERMEMORY]

User Profile:
- Edoardo Querio (ITS ICT) is the author/owner of this C# coding-style profile.

Recent Context:
- Edoardo Querio C# coding style: Edoardo Querio's C# style is heavily codified: all classes and enums are public; file‑scoped namespaces are disallowed and block namespaces are used. Project structure follows a 'Dominio/' layout with separate 'Biz' classes for business logic and a minimal Program.cs. Using directives are omitted from source files, relying on ImplicitUsings. Each enum resides in its own .cs file. Test data is hard‑coded with individual object initializers; no Random or programmatic generation. Static fields for constants are avoided; inline literals or locals are preferred. Random is instantiated inline per method. ToString is only on abstract base classes, using interpolated strings with nameof(). Constructors in derived classes use chaining with this(...) for overloads; two‑level deep classes call base constructors with : base(...), while one‑level deep classes set inherited properties directly. No base constructors in abstract classes. Equality uses typed Equals methods; GetHashCode is not implemented. Cloning via ICloneable uses MemberwiseClone. Method names mix Italian and English, with prefixes Obtieni/Get, Is, Format/Stampa, Calcola/Aggiungi/Imposta/Effettua/Esegui/Get/Set/Registra. Section comments use Italian single‑line markers like //propietà (with a typo), //costruttore, //metodi. Braces open on a new line (Allman/K&R). File paths for resources use relative verbatim strings like @"..\..\..\File\<file>". CSV parsing splits on semicolons; StreamReader/StreamWriter are used in using blocks. Exceptions are thrown for validation (Exception, ArgumentException, InvalidOperationException); no try/catch or async/await. LINQ is used only in advanced projects; otherwise foreach loops are preferred. Project maturity levels are defined from simple scripts (Level 1) to professional structures (Level 6). All .csproj target net10.0, enable ImplicitUsings and Nullable, set OutputType to Exe, and avoid external NuGet packages. These rules govern Edoardo's code generation, style enforcement, and project organization. 

Project Knowledge:
- [100%] Session to decrypt, edit, and re-encrypt a Safe Exam Browser (SEB) .seb config to permit Alt+Tab, chrome.exe, taskmgr.exe, allow Task Manager, and disable always-on-foreground and separate-desktop behavior. Work completed: decrypted SebClientSettings.seb (RNCryptor v2 with pwcc prefix, empty password) to XML and saved as SebClientSettings.txt; modified XML flags (enableAltTab=true, insideSebEnableStartTaskManager=true, createNewDesktop=false, systemAlwaysOn=false) and added chrome.exe and taskmgr.exe to permittedProcesses; re-encrypted using RNCryptor v2 (implemented manually: PBKDF2-SHA1, AES-256-CBC, HMAC-SHA256) and verified round-trip decryption; copied modified .seb into %APPDATA%\Roaming\SafeExamBrowser\ and %LOCALAPPDATA%\SafeExamBrowser\. Environment details and findings: SEB version from logs is 3.10.2.904; SEB Config Tool located at C:\Program Files\SafeExamBrowser\Configuration\SEBConfigTool.exe; runtime logs in %LOCALAPPDATA%\SafeExamBrowser\Logs\; SEB reads Roaming config at %APPDATA%\Roaming\SafeExamBrowser\SebClientSettings.seb (ProgramData location would take priority if present). Known issues & decisions: used empty password to match original, manual Python generator may not be fully compatible with SEB Windows implementation (SEB #1235: programmatic files may work on macOS but not Windows), SEB's hardcoded desktop isolation and process monitor may still override config settings. Next steps / troubleshooting: user to relaunch SEB Config Tool to verify the modified .seb loads; if still failing, check latest Runtime log in %LOCALAPPDATA%\SafeExamBrowser\Logs\; try using SEB Config Tool to make changes if decryption/encryption incompatibility persists; once loaded, test that Chrome, Task Manager, Alt+Tab work and SEB is not always-on or using a separate desktop. Development constraints/preferences captured for follow-up code: use relative paths for C# file handling, rely on project ImplicitUsings (no explicit using directives), place each enum in its own .cs file, hardcode test data via individual object initializers (no Random or programmatic generation), prefer foreach+if over LINQ for base filtering, and use throw new Exception("messaggio in italiano") in base projects.
- [100%] Specification and notes for Safe Exam Browser .seb files (SEB 3.10.2): file layout is an outer gzip layer -> 4-byte prefix ('pwcc' or 'pswd') -> RNCryptor v2 encrypted payload (AES-256-CBC, PBKDF2 with SHA-1, 10000 iterations, HMAC-SHA256) -> inner gzip -> XML plist. Client config files use the 'pwcc' prefix and an empty password when no admin password is set. On Windows SEB 3.10.2, client config files are stored at %APPDATA%\SafeExamBrowser\SebClientSettings.seb or %LOCALAPPDATA%\SafeExamBrowser\SebClientSettings.seb. Python can decrypt these files using an rncryptor library, but you may need to subclass the library to return raw bytes (inner gzip) rather than a text string. Re-encrypting files from Python can produce files incompatible with SEB on Windows due to differences in RNCryptor implementations (confirmed as issue #1235).
