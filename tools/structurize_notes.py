#!/usr/bin/env python3
"""Legge i file estratti e genera appunti strutturati per sessione."""

import os, re, sys
from pathlib import Path

ROOT = Path("C:/Users/edoardo.querio/OneDrive - ITS ICT Piemonte/Desktop/Materie")
EXTRACTED = ROOT / "tools" / "extracted_notes"
OUT = ROOT / "tools" / "structured_notes"

SUBJECT_NAMES = {
    "00_Amministrazione_Corso": "00 - Amministrazione del Corso",
    "01_Inglese_Tecnico": "01 - Inglese Tecnico",
    "02_Orientamento_e_Soft_Skills": "02 - Orientamento e Soft Skills",
    "03_Parita_e_Non_Discriminazione": "03 - Parità e Non Discriminazione",
    "04_Sicurezza_sul_Lavoro": "04 - Sicurezza sul Lavoro",
    "06_Reti_e_Sicurezza_Informatica": "06 - Reti e Sicurezza Informatica",
    "07_Version_Control_Git": "07 - Version Control Git",
    "08_Basi_di_Dati_SQL_NoSQL": "08 - Basi di Dati SQL/NoSQL",
    "09_Programmazione_C_CPP": "09 - Programmazione C/C++",
    "11_Programmazione_DotNet_CSharp": "11 - Programmazione .NET C#",
    "12_RESTful_API": "12 - RESTful API",
    "14_Cloud_Azure": "14 - Cloud Azure",
    "16_Linux_Server_e_Amministrazione": "16 - Linux Server e Amministrazione",
    "17_Container_Docker_Kubernetes": "17 - Container Docker Kubernetes",
    "18_Microsoft_365_SharePoint": "18 - Microsoft 365 SharePoint",
    "19_Virtualizzazione": "19 - Virtualizzazione",
    "20_Data_Analytics_Visualization": "20 - Data Analytics e Visualization",
    "23_Project_Work_e_Laboratori": "23 - Project Work e Laboratori",
}

# Filtri per estrarre sezioni significative
SECTION_PATTERNS = [
    (r'abstract|sommario|riassunto|obiettivi', 'Obiettivi'),
    (r'introduzion', 'Introduzione'),
    (r'concetti chiave|key concepts|terminologia', 'Concetti Chiave'),
    (r'esempi|example', 'Esempi'),
    (r'eserciz', 'Esercizi'),
    (r'comandi|command|istruzion', 'Comandi'),
    (r'configurazion|configuration', 'Configurazione'),
    (r'conclusion|riepilogo|summary', 'Riepilogo'),
]

def find_source(subject_folder, filename):
    """Trova un file sorgente approssimativamente."""
    stem = re.sub(r'^\d+_', '', Path(filename).stem)
    return stem

def summarize_text(text, max_lines=80):
    """Condensa un testo lungo in paragrafi significativi."""
    lines = text.split('\n')
    # Rimuovi linee troppo corte o boilerplate
    meaningful = []
    for line in lines:
        line = line.strip()
        if len(line) < 15 and not line.startswith('#'):
            continue
        if re.match(r'^[\s\*\-_\.]+$', line):
            continue
        meaningful.append(line)
    
    # Se troppo lungo, prendi prime linee significative
    if len(meaningful) > max_lines:
        meaningful = meaningful[:max_lines]
        meaningful.append("\n*[Contenuto troncato — vedi file originale per dettagli completi]*")
    
    return '\n'.join(meaningful)

def detect_topics(text):
    """Identifica i topic principali dal testo."""
    lines = text.lower().split('\n')
    topics = []
    keywords = {
        'installazione': 'Installazione',
        'configurazione': 'Configurazione', 
        'sicurezza': 'Sicurezza',
        'crittografia': 'Crittografia',
        'rete': 'Reti',
        'database': 'Database',
        'programmazione': 'Programmazione',
        'cloud': 'Cloud',
        'docker': 'Docker',
        'kubernetes': 'Kubernetes',
        'linux': 'Linux',
        'git': 'Git',
        'rest': 'API REST',
        'azure': 'Azure',
        'aws': 'AWS',
        'gcp': 'GCP',
        'virtualizzazione': 'Virtualizzazione',
        'data': 'Data Analytics',
        'inglese': 'Inglese',
        'colloquio': 'Colloquio',
        'curriculum': 'Curriculum',
    }
    found = set()
    for line in lines:
        for kw, topic in keywords.items():
            if kw in line and topic not in found:
                found.add(topic)
                topics.append(topic)
    return topics[:5]

def create_structured_note(source_path, session_title, content):
    """Crea una nota strutturata ben formattata."""
    text = content
    # Rimuovi l'intestazione già presente
    text = re.sub(r'^# .+\n+', '', text)
    text = re.sub(r'^Fonte: .+\n+', '', text)
    
    summary = summarize_text(text)
    topics = detect_topics(text) or ['Generale']
    
    # Estrai prime righe come descrizione
    first_lines = [l.strip() for l in text.split('\n') if l.strip() and len(l.strip()) > 30]
    desc = first_lines[0][:200] if first_lines else 'N/A'
    
    note = f"""# {session_title}

## Panoramica
{desc}

## Argomenti trattati
{', '.join(topics)}

---
## Appunti

{summary}

---
*Fonte: {source_path.name}*
"""
    return note

def process_subject(subject_folder):
    """Processa una materia e genera appunti."""
    folder_name = subject_folder.name
    if folder_name not in SUBJECT_NAMES:
        return
    
    subject_name = SUBJECT_NAMES[folder_name]
    files = sorted(subject_folder.glob("*.md"))
    
    if not files:
        return
    
    print(f"\n=== {subject_name} ===")
    
    out_dir = OUT / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)
    
    all_notes = []
    
    for f in files:
        if f.name == "README.md":
            continue
        
        content = f.read_text(encoding='utf-8', errors='replace')
        
        # Estrai titolo sessione
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        session_title = title_match.group(1).strip() if title_match else f.stem
        
        # Pulisci il nome sessione
        clean_title = re.sub(r'^\d+_', '', session_title)
        clean_title = clean_title.replace('_', ' ').strip()
        
        print(f"  -> {clean_title}")
        
        note = create_structured_note(f, clean_title, content)
        all_notes.append((f.stat().st_mtime, clean_title, note))
    
    # Genera indice materie ordinato per data
    all_notes.sort(key=lambda x: x[0])
    
    index_items = []
    combined_parts = [f"# {subject_name} — Tutte le Sessioni\n"]
    
    for i, (mtime, title, note) in enumerate(all_notes, 1):
        safe_name = re.sub(r'[^\w\s\-]', '', title).strip()[:50]
        safe_filename = f"{i:02d}_{re.sub(r'\s+', '_', safe_name)}.md"
        out_file = out_dir / safe_filename
        out_file.write_text(note, encoding='utf-8')
        
        index_items.append(f"- [{title}]({safe_filename})")
        
        # Aggiungi alla nota combinata
        combined_parts.append(f"\n---\n\n## Sessione {i}: {title}\n\n")
        # Estrai solo il corpo dalla nota
        body = re.sub(r'^# .+\n+## Panoramica\n.+\n+## Argomenti trattati\n.+\n+---\n+## Appunti\n+', '', note)
        body = re.sub(r'\n+---\n+\*Fonte:.*\*$', '', body)
        combined_parts.append(body.strip())
    
    # Indice
    index = f"# {subject_name} — Indice Sessioni\n\n"
    index += "Sessioni:\n" + '\n'.join(index_items)
    index += f"\n\nTotale: {len(all_notes)} sessioni"
    (out_dir / "README.md").write_text(index, encoding='utf-8')
    
    # Nota combinata
    combined_parts.append(f"\n\n---\n*Totale: {len(all_notes)} sessioni generate il "
                          f"{__import__('datetime').datetime.now().strftime('%d/%m/%Y')}*")
    (out_dir / "TUTTE_LE_SESSIONI.md").write_text('\n'.join(combined_parts), encoding='utf-8')
    
    print(f"  -> {len(all_notes)} note strutturate create")

if __name__ == "__main__":
    for folder in sorted(EXTRACTED.iterdir()):
        if folder.is_dir():
            process_subject(folder)
    print("\n=== Completato ===")
