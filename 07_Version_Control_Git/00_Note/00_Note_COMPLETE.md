# Version Control Git — Note Complete

## 1. Concetti Base

- **VCS**: tracciamento modifiche, collaborazione, rollback
- **Distribuito**: ogni copia ha intero repository
- **Snapshots** (non diff): ogni commit è un'istantanea
- **Tre aree**: Working Directory → Staging Area (index) → Repository (.git)

## 2. Comandi Essenziali

```bash
git init                          # Nuovo repo
git clone <url>                   # Clona repo remoto
git add <file>                    # Staging file
git commit -m "message"           # Crea commit
git status                        # Stato repo
git log --oneline --graph         # Cronologia
git diff                          # Modifiche unstaged
git diff --staged                 # Modifiche staged
```

## 3. Branching & Merging

```bash
git branch <name>                 # Crea branch
git checkout <branch>             # Switch branch
git switch <branch>               # Modern switch
git merge <branch>                # Merge (fast-forward o merge commit)
git rebase <branch>               # Riapplica commit su base diversa
git cherry-pick <hash>            # Applica commit specifico
```

- **Merge conflicts**: risoluzione manuale, `git mergetool`
- **Strategie**: merge vs rebase, git-flow, trunk-based

## 4. Remoti

```bash
git remote add origin <url>       # Aggiunge remote
git push -u origin main           # Push + upstream
git pull                          # Fetch + merge
git fetch                         # Solo download, no merge
git remote -v                     # Lista remoti
```

## 5. Git avanzato

```bash
git stash                         # Salva modifiche temporanee
git stash pop                     # Recupera stash
git reset HEAD~1                  # Annulla commit (mantenendo files)
git reset --hard HEAD~1           # Annulla commit + modifiche
git revert <hash>                 # Annulla con nuovo commit
git tag v1.0.0                    # Tag semantico
git bisect                        # Ricerca binaria bug
git blame <file>                  # Autore per riga
git reflog                        # Cronologia ref log
```

## 6. Branching Strategies

| Strategy | Uso | Pro | Contro |
|----------|-----|-----|--------|
| **Git Flow** | Release programmate | Produzione stabile, hotfix | Complesso |
| **GitHub Flow** | CI/CD continuo | Semplice, veloce | Senza release branch |
| **Trunk-based** | Feature flag, deploy frequenti | Massima velocità | Richiede disciplina |
| **GitLab Flow** | Environment branch | Mapping ambiente-branch | Media complessità |

## 7. .gitignore

Pattern per escludere file:
- `node_modules/`, `.env`, `*.log`, `build/`, `dist/`
- `__pycache__/`, `*.pyc`, `.DS_Store`
- File con credenziali, chiavi, certificati

## 8. GitHub/GitLab

- **Pull Request / Merge Request**: code review, checks, approval
- **Issues**: bug tracker, feature request, task management
- **Actions / CI**: test automatici, lint, build
- **Protected branches**: main bloccato, richiede PR + review
- **GitHub Pages**: hosting statico da repo

## 9. Quiz / Esercizi

- Creare repo → commit → branch → merge
- Risoluzione conflict manuale
- Rebase interattivo (squash, reorder, reword)
- Cherry-pick tra branch
- Git bisect per trovare bug commit
- Git hooks (pre-commit, post-commit)
