# Prometheus Adaptation Instructions

## Overview
After detecting the current model (via init instructions), Prometheus MUST adapt the following behaviors:

## Step 1: Load Adaptation Matrix
File: `C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\.omo\model-adaptation.json`

```powershell
# Carica la matrice JSON
$matrixPath = "C:\Users\edoardo.querio\OneDrive - ITS ICT Piemonte\Desktop\Materie\.omo\model-adaptation.json"
$matrix = Get-Content -Raw -LiteralPath $matrixPath | ConvertFrom-Json
```

## Step 2: Match Current Model to Profile
- Cercare il profilo corrispondente al modello corrente
- Se non trovato: usare profilo "default"
- Il profilo contiene 5 dimensioni

```powershell
# $model = modello rilevato dall'init (es. "opencode-go/deepseek-v4-flash")
$profile = $matrix.profiles.$model

if (-not $profile) {
    Write-Host "⚠️ Profilo non trovato per '$model' — uso profilo default"
    $profile = $matrix.profiles.default
}
```

### Struttura di un profilo
Ogni profilo nella matrice contiene 5 dimensioni:
```json
{
  "verbosity":      "normal",       // terse | normal | verbose
  "depth":          "normal",       // shallow | normal | deep
  "style":          "bilanciato",     // conciso | bilanciato | dettagliato
  "planLength":     "medium",       // short | medium | long
  "toolPreference": "balanced"      // balanced | creative | conservative
}
```

## Step 3: Apply Adaptation Parameters

### Verbosità
| Valore | Comportamento |
|--------|---------------|
| terse | Risposte brevi, solo risultati essenziali |
| normal | Risposte bilanciate, spiegazioni moderate (DEFAULT) |
| verbose | Risposte dettagliate, tutte le opzioni spiegate |

### Profondità ragionamento
| Valore | Comportamento |
|--------|---------------|
| shallow | 0-1 agenti esplorativi di default |
| normal | 2-3 agenti esplorativi di default (DEFAULT) |
| deep | 4+ agenti esplorativi, analisi multipla |

### Stile output
| Valore | Comportamento |
|--------|---------------|
| conciso | Bullet point, strutture minime |
| bilanciato | Misto bullet + paragrafi (DEFAULT) |
| dettagliato | Sezioni complete, markdown strutturato |

### Lunghezza plan
| Valore | Comportamento |
|--------|---------------|
| short | < 10 task per piano |
| medium | 10-25 task per piano (DEFAULT) |
| long | 25+ task per piano |

### Tool preference
| Valore | Comportamento |
|--------|---------------|
| balanced | Default: mix di strumenti |
| creative | Uso aumentato di websearch, app_searchGitHub |
| conservative | Solo strumenti core (read, write, bash, task) |

## Step 4: Output at Session Start

```powershell
Write-Host "📋 Modello rilevato: $model — Adattamento: verbosità=$($profile.verbosity), profondità=$($profile.depth), stile=$($profile.style)"
```

Esempio di output atteso:
```
📋 Modello rilevato: opencode-go/deepseek-v4-flash — Adattamento: verbosità=normal, profondità=normal, stile=bilanciato
```

## Step 5: Behavior Enforcement

Una volta applicati i parametri, Prometheus DEVE:

### Verbosità
- **terse**: Rispondere con massimo 3-5 frasi. Non spiegare scelte non richieste. Usare solo comandi essenziali.
- **normal**: Rispondere con massimo 1-2 paragrafi. Spiegare brevemente le scelte principali. (COMPORTAMENTO DEFAULT)
- **verbose**: Rispondere in modo esaustivo. Documentare ogni passaggio. Includere alternative quando rilevante.

### Profondità ragionamento
- **shallow**: Non lanciare agenti esplorativi se non esplicitamente richiesti. Decisioni rapide basate sulla conoscenza corrente.
- **normal**: Lanciare 1-2 agenti esplorativi per indagare lo stato attuale prima di pianificare. (COMPORTAMENTO DEFAULT)
- **deep**: Lanciare 3+ agenti esplorativi in parallelo. Esplorare architettura, dipendenze, edge case. Analisi multi-prospettiva.

### Stile output
- **conciso**: Struttura piatta. Usare liste bullet invece di paragrafi. Nessun preambolo o riepilogo.
- **bilanciato**: Alternare bullet e brevi paragrafi. Usare titoli di sezione solo per piani complessi. (COMPORTAMENTO DEFAULT)
- **dettagliato**: Usare markdown strutturato con ## sezioni, ### sottosezioni, tabelle, code block. Includere sommario, svolgimento e conclusione.

### Lunghezza plan
- **short**: Piani con 3-8 task atomic. Nessuna suddivisione fine.
- **medium**: Piani con 10-20 task. Suddivisione ragionevole per fase. (COMPORTAMENTO DEFAULT)
- **long**: Piani con 25-50 task. Suddivisione granulare, fase preparatoria dettagliata.

### Tool preference
- **balanced**: Usare strumenti in base alla necessità: read/grep per esplorazione, bash per esecuzione, task per delega.
- **creative**: Preferire webfetch/websearch/app_searchGitHub per raccogliere informazioni fresche. Usare esplorazione parallela aggressiva.
- **conservative**: Limitarsi a read/write/bash/task. Non usare webfetch, websearch, app_searchGitHub se non richiesto esplicitamente.

## Fallback / Edge Cases

| Scenario | Comportamento |
|----------|---------------|
| Matrice non trovata | Usare default: normal/normal/bilanciato/medium/balanced. Stampare: ⚠️ "Matrice non trovata — uso default" |
| Profilo modello non esistente | Usare profilo "default". Stampare: ⚠️ "Profilo non trovato per {model} — uso default" |
| Dimensione mancante nel profilo | Usare il valore DEFAULT per quella dimensione. Stampare: ⚠️ "Dimensione {dimensione} mancante — uso default" |
| Valore non valido in dimensione | Usare il valore DEFAULT per quella dimensione. Stampare: ⚠️ "Valore '{valore}' non valido per {dimensione} — uso default" |

### Valori DEFAULT per dimensione
| Dimensione | DEFAULT |
|------------|---------|
| verbosity | normal |
| depth | normal |
| style | bilanciato |
| planLength | medium |
| toolPreference | balanced |

## Dependencies
- **model-adaptation.json** → T2 (matrice già creata con 3 profili: deepseek-v4-flash, gpt-4o, default)
- **prometheus-init-instructions.md** → T7 (rilevamento modello all'avvio, completato ✅)
- Questo file **NON modifica** la matrice (solo lettura)
- Questo file **NON altera** la logica core di Prometheus/Atlas

## Changelog
- **2026-06-25** — Creazione file. 5 dimensioni di adattamento. Default per fallback. Istruzioni di enforcement per ogni dimensione.
