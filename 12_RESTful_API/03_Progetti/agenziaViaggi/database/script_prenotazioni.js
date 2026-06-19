export const CREATE_TABLE_PRENOTAZIONI = `CREATE TABLE IF NOT EXISTS prenotazioni (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            viaggio_id INTEGER NOT NULL REFERENCES viaggi(id),
                                            cliente_id INTEGER NOT NULL REFERENCES clienti(id),
                                            data_prenotazione TEXT NOT NULL,
                                            partecipanti INTEGER NOT NULL DEFAULT 1,
                                            note TEXT
                                        )`;

export const SELECT_ALL = `SELECT prenotazioni.*, viaggi.destinazione AS viaggio_destinazione, clienti.nome AS cliente_nome, clienti.cognome AS cliente_cognome
                           FROM prenotazioni
                           JOIN viaggi ON prenotazioni.viaggio_id = viaggi.id
                           JOIN clienti ON prenotazioni.cliente_id = clienti.id`;

export const SELECT_BY_ID = `SELECT prenotazioni.*, viaggi.destinazione AS viaggio_destinazione, clienti.nome AS cliente_nome, clienti.cognome AS cliente_cognome
                             FROM prenotazioni
                             JOIN viaggi ON prenotazioni.viaggio_id = viaggi.id
                             JOIN clienti ON prenotazioni.cliente_id = clienti.id
                             WHERE prenotazioni.id = ?`;

export const SELECT_BY_VIAGGIO_ID = "SELECT * FROM prenotazioni WHERE viaggio_id = ?";

export const SELECT_BY_CLIENTE_ID = "SELECT * FROM prenotazioni WHERE cliente_id = ?";

export const INSERT_PRENOTAZIONE = "INSERT INTO prenotazioni (viaggio_id, cliente_id, data_prenotazione, partecipanti, note) VALUES (?, ?, ?, ?, ?)";

export const UPDATE_PRENOTAZIONE = "UPDATE prenotazioni SET viaggio_id = ?, cliente_id = ?, data_prenotazione = ?, partecipanti = ?, note = ? WHERE id = ?";

export const DELETE_PRENOTAZIONE = "DELETE FROM prenotazioni WHERE id = ?";
