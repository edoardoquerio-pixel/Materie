#!/usr/bin/env python3
"""Generate Notion blocks from markdown notes."""
import json, os, re
from pathlib import Path

ROOT = Path("C:/Users/edoardo.querio/OneDrive - ITS ICT Piemonte/Desktop/Materie/tools/notion_notes")
OUT = Path("C:/Users/edoardo.querio/OneDrive - ITS ICT Piemonte/Desktop/Materie/tools/notion_blocks")

OUT.mkdir(exist_ok=True)

def md_to_blocks(text):
    blocks = []
    in_code = False
    code_lines = []
    
    for line in text.split('\n'):
        # Code block toggle
        if line.strip().startswith('```'):
            if in_code:
                # End code block
                code_text = '\n'.join(code_lines)
                if code_text.strip():
                    # Use paragraph for code content
                    for codeline in code_lines:
                        if codeline.strip():
                            blocks.append({
                                "content_block": {
                                    "content": codeline,
                                    "block_property": "paragraph"
                                }
                            })
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        
        if in_code:
            code_lines.append(line)
            continue
        
        line = line.rstrip()
        if not line:
            continue
        
        # Headings
        if line.startswith('## '):
            blocks.append({'content_block': {'content': line[3:], 'block_property': 'heading_2'}})
        elif line.startswith('### '):
            blocks.append({'content_block': {'content': line[4:], 'block_property': 'heading_3'}})
        # Horizontal rule
        elif line == '---' or line == '___':
            blocks.append({'content_block': {'block_property': 'divider'}})
        # Bullet list
        elif line.startswith('- '):
            blocks.append({'content_block': {'content': line[2:], 'block_property': 'bulleted_list_item'}})
        # Numbered list
        elif re.match(r'^\d+[\.\)] ', line):
            content = re.sub(r'^\d+[\.\)] ', '', line)
            blocks.append({'content_block': {'content': content, 'block_property': 'numbered_list_item'}})
        # Other
        elif line.strip():
            # Check if it's bold text or has special formatting
            content = line.strip()
            blocks.append({'content_block': {'content': content, 'block_property': 'paragraph'}})
    
    return blocks

# Process all files
files_processed = []
for f in sorted(ROOT.glob("*.md")):
    if f.name == "README.md":
        continue
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    blocks = md_to_blocks(content)
    
    # Save individual file
    out_name = f.stem + '.json'
    with open(OUT / out_name, 'w', encoding='utf-8') as fh:
        json.dump(blocks, fh, ensure_ascii=False, indent=2)
    
    files_processed.append({
        'name': f.stem,
        'blocks': len(blocks),
        'chunks': (len(blocks) + 99) // 100  # how many API calls needed
    })
    print(f"{f.name}: {len(blocks)} blocks -> {files_processed[-1]['chunks']} call(s)")

# Save summary
with open(OUT / '_summary.json', 'w', encoding='utf-8') as fh:
    json.dump(files_processed, fh, ensure_ascii=False, indent=2)

total_blocks = sum(f['blocks'] for f in files_processed)
total_calls = sum(f['chunks'] for f in files_processed)
print(f"\nTotal: {len(files_processed)} files, {total_blocks} blocks, ~{total_calls} API calls")
