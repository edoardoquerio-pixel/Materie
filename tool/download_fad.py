#!/usr/bin/env python3
"""FAD Downloader - ITS ICT Piemonte Moodle Downloader"""
import argparse, hashlib, json, logging, os, re, sys
from getpass import getpass
from pathlib import Path
from urllib.parse import urljoin, unquote
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fad.its-ictpiemonte.it"
LOGIN_URL = f"{BASE_URL}/login/index.php"
DASHBOARD_URL = f"{BASE_URL}/my/"
BASE_DIR = Path(__file__).parent.parent.resolve()
STATE_FILE = BASE_DIR / ".fad_state.json"
MAPPING_FILE = BASE_DIR / ".fad_mapping.json"
DOTENV_FILE = BASE_DIR / "tool" / ".env"
MIN_VALID_FILE_SIZE = 1024
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/125.0.0.0 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7"}
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("fad")

def load_dotenv(path: Path):
    if not path.exists(): return
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line: continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip("\"'")
            if k and v: os.environ.setdefault(k, v)
    except OSError: pass

DEFAULT_MAPPING = {
    "materiale condiviso":"00_Amministrazione_Corso","cartella del partecipante":"00_Amministrazione_Corso",
    "erasmus":"00_Amministrazione_Corso","selezione studenti":"00_Amministrazione_Corso",
    "inglese":"01_Inglese_Tecnico",
    "learning by project - soft skill":"02_Orientamento_e_Soft_Skills","percorso di sviluppo soft skills":"02_Orientamento_e_Soft_Skills",
    "orientamento al lavoro":"02_Orientamento_e_Soft_Skills","approfondimenti didattici":"02_Orientamento_e_Soft_Skills",
    "parit":"03_Parita_e_Non_Discriminazione","copyright e norme giuridiche":"03_Parita_e_Non_Discriminazione",
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

def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "_", name); return name.strip().strip("._") or "unnamed"

def extract_filename_from_cd(headers, default: str) -> str:
    cd = headers.get("Content-Disposition", "")
    m = re.search(r"filename\*=(?:UTF-8|ISO-8859-1)''([^;]+)", cd, re.I)
    if m: return unquote(m.group(1))
    m = re.search(r'filename="([^"]*)"', cd, re.I)
    if m: return m.group(1)
    m = re.search(r"filename=([^;]+)", cd, re.I)
    if m: return m.group(1).strip()
    return default

class DownloadState:
    def __init__(self, state_file: Path):
        self.state_file = state_file; self.downloaded: dict[str, str] = {}
        if state_file.exists():
            try:
                self.downloaded = json.loads(state_file.read_text(encoding="utf-8")).get("downloaded", {})
                log.info(f"Ripristino stato: {len(self.downloaded)} file gia scaricati")
            except: log.warning("Stato corrotto, ricomincio")
    def is_downloaded(self, url: str) -> bool: return hashlib.sha256(url.encode()).hexdigest() in self.downloaded
    def mark_downloaded(self, url: str, file_path: str): self.downloaded[hashlib.sha256(url.encode()).hexdigest()] = str(file_path)
    def save(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps({"version":1,"downloaded":self.downloaded},indent=2),encoding="utf-8")

def login(session, username, password):
    log.info(f"Login come {username}...")
    r = session.get(LOGIN_URL, headers=HEADERS, timeout=30)
    t = BeautifulSoup(r.text,"html.parser").find("input",{"name":"logintoken"})
    if not t or not t.get("value"): log.error("Token non trovato"); return False
    r = session.post(LOGIN_URL, data={"username":username,"password":password,"logintoken":t["value"],"anchor":""},
                     headers={**HEADERS,"Referer":LOGIN_URL,"Content-Type":"application/x-www-form-urlencoded"},
                     allow_redirects=True, timeout=30)
    if r.url.rstrip("/") == LOGIN_URL.rstrip("/"):
        log.error("Login fallito.")
        err = BeautifulSoup(r.text,"html.parser").find("div",class_="alert-danger")
        if err: log.error(f"  -> {err.get_text(strip=True)}")
        return False
    d = session.get(DASHBOARD_URL, headers=HEADERS, timeout=15)
    if "/my/" in d.url or "page-my-index" in d.text: log.info("Login riuscito!"); return True
    log.error("Login fallito"); return False

def login_diagnose(session, username, password):
    print("\n=== DIAGNOSI ===\n")
    print("1) Homepage..."); r = session.get(BASE_URL+"/",headers=HEADERS)
    print(f"   Status: {r.status_code}, Session: {dict(session.cookies)}")
    print("2) Login page..."); r = session.get(LOGIN_URL,headers=HEADERS)
    t = BeautifulSoup(r.text,"html.parser").find("input",{"name":"logintoken"})
    print(f"   Status: {r.status_code}, Token: {t is not None}")
    print("3) POST...")
    r = session.post(LOGIN_URL, data={"username":username,"password":password,"logintoken":t["value"]if t else "","anchor":""},
                     headers={**HEADERS,"Referer":LOGIN_URL,"Content-Type":"application/x-www-form-urlencoded"},allow_redirects=True)
    print(f"   Status: {r.status_code}, URL: {r.url}")
    print("4) Dashboard..."); d = session.get(DASHBOARD_URL,headers=HEADERS)
    print("RIUSCITO!\n" if ("/my/"in d.url) else "FALLITO\n")

def get_sesskey(session):
    for url in [DASHBOARD_URL, BASE_URL+"/"]:
        try:
            r = session.get(url, headers=HEADERS, timeout=15)
            m = re.search(r'sesskey":"([^"]+)"', r.text) or re.search(r'sesskey\s*:\s*"([^"]+)"', r.text)
            if m: return m.group(1)
        except: continue
    return None

def call_ajax(session, method, args):
    sk = get_sesskey(session)
    if not sk: return None
    try:
        r = session.post(f"{BASE_URL}/lib/ajax/service.php?sesskey={sk}",
            json=[{"index":0,"methodname":method,"args":args}],
            headers={**HEADERS,"Content-Type":"application/json"},timeout=30)
        if r.ok:
            d = r.json()
            if isinstance(d,list) and d:
                if d[0].get("error"): return None
                return d[0].get("data")
    except: return None
    return None

def get_enrolled_courses(session):
    log.info("Recupero corsi...")
    courses, seen = [], set()
    data = call_ajax(session,"core_course_get_enrolled_courses_by_timeline_classification",
                     {"offset":0,"limit":100,"classification":"all","sort":"fullname"})
    if data:
        for c in data.get("courses",[]):
            cid=c.get("id")
            if cid and cid not in seen: seen.add(cid); courses.append({"id":cid,"fullname":c.get("fullname",""),"url":f"{BASE_URL}/course/view.php?id={cid}"})
        log.info(f"Trovati {len(courses)} corsi"); [log.info(f"  - [{c['id']}] {c['fullname']}") for c in courses]; return courses
    r = session.get(DASHBOARD_URL,headers=HEADERS)
    for a in BeautifulSoup(r.text,"html.parser").find_all("a",href=re.compile(r"/course/view\.php\?id=\d+")):
        m=re.search(r"id=(\d+)",a["href"]);cid=int(m.group(1))if m else 0;name=a.get_text(strip=True)
        if cid and cid not in seen and name: seen.add(cid); courses.append({"id":cid,"fullname":name,"url":urljoin(BASE_URL,a["href"])})
    return courses

def get_course_resources(session, course):
    """Cerca risorse via API (fallisce), poi HTML scanning."""
    # Prova API (quasi sempre disabilitata su questo Moodle)
    data = call_ajax(session,"core_course_get_contents",{"courseid":course["id"],"options":[]})
    if isinstance(data,list) and data:
        resources = []
        for sec in data:
            sn = sec.get("name","") or ""
            for mod in sec.get("modules",[]):
                mt, mn, mid, mu = mod.get("modname",""), mod.get("name",""), mod.get("id",0), mod.get("url","")
                if mt in ("resource","folder"):
                    for c in mod.get("contents",[]):
                        fn, fu, fs = c.get("filename",""), re.sub(r'\?token=[^&]+','',c.get("fileurl","") or ""), c.get("filesize",0)
                        if fn and fu and fs>0: resources.append({"id":mid,"name":fn,"type":mt,"url":mu,"download_url":fu,"section":sn,"filesize":fs})
                elif mt=="page":
                    for c in mod.get("contents",[]):
                        if c.get("filename") and c.get("fileurl"):
                            resources.append({"id":mid,"name":c["filename"],"type":"page_file","url":mu,"download_url":re.sub(r'\?token=[^&]+','',c["fileurl"]),"section":sn})
                    if not any(r["id"]==mid and r["type"]=="page_file" for r in resources):
                        resources.append({"id":mid,"name":f"{mn}.html","type":"page","url":mu,"download_url":None,"section":sn})
                elif mt=="book": resources.append({"id":mid,"name":mn,"type":"book","url":mu,"download_url":None,"section":sn})
        if resources:
            log.info(f"  {course['fullname']}: {len(resources)} risorse via API")
            for r in resources:
                sz=f" ({r.get('filesize',0)//1024} KB)"if r.get('filesize')else ""
                log.info(f"    [{r['type']:8}] {r['name']}{sz}")
            return resources

    # HTML scanning: cerca TUTTI i link nella pagina del corso
    log.info(f"  Scanning HTML {course['fullname']}...")
    try:
        r = session.get(course["url"], headers=HEADERS, timeout=30)
        r.raise_for_status()
    except: return []
    soup = BeautifulSoup(r.text, "html.parser")
    resources = []; seen_ids = set()

    # 1) Cerca TUTTI i link a mod/view.php (qualsiasi tipo)
    for a in soup.find_all("a", href=re.compile(r"/mod/(\w+)/view\.php\?id=\d+")):
        href = urljoin(BASE_URL, a["href"])
        m2 = re.search(r"/mod/(\w+)/view\.php\?id=(\d+)", href)
        if not m2: continue
        mt, mid = m2.group(1), int(m2.group(2))
        if mid in seen_ids: continue
        seen_ids.add(mid)
        name = a.get_text(strip=True) or "risorsa"
        dl_url = href  # default: usa view.php
        # Per resource cerca pluginfile nelle vicinanze
        if mt in ("resource","folder"):
            parent = a.find_parent(["li","div","td"])
            if parent:
                dl = parent.find("a", href=re.compile(r"/pluginfile\.php/"))
                if dl: dl_url = urljoin(BASE_URL, dl["href"])
        resources.append({"id":mid,"name":name,"type":mt,"url":href,"download_url":dl_url,"section":""})

    # 2) Pluginfile diretti (copia di backup, URL, immagini, ecc.)
    seen_names = set()
    for a in soup.find_all("a", href=re.compile(r"/pluginfile\.php/")):
        name = a.get_text(strip=True) or ""
        if name and name not in seen_names:
            seen_names.add(name)
            resources.append({"id":0,"name":name,"type":"file","url":urljoin(BASE_URL,a["href"]),
                              "download_url":urljoin(BASE_URL,a["href"]),"section":""})

    log.info(f"  {course['fullname']}: {len(resources)} risorse")
    return resources

def file_exists(p: Path) -> bool: return p.exists() and p.stat().st_size >= MIN_VALID_FILE_SIZE

def download_file(session, url, dest_path, state, force=False):
    if not force and (state.is_downloaded(url) or file_exists(dest_path)): return True
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = session.get(url, headers=HEADERS, stream=True, timeout=120)
        r.raise_for_status()
        fname = sanitize_filename(unquote(extract_filename_from_cd(r.headers, dest_path.name)))
        dest = dest_path.with_name(fname) if fname != dest_path.name else dest_path
        if not force and file_exists(dest): state.mark_downloaded(url, str(dest)); return True
        dest.write_bytes(r.content)
        state.mark_downloaded(url, str(dest))
        log.info(f"  [OK] {dest.name} ({len(r.content)//1024} KB)"); return True
    except requests.RequestException as e:
        log.warning(f"  [WARN] Download fallito {dest_path.name}: {e}")
        if dest_path.exists() and dest_path.stat().st_size == 0: dest_path.unlink()
        return False

def download_activity(session, act, dest_dir, state, force=False):
    count = 0
    if act.get("download_url"):
        path = dest_dir / sanitize_filename(act["name"])
        if '.' not in path.name and act.get("download_url"):
            ext = os.path.splitext(act["download_url"].split('?')[0])[1]
            if ext: path = path.with_name(path.name + ext)
        if download_file(session, act["download_url"], path, state, force): count += 1
    elif act["type"] == "page":
        try:
            r = session.get(act["url"], headers=HEADERS, timeout=30)
            if r.ok:
                cd = BeautifulSoup(r.text,"html.parser").find("div",class_=re.compile(r"no-overflow|resourcecontent"))
                if cd:
                    sub = dest_dir / sanitize_filename(act["name"].replace(".html",""))
                    sub.mkdir(parents=True,exist_ok=True); (sub/"index.html").write_text(str(cd),encoding="utf-8")
                    log.info(f"  [OK] {act['name']} (HTML)"); count += 1
        except: pass
    elif act["type"] == "book":
        try:
            r = session.get(act["url"].replace("/view.php?","/tool/print/index.php?"), headers=HEADERS, timeout=30)
            if r.ok:
                cd = BeautifulSoup(r.text,"html.parser").find("div",class_=re.compile(r"no-overflow|book_content"))
                if cd:
                    sub = dest_dir / sanitize_filename(act["name"]); sub.mkdir(parents=True,exist_ok=True)
                    (sub/"index.html").write_text(str(cd),encoding="utf-8"); log.info(f"  [OK] {act['name']} (Book)"); count += 1
        except: pass
    return count

def map_course(course_name: str, mapping):
    nl = course_name.lower().strip()
    for pat, folder in mapping.items():
        if pat in nl: return folder
    return f"ZZ_{sanitize_filename(course_name).replace(' ','_')[:50]}"

def get_mapping(mapping_file):
    if mapping_file.exists():
        try: data=json.loads(mapping_file.read_text(encoding="utf-8")); log.info(f"Mapping: {len(data)} regole"); return data
        except: log.warning("Mapping corrotto")
    return DEFAULT_MAPPING.copy()

def gen_mapping(session, mapping_file):
    courses=get_enrolled_courses(session)
    if not courses: return
    folders=sorted(d.name for d in BASE_DIR.iterdir() if d.is_dir() and re.match(r"^\d{2}_",d.name) and not d.name.startswith("."))
    print(f"\nCartelle ({len(folders)}):"); [print(f"  - {f}") for f in folders]
    m={}
    for c in courses:
        print(f"\n--- {c['fullname']} ---")
        auto=map_course(c["fullname"],DEFAULT_MAPPING);hint=" (nuova)"if auto.startswith("ZZ_")else""
        print(f"  Suggerita: {auto}{hint}")
        ans=input(f"  Cartella [Invio={auto}]: ").strip()
        m[c["fullname"]]=ans if ans else auto
    mapping_file.parent.mkdir(parents=True,exist_ok=True);mapping_file.write_text(json.dumps(m,indent=2,ensure_ascii=False),encoding="utf-8")
    print(f"\nSalvato in {mapping_file}")

def main():
    p=argparse.ArgumentParser(description="FAD Downloader - ITS ICT Piemonte")
    p.add_argument("-u","--username");p.add_argument("-p","--password")
    p.add_argument("-n","--dry-run",action="store_true");p.add_argument("-c","--course");p.add_argument("-f","--force",action="store_true")
    p.add_argument("--show-mapping",action="store_true");p.add_argument("--update-mapping",action="store_true")
    p.add_argument("--login-diagnose",action="store_true");p.add_argument("--debug",action="store_true")
    a=p.parse_args()
    if a.debug: log.setLevel(logging.DEBUG)
    load_dotenv(DOTENV_FILE)
    print("== FAD Downloader - ITS ICT Piemonte ==")
    if a.show_mapping:
        for k,v in sorted(get_mapping(MAPPING_FILE).items()):print(f'  "{k}"->{v}');return
    username=a.username or os.environ.get("FAD_USERNAME") or input("Username: ").strip()
    password=a.password or os.environ.get("FAD_PASSWORD") or getpass("Password: ")
    s=requests.Session()
    if a.login_diagnose:login_diagnose(s,username,password);return
    if not login(s,username,password):sys.exit(1)
    if a.update_mapping:gen_mapping(s,MAPPING_FILE);return
    mapping=get_mapping(MAPPING_FILE);courses=get_enrolled_courses(s)
    if not courses:log.error("Nessun corso.");sys.exit(1)
    if a.course:
        q=a.course.lower();f2=[c for c in courses if q in c["fullname"].lower()]
        if not f2:print(f"Nessun corso '{a.course}'.");[print(f"  - {c['fullname']}")for c in courses];sys.exit(1)
        courses=f2;print(f"Filtrati: {len(courses)} corso(i)")
    state=DownloadState(STATE_FILE);total=0
    for course in courses:
        folder=map_course(course["fullname"],mapping);dest=BASE_DIR/folder/"01_Materiale"
        print(f"\n{'='*50}\n  {course['fullname']}\n  -> {dest.relative_to(BASE_DIR)}/\n{'='*50}")
        resources=get_course_resources(s,course)
        if a.dry_run:
            for r in resources:
                sz=f" ({r['filesize']//1024} KB)"if r.get('filesize')else""
                print(f"  [{r['type']:8}] {r['name']}{sz}")
            print(f"  -> {len(resources)} risorse");continue
        for r in resources:
            try:total+=download_activity(s,r,dest,state,force=a.force)
            except Exception as e:log.warning(f"  [ERR] {r['name']}: {e}")
        state.save()
    print(f"\n{'='*50}\n  {'DRY RUN'if a.dry_run else'COMPLETATO'}- {len(courses)} corso(i)\n{'='*50}")

if __name__=="__main__":main()
