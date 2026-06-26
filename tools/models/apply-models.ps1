<#
.SYNOPSIS
    Legge tools/models/agents-models.json e sincronizza i model fields in opencode.json.
    Ogni agente/subagente ottiene il proprio campo "model" in base alla configurazione centralizzata.

.DESCRIPTION
    Comportamento:
      1. Legge agents-models.json come sorgente di verità
      2. Crea backup con timestamp di opencode.json
      3. Per ogni agente in agents-models.json, imposta/cambia il campo "model" in opencode.json
      4. Imposta il campo "model" root-level di opencode.json al valore "default"
      5. Imposta il campo "model" di Sisyphus al valore "sisyphus"
      6. Mostra report delle modifiche

.PARAMETER ConfigPath
    Path a opencode.json. Default: ../opencode.json (relativo a questa script).

.PARAMETER ModelsPath
    Path a agents-models.json. Default: agents-models.json (stessa directory).

.PARAMETER Force
    Salta la conferma prima di scrivere.

.PARAMETER DryRun
    Mostra cosa cambierebbe senza scrivere.

.EXAMPLE
    .\apply-models.ps1 -DryRun
    .\apply-models.ps1 -Force
#>

param(
    [Parameter(Mandatory = $false)]
    [string]$ConfigPath = "$PSScriptRoot\..\..\opencode.json",

    [Parameter(Mandatory = $false)]
    [string]$ModelsPath = "$PSScriptRoot\agents-models.json",

    [Parameter(Mandatory = $false)]
    [switch]$Force,

    [Parameter(Mandatory = $false)]
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

# ─── Colori ─────────────────────────────────────────────────────
function Write-Info  { Write-Host $args[0] -ForegroundColor Cyan }
function Write-Ok    { Write-Host $args[0] -ForegroundColor Green }
function Write-Warn  { Write-Host $args[0] -ForegroundColor Yellow }
function Write-Err   { Write-Host $args[0] -ForegroundColor Red }
function Write-Diff  { Write-Host $args[0] -ForegroundColor Magenta }
function Write-Section { Write-Host "---- $($args[0]) ----" -ForegroundColor White -BackgroundColor DarkBlue }

# ─── Helper: pretty print JSON (preserve key order) ────────────
function Format-JsonPreserveOrder {
    param([Parameter(ValueFromPipeline = $true)] $InputObject, [int]$Depth = 10)
    process {
        # Use Newtonsoft.Json via PowerShell if available, otherwise ConvertTo-Json
        $json = $InputObject | ConvertTo-Json -Depth $Depth
        return $json
    }
}

# ─── Paths ─────────────────────────────────────────────────────
$resolvedConfig = Resolve-Path -LiteralPath $ConfigPath -ErrorAction SilentlyContinue
if (-not $resolvedConfig) {
    Write-Err "File non trovato: $ConfigPath"
    exit 1
}
$configDir = Split-Path -Parent $resolvedConfig

$resolvedModels = Resolve-Path -LiteralPath $ModelsPath -ErrorAction SilentlyContinue
if (-not $resolvedModels) {
    Write-Err "File non trovato: $ModelsPath"
    Write-Err "Crea prima tools/models/agents-models.json con la configurazione modelli."
    exit 1
}

Write-Info "apply-models: Sorgente modelli = $resolvedModels"
Write-Info "apply-models: Target config   = $resolvedConfig"

# ─── Read models config ────────────────────────────────────────
$modelConfig = Get-Content -Path $resolvedModels -Raw -Encoding UTF8 | ConvertFrom-Json
$defaultModel = $modelConfig.default
$sisyphusModel = $modelConfig.sisyphus
$agents = $modelConfig.agents.PSObject.Properties

Write-Info "apply-models: Default model = $defaultModel"
Write-Info "apply-models: Sisyphus model = $sisyphusModel"
Write-Info "apply-models: $(@($agents).Count) agent definitions loaded."

# ─── Read opencode.json ────────────────────────────────────────
$opencodeRaw = Get-Content -Path $resolvedConfig -Raw -Encoding UTF8
$opencodeJson = $opencodeRaw | ConvertFrom-Json

if ($null -eq $opencodeJson) {
    Write-Err "apply-models: FATAL: Impossibile parsare $resolvedConfig"
    exit 1
}

# ─── Collect changes (in memory first) ─────────────────────────
$changes = @()  # List of @{ Agent = "..."; Old = "..."; New = "..." }
$errors = @()

# ─── 1. Set root-level "model" ─────────────────────────────────
$rootCurrent = $opencodeJson.PSObject.Properties | Where-Object { $_.Name -eq "model" } | Select-Object -First 1
$rootCurrentModel = if ($rootCurrent) { $rootCurrent.Value } else { $null }

if ($rootCurrentModel -ne $defaultModel) {
    $changes += @{
        Agent = "(root)"
        Field = "model"
        Old = if ($rootCurrentModel) { $rootCurrentModel } else { "(non impostato)" }
        New = $defaultModel
    }
    if (-not $DryRun) {
        if (-not $rootCurrent) {
            $opencodeJson | Add-Member -MemberType NoteProperty -Name "model" -Value $defaultModel -Force
        } else {
            $rootCurrent.Value = $defaultModel
        }
    }
}

# ─── 2. Set Sisyphus model ─────────────────────────────────────
$sisyphusCurrent = if ($opencodeJson.agent.sisyphus.model) { $opencodeJson.agent.sisyphus.model } else { $null }
if ($sisyphusCurrent -ne $sisyphusModel) {
    $changes += @{
        Agent = "agent.sisyphus"
        Field = "model"
        Old = if ($sisyphusCurrent) { $sisyphusCurrent } else { "(non impostato)" }
        New = $sisyphusModel
    }
    if (-not $DryRun) {
        $opencodeJson.agent.sisyphus | Add-Member -MemberType NoteProperty -Name "model" -Value $sisyphusModel -Force
    }
}

# ─── 3. Set each agent's model ─────────────────────────────────
foreach ($agent in $agents) {
    $agentName = $agent.Name
    $agentModel = $agent.Value

    # Skip empty
    if ([string]::IsNullOrWhiteSpace($agentModel)) { continue }

    # Check if agent exists in opencode.json
    $agentEntry = $opencodeJson.agent.$agentName
    if ($null -eq $agentEntry) {
        $errors += "Agente '$agentName' definito in agents-models.json ma NON presente in opencode.json. Saltato."
        continue
    }

    $currentModel = $agentEntry.model
    if ($null -eq $currentModel) { $currentModel = "(non impostato)" }

    if ($currentModel -ne $agentModel) {
        $changes += @{
            Agent = "agent.$agentName"
            Field = "model"
            Old = $currentModel
            New = $agentModel
        }
        if (-not $DryRun) {
            $agentEntry | Add-Member -MemberType NoteProperty -Name "model" -Value $agentModel -Force
        }
    }
}

# ─── 4. Report ─────────────────────────────────────────────────
Write-Info "`n===================== REPORT MODIFICHE ====================="

if ($errors.Count -gt 0) {
    Write-Warn "`n⚠ Avvisi:"
    foreach ($e in $errors) { Write-Warn "  ⚠ $e" }
}

if ($changes.Count -eq 0) {
    Write-Ok "Nessuna modifica necessaria. Tutti i model fields sono già allineati."
    exit 0
}

Write-Host "`n$($changes.Count) modifica/e da applicare:" -ForegroundColor White
foreach ($c in $changes) {
    Write-Diff "  • $($c.Agent).$($c.Field): $($c.Old) -> $($c.New)"
}

if ($DryRun) {
    Write-Info "`n[DryRun] Nessuna scrittura effettuata. Usa -Force per applicare."
    exit 0
}

# ─── 5. Confirm ────────────────────────────────────────────────
if (-not $Force) {
    $confirm = Read-Host "`nApplicare le modifiche? (s/N)"
    if ($confirm -ne "s" -and $confirm -ne "S") {
        Write-Info "Annullato dall'utente."
        exit 0
    }
}

# ─── 6. Create backup ──────────────────────────────────────────
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backupFile = Join-Path -Path $configDir -ChildPath "opencode.json.models-backup.$timestamp"
Copy-Item -LiteralPath $resolvedConfig -Destination $backupFile -Force
Write-Ok "Backup creato: $($backupFile | Split-Path -Leaf)"

# ─── 7. Write updated config ───────────────────────────────────
$opencodeJson | ConvertTo-Json -Depth 10 | Set-Content -Path $resolvedConfig -Force -Encoding UTF8
Write-Ok "apply-models: $resolvedConfig aggiornato con $($changes.Count) modifiche."

# ─── 8. Update last_updated in agents-models.json ──────────────
$now = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
$modelConfig | Add-Member -MemberType NoteProperty -Name "last_updated" -Value $now -Force
$modelConfig | ConvertTo-Json -Depth 10 | Set-Content -Path $resolvedModels -Force -Encoding UTF8

Write-Info "`nPer verificare: apri opencode.json e controlla i campi 'model' di ogni agente."
Write-Info "Per annullare: copia il backup $($backupFile | Split-Path -Leaf) su opencode.json."

Write-Section "Operazione completata"
