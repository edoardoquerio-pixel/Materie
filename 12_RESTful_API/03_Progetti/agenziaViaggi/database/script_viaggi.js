export const CREATE_TABLE_VIAGGI = `CREATE TABLE IF NOT EXISTS viaggi (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        destinazione TEXT NOT NULL,
                                        descrizione TEXT,
                                        durata INTEGER NOT NULL,
                                        prezzo REAL NOT NULL,
                                        assicurazione INTEGER NOT NULL DEFAULT 0,
                                        data_partenza TEXT,
                                        data_ritorno TEXT,
                                        trasporto TEXT NOT NULL CHECK(trasporto IN ('aereo','treno','nave','bus','auto')),
                                        posti_disponibili INTEGER,
                                        valutazione INTEGER CHECK(valutazione BETWEEN 1 AND 5)
                                    )`;

export const SELECT_ALL = "SELECT * FROM viaggi";

export const SELECT_BY_ID = "SELECT * FROM viaggi WHERE id = ?";

export const SELECT_BY_DESTINAZIONE = "SELECT * FROM viaggi WHERE LOWER(destinazione) LIKE '%' || LOWER(?) || '%'";

export const INSERT_VIAGGIO = "INSERT INTO viaggi (destinazione, descrizione, durata, prezzo, assicurazione, data_partenza, data_ritorno, trasporto, posti_disponibili, valutazione) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

export const UPDATE_VIAGGIO = "UPDATE viaggi SET destinazione = ?, descrizione = ?, durata = ?, prezzo = ?, assicurazione = ?, data_partenza = ?, data_ritorno = ?, trasporto = ?, posti_disponibili = ?, valutazione = ? WHERE id = ?";

export const DELETE_VIAGGIO = "DELETE FROM viaggi WHERE id = ?";

export const SEARCH_VIAGGI = `SELECT * FROM viaggi WHERE
    (CAST(? AS TEXT) IS NULL OR LOWER(destinazione) LIKE '%' || LOWER(?) || '%') AND
    (CAST(? AS TEXT) IS NULL OR trasporto = ?) AND
    (CAST(? AS TEXT) IS NULL OR data_partenza = ?) AND
    (CAST(? AS REAL) IS NULL OR prezzo >= ?) AND
    (CAST(? AS REAL) IS NULL OR prezzo <= ?)`;
