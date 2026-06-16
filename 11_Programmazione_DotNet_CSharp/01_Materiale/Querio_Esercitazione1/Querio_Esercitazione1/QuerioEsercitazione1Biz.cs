namespace Querio_Esercitazione1
{
    public class QuerioEsercitazione1Biz
    {
        //propietà

        public List<Venditore> Venditori { get; set; }
        public ResponsabileVenditori Responsabile { get; set; }
        public List<Ordine> Ordini { get; set; }
        public CapoOfficina Capo { get; set; }

        //costruttore

        public QuerioEsercitazione1Biz()
        {
            //============================================================//
            //  25 VENDITORI                                               //
            //============================================================//

            Venditore v1 = new Venditore { Nome = "Mario", Cognome = "Rossi", Stipendio = 2500, Settore = SettoreVendite.Auto };
            Venditore v2 = new Venditore { Nome = "Luca", Cognome = "Bianchi", Stipendio = 2700, Settore = SettoreVendite.Auto };
            Venditore v3 = new Venditore { Nome = "Giulia", Cognome = "Verdi", Stipendio = 2400, Settore = SettoreVendite.Moto };
            Venditore v4 = new Venditore { Nome = "Marco", Cognome = "Neri", Stipendio = 2600, Settore = SettoreVendite.Moto };
            Venditore v5 = new Venditore { Nome = "Anna", Cognome = "Gialli", Stipendio = 2550, Settore = SettoreVendite.Auto };
            Venditore v6 = new Venditore { Nome = "Paolo", Cognome = "Marroni", Stipendio = 2450, Settore = SettoreVendite.Moto };
            Venditore v7 = new Venditore { Nome = "Sara", Cognome = "Viola", Stipendio = 2650, Settore = SettoreVendite.Auto };
            Venditore v8 = new Venditore { Nome = "Davide", Cognome = "Azzurri", Stipendio = 2350, Settore = SettoreVendite.Moto };
            Venditore v9 = new Venditore { Nome = "Elena", Cognome = "Ferrari", Stipendio = 2750, Settore = SettoreVendite.Auto };
            Venditore v10 = new Venditore { Nome = "Andrea", Cognome = "Russo", Stipendio = 2300, Settore = SettoreVendite.Moto };
            Venditore v11 = new Venditore { Nome = "Francesca", Cognome = "Colombo", Stipendio = 2800, Settore = SettoreVendite.Auto };
            Venditore v12 = new Venditore { Nome = "Roberto", Cognome = "Ricci", Stipendio = 2450, Settore = SettoreVendite.Moto };
            Venditore v13 = new Venditore { Nome = "Chiara", Cognome = "Moretti", Stipendio = 2600, Settore = SettoreVendite.Auto };
            Venditore v14 = new Venditore { Nome = "Simone", Cognome = "Conti", Stipendio = 2500, Settore = SettoreVendite.Moto };
            Venditore v15 = new Venditore { Nome = "Valentina", Cognome = "Costa", Stipendio = 2700, Settore = SettoreVendite.Auto };
            Venditore v16 = new Venditore { Nome = "Alessandro", Cognome = "Mancini", Stipendio = 2400, Settore = SettoreVendite.Moto };
            Venditore v17 = new Venditore { Nome = "Martina", Cognome = "Romano", Stipendio = 2550, Settore = SettoreVendite.Auto };
            Venditore v18 = new Venditore { Nome = "Fabio", Cognome = "Sanna", Stipendio = 2650, Settore = SettoreVendite.Moto };
            Venditore v19 = new Venditore { Nome = "Laura", Cognome = "De Luca", Stipendio = 2450, Settore = SettoreVendite.Auto };
            Venditore v20 = new Venditore { Nome = "Matteo", Cognome = "Gallo", Stipendio = 2750, Settore = SettoreVendite.Moto };
            Venditore v21 = new Venditore { Nome = "Silvia", Cognome = "Rinaldi", Stipendio = 2300, Settore = SettoreVendite.Auto };
            Venditore v22 = new Venditore { Nome = "Stefano", Cognome = "Caruso", Stipendio = 2600, Settore = SettoreVendite.Moto };
            Venditore v23 = new Venditore { Nome = "Giorgia", Cognome = "Greco", Stipendio = 2500, Settore = SettoreVendite.Auto };
            Venditore v24 = new Venditore { Nome = "Federico", Cognome = "Barbieri", Stipendio = 2700, Settore = SettoreVendite.Moto };
            Venditore v25 = new Venditore { Nome = "Beatrice", Cognome = "Fontana", Stipendio = 2400, Settore = SettoreVendite.Auto };

            this.Venditori = new List<Venditore> { v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25 };

            //============================================================//
            //  RESPONSABILE VENDITORI                                      //
            //============================================================//

            this.Responsabile = new ResponsabileVenditori
            {
                Nome = "Alessio",
                Cognome = "Rizzi",
                Stipendio = 4000,
                Settore = SettoreVendite.Auto,
                Venditori = this.Venditori
            };

            //============================================================//
            //  50 PRODOTTI                                                //
            //============================================================//

            Prodotto p1 = new Prodotto { Codice = "P001", Denominazione = "Pastiglie freno", Descrizione = "Set pastiglie freno anteriori", Prezzo = 45.50, Giacenza = 30 };
            Prodotto p2 = new Prodotto { Codice = "P002", Denominazione = "Olio motore 5W40", Descrizione = "Lattina olio motore 5W40 4L", Prezzo = 38.90, Giacenza = 50 };
            Prodotto p3 = new Prodotto { Codice = "P003", Denominazione = "Filtro aria", Descrizione = "Filtro aria abitacolo", Prezzo = 22.30, Giacenza = 40 };
            Prodotto p4 = new Prodotto { Codice = "P004", Denominazione = "Ammortizzatore", Descrizione = "Ammortizzatore posteriore", Prezzo = 120, Giacenza = 15 };
            Prodotto p5 = new Prodotto { Codice = "P005", Denominazione = "Batteria auto", Descrizione = "Batteria 12V 60Ah", Prezzo = 95, Giacenza = 20 };
            Prodotto p6 = new Prodotto { Codice = "P006", Denominazione = "Candela accensione", Descrizione = "Candela accensione iridio", Prezzo = 12.50, Giacenza = 100 };
            Prodotto p7 = new Prodotto { Codice = "P007", Denominazione = "Parabrezza", Descrizione = "Parabrezza anteriore", Prezzo = 250, Giacenza = 8 };
            Prodotto p8 = new Prodotto { Codice = "P008", Denominazione = "Catenone moto", Descrizione = "Catenone trasmissione moto", Prezzo = 85, Giacenza = 12 };
            Prodotto p9 = new Prodotto { Codice = "P009", Denominazione = "Disco freno", Descrizione = "Disco freno anteriore", Prezzo = 65, Giacenza = 25 };
            Prodotto p10 = new Prodotto { Codice = "P010", Denominazione = "Liquido raffreddamento", Descrizione = "Liquido raffreddamento 5L", Prezzo = 32, Giacenza = 35 };
            Prodotto p11 = new Prodotto { Codice = "P011", Denominazione = "Filtro olio", Descrizione = "Filtro olio motore", Prezzo = 18, Giacenza = 60 };
            Prodotto p12 = new Prodotto { Codice = "P012", Denominazione = "Cinghia distribuzione", Descrizione = "Cinghia distribuzione completa", Prezzo = 180, Giacenza = 10 };
            Prodotto p13 = new Prodotto { Codice = "P013", Denominazione = "Radiatore", Descrizione = "Radiatore raffreddamento", Prezzo = 210, Giacenza = 8 };
            Prodotto p14 = new Prodotto { Codice = "P014", Denominazione = "Alternatore", Descrizione = "Alternatore 12V 120A", Prezzo = 160, Giacenza = 12 };
            Prodotto p15 = new Prodotto { Codice = "P015", Denominazione = "Motorino avviamento", Descrizione = "Motorino avviamento 12V", Prezzo = 140, Giacenza = 10 };
            Prodotto p16 = new Prodotto { Codice = "P016", Denominazione = "Faro anteriore", Descrizione = "Faro anteriore LED", Prezzo = 90, Giacenza = 20 };
            Prodotto p17 = new Prodotto { Codice = "P017", Denominazione = "Specchietto retrovisore", Descrizione = "Specchietto retrovisore elettrico", Prezzo = 55, Giacenza = 18 };
            Prodotto p18 = new Prodotto { Codice = "P018", Denominazione = "Pneumatico 205/55R16", Descrizione = "Pneumatico estivo 205/55 R16", Prezzo = 110, Giacenza = 30 };
            Prodotto p19 = new Prodotto { Codice = "P019", Denominazione = "Pneumatico 225/45R17", Descrizione = "Pneumatico estivo 225/45 R17", Prezzo = 130, Giacenza = 25 };
            Prodotto p20 = new Prodotto { Codice = "P020", Denominazione = "Cerchio lega 16", Descrizione = "Cerchio in lega 16 pollici", Prezzo = 150, Giacenza = 15 };
            Prodotto p21 = new Prodotto { Codice = "P021", Denominazione = "Frizione", Descrizione = "Kit frizione completo", Prezzo = 200, Giacenza = 5 };
            Prodotto p22 = new Prodotto { Codice = "P022", Denominazione = "Scarico completo", Descrizione = "Impianto di scarico completo", Prezzo = 280, Giacenza = 6 };
            Prodotto p23 = new Prodotto { Codice = "P023", Denominazione = "Sospensione anteriore", Descrizione = "Molle sospensione anteriori", Prezzo = 95, Giacenza = 18 };
            Prodotto p24 = new Prodotto { Codice = "P024", Denominazione = "Braccetto sospensione", Descrizione = "Braccetto sospensione completo", Prezzo = 75, Giacenza = 22 };
            Prodotto p25 = new Prodotto { Codice = "P025", Denominazione = "Barra stabilizzatrice", Descrizione = "Barra stabilizzatrice anteriore", Prezzo = 120, Giacenza = 14 };
            Prodotto p26 = new Prodotto { Codice = "P026", Denominazione = "Liquido freni", Descrizione = "Liquido freni DOT 4 500ml", Prezzo = 8.50, Giacenza = 80 };
            Prodotto p27 = new Prodotto { Codice = "P027", Denominazione = "Antigelo", Descrizione = "Liquido antigelo parabrezza", Prezzo = 5.90, Giacenza = 70 };
            Prodotto p28 = new Prodotto { Codice = "P028", Denominazione = "Lampadina LED", Descrizione = "Lampadina LED H7", Prezzo = 15, Giacenza = 45 };
            Prodotto p29 = new Prodotto { Codice = "P029", Denominazione = "Tergicristallo", Descrizione = "Coppia tergicristallo anteriore", Prezzo = 22, Giacenza = 55 };
            Prodotto p30 = new Prodotto { Codice = "P030", Denominazione = "Fluido cambio", Descrizione = "Olio cambio manuale 2L", Prezzo = 45, Giacenza = 20 };
            Prodotto p31 = new Prodotto { Codice = "P031", Denominazione = "Guarnizione testata", Descrizione = "Kit guarnizione testata motore", Prezzo = 35, Giacenza = 12 };
            Prodotto p32 = new Prodotto { Codice = "P032", Denominazione = "Pompa acqua", Descrizione = "Pompa acqua raffreddamento", Prezzo = 70, Giacenza = 15 };
            Prodotto p33 = new Prodotto { Codice = "P033", Denominazione = "Termostato", Descrizione = "Termostato motore 88 gradi", Prezzo = 25, Giacenza = 20 };
            Prodotto p34 = new Prodotto { Codice = "P034", Denominazione = "Sensore pressione olio", Descrizione = "Sensore pressione olio motore", Prezzo = 42, Giacenza = 18 };
            Prodotto p35 = new Prodotto { Codice = "P035", Denominazione = "Sonda lambda", Descrizione = "Sonda lambda universale", Prezzo = 88, Giacenza = 10 };
            Prodotto p36 = new Prodotto { Codice = "P036", Denominazione = "Bobina accensione", Descrizione = "Bobina accensione motore", Prezzo = 60, Giacenza = 25 };
            Prodotto p37 = new Prodotto { Codice = "P037", Denominazione = "Iniettore", Descrizione = "Iniettore carburante", Prezzo = 95, Giacenza = 12 };
            Prodotto p38 = new Prodotto { Codice = "P038", Denominazione = "Pompa benzina", Descrizione = "Pompa carburante elettrica", Prezzo = 130, Giacenza = 8 };
            Prodotto p39 = new Prodotto { Codice = "P039", Denominazione = "Filtro carburante", Descrizione = "Filtro carburante diesel", Prezzo = 28, Giacenza = 30 };
            Prodotto p40 = new Prodotto { Codice = "P040", Denominazione = "Tubo flessibile freno", Descrizione = "Tubo freno anteriore sinistro", Prezzo = 18, Giacenza = 40 };
            Prodotto p41 = new Prodotto { Codice = "P041", Denominazione = "Molle anteriori", Descrizione = "Molle sospensione anteriori", Prezzo = 105, Giacenza = 16 };
            Prodotto p42 = new Prodotto { Codice = "P042", Denominazione = "Molle posteriori", Descrizione = "Molle sospensione posteriori", Prezzo = 105, Giacenza = 16 };
            Prodotto p43 = new Prodotto { Codice = "P043", Denominazione = "Ammortizzatore posteriore", Descrizione = "Ammortizzatore posteriore destro", Prezzo = 115, Giacenza = 12 };
            Prodotto p44 = new Prodotto { Codice = "P044", Denominazione = "Cuscinetto ruota", Descrizione = "Cuscinetto ruota anteriore", Prezzo = 55, Giacenza = 22 };
            Prodotto p45 = new Prodotto { Codice = "P045", Denominazione = "Giunto omocinetico", Descrizione = "Giunto omocinetico completo", Prezzo = 85, Giacenza = 14 };
            Prodotto p46 = new Prodotto { Codice = "P046", Denominazione = "Parafango anteriore", Descrizione = "Parafango anteriore sinistro", Prezzo = 45, Giacenza = 20 };
            Prodotto p47 = new Prodotto { Codice = "P047", Denominazione = "Paraurti posteriore", Descrizione = "Paraurti posteriore completo", Prezzo = 190, Giacenza = 5 };
            Prodotto p48 = new Prodotto { Codice = "P048", Denominazione = "Griglia anteriore", Descrizione = "Griglia anteriore cromata", Prezzo = 65, Giacenza = 15 };
            Prodotto p49 = new Prodotto { Codice = "P049", Denominazione = "Tappetini auto", Descrizione = "Set tappetini auto 4 pezzi", Prezzo = 35, Giacenza = 35 };
            Prodotto p50 = new Prodotto { Codice = "P050", Denominazione = "Porta oggetti", Descrizione = "Porta oggetti bracciolo centrale", Prezzo = 40, Giacenza = 28 };

            //============================================================//
            //  25 MECCANICI                                               //
            //============================================================//

            Meccanico m1 = new Meccanico { Nome = "Antonio", Cognome = "Rinaldi", Stipendio = 2300, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m2 = new Meccanico { Nome = "Francesco", Cognome = "Caruso", Stipendio = 2400, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m3 = new Meccanico { Nome = "Giovanni", Cognome = "Greco", Stipendio = 2350, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m4 = new Meccanico { Nome = "Lorenzo", Cognome = "Barbieri", Stipendio = 2450, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m5 = new Meccanico { Nome = "Alberto", Cognome = "Fontana", Stipendio = 2250, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m6 = new Meccanico { Nome = "Daniele", Cognome = "Rizzi", Stipendio = 2500, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m7 = new Meccanico { Nome = "Pietro", Cognome = "Milani", Stipendio = 2400, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m8 = new Meccanico { Nome = "Vincenzo", Cognome = "Fabbri", Stipendio = 2350, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m9 = new Meccanico { Nome = "Salvatore", Cognome = "Monti", Stipendio = 2450, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m10 = new Meccanico { Nome = "Gianni", Cognome = "Leone", Stipendio = 2300, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m11 = new Meccanico { Nome = "Michele", Cognome = "Costa", Stipendio = 2500, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m12 = new Meccanico { Nome = "Claudio", Cognome = "Mancini", Stipendio = 2250, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m13 = new Meccanico { Nome = "Maurizio", Cognome = "Romano", Stipendio = 2400, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m14 = new Meccanico { Nome = "Enrico", Cognome = "Sanna", Stipendio = 2350, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m15 = new Meccanico { Nome = "Filippo", Cognome = "De Luca", Stipendio = 2450, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m16 = new Meccanico { Nome = "Giacomo", Cognome = "Gallo", Stipendio = 2300, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m17 = new Meccanico { Nome = "Luigi", Cognome = "Ricci", Stipendio = 2500, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m18 = new Meccanico { Nome = "Renato", Cognome = "Moretti", Stipendio = 2400, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m19 = new Meccanico { Nome = "Massimo", Cognome = "Conti", Stipendio = 2350, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m20 = new Meccanico { Nome = "Angelo", Cognome = "Verdi", Stipendio = 2450, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m21 = new Meccanico { Nome = "Riccardo", Cognome = "Bianchi", Stipendio = 2250, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m22 = new Meccanico { Nome = "Emanuele", Cognome = "Neri", Stipendio = 2400, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m23 = new Meccanico { Nome = "Giorgio", Cognome = "Rossi", Stipendio = 2500, Tipologia = TipologiaMeccanico.Meccanica };
            Meccanico m24 = new Meccanico { Nome = "Raffaele", Cognome = "Gialli", Stipendio = 2350, Tipologia = TipologiaMeccanico.Carrozzeria };
            Meccanico m25 = new Meccanico { Nome = "Domenico", Cognome = "Marroni", Stipendio = 2300, Tipologia = TipologiaMeccanico.Meccanica };

            //============================================================//
            //  100 ORDINI                                                //
            //============================================================//

            this.Ordini = new List<Ordine>();

            Ordine o1 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 10), ElencoProdotti = new List<Prodotto> { p1, p1, p2, p3, p5 }, Venditore = v1 };
            this.Ordini.Add(o1);
            Ordine o2 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 12), ElencoProdotti = new List<Prodotto> { p3, p6, p6, p6, p8 }, Venditore = v3 };
            this.Ordini.Add(o2);
            Ordine o3 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 14), ElencoProdotti = new List<Prodotto> { p1, p2, p4, p7, p7, p8 }, Venditore = v2 };
            this.Ordini.Add(o3);
            Ordine o4 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 15), ElencoProdotti = new List<Prodotto> { p9, p9, p10, p11 }, Venditore = v4 };
            this.Ordini.Add(o4);
            Ordine o5 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 16), ElencoProdotti = new List<Prodotto> { p12, p13, p14 }, Venditore = v5 };
            this.Ordini.Add(o5);
            Ordine o6 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 17), ElencoProdotti = new List<Prodotto> { p15, p16, p16, p17 }, Venditore = v6 };
            this.Ordini.Add(o6);
            Ordine o7 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 18), ElencoProdotti = new List<Prodotto> { p18, p19, p20, p20 }, Venditore = v7 };
            this.Ordini.Add(o7);
            Ordine o8 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 19), ElencoProdotti = new List<Prodotto> { p1, p3, p6, p9, p12 }, Venditore = v8 };
            this.Ordini.Add(o8);
            Ordine o9 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 20), ElencoProdotti = new List<Prodotto> { p21, p22, p22, p23 }, Venditore = v9 };
            this.Ordini.Add(o9);
            Ordine o10 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 21), ElencoProdotti = new List<Prodotto> { p24, p25, p26, p26, p27 }, Venditore = v10 };
            this.Ordini.Add(o10);
            Ordine o11 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 22), ElencoProdotti = new List<Prodotto> { p28, p29, p29, p30 }, Venditore = v11 };
            this.Ordini.Add(o11);
            Ordine o12 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 23), ElencoProdotti = new List<Prodotto> { p31, p32, p33 }, Venditore = v12 };
            this.Ordini.Add(o12);
            Ordine o13 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 24), ElencoProdotti = new List<Prodotto> { p34, p35, p35, p36 }, Venditore = v13 };
            this.Ordini.Add(o13);
            Ordine o14 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 25), ElencoProdotti = new List<Prodotto> { p37, p38, p39 }, Venditore = v14 };
            this.Ordini.Add(o14);
            Ordine o15 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 26), ElencoProdotti = new List<Prodotto> { p40, p41, p42 }, Venditore = v15 };
            this.Ordini.Add(o15);
            Ordine o16 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 27), ElencoProdotti = new List<Prodotto> { p1, p2, p6, p7, p10, p11 }, Venditore = v16 };
            this.Ordini.Add(o16);
            Ordine o17 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 28), ElencoProdotti = new List<Prodotto> { p43, p44, p44, p45 }, Venditore = v17 };
            this.Ordini.Add(o17);
            Ordine o18 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 29), ElencoProdotti = new List<Prodotto> { p46, p47, p48, p48 }, Venditore = v18 };
            this.Ordini.Add(o18);
            Ordine o19 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 30), ElencoProdotti = new List<Prodotto> { p49, p50, p1, p3 }, Venditore = v19 };
            this.Ordini.Add(o19);
            Ordine o20 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 1), ElencoProdotti = new List<Prodotto> { p4, p5, p7, p9, p13 }, Venditore = v20 };
            this.Ordini.Add(o20);
            Ordine o21 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 2), ElencoProdotti = new List<Prodotto> { p2, p3, p6, p6, p8, p10 }, Venditore = v21 };
            this.Ordini.Add(o21);
            Ordine o22 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 3), ElencoProdotti = new List<Prodotto> { p12, p14, p15, p16 }, Venditore = v22 };
            this.Ordini.Add(o22);
            Ordine o23 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 4), ElencoProdotti = new List<Prodotto> { p17, p18, p19, p21 }, Venditore = v23 };
            this.Ordini.Add(o23);
            Ordine o24 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 5), ElencoProdotti = new List<Prodotto> { p22, p23, p24, p25 }, Venditore = v24 };
            this.Ordini.Add(o24);
            Ordine o25 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 6), ElencoProdotti = new List<Prodotto> { p26, p27, p28, p29, p30 }, Venditore = v25 };
            this.Ordini.Add(o25);
            Ordine o26 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 7), ElencoProdotti = new List<Prodotto> { p31, p32, p33, p34 }, Venditore = v1 };
            this.Ordini.Add(o26);
            Ordine o27 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 8), ElencoProdotti = new List<Prodotto> { p35, p36, p37, p38 }, Venditore = v2 };
            this.Ordini.Add(o27);
            Ordine o28 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 9), ElencoProdotti = new List<Prodotto> { p39, p40, p41, p42 }, Venditore = v3 };
            this.Ordini.Add(o28);
            Ordine o29 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 10), ElencoProdotti = new List<Prodotto> { p43, p44, p45, p46 }, Venditore = v4 };
            this.Ordini.Add(o29);
            Ordine o30 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 11), ElencoProdotti = new List<Prodotto> { p47, p48, p49, p50 }, Venditore = v5 };
            this.Ordini.Add(o30);
            Ordine o31 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 12), ElencoProdotti = new List<Prodotto> { p1, p3, p5, p7, p9, p11 }, Venditore = v6 };
            this.Ordini.Add(o31);
            Ordine o32 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 13), ElencoProdotti = new List<Prodotto> { p2, p4, p6, p8, p10, p12 }, Venditore = v7 };
            this.Ordini.Add(o32);
            Ordine o33 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 14), ElencoProdotti = new List<Prodotto> { p13, p15, p17, p19, p21 }, Venditore = v8 };
            this.Ordini.Add(o33);
            Ordine o34 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 15), ElencoProdotti = new List<Prodotto> { p14, p16, p18, p20, p22 }, Venditore = v9 };
            this.Ordini.Add(o34);
            Ordine o35 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 16), ElencoProdotti = new List<Prodotto> { p23, p25, p27, p29, p31 }, Venditore = v10 };
            this.Ordini.Add(o35);
            Ordine o36 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 17), ElencoProdotti = new List<Prodotto> { p24, p26, p28, p30, p32 }, Venditore = v11 };
            this.Ordini.Add(o36);
            Ordine o37 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 18), ElencoProdotti = new List<Prodotto> { p33, p35, p37, p39, p41 }, Venditore = v12 };
            this.Ordini.Add(o37);
            Ordine o38 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 19), ElencoProdotti = new List<Prodotto> { p34, p36, p38, p40, p42 }, Venditore = v13 };
            this.Ordini.Add(o38);
            Ordine o39 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 20), ElencoProdotti = new List<Prodotto> { p43, p45, p47, p49 }, Venditore = v14 };
            this.Ordini.Add(o39);
            Ordine o40 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 21), ElencoProdotti = new List<Prodotto> { p44, p46, p48, p50 }, Venditore = v15 };
            this.Ordini.Add(o40);
            Ordine o41 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 22), ElencoProdotti = new List<Prodotto> { p1, p1, p2, p2, p3, p3 }, Venditore = v16 };
            this.Ordini.Add(o41);
            Ordine o42 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 23), ElencoProdotti = new List<Prodotto> { p4, p4, p5, p6, p7 }, Venditore = v17 };
            this.Ordini.Add(o42);
            Ordine o43 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 24), ElencoProdotti = new List<Prodotto> { p8, p9, p10, p11, p12 }, Venditore = v18 };
            this.Ordini.Add(o43);
            Ordine o44 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 25), ElencoProdotti = new List<Prodotto> { p13, p14, p15, p16, p17 }, Venditore = v19 };
            this.Ordini.Add(o44);
            Ordine o45 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 26), ElencoProdotti = new List<Prodotto> { p18, p19, p20, p21, p22 }, Venditore = v20 };
            this.Ordini.Add(o45);
            Ordine o46 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 27), ElencoProdotti = new List<Prodotto> { p23, p24, p25, p26, p27 }, Venditore = v21 };
            this.Ordini.Add(o46);
            Ordine o47 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 28), ElencoProdotti = new List<Prodotto> { p28, p29, p30, p31, p32 }, Venditore = v22 };
            this.Ordini.Add(o47);
            Ordine o48 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 29), ElencoProdotti = new List<Prodotto> { p33, p34, p35, p36, p37 }, Venditore = v23 };
            this.Ordini.Add(o48);
            Ordine o49 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 30), ElencoProdotti = new List<Prodotto> { p38, p39, p40, p41, p42 }, Venditore = v24 };
            this.Ordini.Add(o49);
            Ordine o50 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 1), ElencoProdotti = new List<Prodotto> { p43, p44, p45, p46, p47 }, Venditore = v25 };
            this.Ordini.Add(o50);
            Ordine o51 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 2), ElencoProdotti = new List<Prodotto> { p48, p49, p50, p1 }, Venditore = v1 };
            this.Ordini.Add(o51);
            Ordine o52 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 3), ElencoProdotti = new List<Prodotto> { p2, p3, p4, p5, p6 }, Venditore = v2 };
            this.Ordini.Add(o52);
            Ordine o53 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 4), ElencoProdotti = new List<Prodotto> { p7, p8, p9, p10, p11 }, Venditore = v3 };
            this.Ordini.Add(o53);
            Ordine o54 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 5), ElencoProdotti = new List<Prodotto> { p12, p13, p14, p15, p16 }, Venditore = v4 };
            this.Ordini.Add(o54);
            Ordine o55 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 6), ElencoProdotti = new List<Prodotto> { p17, p18, p19, p20, p21 }, Venditore = v5 };
            this.Ordini.Add(o55);
            Ordine o56 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 7), ElencoProdotti = new List<Prodotto> { p22, p23, p24, p25, p26 }, Venditore = v6 };
            this.Ordini.Add(o56);
            Ordine o57 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 8), ElencoProdotti = new List<Prodotto> { p27, p28, p29, p30, p31 }, Venditore = v7 };
            this.Ordini.Add(o57);
            Ordine o58 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 9), ElencoProdotti = new List<Prodotto> { p32, p33, p34, p35, p36 }, Venditore = v8 };
            this.Ordini.Add(o58);
            Ordine o59 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 10), ElencoProdotti = new List<Prodotto> { p37, p38, p39, p40, p41 }, Venditore = v9 };
            this.Ordini.Add(o59);
            Ordine o60 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 11), ElencoProdotti = new List<Prodotto> { p42, p43, p44, p45, p46 }, Venditore = v10 };
            this.Ordini.Add(o60);
            Ordine o61 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 12), ElencoProdotti = new List<Prodotto> { p47, p48, p49, p50, p1, p2 }, Venditore = v11 };
            this.Ordini.Add(o61);
            Ordine o62 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 13), ElencoProdotti = new List<Prodotto> { p3, p4, p5, p6, p7, p8 }, Venditore = v12 };
            this.Ordini.Add(o62);
            Ordine o63 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 14), ElencoProdotti = new List<Prodotto> { p9, p10, p11, p12, p13 }, Venditore = v13 };
            this.Ordini.Add(o63);
            Ordine o64 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 15), ElencoProdotti = new List<Prodotto> { p14, p15, p16, p17, p18 }, Venditore = v14 };
            this.Ordini.Add(o64);
            Ordine o65 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 16), ElencoProdotti = new List<Prodotto> { p19, p20, p21, p22, p23 }, Venditore = v15 };
            this.Ordini.Add(o65);
            Ordine o66 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 17), ElencoProdotti = new List<Prodotto> { p24, p25, p26, p27, p28 }, Venditore = v16 };
            this.Ordini.Add(o66);
            Ordine o67 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 18), ElencoProdotti = new List<Prodotto> { p29, p30, p31, p32, p33 }, Venditore = v17 };
            this.Ordini.Add(o67);
            Ordine o68 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 19), ElencoProdotti = new List<Prodotto> { p34, p35, p36, p37, p38 }, Venditore = v18 };
            this.Ordini.Add(o68);
            Ordine o69 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 20), ElencoProdotti = new List<Prodotto> { p39, p40, p41, p42, p43 }, Venditore = v19 };
            this.Ordini.Add(o69);
            Ordine o70 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 21), ElencoProdotti = new List<Prodotto> { p44, p45, p46, p47, p48 }, Venditore = v20 };
            this.Ordini.Add(o70);
            Ordine o71 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 22), ElencoProdotti = new List<Prodotto> { p49, p50, p1, p2, p3, p4 }, Venditore = v21 };
            this.Ordini.Add(o71);
            Ordine o72 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 23), ElencoProdotti = new List<Prodotto> { p5, p6, p7, p8, p9, p10 }, Venditore = v22 };
            this.Ordini.Add(o72);
            Ordine o73 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 24), ElencoProdotti = new List<Prodotto> { p11, p12, p13, p14, p15 }, Venditore = v23 };
            this.Ordini.Add(o73);
            Ordine o74 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 25), ElencoProdotti = new List<Prodotto> { p16, p17, p18, p19, p20 }, Venditore = v24 };
            this.Ordini.Add(o74);
            Ordine o75 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 26), ElencoProdotti = new List<Prodotto> { p21, p22, p23, p24, p25 }, Venditore = v25 };
            this.Ordini.Add(o75);
            Ordine o76 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 27), ElencoProdotti = new List<Prodotto> { p26, p27, p28, p29, p30 }, Venditore = v1 };
            this.Ordini.Add(o76);
            Ordine o77 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 28), ElencoProdotti = new List<Prodotto> { p31, p32, p33, p34, p35 }, Venditore = v2 };
            this.Ordini.Add(o77);
            Ordine o78 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 29), ElencoProdotti = new List<Prodotto> { p36, p37, p38, p39, p40 }, Venditore = v3 };
            this.Ordini.Add(o78);
            Ordine o79 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 30), ElencoProdotti = new List<Prodotto> { p41, p42, p43, p44, p45 }, Venditore = v4 };
            this.Ordini.Add(o79);
            Ordine o80 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 1), ElencoProdotti = new List<Prodotto> { p46, p47, p48, p49, p50 }, Venditore = v5 };
            this.Ordini.Add(o80);
            Ordine o81 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 2), ElencoProdotti = new List<Prodotto> { p1, p3, p5, p7, p9, p11, p13 }, Venditore = v6 };
            this.Ordini.Add(o81);
            Ordine o82 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 3), ElencoProdotti = new List<Prodotto> { p2, p4, p6, p8, p10, p12, p14 }, Venditore = v7 };
            this.Ordini.Add(o82);
            Ordine o83 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 4), ElencoProdotti = new List<Prodotto> { p15, p17, p19, p21, p23, p25 }, Venditore = v8 };
            this.Ordini.Add(o83);
            Ordine o84 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 5), ElencoProdotti = new List<Prodotto> { p16, p18, p20, p22, p24, p26 }, Venditore = v9 };
            this.Ordini.Add(o84);
            Ordine o85 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 6), ElencoProdotti = new List<Prodotto> { p27, p29, p31, p33, p35, p37 }, Venditore = v10 };
            this.Ordini.Add(o85);
            Ordine o86 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 7), ElencoProdotti = new List<Prodotto> { p28, p30, p32, p34, p36, p38 }, Venditore = v11 };
            this.Ordini.Add(o86);
            Ordine o87 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 8), ElencoProdotti = new List<Prodotto> { p39, p41, p43, p45, p47, p49 }, Venditore = v12 };
            this.Ordini.Add(o87);
            Ordine o88 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 9), ElencoProdotti = new List<Prodotto> { p40, p42, p44, p46, p48, p50 }, Venditore = v13 };
            this.Ordini.Add(o88);
            Ordine o89 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 10), ElencoProdotti = new List<Prodotto> { p1, p6, p11, p16, p21, p26 }, Venditore = v14 };
            this.Ordini.Add(o89);
            Ordine o90 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 11), ElencoProdotti = new List<Prodotto> { p31, p36, p41, p46, p50 }, Venditore = v15 };
            this.Ordini.Add(o90);
            Ordine o91 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 12), ElencoProdotti = new List<Prodotto> { p2, p7, p12, p17, p22, p27 }, Venditore = v16 };
            this.Ordini.Add(o91);
            Ordine o92 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 13), ElencoProdotti = new List<Prodotto> { p32, p37, p42, p47, p50, p1 }, Venditore = v17 };
            this.Ordini.Add(o92);
            Ordine o93 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 14), ElencoProdotti = new List<Prodotto> { p3, p8, p13, p18, p23, p28 }, Venditore = v18 };
            this.Ordini.Add(o93);
            Ordine o94 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 15), ElencoProdotti = new List<Prodotto> { p33, p38, p43, p48, p4, p9 }, Venditore = v19 };
            this.Ordini.Add(o94);
            Ordine o95 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 16), ElencoProdotti = new List<Prodotto> { p14, p19, p24, p29, p34, p39 }, Venditore = v20 };
            this.Ordini.Add(o95);
            Ordine o96 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 17), ElencoProdotti = new List<Prodotto> { p44, p49, p5, p10, p15, p20 }, Venditore = v21 };
            this.Ordini.Add(o96);
            Ordine o97 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 18), ElencoProdotti = new List<Prodotto> { p25, p30, p35, p40, p45, p50 }, Venditore = v22 };
            this.Ordini.Add(o97);
            Ordine o98 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 19), ElencoProdotti = new List<Prodotto> { p1, p2, p3, p4, p5, p6, p7 }, Venditore = v23 };
            this.Ordini.Add(o98);
            Ordine o99 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 20), ElencoProdotti = new List<Prodotto> { p8, p9, p10, p11, p12, p13, p14 }, Venditore = v24 };
            this.Ordini.Add(o99);
            Ordine o100 = new Ordine { Codice = Ordine.GeneraCodiceOrdine(), Data = new DateTime(2026, 6, 21), ElencoProdotti = new List<Prodotto> { p1, p11, p21, p31, p41, p50 }, Venditore = v25 };
            this.Ordini.Add(o100);

            //============================================================//
            //  CAPO OFFICINA                                              //
            //============================================================//

            this.Capo = new CapoOfficina
            {
                Nome = "Roberto",
                Cognome = "Bruni",
                Stipendio = 4500,
                Tipologia = TipologiaMeccanico.Meccanica,
                Ordini = this.Ordini
            };
        }

        //metodi

        public void VisualizzaResponsabile()
        {
            Console.Clear();
            Console.WriteLine("--- RESPONSABILE VENDITORI ---");
            Console.WriteLine(this.Responsabile.Nome + " " + this.Responsabile.Cognome);
            Console.WriteLine("Stipendio: " + this.Responsabile.Stipendio.ToString("C"));
            Console.WriteLine("Tredicesima: " + this.Responsabile.Tredicesima().ToString("C"));
            Console.WriteLine("Settore: " + this.Responsabile.Settore);
            Console.WriteLine("Venditori seguiti: " + this.Responsabile.Venditori.Count);
            Console.WriteLine();

            foreach (Venditore v in this.Responsabile.Venditori)
            {
                Console.WriteLine("- " + v.Nome + " " + v.Cognome +
                    " | " + v.Settore +
                    " | Stipendio: " + v.Stipendio.ToString("C") +
                    " | Tredicesima: " + v.Tredicesima().ToString("C"));
            }

            Console.ReadKey();
        }

        public void VisualizzaCapoOfficina()
        {
            Console.Clear();
            Console.WriteLine("--- CAPO OFFICINA ---");
            Console.WriteLine(this.Capo.Nome + " " + this.Capo.Cognome);
            Console.WriteLine("Stipendio: " + this.Capo.Stipendio.ToString("C"));
            Console.WriteLine("Tredicesima: " + this.Capo.Tredicesima().ToString("C"));
            Console.WriteLine("Tipologia: " + this.Capo.Tipologia);
            Console.WriteLine("Ordini gestiti: " + this.Ordini.Count);
            Console.WriteLine();

            foreach (Ordine o in this.Ordini)
                Console.WriteLine("- " + o.Codice + " - " + o.Data.ToString("dd/MM/yyyy") + " - Pezzi: " + o.NumeroPezzi() + " - Totale: " + o.Totale().ToString("C"));

            Console.ReadKey();
        }

        public void StampaOrdine()
        {
            Console.Clear();
            Console.WriteLine("--- STAMPA ORDINE ---");

            foreach (Ordine o in this.Ordini)
                Console.WriteLine("- " + o.Codice + " (" + o.Data.ToString("dd/MM/yyyy") + ")");

            Console.Write("Codice ordine: ");
            string codice = Console.ReadLine();

            Ordine trovato = null;

            foreach (Ordine o in this.Ordini)
            {
                if (o.Codice == codice)
                {
                    trovato = o;
                    break;
                }
            }

            if (trovato != null)
            {
                trovato.Stampa();
                Console.WriteLine("Ordine " + codice + " stampato su file.");
            }
            else
                Console.WriteLine("Nessun ordine trovato.");

            Console.ReadKey();
        }
    }
}
