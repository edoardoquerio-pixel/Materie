<#
.SYNOPSIS
    Applica un modello a tutti gli agenti in opencode.json.
.DESCRIPTION
    Legge il modello da default.json o dal parametro -Model e riscrive
    TUTTI i campi "model" in opencode.json (top-level e per ogni agente).
    Crea un backup con timestamp prima di modificare.
.PARAMETER Model
    Modello da applicare (es. "opencode/deepseek-v4-flash-free").
    Se omesso, viene letto da default.json.
.PARAMETER Force
    Esegue senza chiedere conferma.
.EXAMPLE
    .\tools\models\apply-model.ps1
    Applica il modello da default.json.

    .\tools\models\apply-model.ps1 -Model "opencode/big-pickle"
    Applica big-pickle a TUTTI gli agenti.

    .\tools\models\apply-model.ps1 -Model "opencode-go/deepseek-v4-flash" -Force
    Applica senza conferma (utile per switch automatici).
#>

param(
    [string]$Model,
    [switch]$Force
)

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path "$scriptRoot\..\.."
$configPath = Join-Path $repoRoot "opencode.json"
$defaultPath = Join-Path $scriptRoot "default.json"

# ---- 1. Determina modello ----
if (-not $Model) {
    if (Test-Path $defaultPath) {
        try {
            $default = Get-Content $defaultPath -Raw -Encoding UTF8 | ConvertFrom-Json
            $Model = $default.model
            if (-not $Model) {
                Write-Error "default.json non contiene un campo 'model' valido."
                exit 1
            }
            Write-Host "Modello letto da default.json: $Model"
        }
        catch {
            Write-Error "Errore leggendo default.json: $_"
            exit 1
        }
    }
    else {
        Write-Error "Nessun parametro -Model specificato e default.json non trovato in $scriptRoot"
        exit 1
    }
}

# ---- 2. Backup ----
$timestamp = Get-Date -Format "yyyyMMddHHmmss"
$backupPath = "$configPath.backup.$timestamp"
try {
    Copy-Item $configPath $backupPath -ErrorAction Stop
    Write-Host "Backup creato: $backupPath" -ForegroundColor Green
}
catch {
    Write-Error "Impossibile creare backup: $_"
    exit 1
}

# ---- 3. Conferma (salta con -Force) ----
if (-not $Force) {
    Write-Host "`nStai per applicare il modello '$Model' a TUTTI gli agenti in opencode.json" -ForegroundColor Yellow
    Write-Host "Un backup è stato salvato in: $backupPath`n" -ForegroundColor Gray
    $confirm = Read-Host "Proseguire? (s/N)"
    if ($confirm -ne "s" -and $confirm -ne "S") {
        Write-Host "Operazione annullata." -ForegroundColor Red
        exit 0
    }
}

# ---- 4. Applica modello ----
try {
    $content = Get-Content $configPath -Raw -Encoding UTF8
    $originalContent = $content

    # Sostituisce TUTTE le occorrenze di "model": "qualcosa" con il nuovo modello
    $replacement = '"model": "' + $Model + '"'
    $content = $content -replace '"model":\s*"[^"]*"', $replacement

    if ($content -eq $originalContent) {
        Write-Warning "Nessuna occorrenza di 'model' trovata in $configPath. Il file non è stato modificato."
        exit 0
    }

    $content | Set-Content $configPath -Encoding UTF8 -NoNewline

    # Conta quante sostituzioni sono state fatte
    $originalCount = [regex]::Matches($originalContent, '"model":\s*"[^"]*"').Count
    $newCount = [regex]::Matches($content, '"model":\s*"[^"]*"').Count

    Write-Host "`nModello '$Model' applicato con successo!" -ForegroundColor Green
    Write-Host "  Campi 'model' aggiornati: $originalCount" -ForegroundColor Cyan
    Write-Host "  File: $configPath" -ForegroundColor Gray
    Write-Host "`nPer ripristinare il backup precedente:" -ForegroundColor Gray
    Write-Host "  Copy-Item '$backupPath' '$configPath'" -ForegroundColor Gray
}
catch {
    Write-Error "Errore durante l'applicazione del modello: $_"
    Write-Host "Ripristina il backup con: Copy-Item '$backupPath' '$configPath'" -ForegroundColor Yellow
    exit 1
}
