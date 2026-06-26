# Task 1: Persistence Report — /models model selection

## Test Metadata
- **Test Date**: 2026-06-25
- **Test Time (start)**: 11:58:22
- **Test Time (end)**: 11:58:44
- **Environment**: Windows, OpenCode (oh-my-openagent)
- **Operator**: Edoardo Querio

---

## Summary Verdict

> **YES — /models DOES persist the model selection to disk.**
> The model selection is stored in **two** files with distinct roles.

---

## Primary Persistence File (Model State)

### Path
`C:\Users\edoardo.querio\.local\state\opencode\model.json`

### File Metadata (at time of investigation)
- **LastWriteTime**: 2026-06-25 11:53:20 (today, highly recent)
- **Size**: 1195 bytes
- **Structure**: Single-line JSON

### JSON Schema
{
  "recent": [
    {"providerID": "opencode", "modelID": "deepseek-v4-flash-free"},
    {"providerID": "opencode-go", "modelID": "deepseek-v4-flash"},
    ...
  ],
  "favorite": [],
  "variant": { ... }
}

### Fields Found
| Field | Path in JSON | Type | Description |
|-------|-------------|------|-------------|
| modelID | .recent[].modelID | string | The model identifier |
| providerID | .recent[].providerID | string | The provider name |
| favorite | .favorite | array | Favorited models (empty) |
| variant | .variant | object | Model variant settings |

### Current Model (active selection)
The **first entry** in the `recent` array is the current/active model:
- Provider: `opencode`
- Model: `deepseek-v4-flash-free`

### Evidence of /models activity
The file LastWriteTime is **2026-06-25 11:53:20** — just ~5 minutes before investigation began.

---

## Secondary Config File (Agent/Category Mapping)

### Path
`C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json`

### File Metadata
- **LastWriteTime**: 2026-06-17 16:21:45
- **Size**: 4273 bytes
- **Structure**: Multi-line formatted JSON

### Fields Found
| Field | Path | Type | Description |
|-------|------|------|-------------|
| model | agents.*.model | string | Model per agent |
| model | categories.*.model | string | Model per category |
| fallback_models | agents.*.fallback_models | array | Fallback models |

### Note
This file NOT updated since 2026-06-17 — /models primarily updates model.json.

---

## Other Checked Locations (Model NOT found)

| Path | Exists? | Model Field? | Notes |
|------|---------|-------------|-------|
| %LOCALAPPDATA%\opencode | NO | N/A | Directory does not exist |
| .cache\opencode\models.json | YES | NO | Read-only model catalog |
| .local\state\opencode\kv.json | YES | NO | UI preferences only |
| .local\state\opencode\frecency.jsonl | YES | NO | No model fields |
| .local\state\opencode\prompt-history.jsonl | YES | NO | No model fields |
| .local\share\opencode\account.json | YES | NO | API credentials only |
| .local\share\opencode\auth.json | YES | NO | API keys only |
| .config\opencode\package.json | YES | NO | Plugin dependency only |
| .opencode\ (messages/parts) | YES | NO | Conversation history only |
| AppData\Local\oh-my-opencode\ | YES | NO | Binary executable only |

---

## How /models Works (Reconstructed Flow)

1. User invokes /models in OpenCode chat
2. OpenCode reads model catalog from .cache\opencode\models.json
3. User selects a model from the list
4. OpenCode writes selection to .local\state\opencode\model.json
   - Selected model prepended to recent array
   - variant object may be updated
5. Model persisted for subsequent conversations

---

## Implications for Task 5 (/setmodel handler)

| Aspect | Finding |
|--------|---------|
| Model persistence exists? | YES — model.json |
| Can T5 read current model? | YES — first entry in .recent array |
| Can T5 write directly? | Technically YES, but format-sensitive |
| Is T5 still needed? | YES — for simplified /setmodel |
| Simplification possible? | YES — T5 can read/write model.json directly |

---

## Change Detection Guidance

To detect if /models was used:
1. Before: Capture LastWriteTime + content of model.json
2. After: Compare timestamps and content (especially recent[0])
3. Change in recent[0] confirms model switch
