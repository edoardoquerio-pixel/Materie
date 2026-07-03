# URL nel database WordPress

Fonte: `URL nel database WordPress.txt`

URL nel database WordPress

Da debian3, connettersi al database su debian4:
mysql -h 10.0.0.2 -u wpuser -p WordPress

Aggiornare i due campi:
UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'siteurl';

UPDATE wp_options SET option_value = 'http://acme.local'
WHERE option_name = 'home';

Verifica:
SELECT option_name, option_value FROM wp_options
WHERE option_name IN ('siteurl', 'home');

# Entrambi devono mostrare http://acme.local
Nota: senza questo passaggio, WordPress continua a generare link e redirect verso il vecchio nome. Lo studente che corregge solo nginx ma non il database vedrà il sito caricarsi in modo anomalo.
 
