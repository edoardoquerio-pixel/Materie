# 22_AI_e_Prompt_Engineering

## 📋 Panoramica

Intelligenza Artificiale e Prompt Engineering. Copre i fondamenti dell'AI, machine learning, deep learning, modelli linguistici (LLM), tecniche di prompt engineering e applicazioni pratiche nell'ecosistema cloud e DevOps.

> ⚠️ **Nessun materiale didattico presente** in `01_Materiale/`. Questa nota è un placeholder da integrare.

## 📚 Indice degli argomenti (attesi dal syllabus)

### 1. Fondamenti di AI/ML
- AI, Machine Learning, Deep Learning — differenze e relazioni
- Apprendimento supervisionato, non supervisionato, per rinforzo
- Bias, varianza, overfitting, underfitting

### 2. Modelli Linguistici (LLM)
- Architettura Transformer (Self-attention, Multi-head attention)
- GPT, Claude, Gemini, Llama — confronto e contesto
- Training: pre-training, fine-tuning, RLHF
- API e integrazione (OpenAI API, Claude API, Google AI)

### 3. Prompt Engineering
- **Zero-shot**, **Few-shot**, **Chain-of-Thought (CoT)**
- **System prompt**, **User prompt**, **Assistant role**
- Struttura prompt: contesto, task, formato, esempi
- **Tecniche avanzate**: Tree-of-Thought, ReAct, Self-Consistency
- Temperature, top-p, max_tokens — parametri di generazione

### 4. AI nel Cloud
- **AI-as-a-Service**: OpenAI, Anthropic, Google Vertex AI, AWS Bedrock, Azure OpenAI
- **RAG (Retrieval-Augmented Generation)**: Embedding, vector database (Pinecone, Weaviate, Chroma)
- **AI Agents**: Tool use, function calling, multi-agent systems

### 5. Etica e Best Practices
- Bias nei modelli, allucinazioni, safety guardrails
- Privacy dei dati (non inviare dati sensibili a API esterne)
- AI Act EU — regolamentazione

## ⚡ Punti Chiave

- **Prompt engineering** è la competenza chiave: un buon prompt definisce ruolo, contesto, task e formato
- **Chain-of-Thought** migliora significativamente il ragionamento in task complessi
- **RAG** combina LLM con knowledge base esterna per risposte aggiornate e contestuali
- Parametri critici: **Temperature** (0=deterministico, 0.7=creativo), **Top-p** (nucleus sampling)
- Le **allucinazioni** sono il problema principale — validare sempre output critici
- **Nessun LLM** va usato per decisioni su dati sensibili senza supervisione umana

## 📎 Risorse Collegate

- **02_Esercizi/**: —
- **03_Progetti/**: —
- **Materie collegate**: `10_Programmazione_Python`, `20_Data_Analytics_Visualization`, `12_RESTful_API`
