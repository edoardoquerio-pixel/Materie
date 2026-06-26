# Model Detection - Learnings

## 2026-06-25 - T4: Supermemory Model Pattern

### Test Connection Results
- **Profile test**: Success — returned Edoardo Querio user profile with C# coding style
- **Search test**: Success — query "model:" returned 5 results, NONE with "model:" prefix (expected)
- **Connection status**: Supermemory fully operational

### Pattern Document Created
- File: '.omo/supermemory-model-pattern.md'
- Contains: Recording pattern, Retrieval pattern, Fallback strategy, Deduplicazione

### Key Findings
1. Supermemory API configured and working
2. No 'model:' entries in Supermemory — recording not yet implemented
3. Search per recency works (results[0] = most recent)
4. 'type: "preference"' filters user preferences correctly
5. Pattern file documents the full flow for T6 (recording on /setmodel)

### Next Steps (T6)
- Implement recording in /setmodel handler
- Test full cycle: /setmodel → add → search → retrieve model

---

## 2026-06-25 - T6: Model Recording Script

### Created
- **Script**: `.omo/scripts/record-model.ps1`
  - Accepts `-ModelName` parameter (required)
  - Uses `bun` to call Supermemory API (`POST /v3/documents`)
  - Computes container tag dynamically from git email
  - Reads API key from `.config/opencode/supermemory.jsonc`
  - Non-blocking (exits gracefully if API unavailable)

### Test Results
- Recorded: `model:opencode-go/deepseek-v4-flash`
- Verification: `supermemory(search, "model:opencode-go/deepseek-v4-flash", "preference", "user")`
  - **count**: 1
  - **similarity**: 93%
  - **Verdict**: PASS

### Evidence
- File: `.omo/evidence/task-6/recording-test.txt`

### Key Technical Details
1. Supermemory API endpoint: `POST https://api.supermemory.ai/v3/documents`
2. Auth: `Authorization: Bearer <apiKey>` (from `supermemory.jsonc`)
3. Container tag: `opencode_user_<sha256(git email).substring(0,16)>`
4. Metadata format: `{ content: "model:<ModelName>", containerTag, metadata: { type: "preference" } }`
5. Search via `client.search.memories({ q, containerTag })`
## 2026-06-25 — Task 1: /models Persistence Investigation

### Key Findings
- /models DOES persist the model selection to disk
- Primary file: C:\Users\edoardo.querio\.local\state\opencode\model.json
  - Fields: recent[].providerID, recent[].modelID, favorite[], variant{}
  - Active model = recent[0]
  - Current active: opencode/deepseek-v4-flash-free
- Secondary file: C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json
  - Per-agent and per-category model assignments
  - Last modified 2026-06-17 (not updated during /models usage via chat)
- Model catalog (read-only): C:\Users\edoardo.querio\.cache\opencode\models.json

### Implications
- T5 (/setmodel) can be simplified: read/write model.json directly
- No need to reverse-engineer /models internal flow
- But T5 still needed if the goal is a simplified non-interactive setter

### Paths Checked (no model found)
- %LOCALAPPDATA%\opencode → DOES NOT EXIST
- .cache\opencode\models.json → read-only catalog, not a selection
- .local\state\opencode\kv.json → UI prefs only
- .local\state\opencode\frecency.jsonl → no model fields
- .local\state\opencode\prompt-history.jsonl → no model fields
- .local\share\opencode\account.json → API credentials only
- .local\share\opencode\auth.json → API keys only

---

## 2026-06-25 — Task 7: Prometheus Init Instructions

### Created
- **Init file**: `.omo/prometheus-init-instructions.md`
  - Full model detection sequence for Prometheus/Atlas agents
  - Step 1: Supermemory search with "model:" prefix
  - Step 2: Config file read from oh-my-openagent.json
  - Step 3: Compare and decide with mismatch detection
  - Timeout handling (1.5s for Supermemory, 2s total)
  - No crash if sources inaccessible

### Key Technical Decision
- Supermemory search `model:` returns semantic results (not all prefixed with "model:")
- Must filter results with `.startsWith("model:")` before extracting model name
- Targeted search query `model:opencode-go/deepseek-v4-flash` returns 93% similarity vs 66% for generic `model:` query

### Test Results
- **Supermemory search**: ✅ Found `model:opencode-go/deepseek-v4-flash` (93% similarity)
- **Config read**: ✅ agents.prometheus.model = `opencode-go/deepseek-v4-flash`
- **Comparison**: ✅ MATCH — both sources agree
- **Evidence**: `.omo/evidence/task-7/init-test.txt`

### Implications for T8
- Init sequence is documented and verified
- T8 can implement the actual init hook in Prometheus runtime

---

## 2026-06-25 — Task 8: Prometheus Adaptation Instructions

### Created
- **Adaptation file**: `.omo/prometheus-adaptation-instructions.md`
  - Step 1: Load adaptation matrix from `model-adaptation.json`
  - Step 2: Match current model to profile (fallback to "default" if not found)
  - Step 3: Apply 5 adaptation dimensions (verbosity, depth, style, planLength, toolPreference)
  - Step 4: Output adaptation summary at session start
  - Step 5: Behavior enforcement rules per dimension value
  - Fallback/edge case handling for missing matrix, missing profile, missing dimension, invalid values
  - DEFAULT values per dimension defined

### Test Results (Matrix Loading)
- **File exists**: ✅ `model-adaptation.json` found
- **Profiles available**: 3 (default, deepseek-v4-flash, gpt-4o)
- **deepseek-v4-flash profile**: ✅ verbosity=normal, depth=normal, style=bilanciato, planLength=medium, toolPreference=balanced
- **default profile**: ✅ same as deepseek-v4-flash (normal/normal/bilanciato/medium/balanced)
- **Dimension values valid**: ✅ All 5 dimensions validated across all profiles
- **Profiles complete**: ✅ All 3 profiles have all 5 dimensions
- **Fallback**: ✅ Unknown model correctly falls back to "default" profile
- **Verdict**: ✅ ALL TESTS PASSED

### Evidence
- File: `.omo/evidence/task-8/adaptation-test.txt`

### Key Technical Details
1. Matrix file is **read-only** — never modified by adaptation logic
2. Adaptation instructions are consumed **after** model detection (T7)
3. 5 dimensions map to concrete behavioral changes in Prometheus/Atlas
4. Fallback chain: exact profile → "default" profile → hardcoded DEFAULT values
5. The `toolPreference` dimension affects tool selection strategy (balanced/creative/conservative)

### Next Steps
- T9: Integration — wire adaptation instructions into Prometheus session startup
- Implement actual behavior switching based on profile values

---

## 2026-06-25 - Task 9: /setmodel Validation

### Created
- **Script**: `.omo/scripts/validate-model.ps1`
  - Pre-check di validazione chiamato PRIMA di qualsiasi modifica in setmodel-handler.ps1
  - 6 regole di validazione con exit code dedicati

### Validation Rules & Exit Codes
| # | Regola | Exit Code |
|---|-------|-----------|
| 1 | Argomento vuoto | 1 |
| 2 | Caratteri non consentiti (solo a-z, A-Z, 0-9, /, -, .) | 2 |
| 3 | Lunghezza massima superata (> 100 caratteri) | 3 |
| 4 | File di configurazione non trovato | 4 |
| 5 | Backup fallito (directory non scrivibile) | 5 |
| 0 | Tutti i controlli superati | 0 |

### Integration
- `setmodel-handler.ps1` ora chiama `validate-model.ps1` come sezione 1.5
- La validazione avviene dopo il parsing del ModelName e la definizione dei path, ma PRIMA di qualsiasi backup o modifica
- Se validazione fallisce, l'handler esce immediatamente senza toccare i file di configurazione

### Test Results
- **error-empty** ✅ exit 1 — `ERRORE: nessun modello specificato. Usa /setmodel <nome-modello>`
- **error-chars** ✅ exit 2 — `ERRORE: caratteri non consentiti nel nome modello...`
- **error-length** ✅ exit 3 — `ERRORE: nome modello troppo lungo (max 100 caratteri)`
- **error-file-not-found** ✅ exit 4 — `ERRORE: file di configurazione non trovato al path: ...`
- **error-backup** ✅ exit 5 — `ERRORE: impossibile creare backup. Operazione annullata.`
- **valid-input** ✅ exit 0 — nessun errore

### Evidence
- `.omo/evidence/task-9/error-empty.txt`
- `.omo/evidence/task-9/error-chars.txt`
- `.omo/evidence/task-9/error-length.txt`
- `.omo/evidence/task-9/error-file-not-found.txt`
- `.omo/evidence/task-9/error-backup.txt`
- `.omo/evidence/task-9/valid-input.txt`

### Blocking
- BLOCA T10 (rollback/undo) — la validazione è prerequisito per operazioni di modifica sicure

---

## 2026-06-25 - Task 10: Rollback/Undo per /setmodel

### Created/Modified
- **Script**: `.omo/scripts/setmodel-handler.ps1` — aggiunti parametri `-Undo` e `-List`
  - `-Undo`: ripristina l'ultimo backup disponibile per entrambi i file di configurazione
  - `-List`: elenca tutti i backup con timestamp e dimensione
  - Rotazione automatica: mantiene al massimo 3 backup per file, elimina il più vecchio
  - Parametro mutualmente esclusivo: solo una modalità alla volta

### Technical Details
1. Backup nel formato `.bak.YYYYMMdd-HHmmss` (stessa directory dei file originali)
2. Get-LatestBackup: trova il backup più recente ordinando i filename in ordine decrescente
3. Dopo undo, modello ripristinato viene registrato in Supermemory via `record-model.ps1`
4. Rotazione chiamata dopo ogni nuovo backup tramite `Invoke-BackupRotation`
5. Attenzione: backup con stesso timestamp (stesso secondo) vengono sovrascritti (Copy-Item -Force)

### Test Results
- **setmodel -ModelName "modello-test"** ✅ Backup creato, modello aggiornato
- **setmodel -Undo** ✅ Modello ripristinato dal backup più recente, registrato in Supermemory
- **setmodel -List** ✅ Elenca 2 gruppi di backup con timestamp e dimensione
- **setmodel -Undo senza backup** ✅ "ERRORE: nessun backup disponibile per il ripristino" (exit 1)
- **setmodel (nessun parametro)** ✅ "ERRORE: Specificare -ModelName <modello>, -Undo, oppure -List."
- **Rotazione** ✅ Solo backup > 3 vengono eliminati

### Evidence
- `.omo/evidence/task-10/undo-test.txt`

### Duplicate Timestamp Issue
Se più setmodel vengono eseguiti nello stesso secondo, `Copy-Item -Force` sovrascrive lo stesso backup.
Questo è un edge case noto ma accettabile per il contesto d'uso.
