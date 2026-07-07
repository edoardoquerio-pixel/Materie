# Azure App Service — Guida all'ottimizzazione del codice

## Principi generali

| Principio | Perché su App Service |
|-----------|----------------------|
| **Stateless** | L'app può essere replicata su più istanze — lo stato locale non è condiviso |
| **Config via env** | App Settings = variabili d'ambiente in App Service, cambiabili senza rebuild |
| **Health endpoint** | Azure usa `/health` per verificare che l'istanza sia sana (load balancer + autoscale) |
| **Structured logging** | Log in JSON → Application Insights per diagnostica e monitoraggio |
| **Cold start** | App Service ferma le istanze inattive (solo Basic/Free) — minimizzare init time |

---

## Node.js / Express

### 1. Health endpoint (obbligatorio)

```js
// health.js — endpoint usato da Azure per probe
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});
```

### 2. Application Insights

```bash
npm install applicationinsights
```

```js
// app.js — all'inizio, PRIMA di express()
const appInsights = require('applicationinsights');
if (process.env.APPLICATIONINSIGHTS_CONNECTION_STRING) {
  appInsights.setup().start();
  const client = appInsights.defaultClient;
  // Traccia eventi custom
  client.trackEvent({ name: 'app-started', properties: { env: process.env.NODE_ENV } });
}
```

### 3. Config via ambiente (mai hardcoded)

```js
// config.js
module.exports = {
  port: process.env.PORT || 8080,                    // App Service inietta PORT
  dbConnection: process.env.DB_CONNECTION_STRING,
  redisUrl: process.env.REDIS_URL,
  environment: process.env.NODE_ENV || 'development',
  logLevel: process.env.LOG_LEVEL || 'info'
};
```

### 4. Gestione errori (middleware)

```js
// middleware/errorHandler.js
function errorHandler(err, req, res, next) {
  console.error(JSON.stringify({
    message: err.message,
    stack: process.env.NODE_ENV === 'development' ? err.stack : undefined,
    path: req.path,
    method: req.method
  }));
  res.status(err.status || 500).json({ error: 'Internal Server Error' });
}
```

### 5. package.json ottimizzato per App Service

```jsonc
{
  "name": "libreriaonline",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js",                    // App Service chiama npm start
    "build": "npm install --production"           // SCM_DO_BUILD_DURING_DEPLOYMENT=true
  },
  "main": "server.js",
  "engines": {
    "node": ">=20.0.0"
  }
}
```

---

## Python / FastAPI

### 1. Health endpoint

```python
# app/main.py
from fastapi import FastAPI
import time

app = FastAPI()
start_time = time.time()

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "uptime_seconds": time.time() - start_time
    }
```

### 2. Application Insights (OpenTelemetry)

```bash
pip install opentelemetry-api opentelemetry-sdk \
  opentelemetry-instrumentation-fastapi \
  opentelemetry-exporter-azure-monitor
```

```python
# app/telemetry.py
from opentelemetry import trace
from opentelemetry.exporter.azure_monitor import AzureMonitorTraceExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

def setup_telemetry(app: FastAPI, connection_string: str = None):
    if not connection_string:
        return
    exporter = AzureMonitorTraceExporter(connection_string=connection_string)
    provider = TracerProvider()
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    FastAPIInstrumentor.instrument_app(app)
```

### 3. startup.sh per App Service Linux

```bash
# startup.sh — App Service esegue questo all'avvio (app_command_line)
gunicorn --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --timeout 60 \
  --access-logfile - \
  app.main:app
```

```python
# startup.py (alternativa per Azure)
import uvicorn
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(environ.get("PORT", 8000)))
```

---

## C# / ASP.NET Core

### 1. Health checks

```bash
dotnet add package Microsoft.Extensions.Diagnostics.HealthChecks
```

```csharp
// Program.cs
builder.Services.AddHealthChecks();
app.MapHealthChecks("/health");
```

### 2. Application Insights

```bash
dotnet add package Microsoft.ApplicationInsights.AspNetCore
```

```csharp
// Program.cs
builder.Services.AddApplicationInsightsTelemetry(builder.Configuration["APPLICATIONINSIGHTS_CONNECTION_STRING"]);
```

---

## Deploy automation (PowerShell + Azure CLI)

```powershell
# deploy-appservice.ps1
param(
  [string]$ResourceGroup = "rg-prod-materie-api",
  [string]$WebAppName = "app-prod-materie-api",
  [string]$Slot = "staging",
  [string]$SourcePath = "."
)

# 1. Prepara pacchetto (skip node_modules)
Compress-Archive -Path "$SourcePath\*" -DestinationPath deploy.zip -Force `
  -ExcludePath "node_modules", ".git", ".terraform"

# 2. Deploy nello slot staging
az webapp deploy --resource-group $ResourceGroup --name $WebAppName `
  --src-path deploy.zip --type zip --slot $Slot

# 3. Swap con produzione
az webapp deployment slot swap --resource-group $ResourceGroup `
  --name $WebAppName --slot $Slot --target-slot production

Write-Host "✅ Deploy completato su $WebAppName (slot: $Slot → production)"
```

---

## Checklist verifica deploy

- [ ] Health endpoint `/health` risponde 200
- [ ] Application Insights connection string configurata (App Setting)
- [ ] `WEBSITE_RUN_FROM_PACKAGE=1` (deploy via zip, non FTP)
- [ ] `NODE_ENV=production` (disabilita stack trace e debug)
- [ ] Log strutturati (JSON) visibili in Log Analytics
- [ ] CORS configurato se frontend su dominio diverso
- [ ] HTTPS Only = true
- [ ] TLS minimo 1.2
- [ ] Auto-scale configurato (se SKU Standard+)
- [ ] Staging slot usato per deployment prima dello swap
