# [07] Version Control Git

## 📋 Panoramica

Materia dedicata al controllo di versione distribuito con Git. Copre l'intero flusso di lavoro: repository locale, branching, repository remoti (GitHub/GitLab) e client grafici. Approccio progressivo dai fondamenti agli strumenti GUI.

**Tecnologie**: Git (CLI), GitHub, GitLab, Git GUI (Sourcetree, GitKraken, VS Code)

---

## 📚 Indice degli argomenti

### 1. Fondamenti di Version Control

- **Cos'è il version control**: tracciamento delle modifiche ai file nel tempo
- **VCS Centralizzato** (SVN, CVS): server singolo, single point of failure
- **VCS Distribuito** (Git, Mercurial): ogni clone è un backup completo
- **Concetti base**:
  - Repository (repo): contenitore del progetto
  - Commit: snapshot dello stato dei file
  - Hash SHA-1: identificatore univoco di ogni commit
- **Flusso base**:
  ```
  git init                    # crea nuovo repository
  git add <file>              # staging area
  git commit -m "messaggio"   # salva snapshot
  git log                     # cronologia commit
  git status                  # stato attuale
  ```

### 2. Git Locale e Branch

- **Working directory → Staging area → Repository** (tre stati di Git)
- **Branch**: puntatore mobile a un commit; ramo di sviluppo indipendente
- **Comandi branch**:
  ```
  git branch <nome>           # crea branch
  git checkout <nome>         # switcha a branch
  git switch <nome>           # alternativa moderna (Git 2.23+)
  git merge <branch>          # unisce branch nel corrente
  ```
- **Merge**: automatico (fast-forward o 3-way) o manuale (conflitto da risolvere)
- **Conflitti**: succedono quando stesso file modificato in due branch
  ```
  <<<<<<< HEAD
  nostro codice
  =======
  loro codice
  >>>>>>> feature-branch
  ```
- **Stash**: salva modifiche temporanee senza commit
  ```
  git stash        # salva
  git stash pop    # ripristina
  ```

### 3. Git Remoto e Repository Online

- **git clone**: copia un repository remoto in locale
- **git remote**: gestisce connessioni a repository remoti
- **git push**: invia commit locali al remoto
- **git pull**: recupera e unisce (fetch + merge) dal remoto
- **git fetch**: recupera senza unire
- **Flusso collaborativo base**:
  ```
  git clone <url>
  git checkout -b feature/nuova-funzionalità
  # ...lavoro...
  git add . && git commit -m "feat: aggiunta funzionalità X"
  git push origin feature/nuova-funzionalità
  # → aprire Pull Request su GitHub
  ```
- **GitHub/Lab**: fork, pull request, code review, issues, actions/CI

### 4. Git GUI e Client Grafici

- **GitHub Desktop**: semplice, integrazione GitHub nativa
- **Sourcetree**: visuale, branching grafico, flow Git-flow
- **GitKraken**: cross-platform, integrazione issue tracker
- **VS Code Git**: built-in, staging visuale, diff editor, branch switcher
- **gitg / GitEye / Git Cola**: alternative Linux/lightweight

---

## ⚡ Punti Chiave

1. **Commit atomici e frequenti**: un commit = un'unità logica di modifica
2. **Messaggi di commit chiari**: imperativo, prima riga <72 caratteri
3. **Mai pushare su main/master diretto**: usare feature branch + PR
4. **Pull sempre prima di push**: `git pull --rebase` per cronologia lineare
5. **`.gitignore`**: non committare mai file binari, secret, `node_modules/`, `.env`
6. **Non fare rebase su branch pubblici**: altera la cronologia

---

## 📎 Risorse Collegate

- **02_Esercizi/** — Esercizi pratici su Git locale e remoto
- **03_Progetti/** — Progetti con workflow Git
- **Materiale**: 4 PDF (lezioni 1-4) + quiz DOCX
