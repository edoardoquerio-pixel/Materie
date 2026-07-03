# Lezione 4

## Panoramica
Binario e Rappresentazione Caratteri

## Argomenti trattati
API REST, Inglese, Programmazione, Git

---
## Appunti

LEZIONE 4 - Numeri Decimali in
Binario e Rappresentazione Caratteri
Durata: 4 ore | Teoria: 2h | Esercizi: 2h
PARTE TEORICA (2 ore)
4.1 Rappresentazione dei Numeri con Virgola (30 min)
Finora abbiamo visto solo numeri interi. Ma come rappresentare numeri con la virgola
(es. 3.14, -0.5, 123.456)?
Virgola Fissa vs Virgola Mobile
Due approcci principali:
Fixed Point (Virgola Fissa): la posizione della virgola è predefinita
Floating Point (Virgola Mobile): la virgola può “galleggiare” - maggiore flessibilità
4.2 Virgola Fissa (Fixed Point) (25 min)
Nella virgola fissa, si decide a priori quanti bit dedicare alla parte intera e quanti alla
parte decimale.
Esempio: Formato 8.8 (8 bit per parte intera, 8 bit per parte decimale)
┌─────────────┬─────────────┐
│ Parte │ Parte │
│ Intera │ Decimale │
│ 8 bit │ 8 bit │
└─────────────┴─────────────┘
Posizioni Decimali in Binario
Come nel sistema decimale, le posizioni dopo la virgola hanno pesi negativi:
Sistema Decimale:
123.45 = 1×10² + 2×10¹ + 3×10⁰ + 4×10⁻¹ + 5×10⁻²
= 100 + 20 + 3 + 0.4 + 0.05
Sistema Binario:
Posizioni: 2² 2¹ 2⁰ . 2⁻¹ 2⁻² 2⁻³ 2⁻⁴
Pesi: 4 2 1 . 0.5 0.25 0.125 0.0625
Tabella Potenze Negative di 2
Valore Decimale
Conversione Decimale → Binario (Parte Frazionaria)
Metodo delle Moltiplicazioni Successive:
Moltiplica la parte decimale per 2
Prendi la parte intera del risultato (0 o 1)
Usa solo la parte decimale per la moltiplicazione successiva
Ripeti finché la parte decimale diventa 0 o raggiungi il numero di bit desiderato
Leggi i bit dall’alto verso il basso (ordine di generazione)
Esempio 1: Convertire 0.75₁₀ in binario
0.75 × 2 = 1.50 → bit 1, continua con 0.50
0.50 × 2 = 1.00 → bit 1, continua con 0.00
Risultato: 0.75₁₀ = 0.11₂
Verifica: 0.11₂ = 1×2⁻¹ + 1×2⁻² = 0.5 + 0.25 = 0.75 ✓
Esempio 2: Convertire 0.625₁₀ in binario
0.625 × 2 = 1.25 → bit 1, continua con 0.25
0.25 × 2 = 0.50 → bit 0, continua con 0.50
0.50 × 2 = 1.00 → bit 1, continua con 0.00
Risultato: 0.625₁₀ = 0.101₂
Verifica: 0.101₂ = 1×0.5 + 0×0.25 + 1×0.125 = 0.5 + 0.125 = 0.625 ✓
Esempio 3: Convertire 0.1₁₀ in binario (PROBLEMA!)
0.1 × 2 = 0.2 → bit 0, continua con 0.2
0.2 × 2 = 0.4 → bit 0, continua con 0.4
0.4 × 2 = 0.8 → bit 0, continua con 0.8
0.8 × 2 = 1.6 → bit 1, continua con 0.6
0.6 × 2 = 1.2 → bit 1, continua con 0.2
0.2 × 2 = 0.4 → bit 0, continua con 0.4 (CICLO!)
Risultato: 0.1₁₀ = 0.0001100110011... (periodico!)
IMPORTANTE: Non tutti i numeri decimali hanno una rappresentazione binaria finita!
0.5, 0.25, 0.125, 0.75, 0.625 → rappresentazione finita
0.1, 0.2, 0.3, 0.6, 0.7 → rappresentazione periodica infinita
Questo causa errori di arrotondamento nei calcoli con virgola mobile!
Conversione Binario → Decimale (Numeri con Virgola)
Metodo: Somma dei bit moltiplicati per i loro pesi (potenze negative di 2)
Esempio 1: Convertire 101.011₂ in decimale
4 2 1 0.5 0.25 0.125
= 1×4 + 0×2 + 1×1 + 0×0.5 + 1×0.25 + 1×0.125
= 4 + 0 + 1 + 0 + 0.25 + 0.125
Esempio 2: Convertire 11.11₂ in decimale
= 1×2 + 1×1 + 1×0.5 + 1×0.25
= 2 + 1 + 0.5 + 0.25
Conversione Numero Completo (Parte Intera + Decimale)
Esempio: Convertire 13.625₁₀ in binario
Passo 1 - Parte intera (13):
13 ÷ 2 = 6 resto 1 ←┐
6 ÷ 2 = 3 resto 0 │
3 ÷ 2 = 1 resto 1 │
1 ÷ 2 = 0 resto 1 ←┘
Parte intera: 1101₂
Passo 2 - Parte decimale (0.625):
0.625 × 2 = 1.25 → bit 1
0.25 × 2 = 0.50 → bit 0

*[Contenuto troncato — vedi file originale per dettagli completi]*

---
*Fonte: 004_lezione4_decimali_char.md*
