# Supermemory Model Pattern

## Recording (da `/setmodel` handler)

```javascript
// Quando l'utente esegue /setmodel <nome-modello>
supermemory(mode: "add", content: "model:opencode-go/deepseek-v4-flash", type: "preference", scope: "user")
```

**Dettagli:**
- `content` inizia sempre con `model:` per consentire search mirata
- `type: "preference"` — è una preferenza utente, non un progetto
- `scope: "user"` — vale cross-progetto (non legato a un workspace specifico)
- Il contenuto dopo `model:` è il nome esatto del modello passato a `/setmodel`
- Richiamare `add()` OGNI VOLTA che `/setmodel` viene eseguito (sovrascrittura per recency)

## Retrieval (da Prometheus init)

```javascript
// Quando Prometheus deve determinare quale modello usare
const result = supermemory(mode: "search", query: "model:", type: "preference")
const lastModel = result.results[0]?.content?.replace(/^model:/, "")
```

**Dettagli:**
- `query: "model:"` cerca solo entry con il prefisso dedicato
- `type: "preference"` filtra per preferenze utente
- Supermemory restituisce i risultati ordinati per recency (più recente primo)
- Prendere il PRIMO risultato `results[0]` — è l'ultimo modello registrato

## Fallback

Se Supermemory non ha risultati (nessun modello mai registrato):

```bash
# Legge il modello di default dalla configurazione di oh-my-openagent
jq -r '.agents.prometheus.model' "C:\Users\edoardo.querio\.config\opencode\oh-my-openagent.json"
```

**Strategia di fallback (pseudocodice):**

```
function getModel():
    result = supermemory.search("model:", "preference")
    if result.count > 0:
        return result.results[0].content.replace("model:", "")
    else:
        return readDefaultModelFromConfig()
```

## Deduplicazione

| Principio | Descrizione |
|---|---|
| **Prefisso `model:`** | Il contenuto inizia con `model:` per permettere search esatta con query `"model:"` |
| **Recency ordering** | Prendere SEMPRE `results[0]` (ultimo inserito = più recente) |
| **Sovrascrittura naturale** | `add()` non ha upsert; chiamarlo ogni volta crea una nuova entry. La search restituisce l'ultima. |
| **Nessuna delete** | Non serve cancellare le vecchie entry — il primo risultato è sempre il corrente |
| **Search tipizzata** | `type: "preference"` esclude rumore da altri tipi di memoria |

## Esempio di flusso completo

```
/setmodel gpt-4o
  └─ supermemory.add("model:gpt-4o", "preference", "user")

[successiva sessione] Prometheus init
  └─ supermemory.search("model:", "preference")
  └─ results[0] → "model:gpt-4o" → estrae "gpt-4o"
  └─ imposta modello corrente

/setmodel claude-sonnet-4
  └─ supermemory.add("model:claude-sonnet-4", "preference", "user")

[prossima sessione] Prometheus init
  └─ supermemory.search("model:", "preference")
  └─ results[0] → "model:claude-sonnet-4" ← il più recente
  └─ results[1] → "model:gpt-4o" ← storico, ignorato
```

## Verifica connessione

Test eseguito il 2026-06-25:

```json
// supermemory(mode: "profile")
{
  "success": true,
  "profile": {
    "static": ["Edoardo Querio (ITS ICT) is the author/owner of this C# coding-style profile."],
    "dynamic": ["Edoardo Querio C# coding style: ..."]
  }
}

// supermemory(mode: "search", query: "model:", type: "preference")
{
  "success": true,
  "query": "model:",
  "count": 5,
  "results": [...]  // nessuna entry con prefisso "model:" ancora presente
}
```
