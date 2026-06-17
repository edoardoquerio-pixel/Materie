import express from 'express';
import { db } from '../server.js';
import { SELECT_ALL, SELECT_BY_ID, SELECT_BY_NOME, SELECT_BY_COGNOME, INSERT_CLIENTE,
    UPDATE_CLIENTE, DELETE_CLIENTE } from '../database/script_clienti.js';

const clientiRouter = express.Router();

clientiRouter.get("/", (req, res) => {
    console.log("GET /api/v2/clienti");
    db.all(SELECT_ALL, [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json(rows);
        }
    });
});

clientiRouter.get("/search", (req, res) => {
    const { nome, cognome } = req.query;
    console.log("GET /api/v2/clienti/search");

    if (!nome && !cognome) {
        res.status(400).json({ error: "Almeno uno tra nome e cognome è richiesto" });
        return;
    }

    if (nome && cognome) {
        // cerca per entrambi
        const sql = "SELECT * FROM clienti WHERE LOWER(nome) LIKE '%' || LOWER(?) || '%' AND LOWER(cognome) LIKE '%' || LOWER(?) || '%'";
        db.all(sql, [nome, cognome], (err, rows) => {
            if (err) { res.status(500).json({ error: err.message }); return; }
            res.json(rows);
        });
    } else if (nome) {
        db.all(SELECT_BY_NOME, [nome], (err, rows) => {
            if (err) { res.status(500).json({ error: err.message }); return; }
            res.json(rows);
        });
    } else {
        db.all(SELECT_BY_COGNOME, [cognome], (err, rows) => {
            if (err) { res.status(500).json({ error: err.message }); return; }
            res.json(rows);
        });
    }
});

clientiRouter.get("/:id", (req, res) => {
    console.log(`GET /api/v2/clienti/${req.params.id}`);

    db.get(SELECT_BY_ID, [req.params.id], function(err, row) {
        if (err) {
            res.status(500).json({ error: err.message });
        } else if (!row) {
            res.status(404).json({ message: "Cliente non trovato con l'id specificato" });
        } else {
            res.json(row);
        }
    });
});

clientiRouter.post("/", (req, res) => {
    console.log("POST /api/v2/clienti");

    const errorMessage = validaCliente(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    const { nome, cognome, email, telefono } = req.body;

    db.run(INSERT_CLIENTE, [nome, cognome, email, telefono || null], function(err) {
        if (err) {
            // UNIQUE constraint violation su email
            if (err.message && err.message.includes("UNIQUE constraint failed")) {
                res.status(409).json({ error: "Email già registrata. Utilizzare un'altra email." });
                return;
            }
            res.status(500).json({ error: err.message });
            return;
        }
        res.status(201).json({ message: `Cliente creato con ID ${this.lastID}` });
    });
});

clientiRouter.put("/:id", (req, res) => {
    console.log(`PUT /api/v2/clienti/${req.params.id}`);

    const errorMessage = validaCliente(req.body);
    if (errorMessage) {
        res.status(400).json({ error: errorMessage });
        return;
    }

    const { nome, cognome, email, telefono } = req.body;

    db.run(UPDATE_CLIENTE, [nome, cognome, email, telefono || null, req.params.id], function(err) {
        if (err) {
            if (err.message && err.message.includes("UNIQUE constraint failed")) {
                res.status(409).json({ error: "Email già registrata. Utilizzare un'altra email." });
                return;
            }
            res.status(500).json({ error: err.message });
            return;
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Cliente non presente in database" });
        } else {
            res.json({ message: "Cliente aggiornato con successo" });
        }
    });
});

clientiRouter.delete("/:id", (req, res) => {
    const id = req.params.id;
    console.log(`DELETE /api/v2/clienti/${id}`);

    db.run(DELETE_CLIENTE, [id], function(err) {
        if (err) {
            // FK constraint violation (cliente ha prenotazioni)
            if (err.message && err.message.includes("FOREIGN KEY constraint failed")) {
                res.status(400).json({ error: "Impossibile eliminare il cliente: ha prenotazioni attive." });
                return;
            }
            res.status(500).json({ error: err.message });
            return;
        } else if (this.changes === 0) {
            res.status(404).json({ message: "Cliente non presente in database" });
        } else {
            res.json({ message: "Cliente eliminato con successo" });
        }
    });
});

/* UTILITY */
function validaCliente(cliente) {
    let errorMessage;

    if (!cliente) {
        return "Cliente non presente.";
    }
    if (!cliente.nome || typeof cliente.nome !== 'string' || !cliente.nome.trim()) {
        errorMessage = "Nome obbligatorio.";
    }
    if (!cliente.cognome || typeof cliente.cognome !== 'string' || !cliente.cognome.trim()) {
        errorMessage = "Cognome obbligatorio.";
    }
    if (!cliente.email || typeof cliente.email !== 'string' || !cliente.email.trim()) {
        errorMessage = "Email obbligatoria.";
    } else if (!isValidEmail(cliente.email)) {
        errorMessage = "Email non valida.";
    }

    return errorMessage;
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

export default clientiRouter;
