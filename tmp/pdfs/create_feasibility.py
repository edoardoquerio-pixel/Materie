from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
import fitz

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/pdf/QUERIOGIANETTOEDOARDO.pdf'
navy=colors.HexColor('#183348'); teal=colors.HexColor('#147D86'); gray=colors.HexColor('#52616C')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyIT',fontName='Helvetica',fontSize=10.5,leading=14,spaceAfter=8,textColor=navy))
styles.add(ParagraphStyle(name='TitleIT',fontName='Helvetica-Bold',fontSize=32,leading=37,textColor=navy,spaceAfter=18))
styles.add(ParagraphStyle(name='SubIT',fontName='Helvetica',fontSize=15,leading=21,textColor=gray,spaceAfter=14))
styles.add(ParagraphStyle(name='SectionIT',fontName='Helvetica-Bold',fontSize=17,leading=22,textColor=teal,spaceBefore=14,spaceAfter=11))
styles.add(ParagraphStyle(name='SmallIT',fontName='Helvetica',fontSize=9,leading=12,textColor=gray))
styles.add(ParagraphStyle(name='CellIT',fontName='Helvetica',fontSize=9.5,leading=13,textColor=navy))
story=[]
def p(text,style='BodyIT'): story.append(Paragraph(text,styles[style]))
def heading(text): p(text,'SectionIT')
def bullet(title,text): p(f'<b>{title}.</b> {text}')
def footer(canvas,doc):
    canvas.saveState()
    w,h=A4
    canvas.setStrokeColor(teal); canvas.setLineWidth(.6)
    canvas.line(48,45,w-48,45)
    canvas.setFont('Helvetica',8); canvas.setFillColor(gray)
    canvas.drawString(48,31,'FAD Downloader | Studio di fattibilità | 2026/2027')
    canvas.drawRightString(w-48,31,str(doc.page))
    canvas.restoreState()

p('ITS-ICT PIEMONTE','SubIT')
story.append(Spacer(1,70))
p('FAD Downloader','TitleIT')
p('Download e organizzazione dei materiali<br/>didattici da Moodle','SubIT')
story.append(Spacer(1,24))
p('ANALISI DI FATTIBILITÀ<br/>Progetto per la prova finale','SectionIT')
story.append(Spacer(1,45))
rows=[('Studente','Edoardo Querio Gianetto'),('Scuola','ITS-ICT Piemonte'),('Anno formativo','2026/2027'),('Materia','Python'),('Docente','Massimo Papa')]
t=Table([[Paragraph(a,styles['SmallIT']),Paragraph(b,styles['BodyIT'])] for a,b in rows],colWidths=[120,360])
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
story.append(t)
story.append(PageBreak())
heading('1. Oggetto')
p('Il progetto consiste nello sviluppo di un’applicazione Python con interfaccia grafica per scaricare e organizzare i materiali didattici dei corsi Moodle della piattaforma FAD di ITS-ICT Piemonte. Il software sarà eseguibile su distribuzioni GNU/Linux e consentirà allo studente di mantenere una raccolta locale dei materiali a cui è autorizzato ad accedere.')
heading('2. Scopo')
p('Il progetto nasce dall’esigenza di ridurre le operazioni manuali necessarie per recuperare documenti distribuiti tra corsi, sezioni e attività. Il download tramite browser richiede di aprire più pagine, scegliere i singoli allegati e rinominarli o collocarli nelle cartelle appropriate.')
p('L’applicazione si propone di automatizzare queste operazioni, rendere più ordinata la raccolta dei materiali e facilitarne la consultazione locale. Dovrà inoltre distinguere file nuovi, aggiornati e già presenti, evitare sovrascritture accidentali e segnalare errori o attività non supportate.')
heading('3. Modalità operative')
p('<b>Percorso di sviluppo.</b> Il lavoro comprenderà la definizione dei requisiti, lo sviluppo delle funzionalità, la verifica sul servizio Moodle, il collaudo su GNU/Linux e la preparazione della documentazione. Saranno predisposti test automatici locali per controllare il comportamento delle funzioni e prove su un corso reale per verificare la compatibilità con la piattaforma.')
p('<b>Ambiente di sviluppo.</b> Il progetto sarà sviluppato in Python 3.10 o successivo, utilizzando Visual Studio Code, Git e un ambiente virtuale <font face="Courier">venv</font>. Il collaudo principale sarà svolto su Ubuntu, installato in una macchina virtuale o su una postazione GNU/Linux. L’applicazione offrirà un’interfaccia grafica completa realizzata con Tkinter e i widget ttk. La riga di comando resterà una modalità facoltativa per automatizzare le operazioni. Non saranno necessari servizi cloud aggiuntivi.')
p('<b>Librerie.</b> <font face="Courier">requests</font> gestirà sessioni HTTP, cookie e download; <font face="Courier">BeautifulSoup4</font> analizzerà le pagine HTML; <font face="Courier">python-dotenv</font> caricherà la configurazione delle credenziali. <font face="Courier">tkinter</font> realizzerà l’interfaccia grafica completa e <font face="Courier">keyring</font> gestirà il salvataggio nel portachiavi di sistema GNU/Linux. Saranno verificate la disponibilità di Tk e di un portachiavi compatibile nella distribuzione scelta. La libreria standard fornirà <font face="Courier">argparse</font> per i comandi, <font face="Courier">pathlib</font> per i percorsi, <font face="Courier">json</font> per lo stato, <font face="Courier">hashlib</font> per SHA-256, <font face="Courier">logging</font> per i messaggi e <font face="Courier">unittest</font> per i test.')
p('<b>Struttura tecnica.</b> Le responsabilità saranno separate in blocchi dedicati a configurazione, autenticazione, scoperta delle risorse, download, stato persistente e associazione dei corsi alle cartelle. Le API AJAX disponibili saranno integrate con l’analisi HTML delle pagine quando necessario. Scansioni e download saranno eseguiti in attività di background; la GUI riceverà gli aggiornamenti tramite una coda, mantenendo reattiva la finestra.')
story.append(PageBreak())
heading('3. Modalità operative - funzionalità')
bullet('Scansione iniziale e mappatura','Al primo avvio, dopo il login, il programma analizzerà la struttura della FAD accessibile allo studente, individuando corsi, sezioni e attività. Proporrà una mappa dei corsi e delle cartelle locali che l’utente potrà confermare o modificare; la configurazione sarà salvata per i lanci successivi. Una nuova scansione potrà essere richiesta per riconoscere nuovi corsi e attività, mantenendo le associazioni alle cartelle già confermate.')
bullet('Form di login e credenziali','Una finestra presenterà i campi username e password, con password mascherata, il pulsante Accedi e l’opzione Ricorda credenziali. Solo dopo un login riuscito e con il consenso dell’utente, la password sarà salvata nel portachiavi di sistema tramite keyring e potrà essere riutilizzata nei lanci successivi. Sarà possibile cambiare account o eliminare le credenziali salvate. Se il portachiavi non sarà disponibile, il login resterà utilizzabile senza memorizzazione della password. Password e valori dei cookie non saranno riportati nei log.')
bullet('Accesso e selezione dei corsi','Dopo l’autenticazione il programma recupererà i corsi accessibili, consentendo di selezionarli per nome o ID. L’utente potrà scegliere singole sezioni e scaricare materiali, test svolti oppure entrambi.')
bullet('Gestione della sessione','In caso di scadenza della sessione, il programma richiederà nuovamente l’autenticazione e riprenderà le operazioni mantenendo i progressi salvati. Gli errori di accesso saranno distinti dai problemi di rete o dai contenuti non disponibili.')
bullet('Nomenclatura della directory di lavoro','L’utente potrà scegliere il percorso e il nome della directory di lavoro, configurando anche i nomi delle sottocartelle per corsi, sezioni, materiali e test. Saranno disponibili regole basate su nome del corso, ID, numero progressivo e data, con scelta di prefissi e separatori. Prima della creazione sarà mostrata un’anteprima della struttura; le preferenze saranno salvate e riutilizzate. Il programma controllerà caratteri non validi e collisioni tra nomi. Le modifiche alle regole si applicheranno alle nuove cartelle; quelle già presenti non saranno rinominate automaticamente.')
bullet('Raccolta e organizzazione','Download degli allegati e dei file contenuti nelle cartelle; esportazione di pagine e libri in HTML con allegati locali. I materiali saranno organizzati per materia, sezione e attività, con regole di associazione configurabili.')
bullet('Esportazione dei test svolti','Il programma consentirà di salvare in HTML i tentativi già svolti dei quiz, riportando domande, risposte fornite, punteggi, esito e feedback nella misura in cui siano visibili nella pagina di revisione dell’account. Gli eventuali allegati accessibili saranno scaricati; i tentativi saranno distinti per quiz e data, con possibilità di esportarli tutti oppure selezionare quelli desiderati. Non saranno avviati nuovi tentativi né modificate le risposte.')
story.append(PageBreak())
heading('3. Modalità operative - gestione e verifica')
bullet('Affidabilità dei trasferimenti','Download a blocchi, controllo di dimensione e hash, scrittura su file temporaneo e sostituzione finale solo dopo la verifica. Saranno gestiti nomi duplicati, timeout, errori HTTP e tentativi limitati per problemi temporanei.')
bullet('Stato e aggiornamenti','Salvataggio dei progressi dopo ogni file completato, verifica delle copie locali e controllo degli aggiornamenti sul server. Quando disponibili, ETag e Last-Modified consentiranno richieste condizionali. Un lock impedirà esecuzioni simultanee nella stessa destinazione.')
bullet('Interfaccia utente','Dopo il login, una finestra principale mostrerà corsi, sezioni e attività in una struttura ad albero, con ricerca e selezione dei contenuti e dei tentativi dei quiz. Pannelli dedicati consentiranno di configurare cartelle, nomenclatura e preferenze, con anteprima dei percorsi. Pulsanti permetteranno di avviare la scansione, simulare o eseguire i download, interrompere il lavoro e ritentare gli errori. Una barra di avanzamento e un registro dei messaggi mostreranno lo stato delle operazioni; al termine saranno disponibili report e apertura dell’indice locale. La CLI facoltativa userà la stessa logica applicativa della GUI.')
bullet('Report finale e nuovi tentativi','Al termine sarà salvato un report consultabile con download riusciti, file aggiornati, errori e contenuti non accessibili. L’utente potrà ritentare i trasferimenti falliti senza ripetere quelli completati, rispettando i permessi di accesso.')
bullet('Indice locale dei contenuti','Sarà generata una pagina HTML con collegamenti ai materiali e ai test esportati, organizzata per corso e sezione. L’indice sarà aggiornato dopo i download e consentirà di aprire le copie locali dal browser senza cercarle manualmente nelle cartelle.')
p('<b>Esempio di utilizzo su GNU/Linux.</b> Dopo l’installazione delle dipendenze, l’utente avvierà l’applicazione e accederà dalla finestra di login. Al primo avvio confermerà la mappatura proposta, configurerà la directory di lavoro e selezionerà materiali e test dall’albero dei corsi. Potrà controllare l’anteprima, avviare il download e consultare il report e l’indice locale dalla GUI.')
p('<b>Fattibilità e limiti.</b> Le funzionalità previste e le librerie scelte rendono il progetto tecnicamente realizzabile senza costi software aggiuntivi previsti. Servono una connessione Internet e un account con accesso ai corsi. Il rischio principale è la dipendenza dal tema, dai permessi e dagli endpoint Moodle: sarà affrontato con test su un corso reale e messaggi espliciti in caso di incompatibilità. Per i quiz, l’esportazione dipenderà dai permessi e dalle opzioni di revisione impostate dal docente: i contenuti non visibili saranno segnalati senza tentare di recuperarli. Forum, video esterni e contenuti dinamici non rientrano nella raccolta offline prevista.')
heading('4. Tempistica complessiva')
p('Il completamento del progetto è previsto indicativamente entro la fine di novembre 2026, includendo il collaudo su GNU/Linux, la verifica sulla piattaforma Moodle e la preparazione della documentazione finale.')
SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=43,bottomMargin=60,title='FAD Downloader - Analisi di fattibilità',author='Edoardo Querio Gianetto').build(story,onFirstPage=footer,onLaterPages=footer)
doc=fitz.open(OUT)
print('PDF:',OUT,'Pagine:',len(doc))
for i,page in enumerate(doc):
    page.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(ROOT/f'tmp/pdfs/fattibilita-{i+1}.png')
    print(i+1,len(page.get_text()))
