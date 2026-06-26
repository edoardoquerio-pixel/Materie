<#
.SYNOPSIS
    Handler per il comando /setmodel — aggiorna sia oh-my-openagent.json (config agenti)
    che model.json (stato runtime modello selezionato). Supporta undo e list backup.

.DESCRIPTION
    Modalità:
      -ModelName <string> : Imposta un nuovo modello (comportamento principale)
      -Undo              : Ripristina l'ultimo backup disponibile
      -List              : Elenca tutti i backup disponibili con timestamp e dimensione

    Caratteristiche:
      - Backup con timestamp PRIMA di ogni modifica (formato .bak.YYYYMMdd-HHmmss)
      - Rotazione automatica: mantiene al massimo 3 backup per file
      - Undo ripristina sia oh-my-openagent.json che model.json dall'ultimo backup
      - Dopo undo, registra il modello ripristinato in Supermemory

.PARAMETER ModelName
    Nome completo del modello, es: "opencode-go/deepseek-v4-flash".
    Il formato è "providerID/modelID". Se non contiene "/", providerID default="opencode".

.PARAMETER Undo
    Switch: ripristina l'ultimo backup disponibile.

.PARAMETER List
    Switch: elenca tutti i backup disponibili.

.EXAMPLE
    .\setmodel-handler.ps1 -ModelName "opencode-go/deepseek-v4-flash"
    .\setmodel-handler.ps1 -ModelName "anthropic/claude-sonnet-4-6"
    .\setmodel-handler.ps1 -Undo
    .\setmodel-handler.ps1 -List
#>

param(
    [string]$ModelName,
    [switch]$Undo,
    [switch]$List
)

$ErrorActionPreference = "Stop"

# ──────────────────────────────────────────────
# 0. Validate parameter mutual exclusivity
# ──────────────────────────────────────────────
$modesSpecified = @(
    if ($ModelName) { "ModelName" }
    if ($Undo) { "Undo" }
    if ($List) { "List" }
)

if ($modesSpecified.Count -eq 0) {
    Write-Host "ERRORE: Specificare -ModelName <modello>, -Undo, oppure -List." -ForegroundColor Red
    Write-Host ""
    Write-Host "Esempi:"
    Write-Host "  .\setmodel-handler.ps1 -ModelName opencode-go/deepseek-v4-flash"
    Write-Host "  .\setmodel-handler.ps1 -Undo"
    Write-Host "  .\setmodel-handler.ps1 -List"
    exit 1
}

if ($modesSpecified.Count -gt 1) {
    Write-Error "ERRORE: Specificare una sola modalità: -ModelName, -Undo, oppure -List (non più di una)."
    exit 1
}

# ──────────────────────────────────────────────
# Common paths
# ──────────────────────────────────────────────
$omoRoot      = "$env:USERPROFILE\OneDrive - ITS ICT Piemonte\Desktop\Materie\.omo"
$scriptsDir   = "$omoRoot\scripts"

$ohMyOpenAgentPath = "$env:USERPROFILE\.config\opencode\oh-my-openagent.json"
$modelJsonPath     = "$env:USERPROFILE\.local\state\opencode\model.json"

# ──────────────────────────────────────────────
# Helper: get all backup files for a given base path
# ──────────────────────────────────────────────
function Get-BackupFiles {
    param([string]$BasePath)
    $pattern = "${BasePath}.bak.*"
    return @(Get-ChildItem -Path $pattern -ErrorAction SilentlyContinue | Sort-Object Name -Descending)
}

# ──────────────────────────────────────────────
# Helper: rotate backups (keep max N, delete oldest)
# ──────────────────────────────────────────────
function Invoke-BackupRotation {
    param(
        [string]$BasePath,
        [int]$MaxBackups = 3
    )
    $backups = Get-BackupFiles -BasePath $BasePath
    if ($backups.Count -gt $MaxBackups) {
        $toDelete = $backups | Select-Object -Skip $MaxBackups
        foreach ($b in $toDelete) {
            Remove-Item -Path $b.FullName -Force
            Write-Host "[setmodel] Backup vecchio rimosso: $($b.Name)" -ForegroundColor DarkYellow
        }
    }
}

# ──────────────────────────────────────────────
# Helper: parse timestamp from backup filename
# ──────────────────────────────────────────────
function Get-BackupTimestamp {
    param([string]$FileName)
    if ($FileName -match '\.bak\.(\d{8}-\d{6})$') {
        $ts = $matches[1]
        $year   = $ts.Substring(0,4)
        $month  = $ts.Substring(4,2)
        $day    = $ts.Substring(6,2)
        $hour   = $ts.Substring(9,2)
        $minute = $ts.Substring(11,2)
        $second = $ts.Substring(13,2)
        try {
            return Get-Date -Year $year -Month $month -Day $day -Hour $hour -Minute $minute -Second $second
        } catch {
            return $null
        }
    }
    return $null
}

# ──────────────────────────────────────────────
# Helper: find latest backup for a file
# ──────────────────────────────────────────────
function Get-LatestBackup {
    param([string]$BasePath)
    $backups = Get-BackupFiles -BasePath $BasePath
    if ($backups.Count -eq 0) { return $null }
    # Already sorted descending by name (timestamp DESC)
    return $backups[0]
}

# ==================================================
# MODE: -List
# ==================================================
if ($List) {
    Write-Host "`n=== Backup Disponibili ===" -ForegroundColor Cyan
    Write-Host ""

    $ohMyBackups = Get-BackupFiles -BasePath $ohMyOpenAgentPath
    $modelBackups = Get-BackupFiles -BasePath $modelJsonPath

    if ($ohMyBackups.Count -eq 0 -and $modelBackups.Count -eq 0) {
        Write-Host "Nessun backup disponibile." -ForegroundColor Yellow
        exit 0
    }

    # Group by common timestamp across both files
    $allTimestamps = @{}
    foreach ($b in (@($ohMyBackups) + @($modelBackups))) {
        $ts = Get-BackupTimestamp -FileName $b.Name
        if ($ts) {
            $tsKey = $ts.ToString("yyyyMMdd-HHmmss")
            if (-not $allTimestamps.ContainsKey($tsKey)) {
                $allTimestamps[$tsKey] = @{ Timestamp = $ts; Files = @() }
            }
            $allTimestamps[$tsKey].Files += $b
        }
    }

    foreach ($key in ($allTimestamps.Keys | Sort-Object -Descending)) {
        $entry = $allTimestamps[$key]
        $tsFormatted = $entry.Timestamp.ToString("yyyy-MM-dd HH:mm:ss")
        Write-Host "── Backup del $tsFormatted ──" -ForegroundColor Green
        foreach ($f in $entry.Files) {
            $size = "{0:N0} bytes" -f $f.Length
            Write-Host "  📄 $($f.Name)  ($size)" -ForegroundColor Gray
        }
        Write-Host ""
    }

    exit 0
}

# ==================================================
# MODE: -Undo
# ==================================================
if ($Undo) {
    Write-Host "[setmodel] Modalità Undo avviata..." -ForegroundColor Cyan

    $latestOhMy = Get-LatestBackup -BasePath $ohMyOpenAgentPath
    $latestModel = Get-LatestBackup -BasePath $modelJsonPath

    if (-not $latestOhMy -and -not $latestModel) {
        Write-Host "ERRORE: nessun backup disponibile per il ripristino" -ForegroundColor Red
        exit 1
    }

    $restoredTimestamp = $null

    # Restore oh-my-openagent.json
    if ($latestOhMy) {
        $ts = Get-BackupTimestamp -FileName $latestOhMy.Name
        if ($ts) { $restoredTimestamp = $ts.ToString("yyyy-MM-dd HH:mm:ss") }
        Copy-Item -Path $latestOhMy.FullName -Destination $ohMyOpenAgentPath -Force
        Write-Host "[setmodel] Ripristinato: $($latestOhMy.Name)" -ForegroundColor Green
    } else {
        Write-Host "[setmodel] Nessun backup per oh-my-openagent.json, saltato." -ForegroundColor Yellow
    }

    # Restore model.json
    if ($latestModel) {
        $ts = Get-BackupTimestamp -FileName $latestModel.Name
        if (-not $restoredTimestamp -and $ts) { $restoredTimestamp = $ts.ToString("yyyy-MM-dd HH:mm:ss") }
        Copy-Item -Path $latestModel.FullName -Destination $modelJsonPath -Force
        Write-Host "[setmodel] Ripristinato: $($latestModel.Name)" -ForegroundColor Green
    } else {
        Write-Host "[setmodel] Nessun backup per model.json, saltato." -ForegroundColor Yellow
    }

    if (-not $restoredTimestamp) { $restoredTimestamp = "timestamp sconosciuto" }

    Write-Host "✅ Modello ripristinato da backup del $restoredTimestamp" -ForegroundColor Green

    # ── Supermemory recording after undo ──
    $recordScript = Join-Path $PSScriptRoot "record-model.ps1"
    if (Test-Path -LiteralPath $recordScript) {
        # Read the restored model from model.json
        if (Test-Path -LiteralPath $modelJsonPath) {
            try {
                $restoredModelContent = Get-Content -Path $modelJsonPath -Raw -ErrorAction Stop
                $restoredModelJson = $restoredModelContent | ConvertFrom-Json -ErrorAction SilentlyContinue
                if ($restoredModelJson -and $restoredModelJson.recent -and $restoredModelJson.recent.Count -gt 0) {
                    $entry0 = $restoredModelJson.recent[0]
                    $restoredProvider = if ($entry0.providerID) { $entry0.providerID } else { "opencode" }
                    $restoredModelId = if ($entry0.modelID) { $entry0.modelID } else { "" }
                    if ($restoredModelId) {
                        $restoredFullModel = "${restoredProvider}/${restoredModelId}"
                        Write-Host "[setmodel] Registro modello ripristinato in Supermemory: '$restoredFullModel'..." -ForegroundColor Cyan
                        & $recordScript -ModelName $restoredFullModel
                    }
                }
            } catch {
                Write-Host "[setmodel] WARN: Impossibile leggere model.json per Supermemory recording: $_" -ForegroundColor Yellow
            }
        }
    } else {
        Write-Host "[setmodel] WARN: record-model.ps1 non trovato, Supermemory recording saltato." -ForegroundColor Yellow
    }

    # ── Evidence ──
    $evidenceDir = Join-Path $omoRoot "evidence\task-10"
    New-Item -ItemType Directory -Path $evidenceDir -Force | Out-Null
    $undoEvidence = @"
Undo eseguito il $(Get-Date -Format "yyyy-MM-dd HH:mm:ss"):
  Backup ripristinato del: ${restoredTimestamp}
  oh-my-openagent.json ripristinato da: $(if($latestOhMy){$latestOhMy.Name}else{'N/A'})
  model.json ripristinato da: $(if($latestModel){$latestModel.Name}else{'N/A'})
"@
    Set-Content -Path (Join-Path $evidenceDir "undo-test.txt") -Value $undoEvidence -Force
    Write-Host "[setmodel] Evidenza salvata in ${evidenceDir}\undo-test.txt"

    exit 0
}

# ==================================================
# MODE: -ModelName (original flow + backup rotation)
# ==================================================

# ── Parse ModelName → providerID / modelID ──
$providerID = "opencode"
$modelID   = $ModelName

if ($ModelName -match "/") {
    $slashIndex = $ModelName.IndexOf("/")
    $providerID = $ModelName.Substring(0, $slashIndex)
    $modelID    = $ModelName.Substring($slashIndex + 1)
}

Write-Host "[setmodel] ModelName = '$ModelName' → providerID='$providerID' modelID='$modelID'"

# ── Paths ──
$evidenceDir  = "$omoRoot\evidence\task-5"

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

# Ensure evidence dir exists
New-Item -ItemType Directory -Path $evidenceDir -Force | Out-Null

Write-Host "[setmodel] oh-my-openagent.json → $ohMyOpenAgentPath"
Write-Host "[setmodel] model.json          → $modelJsonPath"

# ── 1.5 Validazione modello (pre-check) ──
$validateScript = Join-Path $PSScriptRoot "validate-model.ps1"
if (-not (Test-Path -LiteralPath $validateScript)) {
    Write-Error "[setmodel] FATAL: validate-model.ps1 not found at $validateScript"
    exit 1
}

& $validateScript -ModelName $ModelName -ConfigPath $ohMyOpenAgentPath
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
Write-Host "[setmodel] Validazione superata per '$ModelName'."

# ── 2. Helper: recursively update ALL 'model' string fields ──
function Set-ModelFieldsRecursive {
    param(
        [Parameter(Mandatory = $true)]
        [object]$InputObject,
        [Parameter(Mandatory = $true)]
        [string]$NewModel
    )

    if ($null -eq $InputObject) { return }

    # PSCustomObject (from ConvertFrom-Json)
    if ($InputObject -is [System.Management.Automation.PSCustomObject]) {
        foreach ($prop in $InputObject.PSObject.Properties) {
            if ($prop.Name -eq "model" -and $prop.Value -is [string]) {
                $prop.Value = $NewModel
            }
            elseif ($prop.Value -is [System.Management.Automation.PSCustomObject]) {
                Set-ModelFieldsRecursive -InputObject $prop.Value -NewModel $NewModel
            }
            elseif ($prop.Value -is [System.Collections.IList]) {
                foreach ($item in $prop.Value) {
                    Set-ModelFieldsRecursive -InputObject $item -NewModel $NewModel
                }
            }
        }
    }
    # Hashtable (fallback)
    elseif ($InputObject -is [System.Collections.IDictionary]) {
        foreach ($key in $InputObject.Keys) {
            if ($key -eq "model" -and $InputObject[$key] -is [string]) {
                $InputObject[$key] = $NewModel
            }
            elseif ($InputObject[$key] -is [System.Management.Automation.PSCustomObject] -or
                    $InputObject[$key] -is [System.Collections.IDictionary]) {
                Set-ModelFieldsRecursive -InputObject $InputObject[$key] -NewModel $NewModel
            }
            elseif ($InputObject[$key] -is [System.Collections.IList]) {
                foreach ($item in $InputObject[$key]) {
                    Set-ModelFieldsRecursive -InputObject $item -NewModel $NewModel
                }
            }
        }
    }
    # Array
    elseif ($InputObject -is [System.Collections.IList]) {
        foreach ($item in $InputObject) {
            Set-ModelFieldsRecursive -InputObject $item -NewModel $NewModel
        }
    }
}

# ── 3. Update oh-my-openagent.json ──
Write-Host "[setmodel] Reading oh-my-openagent.json..."

if (-not (Test-Path -LiteralPath $ohMyOpenAgentPath)) {
    Write-Error "[setmodel] FATAL: oh-my-openagent.json not found at $ohMyOpenAgentPath"
    exit 1
}

$ohMyContent = Get-Content -Path $ohMyOpenAgentPath -Raw -ErrorAction Stop
$ohMyJson = $ohMyContent | ConvertFrom-Json -ErrorAction Stop
if ($null -eq $ohMyJson) {
    Write-Error "[setmodel] FATAL: Failed to parse oh-my-openagent.json"
    exit 1
}
Write-Host "[setmodel] oh-my-openagent.json parsed successfully."

# Backup
$ohMyBackup = "${ohMyOpenAgentPath}.bak.${timestamp}"
Copy-Item -Path $ohMyOpenAgentPath -Destination $ohMyBackup -Force
Write-Host "[setmodel] Backup created: $ohMyBackup"

# Rotate backups for oh-my-openagent.json (keep max 3)
Invoke-BackupRotation -BasePath $ohMyOpenAgentPath -MaxBackups 3

# Update ALL model fields
Set-ModelFieldsRecursive -InputObject $ohMyJson -NewModel $ModelName

# Write back (Depth=10 ensures fallback_models[].model is not truncated)
$ohMyJson | ConvertTo-Json -Depth 10 | Set-Content -Path $ohMyOpenAgentPath -Force -Encoding UTF8
Write-Host "[setmodel] oh-my-openagent.json updated."

# ── 4. Update model.json ──
Write-Host "[setmodel] Reading model.json..."

if (-not (Test-Path -LiteralPath $modelJsonPath)) {
    Write-Error "[setmodel] FATAL: model.json not found at $modelJsonPath"
    Write-Host "[setmodel] Rolling back oh-my-openagent.json from backup..."
    Copy-Item -Path $ohMyBackup -Destination $ohMyOpenAgentPath -Force
    Write-Host "[setmodel] Rollback complete."
    exit 1
}

$modelContent = Get-Content -Path $modelJsonPath -Raw -ErrorAction Stop
$modelJson = $modelContent | ConvertFrom-Json -ErrorAction Stop
if ($null -eq $modelJson) {
    Write-Error "[setmodel] FATAL: Failed to parse model.json"
    Write-Host "[setmodel] Rolling back oh-my-openagent.json from backup..."
    Copy-Item -Path $ohMyBackup -Destination $ohMyOpenAgentPath -Force
    Write-Host "[setmodel] Rollback complete."
    exit 1
}
Write-Host "[setmodel] model.json parsed successfully."

# Backup
$modelBackup = "${modelJsonPath}.bak.${timestamp}"
Copy-Item -Path $modelJsonPath -Destination $modelBackup -Force
Write-Host "[setmodel] Backup created: $modelBackup"

# Rotate backups for model.json (keep max 3)
Invoke-BackupRotation -BasePath $modelJsonPath -MaxBackups 3

# New entry
$newEntry = @{
    providerID = $providerID
    modelID    = $modelID
}

# Ensure 'recent' exists
if ($null -eq $modelJson.recent) {
    $modelJson | Add-Member -MemberType NoteProperty -Name "recent" -Value @()
    $recent = @()
}
else {
    $recent = @($modelJson.recent)
}

# Dedup: remove existing entries with same providerID+modelID
$recent = @($recent | Where-Object {
    -not ($_.providerID -eq $providerID -and $_.modelID -eq $modelID)
})

# Prepend new entry
$recent = @($newEntry) + $recent

# Trim to max 10
if ($recent.Count -gt 10) {
    $recent = $recent[0..9]
}

$modelJson.recent = $recent

# Write back
$modelJson | ConvertTo-Json -Depth 10 | Set-Content -Path $modelJsonPath -Force -Encoding UTF8
Write-Host "[setmodel] model.json updated."

# ── 5. Supermemory recording ──
$recordScriptSM = Join-Path $PSScriptRoot "record-model.ps1"
if (Test-Path -LiteralPath $recordScriptSM) {
    Write-Host "[setmodel] Registro modello in Supermemory: '$ModelName'..." -ForegroundColor Cyan
    & $recordScriptSM -ModelName $ModelName
} else {
    Write-Host "[setmodel] WARN: record-model.ps1 non trovato, Supermemory recording saltato." -ForegroundColor Yellow
}

# ── 6. Create evidence files ──
$backupEvidence = @"
Backup files created at ${timestamp}:
  1. ${ohMyBackup}
  2. ${modelBackup}

Operation: /setmodel handler execution
"@
Set-Content -Path (Join-Path $evidenceDir "backup-test.txt") -Value $backupEvidence -Force

$updateEvidence = @"
Model update at ${timestamp}:
  - ModelName:        ${ModelName}
  - Parsed providerID: ${providerID}
  - Parsed modelID:    ${modelID}

oh-my-openagent.json:
  - Tutti i campi 'model' in agents.* e categories.* impostati a '${ModelName}'
  - Campi fallback_models preservati, solo 'model' al loro interno aggiornati

model.json:
  - Preposto { providerID: '${providerID}', modelID: '${modelID}' } a 'recent'
  - Deduplicato (rimossa vecchia entry per stesso providerID+modelID se presente)
  - Recent array ora contiene $($recent.Count) entries (max 10)
"@
Set-Content -Path (Join-Path $evidenceDir "update-test.txt") -Value $updateEvidence -Force

Write-Host "[setmodel] Evidence files created in ${evidenceDir}"
Write-Host "[setmodel] ✅ Done! Model set to '${ModelName}'"
