# Lezione 3

## Panoramica
Rappresentazione Binaria degli Interi

## Argomenti trattati
Git, API REST, Data Analytics, Programmazione

---
## Appunti

LEZIONE 3 - Sistemi Numerici e
Rappresentazione Binaria degli Interi
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
3.1 Sistemi di Numerazione Posizionali (25 min)
Cosa Significa “Posizionale”?
Un sistema di numerazione è posizionale quando il valore di una cifra dipende sia dal
suo valore intrinseco che dalla sua posizione.
Esempio in base 10:
Il numero 352 significa:
3 centinaia (3 × 100)
5 decine (5 × 10)
2 unità (2 × 1)
Formula generale:
352₁₀ = 3×10² + 5×10¹ + 2×10⁰
= 3×100 + 5×10 + 2×1
Componenti di un Sistema Posizionale
1. Base (o radice):
Determina quante cifre diverse si possono usare
Base 10: cifre da 0 a 9
Base 2: cifre 0 e 1
Base 8: cifre da 0 a 7
Base 16: cifre da 0 a 9 e A a F
Simboli usati per rappresentare valori
Il valore massimo di una cifra è (base - 1)
3. Peso Posizionale:
Ogni posizione ha un peso che è una potenza della base
Le posizioni si numerano da destra verso sinistra partendo da 0
Rappresentazione generale:
N = dₙ×baseⁿ + dₙ₋₁×baseⁿ⁻¹ + ... + d₁×base¹ + d₀×base⁰
3.2 Il Sistema Decimale (Base 10) (10 min)
Il sistema decimale è quello che usiamo quotidianamente.
Caratteristiche:
Cifre: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
Pesi posizionali: …10³, 10², 10¹, 10⁰ = …1000, 100, 10, 1
Esempio Dettagliato: 2547₁₀
Posizione: 3 2 1 0
Peso: 10³ 10² 10¹ 10⁰
Valore: 2×1000 + 5×100 + 4×10 + 7×1
= 2000 + 500 + 40 + 7
Numeri con Virgola:
Numero: 123.45₁₀
Posizione: 2 1 0 -1 -2
Cifra: 1 2 3 4 5
Peso: 10² 10¹ 10⁰ 10⁻¹ 10⁻²
100 10 1 0.1 0.01
Valore: 1×100 + 2×10 + 3×1 + 4×0.1 + 5×0.01
= 100 + 20 + 3 + 0.4 + 0.05
3.3 Il Sistema Binario (Base 2) (30 min)
Il sistema binario è fondamentale per i computer, che lavorano solo con due stati:
acceso/spento, vero/falso, 1/0.
Caratteristiche:
Cifre: 0, 1 (chiamate bit = binary digit)
Pesi posizionali: …2³, 2², 2¹, 2⁰ = …8, 4, 2, 1
Tabella delle Potenze di 2 (da memorizzare!)
Valore Decimale
Valore Decimale
Esempio: Convertire 1011₂ in Decimale
Posizione: 3 2 1 0
Peso: 2³ 2² 2¹ 2⁰
Valore: 1×8 + 0×4 + 1×2 + 1×1
= 8 + 0 + 2 + 1
Conversione Binario → Decimale (Metodo Generale)
Somma di (cifra × 2^posizione) per ogni bit
10101₂ in decimale:
= 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
= 1×16 + 0×8 + 1×4 + 0×2 + 1×1
= 16 + 0 + 4 + 0 + 1
11111111₂ in decimale:
= 1×128 + 1×64 + 1×32 + 1×16 + 1×8 + 1×4 + 1×2 + 1×1
= 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1
10000000₂ in decimale:
= 1×128 = 128₁₀
Conversione Decimale → Binario
Metodo delle Divisioni Successive:
Dividi il numero decimale per 2
Annota il resto (0 o 1)
Usa il quoziente per la divisione successiva
Ripeti fino a quando il quoziente diventa 0
Il numero binario si legge dai resti dal basso verso l’alto

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 003_lezione3_binario.md*
