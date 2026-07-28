#!/usr/bin/env python3
"""
Convert markdown to a styled HTML, then save as HTML that can be opened
in a browser and printed to PDF (Ctrl+P -> Save as PDF).
"""
import re
import sys
from pathlib import Path


def md_to_html(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove emoji characters that don't render well in print
    emoji_pattern = re.compile(
        "[\U0001F000-\U0001F9FF"
        "\U00002702-\U000027B0"
        "\U0000FE00-\U0000FE0F"
        "\U0001F000-\U0001FAFF"
        "\U0000200D"
        "\U00002600-\U000026FF"
        "\U00002B50"
        "\U0000231A-\U0000231B"
        "\U00002328"
        "\U000023CF"
        "\U000023E9-\U000023F3"
        "\U000023F8-\U000023FA"
        "\U0000FE0F"
        "]+", flags=re.UNICODE
    )

    lines = content.split('\n')
    html_parts = []
    in_code_block = False
    code_lines = []
    code_lang = ''
    in_table = False
    table_rows = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Code block
        if stripped.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_lang = stripped[3:].strip()
                code_lines = []
            else:
                in_code_block = False
                code = '\n'.join(code_lines)
                code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                html_parts.append(
                    f'<pre class="code-block"><code>{code}</code></pre>'
                )
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        # Close table if we hit a non-table line
        if in_table and not (stripped.startswith('|') and stripped.endswith('|')):
            in_table = False
            html_parts.append(render_table(table_rows))
            table_rows = []

        # Headers
        if stripped.startswith('# ') and not stripped.startswith('## '):
            text = format_inline(emoji_pattern.sub('', stripped[2:]))
            html_parts.append(f'<h1 class="doc-title">{text}</h1>')
        elif stripped.startswith('## '):
            text = format_inline(emoji_pattern.sub('', stripped[3:]))
            html_parts.append(f'<h2 class="section-title">{text}</h2>')
        elif stripped.startswith('### '):
            text = format_inline(emoji_pattern.sub('', stripped[4:]))
            html_parts.append(f'<h3 class="subsection-title">{text}</h3>')
        elif stripped.startswith('#### '):
            text = format_inline(emoji_pattern.sub('', stripped[5:]))
            html_parts.append(f'<h4>{text}</h4>')
        # Table
        elif stripped.startswith('|') and stripped.endswith('|'):
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                continue  # separator row
            cells = [format_inline(emoji_pattern.sub('', c.strip()))
                     for c in stripped[1:-1].split('|')]
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
        # Blockquote
        elif stripped.startswith('> '):
            text = format_inline(emoji_pattern.sub('', stripped[2:]))
            html_parts.append(f'<blockquote class="doc-blockquote">{text}</blockquote>')
        # Horizontal rule
        elif stripped in ('---', '***', '___'):
            html_parts.append('<hr class="doc-hr">')
        # List items
        elif re.match(r'^\s*[-*+]\s+', stripped):
            match = re.match(r'^(\s*)[-*+]\s+(.*)', line)
            if match:
                indent = len(match.group(1))
                text = format_inline(emoji_pattern.sub('', match.group(2)))
                level = indent // 2
                padding = level * 20
                html_parts.append(
                    f'<div class="list-item" style="padding-left:{padding}px">'
                    f'<span class="bullet">&bull;</span> {text}</div>'
                )
        # Numbered list
        elif re.match(r'^\s*\d+\.\s+', stripped):
            match = re.match(r'^(\s*)\d+\.\s+(.*)', line)
            if match:
                indent = len(match.group(1))
                text = format_inline(emoji_pattern.sub('', match.group(2)))
                level = indent // 2
                padding = level * 20
                html_parts.append(
                    f'<div class="list-item" style="padding-left:{padding}px">'
                    f'<span class="bullet">1.</span> {text}</div>'
                )
        # Empty line
        elif stripped == '':
            pass  # skip empty lines for cleaner output
        # Paragraph
        else:
            text = format_inline(emoji_pattern.sub('', stripped))
            if text.strip():
                html_parts.append(f'<p class="doc-para">{text}</p>')

    # Close any remaining table
    if in_table and table_rows:
        html_parts.append(render_table(table_rows))

    body = '\n'.join(html_parts)

    return f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Schema Infrastruttura Full Cloud Azure - TP Group</title>
<style>
@page {{
    size: A4;
    margin: 18mm 15mm 20mm 15mm;
}}
* {{
    box-sizing: border-box;
}}
body {{
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.5;
    color: #1a1a2e;
    max-width: 210mm;
    margin: 0 auto;
    padding: 10mm 5mm;
    background: white;
}}
/* Cover / Title */
.doc-title {{
    font-size: 22pt;
    font-weight: 700;
    color: #0d2b5e;
    border-bottom: 3px solid #1a56db;
    padding-bottom: 8px;
    margin-top: 0;
    margin-bottom: 16px;
    page-break-after: avoid;
}}
/* Section headers */
.section-title {{
    font-size: 14pt;
    font-weight: 700;
    color: #1a365d;
    border-bottom: 2px solid #cbd5e0;
    padding-bottom: 5px;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
}}
.subsection-title {{
    font-size: 11pt;
    font-weight: 600;
    color: #2d3748;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}}
h4 {{
    font-size: 10pt;
    font-weight: 600;
    color: #4a5568;
    margin-top: 10px;
    margin-bottom: 4px;
}}
/* Blockquote */
.doc-blockquote {{
    background: #eef2ff;
    border-left: 4px solid #1a56db;
    padding: 8px 14px;
    margin: 10px 0;
    font-size: 9pt;
    color: #334155;
    border-radius: 0 4px 4px 0;
}}
.doc-blockquote p {{
    margin: 2px 0;
}}
/* Paragraph */
.doc-para {{
    margin: 4px 0;
    text-align: justify;
}}
/* Lists */
.list-item {{
    margin: 2px 0;
    line-height: 1.45;
}}
.bullet {{
    color: #1a56db;
    font-weight: bold;
    margin-right: 4px;
}}
/* Code blocks */
.code-block {{
    background: #f0f4f8;
    border: 1px solid #d1d5db;
    border-radius: 5px;
    padding: 10px 14px;
    font-family: 'Cascadia Code', 'Fira Code', 'Consolas', 'Courier New', monospace;
    font-size: 7pt;
    line-height: 1.35;
    overflow-x: auto;
    white-space: pre;
    margin: 10px 0;
    color: #1e293b;
    page-break-inside: avoid;
}}
/* Tables */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 8pt;
    page-break-inside: avoid;
}}
th {{
    background: #1a365d;
    color: white;
    font-weight: 600;
    padding: 6px 8px;
    text-align: left;
    border: 1px solid #2d3748;
    font-size: 8pt;
}}
td {{
    padding: 5px 8px;
    border: 1px solid #d1d5db;
    vertical-align: top;
}}
tr:nth-child(even) td {{
    background: #f8fafc;
}}
tr:nth-child(odd) td {{
    background: white;
}}
/* Horizontal rule */
.doc-hr {{
    border: none;
    border-top: 2px solid #cbd5e0;
    margin: 16px 0;
}}
/* Print styles */
@media print {{
    body {{
        padding: 0;
        max-width: none;
    }}
    .code-block {{
        page-break-inside: avoid;
    }}
    table {{
        page-break-inside: avoid;
    }}
    h2, h3, h4 {{
        page-break-after: avoid;
    }}
    .doc-blockquote {{
        page-break-inside: avoid;
    }}
}}
/* Bold in inline */
strong {{
    color: #1a202c;
}}
em {{
    color: #4a5568;
}}
code {{
    background: #edf2f7;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: 'Cascadia Code', 'Consolas', monospace;
    font-size: 8.5pt;
    color: #c53030;
}}
</style>
</head>
<body>
{body}
</body>
</html>'''


def render_table(rows):
    """Convert table rows to HTML table."""
    if not rows:
        return ''

    html = '<table>\n<thead><tr>'
    for cell in rows[0]:
        html += f'<th>{cell}</th>'
    html += '</tr></thead>\n<tbody>'

    for row in rows[1:]:
        html += '<tr>'
        for cell in row:
            html += f'<td>{cell}</td>'
        html += '</tr>\n'

    html += '</tbody></table>'
    return html


def format_inline(text):
    """Convert markdown inline formatting to HTML."""
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


if __name__ == '__main__':
    md_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('SCHEMA_INFRASTRUTTURA.md')
    html_file = md_file.with_suffix('.html')

    if not md_file.exists():
        print(f"Errore: File non trovato: {md_file}")
        sys.exit(1)

    html = md_to_html(md_file)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML generato: {html_file}")
    print(f"\nPer generare il PDF:")
    print(f"  1. Apri il file '{html_file.name}' nel browser")
    print(f"  2. Premi Ctrl+P (Stampa)")
    print(f"  3. Seleziona 'Salva come PDF' come destinazione")
    print(f"  4. Imposta margini: Nessuno / Predefinito")
    print(f"  5. Abilita: Grafica in background, Intestazioni e piè di pagina")
    print(f"\nOppure apri direttamente con:")
    print(f"  start {html_file.name}")
