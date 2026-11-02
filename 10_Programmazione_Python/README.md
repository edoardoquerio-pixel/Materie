# 10 Programmazione Python

## Struttura
- 00_Note
- 01_Materiale
- 01_Esercizi
- 02_Progetti
- Final exams project *(submodule Git)*

## Final exams project (submodule)
Il progetto finale Python è stato separato in un repository dedicato e collegato qui come submodule:

- Percorso locale: `10_Programmazione_Python/Final exams project`
- Repository remoto: `https://github.com/edoardoquerio-pixel/Final-exams-project.git`

### Clone completo del repository Materie con submodule
```bash
git clone --recurse-submodules <URL_MATERIE>
```

### Se hai già clonato Materie
```bash
git submodule update --init --recursive
```

### Aggiornare il submodule all'ultima versione disponibile
```bash
git submodule update --remote --merge "10_Programmazione_Python/Final exams project"
```
