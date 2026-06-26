<#
.SYNOPSIS
    Record the current model in Supermemory for cross-session persistence.
.DESCRIPTION
    This script stores a model identifier in Supermemory using the prefix "model:".
    Designed to be called from the /setmodel handler or standalone.

    Supermemory pattern:
        mode: "add", content: "model:<ModelName>", type: "preference", scope: "user"

.PARAMETER ModelName
    The model identifier to record (e.g. "opencode-go/deepseek-v4-flash").

.EXAMPLE
    .\record-model.ps1 -ModelName "opencode-go/deepseek-v4-flash"
#>

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$ModelName
)

$ErrorActionPreference = "Stop"

# ── Paths ──────────────────────────────────────────────────────────────────
$ConfigPath  = "$env:USERPROFILE\.config\opencode\supermemory.jsonc"
$BunPath     = "$env:USERPROFILE\.bun\bin\bun.exe"

# ── Colours ────────────────────────────────────────────────────────────────
function Write-Info { Write-Host "[INFO] $($args -join ' ')" -ForegroundColor Cyan }
function Write-Ok   { Write-Host "[OK] $($args -join ' ')" -ForegroundColor Green }
function Write-Warn { Write-Host "[WARN] $($args -join ' ')" -ForegroundColor Yellow }

# ── Validate ───────────────────────────────────────────────────────────────
if (-not (Test-Path -LiteralPath $ConfigPath)) {
    Write-Warn "Supermemory not configured: '$ConfigPath' not found. Skipping."
    exit 0
}
if (-not (Test-Path -LiteralPath $BunPath)) {
    Write-Warn "Bun not found: '$BunPath'. Skipping."
    exit 0
}

try {
    $raw = Get-Content -Raw -LiteralPath $ConfigPath
    $ApiKey = ($raw | ConvertFrom-Json).apiKey
    if (-not $ApiKey) { throw "apiKey missing" }
} catch {
    Write-Warn "Cannot read apiKey from config. Skipping."
    exit 0
}

# ── Inline JavaScript payload ──────────────────────────────────────────────
Write-Info "Recording model '$ModelName' in Supermemory..."

$jsCode = @"
const crypto = require('crypto');
const { execSync } = require('child_process');

// 1. Compute user container tag (same logic as opencode-supermemory plugin)
let email;
try { email = execSync('git config user.email', { encoding: 'utf-8' }).trim(); }
catch { email = process.env.USERNAME || 'anonymous'; }
const hash = crypto.createHash('sha256').update(email).digest('hex').substring(0, 16);
const userTag = 'opencode_user_' + hash;

// 2. Read API key
const apiKey = JSON.parse(
    require('fs').readFileSync(
        require('path').join(require('os').homedir(), '.config/opencode/supermemory.jsonc'),
        'utf-8'
    )
).apiKey;

// 3. Call Supermemory API: POST /v3/documents
const https = require('https');
const body = JSON.stringify({
    content: 'model:$ModelName',
    containerTag: userTag,
    metadata: {
        type: 'preference',
        sm_source: 'opencode',
        sm_capture_mode: 'script'
    }
});

const opts = {
    hostname: 'api.supermemory.ai',
    path: '/v3/documents',
    method: 'POST',
    headers: {
        'Authorization': 'Bearer ' + apiKey,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
        'x-sm-source': 'opencode'
    }
};

const req = https.request(opts, (res) => {
    let data = '';
    res.on('data', (c) => { data += c; });
    res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
            try {
                const j = JSON.parse(data);
                console.log('OK:' + (j.id || j.status || 'done'));
            } catch {
                console.log('OK:' + (data.substring(0, 80) || 'done'));
            }
        } else {
            console.log('FAIL:' + res.statusCode + ':' + data.substring(0, 200));
        }
    });
});
req.on('error', (e) => console.log('FAIL:0:' + e.message));
req.write(body);
req.end();
"@

# Write JS to temp file & execute
$tmpFile = [System.IO.Path]::GetTempFileName() + ".js"
try {
    Set-Content -Path $tmpFile -Value $jsCode -Encoding UTF8
    $output = & $BunPath run $tmpFile 2>&1
    $exitCode = $LASTEXITCODE

    if ($output -match '^OK:') {
        Write-Ok "Model '$ModelName' recorded in Supermemory ($($output -replace '^OK:', ''))"
    } elseif ($output -match '^FAIL:') {
        Write-Warn "Supermemory API error: $($output -replace '^FAIL:', '')"
    } else {
        Write-Warn "Unexpected output: $output"
    }
} catch {
    Write-Warn "Failed: $_"
} finally {
    if (Test-Path $tmpFile) { Remove-Item $tmpFile -Force }
}
