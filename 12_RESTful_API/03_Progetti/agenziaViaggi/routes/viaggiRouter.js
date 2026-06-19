import express from 'express';
import { db } from "../server.js";
import { SELECT_ALL, SELECT_BY_ID, INSERT_VIAGGIO, UPDATE_VIAGGIO, DELETE_VIAGGIO, SEARCH_VIAGGI } from "../database/script_viaggi.js";

const viaggiRouter = express.Router();

viaggiRouter.get("/", (req, res) => {
    console.log("GET /api/v2/viaggi");

    db.all(SELECT_ALL, (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json(rows);
        }
    });
});

viaggiRouter.get("/search", (req, res) => {
    const { destinazione, trasporto, data_partenza, prezzo_min, prezzo_max } = req.query;
    console.log("GET /api/v2/viaggi/search");

    // tutti i parametri sono opzionali; se null/non forniti la condizione è TRUE
    const params = [
        destinazione || null, destinazione || null,
        trasporto || null, trasporto || null,
        data_partenza || null, data_partenza || null,
        prezzo_min || null, prezzo_min || null,
        prezzo_max || null, prezzo_max || null
    ];

    db.all(SEARCH_VIAGGI, params, (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

viaggiRouter.get("/:id", (req, res) => {
    console.log(`GET /api/v2/viaggi/${req.params.id}`);

    db.get(SELECT_BY_ID, [req.params.id], function(err, row) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (!row) {
            res.status(404).json({ message: "Viaggio non trovato con l'id specificato" });
        } else {
            res.json(row);
        }
    });
});

viaggiRouter.post("/", (req, res) => {
    console.log("POST /api/v2/viaggi");

    const errorMessage = validaViaggio(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    const { destinazione, descrizione, durata, prezzo, assicurazione, data_partenza, data_ritorno, trasporto, posti_disponibili, valutazione } = req.body;

    db.run(INSERT_VIAGGIO, [
        destinazione, descrizione || null, durata, prezzo,
        assicurazione ? 1 : 0, data_partenza || null, data_ritorno || null,
        trasporto, posti_disponibili || null, valutazione || null
    ], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.status(201).json({ message: `Viaggio creato con ID ${this.lastID}` });
    });
});

viaggiRouter.put("/:id", (req, res) => {
    console.log(`PUT /api/v2/viaggi/${req.params.id}`);

    const errorMessage = validaViaggio(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    const { destinazione, descrizione, durata, prezzo, assicurazione, data_partenza, data_ritorno, trasporto, posti_disponibili, valutazione } = req.body;

    db.run(UPDATE_VIAGGIO, [
        destinazione, descrizione || null, durata, prezzo,
        assicurazione ? 1 : 0, data_partenza || null, data_ritorno || null,
        trasporto, posti_disponibili || null, valutazione || null,
        req.params.id
    ], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Viaggio non presente in database" });
        } else {
            res.json({ message: "Viaggio aggiornato con successo" });
        }
    });
});

viaggiRouter.delete("/:id", (req, res) => {
    const id = req.params.id;
    console.log(`DELETE /api/v2/viaggi/${id}`);

    db.run(DELETE_VIAGGIO, [id], function(err) {
        if (err) {
            if (err.message && err.message.includes("FOREIGN KEY constraint failed")) {
                res.status(400).json({ error: "Impossibile eliminare il viaggio: ci sono prenotazioni attive." });
                return;
            }
            res.status(500).json({ error: err.message });
            return;
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Viaggio non presente in database" });
        } else {
            res.json({ message: "Viaggio eliminato con successo" });
        }
    });
});

/* UTILITY */
function validaViaggio(viaggio) {
    let errorMessage;

    if (!viaggio) {
        return "Viaggio non presente.";
    }
    if (!viaggio.destinazione || typeof viaggio.destinazione !== 'string' || !viaggio.destinazione.trim()) {
        errorMessage = "Destinazione obbligatoria.";
    }
    if (!viaggio.durata || isNaN(viaggio.durata) || viaggio.durata <= 0) {
        errorMessage = "Durata deve essere un numero positivo.";
    }
    if (viaggio.prezzo === undefined || isNaN(viaggio.prezzo) || viaggio.prezzo <= 0) {
        errorMessage = "Prezzo deve essere un numero positivo.";
    }
    if (!viaggio.trasporto || !['aereo','treno','nave','bus','auto'].includes(viaggio.trasporto)) {
        errorMessage = "Trasporto non valido. Valori ammessi: aereo, treno, nave, bus, auto.";
    }
    if (viaggio.valutazione !== undefined && viaggio.valutazione !== null) {
        const v = Number(viaggio.valutazione);
        if (isNaN(v) || v < 1 || v > 5 || !Number.isInteger(v)) {
            errorMessage = "Valutazione deve essere un intero tra 1 e 5.";
        }
    }

    return errorMessage;
}

export default viaggiRouter;
