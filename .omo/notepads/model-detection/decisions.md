# Model Detection - Decisions

## 2026-06-25 — T5: /setmodel Handler Implementation

### Architecture Decision
- **Script**: setmodel-handler.ps1 in .omo/scripts/
- **Parameter**: -ModelName (stringa, formato providerID/modelID)
- **Dual-file update**: both oh-my-openagent.json (config agenti) and model.json (runtime stato)

### ModelName Parsing
- Split on first / ? providerID (before) + modelID (after)
- If no / present, default providerID = opencode
- Esempio: opencode-go/deepseek-v4-flash ? provider=opencode-go, model=deepseek-v4-flash

### oh-my-openagent.json Update Strategy
- **Recursive field walk**: function Set-ModelFieldsRecursive traverses the entire JSON object tree
- Updates ALL model **string** properties at any depth:
  - gents.*.model
  - gents.*.fallback_models[].model
  - categories.*.model
  - categories.*.fallback_models[].model
- allback_models arrays are PRESERVED (only the model strings inside them update)
- Other fields ($schema, allback_models structure, etc.) remain untouched

### model.json Update Strategy
- New entry: { providerID: "...", modelID: "..." }
- **Prepend** to ecent array (position 0 = active model)
- **Dedup**: remove any existing entry with same providerID + modelID
- **Max 10**: trim after dedup+prepend
- avorite and ariant fields untouched

### Backup Strategy
- **Timestamped**: ile.json.bak.YYYYMMdd-HHmmss
- Backup BEFORE each modification
- If model.json read fails ? rollback oh-my-openagent.json from its backup
- If oh-my-openagent.json read fails ? abort entirely

### Error Handling
- Validate JSON with ConvertFrom-Json before any write
- Atomic backup ? modify flow per file
- $ErrorActionPreference = "Stop" throughout

### Evidence
- ackup-test.txt: lists backup files created
- update-test.txt: shows what was changed and counts

### ConvertTo-Json Depth
- Default depth=2 truncates nested structures
- Used -Depth 10 to preserve allback_models[].model and any deep nesting

### Join-Path Limitation (PowerShell 5.1)
- Join-Path only accepts 2 path segments
- Used string interpolation instead of multi-arg Join-Path
- Avoided .NET Path.Combine due to 4-param limit in .NET Framework

### Dependencies
- Blocks T7 (recording su Supermemory) and T9 (integrazione comando /setmodel in opencode.json)
