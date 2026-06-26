<#
.SYNOPSIS
    Validazione del nome modello per /setmodel handler.

.DESCRIPTION
    Esegue controlli di validazione sul nome modello PRIMA che venga passato
    all'handler /setmodel. Se la validazione fallisce, esce con codice errore.

    Casi gestiti:
      - Arg vuoto         → exit 1
      - Caratteri invalidi → exit 2
      - Lunghezza max      → exit 3
      - File non trovato   → exit 4
      - Backup fallito     → exit 5
      - Successo           → exit 0

.PARAMETER ModelName
    Nome completo del modello da validare, es: "opencode-go/deepseek-v4-flash".

.PARAMETER ConfigPath
    Path assoluto al file oh-my-openagent.json. Default:
    $env:USERPROFILE\.config\opencode\oh-my-openagent.json

.EXAMPLE
    .\validate-model.ps1 -ModelName "opencode-go/deepseek-v4-flash"
    .\validate-model.ps1 -ModelName ""                          # exit 1
    .\validate-model.ps1 -ModelName "modello con spazi"         # exit 2
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$ModelName,

    [Parameter(Mandatory = $false)]
    [string]$ConfigPath = "$env:USERPROFILE\.config\opencode\oh-my-openagent.json"
)

# ──────────────────────────────────────────────
# 1. Argomento vuoto
# ──────────────────────────────────────────────
if ([string]::IsNullOrWhiteSpace($ModelName)) {
    Write-Output "ERRORE: nessun modello specificato. Usa /setmodel <nome-modello>"
    exit 1
}

# ──────────────────────────────────────────────
# 2. Caratteri non consentiti
#    Sono permessi: a-z, A-Z, 0-9, /, -, ., spazio
# ──────────────────────────────────────────────
# Se MATCHA caratteri NON nel set permesso → rifiuta
if ($ModelName -match '[^a-zA-Z0-9/\-.\s]') {
    Write-Output "ERRORE: caratteri non consentiti nel nome modello. Sono permessi solo lettere, numeri, /, -, ., spazio"
    exit 2
}

# ──────────────────────────────────────────────
# 3. Lunghezza massima (> 100 caratteri)
# ──────────────────────────────────────────────
if ($ModelName.Length -gt 100) {
    Write-Output "ERRORE: nome modello troppo lungo (max 100 caratteri)"
    exit 3
}

# ──────────────────────────────────────────────
# 4. File di configurazione non trovato
# ──────────────────────────────────────────────
if (-not (Test-Path -LiteralPath $ConfigPath)) {
    Write-Output "ERRORE: file di configurazione non trovato al path: $ConfigPath"
    exit 4
}

# ──────────────────────────────────────────────
# 5. Backup fallito — verifica che si possa
#    scrivere nella directory del config
# ──────────────────────────────────────────────
$configDir = Split-Path -Parent $ConfigPath -ErrorAction SilentlyContinue
if ($configDir) {
    $timestamp  = Get-Date -Format "yyyyMMdd-HHmmss"
    $testFile   = Join-Path $configDir ".validate-backup-test.${timestamp}.tmp"

    try {
        "test" | Out-File -FilePath $testFile -Force -ErrorAction Stop
        Remove-Item -Path $testFile -Force -ErrorAction SilentlyContinue
    }
    catch {
        Write-Output "ERRORE: impossibile creare backup. Operazione annullata."
        exit 5
    }
}

# ──────────────────────────────────────────────
# 6. Tutti i controlli superati ✅
# ──────────────────────────────────────────────
exit 0
