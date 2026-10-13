# FAD Downloader

Richiede Python 3.10 o successivo.

```powershell
python -m pip install -r tool/requirements.txt
python tool/download_fad.py --dry-run
python tool/download_fad.py --course-id 123
python tool/download_fad.py --show-mapping
python tool/download_fad.py --update-mapping
python -m unittest discover -s tool/tests -v
```

Le credenziali vengono richieste interattivamente oppure lette da `FAD_USERNAME` e
`FAD_PASSWORD` in `tool/.env`. Le variabili già presenti nell'ambiente hanno precedenza.
Il parametro `--password` resta compatibile, ma può esporre la password nella
cronologia della shell. La diagnosi non stampa i valori dei cookie.

Opzioni: `--output-dir`, `--state-file`, `--mapping-file`, `--env-file`,
`--timeout` (secondi), `--retries` (0–10), `--course` (testo), `--course-id`,
`--force` e `--debug`. Le modalità dry-run, mapping e diagnosi sono mutuamente esclusive.

Le regole personalizzate integrano quelle predefinite. `id:123` associa esattamente
un corso; seguono i titoli esatti e le regole per parole, dalla più specifica.
Le destinazioni devono essere percorsi relativi contenuti nella directory di output.
Il materiale viene organizzato per sezione e attività; i nomi duplicati ricevono
un suffisso stabile. I file esistenti non associati allo stato non vengono sovrascritti.

Lo stato v2 conserva percorsi relativi, dimensioni, SHA-256 e validatori HTTP.
Lo stato v1 viene riletto ma i download vengono nuovamente verificati.
Uno stato corrotto causa un errore esplicito: conservarne una copia e ripristinare
una versione valida oppure scegliere un nuovo `--state-file`.
I file sono scritti prima in temporanei e sostituiti solo dopo la verifica.
Ogni trasferimento completato salva lo stato. I file vengono verificati nuovamente
sul server, con richieste condizionali se sono disponibili ETag/Last-Modified.

Pagine e libri esportano il contenuto HTML e gli allegati pluginfile; i collegamenti
esterni rimangono online. Contenuti dinamici, video esterni e risorse incorporate
via CSS non sono convertiti in un sito offline completo. Quiz, forum e altri tipi
non gestiti vengono segnalati nel riepilogo. La compatibilità con il tema Moodle
va verificata con `--dry-run` e un corso di prova.

Codici di uscita: 0 successo, 1 errori, 2 argomenti non validi, 130 interruzione.
Un lock impedisce download contemporanei nella stessa directory. Dopo un arresto
forzato può rimanere `.fad_download.lock`: rimuoverlo solo quando non ci sono processi attivi.
I materiali preesistenti non vengono eliminati o riorganizzati automaticamente.
