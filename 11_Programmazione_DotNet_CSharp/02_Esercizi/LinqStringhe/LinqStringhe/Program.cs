
//Utilizzando la sintassi LINQ, dato il seguente array di nomi:
//  - Stampare l'elenco completo
//  - Stampare i nomi che iniziano con A
//  - Stampare i nomi in ordine alfabetico crescente
//  - Stampare i nomi con lunghezza 7 in ordine decrescente
//  - Stampare i nomi tutti in maiuscolo

string[] nomi = {
    "Pietro", "Mario", "Giulia", "Francesca", "Laura", "Piero",
    "antonio", "Vito", "Antonella", "Giada", "Rossella", "Simone",
    "Saverio", "Rosa", "Michela", "Andrea", "Mattia", "Ilaria",
    "Alex", "Vanessa", "Ciro", "Elia", "Giuditta", "Stefano",
    "Alessandro", "Carlo", "Drusilla", "Dorothea", "Lucilla",
    "Marialuisa", "Marcolino", "Pietrangelo", "Ermenegildo"
};

// 1. Stampa elenco completo
Console.WriteLine("=== 1. ELENCO COMPLETO ===");
var completo = from n in nomi select n;
foreach (var n in completo)
    Console.WriteLine(n);

// 2. Stampa elenco nomi che iniziano con A (case-insensitive)
Console.WriteLine("\n=== 2. NOMI CHE INIZIANO CON A ===");
var conA = from n in nomi
           where n.StartsWith("A", StringComparison.OrdinalIgnoreCase)
           select n;
foreach (var n in conA)
    Console.WriteLine(n);

// 3. Stampa elenco nomi in ordine alfabetico crescente
Console.WriteLine("\n=== 3. ORDINE ALFABETICO CRESCENTE ===");
var ordineCrescente = from n in nomi
                      orderby n
                      select n;
foreach (var n in ordineCrescente)
    Console.WriteLine(n);

// 4. Stampa elenco nomi con lunghezza pari a 7 in ordine decrescente
Console.WriteLine("\n=== 4. LUNGHEZZA 7, ORDINE DECRESCENTE ===");
var lunghi7 = from n in nomi
              where n.Length == 7
              orderby n descending
              select n;
foreach (var n in lunghi7)
    Console.WriteLine(n);

// 5. Stampa elenco nomi tutti in maiuscolo
Console.WriteLine("\n=== 5. TUTTI IN MAIUSCOLO ===");
var maiuscoli = from n in nomi
                select n.ToUpper();
foreach (var n in maiuscoli)
    Console.WriteLine(n);
