#!/usr/bin/env python3
"""
Moodle FAD Sync Tool - ITS ICT Piemonte
========================================
Scarica automaticamente i materiali da TUTTI i corsi del portale FAD
e li organizza nelle directory corrispondenti del workspace.

Parte dalla dashboard /my/ per scoprire tutti i corsi disponibili,
poi per ogni corso mappato in COURSE_MAP scarica le risorse (mod/resource)
organizzandole in sottocartelle per sezione.

Utilizzo:
    python tools/moodle-sync.py

Config:
    tools/.env con:
        MOODLE_USERNAME=tua@email.it
        MOODLE_PASSWORD=tua_password

Requisiti:
    pip install playwright python-dotenv
    python -m playwright install chromium
"""

import os
import re
import base64
import sys
import pathlib
import argparse
from datetime import datetime
from urllib.parse import unquote

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

try:
    import keyring
    KEYRING_AVAILABLE = True
except ImportError:
    KEYRING_AVAILABLE = False

SERVICE_NAME = "moodle-fad-its-ict"


# =============================================================================
# WORKSPACE ROOT (rilevata automaticamente)
# =============================================================================
SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WORKSPACE_ROOT = SCRIPT_DIR.parent  # tools/ -> workspace root

# =============================================================================
# CONFIGURAZIONE GENERALE
# =============================================================================

BASE_URL = "https://fad.its-ictpiemonte.it"
DASHBOARD_URL = f"{BASE_URL}/my/"

# COURSE_MAP: mappa i codici corso Moodle alle directory del workspace.
# Il codice corso viene estratto dal nome del corso sulla dashboard:
#   "(CSP_25-27-11) Inglese" -> codice = "CSP_25-27-11"

COURSE_MAP: dict[str, dict] = {
    # (codice, directory workspace, sottocartella materiali)
    "CSP_25-27-00": {"dir": "00_Amministrazione_Corso",   "materials": "_FAD"},
    "CSP_25-27-04": {"dir": "00_Amministrazione_Corso",   "materials": "_FAD"},
    "CSP_25-27-11": {"dir": "01_Inglese_Tecnico",         "materials": "01_Materiale"},
    "CSP_25-27-02": {"dir": "02_Orientamento_e_Soft_Skills", "materials": "_FAD"},
    "CSP_25-27-14": {"dir": "02_Orientamento_e_Soft_Skills", "materials": "_FAD"},
    "CSP_25-27-21": {"dir": "02_Orientamento_e_Soft_Skills", "materials": "_FAD"},
    "CSP_25-27-20": {"dir": "03_Parita_e_Non_Discriminazione", "materials": "_FAD"},
    "CSP_25-27-26": {"dir": "04_Sicurezza_sul_Lavoro",    "materials": "_FAD"},
    "CSP_25-27-07": {"dir": "05_Fondamenti_ICT",          "materials": "_FAD"},
    "CSP_25-27-08": {"dir": "06_Reti_e_Sicurezza_Informatica", "materials": "_FAD"},
    "CSP_25-27-25": {"dir": "06_Reti_e_Sicurezza_Informatica", "materials": "_FAD"},
    "CSP_25-27-09": {"dir": "07_Version_Control_Git",     "materials": "_FAD"},
    "CSP_25-27-06": {"dir": "08_Basi_di_Dati_SQL_NoSQL",  "materials": "_FAD"},
    "CSP_25-27-23": {"dir": "10_Programmazione_Python",    "materials": "_FAD"},
    "CSP_25-27-22": {"dir": "11_Programmazione_DotNet_CSharp", "materials": "_FAD"},
    "CSP_25-27-24": {"dir": "12_RESTful_API",              "materials": "_FAD"},
    "CSP_25-27-01": {"dir": "13_Cloud_AWS",                "materials": "_FAD"},
    "CSP_25-27-18": {"dir": "14_Cloud_Azure",              "materials": "_FAD"},
    "CSP_25-27-10": {"dir": "15_Cloud_GCP",                "materials": "_FAD"},
    "CSP_25-27-16": {"dir": "16_Linux_Server_e_Amministrazione", "materials": "_FAD"},
    "CSP_25-27-03": {"dir": "17_Container_Docker_Kubernetes",    "materials": "_FAD"},
    "CSP_25-27-17": {"dir": "18_Microsoft_365_SharePoint", "materials": "_FAD"},
    "CSP_25-27-27": {"dir": "19_Virtualizzazione",         "materials": "_FAD"},
    "CSP_25-27-05": {"dir": "20_Data_Analytics_Visualization", "materials": "_FAD"},
    "CSP_25-27-12": {"dir": "21_Internet_of_Things",       "materials": "_FAD"},
    "CSP_25-27-28": {"dir": "22_AI_e_Prompt_Engineering",  "materials": "_FAD"},
    "CSP_25-27-13": {"dir": "23_Project_Work_e_Laboratori", "materials": "_FAD"},
    "CSP_25-27-15": {"dir": "23_Project_Work_e_Laboratori", "materials": "_FAD"},
    "CSP_25-27-19": {"dir": "24_Stage_Professionale",      "materials": "_FAD"},
}

# Moduli Moodle da scaricare (contengono file)
DOWNLOADABLE_MODULES = {"resource"}


# =============================================================================
# FUNZIONI DI SUPPORTO
# =============================================================================

def load_credentials(use_keyring: bool = True) -> tuple[str, str]:
    """Carica le credenziali: prima da Windows Credential Manager (keyring),
    poi da file .env come fallback."""

    # 1) Prova Windows Credential Manager
    if use_keyring and KEYRING_AVAILABLE:
        try:
            username = keyring.get_password(SERVICE_NAME, "username")
            password = keyring.get_password(SERVICE_NAME, "password")
            if username and password:
                return username.strip(), password
        except Exception:
            pass

    # 2) Fallback: file .env
    env_path = SCRIPT_DIR / ".env"
    load_dotenv(env_path)
    username = os.getenv("MOODLE_USERNAME", "").strip()
    password = os.getenv("MOODLE_PASSWORD", "")
    if username and password:
        return username, password

    print(f"\n[ERR] Credenziali non trovate.")
    print("Opzioni:")
    print(f"  1. python tools/moodle-sync.py --store-creds   (salva in Windows Credential Manager)")
    print(f"  2. Creare {SCRIPT_DIR / '.env'} con:")
    print("     MOODLE_USERNAME=tua@email.it")
    print("     MOODLE_PASSWORD=tua_password")
    sys.exit(1)


def store_credentials(username: str, password: str) -> bool:
    """Salva le credenziali in Windows Credential Manager."""
    if not KEYRING_AVAILABLE:
        print("[ERR] Libreria 'keyring' non installata. Installa con: pip install keyring")
        return False
    try:
        keyring.set_password(SERVICE_NAME, "username", username)
        keyring.set_password(SERVICE_NAME, "password", password)
        return True
    except Exception as e:
        print(f"[ERR] Impossibile salvare credenziali: {e}")
        return False


def sanitize_filename(name: str) -> str:
    """Rimuove caratteri non validi per filename su Windows."""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = name.strip('. ')
    name = re.sub(r'\s+', ' ', name)
    return name[:200]


def extract_filename_from_cd(content_disposition: str, fallback_title: str,
                              content_type: str) -> str:
    """Estrae il filename dall'header Content-Disposition."""
    match = re.search(r"filename\*=(?:UTF-8|ISO-8859-1)''(.+?)(?:;|$)",
                       content_disposition)
    if match:
        return sanitize_filename(unquote(match.group(1)))
    match = re.search(r'filename="([^"]*)"', content_disposition)
    if match:
        return sanitize_filename(match.group(1))
    match = re.search(r'filename=([^;]+)', content_disposition)
    if match:
        return sanitize_filename(match.group(1).strip())
    ext_map = {
        'application/pdf': '.pdf',
        'application/msword': '.doc',
        'application/vnd.openxmlformats-officedocument.'
        'wordprocessingml.document': '.docx',
        'application/vnd.ms-powerpoint': '.ppt',
        'application/vnd.openxmlformats-officedocument.'
        'presentationml.presentation': '.pptx',
        'application/vnd.ms-excel': '.xls',
        'application/vnd.openxmlformats-officedocument.'
        'spreadsheetml.sheet': '.xlsx',
        'text/plain': '.txt',
        'text/html': '.html',
        'application/zip': '.zip',
        'image/png': '.png',
        'image/jpeg': '.jpg',
    }
    ct_clean = content_type.split(';')[0].strip()
    ext = ext_map.get(ct_clean, '')
    return sanitize_filename(f"{fallback_title}{ext}")


def shorten_course_name(name: str, max_len: int = 60) -> str:
    """Accorcia il nome del corso per la stampa."""
    # Toglie il prefisso (CSP_25-27-XX)
    clean = re.sub(r'^\([\w-]+\)\s*', '', name)
    if len(clean) > max_len:
        clean = clean[:max_len-3] + "..."
    return clean


# =============================================================================
# FUNZIONI MOODLE
# =============================================================================

def scrape_dashboard_courses(page) -> list[dict]:
    """Estrae l'elenco di tutti i corsi dalla dashboard."""
    page.goto(DASHBOARD_URL, wait_until="networkidle")
    page.wait_for_timeout(2000)

    courses = page.evaluate("""
        () => {
            const links = document.querySelectorAll(
                'a[href*="course/view.php?id="]'
            );
            const seen = new Set();
            const results = [];

            for (const link of links) {
                const href = link.getAttribute('href');
                const text = link.textContent.trim();

                if (!text || !href) continue;
                if (text.length < 5) continue;

                // Estrai ID corso
                const idMatch = href.match(/id=(\\d+)/);
                const courseId = idMatch ? idMatch[1] : null;

                // Estrai codice corso: (CODICE) Nome
                const codeMatch = text.match(/\\(([\\w-]+)\\)/);
                const code = codeMatch ? codeMatch[1] : null;

                const key = courseId || href;
                if (seen.has(key)) continue;
                seen.add(key);

                results.push({
                    title: text,
                    code: code,
                    id: courseId,
                    url: href.startsWith('http') ? href
                        : 'https://fad.its-ictpiemonte.it' + href,
                });
            }

            return results;
        }
    """)

    return courses


def scrape_course_sections(page, course_url: str) -> list[dict]:
    """
    Scopre tutte le sezioni di un corso Moodle navigando ogni sezione
    singolarmente via ?section=N (formato sezione singola).
    """
    # 1) Carica pagina base per scoprire la navigazione sezioni
    page.goto(course_url, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)

    nav_sections = page.evaluate("""
        () => {
            const result = [];
            // Cerca link di navigazione alle sezioni: href ~ "#section-N"
            const links = document.querySelectorAll(
                'a[href*="#section-"]:not([href*="module-"])'
            );
            const seen = new Set();
            for (const a of links) {
                const text = a.textContent.trim();
                if (!text || text.length < 2) continue;
                const m = a.href.match(/#section-(\\d+)$/);
                if (!m) continue;
                const num = parseInt(m[1]);
                const key = num + ':' + text;
                if (seen.has(key)) continue;
                seen.add(key);
                result.push({ number: num, title: text });
            }
            return result;
        }
    """)
    nav_sections.sort(key=lambda s: s["number"])

    if not nav_sections:
        # Fallback: estrai da pagina corrente
        return scrape_visible_section(page, course_url)

    sections_out = []

    # 2) Sezione 0: gia' visibile, estrai subito
    sec0 = [s for s in nav_sections if s["number"] == 0]
    other_secs = [s for s in nav_sections if s["number"] != 0]

    for sec in sec0 + other_secs:
        num = sec["number"]
        title = sec["title"]

        if num > 0:
            # Carica la sezione specifica via URL parameter
            sep = "&" if "?" in course_url else "?"
            sec_url = f"{course_url}{sep}section={num}"
            page.goto(sec_url, wait_until="domcontentloaded")
            page.wait_for_timeout(2000)

        # Estrai risorse dalla sezione corrente
        resources = page.evaluate("""
            (targetNum) => {
                const sec = document.getElementById('section-' + targetNum);
                if (!sec) return [];

                const links = sec.querySelectorAll('a[href*="mod/resource/view.php"]');
                const seen = new Set();
                const res = [];
                for (const l of links) {
                    const href = l.getAttribute('href');
                    const text = l.textContent.trim();
                    if (!text || !href || text.length < 2 || /sezione|sposta/i.test(text)) continue;
                    const idm = href.match(/[?&]id=(\\d+)/);
                    const rid = idm ? idm[1] : href;
                    if (seen.has(rid)) continue;
                    seen.add(rid);
                    res.push({
                        title: text,
                        url: href.startsWith('http') ? href : 'https://fad.its-ictpiemonte.it' + href,
                        id: rid,
                    });
                }
                return res;
            }
        """, num)

        sections_out.append({
            "id": f"section-{num}",
            "number": num,
            "title": title,
            "resources": resources,
        })

    return sections_out


def scrape_visible_section(page, course_url: str) -> list[dict]:
    """Fallback: estrae la/le sezioni visibili nella pagina corrente."""
    page.goto(course_url, wait_until="domcontentloaded")
    page.wait_for_timeout(2000)

    return page.evaluate("""
        () => {
            function qs(e, s) { try { return e.querySelector(s); } catch(_) { return null; } }
            function qsa(e, s) { try { return e.querySelectorAll(s); } catch(_) { return []; } }
            const all = document.querySelectorAll('li.section.main, .section, [id^="section-"]');
            const out = [];
            for (const sec of all) {
                if (sec.tagName === 'LI' && !sec.classList.contains('section')) continue;
                const secId = sec.id || '';
                if (!secId.startsWith('section-') && !sec.querySelector('.content')) continue;
                const tel = qs(sec, '.sectionname');
                const title = tel ? tel.textContent.trim() : (secId.replace('section-', 'S') || 'Generale');
                if (!title || /precedente|successiva/i.test(title)) continue;
                const nm = secId.match(/section-(\\d+)/);
                const num = nm ? parseInt(nm[1]) : null;
                const rls = qsa(sec, 'a[href*="mod/resource/view.php"]');
                const res = [];
                const seen = new Set();
                for (const l of rls) {
                    const href = l.getAttribute('href');
                    const text = l.textContent.trim();
                    if (!text || !href || text.length < 2 || /sezione|sposta/i.test(text)) continue;
                    const idm = href.match(/[?&]id=(\\d+)/);
                    const rid = idm ? idm[1] : href;
                    if (seen.has(rid)) continue;
                    seen.add(rid);
                    res.push({
                        title: text,
                        url: href.startsWith('http') ? href : 'https://fad.its-ictpiemonte.it' + href,
                        id: rid,
                    });
                }
                if (res.length > 0 || qsa(sec, 'a[href*="mod/"]').length > 0) {
                    out.push({ id: secId, number: num, title: title, resources: res });
                }
            }
            return out;
        }
    """)


def download_resource(page, resource: dict, target_dir: pathlib.Path) -> bool:
    """Scarica una risorsa Moodle. Se il file esiste gia', lo salta."""
    title = resource["title"]
    url = resource["url"]

    # Fase 1: HEAD request per determinare filename senza scaricare il corpo
    try:
        head = page.evaluate("""
            async (url) => {
                try {
                    const r = await fetch(url, {
                        credentials: 'include', method: 'HEAD', redirect: 'follow'
                    });
                    if (!r.ok) return { error: 'HTTP ' + r.status };
                    const h = {};
                    r.headers.forEach((v, k) => { h[k.toLowerCase()] = v; });
                    return {
                        filename: h['content-disposition'] || '',
                        contentType: (h['content-type'] || '').split(';')[0].trim(),
                        size: parseInt(h['content-length'] || '0'),
                    };
                } catch (e) { return { error: e.message }; }
            }
        """, url)

        if "error" in head:
            print(f"    [ERR] {title}: HEAD fallito ({head['error']})")
            return False

        cd = head.get("filename", "")
        ctype = head.get("contentType", "")
        filename = extract_filename_from_cd(cd, title, ctype)
        file_path = target_dir / filename

        # Skip se gia' presente
        if file_path.exists():
            print(f"    [SKIP] {title} - file gia' presente")
            return True

    except Exception as e:
        print(f"    [ERR] {title}: HEAD exception ({e})")
        return False

    # Fase 2: download effettivo (solo se file mancante)
    print(f"    [DL] {title} ... ", end="", flush=True)
    try:
        result = page.evaluate("""
            async (url) => {
                try {
                    const r = await fetch(url, {
                        credentials: 'include', redirect: 'follow'
                    });
                    if (!r.ok) return { error: 'HTTP ' + r.status };
                    const blob = await r.blob();
                    return new Promise((res) => {
                        const reader = new FileReader();
                        reader.onload = () => {
                            const b64 = reader.result.split(',')[1];
                            res({ data: b64, size: blob.size });
                        };
                        reader.onerror = () => res({ error: 'FileReader error' });
                        reader.readAsDataURL(blob);
                    });
                } catch (e) { return { error: e.message }; }
            }
        """, url)

        if "error" in result:
            print(f"[ERR] {result['error']}")
            return False

        file_data = base64.b64decode(result["data"])

        with open(file_path, "wb") as f:
            f.write(file_data)

        size_kb = result["size"] / 1024
        print(f"[OK] ({size_kb:.1f} KB)")
        return True

    except Exception as e:
        print(f"[ERR] {e}")
        return False


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Moodle FAD Sync Tool - ITS ICT Piemonte"
    )
    parser.add_argument(
        "--store-creds", action="store_true",
        help="Migra credenziali da .env a Windows Credential Manager e esci"
    )
    parser.add_argument(
        "--creds", nargs=2, metavar=("USER", "PASS"),
        help="Salva credenziali (USER PASS) in Windows Credential Manager e esci"
    )
    parser.add_argument(
        "--no-keyring", action="store_true",
        help="Ignora Windows Credential Manager, usa solo .env"
    )
    args = parser.parse_args()

    print("+" + "=" * 58 + "+")
    print("|           Moodle FAD Sync Tool - ITS ICT Piemonte             |")
    print("+" + "=" * 58 + "+")
    print()

    if args.creds:
        u, p = args.creds
        if store_credentials(u, p):
            print("[OK] Credenziali salvate in Windows Credential Manager.")
            return 0
        return 1

    if args.store_creds:
        env_path = SCRIPT_DIR / ".env"
        u = p = ""
        if env_path.exists():
            load_dotenv(env_path)
            u = os.getenv("MOODLE_USERNAME", "").strip()
            p = os.getenv("MOODLE_PASSWORD", "")
        if not u or not p:
            print("[ERR] Usa: python tools/moodle-sync.py --creds USER PASSWORD")
            return 1
        if store_credentials(u, p):
            print("[OK] Credenziali migrate in Windows Credential Manager.")
            print("Puoi eliminare tools/.env se preferisci.")
            return 0
        return 1

    username, password = load_credentials(use_keyring=not args.no_keyring)
    print(f"  Utente: {username}")
    print(f"  Workspace: {WORKSPACE_ROOT.name}/")
    print(f"  Corsi mappati: {len(COURSE_MAP)}")
    print()

    with sync_playwright() as pw:
        browser = pw.chromium.launch(
            headless=True,
            args=["--disable-gpu", "--no-sandbox"],
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            locale="it-IT",
        )
        page = context.new_page()

        try:
            # ======================== LOGIN ========================
            print("[Login] ... ", end="", flush=True)
            page.goto(f"{BASE_URL}/login/index.php", wait_until="networkidle")
            page.fill("input[name=username]", username)
            page.fill("input[name=password]", password)
            page.click("button#loginbtn")
            page.wait_for_load_state("networkidle", timeout=20000)

            if "login" in page.url.lower():
                err = page.locator(".alert-danger").text_content(timeout=5000)
                print(f"[ERR] Login fallito: {err.strip() if err else 'credenziali?'}")
                return 1
            print("[OK]")

            # ======================== DASHBOARD ========================
            print("\n[Scan] Scansione dashboard corsi ...")
            all_courses = scrape_dashboard_courses(page)
            print(f"  Trovati {len(all_courses)} corsi sulla dashboard")

            # Filtra solo quelli mappati in COURSE_MAP
            mapped_courses = []
            for c in all_courses:
                code = c.get("code")
                if code and code in COURSE_MAP:
                    mapped_courses.append(c)

            if not mapped_courses:
                print("  Nessun corso mappato trovato.")
                print("  Verifica COURSE_MAP in moodle-sync.py")
                return 0

            print(f"  Corsi da sincronizzare: {len(mapped_courses)}")
            for c in mapped_courses:
                cfg = COURSE_MAP[c["code"]]
                print(f"    - {c['title']} -> {cfg['dir']}/")
            print()

            # ======================== DOWNLOAD ========================
            print("+" + "=" * 58 + "+")
            print("|                    DOWNLOAD MATERIALI                  |")
            print("+" + "=" * 58 + "+")
            print()

            grand_total = {"ok": 0, "err": 0}
            course_stats = {}

            for course in mapped_courses:
                code = course["code"]
                name_short = shorten_course_name(course["title"])
                cfg = COURSE_MAP[code]

                target_base = WORKSPACE_ROOT / cfg["dir"]
                materials_subdir = cfg.get("materials", "_FAD")
                target_dir = target_base / materials_subdir

                print(f"[{code}] {name_short}")
                print(f"  Cartella: {cfg['dir']}/{materials_subdir}/")
                target_dir.mkdir(parents=True, exist_ok=True)

                # Scopri sezioni e risorse
                sections = scrape_course_sections(page, course["url"])

                if not sections:
                    print("  [INFO] Nessuna sezione con risorse trovata.")
                    course_stats[code] = {"ok": 0, "err": 0}
                    print()
                    continue

                # Filtra solo sezioni con risorse scaricabili
                sections_with_resources = [
                    s for s in sections if s.get("resources")
                ]

                if not sections_with_resources:
                    print("  [INFO] Nessuna risorsa scaricabile trovata.")
                    course_stats[code] = {"ok": 0, "err": 0}
                    print()
                    continue

                ok = 0
                err = 0
                seen_ids = set()  # dedup globale tra sezioni

                for section in sections_with_resources:
                    sec_title = section["title"]
                    sec_num = section["number"]

                    if sec_num is not None:
                        subdir_name = f"{sec_num:02d}_{sanitize_filename(sec_title)}"
                    else:
                        subdir_name = sanitize_filename(sec_title)

                    subdir = target_dir / subdir_name
                    subdir.mkdir(parents=True, exist_ok=True)

                    # Filtra duplicati tra sezioni
                    res_list = []
                    for r in section["resources"]:
                        if r["id"] not in seen_ids:
                            seen_ids.add(r["id"])
                            res_list.append(r)

                    if not res_list:
                        continue

                    print(f"  [{subdir_name}] {len(res_list)} risorsa/e")

                    for res in res_list:
                        if download_resource(page, res, subdir):
                            ok += 1
                        else:
                            err += 1

                course_stats[code] = {"ok": ok, "err": err}
                grand_total["ok"] += ok
                grand_total["err"] += err

                # Scrivi README per questo corso
                summary_lines = [
                    f"# {course['title']}",
                    "",
                    f"*Sincronizzato il {datetime.now().strftime('%d/%m/%Y %H:%M')}*",
                    "",
                    "## Sezioni",
                    "",
                ]
                for section in sections:
                    sec_title = section["title"]
                    sec_num = section["number"]
                    if sec_num is not None:
                        sn = f"{sec_num:02d}"
                    else:
                        sn = "--"
                    res_count = len(section.get("resources", []))
                    other_info = ""
                    if section.get("other"):
                        types = set(m["type"] for m in section["other"])
                        other_info = f" [+{len(section['other'])} altro: {', '.join(sorted(types))}]"
                    summary_lines.append(
                        f"- **{sn} {sec_title}**: {res_count} file{other_info}"
                    )

                # Sezioni senza risorse ma con altri moduli
                sections_other = [s for s in sections
                                  if not s.get("resources") and s.get("other")]
                for section in sections_other:
                    sec_title = section["title"]
                    sec_num = section["number"]
                    if sec_num is not None:
                        sn = f"{sec_num:02d}"
                    else:
                        sn = "--"
                    types = set(m["type"] for m in section["other"])
                    summary_lines.append(
                        f"- **{sn} {sec_title}**: "
                        f"[solo {', '.join(sorted(types))} - non scaricabili]"
                    )

                summary_lines.extend([
                    "",
                    f"Totale: {ok} file scaricati, {err} errori",
                    "",
                    "---",
                    "*Generato da moodle-sync.py*",
                ])
                readme_path = target_dir / "README.md"
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(summary_lines))

                print(f"  [FILE] README.md creato")
                print()

            # ======================== REPORT FINALE ========================
            print("+" + "=" * 58 + "+")
            print("|                    Sincronizzazione completata           |")
            print("+" + "=" * 58 + "+")
            print(f"\n  Totale file scaricati: {grand_total['ok']}")
            if grand_total["err"]:
                print(f"  Errori: {grand_total['err']}")
            print()

            for code, stat in course_stats.items():
                name = next(
                    (c["title"] for c in mapped_courses if c["code"] == code),
                    code
                )
                dir_name = COURSE_MAP[code]["dir"]
                err_str = f", {stat['err']} err" if stat["err"] else ""
                print(f"  [{code}] {dir_name}/ -> {stat['ok']} file{err_str}")

            print("\n[OK] Done!")
            return 0

        except Exception as e:
            print(f"\n[ERR] ERRORE CRITICO: {e}")
            import traceback
            traceback.print_exc()
            return 1
        finally:
            browser.close()


if __name__ == "__main__":
    sys.exit(main())
