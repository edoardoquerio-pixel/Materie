# Esercitazione 1 - Programmazione .NET C#

---

**Studente:** Edoardo Querio  
**Corso:** ITS ICT  
**Modulo:** Programmazione DotNet CSharp  
**Data:** 15/06/2026

---

## 1. Persona (classe astratta)

**File:** `Dominio/Persona.cs`

```csharp
namespace Querio_Esercitazione1
{
    public abstract class Persona
    {
        //propietà

        public string Nome { get; set; } = "";
        public string Cognome { get; set; } = "";
        public double Stipendio { get; set; }

        //metodi

        public abstract double Tredicesima();

        public override string ToString()
        {
            return $"{nameof(Nome)}={Nome}" +
                $", {nameof(Cognome)}={Cognome}" +
                $", {nameof(Stipendio)}={Stipendio}"
                ;
        }
    }
}
```

---

## 2. Venditore

**File:** `Dominio/Venditore.cs`

```csharp
namespace Querio_Esercitazione1
{
    public enum SettoreVendite
    {
        Auto,
        Moto
    }

    public class Venditore : Persona, ICloneable
    {
        //propietà

        public SettoreVendite Settore { get; set; }

        //metodi

        public override double Tredicesima()
        {
            return this.Stipendio * 1.91;
        }

        public object Clone()
        {
            return this.MemberwiseClone();
        }
    }
}
```

---

## 3. Meccanico

**File:** `Dominio/Meccanico.cs`

```csharp
namespace Querio_Esercitazione1
{
    public enum TipologiaMeccanico
    {
        Carrozzeria,
        Meccanica
    }

    public class Meccanico : Persona
    {
        //propietà

        public TipologiaMeccanico Tipologia { get; set; }

        //metodi

        public override double Tredicesima()
        {
            return this.Stipendio * 1.93;
        }

        public override bool Equals(object obj)
        {
            if (obj == null || this.GetType() != obj.GetType())
                return false;

            Meccanico other = (Meccanico)obj;

            return this.Nome == other.Nome &&
                   this.Cognome == other.Cognome &&
                   this.Stipendio == other.Stipendio &&
                   this.Tipologia == other.Tipologia;
        }

        public override int GetHashCode()
        {
            return this.Nome.GetHashCode() +
                   this.Cognome.GetHashCode() +
                   this.Stipendio.GetHashCode() +
                   this.Tipologia.GetHashCode();
        }
    }
}
```

---

## 4. ResponsabileVenditori

**File:** `Dominio/ResponsabileVenditori.cs`

```csharp
namespace Querio_Esercitazione1
{
    public class ResponsabileVenditori : Venditore
    {
        //propietà

        public List<Venditore> Venditori { get; set; }

        //metodi

        public override double Tredicesima()
        {
            double bonus = 0;

            foreach (Venditore v in this.Venditori)
            {
                double tariffaGiornaliera = v.Stipendio / 30.0;
                bonus += tariffaGiornaliera * 0.15;
            }

            return this.Stipendio * 2 + bonus;
        }
    }
}
```

---

## 5. CapoOfficina

**File:** `Dominio/CapoOfficina.cs`

```csharp
namespace Querio_Esercitazione1
{
    public class CapoOfficina : Meccanico
    {
        //propietà

        public List<Ordine> Ordini { get; set; }

        //metodi

        public override double Tredicesima()
        {
            double importoOrdini = 0;

            foreach (Ordine o in this.Ordini)
            {
                importoOrdini += o.Totale();
            }

            return this.Stipendio * 2 + importoOrdini * 0.05;
        }
    }
}
```

---

## 6. Prodotto

**File:** `Dominio/Prodotto.cs`

```csharp
namespace Querio_Esercitazione1
{
    public class Prodotto
    {
        //propietà

        public string Codice { get; set; } = "";
        public string Denominazione { get; set; } = "";
        public string Descrizione { get; set; } = "";
        public double Prezzo { get; set; }
        public int Giacenza { get; set; }
    }
}
```

---

## 7. Ordine (classe sealed)

**File:** `Dominio/Ordine.cs`

```csharp
namespace Querio_Esercitazione1
{
    public sealed class Ordine
    {
        //propietà

        public string Codice { get; set; } = "";
        public DateTime Data { get; set; }
        public List<Prodotto> ElencoProdotti { get; set; }
        public Venditore Venditore { get; set; }

        //metodi pubblici

        public int NumeroPezzi()
        {
            return this.ElencoProdotti.Count;
        }

        public double Totale()
        {
            double totale = 0;

            foreach (Prodotto p in this.ElencoProdotti)
                totale += p.Prezzo;

            return totale;
        }

        public void Stampa()
        {
            string path = @"..\..\..\file\" + this.Codice + ".txt";

            using (StreamWriter sw = new StreamWriter(path))
            {
                sw.WriteLine("ORDINE: " + this.Codice);
                sw.WriteLine("Data: " + this.Data.ToString("dd/MM/yyyy"));
                sw.WriteLine("Venditore: " + this.Venditore.Nome + " " + this.Venditore.Cognome);
                sw.WriteLine("----------------------------------------");

                //raggruppo i prodotti per calcolare le quantita'
                List<string> codiciStampati = new List<string>();

                foreach (Prodotto p in this.ElencoProdotti)
                {
                    bool giaStampato = false;

                    foreach (string c in codiciStampati)
                    {
                        if (c == p.Codice)
                        {
                            giaStampato = true;
                            break;
                        }
                    }

                    if (!giaStampato)
                    {
                        codiciStampati.Add(p.Codice);

                        int qta = 0;

                        foreach (Prodotto inner in this.ElencoProdotti)
                        {
                            if (inner.Codice == p.Codice)
                                qta++;
                        }

                        double subtotale = p.Prezzo * qta;

                        sw.WriteLine(p.Codice + " | " +
                                     p.Denominazione + " | " +
                                     "Qta: " + qta + " | " +
                                     "Prezzo: " + p.Prezzo.ToString("C") + " | " +
                                     "Subtotale: " + subtotale.ToString("C"));
                    }
                }

                sw.WriteLine("----------------------------------------");
                sw.WriteLine("TOTALE ORDINE: " + this.Totale().ToString("C"));
            }
        }

        public static string GeneraCodiceOrdine()
        {
            string caratteri = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            char[] chars = new char[8];
            Random random = new Random();

            chars[0] = caratteri[random.Next(26)];

            for (int i = 1; i < 8; i++)
                chars[i] = caratteri[random.Next(36)];

            return new string(chars);
        }
    }
}
```

---

## 8. QuerioEsercitazione1Biz

**File:** `Dominio/QuerioEsercitazione1Biz.cs`

```csharp
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
            //creazione dati test

            Venditore v1 = new Venditore
            {
                Nome = "Mario",
                Cognome = "Rossi",
                Stipendio = 2500.00,
                Settore = SettoreVendite.Auto
            };

            Venditore v2 = new Venditore
            {
                Nome = "Luca",
                Cognome = "Bianchi",
                Stipendio = 2700.00,
                Settore = SettoreVendite.Auto
            };

            Venditore v3 = new Venditore
            {
                Nome = "Giulia",
                Cognome = "Verdi",
                Stipendio = 2400.00,
                Settore = SettoreVendite.Moto
            };

            Venditore v4 = new Venditore
            {
                Nome = "Marco",
                Cognome = "Neri",
                Stipendio = 2600.00,
                Settore = SettoreVendite.Moto
            };

            this.Venditori = new List<Venditore> { v1, v2, v3, v4 };

            this.Responsabile = new ResponsabileVenditori
            {
                Nome = "Paolo",
                Cognome = "Gialli",
                Stipendio = 3200.00,
                Settore = SettoreVendite.Auto,
                Venditori = this.Venditori
            };

            Prodotto p1 = new Prodotto
            {
                Codice = "P001",
                Denominazione = "Pastiglie freno",
                Descrizione = "Set pastiglie freno anteriori",
                Prezzo = 45.50,
                Giacenza = 30
            };

            Prodotto p2 = new Prodotto
            {
                Codice = "P002",
                Denominazione = "Olio motore 5W40",
                Descrizione = "Lattina olio motore 5W40 4L",
                Prezzo = 38.90,
                Giacenza = 50
            };

            Prodotto p3 = new Prodotto
            {
                Codice = "P003",
                Denominazione = "Filtro aria",
                Descrizione = "Filtro aria abitacolo",
                Prezzo = 22.30,
                Giacenza = 40
            };

            Prodotto p4 = new Prodotto
            {
                Codice = "P004",
                Denominazione = "Ammortizzatore",
                Descrizione = "Ammortizzatore posteriore",
                Prezzo = 120.00,
                Giacenza = 15
            };

            Prodotto p5 = new Prodotto
            {
                Codice = "P005",
                Denominazione = "Batteria auto",
                Descrizione = "Batteria 12V 60Ah",
                Prezzo = 95.00,
                Giacenza = 20
            };

            Prodotto p6 = new Prodotto
            {
                Codice = "P006",
                Denominazione = "Candela accensione",
                Descrizione = "Candela accensione iridio",
                Prezzo = 12.50,
                Giacenza = 100
            };

            Prodotto p7 = new Prodotto
            {
                Codice = "P007",
                Denominazione = "Parabrezza",
                Descrizione = "Parabrezza anteriore",
                Prezzo = 250.00,
                Giacenza = 8
            };

            Prodotto p8 = new Prodotto
            {
                Codice = "P008",
                Denominazione = "Catenone moto",
                Descrizione = "Catenone trasmissione moto",
                Prezzo = 85.00,
                Giacenza = 12
            };

            List<Prodotto> prodottiOrd1 = new List<Prodotto> { p1, p1, p2, p3, p5 };
            List<Prodotto> prodottiOrd2 = new List<Prodotto> { p4, p6, p6, p6, p8 };
            List<Prodotto> prodottiOrd3 = new List<Prodotto> { p2, p3, p5, p7, p7, p8 };

            Ordine ord1 = new Ordine
            {
                Codice = Ordine.GeneraCodiceOrdine(),
                Data = new DateTime(2026, 6, 10),
                ElencoProdotti = prodottiOrd1,
                Venditore = v1
            };

            Ordine ord2 = new Ordine
            {
                Codice = Ordine.GeneraCodiceOrdine(),
                Data = new DateTime(2026, 6, 12),
                ElencoProdotti = prodottiOrd2,
                Venditore = v3
            };

            Ordine ord3 = new Ordine
            {
                Codice = Ordine.GeneraCodiceOrdine(),
                Data = new DateTime(2026, 6, 14),
                ElencoProdotti = prodottiOrd3,
                Venditore = v2
            };

            this.Ordini = new List<Ordine> { ord1, ord2, ord3 };

            this.Capo = new CapoOfficina
            {
                Nome = "Roberto",
                Cognome = "Bruni",
                Stipendio = 3000.00,
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
            Console.WriteLine("Venditori seguiti:");

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
```

---

## 9. Program (Presentation Layer)

**File:** `Program.cs`

```csharp
namespace Querio_Esercitazione1
{
    public class Program
    {
        static void Main(string[] args)
        {
            QuerioEsercitazione1Biz biz = new QuerioEsercitazione1Biz();

            while (true)
            {
                Console.Clear();
                Console.WriteLine("--- GESTIONALE OFFICINA ---");
                Console.WriteLine("1) Visualizza dati responsabile venditori");
                Console.WriteLine("2) Visualizza dati capo officina");
                Console.WriteLine("3) Stampa ordine tramite codice");
                Console.WriteLine("4) Termina programma");
                Console.Write("Scegli: ");

                string scelta = Console.ReadLine();

                switch (scelta)
                {
                    case "1":
                        biz.VisualizzaResponsabile();
                        break;

                    case "2":
                        biz.VisualizzaCapoOfficina();
                        break;

                    case "3":
                        biz.StampaOrdine();
                        break;

                    case "4":
                        return;

                    default:
                        Console.WriteLine("Opzione non valida.");
                        Console.ReadKey();
                        break;
                }
            }
        }
    }
}
```

---

## Gerarchia delle classi

```
Persona (abstract)
├── Venditore : Persona, ICloneable
│   └── ResponsabileVenditori : Venditore
└── Meccanico : Persona
    └── CapoOfficina : Meccanico

Prodotto (classe semplice)
Ordine (sealed - non ereditabile)
QuerioEsercitazione1Biz (business layer)
Program (presentation layer / menu)
```

---

## Struttura del progetto

```
Querio_Esercitazione1/
├── Querio_Esercitazione1.slnx
└── Querio_Esercitazione1/
    ├── Querio_Esercitazione1.csproj
    ├── Program.cs
    ├── file/                          (cartella output ordini .txt)
    └── Dominio/
        ├── Persona.cs                 (classe astratta)
        ├── Venditore.cs               (enum SettoreVendite + classe)
        ├── Meccanico.cs               (enum TipologiaMeccanico + classe)
        ├── ResponsabileVenditori.cs
        ├── CapoOfficina.cs
        ├── Prodotto.cs
        ├── Ordine.cs                  (sealed)
        └── QuerioEsercitazione1Biz.cs (business layer)
```
