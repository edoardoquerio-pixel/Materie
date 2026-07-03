# [11] Programmazione DotNet C#

## 📋 Panoramica

Materia di programmazione C# su piattaforma .NET. Si parte dalla console application con esercizi progressivi su iterazione, selezione, array e strutture dati. Utilizza .NET 10 SDK con top-level statements e formato soluzione `.slnx`.

**Tecnologie**: C# (.NET 10), Visual Studio / VS Code, ADO.NET (database)

---

## 📚 Indice degli argomenti

### 1. Introduzione a C# e .NET

- **Framework**: .NET 10, runtime cross-platform
- **Struttura progetto**:
  ```xml
  <!-- .csproj -->
  <Project Sdk="Microsoft.NET.Sdk">
    <PropertyGroup>
      <OutputType>Exe</OutputType>
      <TargetFramework>net10.0</TargetFramework>
      <ImplicitUsings>enable</ImplicitUsings>
      <Nullable>enable</Nullable>
    </PropertyGroup>
  </Project>
  ```
- **Pattern entry point**: top-level statements
  ```csharp
  Console.Write("Inserisci nome: ");
  string nome = Console.ReadLine();
  Console.WriteLine($"Ciao, {nome}!");
  ```

### 2. Iterazione (Cicli)

- **for**: contatore definito
  ```csharp
  for (int i = 0; i < 10; i++) { ... }
  ```
- **while / do-while**: iterazione condizionata
- **foreach**: iterazione su collezioni
  ```csharp
  foreach (int n in numeri) { ... }
  ```
- **Esercizi**: stampa 100 interi positivi, stampa 100 pari positivi, frequenza lancio dado, numero primo, estrazione lotto, quadrato somma N numeri dispari

### 3. Selezione Multipla

- **if / else if / else**
- **switch** (con pattern matching C# 7+):
  ```csharp
  int giorno = 3;
  string nomeGiorno = giorno switch
  {
      1 => "Lunedì",
      2 => "Martedì",
      _ => "Altro giorno"
  };
  ```
- **Esercizi**: giorno della settimana, calcolo età, pari/dispari, positivo/negativo

### 4. OOP in C#

- **Classi e oggetti**:
  ```csharp
  public class Persona {
      public string Nome { get; set; }
      public int Eta { get; set; }
      public override string ToString() => $"{Nome}, {Eta} anni";
  }
  ```
- **Object initializer**: `new Persona { Nome = "Mario", Eta = 25 };`
- **Enum**: `enum GiornoSettimana { Lun, Mar, Mer, Gio, Ven, Sab, Dom }`
- **String interpolation**: `$"Valore: {x}"`

### 5. ADO.NET e Database

- Connessione a SQL Server / SQLite
- `SqlConnection`, `SqlCommand`, `SqlDataReader`
- Esecuzione query parametrizzate (protezione SQL injection)

---

## ⚡ Punti Chiave

1. **`ImplicitUsings` abilita**: System, System.Collections.Generic, System.Linq, System.Threading.Tasks ecc.
2. **Nullable enable**: il compilatore avverte su possibili null reference
3. **Console.ReadLine()** restituisce `string?` — gestire il null
4. **`$""` per string interpolation** — più leggibile di concatenazione
5. **Top-level statements**: C# 10+ permette codice senza classe Program

---

## 📎 Risorse Collegate

- **02_Esercizi/** — 10+ esercizi su iterazione, selezione, array
- **03_Progetti/** — Progetti completi WinForms e console
- **04_Visual C#/** — Materiale Visual C# aggiuntivo
