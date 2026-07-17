# Programmazione .NET C# — Note Complete

## 1. Fondamenti del Linguaggio

- **Tipi**: `int`, `long`, `float`, `double`, `decimal`, `bool`, `char`, `string`
- **Value types vs Reference types**: struct (stack) vs class (heap)
- **Nullable**: `int?`, `string?` (C# 8+)
- **Operatori**: `??` (null-coalescing), `?.` (null-conditional), `=>` (lambda/expression body)
- **Control flow**: `if/else`, `switch` (pattern matching), `for`, `foreach`, `while`, `do`

## 2. Programmazione OOP

```csharp
public class Studente
{
    public int Id { get; set; }                     // Auto-property
    public string Nome { get; private set; }        // Read-only esterno
    public string Cognome { get; init; }             // Init-only (C# 9+)
    
    public Studente(string nome, string cognome)     // Costruttore
    {
        Nome = nome;
        Cognome = cognome;
    }
    
    public override string ToString() => $"{Nome} {Cognome}";
}

public enum StatoStudente { Attivo, Sospeso, Ritirato }
```

## 3. .NET 10

- **Target Framework**: `net10.0`
- **`.csproj` SDK-style**: `<ImplicitUsings>enable</ImplicitUsings>`, `<Nullable>enable</Nullable>`
- **Top-level statements**: entry point senza `class Program` / `Main`
- **`.slnx`**: nuovo formato XML soluzione (non più `.sln`)
- **Minimal APIs**: per servizi HTTP leggeri

```xml
<!-- .csproj template -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
```

## 4. LINQ

```csharp
var studentiAttivi = db.Studenti
    .Where(s => s.Stato == StatoStudente.Attivo)
    .OrderBy(s => s.Cognome)
    .ThenBy(s => s.Nome)
    .Select(s => new { s.Nome, s.Cognome })
    .ToList();
```

## 5. ADO.NET

```csharp
string connString = "Server=.;Database=Scuola;Integrated Security=true;";
using var conn = new SqlConnection(connString);
conn.Open();

string sql = "SELECT Id, Nome FROM Studenti WHERE CorsoId = @CorsoId";
using var cmd = new SqlCommand(sql, conn);
cmd.Parameters.AddWithValue("@CorsoId", corsoId);

using var reader = cmd.ExecuteReader();
while(reader.Read())
    Console.WriteLine($"{reader["Id"]}: {reader["Nome"]}");
```

## 6. Windows Forms

- **Control**: Button, TextBox, Label, DataGridView, ListBox, ComboBox
- **Eventi**: Click, TextChanged, Load, SelectedIndexChanged
- **BindingSource**: connessione DataSet → controlli
- **DataGridView**: visualizzazione/modifica dati tabellari

## 7. Console App Patterns

- Menu-driven con `switch` / `do-while`
- Separazione: entità (classi), servizi (logica), UI (console)
- File I/O: `StreamReader`/`StreamWriter`, `JSON` serialization
- Error handling: `try/catch/finally`, eccezioni specifiche

## 8. Progetti Tipici (ITS)

| Progetto | Concetti | 
|----------|----------|
| Calcolatrice | Tipi, operatori, controllo |
| Rubrica Contatti | OOP, liste, file I/O |
| Gestione Studenti | ADO.NET, DataGridView, CRUD |
| Biblioteca | Classi, LINQ, ricerca |
| Login System | Validazione, regex, sicurezza base |
