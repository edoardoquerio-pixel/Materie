import sqlite3 from 'sqlite3';

const db = new sqlite3.Database('./database/database.db');

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS viaggi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    destinazione TEXT NOT NULL,
    durata INTEGER NOT NULL,
    prezzo REAL NOT NULL,
    assicurazione BOOLEAN NOT NULL
  )`);
});


export default db;