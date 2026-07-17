# Programmazione Python — Note Complete

## 1. Type Hints (Tipizzazione)

```python
from typing import List, Dict, Optional, Tuple, Union, Callable, TypeVar

def somma(a: int, b: int) -> int:
    return a + b

# Tipo generico
T = TypeVar('T')
def primo(lista: List[T]) -> Optional[T]:
    return lista[0] if lista else None

# NamedTuple
from typing import NamedTuple
class Coordinate(NamedTuple):
    lat: float; lon: float; città: str

# Protocol (structural typing)
from typing import Protocol
class Leggibile(Protocol):
    def read(self) -> str: ...
```

## 2. OOP

```python
from abc import ABC, abstractmethod

class Persona:
    count = 0
    def __init__(self, nome: str):
        self._nome = nome  # protected
        self.__id = Persona.count  # private (name mangling)
        Persona.count += 1

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if not value.strip(): raise ValueError
        self._nome = value

    def __str__(self): return self._nome

class Studente(Persona):
    def __init__(self, nome: str, mat: int):
        super().__init__(nome)
        self._matricola = mat
```

**Principi:**
- Ereditarietà: `class B(A):`
- Polimorfismo: metodi con stessa firma, comportamento diverso
- Incapsulamento: `_` protected, `__` private
- Composizione: has-a vs is-a
- ABC: classi astratte con `@abstractmethod`

## 3. Decorators

```python
import functools, time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter()-start:.4f}s")
        return result
    return wrapper

@timer
def lento(): time.sleep(0.1)

# Con parametri
def repeat(n=3):
    def deco(f):
        @functools.wraps(f)
        def wrapper(*a, **kw):
            return [f(*a, **kw) for _ in range(n)]
        return wrapper
    return deco
```

## 4. Context Manager

```python
# Classe
class FileGestito:
    def __init__(self, name, mode='r'):
        self.file = open(name, mode)
    def __enter__(self): return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Con contextlib
from contextlib import contextmanager
@contextmanager
def aperto(name, mode='r'):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()
```

## 5. Generators

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Pipeline di generatori
def numeri_pari(seq):
    for n in seq:
        if n % 2 == 0: yield n

# Generator expression: (x**2 for x in range(10))

# yield from
def appiattisci(liste):
    for l in liste:
        yield from l
```

## 6. pathlib

```python
from pathlib import Path

p = Path("/home/user/doc.txt")
p.name      # doc.txt
p.stem      # doc
p.suffix    # .txt
p.parent    # /home/user
p.exists()  # bool
p.is_file() # bool
p.is_dir()  # bool
p.read_text()
p.write_text("contenuto")
p.iterdir()  # contenuti dir
p.glob("*.py")
p.rglob("**/*.py")
Path.cwd(), Path.home()
```

## 7. CLI Building

```python
# argparse (stdlib)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="File input")
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

# Typer (terze parti)
import typer
app = typer.Typer()
@app.command()
def hello(nome: str):
    typer.echo(f"Ciao {nome}")
app()
```

## 8. Librerie Standard Essenziali

| Modulo | Uso |
|--------|-----|
| `os` | Interazione SO (env, processi, path) |
| `sys` | Argomenti CLI, exit code, path Python |
| `json` | JSON parsing/serialization |
| `csv` | Lettura/scrittura CSV |
| `re` | Regex |
| `datetime` | Date, time, timedelta |
| `collections` | defaultdict, Counter, deque, namedtuple |
| `itertools` | chain, cycle, groupby, permutations, product |
| `functools` | lru_cache, reduce, partial, wraps |
| `asyncio` | Programmazione asincrona |
| `sqlite3` | Database SQLite |
| `unittest` / `pytest` | Testing |

## 9. Error Handling

```python
try:
    risultato = 10 / 0
except ZeroDivisionError:
    print("Divisione per zero")
except (ValueError, TypeError) as e:
    print(f"Errore: {e}")
else:
    print("Nessun errore")
finally:
    print("Sempre eseguito")

# Custom exception
class MioErrore(Exception):
    pass
```

## 10. Virtual Environments

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
pip freeze > requirements.txt
```
