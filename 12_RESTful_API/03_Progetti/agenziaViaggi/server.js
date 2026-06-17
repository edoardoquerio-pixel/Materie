import express from 'express';
import bodyParser from 'body-parser';
import sqlite3 from 'sqlite3';
import { CREATE_TABLE_VIAGGI } from './database/script_viaggi.js';
import { CREATE_TABLE_CLIENTI } from './database/script_clienti.js';
import { CREATE_TABLE_PRENOTAZIONI } from './database/script_prenotazioni.js';
import viaggiRouter from './routes/viaggiRouter.js';
import clientiRouter from './routes/clientiRouter.js';
import prenotazioniRouter from './routes/prenotazioniRouter.js';
import swaggerUi from 'swagger-ui-express';
import swaggerConf from './swagger/swagger.json' with { type: 'json' };
import cors from 'cors';

const app = express();
const port = 3000;
app.use(cors());
app.use(bodyParser.json());
app.use(express.static('public'));
app.use("/api/v2/viaggi", viaggiRouter);
app.use("/api/v2/clienti", clientiRouter);
app.use("/api/v2/prenotazioni", prenotazioniRouter);

//integrazione Swagger UI per la documentazione interattiva dell'API
app.use("/api-docs",swaggerUi.serve, swaggerUi.setup(swaggerConf));

export const db = new sqlite3.Database("./database/agenzia.db");

// Abilita i vincoli di chiave esterna (SQLite default: OFF)
db.run("PRAGMA foreign_keys = ON");

app.listen(port, () => {
  console.log(`Il server è attivo sulla porta ${port}`);
  initializeDatabase();
});

function initializeDatabase() {
  console.log("Inizializzazione del database...");

  db.exec(CREATE_TABLE_VIAGGI, (err) => {
    if (err){
      console.error("Errore durante la creazione della tabella viaggi:", err.message);
    } else {
      console.log("Tabella viaggi creata o già esistente.");
    }
  });
  db.exec(CREATE_TABLE_CLIENTI, (err) => {
    if (err){
      console.error("Errore durante la creazione della tabella clienti:", err.message);
    } else {
      console.log("Tabella clienti creata o già esistente.");
    }
  });
  db.exec(CREATE_TABLE_PRENOTAZIONI, (err) => {
    if (err){
      console.error("Errore durante la creazione della tabella prenotazioni:", err.message);
    } else {
      console.log("Tabella prenotazioni creata o già esistente.");
    }
  });
}
