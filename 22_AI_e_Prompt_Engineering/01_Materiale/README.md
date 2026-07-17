# Materiali Didattici — Materia 22_AI_e_Prompt_Engineering

## Contenuti

### Fondamenti AI/ML
- Fondamenti AI/ML — Panoramica (from notion)
- Configurazione dell'ambiente (open-source nel repo)

### Architettura Transformer e LLM
- Diagramma dell'architettura Transformer (PDF)
- Confronto LLM (Markdown)
- Nozioni sui parametri di training (notion)

### Prompt Engineering
- Schema 1-Shot/Few-Shot (Markdown)
- Notas delle tecniche CoT/ToT (notion)
- Esempi di sviluppo di Prompt (Markdown)

### AI nel Cloud e IA-as-a-Service
- Tabelle di confronto delle opzioni AIaaS (Markdown)
- Configurazione degli esempi RAG (notion)

### Etica, Best Practices e AI Act
- Gestione delle best practices di sicurezza dei dati di training (Markdown)
- Codice AI Act EU (notion)

## Risorse Utili nel Repository di Classe

- **tools/notion_notes/22_AI_e_Prompt_Engineering.md** — Panoramica completa del syllabus e indice proposto (vedi nel diff del PR il contenuto completo)

## Note di Instaurazione per studenti

1. **Potenzialmente git submodule necessario**
2. **Controllo delle dipendenze**
3. **Installazione di Git LFS per file pesanti (poiché presenti in alcuni esempi di materiali)

## Struttura per Utenti (Confronto tra materie)

In altre materie (ad es. 12_RESTful_API, 20_Data_Analytics_Visualization) la cartella 01_Materiale/ contiene
PDF → PPT → Spiegazioni di codice → Risorse per l insegnante.

Questa materia è la prima ad iniziare a popolare le risorse in modo completo, su suggerimento del professore.

## Impostazioni per lo sviluppo e-testing

Questo materiale è concepito principalmente per insegnamento in aula (integrazione nell'insegnamento tradizionale dell'ITS ICT in aula + laboratorio cloud). La fase di testing può essere eseguita con strumenti standard come:

- **dotenv + Python** per le API esterne tramite .env
- **Node + Express** per deployment basati su RAG tramite
- **GitHub CI/CD**, automatizzando anche report di test tramite **GitHub Actions**
- **Istanti cloud-only per live:** GCP AIML, AWS Bedrock, Azure OpenAI (gli studenti prepareranno percorsi in base alle sue unità)

## Tag Mylearn

- prompt engineering
- chain-of-thought
- few-shot
- transformer
- retrieval augmented generation