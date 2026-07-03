#requires -Version 5.1

<#
.SYNOPSIS
    Scarica automaticamente tutti i materiali dai corsi FAD (Moodle/Open LMS con Snap theme)
    direttamente nelle cartelle 01_Materiale/ di ogni materia.

.PARAMETER CourseId
    ID del corso FAD da scaricare. Usa "*" o "all" per scaricare TUTTI i corsi configurati.
    Usa "list" per vedere la lista dei corsi disponibili.
    Default: scarica tutti i corsi.

.PARAMETER ConfigPath
    Path del file JSON di configurazione (mapping corsi FAD -> directory locali).
    Default: fad-courses.json nella stessa cartella dello script.

.PARAMETER EnvFile
    Path del file .env con le credenziali FAD.

.EXAMPLE
    # Scarica TUTTI i corsi
    .\download-fad.ps1

    # Scarica solo un corso specifico
    .\download-fad.ps1 -CourseId 2225

    # Scarica più corsi
    .\download-fad.ps1 -CourseId 2225,2218,2235

    # Mostra la lista corsi
    .\download-fad.ps1 -CourseId list
#>

param(
    [Parameter(Position=0)]
    [object]$CourseId = "all",
    [string]$ConfigPath = "",
    [string]$EnvFile = ""
)

Add-Type -AssemblyName System.Net.Http

# === PATHS (resolve script directory for defaults) ===
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $ConfigPath) { $ConfigPath = Join-Path -Path $scriptDir -ChildPath "fad-courses.json" }
if (-not $EnvFile) { $EnvFile = Join-Path -Path $scriptDir -ChildPath ".env" }
if (-not (Test-Path -LiteralPath $EnvFile)) {
    # Fallback: cerca nella cartella _FAD
    $fallbackEnv = Join-Path -Path $scriptDir -ChildPath "..\14_Cloud_Azure\_FAD\.env"
    if (Test-Path -LiteralPath $fallbackEnv) {
        $EnvFile = (Resolve-Path -LiteralPath $fallbackEnv).Path
        Write-Host "  .env trovato in _FAD (fallback)" -ForegroundColor DarkGray
    }
}

# === CONFIG ===

function Read-Config {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Error "File config non trovato: $Path"
        Write-Host "  Crea il file fad-courses.json con la mappa corsi FAD -> directory locali." -ForegroundColor Yellow
        exit 1
    }
    $config = Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
    return $config
}

function Read-EnvFile {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Error "File .env non trovato: $Path`nCopia .env.example in .env e inserisci le tue credenziali."
        exit 1
    }
    $envVars = @{}
    Get-Content -LiteralPath $Path | ForEach-Object {
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith('#')) {
            $parts = $line.Split('=', 2)
            if ($parts.Count -eq 2) { $envVars[$parts[0].Trim()] = $parts[1].Trim() }
        }
    }
    return $envVars
}

# === HELPERS ===

function ConvertTo-Hashtable {
    param([object]$InputObject)
    # PowerShell 5.1: ConvertFrom-Json restituisce PSCustomObject, non hashtable.
    # Questa funzione converte ricorsivamente in hashtable per permettere
    # assegnazioni dinamiche (es. $cache["nuovaChiave"] = "valore").
    if ($InputObject -is [System.Management.Automation.PSCustomObject]) {
        $ht = @{}
        $InputObject.PSObject.Properties | ForEach-Object {
            $ht[$_.Name] = ConvertTo-Hashtable -InputObject $_.Value
        }
        return $ht
    }
    elseif ($InputObject -is [System.Collections.IList]) {
        $list = @()
        foreach ($item in $InputObject) { $list += ConvertTo-Hashtable -InputObject $item }
        return $list
    }
    return $InputObject
}

# === HTTP CLIENT ===

function New-HttpClient {
    $cookieContainer = New-Object System.Net.CookieContainer
    $handler = New-Object System.Net.Http.HttpClientHandler
    $handler.CookieContainer = $cookieContainer
    $handler.AllowAutoRedirect = $true
    $handler.MaxAutomaticRedirections = 10
    
    $client = New-Object System.Net.Http.HttpClient($handler)
    $client.Timeout = [TimeSpan]::FromSeconds(120)
    $client.DefaultRequestHeaders.Add('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
    $client.DefaultRequestHeaders.Add('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
    $client.DefaultRequestHeaders.Add('Accept-Language', 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7')
    
    return @{
        Client = $client
        Handler = $handler
        Cookies = $cookieContainer
    }
}

# === FAD LOGIN ===

function Get-LoginToken {
    param($HttpClient)
    $response = $HttpClient.Client.GetAsync("https://fad.its-ictpiemonte.it/login/index.php").Result
    $html = $response.Content.ReadAsStringAsync().Result
    
    $tokenMatch = [regex]::Match($html, 'name="logintoken"\s+value="([^"]+)"')
    if ($tokenMatch.Success) {
        return $tokenMatch.Groups[1].Value
    }
    return $null
}

function Invoke-FadLogin {
    param($HttpClient, [string]$Username, [string]$Password)
    
    Write-Host "[LOGIN] Autenticazione come $Username..." -ForegroundColor Cyan
    
    $loginToken = Get-LoginToken -HttpClient $HttpClient
    if (-not $loginToken) { Write-Error "  Token login non trovato"; return $false }
    
    $formBuilder = New-Object System.Text.StringBuilder
    $formBuilder.Append("username=") | Out-Null
    $formBuilder.Append([System.Uri]::EscapeDataString($Username)) | Out-Null
    $formBuilder.Append("&password=") | Out-Null
    $formBuilder.Append([System.Uri]::EscapeDataString($Password)) | Out-Null
    $formBuilder.Append("&logintoken=") | Out-Null
    $formBuilder.Append([System.Uri]::EscapeDataString($loginToken)) | Out-Null
    
    $formContent = New-Object System.Net.Http.StringContent($formBuilder.ToString(), [System.Text.Encoding]::UTF8, "application/x-www-form-urlencoded")
    
    try {
        $response = $HttpClient.Client.PostAsync("https://fad.its-ictpiemonte.it/login/index.php", $formContent).Result
        $finalUrl = $response.RequestMessage.RequestUri.ToString()
        
        if ($finalUrl -notmatch '/login/') {
            Write-Host "  Login riuscito!`n" -ForegroundColor Green
            return $true
        }
        Write-Error "  Login fallito"
        return $false
    }
    catch {
        Write-Error "  Eccezione login: $_"
        return $false
    }
}

# === COURSE MODULE EXTRACTION ===

function Get-CourseModules {
    param($HttpClient, [int]$CourseId, [string]$CourseName)
    
    Write-Host "  Carico corso ID $CourseId ($CourseName)..." -ForegroundColor Gray
    
    $courseUrl = "https://fad.its-ictpiemonte.it/course/view.php?id=$CourseId"
    
    try {
        $response = $HttpClient.Client.GetAsync($courseUrl).Result
        $html = $response.Content.ReadAsStringAsync().Result
        
        if ($html -match 'notloggedin|Log in to the site|login/index') {
            Write-Host "    NON autenticato!" -ForegroundColor Red
            return $null
        }
        
        $modules = @()
        
        # === PASSO 1: Estrai lista moduli dalla TOC (Snap theme) ===
        # La TOC contiene TUTTI i moduli con data-id, icona (che rivela il tipo), e nome
        $tocMatch = [regex]::Match($html, 'id="toc-searchables"[^>]*>(.*?)</ul>', [System.Text.RegularExpressions.RegexOptions]::Singleline)
        if (-not $tocMatch.Success) {
            Write-Host "    TOC searchables non trovato!" -ForegroundColor Yellow
            return @()
        }
        
        $tocHtml = $tocMatch.Groups[1].Value
        
        # Pattern 1: moduli standard con icona snap/{type}/...
        # <li role=option data-id="52847">
        #   <a href="#section-N&amp;module-N" tabindex="0">
        #     <img src=".../snap/folder/..." alt="" />
        #     <span class="sr-only">Cartella</span>
        #     NomeModulo
        #   </a>
        # </li>
        $pattern1 = '<li[^>]*data-id="(\d+)"[^>]*>.*?<img[^>]*src="[^"]*snap/([a-z]+)(?:/|\?)[^"]*"[^>]*>.*?<span[^>]*class="sr-only"[^>]*>.*?</span>\s*([^<]*?)\s*</a>'
        $matches1 = [regex]::Matches($tocHtml, $pattern1, [System.Text.RegularExpressions.RegexOptions]::Singleline)
        
        # Pattern 2: risorse core con icona snap/core/.../f/{filetype}
        # <img src=".../snap/core/.../f/archive" ... />
        $pattern2 = '<li[^>]*data-id="(\d+)"[^>]*>.*?<img[^>]*src="[^"]*snap/core/[^"]*/f/(\w+)[^"]*"[^>]*>.*?<span[^>]*class="sr-only"[^>]*>.*?</span>\s*([^<]*?)\s*</a>'
        $matches2 = [regex]::Matches($tocHtml, $pattern2, [System.Text.RegularExpressions.RegexOptions]::Singleline)
        
        # Pattern 3: Google Meet (icona snap/googlemeet/...)
        $pattern3 = '<li[^>]*data-id="(\d+)"[^>]*>.*?<img[^>]*src="[^"]*snap/googlemeet[^"]*"[^>]*>.*?<span[^>]*class="sr-only"[^>]*>.*?</span>\s*([^<]*?)\s*</a>'
        $matches3 = [regex]::Matches($tocHtml, $pattern3, [System.Text.RegularExpressions.RegexOptions]::Singleline)
        
        # === PASSO 2: Mappa tipo modulo -> DlType + URL handler ===
        $seenIds = @{}  # evita duplicati
        
        # Pattern 3 prima (Google Meet)
        foreach ($m in $matches3) {
            $id = $m.Groups[1].Value
            $name = $m.Groups[2].Value.Trim()
            if (-not $seenIds.ContainsKey($id)) {
                $seenIds[$id] = $true
                $modules += @{
                    Id      = [int]$id
                    Name    = if ($name) { $name } else { "Meet $id" }
                    Type    = "googlemeet"
                    DlType  = "meet"
                    Url     = "https://fad.its-ictpiemonte.it/mod/url/view.php?id=$id"
                    Handler = "url"
                }
            }
        }
        
        # Pattern 2 (core resources: archive, spreadsheet, pdf, etc.)
        foreach ($m in $matches2) {
            $id = $m.Groups[1].Value
            $filetype = $m.Groups[2].Value.ToLower()
            $name = $m.Groups[3].Value.Trim()
            if (-not $seenIds.ContainsKey($id)) {
                $seenIds[$id] = $true
                $modules += @{
                    Id      = [int]$id
                    Name    = if ($name) { $name } else { "File $id" }
                    Type    = "file_$filetype"
                    DlType  = "resource"
                    Url     = "https://fad.its-ictpiemonte.it/mod/resource/view.php?id=$id"
                    Handler = "resource"
                }
            }
        }
        
        # Pattern 1 (standard mod types: url, folder, quiz, assign, resource, page, etc.)
        foreach ($m in $matches1) {
            $id = $m.Groups[1].Value
            $modType = $m.Groups[2].Value.ToLower()
            $name = $m.Groups[3].Value.Trim()
            
            if ($seenIds.ContainsKey($id)) { continue }
            $seenIds[$id] = $true
            
            # Determina DlType e URL handler dal tipo Moodle
            $dlType = "other"
            $handler = $modType
            
            switch ($modType) {
                "folder"   { $dlType = "folder" }
                "url"      { $dlType = "url" }
                "page"     { $dlType = "page" }
                "resource" { $dlType = "resource" }
                "file"     { $dlType = "resource" }
                "googlemeet" { $dlType = "meet" }
                "assign"   { $dlType = "other" }  # compiti interattivi
                "quiz"     { $dlType = "other" }  # quiz interattivi
                "forum"    { $dlType = "other" }  # forum
                "feedback" { $dlType = "other" }  # feedback
                "choice"   { $dlType = "other" }  # sondaggi
                "data"     { $dlType = "other" }  # database
                "glossary" { $dlType = "other" }  # glossario
                "workshop" { $dlType = "other" }  # workshop
                "scorm"    { $dlType = "resource" } # SCORM package
                "h5pactivity" { $dlType = "other" } # H5P interattivo
                "core"     { $dlType = "resource"; $handler = "resource" } # Snap core resources -> mod/resource
                default    { $dlType = "resource" } # default: prova come resource
            }
            
            # Se il nome contiene Google Meet, salta
            if ($name -match 'Google Meet|meet\.google|^\(\w+-\d+.*\)\s*(Fad|Meet)') {
                $dlType = "meet"
            }
            
            $modules += @{
                Id      = [int]$id
                Name    = if ($name) { $name } else { "Modulo $id" }
                Type    = $modType
                DlType  = $dlType
                Url     = "https://fad.its-ictpiemonte.it/mod/$handler/view.php?id=$id"
                Handler = $handler
            }
        }
        
        # === PASSO 3: Fallback riga per riga per moduli non catturati ===
        # Cerca ID nella TOC non ancora processati
        $allIds = [regex]::Matches($tocHtml, 'data-id="(\d+)"')
        foreach ($m in $allIds) {
            $id = $m.Groups[1].Value
            if (-not $seenIds.ContainsKey($id)) {
                $seenIds[$id] = $true
                $modules += @{
                    Id      = [int]$id
                    Name    = "Modulo $id"
                    Type    = "unknown"
                    DlType  = "resource"
                    Url     = "https://fad.its-ictpiemonte.it/mod/resource/view.php?id=$id"
                    Handler = "resource"
                }
                Write-Host "    [FALLBACK] Modulo $id tipo sconosciuto, tentativo resource" -ForegroundColor DarkYellow
            }
        }
        
        # Ordina per ID
        $modules = $modules | Sort-Object Id
        
        Write-Host "    Trovati $($modules.Count) moduli" -ForegroundColor Yellow
        
        $typeCounts = @{}
        foreach ($m in $modules) {
            $tc = if ($typeCounts.ContainsKey($m.DlType)) { $typeCounts[$m.DlType] + 1 } else { 1 }
            $typeCounts[$m.DlType] = $tc
        }
        $typeSummary = (($typeCounts.Keys | ForEach-Object { "$_=$($typeCounts[$_])" }) -join ', ')
        Write-Host "    Tipi: $typeSummary" -ForegroundColor DarkGray
        
        return $modules
    }
    catch {
        Write-Error "    Errore caricamento corso: $($_.Exception.Message)"
        return $null
    }
}

# === DOWNLOAD ===

function Get-FileExtension {
    param([string]$ContentType, [string]$Url)
    
    $ct = if ($ContentType) { $ContentType.ToLower() } else { "" }
    
    # Mappa Content-Type -> estensione
    if ($ct -match 'pdf') { return ".pdf" }
    elseif ($ct -match 'wordprocessingml\.document') { return ".docx" }
    elseif ($ct -match 'powerpoint|presentationml') { return ".pptx" }
    elseif ($ct -match 'excel|spreadsheetml') { return ".xlsx" }
    elseif ($ct -match 'zip') { return ".zip" }
    elseif ($ct -match 'image/jpeg') { return ".jpg" }
    elseif ($ct -match 'image/png') { return ".png" }
    elseif ($ct -match 'image') { $ext = $ct.Split('/')[1]; return ".$ext" }
    elseif ($ct -match 'video/mp4') { return ".mp4" }
    elseif ($ct -match 'text/html') { return ".html" }
    elseif ($ct -match 'octet-stream' -or $ct -eq '') {
        if ($Url -match '\.(\w+)(?:\?|$)') { return ".$($matches[1])" }
        return ".bin"
    }
    else {
        if ($Url -match '\.(\w+)(?:\?|$)') { return ".$($matches[1])" }
        return ".dat"
    }
}

function Get-CleanFileName {
    param([string]$Name)
    # Decodifica HTML
    $name = $Name -replace '&amp;', '&' -replace '&lt;', '<' -replace '&gt;', '>' -replace '&quot;', '"' -replace '&#39;', "'"
    # Rimuovi estensione se presente (la determineremo dal Content-Type)
    $name = $name -replace '\.(pptx|ppt|pdf|docx|doc|xlsx|xls|zip|mp4|png|jpg|jpeg|html?)$', ''
    # Rimuovi caratteri non validi per filesystem
    $name = $name -replace '[<>:"/\\|?*]', '_' -replace '\s+', ' ' -replace '\.\.\.', ''
    $name = $name.Trim()
    if ($name.Length -gt 100) { $name = $name.Substring(0, 100).Trim() }
    return $name
}

function Write-CacheEntry {
    param([string]$Key, [string]$Value)
    $script:ModuleCache[$Key] = $Value
    $script:CacheDirty = $true
}

function Read-CacheEntry {
    param([string]$Key)
    if ($script:ModuleCache.ContainsKey($Key)) { return $script:ModuleCache[$Key] }
    return $null
}

function Save-UrlShortcut {
    param([string]$Url, [string]$FilePath)
    $shortcut = "[InternetShortcut]`r`nURL=$Url`r`n"
    Set-Content -LiteralPath $FilePath -Value $shortcut -Encoding ascii
}

function Download-FolderModule {
    param($HttpClient, $FolderUrl, [string]$DestDir, [string]$BaseName)
    
    try {
        $response = $HttpClient.Client.GetAsync($FolderUrl).Result
        $finalUrl = $response.RequestMessage.RequestUri.ToString()
        
        # Controllo reale: la URL finale contiene /login/ (sessione scaduta)
        if ($finalUrl -match '/login/') {
            Write-Warning "      Sessione scaduta (folder)"
            return $false
        }
        
        $html = $response.Content.ReadAsStringAsync().Result
        
        # Estrai SOLO i file del corso dalla cartella (salta temi/icone)
        # Pattern: pluginfile.php/NNN/mod_folder/content/0/NomeFile
        $fileLinks = @()
        $fileMatches = [regex]::Matches($html, 'href="([^"]*pluginfile\.php/\d+/mod_folder/content/\d+/[^"]+)"', [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
        
        foreach ($m in $fileMatches) {
            $fileUrl = $m.Groups[1].Value
            
            # Gestisci URL protocollo-relativi (//...)
            if ($fileUrl -match '^//') { $fileUrl = "https:$fileUrl" }
            elseif ($fileUrl -notmatch '^https?://') { $fileUrl = "https://fad.its-ictpiemonte.it$fileUrl" }
            
            $cleanUrl = $fileUrl -replace '\?.*$', ''
            $fileName = [System.IO.Path]::GetFileName($cleanUrl)
            
            if ($fileName) {
                $fileLinks += @{ Url = $fileUrl; Name = $fileName }
            }
        }
        
        if ($fileLinks.Count -eq 0) {
            Write-Host "      -> Nessun file trovato nella cartella" -ForegroundColor Yellow
            return $false
        }
        
        $ok = 0
        $fi = 0
        foreach ($fl in $fileLinks) {
            $fi++
            $fileName = "$($BaseName)_$($fi.ToString('00'))_$($fl.Name)"
            $cleanName = $fileName -replace '[<>:"/\\|?*]', '_'
            $filePath = Join-Path -Path $DestDir -ChildPath $cleanName
            
            try {
                $fileResp = $HttpClient.Client.GetAsync($fl.Url).Result
                $fileBytes = $fileResp.Content.ReadAsByteArrayAsync().Result
                [System.IO.File]::WriteAllBytes($filePath, $fileBytes)
                Write-Host "        -> $cleanName ($($fileBytes.Length) bytes)" -ForegroundColor DarkGreen
                $ok++
            }
            catch {
                Write-Warning "        Errore file $($fl.Name): $_"
            }
        }
        
        Write-Host "      -> Cartella: $ok file scaricati" -ForegroundColor Green
        return $ok -gt 0
    }
    catch {
        Write-Warning "      Errore folder: $_"
        return $false
    }
}

function Download-Module {
    param($HttpClient, $Module, [string]$DestDir, [int]$Index)
    
    $name = Get-CleanFileName -Name $Module.Name
    $prefix = if ($Index) { "$($Index.ToString('00'))_" } else { "" }
    $displayName = "$prefix$name"
    if ($displayName.Length -gt 70) { $displayName = $displayName.Substring(0, 70) + "..." }
    
    Write-Host "    [$($Module.Id)] ($($Module.Type)) $displayName" -ForegroundColor Gray
    
    $modIdStr = "$($Module.Id)"
    
    # === GESTIONE PER TIPO ===
    switch ($Module.DlType) {
        "meet" {
            Write-Host "      -> Saltato (evento Google Meet)" -ForegroundColor DarkGray
            return $false
        }
        
        "other" {
            Write-Host "      -> Saltato (tipo $($Module.Type), non scaricabile)" -ForegroundColor DarkGray
            return $false
        }
        
        "folder" {
            # Controlla cache
            $cached = Read-CacheEntry -Key $modIdStr
            if ($cached) {
                Write-Host "      -> Già presente (cache)" -ForegroundColor DarkGray
                return $true
            }
            
            $url = $Module.Url
            if (-not $url) { $url = "https://fad.its-ictpiemonte.it/mod/folder/view.php?id=$modIdStr" }
            
            $result = Download-FolderModule -HttpClient $HttpClient -FolderUrl $url -DestDir $DestDir -BaseName "$prefix$name"
            if ($result) { Write-CacheEntry -Key $modIdStr -Value "$prefix$name (folder)" }
            return $result
        }
        
        "url" {
            $url = $Module.Url
            if (-not $url) { $url = "https://fad.its-ictpiemonte.it/mod/url/view.php?id=$modIdStr" }
            
            try {
                $resp = $HttpClient.Client.GetAsync($url).Result
                $finalUrl = $resp.RequestMessage.RequestUri.ToString()
                
                if ($finalUrl -match '/login/') { Write-Warning "      Sessione scaduta"; return $false }
                if ($finalUrl -eq $url -or $finalUrl -match 'mod/url/view') {
                    # Pagina intermedia URL: cerca il redirect
                    $html = $resp.Content.ReadAsStringAsync().Result
                    $redirMatch = [regex]::Match($html, 'url=([^"&\s]+)')
                    if ($redirMatch.Success) {
                        $finalUrl = [System.Uri]::UnescapeDataString($redirMatch.Groups[1].Value)
                    }
                }
                
                $urlFile = Join-Path -Path $DestDir -ChildPath "$name.url"
                Save-UrlShortcut -Url $finalUrl -FilePath $urlFile
                Write-Host "      -> $name.url -> $finalUrl" -ForegroundColor Cyan
                Write-CacheEntry -Key $modIdStr -Value "$name.url"
                return $true
            }
            catch {
                Write-Warning "      Errore URL: $_"
                return $false
            }
        }
        
        "page" {
            $url = $Module.Url
            if (-not $url) { $url = "https://fad.its-ictpiemonte.it/mod/page/view.php?id=$modIdStr" }
            
            try {
                $resp = $HttpClient.Client.GetAsync($url).Result
                $html = $resp.Content.ReadAsStringAsync().Result
                if ($html -match '/login/') { Write-Warning "      Sessione scaduta"; return $false }
                
                $htmlPath = Join-Path -Path $DestDir -ChildPath "$name.html"
                $html | Out-File -FilePath $htmlPath -Encoding utf8
                Write-Host "      -> $name.html (pagina Moodle)" -ForegroundColor Yellow
                Write-CacheEntry -Key $modIdStr -Value "$name.html"
                return $true
            }
            catch {
                Write-Warning "      Errore page: $_"
                return $false
            }
        }
        
        default {
            # === RESOURCE: download file ===
            # Controlla cache
            $cached = Read-CacheEntry -Key $modIdStr
            if ($cached) {
                $cachedFull = if ([System.IO.Path]::IsPathRooted($cached)) { $cached } else { Join-Path -Path $DestDir -ChildPath $cached }
                if (Test-Path -LiteralPath $cachedFull -PathType Leaf) {
                    Write-Host "      -> Già presente (cache)" -ForegroundColor DarkGray
                    return $true
                }
            }
            
            try {
                $url = $Module.Url
                if (-not $url) { $url = "https://fad.its-ictpiemonte.it/mod/resource/view.php?id=$modIdStr" }
                
                $response = $HttpClient.Client.GetAsync($url).Result
                $statusCode = [int]$response.StatusCode
                $finalUrl = $response.RequestMessage.RequestUri.ToString()
                
                if ($statusCode -ge 400) { Write-Warning "      Errore HTTP $statusCode"; return $false }
                if ($finalUrl -match '/login/') { Write-Warning "      Sessione scaduta"; return $false }
                
                # Se redirect diretto al file (pluginfile)
                if ($finalUrl -match 'pluginfile\.php') {
                    $ct = if ($response.Content.Headers.ContentType) { $response.Content.Headers.ContentType.MediaType } else { "" }
                    $bytes = $response.Content.ReadAsByteArrayAsync().Result
                    $ext = Get-FileExtension -ContentType $ct -Url $finalUrl
                    $filePath = Join-Path -Path $DestDir -ChildPath "$name$ext"
                    [System.IO.File]::WriteAllBytes($filePath, $bytes)
                    Write-Host "      -> $name$ext ($($bytes.Length) bytes)" -ForegroundColor Green
                    Write-CacheEntry -Key $modIdStr -Value "$name$ext"
                    return $true
                }
                
                # Se pagina HTML resource, cerca link pluginfile
                if ($finalUrl -match 'mod/resource/view') {
                    $html = $response.Content.ReadAsStringAsync().Result
                    
                    $dlMatch = [regex]::Match($html, 'href="([^"]*pluginfile\.php[^"]*)"')
                    if (-not $dlMatch.Success) {
                        $dlMatch = [regex]::Match($html, '"action":\s*"([^"]*pluginfile\.php[^"]*)"')
                    }
                    
                    if ($dlMatch.Success) {
                        $downloadUrl = $dlMatch.Groups[1].Value
                        if ($downloadUrl -notmatch '^https?://') { $downloadUrl = "https://fad.its-ictpiemonte.it$downloadUrl" }
                        
                        $fileResp = $HttpClient.Client.GetAsync($downloadUrl).Result
                        $fileFinalUrl = $fileResp.RequestMessage.RequestUri.ToString()
                        
                        $ct = if ($fileResp.Content.Headers.ContentType) { $fileResp.Content.Headers.ContentType.MediaType } else { "" }
                        
                        if ($ct -match 'text/html') {
                            $bodyText = $fileResp.Content.ReadAsStringAsync().Result
                            if ($bodyText -match 'login|Login') {
                                Write-Warning "      Redirect a login"
                                return $false
                            }
                        }
                        
                        $bytes = $fileResp.Content.ReadAsByteArrayAsync().Result
                        $ext = Get-FileExtension -ContentType $ct -Url $fileFinalUrl
                        $filePath = Join-Path -Path $DestDir -ChildPath "$name$ext"
                        [System.IO.File]::WriteAllBytes($filePath, $bytes)
                        Write-Host "      -> $name$ext ($($bytes.Length) bytes)" -ForegroundColor Green
                        Write-CacheEntry -Key $modIdStr -Value "$name$ext"
                        return $true
                    } else {
                        $htmlPath = Join-Path -Path $DestDir -ChildPath "$name.html"
                        $html | Out-File -FilePath $htmlPath -Encoding utf8
                        Write-Host "      -> HTML salvato (no file link)" -ForegroundColor Yellow
                        return $false
                    }
                }
                
                # Altri casi: salva come binary
                $ct = if ($response.Content.Headers.ContentType) { $response.Content.Headers.ContentType.MediaType } else { "" }
                if ($ct -match 'text/html') {
                    $html = $response.Content.ReadAsStringAsync().Result
                    $htmlPath = Join-Path -Path $DestDir -ChildPath "$name.html"
                    $html | Out-File -FilePath $htmlPath -Encoding utf8
                    Write-Host "      -> HTML salvato" -ForegroundColor Yellow
                    return $false
                }
                
                $bytes = $response.Content.ReadAsByteArrayAsync().Result
                $ext = Get-FileExtension -ContentType $ct -Url $finalUrl
                $filePath = Join-Path -Path $DestDir -ChildPath "$name$ext"
                [System.IO.File]::WriteAllBytes($filePath, $bytes)
                Write-Host "      -> $name$ext ($($bytes.Length) bytes)" -ForegroundColor Green
                Write-CacheEntry -Key $modIdStr -Value "$name$ext"
                return $true
            }
            catch {
                Write-Warning "      Errore modulo $($Module.Id): $_"
                return $false
            }
        }
    }
}

function Download-Course {
    param($HttpClient, $CourseConfig)
    
    $courseDir = Join-Path -Path $CourseConfig.BaseDir -ChildPath "$($CourseConfig.Dir)\01_Materiale"
    
    Write-Host "`n========================================" -ForegroundColor Magenta
    Write-Host "  $($CourseConfig.Name)" -ForegroundColor Magenta
    Write-Host "  ID: $($CourseConfig.Id) -> $courseDir" -ForegroundColor Magenta
    Write-Host "========================================" -ForegroundColor Magenta
    
    # Ottieni moduli
    $modules = Get-CourseModules -HttpClient $HttpClient -CourseId $CourseConfig.Id -CourseName $CourseConfig.Name
    if (-not $modules -or $modules.Count -eq 0) {
        Write-Host "  Nessun modulo trovato, salto." -ForegroundColor Yellow
        return
    }
    
    # Crea directory
    New-Item -ItemType Directory -Path $courseDir -Force | Out-Null
    
    # Nella directory 01_Materiale, vediamo se ci sono già file per capire se è già scaricato
    $existingFiles = @(Get-ChildItem -LiteralPath $courseDir -Filter "*" -ErrorAction SilentlyContinue)
    if ($existingFiles.Count -gt 2) {
        Write-Host "  01_Materiale ha già $($existingFiles.Count) file. Aggiungo nuovi moduli." -ForegroundColor DarkGray
    }
    
    $downloaded = 0
    $skipped = 0
    $index = 0
    
    foreach ($module in $modules) {
        $index++
        
        if ($module.DlType -eq "meet" -or $module.Name -match 'Fad \d+|meet\.google|Google Meet') {
            $skipped++
            continue
        }
        
        if (Download-Module -HttpClient $HttpClient -Module $module -DestDir $courseDir -Index $index) {
            $downloaded++
        }
    }
    
    Write-Host "  Fatto: $downloaded scaricati, $skipped saltati" -ForegroundColor Cyan
}

# === COURSE DISCOVERY ===

function Discover-Courses {
    param($HttpClient, $Config)
    
    Write-Host "[DISCOVER] Recupero corsi dalla FAD..." -ForegroundColor Cyan
    
    $response = $HttpClient.Client.GetAsync("https://fad.its-ictpiemonte.it/my/").Result
    $html = $response.Content.ReadAsStringAsync().Result
    
    if ($html -match 'notloggedin|Log in') {
        Write-Error "  Non autenticato"
        return
    }
    
    # Estrai tutti i corsi dalla dashboard
    $fadCourses = @{}
    $cardMatches = [regex]::Matches($html, 'data-courseid="(\d+)"[^>]*data-model="([^"]+)"', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    foreach ($m in $cardMatches) {
        $cid = $m.Groups[1].Value
        $jsonData = $m.Groups[2].Value -replace '&quot;', '"'
        try {
            $data = $jsonData | ConvertFrom-Json
            $fadCourses[$cid] = $data.fullname
        } catch {
            $fadCourses[$cid] = "Unknown"
        }
    }
    
    Write-Host "`nTrovati $($fadCourses.Count) corsi sulla FAD:`n" -ForegroundColor Green
    
    $configuredIds = @{}
    foreach ($c in $Config.courses) { $configuredIds[$c.id.ToString()] = $c }
    
    foreach ($cid in $fadCourses.Keys | Sort-Object) {
        $name = $fadCourses[$cid]
        if ($configuredIds.ContainsKey($cid)) {
            $cfg = $configuredIds[$cid]
            Write-Host "  [$cid] $name" -ForegroundColor Green
            Write-Host "         -> $($cfg.dir)\01_Materiale\" -ForegroundColor DarkGray
        } else {
            Write-Host "  [$cid] $name" -ForegroundColor Yellow
            Write-Host "         !! NON configurato in fad-courses.json" -ForegroundColor Red
        }
    }
}

# === MAIN ===

$config = Read-Config -Path $ConfigPath
$creds = Read-EnvFile -Path $EnvFile
$username = $creds['FAD_USERNAME']
$password = $creds['FAD_PASSWORD']

# Cache: evita richieste HTTP per moduli già scaricati
$CacheFile = Join-Path -Path $scriptDir -ChildPath "module_cache.json"
if (Test-Path -LiteralPath $CacheFile) {
    try {
        $raw = Get-Content -LiteralPath $CacheFile -Raw -ErrorAction Stop | ConvertFrom-Json -ErrorAction Stop
        $ModuleCache = ConvertTo-Hashtable -InputObject $raw
    } catch {
        Write-Host "  Cache danneggiata, ricreo..." -ForegroundColor DarkYellow
        $ModuleCache = @{}
    }
} else {
    $ModuleCache = @{}
}
$CacheDirty = $false

if (-not $username -or -not $password) {
    Write-Error "Credenziali mancanti in $EnvFile"
    exit 1
}

# Determina quali corsi scaricare
$targetCourses = @()

if ($CourseId -eq "list" -or $CourseId -eq "discover") {
    $http = New-HttpClient
    if (Invoke-FadLogin -HttpClient $http -Username $username -Password $password) {
        Discover-Courses -HttpClient $http -Config $config
    }
    exit 0
}
elseif ($CourseId -eq "all" -or $CourseId -eq "*") {
    Write-Host "============================================" -ForegroundColor Magenta
    Write-Host "  FAD Downloader - Modalità: TUTTI I CORSI" -ForegroundColor Magenta
    Write-Host "============================================" -ForegroundColor Magenta
    Write-Host ""

    # Filtra solo corsi con directory valida
    foreach ($c in $config.courses) {
        $fullDir = Join-Path -Path $config.baseDir -ChildPath $c.dir
        if (Test-Path -LiteralPath $fullDir) {
            $targetCourses += @{
                Id = [int]$c.id
                Name = $c.name
                Dir = $c.dir
                BaseDir = $config.baseDir
            }
        } else {
            Write-Host "[WARN] Directory non trovata: $fullDir - salto $($c.name)" -ForegroundColor DarkYellow
        }
    }
    Write-Host "Da scaricare: $($targetCourses.Count) corsi`n" -ForegroundColor Cyan
}
else {
    # Specific course ID(s)
    $ids = @($CourseId)
    foreach ($id in $ids) {
        $found = $false
        foreach ($c in $config.courses) {
            if ([int]$c.id -eq [int]$id) {
                $fullDir = Join-Path -Path $config.baseDir -ChildPath $c.dir
                if (-not (Test-Path -LiteralPath $fullDir)) {
                    Write-Error "Directory non trovata: $fullDir"
                    exit 1
                }
                $targetCourses += @{
                    Id = [int]$c.id
                    Name = $c.name
                    Dir = $c.dir
                    BaseDir = $config.baseDir
                }
                $found = $true
                break
            }
        }
        if (-not $found) {
            Write-Error "Corso ID $id non trovato in fad-courses.json"
            exit 1
        }
    }
}

if ($targetCourses.Count -eq 0) {
    Write-Host "Nessun corso da scaricare." -ForegroundColor Yellow
    exit 0
}

# Login una volta sola
$http = New-HttpClient
if (-not (Invoke-FadLogin -HttpClient $http -Username $username -Password $password)) {
    Write-Host "`nSuggerimenti:" -ForegroundColor Yellow
    Write-Host "  1. Verifica le credenziali in .env" -ForegroundColor Yellow
    Write-Host "  2. Prova ad accedere dal browser per sbloccare eventuali blocchi" -ForegroundColor Yellow
    exit 1
}

# Scarica ogni corso
$ok = 0
$fail = 0
foreach ($course in $targetCourses) {
    try {
        Download-Course -HttpClient $http -CourseConfig $course
        $ok++
    }
    catch {
        Write-Error "Errore durante download corso $($course.Name): $_"
        $fail++
    }
}

# Salva cache per la prossima esecuzione
if ($CacheDirty) {
    $ModuleCache | ConvertTo-Json | Out-File -FilePath $CacheFile -Encoding utf8
}

Write-Host "`n============================================" -ForegroundColor Magenta
Write-Host "  COMPLETATO!" -ForegroundColor Green
Write-Host "  Corsi completati: $ok / $($targetCourses.Count)" -ForegroundColor Cyan
if ($fail -gt 0) { Write-Host "  Corsi falliti: $fail" -ForegroundColor Red }
Write-Host "============================================" -ForegroundColor Magenta
