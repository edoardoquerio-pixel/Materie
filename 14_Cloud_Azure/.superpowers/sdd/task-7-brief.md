# Task 7: Final Cleanup and .gitignore

## Context
This is the seventh and final task in an Azure E2E lab project. Tasks 1-6 created all application code and documentation. This task cleans up the project with a proper .gitignore.

**Working directory:** `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\labs`

## What to do

### Step 1: Write `.gitignore`

```
# Terraform
infra/.terraform/
infra/*.tfstate
infra/*.tfstate.backup
infra/tfplan
infra/.terraform.lock.hcl

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/

# Node
node_modules/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Env files
.env
*.env.local

# Docker
docker-compose.override.yml
```

### Step 2: Remove empty `frontend/script.js` (if it exists)
```bash
rm -f /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs/frontend/script.js
```

### Step 3: Final commit
```bash
cd /c/Users/edoardo.querio/Desktop/Materie/14_Cloud_Azure/labs
git add .
git commit -m "chore: add .gitignore and clean up empty files"
```

## Report
Write your report to: `C:\Users\edoardo.querio\Desktop\Materie\14_Cloud_Azure\.superpowers\sdd\task-7-report.md`

Include: status (DONE/BLOCKED/NEEDS_CONTEXT), files created/modified, any concerns.
