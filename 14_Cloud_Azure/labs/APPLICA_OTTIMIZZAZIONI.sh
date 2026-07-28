#!/bin/bash
set -e

echo "=========================================="
echo "Applicazione Ottimizzazioni Azure E2E Lab"
echo "=========================================="
echo ""

# Backup dei file originali
echo "1. Creazione backup dei file originali..."
mkdir -p backup_$(date +%Y%m%d_%H%M%S)
cp backend/requirements.txt backup_$(date +%Y%m%d_%H%M%S)/
cp backend/function_app.py backup_$(date +%Y%m%d_%H%M%S)/
cp infra/main.tf backup_$(date +%Y%m%d_%H%M%S)/
cp infra/outputs.tf backup_$(date +%Y%m%d_%H%M%S)/
echo "✓ Backup completato"
echo ""

# 1. Aggiornare requirements.txt
echo "2. Aggiornamento backend/requirements.txt..."
cat > backend/requirements.txt << 'EOF'
azure-functions
azure-cosmos
azure-storage-queue
EOF
echo "✓ requirements.txt aggiornato"
echo ""

# 2. Migliorare gestione errori in function_app.py
echo "3. Miglioramento gestione errori in backend/function_app.py..."
# Questo richiede modifica manuale - vedi OTTIMIZZAZIONI_DA_APPLICARE.md punto 6
echo "⚠ MANUALE: Modifica function riepilogo in backend/function_app.py (vedi punto 6 del documento)"
echo ""

# 3. Modificare infra/main.tf
echo "4. Modifiche a infra/main.tf..."
echo "⚠ MANUALE: Le seguenti modifiche vanno applicate manualmente:"
echo "   - Aggiungere segreto storage_conn in Key Vault (punto 1.1)"
echo "   - Modificare app_settings con Key Vault references (punto 1.2)"
echo "   - Aggiungere always_on = true (punto 3)"
echo "   - Restringere CORS (punto 2)"
echo "   - Disabilitare admin_enabled ACR (punto 4.1)"
echo "   - Aggiungere identity al frontend (punto 4.2)"
echo "   - Modificare site_config frontend (punto 4.3)"
echo "   - Aggiungere role assignment ACR (punto 4.4)"
echo ""

echo "=========================================="
echo "Riepilogo:"
echo "✓ requirements.txt aggiornato automaticamente"
echo "⚠ function_app.py richiede modifica manuale"
echo "⚠ main.tf richiede modifiche manuali"
echo ""
echo "Consulta OTTIMIZZAZIONI_DA_APPLICARE.md per i dettagli"
echo "=========================================="
