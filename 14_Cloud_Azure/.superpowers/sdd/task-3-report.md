# Task 3 Report: Backend — Azure Functions (All 5)

## Status: DONE

## Files Created/Modified
- `backend/requirements.txt` — rewrote with single line `azure-functions`
- `backend/host.json` — rewrote (was already correct, no changes needed)
- `backend/local.settings.json` — rewrote with `QUEUE_STORAGE_CONNECTION` added (was missing)
- `backend/function_app.py` — rewrote with all 5 functions and bug fix

## Bug Fix Verification
The existing `function_app.py` had `connection="COSMOS_DB"` in three places (elabora_richiesta line 171, riepilogo lines 207/214). The rewritten code uses `connection="COSMOS_CONNECTION_STRING"` everywhere — verified with grep: 5 occurrences of `COSMOS_CONNECTION_STRING`, 0 occurrences of `COSMOS_DB`.

## Python Syntax Check
`python -c "import py_compile; py_compile.compile('function_app.py', doraise=True)"` — passed with no output (success).

## Git Commit
```
fdf1d51 feat(backend): add all 5 Azure Functions (crea, lista, pubblica, elabora, riepilogo)
```
3 files changed, 160 insertions, 9 deletions.

## 5 Functions Implemented
1. **crea_richiesta** — HTTP POST → Cosmos DB (sincrono, 201 Created)
2. **lista_richieste** — HTTP GET ← Cosmos DB (input binding, 200 OK)
3. **pubblica_richiesta** — HTTP POST → Queue (asincrono, 202 Accepted)
4. **elabora_richiesta** — Queue Trigger → Cosmos DB (output binding)
5. **riepilogo** — Timer Trigger (*/2 min) → Cosmos DB input + output

## Concerns
- `local.settings.json` uses the well-known local Cosmos DB emulator key — acceptable for local dev only.
- No concerns blocking delivery.
