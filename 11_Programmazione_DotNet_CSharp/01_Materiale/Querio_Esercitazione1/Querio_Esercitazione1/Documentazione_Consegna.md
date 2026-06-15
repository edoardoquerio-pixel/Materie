# Esercitazione 1 - Programmazione .NET C#

---

**Studente:** Edoardo Querio Gianetto
**Corso:** Cloud Specialist  
**Modulo:** Programmazione .Net C#  
**Data:** 15/06/2026

---

## 1. Persona (classe astratta)

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

## 2. SettoreVendite

```csharp
namespace Querio_Esercitazione1
{
    public enum SettoreVendite
    {
        Auto,
        Moto
    }
}
```

---

## 3. Venditore

```csharp
namespace Querio_Esercitazione1
{
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

## 4. TipologiaMeccanico

```csharp
namespace Querio_Esercitazione1
{
    public enum TipologiaMeccanico
    {
        Carrozzeria,
        Meccanica
    }
}
```

---

## 5. Meccanico

```csharp
namespace Querio_Esercitazione1
{
    public class Meccanico : Persona
    {
        //propietà

        public TipologiaMeccanico Tipologia { get; set; }

        //metodi

        public override double Tredicesima()
        {
            return this.Stipendio * 1.93;
        }

        public bool Equals(Meccanico altro)
        {
            return this.Nome == altro.Nome &&
                   this.Cognome == altro.Cognome &&
                   this.Stipendio == altro.Stipendio &&
                   this.Tipologia == altro.Tipologia;
        }
    }
}
```

---

## 6. ResponsabileVenditori

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

## 7. CapoOfficina

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

## 8. Prodotto

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

## 9. Ordine (sealed)

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

## 10. QuerioEsercitazione1Biz

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
            //25 venditori, 50 prodotti, 25 meccanici, 100 ordini

            Venditore v1 = new Venditore { Nome = "Mario", Cognome = "Rossi", Stipendio = 2500, Settore = SettoreVendite.Auto };
            //... altri 24 venditori ...

            this.Venditori = new List<Venditore> { v1, /*...*/ };

            this.Responsabile = new ResponsabileVenditori
            {
                Nome = "Alessio", Cognome = "Rizzi",
                Stipendio = 4000, Settore = SettoreVendite.Auto,
                Venditori = this.Venditori
            };

            Prodotto p1 = new Prodotto { Codice = "P001", Denominazione = "Pastiglie freno", Prezzo = 45.50, Giacenza = 30 };
            //... altri 49 prodotti ...

            Meccanico m1 = new Meccanico { Nome = "Antonio", Cognome = "Rinaldi", Stipendio = 2300, Tipologia = TipologiaMeccanico.Meccanica };
            //... altri 24 meccanici ...

            //100 ordini con prodotti e venditori
            this.Ordini = new List<Ordine>();
            //... 100 ordini creati e aggiunti ...

            this.Capo = new CapoOfficina
            {
                Nome = "Roberto", Cognome = "Bruni",
                Stipendio = 4500, Tipologia = TipologiaMeccanico.Meccanica,
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
```

---

## 11. Program

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
