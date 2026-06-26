# Prometheus Init: Model Detection

## All'inizio di ogni sessione, Esegui QUESTA sequenza:

### Step 1: Cerca modello in Supermemory
```javascript
// Cerca in Supermemory preferenze con "model:" prefix
const smResult = supermemory(mode: "search", query: "model:", type: "preference")

// Filtra SOLO risultati che iniziano con "model:" (la search è semantica,
// può tornare risultati non correlati al modello)
const modelEntry = smResult.results?.find(r => 
  r.content?.startsWith("model:")
)
const smModel = modelEntry?.content?.replace(/^model:/, "").trim()
```

### Step 2: Leggi modello da config file
```bash
# Leggi da oh-my-openagent.json — modello assegnato a Prometheus
jq -r '.agents.prometheus.model' "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json"
```

Se Powershell (senza jq):
```powershell
$config = Get-Content -Raw -LiteralPath "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json" | ConvertFrom-Json
$configModel = $config.agents.prometheus.model
```

### Step 3: Confronta e decidi
```
SE smModel è definito E non vuoto:
    usa smModel come "ultimo modello noto da Supermemory"
ALTRIMENTI:
    usa $configModel come fallback (valore corrente di configurazione)

SE smModel ESISTE E $configModel ESISTE:
    SE smModel == $configModel:
        ✅ "Modello rilevato: {smModel} (fonte: Supermemory)"
    ALTRIMENTI:
        ⚠️ "Attenzione: Supermemory ha '{smModel}' ma config ha '{configModel}'. Usa /setmodel per sincronizzare."
ALTRIMENTI SE solo smModel:
    ✅ "Modello rilevato: {smModel} (fonte: Supermemory)"
ALTRIMENTI:
    ℹ️ "Modello attivo: {configModel} (fonte: oh-my-openagent.json)"
```

### Timeout e resilienza
```
- Timeout Supermemory: 1500ms (1.5 secondi)
- Se Supermemory non risponde entro 1500ms:
    salta Step 1, vai direttamente a Step 2
    usa solo config file
    stampa: "ℹ️ Supermemory non disponibile, modello da configurazione"
- Init totale deve richiedere < 2 secondi
- Non crashare se Supermemory o config file non sono accessibili
- Non mostrare stack trace all'utente
```

### Esempio output

**Caso normale (match):**
```
📋 Modello rilevato: opencode-go/deepseek-v4-flash (fonte: Supermemory)
```

**Caso mismatch:**
```
⚠️ Attenzione: Supermemory ha 'opencode-go/deepseek-v4-flash' ma config ha 'opencode/deepseek-v4-flash-free'. Usa /setmodel per sincronizzare.
```

**Caso solo config (Supermemory timeout/empty):**
```
ℹ️ Modello attivo: opencode-go/deepseek-v4-flash (fonte: oh-my-openagent.json)
```

### Verifica iniziale rapida
```
1. Supermemory search("model:", "preference")
   └── risposta in < 1500ms → estrai primo risultato con prefisso "model:"
   └── timeout → skip
2. Leggi agents.prometheus.model da oh-my-openagent.json
3. Confronta i due valori
4. Stampa messaggio all'utente
```

### Note tecniche
- Il pattern `model:` in Supermemory è salvato con `scope: "user"` e `type: "preference"`
- Il comando `/setmodel` aggiorna ENTRAMBE le fonti (config + Supermemory)
- In caso di disaccordo, Supermemory è considerato più recente (l'utente potrebbe aver cambiato modello in una sessione precedente senza aggiornare il config)
