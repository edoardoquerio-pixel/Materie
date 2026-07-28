"""
Genera documento Word professionale per l'offerta FortyGroup → TP Group
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

# ============================================================
# COLORI
# ============================================================
DARK_BLUE   = RGBColor(0x0F, 0x17, 0x2A)  # quasi nero blu
BLUE        = RGBColor(0x1E, 0x3A, 0x5F)
SKY         = RGBColor(0x38, 0xBD, 0xF8)
ACCENT_BLUE = RGBColor(0x3B, 0x82, 0xF6)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY  = RGBColor(0xF1, 0xF5, 0xF9)
MID_GRAY    = RGBColor(0x64, 0x74, 0x8B)
TEXT_DARK   = RGBColor(0x1E, 0x29, 0x3B)
ACCENT_GOLD = RGBColor(0xF5, 0x9E, 0x0B)
TABLE_HEADER_BG = "1E3A5F"
TABLE_ALT_BG    = "F1F5F9"
TABLE_BORDER    = "CBD5E1"

# ============================================================
# HELPERS
# ============================================================

def set_cell_bg(cell, color_hex):
    """Imposta sfondo cella tabella."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_border(cell, **kwargs):
    """Bordi singola cella."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}></w:tcBorders>')
    for edge, val in kwargs.items():
        element = parse_xml(
            f'<w:{edge} {nsdecls("w")} w:val="{val.get("val","single")}" '
            f'w:sz="{val.get("sz","4")}" w:space="0" w:color="{val.get("color","CBD5E1")}"/>'
        )
        tcBorders.append(element)
    tcPr.append(tcBorders)

def styled_table(doc, headers, rows, col_widths=None):
    """Crea tabella professionale con header scuro e righe alterne."""
    ncols = len(headers)
    table = doc.add_table(rows=1 + len(rows), cols=ncols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    # Rimuovi bordi default
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="{TABLE_BORDER}"/>'
        f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="{TABLE_BORDER}"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{TABLE_BORDER}"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="{TABLE_BORDER}"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{TABLE_BORDER}"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{TABLE_BORDER}"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    # Header row
    hdr_row = table.rows[0]
    hdr_row.height = Cm(0.9)
    for j, h in enumerate(headers):
        cell = hdr_row.cells[j]
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg(cell, TABLE_HEADER_BG)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = WHITE
        run.font.name = 'Calibri'

    # Data rows
    for i, row_data in enumerate(rows):
        row = table.rows[i + 1]
        row.height = Cm(0.7)
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if i % 2 == 1:
                set_cell_bg(cell, TABLE_ALT_BG)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(str(val))
            run.font.size = Pt(9)
            run.font.color.rgb = TEXT_DARK
            run.font.name = 'Calibri'

    # Widths
    if col_widths:
        for i_row, row in enumerate(table.rows):
            for j, w in enumerate(col_widths):
                row.cells[j].width = Cm(w)

    doc.add_paragraph()  # spacing
    return table

def add_note(doc, text):
    """Nota stile callout grigio."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("⚠  " + text)
    run.font.size = Pt(9)
    run.font.italic = True
    run.font.color.rgb = MID_GRAY

def add_bullet(doc, text, bold_prefix=None):
    """Bullet con eventuale prefisso in grassetto."""
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2)
    if bold_prefix:
        r = p.add_run(bold_prefix)
        r.bold = True
        r.font.size = Pt(10)
        r.font.name = 'Calibri'
        r.font.color.rgb = TEXT_DARK
        r2 = p.add_run(text)
        r2.font.size = Pt(10)
        r2.font.name = 'Calibri'
        r2.font.color.rgb = TEXT_DARK
    else:
        r = p.add_run(text)
        r.font.size = Pt(10)
        r.font.name = 'Calibri'
        r.font.color.rgb = TEXT_DARK

def add_body(doc, text, indent=False):
    """Paragrafo corpo testo."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    if indent:
        p.paragraph_format.left_indent = Cm(0.5)
    r = p.add_run(text)
    r.font.size = Pt(10.5)
    r.font.name = 'Calibri'
    r.font.color.rgb = TEXT_DARK
    return p

def add_section_heading(doc, number, title, level=1):
    """Titolo sezione con numero."""
    text = f"{number}. {title}" if number else title
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = BLUE
        run.font.name = 'Calibri'
    return h

def add_sub_heading(doc, text, level=2):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = BLUE
        run.font.name = 'Calibri'
    return h


# ============================================================
# DOCUMENTO
# ============================================================

doc = Document()

# -- Layout pagina ------------------------------------------------
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

# -- Default style ------------------------------------------------
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)
style.font.color.rgb = TEXT_DARK
style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
style.paragraph_format.line_spacing = 1.15

for level in range(1, 5):
    hs = doc.styles[f'Heading {level}']
    hs.font.name = 'Calibri'
    hs.font.color.rgb = BLUE

# ============================================================
# COPERTINA
# ============================================================

# Spaziatura iniziale
for _ in range(6):
    doc.add_paragraph()

# Titolo
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Convergenza, Integrazione e\nPotenziamento Servizi IT")
run.font.size = Pt(28)
run.font.color.rgb = BLUE
run.font.name = 'Calibri'
run.bold = True

# Linea decorativa
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("━" * 40)
run.font.size = Pt(12)
run.font.color.rgb = SKY

# Sottotitolo
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Azienda TP Group srl")
run.font.size = Pt(18)
run.font.color.rgb = SKY
run.font.name = 'Calibri'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Variante Full Cloud Azure")
run.font.size = Pt(14)
run.font.color.rgb = MID_GRAY
run.font.name = 'Calibri'

# Spaziatura
doc.add_paragraph()
doc.add_paragraph()

# Meta info
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("28 Luglio 2026")
run.font.size = Pt(12)
run.font.color.rgb = MID_GRAY
run.font.name = 'Calibri'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Budget: € 520.000 + IVA")
run.font.size = Pt(12)
run.font.color.rgb = MID_GRAY
run.font.name = 'Calibri'

doc.add_paragraph()

# Team
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("FortyGroup")
run.font.size = Pt(14)
run.bold = True
run.font.color.rgb = ACCENT_BLUE
run.font.name = 'Calibri'

team = "Mario Mogavero · Rita Cignarelli · Lorenzo Sasso\nEdoardo Querio · Luca Tarallo"
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(team)
run.font.size = Pt(10)
run.font.color.rgb = MID_GRAY
run.font.name = 'Calibri'

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Torino, Italia")
run.font.size = Pt(10)
run.font.color.rgb = MID_GRAY
run.font.name = 'Calibri'

# Page break
doc.add_page_break()


# ============================================================
# 1 — PRESENTAZIONE FORTYGROUP
# ============================================================
add_section_heading(doc, 1, "Presentazione FortyGroup")

add_body(doc, "FortyGroup è una startup torinese, fondata nel maggio 2026, con l'obiettivo di creare soluzioni cloud innovative. Il team è composto da 5 specialisti nell'ambito cloud, sempre alla ricerca di nuovi modi per innovare.")

add_sub_heading(doc, "Il nostro team", 2)

team_data = [
    ("Mario Mogavero", "Project Manager", "Responsabile del lavoro del team e del potenziamento dell'applicazione Pondus."),
    ("Rita Cignarelli", "Business Analyst", "Incaricata della redazione del budget e dell'analisi dei costi."),
    ("Lorenzo Sasso", "Infrastructure Architect", "Responsabile dell'infrastruttura e del merge dei sistemi."),
    ("Edoardo Querio", "Cloud & Datacenter Engineer", "Responsabile del potenziamento del datacenter e della migrazione verso Azure."),
    ("Luca Tarallo", "Security & Compliance Engineer", "Responsabile della sicurezza e della conformità ISO 27001."),
]
styled_table(doc, ["Membro", "Ruolo", "Responsabilità"], team_data, [5, 5, 9])


# ============================================================
# 2 — INTRODUZIONE OFFERTA
# ============================================================
add_section_heading(doc, 2, "Introduzione Offerta")

add_body(doc, "Dopo un'analisi approfondita della situazione attuale, abbiamo identificato le seguenti criticità principali che la nostra soluzione intende risolvere:")

problems = [
    "Il datacenter è al limite delle proprie capacità e uno degli obiettivi è il potenziamento dell'infrastruttura.",
    "La sede, che si intende mantenere unica, può ospitare al massimo 40 persone, ma dopo la fusione ci saranno 50 dipendenti.",
    "L'applicazione Pondus deve essere accessibile da più clienti, ma l'infrastruttura attuale non è in grado di garantirlo.",
    "È necessario applicare le macroaree ISO/IEC 27001 richieste dalla normativa di settore.",
    "Le due aziende utilizzano servizi differenti e si deve scegliere quali mantenere e come migrarli.",
    "Il progetto deve rispettare il budget prefissato di € 520.000 + IVA.",
]
for prob in problems:
    add_bullet(doc, prob)

add_sub_heading(doc, "La nostra proposta", 2)

add_body(doc, "Per il datacenter abbiamo deciso di migrare la maggior parte dell'hardware (ad eccezione del cluster HPC) su Microsoft Azure, scelto come provider cloud in quanto è l'unico in grado di offrire tutti i servizi di cui l'azienda ha bisogno, incluso il noleggio di cluster HPC per il calcolo intensivo.")

add_body(doc, "Per ovviare al problema delle postazioni di lavoro nella sede, consigliamo di adottare un modello di smart working rotativo (almeno 1 volta a settimana), con collegamento ai sistemi aziendali tramite VPN. Le postazioni non saranno assegnate in modo fisso ma rotative tra i dipendenti, favorendo l'agilità organizzativa.")

add_body(doc, "Per l'applicazione Pondus è stato progettato l'utilizzo di Azure App Service, piattaforma PaaS costruita specificamente per l'hosting di Web App. Scalabilità e load balancing vengono gestiti automaticamente, garantendo business continuity e semplificando deploy e patching.")

p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.6)
run = p.add_run("Alternativa agnostica: ")
run.bold = True
run.font.size = Pt(10)
run.font.name = 'Calibri'
run.font.color.rgb = BLUE
run2 = p.add_run("In caso si preferisca un approccio indipendente dal cloud provider, è possibile containerizzare l'applicazione e gestirla tramite Kubernetes. Questa soluzione funziona sia su Azure sia su qualsiasi altro cloud provider, ma richiede competenze dedicate per la gestione del cluster.")
run2.font.size = Pt(10)
run2.font.name = 'Calibri'
run2.font.color.rgb = TEXT_DARK

add_body(doc, "Per quanto riguarda la conformità ISO 27001, tutte le macroaree richieste verranno rispettate: verrà creata ridondanza, applicato il disaster recovery plan, criptati tutti i dati e configurata la VPN protetta.")

add_body(doc, "L'integrazione dei servizi avverrà tramite l'ecosistema Microsoft 365 (incluso nella licenza Azure) per la maggior parte dei servizi. Per quelli che non hanno un corrispettivo nativo, verrà mantenuto il servizio cloud di Pro Studio o verranno self-hostati su VM Azure (come nel caso di MediaWiki). La migrazione avverrà gradualmente per non compromettere la business continuity.")


# ============================================================
# 3 — ASSUNZIONI
# ============================================================
add_section_heading(doc, 3, "Assunzioni")

assumptions = [
    "L'azienda provvederà a fornire ai dipendenti di Pro Studio un laptop con cui lavorare da remoto.",
    "L'azienda gestirà la rotazione dei dipendenti per lo smart working.",
    "L'azienda darà l'accesso a FortyGroup ai sistemi aziendali (credenziali, dati, infrastruttura).",
]
for a in assumptions:
    add_bullet(doc, a)


# ============================================================
# 4 — FORNITURA HARDWARE
# ============================================================
add_section_heading(doc, 4, "Fornitura Hardware")

add_sub_heading(doc, "4.1 Hardware Mantenuto", 2)
add_body(doc, "Non si prevede la sostituzione dei seguenti componenti, che verranno integrati nella nuova architettura:")

maintained = [
    ("Cluster HPC esistente: ", "Composto da 8 nodi fisici dedicati al calcolo, interconnessi tramite schede InfiniBand, e da un nodo Front-end con sistema operativo Linux e orchestratore Slurm."),
    ("Firewall: ", "Il dispositivo FortiGate FG-60F verrà riconfigurato per supportare la doppia linea WAN e la connessione VPN verso Azure."),
    ("UPS: ", "Il gruppo di continuità attualmente in dotazione, in grado di garantire 10 minuti di autonomia, verrà mantenuto."),
]
for bp, bt in maintained:
    add_bullet(doc, bt, bold_prefix=bp)

add_sub_heading(doc, "4.2 Hardware da Acquistare", 2)

to_buy = [
    ("Cavi e accessori di rete: ", "Verrà installato un nuovo cavo di rete per la seconda linea internet."),
    ("Seconda linea Internet (backup): ", "Verrà attivato un contratto con un fornitore di connettività per disporre di una linea secondaria dedicata. In caso di guasto della linea primaria, il firewall FortiGate provvederà al failover automatico."),
]
for bp, bt in to_buy:
    add_bullet(doc, bt, bold_prefix=bp)

add_sub_heading(doc, "4.3 Hardware Dismesso", 2)
add_body(doc, "I seguenti componenti verranno rimossi e sostituiti nell'ambito del progetto:")

dismessi = [
    ("2 host VMWare e SAN NetApp da 24 TB: ", "L'infrastruttura di virtualizzazione on-premise risulta obsoleta e non più espandibile. I servizi attualmente ospitati verranno migrati su Azure."),
    ("Web Server Pondus e DB Server SQL: ", "I server fisici che ospitano l'applicazione Pondus e il relativo database verranno dismessi, poiché l'applicazione verrà migrata su Azure App Service e il database su Azure SQL."),
    ("NAS QNAP per backup: ", "Il dispositivo dedicato ai backup on-premise verrà sostituito dal servizio Azure Storage Account."),
]
for bp, bt in dismessi:
    add_bullet(doc, bt, bold_prefix=bp)


# ============================================================
# 5 — ATTIVITÀ RICHIESTE PER SETTORE
# ============================================================
add_section_heading(doc, 5, "Attività Richieste per Settore")

# 5.1 DATACENTER
add_sub_heading(doc, "5.1 Datacenter", 2)
add_body(doc, "Il datacenter on-prem di TP Group (sede unica) viene potenziato per supportare l'infrastruttura ibrida e garantire resilienza:")

dc_items = [
    ("Firewall HA cluster", "FortiGate FG-100F in configurazione active-active per ridondanza completa"),
    ("Switch L3 core", "Due switch 48 porte PoE+ stackable con uplink 10G per la dorsale di rete"),
    ("Switch accesso", "Tre switch 24 porte per la distribuzione verso gli uffici"),
    ("Wireless", "Quattro access point WiFi 6 per copertura completa della sede"),
    ("Alimentazione", "Due UPS rack 1500 VA per continuità elettrica ridondante"),
    ("Cablaggio", "Rete strutturata cat.6A con patch panel in rack 42U"),
    ("Connettività secondaria", "Linea FTTH 1 Gbps come secondo ISP per failover automatico"),
    ("VPN Azure", "Gateway VpnGw1AZ active-standby, IPsec IKEv2 con throughput 250 Mbps"),
    ("VPN Client", "WireGuard integrato con Azure VPN Client per accesso remoto sicuro"),
    ("SIEM (opzionale)", "Microsoft Sentinel come add-on per monitoring avanzato della sicurezza"),
]
styled_table(doc, ["Componente", "Dettaglio"], dc_items, [6, 13])

add_note(doc, "Il cluster HPC on-prem (8 nodi esistenti) viene mantenuto operativo e potenziato con rinnovo licenze e miglioramento dell'interconnessione InfiniBand.")

# 5.2 HPC
add_sub_heading(doc, "5.2 HPC — High Performance Computing", 2)
add_body(doc, "Architettura cluster ibrido: gli 8 nodi on-prem esistenti restano attivi, mentre il burst di capacità viene gestito su Azure tramite CycleCloud con 8 nodi SPOT HB176-96rs v4.")

hpc_items = [
    ("Rinnovo licenze on-prem", "Slurm, Lustre client, driver InfiniBand per i prossimi 3 anni"),
    ("Potenziamento InfiniBand", "Upgrade switch e cavi a standard HDR per abbattere la latenza interna"),
    ("CycleCloud head node", "VM D2s_v3 Linux deployata nella subnet dedicata snet-cyclecloud-westeu"),
    ("Configurazione CycleCloud", "Template cluster per nodi HBv4 con scheduler Slurm integrato"),
    ("Azure Managed Lustre", "Filesystem parallelo gestito 4 TB / 500 MB/s, montato on-prem e Azure"),
    ("Provisioning nodi SPOT", "8 nodi HB176-96rs v4, attivati 8 ore/giorno per 200 giorni/anno"),
    ("Forwarder PBS → Slurm", "Traduzione code on-prem verso Azure per burst trasparente"),
    ("Test di burst", "Provisioning 2 nodi HBv4 SPOT, esecuzione job MPI di validazione"),
]
styled_table(doc, ["Attività", "Dettaglio"], hpc_items, [6, 13])

add_note(doc, "Vincolo tecnico: I job MPI non attraversano la VPN (latenza ~5 ms). La schedulazione separa job on-prem (InfiniBand locale) da job Azure (InfiniBand Azure). I dati sono condivisi via Lustre.")

# 5.3 STORAGE
add_sub_heading(doc, "5.3 Storage", 2)

p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.3)
run = p.add_run("GDPR — Dismissione storage legacy: ")
run.bold = True
run.font.size = Pt(10)
run.font.color.rgb = RGBColor(0xDC, 0x26, 0x26)
run.font.name = 'Calibri'
run2 = p.add_run("Lo storage on-prem attuale (NAS QNAP e SAN NetApp) verrà completamente formattato in modo che i dati non siano più recuperabili, per essere conforme al GDPR. La formattazione avviene solo dopo la verifica completa della migrazione.")
run2.font.size = Pt(10)
run2.font.name = 'Calibri'
run2.font.color.rgb = TEXT_DARK

storage_items = [
    ("Migrazione file", "Dati da NextCloud e Google Drive a SharePoint Online e OneDrive per 50 utenti"),
    ("Verifica integrità", "Checksum, conteggio file, validazione permessi e metadati post-migrazione"),
    ("Backup blob Azure", "Blob Storage RA-GRS per backup configurazioni HPC e Active Directory"),
    ("Azure Backup", "Servizio gestito per VM, database SQL e file con PITR e long-term retention"),
    ("Formattazione NAS QNAP", "Cancellazione sicura completa — dati non recuperabili (GDPR)"),
    ("Formattazione SAN NetApp", "Cancellazione sicura completa LUN — dati non recuperabili (GDPR)"),
    ("Aggiornamento inventario", "Rimozione asset storage legacy dal registro IT aziendale"),
]
styled_table(doc, ["Attività", "Dettaglio"], storage_items, [6, 13])

add_note(doc, "La formattazione fisica (QNAP e NetApp) viene eseguita solo al termine della Fase 7 (Dismissione), dopo verifica completa dei dati su SharePoint/OneDrive e Azure Blob.")

add_sub_heading(doc, "Soluzione Azure — Storage & Cifratura", 3)
add_bullet(doc, "Migrazione e bonifica: I dati correnti (56 TB) vengono migrati verso Azure Storage Account con replica Multi-Zona (ZRS).")
add_bullet(doc, "Formattazione sicura e GDPR: Lo storage dismesso on-premise verrà sottoposto a cancellazione sicura tramite software certificato (Blancco Drive Eraser).")
add_bullet(doc, "Protezione dati: Cifratura in transito e a riposo tramite PMK (FIPS 140-2) e TDE su database Azure SQL.")

# 5.4 SERVIZI
add_sub_heading(doc, "5.4 Servizi", 2)
add_body(doc, "Migrazione completa dei 12 servizi (M1–M12) dall'infrastruttura AS-IS all'ecosistema Microsoft Azure.")

add_sub_heading(doc, "Produttività e Identità — M365 Business Premium (50 utenti)", 3)
serv_m365 = [
    ("M1", "Posta / Calendario", "Zimbra + Google Workspace → Exchange Online", "50"),
    ("M2", "Suite Office", "MS365 + LibreOffice + GWS → M365 BP (desktop + web)", "50"),
    ("M3", "Videoconferenza", "MS Teams + Google Meet → MS Teams", "50"),
    ("M4", "Identità / MFA", "AD Samba4 + Google Auth → Entra ID P1 + MFA", "50"),
    ("M5", "File server", "NextCloud + Google Drive → SharePoint + OneDrive", "50"),
    ("—", "Protezione", "— → Defender for Office 365", "50"),
]
styled_table(doc, ["#", "Servizio", "Migrazione", "Utenti"], serv_m365, [1.5, 4.5, 9, 2])

add_sub_heading(doc, "Applicazioni Gestionali — Dynamics 365", 3)
serv_d365 = [
    ("M6", "CRM", "Sugar CRM + Odoo → Dynamics 365 Sales Pro", "20"),
    ("M7", "ERP / Contabilità", "Profis + Odoo → Dynamics 365 BC Essentials", "10"),
    ("M8", "Timesheet", "Kimai + Odoo → Dynamics 365 BC (incluso)", "10"),
]
styled_table(doc, ["#", "Servizio", "Migrazione", "Utenti"], serv_d365, [1.5, 4.5, 9, 2])

add_sub_heading(doc, "Cloud — Azure PaaS e IaaS", 3)
serv_azure = [
    ("M12", "Pondus Web App", "Azure App Service P1v3 (Linux, 2 vCPU, 8 GB RAM)"),
    ("—", "Pondus Database", "Azure SQL Database S2 (50 DTU, 250 GB)"),
    ("M11", "Media Wiki", "VM Azure B2s (2 vCPU, 4 GB RAM, 30 GB disk)"),
    ("M9/M10", "DevOps", "Azure DevOps — Repos + Pipelines + Artifacts (50 utenti)"),
    ("—", "Connettività", "VPN Gateway VpnGw1AZ active-standby, IPsec IKEv2 (250 Mbps)"),
    ("—", "Backup e DR", "Azure Backup (RA-GRS) + Azure Site Recovery (W.EU → N.EU)"),
]
styled_table(doc, ["#", "Servizio", "Soluzione Azure"], serv_azure, [2, 5, 12])

add_sub_heading(doc, "Backup e Disaster Recovery", 3)
add_bullet(doc, "VM: Azure Backup con storage RA-GRS per VM B2s (Media Wiki) ed eventuali future VM.")
add_bullet(doc, "Database SQL: Point-in-time recovery (35 giorni) + long-term retention annuale su Azure SQL.")
add_bullet(doc, "Disaster Recovery cross-regione: Azure Site Recovery con replica asincrona West Europe → North Europe, RPO < 1h, RTO < 4h.")
add_bullet(doc, "M365 Backup (opzionale): Microsoft 365 Backup dedicato per Exchange, SharePoint, OneDrive.")
add_bullet(doc, "HPC: Blob Storage RA-GRS per configurazioni cluster, script Slurm, snapshot dati Lustre.")

# 5.5 PONDUS
add_sub_heading(doc, "5.5 Applicazione Pondus", 2)
add_body(doc, "Applicazione clienti (C#/.NET) attualmente su hardware fisico, migrata interamente ad Azure PaaS.")

pondus = [
    ("Analisi compatibilità", "Verifica codice .NET per deployment su App Service Linux"),
    ("Adattamento codice", "Modifiche minime: connection string, logging, health check, config Azure"),
    ("Setup App Service", "Provisioning P1v3, VNet integration, slot staging per zero-downtime"),
    ("Setup Azure SQL", "Provisioning S2, firewall regole, geo-replica per DR"),
    ("Migrazione database", "Schema + dati + stored procedure + indici; validazione integrità"),
    ("Test e validazione", "Test funzionali E2E, carico, penetration test, validazione utenti pilota"),
    ("CI/CD Pipeline", "Azure DevOps: build → test → staging → production con approvazione"),
    ("DNS e go-live", "pondus.tpgroup.it → App Service, custom domain + TLS, monitoraggio"),
]
styled_table(doc, ["Attività", "Dettaglio"], pondus, [5.5, 13.5])

add_sub_heading(doc, "Soluzione Azure — Potenziamento Applicativo", 3)
add_bullet(doc, "Azure App Service: PaaS Linux in configurazione Multi-Zona (2 istanze, Load Balancer Standard), scalabilità automatica, zero downtime.")
add_bullet(doc, "Azure SQL Database: General Purpose, Zone-Redundant, replica sincrona su 3 zone logiche.")

# 5.6 SICUREZZA
add_sub_heading(doc, "5.6 Sicurezza e Conformità ISO/IEC 27001", 2)
add_bullet(doc, "Autenticazione multi-fattore (MFA) ed estensione del RBAC con principio del minimo privilegio.")
add_bullet(doc, "Tunnel VPN protetti (WireGuard / Azure VPN Gateway VpnGw1).")
add_bullet(doc, "Monitoraggio continuo, logging, gestione incidenti e audit periodici per il rispetto delle macroaree ISO/IEC 27001.")

# 5.7 BCDR
add_sub_heading(doc, "5.7 Business Continuity e Disaster Recovery", 2)
add_body(doc, "Per soddisfare i requisiti di RTO < 4 ore e RPO < 1 ora, la soluzione implementa Azure Site Recovery (ASR):")
add_bullet(doc, "Cloud-to-Cloud (Cross-Region Intra-UE): Produzione su Azure Italy North (Milano) replicata in modo asincrono verso West Europe (Paesi Bassi). Recovery Plan automatizzato con ripristino in < 30 minuti.")
add_bullet(doc, "On-Premises-to-Cloud (Sede Torino): Server locali protetti via ASR in modalità DRaaS, mantenuti in cloud spenti per azzerare i costi di calcolo fino al ripristino.")


# ============================================================
# 6 — ATTIVITÀ DI IMPLEMENTAZIONE
# ============================================================
add_section_heading(doc, 6, "Attività di Implementazione")

add_sub_heading(doc, "6.1 Installazione Hardware e Connettività", 2)
add_bullet(doc, "Attestazione e configurazione della seconda linea internet di backup.")
add_bullet(doc, "Configurazione delle regole di failover automatico e delle policy SD-WAN sul firewall FortiGate.")

add_sub_heading(doc, "6.2 Migrazione e Installazione Software", 2)
add_bullet(doc, "Rollout di Microsoft 365 per i 50 utenti aziendali (posta, Teams, SharePoint/OneDrive).")
add_bullet(doc, "Configurazione di MediaWiki su VM dedicata Azure.")
add_bullet(doc, "Esecuzione della procedura di formattazione sicura dei dischi dismessi tramite Blancco Drive Eraser.")
add_bullet(doc, "Predisposizione delle pipeline di CI/CD e versionamento software su Azure DevOps.")

add_sub_heading(doc, "6.3 Test Funzionali, Collaudo e Rollback", 2)
add_bullet(doc, "Validazione Performance e Licenze: Test di carico e verifica compatibilità licenze software ingegneristiche in ambiente Cloud/Ibrido.")
add_bullet(doc, "Test di DR Non Distruttivi: Simulazione disaster recovery in ambienti isolati tramite Azure Site Recovery.")
add_bullet(doc, "Strategia di Rollback: L'infrastruttura locale legacy rimane attiva fino al collaudo finale. In caso di criticità bloccanti, il reindirizzamento del traffico su Torino avviene entro 30 minuti.")


# ============================================================
# 7 — ESCLUSIONI
# ============================================================
add_section_heading(doc, 7, "Esclusioni")
add_body(doc, "Sono esclusi dal perimetro del presente progetto:")
add_bullet(doc, "Laptop e postazioni di lavoro per i dipendenti.")
add_bullet(doc, "Arredi e infrastruttura fisica della sede.")
add_bullet(doc, "Licenze software ingegneristiche di terze parti (a carico del Cliente).")
add_bullet(doc, "Connessione internet primaria (già esistente).")
add_bullet(doc, "Organizzazione della rotazione smart working (a carico del Cliente).")


# ============================================================
# 8 — DOCUMENTAZIONE E FORMAZIONE
# ============================================================
add_section_heading(doc, 8, "Documentazione e Formazione")

add_sub_heading(doc, "8.1 Documentazione Tecnica", 2)
add_body(doc, "Al termine del progetto, il Fornitore consegna:")
add_bullet(doc, "Documentazione as-built dell'infrastruttura.")
add_bullet(doc, "Manuali utente per i nuovi servizi (M365, Dynamics, Teams).")
add_bullet(doc, "Procedure di backup e restore.")
add_bullet(doc, "Piano di disaster recovery.")
add_bullet(doc, "Report finale di migrazione.")

add_sub_heading(doc, "8.2 Formazione", 2)
add_body(doc, "Il Fornitore eroga sessioni di formazione suddivise in due fasi:")

add_body(doc, "Fase 1 — Formazione utenti base (inclusa)", indent=True)
form1 = [
    ("M365 base (posta, calendario, Office Online)", "4 ore", "Tutti i 50 utenti"),
    ("Dynamics 365 (CRM + ERP)", "8 ore", "10 utenti chiave"),
    ("Teams (comunicazione, riunioni, canali)", "2 ore", "Tutti i 50 utenti"),
    ("Amministrazione M365 + SharePoint", "4 ore", "Sistemisti"),
]
styled_table(doc, ["Tipologia", "Durata", "Destinatari"], form1, [10, 3, 6])

add_body(doc, "Fase 2 — Formazione nuova infrastruttura (dipendenti TP Group)", indent=True)
form2 = [
    ("SharePoint/OneDrive", "2 ore", "50 utenti standard"),
    ("Rete aziendale: FortiGate HA, VLAN, VPN WireGuard", "4 ore", "IT staff (5-6)"),
    ("Azure administration: portale, costi, monitoraggio", "4 ore", "IT staff"),
    ("Azure DevOps: repos, pipelines, CI/CD", "4 ore", "Dev team (5-8)"),
    ("HPC ibrido: CycleCloud, job submission, Lustre", "4 ore", "HPC team (3-4)"),
    ("Backup e DR: Azure Backup, Site Recovery, restore", "4 ore", "IT staff"),
    ("Procedure sicurezza: ISO 27001, incident response", "4 ore", "IT staff + referenti"),
]
styled_table(doc, ["Modulo", "Durata", "Destinatari"], form2, [10, 3, 6])

add_note(doc, "Costo Fase 2: € 4.000, corrisposto contestualmente al completamento (entro milestone M6). Documentazione utente e guide operative incluse nel progetto (€ 2.000). Totale formazione: 27 ore — € 9.000.")


# ============================================================
# 9 — TERMINI E CONDIZIONI
# ============================================================
add_section_heading(doc, 9, "Termini e Condizioni")

# 9.1
add_sub_heading(doc, "9.1 Oggetto del Contratto", 2)
add_body(doc, "Il presente documento definisce i termini e le condizioni che regolano il rapporto tra il Fornitore (FortyGroup) e il Cliente (TP Group — Thema Consulting srl + Pro Studio srl) per la realizzazione del progetto di integrazione IT secondo la variante Full Cloud Azure.")
add_body(doc, "Il Fornitore si impegna a erogare i servizi descritti nell'Offerta Tecnico-Economica, comprensivi di:")
add_bullet(doc, "Migrazione dei servizi M1-M12 verso l'ecosistema Microsoft/Azure.")
add_bullet(doc, "Infrastruttura di rete e connettività VPN.")
add_bullet(doc, "Configurazione sicurezza ISO 27001.")
add_bullet(doc, "Cluster HPC ibrido (on-prem + Azure CycleCloud).")
add_bullet(doc, "Backup e disaster recovery.")
add_bullet(doc, "Formazione utenti e affiancamento post-migrazione.")

add_body(doc, "Ordine di prevalenza in caso di conflitto tra documenti:", indent=True)
add_bullet(doc, "Il presente contratto e i suoi allegati.", bold_prefix="1. ")
add_bullet(doc, "L'Offerta Tecnico-Economica.", bold_prefix="2. ")
add_bullet(doc, "I documenti tecnici di progetto (aree 01–09).", bold_prefix="3. ")
add_bullet(doc, "Le specifiche tecniche dei produttori (Microsoft, Fortinet, ecc.).", bold_prefix="4. ")

# 9.2
add_sub_heading(doc, "9.2 Durata e Decorrenza", 2)
durata = [
    ("Migrazione", "10 settimane", "01/09/2026 – 07/11/2026"),
    ("Affiancamento post-migrazione", "2 settimane", "08/11/2026 – 21/11/2026"),
    ("Manutenzione ordinaria (opzionale)", "3 anni", "Dalla data di collaudo"),
]
styled_table(doc, ["Fase", "Durata", "Periodo"], durata, [7, 3.5, 6])
add_body(doc, "Il contratto si intende efficace dalla data di sottoscrizione da parte di entrambe le parti. I servizi di manutenzione e i canoni cloud si intendono rinnovati tacitamente di anno in anno, salvo disdetta via PEC almeno 60 giorni prima della scadenza.")

# 9.3
add_sub_heading(doc, "9.3 Corrispettivi e Modalità di Pagamento", 2)
add_body(doc, "Tranche di pagamento — Investimento iniziale:")
tranche = [
    ("1ª — Acconto", "30%", "Alla sottoscrizione del contratto"),
    ("2ª — Stato avanzamento", "30%", "Al completamento della Fase 3 (Dynamics 365 attivo)"),
    ("3ª — Saldo", "40%", "Al collaudo positivo e accettazione finale"),
]
styled_table(doc, ["Tranche", "Importo", "Evento"], tranche, [5, 3, 9])

add_body(doc, "Canoni cloud (ricorrenti) — fatturati trimestralmente in via anticipata:")
cloud = [
    ("Anno 1 (mesi 1-12)", "€ 11.384,50"),
    ("Anno 2 (mesi 13-24)", "€ 11.384,50"),
    ("Anno 3 (mesi 25-36)", "€ 11.384,50"),
]
styled_table(doc, ["Periodo", "Importo trimestrale"], cloud, [8, 5])

add_body(doc, "Ritardi di pagamento: Trascorsi 30 giorni dalla fattura, interessi di mora al tasso legale + 8 punti percentuali. Trascorsi 60 giorni, facoltà di sospensione servizi cloud previa comunicazione di 7 giorni.")
add_body(doc, "Adeguamento prezzi: I canoni cloud sono soggetti ad adeguamento annuale in base alle variazioni dei listini Microsoft, con preavviso di 60 giorni.")

# 9.4
add_sub_heading(doc, "9.4 Penali e Ritardi", 2)
penali = [
    ("Oltre la data di collaudo prevista", "0,5% dell'investimento iniziale per settimana"),
    ("Oltre 4 settimane di ritardo", "1,0% per ogni settimana aggiuntiva"),
    ("Massimale penali", "15% dell'investimento iniziale"),
]
styled_table(doc, ["Ritardo", "Penale"], penali, [8, 10])
add_body(doc, "Le penali non si applicano in caso di ritardi imputabili al Cliente, eventi di forza maggiore, o variazioni del perimetro richieste dal Cliente (change request).")

# 9.5
add_sub_heading(doc, "9.5 Responsabilità e Garanzie", 2)
add_body(doc, "Il Fornitore si impegna a:")
add_bullet(doc, "Eseguire le lavorazioni a regola d'arte, secondo le best practice del settore.")
add_bullet(doc, "Utilizzare personale qualificato e adeguatamente formato.")
add_bullet(doc, "Garantire la conformità del progetto alle specifiche tecniche concordate.")
add_bullet(doc, "Mantenere la massima riservatezza sui dati del Cliente.")
add_bullet(doc, "Rispettare le normative sulla protezione dei dati (GDPR).")

add_body(doc, "Limitazione di responsabilità: Salvo casi di dolo o colpa grave, la responsabilità del Fornitore è limitata all'importo dell'investimento iniziale.", indent=True)
add_body(doc, "Garanzia sui servizi: 6 mesi dalla data di collaudo per difetti imputabili alle attività di migrazione (corretti senza addebito).", indent=True)
add_body(doc, "Garanzia sull'hardware: Coperta dalla garanzia del produttore (3 anni). Il Fornitore gestisce le pratiche RMA per conto del Cliente.", indent=True)

# 9.6
add_sub_heading(doc, "9.6 Service Level Agreement (SLA)", 2)
add_body(doc, "Disponibilità servizi cloud (SLA Microsoft):")
sla_ms = [
    ("M365 Business Premium", "99,9%"),
    ("Dynamics 365", "99,9%"),
    ("Azure App Service", "99,95% (multi-istanza)"),
    ("Azure SQL Database", "99,99%"),
]
styled_table(doc, ["Servizio", "Disponibilità"], sla_ms, [8, 8])

add_body(doc, "SLA del Fornitore (supporto post-migrazione):")
sla_fg = [
    ("Critico — Servizio non accessibile", "P1", "≤ 1 ora", "≤ 8 ore"),
    ("Alto — Funzionalità gravemente degradata", "P2", "≤ 4 ore", "≤ 24 ore"),
    ("Medio — Funzionalità parzialmente degradata", "P3", "≤ 8 ore", "≤ 48 ore"),
    ("Basso — Richiesta di informazione", "P4", "≤ 24 ore", "≤ 5 giorni"),
]
styled_table(doc, ["Categoria", "Priorità", "Risposta", "Risoluzione"], sla_fg, [8, 2, 3, 4])

add_body(doc, "Crediti SLA:")
crediti = [
    ("< 99,9%", "5% del canone annuo cloud"),
    ("< 99,5%", "10% del canone annuo cloud"),
    ("< 99,0%", "15% del canone annuo cloud"),
]
styled_table(doc, ["Disponibilità", "Credito"], crediti, [8, 8])

add_body(doc, "Gli SLA non si applicano in caso di manutenzione programmata (comunicata 48h prima), forza maggiore, azioni del Cliente, o servizi contrassegnati come 'beta' da Microsoft.")

# 9.7–9.15 Compattati
tc_sections = [
    ("9.7 Proprietà Intellettuale", [
        "Codice sviluppato (script, config DevOps, personalizzazioni Dynamics) → proprietà del Cliente.",
        "Strumenti e metodologie del Fornitore → esclusiva proprietà del Fornitore.",
        "Licenze Microsoft, Fortinet e terzi → regolate dai rispettivi contratti EULA.",
    ]),
    ("9.8 Privacy e GDPR", [
        "TP Group è Titolare del trattamento. Il Fornitore agisce come Responsabile (art. 28 GDPR).",
        "Dati: dipendenti, contabili/fiscali, tecnici (credenziali, certificati), clienti (Pondus/Dynamics).",
        "Misure: Cifratura in transito/a riposo, RBAC, MFA, logging/auditing.",
        "Data breach: Notifica al Titolare entro 24 ore dalla conoscenza.",
        "Sub-responsori: Microsoft Corporation (DPA Microsoft).",
    ]),
    ("9.9 Riservatezza", [
        "Obbligo di riservatezza sulle informazioni confidenziali per la durata del contratto + 5 anni.",
        "Esclusioni: informazioni di pubblico dominio, ricevute da terzi, richieste da autorità.",
    ]),
    ("9.10 Gestione del Cambiamento", [
        "Qualsiasi modifica deve essere formalizzata con Change Request scritta, approvata da entrambe le parti.",
        "Variazione < 5%: approvazione PM Fornitore | 5–15%: Comitato di Progetto | > 15%: Direzione TP Group + Fornitore.",
    ]),
    ("9.11 Forza Maggiore", [
        "Eventi esclusi: disastri naturali, terrorismo, pandemie, blackout, attacchi informatici non prevenibili.",
        "Notifica entro 5 giorni. Se l'evento si protrae > 60 giorni, recesso senza penalità.",
    ]),
    ("9.12 Recesso Anticipato", [
        "Per giusta causa: diffida ad adempiere entro 30 giorni.",
        "Senza giusta causa (Cliente): preavviso 90 giorni + pagamento prestazioni eseguite e 50% di quelle pianificate.",
        "Effetti: consegna documentazione, esporta dati, assistenza passaggio fornitore.",
    ]),
    ("9.13 Collaudo e Accettazione", [
        "Collaudo per ciascuna fase (F0–F7) secondo criteri di successo definiti.",
        "15 giorni lavorativi per verifiche. Trascorsi senza comunicazioni → accettazione implicita.",
        "Collaudo finale (Fase 7) = condizione per saldo 40%.",
    ]),
    ("9.14 Subappalto", [
        "Non consentito senza autorizzazione scritta. Il Fornitore resta responsabile.",
    ]),
    ("9.15 Legge Applicabile e Foro Competente", [
        "Legge italiana. Foro competente: Torino.",
    ]),
]
for title, bullets in tc_sections:
    add_sub_heading(doc, title, 2)
    for b in bullets:
        add_bullet(doc, b)


# ============================================================
# 10 — QUOTAZIONE ECONOMICA
# ============================================================
add_section_heading(doc, 10, "Quotazione Economica")

add_sub_heading(doc, "10.1 Massimizzazione dell'Efficienza Cloud", 2)
add_bullet(doc, "Reserved Instances (3 & 5 anni): Blocco tariffe su servizi dati e di rete per 3 anni. Per il calcolo (VM Burst), opzioni a 5 anni con sconto ~67%, risparmio netto triennale di € 42.500.")
add_bullet(doc, "Ottimizzazione VPN: VpnGw1 (~€ 300/mese) al posto di VpnGw3 (~€ 1.050/mese), risparmio € 9.000/anno = € 27.000 nel triennio.")

add_sub_heading(doc, "10.2 Introduzione Progressiva dei Servizi", 2)
add_bullet(doc, "Differimento HPC: Infrastruttura di calcolo avanzata attivata dal Mese 13.")
add_bullet(doc, "Spese inattive azzerate: Solo 2 anni di utilizzo effettivo (€ 38.500/anno × 2 = € 77.000). MediaWiki operativa dal giorno 1 (~€ 100/mese).")

add_sub_heading(doc, "10.3 Calibrazione Licenzionamento", 2)
add_bullet(doc, "Microsoft 365 (50 utenti): € 18,00/utente/mese = € 10.800/anno = € 32.400 nei 3 anni.")
add_bullet(doc, "Gestionali Dynamics 365 & DevOps (10 utenti chiave): € 35,00/utente/mese = € 4.200/anno = € 12.600 nei 3 anni.")

add_sub_heading(doc, "10.4 Scalabilità e Conformità ISO/IEC 27001", 2)
add_bullet(doc, "App Service P3mv3 per Pondus: 64 GB RAM (~€ 850/mese), multi-hosting possibile per ulteriori servizi.")
add_bullet(doc, "Storage ZRS: Replica sincronizzata su 3 zone, piena conformità BCDR ISO/IEC 27001.")

add_sub_heading(doc, "10.5 Riepilogo Economico Triennale", 2)
riepilogo = [
    ("Costo complessivo triennale", "€ 453.023,92 (IVA esclusa)"),
    ("Budget disponibile", "€ 525.000 + IVA"),
    ("Margine residuo", "~€ 77.000"),
]
styled_table(doc, ["Voce", "Importo"], riepilogo, [8, 8])
add_body(doc, "Il margine residuo potrà assorbire eventuali costi imprevisti, variazioni di utilizzo o futuri potenziamenti dell'infrastruttura.")


# ============================================================
# 11 — GANTT
# ============================================================
add_section_heading(doc, 11, "Gantt")
add_body(doc, "[Inserire diagramma di Gantt — riferimento al documento 09_Project_Management/gantt.md]")

# ============================================================
# 12 — MATRICE RASCI
# ============================================================
add_section_heading(doc, 12, "Matrice RASCI")
add_body(doc, "[Inserire matrice RASCI — riferimento al documento 09_Project_Management/matrice_rasci.md]")
add_body(doc, "Responsible (R) · Accountable (A) · Supports (S) · Consulted (C) · Informed (I)", indent=True)


# ============================================================
# FOOTER & HEADER
# ============================================================
for section in doc.sections:
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("FortyGroup — Offerta TP Group — Confidential")
    run.font.size = Pt(8)
    run.font.color.rgb = MID_GRAY
    run.font.name = 'Calibri'


# ============================================================
# SALVATAGGIO
# ============================================================
out = "C:/Users/edoardo.querio/Desktop/Materie/23_Project_Work_e_Laboratori/03_Progetti/ProjectWork_Infrastruttura_IT/FullCloudAzure/08_Offerta_Documenti/Documento_Offerta_TP_Group_FortyGroup_BOZZA_OTTIMIZZATO.docx"
doc.save(out)
print(f"OK Documento salvato: {out}")
print(f"   Dimensione: {os.path.getsize(out) / 1024:.1f} KB")
