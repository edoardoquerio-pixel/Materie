#!/usr/bin/env python3
"""Scarica e organizza le risorse del Moodle ITS ICT Piemonte.

Flusso: configurazione ? login ? scoperta corsi/risorse ? download ? stato.
Il file ? diviso in sezioni ripiegabili nell'IDE. Le funzioni di supporto
non avviano richieste o download al momento dell'importazione.
Richiede Python 3.10+; installazione e utilizzo sono descritti in tool/README.md.
"""
import argparse
from collections import Counter
from contextlib import contextmanager, nullcontext
from datetime import datetime, timezone
from email.message import Message
from getpass import getpass
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import parse_qs, parse_qsl, unquote, urlencode, urljoin, urlsplit, urlunsplit

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# ============================================================================
# region 1. Configurazione e regole predefinite
# ============================================================================

BASE_URL = "https://fad.its-ictpiemonte.it"
LOGIN_URL = f"{BASE_URL}/login/index.php"
DASHBOARD_URL = f"{BASE_URL}/my/"
BASE_DIR = Path(__file__).resolve().parent.parent
STATE_FILE = BASE_DIR / ".fad_state.json"
MAPPING_FILE = BASE_DIR / ".fad_mapping.json"
DOTENV_FILE = BASE_DIR / "tool" / ".env"
HEADERS = {"User-Agent": "FADDownloader/2.0", "Accept-Language": "it-IT,it;q=0.9"}
log = logging.getLogger("fad")
DEFAULT_MAPPING = {
    "materiale condiviso":"00_Amministrazione_Corso","cartella del partecipante":"00_Amministrazione_Corso",
    "erasmus":"00_Amministrazione_Corso","selezione studenti":"00_Amministrazione_Corso",
    "inglese":"01_Inglese_Tecnico",
    "learning by project - soft skill":"02_Orientamento_e_Soft_Skills","percorso di sviluppo soft skills":"02_Orientamento_e_Soft_Skills",
    "orientamento al lavoro":"02_Orientamento_e_Soft_Skills","approfondimenti didattici":"02_Orientamento_e_Soft_Skills",
    "parit?":"03_Parita_e_Non_Discriminazione","parita":"03_Parita_e_Non_Discriminazione","copyright e norme giuridiche":"03_Parita_e_Non_Discriminazione",
    "sicurezza sul lavoro":"04_Sicurezza_sul_Lavoro",
    "sicurezza informatica":"06_Reti_e_Sicurezza_Informatica",
    "fondamenti di reti":"06_Reti_e_Sicurezza_Informatica",
    "fondamenti di version control":"07_Version_Control_Git",
    "fondamenti di basi di dati":"08_Basi_di_Dati_SQL_NoSQL",
    "fondamenti di programmazione":"09_Programmazione_C_CPP",
    "python":"10_Programmazione_Python",
    ".net":"11_Programmazione_DotNet_CSharp","framework c#":"11_Programmazione_DotNet_CSharp",
    "rest":"12_RESTful_API",
    "aws":"13_Cloud_AWS","amazon web services":"13_Cloud_AWS",
    "azure":"14_Cloud_Azure","microsoft azure":"14_Cloud_Azure",
    "gcp":"15_Cloud_GCP","google cloud":"15_Cloud_GCP",
    "linux server":"16_Linux_Server_e_Amministrazione",
    "container":"17_Container_Docker_Kubernetes","microservizi":"17_Container_Docker_Kubernetes",
    "microsoft 365":"18_Microsoft_365_SharePoint","sharepoint":"18_Microsoft_365_SharePoint",
    "virtualizzazione":"19_Virtualizzazione",
    "data analytics":"20_Data_Analytics_Visualization",
    "iot":"21_Internet_of_Things","internet of things":"21_Internet_of_Things",
    "strumenti ai":"22_AI_e_Prompt_Engineering","prompt engineering":"22_AI_e_Prompt_Engineering",
    "learning by project - tech":"23_Project_Work_e_Laboratori","laboratorio di preparazione project work":"23_Project_Work_e_Laboratori",
}

SUPPORTED = {"resource", "folder", "page", "book", "file", "page_file"}


# endregion

# ============================================================================
# region 2. Errori e client HTTP
# ============================================================================

class FadError(Exception):
    """Errore di download o autenticazione da mostrare all?utente."""


class Client(requests.Session):
    """Sessione HTTP condivisa: timeout, connessioni riutilizzate e retry dei GET."""
    def __init__(self, timeout: float = 60, retries: int = 3):
        super().__init__()
        self.timeout = timeout
        self.headers.update(HEADERS)
        self.sesskey = None
        self.unavailable = set()
        retry = Retry(total=retries, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504),
                      allowed_methods=frozenset({"GET", "HEAD"}), respect_retry_after_header=True)
        self.mount("https://", HTTPAdapter(max_retries=retry))

    def request(self, method, url, **kwargs):
        kwargs.setdefault("timeout", (min(15, self.timeout), self.timeout))
        log.debug("HTTP %s %s", method, urlsplit(url).path)
        return super().request(method, url, **kwargs)


# endregion

# ============================================================================
# region 3. Nomi, URL e scrittura sicura
# ============================================================================

def sanitize_filename(name: str) -> str:
    """Rende un nome utilizzabile su Windows e ne limita la lunghezza."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f\x7f]', "_", name).strip().strip(". ") or "unnamed"
    if re.match(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\.|$)", name, re.I):
        name = "_" + name
    if len(name) > 140:
        suffix = Path(name).suffix[:20]
        name = name[:120] + "_" + hashlib.sha256(name.encode()).hexdigest()[:8] + suffix
    return name


def extract_filename_from_cd(headers, default: str) -> str:
    """Legge il nome dell?allegato rispettando la codifica di Content-Disposition."""
    message = Message()
    message["Content-Disposition"] = headers.get("Content-Disposition", "")
    return message.get_filename() or default


def canonical_url(url: str) -> str:
    """Crea un?identit? stabile senza token temporanei; non modifica l?URL richiesto."""
    parts = urlsplit(url)
    query = sorted((k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
                   if k.casefold() not in {"token", "sesskey", "forcedownload"})
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path, urlencode(query), ""))


def safe_path(root: Path, relative: str) -> Path:
    # Controlla entrambi i separatori anche se i test girano su un altro sistema.
    """Valida un percorso relativo e impedisce scritture fuori dalla directory prevista."""
    if not relative or re.match(r"^[A-Za-z]:", relative) or relative.startswith(("/", "\\")):
        raise FadError(f"Percorso non relativo: {relative!r}")
    parts = relative.replace("\\", "/").split("/")
    if any(part in {"", ".", ".."} or sanitize_filename(part) != part for part in parts):
        raise FadError(f"Percorso non valido: {relative!r}")
    path = root.joinpath(*parts).resolve()
    if not path.is_relative_to(root.resolve()):
        raise FadError("Destinazione esterna alla directory di output")
    return path


def atomic_write(path: Path, data: bytes) -> None:
    """Scrive in un temporaneo e sostituisce la destinazione solo a scrittura completata."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
            temp = Path(handle.name)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if temp is not None:
            temp.unlink(missing_ok=True)


def file_hash(path: Path) -> str:
    """Calcola SHA-256 a blocchi, senza caricare tutto il file in memoria."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


# endregion

# ============================================================================
# region 4. Stato persistente e lock
# ============================================================================

class DownloadState:
    """Registro persistente dei file verificati e contatori della singola esecuzione."""
    def __init__(self, state_file: Path, root: Path = BASE_DIR):
        self.state_file = state_file
        self.root = root.resolve()
        self.downloaded = {}
        self.stats = Counter()
        if state_file.exists():
            try:
                data = json.loads(state_file.read_text(encoding="utf-8"))
                if not isinstance(data, dict) or data.get("version") not in (1, 2):
                    raise ValueError("Versione dello stato non supportata")
                records = data.get("downloaded")
                if not isinstance(records, dict):
                    raise ValueError("downloaded deve essere un oggetto")
                # Lo stato v1 non ha hash: richiede una nuova verifica tramite download.
                if data["version"] == 2:
                    for key, record in records.items():
                        if not isinstance(key, str) or not isinstance(record, dict):
                            raise ValueError("Record non valido")
                        if not isinstance(record.get("size"), int) or record["size"] < 0:
                            raise ValueError("Dimensione non valida")
                        if not re.fullmatch(r"[0-9a-f]{64}", str(record.get("sha256", ""))):
                            raise ValueError("Hash non valido")
                        safe_path(self.root, record["path"])
                    self.downloaded = records
                else:
                    log.info("Stato v1: i file saranno verificati nuovamente")
            except (OSError, ValueError, KeyError, TypeError, FadError) as exc:
                raise FadError(f"Stato non valido ({state_file}): {exc}") from exc

        self.owned_paths = {
            str(safe_path(self.root, record["path"])).casefold()
            for record in self.downloaded.values()
        }

    def key(self, identity: str) -> str:
        """Trasforma l?identit? della risorsa nella chiave del registro."""
        return hashlib.sha256(identity.encode()).hexdigest()

    def record(self, identity: str):
        """Restituisce i metadati registrati oppure None."""
        return self.downloaded.get(self.key(identity))

    def valid(self, identity: str) -> bool:
        """Verifica esistenza, dimensione e hash della copia locale."""
        record = self.record(identity)
        if not record:
            return False
        try:
            path = safe_path(self.root, record["path"])
            return path.is_file() and path.stat().st_size == record["size"] and file_hash(path) == record["sha256"]
        except OSError:
            return False

    def mark(self, identity: str, path: Path, headers=None, deps=None, *, size=None, sha256=None):
        """Registra un file completato e salva un checkpoint atomico.

        size e sha256 possono essere passati dal downloader per evitare
        una seconda lettura del file appena trasferito."""
        headers = headers or {}
        self.downloaded[self.key(identity)] = {
            "path": str(path.resolve().relative_to(self.root)).replace("\\", "/"),
            "size": path.stat().st_size if size is None else size,
            "sha256": file_hash(path) if sha256 is None else sha256,
            "etag": headers.get("ETag"), "modified": headers.get("Last-Modified"),
            "downloaded_at": datetime.now(timezone.utc).isoformat(), "dependencies": deps or [],
        }
        self.owned_paths.add(str(path.resolve()).casefold())
        self.save()

    def save(self):
        """Salva il registro v2 senza lasciare JSON parziali."""
        atomic_write(self.state_file, json.dumps({"version": 2, "downloaded": self.downloaded},
                                                indent=2, ensure_ascii=False).encode("utf-8"))


@contextmanager
def run_lock(path: Path):
    """Impedisce esecuzioni concorrenti e rimuove il lock anche in caso di errore."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise FadError(f"Esecuzione già attiva o lock residuo: {path}. Rimuovilo solo dopo aver verificato che nessun downloader sia attivo.") from exc
    try:
        with os.fdopen(descriptor, "w") as handle:
            handle.write(str(os.getpid()))
        yield
    finally:
        path.unlink(missing_ok=True)


# endregion

# ============================================================================
# region 5. Autenticazione e API Moodle
# ============================================================================

def check_response(response):
    """Rifiuta errori HTTP e redirect alla pagina di autenticazione."""
    response.raise_for_status()
    if urlsplit(response.url).path.rstrip("/") == "/login/index.php":
        raise FadError("Sessione scaduta o autenticazione richiesta")


def html_soup(session, url):
    """Recupera HTML autenticato e restituisce DOM e URL finale dopo i redirect."""
    with session.get(url) as response:
        check_response(response)
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.select_one('input[name="logintoken"]') or soup.select_one('.errorbox, [data-rel="fatalerror"]'):
            raise FadError("Pagina di login o errore Moodle ricevuto")
        return soup, response.url


def login(session, username, password):
    """Invia le credenziali con il token CSRF e verifica la dashboard autenticata."""
    with session.get(LOGIN_URL) as response:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        token = soup.find("input", attrs={"name": "logintoken"})
        if not token or not token.get("value"):
            raise FadError("Token di login non trovato")
    with session.post(LOGIN_URL, data={"username": username, "password": password,
                      "logintoken": token["value"], "anchor": ""}, headers={"Referer": LOGIN_URL}) as response:
        check_response(response)
    soup, _ = html_soup(session, DASHBOARD_URL)
    if not soup.select_one('a[href*="/login/logout.php"], body#page-my-index'):
        raise FadError("Impossibile confermare il login")
    log.info("Login riuscito")
    return True


def login_diagnose(session, username, password):
    """Controlla connettivit? e login senza esporre i valori dei cookie."""
    with session.get(BASE_URL) as response:
        response.raise_for_status()
        print(f"Homepage: HTTP {response.status_code}; cookie presenti: {', '.join(session.cookies.keys())}")
    return login(session, username, password)


def get_sesskey(session):
    """Recupera il token AJAX e lo conserva per la durata della sessione."""
    if session.sesskey:
        return session.sesskey
    for url in (DASHBOARD_URL, BASE_URL):
        soup, _ = html_soup(session, url)
        match = re.search(r'["\']?sesskey["\']?\s*:\s*["\']([^"\']+)', str(soup))
        if match:
            session.sesskey = match.group(1)
            return session.sesskey
    return None


def call_ajax(session, method, args):
    """Invoca un metodo Moodle; restituisce None quando serve il fallback HTML."""
    if method in session.unavailable:
        return None
    key = get_sesskey(session)
    if not key:
        log.debug("Sesskey non disponibile; uso HTML")
        return None
    try:
        with session.post(f"{BASE_URL}/lib/ajax/service.php", params={"sesskey": key},
                          json=[{"index": 0, "methodname": method, "args": args}]) as response:
            check_response(response)
            data = response.json()
        if not isinstance(data, list) or not data or not isinstance(data[0], dict):
            raise ValueError("Risposta AJAX non valida")
        if data[0].get("error"):
            error = data[0].get("exception", {})
            code = data[0].get("errorcode") or (error.get("errorcode", "") if isinstance(error, dict) else "")
            if code in {"servicenotavailable", "invalidrecord", "invalidfunction", "accessdenied"}:
                session.unavailable.add(method)
            log.debug("AJAX %s: %s", method, code or "errore")
            return None
        return data[0].get("data")
    except (requests.RequestException, ValueError) as exc:
        log.warning("AJAX %s non disponibile: %s", method, type(exc).__name__)
        return None


# endregion

# ============================================================================
# region 6. Scoperta di corsi e risorse
# ============================================================================

def get_enrolled_courses(session):
    """Unisce corsi API paginati e link della dashboard, deduplicandoli per ID."""
    courses = {}
    offset = 0
    while True:
        data = call_ajax(session, "core_course_get_enrolled_courses_by_timeline_classification",
                         {"offset": offset, "limit": 100, "classification": "all", "sort": "fullname"})
        if not isinstance(data, dict) or not isinstance(data.get("courses"), list):
            break
        batch = data["courses"]
        before = len(courses)
        for course in batch:
            cid = int(course["id"])
            courses[cid] = {"id": cid, "fullname": course.get("fullname", str(cid)),
                            "url": f"{BASE_URL}/course/view.php?id={cid}"}
        if len(batch) < 100 or len(courses) == before:
            break
        offset += len(batch)
    soup, final_url = html_soup(session, DASHBOARD_URL)
    for anchor in soup.select("a[href]"):
        url = urljoin(final_url, anchor["href"])
        parts = urlsplit(url)
        cid = parse_qs(parts.query).get("id", [""])[0]
        if parts.path == "/course/view.php" and cid.isdigit():
            courses.setdefault(int(cid), {"id": int(cid), "fullname": anchor.get_text(" ", strip=True) or cid, "url": url})
    return list(courses.values())


def folder_relative(url):
    """Estrae le sottocartelle da un URL mod_folder, escludendo revisione e nome file."""
    path = unquote(urlsplit(url).path)
    marker = "/mod_folder/content/"
    if marker not in path:
        return ""
    segments = path.split(marker, 1)[1].split("/")
    # Il primo segmento ? la revisione Moodle; l?ultimo ? il nome del file.
    return "/".join(sanitize_filename(p) for p in segments[1:-1] if p)


def plugin_files(soup, base):
    """Raccoglie i link pluginfile e li deduplica per URL stabile."""
    files = {}
    for anchor in soup.select("a[href]"):
        url = urljoin(base, anchor["href"])
        if "/pluginfile.php/" in urlsplit(url).path:
            files[canonical_url(url)] = {"url": url, "name": unquote(urlsplit(url).path.rsplit("/", 1)[-1]) or "file",
                "filepath": folder_relative(url)}
    return list(files.values())


def get_course_resources(session, course):
    """Unisce risorse API e HTML senza trattare pagine e cartelle come file diretti."""
    resources = []
    covered = set()
    data = call_ajax(session, "core_course_get_contents", {"courseid": course["id"], "options": []})
    if isinstance(data, list):
        for section in data:
            for mod in section.get("modules", []):
                common = {"id": int(mod["id"]), "name": mod.get("name", "risorsa"), "type": mod.get("modname", ""),
                          "url": mod.get("url", ""), "section": section.get("name", "")}
                contents = [c for c in mod.get("contents", []) if c.get("fileurl") and c.get("filename")]
                if common["type"] in {"resource", "folder"} and contents:
                    for item in contents:
                        resources.append({**common, "activity_name": common["name"], "name": item["filename"], "download_url": item["fileurl"],
                                          "filepath": item.get("filepath", "/"), "filesize": item.get("filesize")})
                    covered.add(int(mod["id"]))
                elif common["type"] in {"page", "book"}:
                    resources.append(common)
                    covered.add(int(mod["id"]))
    soup, base = html_soup(session, course["url"])
    for anchor in soup.select("a[href]"):
        url = urljoin(base, anchor["href"])
        parts = urlsplit(url)
        match = re.fullmatch(r"/mod/(\w+)/view\.php", parts.path)
        cid = parse_qs(parts.query).get("id", [""])[0]
        if not match or not cid.isdigit() or int(cid) in covered:
            continue
        covered.add(int(cid))
        section = anchor.find_parent(attrs={"data-sectionid": True}) or anchor.find_parent("li", class_="section")
        heading = section.find(["h2", "h3"]) if section else None
        resources.append({"id": int(cid), "type": match[1], "name": anchor.get_text(" ", strip=True) or f"attività_{cid}",
                          "url": url, "section": heading.get_text(" ", strip=True) if heading else ""})
    for item in plugin_files(soup, base):
        resources.append({"id": 0, "type": "file", "name": item["name"], "url": item["url"],
                          "download_url": item["url"], "section": ""})
    unique = {}
    for resource in resources:
        key = canonical_url(resource.get("download_url") or resource["url"])
        unique.setdefault(key, resource)
    return list(unique.values())


# endregion

# ============================================================================
# region 7. Download, collisioni ed esportazione HTML
# ============================================================================

def collision_path(path: Path, identity: str, state: DownloadState) -> Path:
    """Riusa il percorso della risorsa o assegna un suffisso senza sovrascrivere file estranei."""
    record = state.record(identity)
    if record:
        stored = safe_path(state.root, record["path"])
        if stored.parent == path.parent:
            return stored
    owned = state.owned_paths
    if path.exists() or str(path.resolve()).casefold() in owned:
        suffix = hashlib.sha256(identity.encode()).hexdigest()[:12]
        path = path.with_name(f"{path.stem}_{suffix}{path.suffix}")
        if path.exists() or str(path.resolve()).casefold() in owned:
            raise FadError(f"Collisione con file non associato: {path}")
    return path


def download_file(session, url, dest_path, state, force=False, *, identity=None, expected_size=None, allow_html=False, response=None):
    """Scarica un file in streaming, lo verifica e aggiorna subito lo stato.

    Se response ? fornita, il chiamante ne gestisce la chiusura: questo evita
    una seconda richiesta dopo la scoperta di una risorsa diretta.
    L?hash e la dimensione calcolati durante il trasferimento vengono riusati.
    Restituisce il percorso locale; propaga gli errori al gestore dell?attivit?."""
    identity = identity or canonical_url(url)
    identity = f"{dest_path.parent.resolve().relative_to(state.root)}:{identity}"
    record = state.record(identity)
    valid = not force and state.valid(identity)
    # I validatori HTTP sono utilizzabili solo se la copia locale ? integra.
    headers = {}
    if valid and not force and record:
        if record.get("etag"):
            headers["If-None-Match"] = record["etag"]
        elif record.get("modified"):
            headers["If-Modified-Since"] = record["modified"]
    temp = None
    try:
        # La risposta di scoperta viene chiusa dal chiamante che l?ha aperta.
        response_context = nullcontext(response) if response is not None else session.get(url, headers=headers, stream=True)
        with response_context as response:
            if response.status_code == 304:
                if not valid:
                    raise FadError("HTTP 304 senza copia locale valida")
                state.stats["presenti"] += 1
                return safe_path(state.root, record["path"])
            check_response(response)
            name = dest_path.name if ":asset:" in identity else sanitize_filename(extract_filename_from_cd(response.headers, dest_path.name))
            dest = collision_path(dest_path.with_name(name), identity, state)
            dest.parent.mkdir(parents=True, exist_ok=True)
            digest = hashlib.sha256()
            size = 0
            prefix = bytearray()
            with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False) as handle:
                temp = Path(handle.name)
                for chunk in response.iter_content(256 * 1024):
                    if not chunk:
                        continue
                    if len(prefix) < 16384:
                        prefix.extend(chunk[:16384 - len(prefix)])
                    digest.update(chunk)
                    size += len(chunk)
                    handle.write(chunk)
                handle.flush()
                os.fsync(handle.fileno())
            sample = bytes(prefix).lower().lstrip()
            html = "html" in response.headers.get("Content-Type", "").lower() or sample.startswith((b"<!doctype html", b"<html"))
            if html:
                if b'logintoken' in sample or b'page-login-index' in sample or b'class="errorbox' in sample:
                    raise FadError("Pagina di login/errore ricevuta al posto del file")
                if not allow_html:
                    raise FadError("HTML inatteso al posto del file")
            if expected_size is not None and size != expected_size:
                raise FadError(f"Dimensione errata: {size}, attesa {expected_size}")
            length = response.headers.get("Content-Length")
            if length and not response.headers.get("Content-Encoding") and size != int(length):
                raise FadError("Trasferimento incompleto")
            if valid and record["sha256"] == digest.hexdigest() and not force:
                state.mark(identity, safe_path(state.root, record["path"]), response.headers,
                           size=size, sha256=digest.hexdigest())
                state.stats["presenti"] += 1
                return safe_path(state.root, record["path"])
            # Il file definitivo cambia soltanto dopo tutti i controlli.
            os.replace(temp, dest)
            state.mark(identity, dest, response.headers, size=size, sha256=digest.hexdigest())
            state.stats["aggiornati" if record else "scaricati"] += 1
            log.info("[OK] %s (%s byte)", dest.name, size)
            return dest
    finally:
        if temp:
            temp.unlink(missing_ok=True)


def export_html(session, act, directory, state, force):
    """Esporta pagina/libro e allegati pluginfile, riscrivendo i riferimenti locali."""
    url = act["url"]
    if act["type"] == "book":
        parts = urlsplit(url)
        params = parse_qs(parts.query)
        url = urlunsplit((parts.scheme, parts.netloc, "/mod/book/tool/print/index.php",
                         urlencode({"id": params["id"][0]}), ""))
    soup, final = html_soup(session, url)
    if act["type"] == "book":
        nodes = soup.select(".book_content")
    else:
        nodes = soup.select(".activity-description .no-overflow, #region-main .generalbox .no-overflow, .resourcecontent")
    if not nodes:
        raise FadError(f"Contenuto {act['type']} non trovato")
    document = BeautifulSoup('<!doctype html><html><head><meta charset="utf-8"></head><body></body></html>', "html.parser")
    title = document.new_tag("title")
    title.string = act["name"]
    document.head.append(title)
    for node in nodes:
        document.body.append(node)
    deps = []
    assets = {}
    for tag in document.select("[src], a[href], [poster], object[data]"):
        attr = next((a for a in ("src", "poster", "data", "href") if tag.has_attr(a)), None)
        raw = tag[attr]
        if raw.startswith(("data:", "#", "mailto:", "javascript:")):
            continue
        absolute = urljoin(final, raw)
        if urlsplit(absolute).scheme not in {"http", "https"}:
            continue
        if "/pluginfile.php/" in urlsplit(absolute).path:
            key = canonical_url(absolute)
            if key not in assets:
                filename = sanitize_filename(unquote(urlsplit(absolute).path.rsplit("/", 1)[-1]))
                filename = f"{hashlib.sha256(key.encode()).hexdigest()[:12]}_{filename}"
                asset_id = f"asset:{canonical_url(act['url'])}:{key}"
                assets[key] = download_file(session, absolute, directory / "assets" / filename, state, force,
                                             identity=asset_id, allow_html=Path(filename).suffix.lower() in {".html", ".htm"})
                deps.append(asset_id)
            tag[attr] = os.path.relpath(assets[key], directory).replace("\\", "/")
        else:
            tag[attr] = absolute
    # Evita varianti di immagini che mantengono riferimenti al server Moodle.
    for tag in document.select("[srcset]"):
        del tag["srcset"]
    identity = f"{directory.resolve().relative_to(state.root)}:html:{canonical_url(act['url'])}"
    content = str(document).encode("utf-8")
    path = collision_path(directory / "index.html", identity, state)
    content_hash = hashlib.sha256(content).hexdigest()
    old = state.record(identity)
    unchanged = not force and state.valid(identity) and old["sha256"] == content_hash
    if not unchanged or force:
        atomic_write(path, content)
    state.mark(identity, path, deps=deps, size=len(content), sha256=content_hash)
    state.stats["presenti" if unchanged and not force else "aggiornati" if old else "scaricati"] += 1


def activity_dir(dest, act):
    """Costruisce la destinazione organizzata per sezione e ID dell?attivit?."""
    if act.get("section"):
        dest = dest / sanitize_filename(act["section"])
    if act.get("id"):
        dest = dest / f"{act['id']}_{sanitize_filename(act.get('activity_name', act['name']))}"
    return dest


def download_activity(session, act, dest_dir, state, force=False):
    """Seleziona il gestore del tipo di attivit? e conta i tipi non supportati."""
    if act["type"] not in SUPPORTED:
        state.stats["non_supportati"] += 1
        log.warning("Tipo non supportato: %s (%s)", act["type"], act["name"])
        return
    directory = activity_dir(dest_dir, act)
    if act.get("download_url"):
        relative = act.get("filepath", "/").strip("/")
        if relative:
            directory = safe_path(directory, relative)
        download_file(session, act["download_url"], directory / sanitize_filename(act["name"]), state, force,
                      expected_size=act.get("filesize"), allow_html=Path(act["name"]).suffix.lower() in {".html", ".htm"})
    elif act["type"] in {"page", "book"}:
        export_html(session, act, directory, state, force)
    elif act["type"] in {"folder", "resource"}:
        with session.get(act["url"], stream=True) as response:
            check_response(response)
            is_html = "html" in response.headers.get("Content-Type", "").lower()
            if not is_html:
                download_file(session, response.url, directory / sanitize_filename(act["name"]), state, force,
                              identity=canonical_url(act["url"]), response=response)
                return
            soup = BeautifulSoup(response.text, "html.parser")
            direct = response.url
            if soup.select_one('input[name="logintoken"], .errorbox'):
                raise FadError("Login o errore durante la scoperta della risorsa")
        files = plugin_files(soup, direct)
        if not files:
            raise FadError("Nessun file trovato nell'attività")
        for item in files:
            try:
                file_dir = safe_path(directory, item["filepath"]) if item.get("filepath") else directory
                download_file(session, item["url"], file_dir / sanitize_filename(item["name"]), state, force,
                              allow_html=Path(item["name"]).suffix.lower() in {".html", ".htm"})
            except (requests.RequestException, OSError, ValueError, FadError) as exc:
                state.stats["falliti"] += 1
                log.error("%s: %s", item["name"], exc)


# endregion

# ============================================================================
# region 8. Associazione dei corsi alle cartelle
# ============================================================================

def map_course(course_name: str, mapping, course_id=None):
    """Applica prima ID e titolo esatto, poi le regole testuali pi? specifiche."""
    if course_id is not None and f"id:{course_id}" in mapping:
        return mapping[f"id:{course_id}"]
    name = course_name.casefold().strip()
    rules = [(k.casefold().strip(), v) for k, v in mapping.items() if not k.startswith("id:")]
    for pattern, folder in rules:
        if pattern == name:
            return folder
    for pattern, folder in sorted(rules, key=lambda pair: len(pair[0]), reverse=True):
        if re.search(r"(?<!\w)" + re.escape(pattern) + r"(?!\w)", name):
            return folder
    return f"ZZ_{sanitize_filename(course_name).replace(' ', '_')[:80]}"


def get_mapping(mapping_file, root=BASE_DIR):
    """Integra le regole personalizzate e valida tutte le destinazioni."""
    data = DEFAULT_MAPPING.copy()
    if mapping_file.exists():
        try:
            custom = json.loads(mapping_file.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise FadError(f"Mapping non leggibile: {exc}") from exc
        if not isinstance(custom, dict) or any(not isinstance(k, str) or not k.strip() or not isinstance(v, str) for k, v in custom.items()):
            raise FadError("Il mapping deve essere un oggetto con chiavi e valori stringa non vuoti")
        data.update(custom)
    for folder in data.values():
        safe_path(root, folder)
    return data


def gen_mapping(session, mapping_file, root=BASE_DIR):
    """Conserva le associazioni esistenti e chiede solo quelle mancanti."""
    mapping = get_mapping(mapping_file, root)
    for course in get_enrolled_courses(session):
        key = f"id:{course['id']}"
        if key in mapping or any(k.casefold() == course["fullname"].casefold() for k in mapping):
            continue
        suggested = map_course(course["fullname"], mapping)
        answer = input(f"{course['fullname']} — cartella [{suggested}]: ").strip() or suggested
        safe_path(root, answer)
        mapping[key] = answer
    atomic_write(mapping_file, json.dumps(mapping, indent=2, ensure_ascii=False).encode("utf-8"))


# endregion

# ============================================================================
# region 9. Interfaccia CLI e coordinamento
# ============================================================================

def positive(value):
    """Validatore argparse per valori numerici strettamente positivi."""
    number = float(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("Deve essere positivo")
    return number


def build_parser() -> argparse.ArgumentParser:
    """Definisce opzioni e modalit? mutuamente esclusive della riga di comando."""
    parser = argparse.ArgumentParser(description="FAD Downloader - ITS ICT Piemonte")
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password", help="Compatibilità: preferire il prompt o FAD_PASSWORD")
    parser.add_argument("-c", "--course", help="Parte del nome del corso")
    parser.add_argument("--course-id", type=int)
    parser.add_argument("-f", "--force", action="store_true")
    modes = parser.add_mutually_exclusive_group()
    for option in ("dry-run", "show-mapping", "update-mapping", "login-diagnose"):
        modes.add_argument("--" + option, *(["-n"] if option == "dry-run" else []), action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=BASE_DIR)
    parser.add_argument("--state-file", type=Path)
    parser.add_argument("--mapping-file", type=Path, default=MAPPING_FILE)
    parser.add_argument("--env-file", type=Path, default=DOTENV_FILE)
    parser.add_argument("--timeout", type=positive, default=60)
    parser.add_argument("--retries", type=int, choices=range(0, 11), default=3)
    return parser


def main(argv=None):
    """Coordina configurazione, autenticazione e download; restituisce il codice di uscita."""
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    root = args.output_dir.resolve()
    state_file = args.state_file or root / ".fad_state.json"
    try:
        mapping = get_mapping(args.mapping_file, root)
        if args.show_mapping:
            for key, value in sorted(mapping.items()):
                print(f'"{key}" -> {value}')
            return 0
        # Precedenza credenziali: argomenti CLI, ambiente/.env, prompt.
        load_dotenv(args.env_file, override=False)
        username = args.username or os.environ.get("FAD_USERNAME") or input("Username: ").strip()
        password = args.password or os.environ.get("FAD_PASSWORD") or getpass("Password: ")
        if not username or not password:
            raise FadError("Username e password richiesti")
        with Client(args.timeout, args.retries) as session:
            if args.login_diagnose:
                login_diagnose(session, username, password)
                return 0
            login(session, username, password)
            if args.update_mapping:
                with run_lock(args.mapping_file.with_suffix(".json.lock")):
                    gen_mapping(session, args.mapping_file, root)
                return 0
            courses = get_enrolled_courses(session)
            courses = [c for c in courses if (not args.course or args.course.casefold() in c["fullname"].casefold())
                       and (args.course_id is None or c["id"] == args.course_id)]
            if not courses:
                raise FadError("Nessun corso corrispondente")
            # Il lock copre sia i file scaricati sia gli aggiornamenti dello stato.
            with run_lock(root / ".fad_download.lock"):
                state = DownloadState(state_file, root)
                for course in courses:
                    folder = map_course(course["fullname"], mapping, course["id"])
                    dest = safe_path(root, folder) / "01_Materiale"
                    log.info("Corso %s: %s -> %s", course["id"], course["fullname"], dest)
                    try:
                        resources = get_course_resources(session, course)
                    except (requests.RequestException, OSError, ValueError, KeyError, FadError) as exc:
                        log.error("Scoperta risorse fallita: %s", exc)
                        state.stats["falliti"] += 1
                        continue
                    for act in resources:
                        if args.dry_run:
                            identity = canonical_url(act.get("download_url") or act["url"])
                            planned = activity_dir(dest, act)
                            relative = act.get("filepath", "/").strip("/")
                            if relative:
                                planned = safe_path(planned, relative)
                            identity = f"{planned.resolve().relative_to(state.root)}:{identity}"
                            action = "non supportato" if act["type"] not in SUPPORTED else "verifica aggiornamento" if state.valid(identity) else "scarica/esporta"
                            print(f"[{act['type']}] {act['name']} -> {activity_dir(dest, act)} ({action}; nomi finali verificati durante il download)")
                            continue
                        try:
                            download_activity(session, act, dest, state, args.force)
                        except (requests.RequestException, OSError, ValueError, KeyError, FadError) as exc:
                            state.stats["falliti"] += 1
                            log.error("%s: %s", act["name"], exc, exc_info=args.debug)
                print("DRY RUN" if args.dry_run else "Risultato", " | ".join(f"{k}: {state.stats[k]}" for k in
                      ("scaricati", "presenti", "aggiornati", "falliti", "non_supportati")))
                return 1 if state.stats["falliti"] else 0
    except KeyboardInterrupt:
        log.warning("Interrotto: i download completati sono già salvati")
        return 130
    except (requests.RequestException, OSError, ValueError, FadError) as exc:
        log.error("%s", exc, exc_info=args.debug)
        return 1


# endregion


# Avvia il programma solo quando il file viene eseguito direttamente.
if __name__ == "__main__":
    sys.exit(main())
