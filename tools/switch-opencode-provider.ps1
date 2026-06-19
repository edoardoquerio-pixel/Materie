<#
.SYNOPSIS
    Switches all agents in opencode.json between OpenCode Zen (free) and OpenCode Go (paid) providers.

.DESCRIPTION
    Detects the current provider state and swaps model IDs for ALL agents (top-level model,
    small_model, and every agent.model) between Zen free models and their Go equivalents.
    Creates a timestamped backup before any modification.

    Going FROM Zen TO Go: applies model substitution (forward mapping).
    Going FROM Go TO Zen: restores from the most recent *.zen-backup.* (exact recovery).

.PARAMETER To
    Target provider: "Go" to switch from Zen to Go, "Zen" to switch from Go to Zen.

.PARAMETER ConfigPath
    Path to opencode.json. Defaults to the Materie workspace root.

.PARAMETER Force
    Skip confirmation prompt.

.EXAMPLE
    .\switch-opencode-provider.ps1 -To Go
    Switch all agents from Zen free models to Go paid models.

.EXAMPLE
    .\switch-opencode-provider.ps1 -To Zen
    Restore all agents back to Zen free models (uses most recent backup).

.NOTES
    Forward Model Mapping (Zen free -> Go):
      opencode/deepseek-v4-flash-free  -> opencode-go/deepseek-v4-flash
      opencode/nemotron-3-ultra-free   -> opencode-go/deepseek-v4-flash
      opencode/north-mini-code-free    -> opencode-go/mimo-v2.5
      opencode/mimo-v2.5-free          -> opencode-go/mimo-v2.5
      opencode/big-pickle              -> UNCHANGED (not a Zen model)

    Reverse (Go -> Zen): restores from backup for exact original state.
#>

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("Go", "Zen")]
    [string]$To,

    [Parameter(Mandatory = $false)]
    [string]$ConfigPath = "$PSScriptRoot\..\opencode.json",

    [Parameter(Mandatory = $false)]
    [switch]$Force
)

# === Helpers ================================================================

function Write-Info  { Write-Host $args[0] -ForegroundColor Cyan }
function Write-Ok    { Write-Host $args[0] -ForegroundColor Green }
function Write-Warn  { Write-Host $args[0] -ForegroundColor Yellow }
function Write-Err   { Write-Host $args[0] -ForegroundColor Red }
function Write-Diff  { Write-Host $args[0] -ForegroundColor Magenta }

function Write-Section {
    $msg = $args[0]
    Write-Host "---- $msg ----" -ForegroundColor White -BackgroundColor DarkBlue
}

# === Validation =============================================================

$resolvedPath = Resolve-Path -LiteralPath $ConfigPath -ErrorAction SilentlyContinue
if (-not $resolvedPath) {
    Write-Err "File non trovato: $ConfigPath"
    exit 1
}
$configDir = Split-Path -Parent $resolvedPath

Write-Section "Provider Switch: -> $To"

# === Read current config ====================================================

$config = Get-Content -LiteralPath $resolvedPath -Raw -Encoding UTF8
if (-not $config) {
    Write-Err "Impossibile leggere $resolvedPath"
    exit 1
}

# === Detect current provider ================================================

$isCurrentlyGo = $config -match 'opencode-go/'
$isCurrentlyZen = $config -match 'opencode/.+?-free'

if (-not $isCurrentlyGo -and -not $isCurrentlyZen) {
    Write-Warn "Nessun modello Zen (-free) o Go (opencode-go/) trovato. Nessuna modifica."
    exit 0
}

# === Route based on direction ===============================================

if ($To -eq "Go") {
    # ── FORWARD: Zen -> Go ─────────────────────────────────────────────────
    if ($isCurrentlyGo -and -not $isCurrentlyZen) {
        Write-Ok "Gia su provider Go. Nessuna modifica necessaria."
        exit 0
    }

    # Mapping table: Zen -> Go
    $zenToGo = @{
        "opencode/deepseek-v4-flash-free"  = "opencode-go/deepseek-v4-flash"
        "opencode/nemotron-3-ultra-free"   = "opencode-go/deepseek-v4-flash"
        "opencode/north-mini-code-free"    = "opencode-go/mimo-v2.5"
        "opencode/mimo-v2.5-free"          = "opencode-go/mimo-v2.5"
    }

    if (-not $Force) {
        Write-Warn "Stai per cambiare provider: Zen (free) -> Go (paid)"
        Write-Warn "File: $resolvedPath"
        $confirm = Read-Host "Procedere? (s/N)"
        if ($confirm -ne "s" -and $confirm -ne "S") {
            Write-Info "Annullato dall'utente."
            exit 0
        }
    }

    # Create backup
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupFile = Join-Path -Path $configDir -ChildPath "opencode.json.zen-backup.$timestamp"
    Copy-Item -LiteralPath $resolvedPath -Destination $backupFile -Force
    Write-Ok "Backup creato: $($backupFile | Split-Path -Leaf)"

    # Apply forward replacements
    $changes = @()
    $modifiedConfig = $config
    foreach ($zen in $zenToGo.Keys) {
        $go = $zenToGo[$zen]
        if ($modifiedConfig -match [regex]::Escape($zen)) {
            $count = [regex]::Matches($modifiedConfig, [regex]::Escape($zen)).Count
            $modifiedConfig = $modifiedConfig -replace [regex]::Escape($zen), $go
            $changes += @{ From = $zen; To = $go; Count = $count }
            Write-Diff "$zen -> $go (x$count)"
        }
    }

    # Write new config
    $modifiedConfig | Set-Content -LiteralPath $resolvedPath -Encoding UTF8 -NoNewline
    Write-Ok "File aggiornato: $resolvedPath"

    # Summary
    Write-Section "Riepilogo modifiche"
    if ($changes.Count -eq 0) {
        Write-Warn "Nessuna modifica effettuata."
    } else {
        foreach ($c in $changes) {
            Write-Host "  $($c.From)  ->  $($c.To)  (x$($c.Count))" -ForegroundColor Yellow
        }
    }

    Write-Section "Operazione completata"
    Write-Info "Per tornare a Zen: .\switch-opencode-provider.ps1 -To Zen"
    Write-Info "Backup: $($backupFile | Split-Path -Leaf)"

} else {
    # ── REVERSE: Go -> Zen ─────────────────────────────────────────────────
    if ($isCurrentlyZen -and -not $isCurrentlyGo) {
        Write-Ok "Gia su provider Zen. Nessuna modifica necessaria."
        exit 0
    }

    # Find most recent zen-backup file in the config directory
    $backupPattern = Join-Path -Path $configDir -ChildPath "opencode.json.zen-backup.*"
    $backups = Get-ChildItem -LiteralPath $backupPattern | Sort-Object LastWriteTime -Descending
    if (-not $backups) {
        Write-Err "Nessun backup Zen trovato con pattern: $backupPattern"
        Write-Err "Impossibile ripristinare. Esegui manualmente il reverse mapping dal backup."
        exit 1
    }
    $restoreFile = $backups[0].FullName

    if (-not $Force) {
        Write-Warn "Stai per ripristinare: Go (paid) -> Zen (free)"
        Write-Warn "File sorgente: $resolvedPath"
        Write-Warn "Backup da ripristinare: $($backups[0].Name) ($($backups[0].LastWriteTime))"
        $confirm = Read-Host "Procedere? (s/N)"
        if ($confirm -ne "s" -and $confirm -ne "S") {
            Write-Info "Annullato dall'utente."
            exit 0
        }
    }

    # Create a Go-backup before restoring Zen
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $goBackup = Join-Path -Path $configDir -ChildPath "opencode.json.go-backup.$timestamp"
    Copy-Item -LiteralPath $resolvedPath -Destination $goBackup -Force
    Write-Ok "Backup Go creato: $($goBackup | Split-Path -Leaf)"

    # Restore from the most recent zen-backup
    Copy-Item -LiteralPath $restoreFile -Destination $resolvedPath -Force
    Write-Ok "Ripristinato da: $($restoreFile | Split-Path -Leaf)"

    Write-Section "Operazione completata"
    Write-Info "Per tornare a Go: .\switch-opencode-provider.ps1 -To Go"
    Write-Info "Backup Go salvato: $($goBackup | Split-Path -Leaf)"
}
