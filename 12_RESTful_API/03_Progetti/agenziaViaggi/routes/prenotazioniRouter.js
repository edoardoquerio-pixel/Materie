import express from 'express';
import { db } from '../server.js';
import { SELECT_ALL, SELECT_BY_ID, INSERT_PRENOTAZIONE, UPDATE_PRENOTAZIONE, DELETE_PRENOTAZIONE } from '../database/script_prenotazioni.js';

const prenotazioniRouter = express.Router();

prenotazioniRouter.get("/", (req, res) => {
    console.log("GET /api/v2/prenotazioni");

    db.all(SELECT_ALL, (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json(rows);
        }
    });
});

prenotazioniRouter.get("/search", (req, res) => {
    const { viaggio_id, cliente_id, data_prenotazione } = req.query;
    console.log("GET /api/v2/prenotazioni/search");

    let conditions = [];
    let params = [];

    if (viaggio_id) {
        conditions.push("viaggio_id = ?");
        params.push(viaggio_id);
    }
    if (cliente_id) {
        conditions.push("cliente_id = ?");
        params.push(cliente_id);
    }
    if (data_prenotazione) {
        conditions.push("data_prenotazione = ?");
        params.push(data_prenotazione);
    }

    if (conditions.length === 0) {
        res.status(400).json({ error: "Almeno un parametro di ricerca è richiesto (viaggio_id, cliente_id, data_prenotazione)" });
        return;
    }

    const sql = `SELECT * FROM prenotazioni WHERE ${conditions.join(" AND ")}`;

    db.all(sql, params, (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

prenotazioniRouter.get("/:id", (req, res) => {
    console.log(`GET /api/v2/prenotazioni/${req.params.id}`);

    db.get(SELECT_BY_ID, [req.params.id], function(err, row) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (!row) {
            res.status(404).json({ message: "Prenotazione non trovata con l'id specificato" });
        } else {
            res.json(row);
        }
    });
});

prenotazioniRouter.post("/", (req, res) => {
    console.log("POST /api/v2/prenotazioni");

    const errorMessage = validaPrenotazione(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    const { viaggio_id, cliente_id, partecipanti, note } = req.body;

    // Verifica esistenza viaggio e cliente prima di inserire
    db.get("SELECT id FROM viaggi WHERE id = ?", [viaggio_id], (err, viaggio) => {
        if (err) { res.status(500).json({ error: err.message }); return; }
        if (!viaggio) {
            res.status(400).json({ error: "Viaggio non trovato con l'id specificato." });
            return;
        }

        db.get("SELECT id FROM clienti WHERE id = ?", [cliente_id], (err, cliente) => {
            if (err) { res.status(500).json({ error: err.message }); return; }
            if (!cliente) {
                res.status(400).json({ error: "Cliente non trovato con l'id specificato." });
                return;
            }

            // data_prenotazione auto-generata dal server
            const dataPrenotazione = new Date().toISOString().split('T')[0];

            db.run(INSERT_PRENOTAZIONE, [viaggio_id, cliente_id, dataPrenotazione, partecipanti || 1, note || null], function(err) {
                if (err) {
                    res.status(500).json({ error: err.message });
                    return;
                }
                res.status(201).json({ message: `Prenotazione creata con ID ${this.lastID}` });
            });
        });
    });
});

prenotazioniRouter.put("/:id", (req, res) => {
    console.log(`PUT /api/v2/prenotazioni/${req.params.id}`);

    const errorMessage = validaPrenotazione(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    const { viaggio_id, cliente_id, data_prenotazione, partecipanti, note } = req.body;

    db.run(UPDATE_PRENOTAZIONE, [viaggio_id, cliente_id, data_prenotazione, partecipanti || 1, note || null, req.params.id], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Prenotazione non presente in database" });
        } else {
            res.json({ message: "Prenotazione aggiornata con successo" });
        }
    });
});

prenotazioniRouter.delete("/:id", (req, res) => {
    const id = req.params.id;
    console.log(`DELETE /api/v2/prenotazioni/${id}`);

    db.run(DELETE_PRENOTAZIONE, [id], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Prenotazione non presente in database" });
        } else {
            res.json({ message: "Prenotazione eliminata con successo" });
        }
    });
});

/* UTILITY */
function validaPrenotazione(prenotazione) {
    let errorMessage;

    if (!prenotazione) {
        return "Prenotazione non presente.";
    }
    if (!prenotazione.viaggio_id || isNaN(prenotazione.viaggio_id)) {
        errorMessage = "viaggio_id obbligatorio e deve essere numerico.";
    }
    if (!prenotazione.cliente_id || isNaN(prenotazione.cliente_id)) {
        errorMessage = "cliente_id obbligatorio e deve essere numerico.";
    }
    if (prenotazione.partecipanti !== undefined && prenotazione.partecipanti !== null) {
        if (isNaN(prenotazione.partecipanti) || prenotazione.partecipanti < 1) {
            errorMessage = "partecipanti deve essere almeno 1.";
        }
    }

    return errorMessage;
}

export default prenotazioniRouter;
