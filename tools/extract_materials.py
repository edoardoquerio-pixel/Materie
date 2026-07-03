#!/usr/bin/env python3
"""Estrae testo da PDF, DOCX, PPTX e genera appunti strutturati in .md."""

import os, sys, re, json, glob
from pathlib import Path

# Root del workspace
ROOT = Path("C:/Users/edoardo.querio/OneDrive - ITS ICT Piemonte/Desktop/Materie")
OUT = ROOT / "tools" / "extracted_notes"

# Mappa nomi cartella -> nome materia
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
    "16_Linux_Server_e_Amministrazione": "16 - Linux Server",
    "17_Container_Docker_Kubernetes": "17 - Container Docker Kubernetes",
    "18_Microsoft_365_SharePoint": "18 - Microsoft 365 SharePoint",
    "19_Virtualizzazione": "19 - Virtualizzazione",
    "20_Data_Analytics_Visualization": "20 - Data Analytics e Visualization",
    "23_Project_Work_e_Laboratori": "23 - Project Work e Laboratori",
}

def extract_pdf(path):
    """Estrae testo da PDF usando pdfminer."""
    from pdfminer.high_level import extract_text
    try:
        text = extract_text(str(path))
        return clean_text(text)
    except Exception as e:
        return f"*Errore estrazione PDF: {e}*"

def extract_docx(path):
    """Estrae testo da DOCX."""
    from docx import Document
    try:
        doc = Document(str(path))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)
    except Exception as e:
        return f"*Errore estrazione DOCX: {e}*"

def extract_pptx(path):
    """Estrae testo da PPTX."""
    from pptx import Presentation
    try:
        prs = Presentation(str(path))
        slides = []
        for i, slide in enumerate(prs.slides, 1):
            texts = []
            for shape in slide.shapes:
                if hasattr(shape, "text") and shape.text.strip():
                    texts.append(shape.text.strip())
                if shape.has_table:
                    for row in shape.table.rows:
                        row_text = " | ".join(cell.text for cell in row.cells)
                        texts.append(row_text)
            if texts:
                slides.append(f"### Slide {i}\n\n" + "\n\n".join(texts))
        return "\n\n---\n\n".join(slides)
    except Exception as e:
        return f"*Errore estrazione PPTX: {e}*"

def clean_text(text):
    """Pulisce il testo estratto."""
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)  # unisci parole spezzate
    return text.strip()

def extract_file(path):
    """Estrae testo in base all'estensione."""
    ext = path.suffix.lower()
    if ext == '.pdf':
        return extract_pdf(path)
    elif ext in ('.docx', '.doc'):
        return extract_docx(path)
    elif ext in ('.pptx', '.ppt'):
        return extract_pptx(path)
    elif ext == '.md':
        return path.read_text(encoding='utf-8', errors='replace')
    elif ext == '.txt':
        return path.read_text(encoding='utf-8', errors='replace')
    elif ext == '.csv':
        return path.read_text(encoding='utf-8', errors='replace')
    elif ext == '.html':
        return path.read_text(encoding='utf-8', errors='replace')
    else:
        return None

def get_session_name(filename):
    """Tenta di determinare il nome della sessione/lezione dal filename."""
    name = filename.stem
    # Cerca pattern come "Lezione 1", "Modulo 1", numeri
    patterns = [
        (r'[Ll]ezione\s*(\d+)', 'Lezione {}'),
        (r'[Mm]odulo\s*(\d+)', 'Modulo {}'),
        (r'[Pp]arte\s*(\d+)', 'Parte {}'),
        (r'^(\d+)[)\s\.\-]', 'Lezione {}'),
        (r'[Ss]lide\s*[Cc]SP?\s*(\w+)', 'Lezione {}'),
        (r'^(\d+)\)', 'Sessione {}'),
    ]
    for pat, fmt in patterns:
        m = re.search(pat, name)
        if m:
            return fmt.format(m.group(1))
    return name

def get_session_order(filename):
    """Tenta di estrarre un numero d'ordine dal filename."""
    name = filename.stem
    patterns = [
        r'(\d+)',
    ]
    for pat in patterns:
        m = re.search(pat, name)
        if m:
            return int(m.group(1))
    return 999

def process_subject(subject_dir):
    """Processa una materia: estrae tutti i file e genera appunti."""
    folder_name = subject_dir.name
    if folder_name not in SUBJECT_NAMES:
        print(f"  SKIP: {folder_name} - non in mappa")
        return

    subject_name = SUBJECT_NAMES[folder_name]
    material_dir = subject_dir / "01_Materiale"

    if not material_dir.exists():
        print(f"  SKIP: {folder_name} - 01_Materiale non esiste")
        return

    files = sorted(material_dir.iterdir(), key=lambda p: (p.suffix.lower(), p.name))
    
    out_dir = OUT / folder_name
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n=== {subject_name} ===")
    
    all_sessions = []

    for f in files:
        if f.is_dir():
            continue
        
        ext = f.suffix.lower()
        if ext in ('.url', '.bak', '.pkt', '.zip', '.xlsx', '.xls', '.exe', '.msi', '.7z', '.rar') or ext in ('.exe', '.msi', '.dll'):
            continue

        if f.stat().st_size == 0:
            continue

        print(f"  -> {f.name}")
        text = extract_file(f)
        if text is None or not text.strip():
            continue

        session_name = get_session_name(f)
        order = get_session_order(f)

        # Crea file markdown pulito
        clean = f"# {session_name}\n\nFonte: `{f.name}`\n\n{text}"
        safe_name = re.sub(r'[^\w\-]+', '_', f.stem)[:80]
        out_file = out_dir / f"{order:03d}_{safe_name}.md"
        
        # Evita file troppo lunghi (sopra 50KB) in singolo file
        if len(clean) > 50000:
            clean = clean[:50000] + f"\n\n*[Estratto troncato a 50KB — file originale: {f.name}]*"

        out_file.write_text(clean, encoding='utf-8')
        all_sessions.append((order, session_name, out_file.name))

    # Genera indice delle sessioni
    if all_sessions:
        all_sessions.sort()
        index_lines = [f"# {subject_name} — Appunti per Sessione\n",
                       f"\nMateriali estratti da `01_Materiale/`.\n\n## Indice Sessioni\n"]
        for order, name, fname in all_sessions:
            index_lines.append(f"- [{name}]({fname})")
        
        (out_dir / "README.md").write_text('\n'.join(index_lines), encoding='utf-8')
        print(f"  -> {len(all_sessions)} sessioni estratte")

if __name__ == "__main__":
    for folder in sorted(ROOT.iterdir()):
        if folder.is_dir() and re.match(r'^\d{2}_', folder.name):
            process_subject(folder)
    print("\n=== Completato ===")
