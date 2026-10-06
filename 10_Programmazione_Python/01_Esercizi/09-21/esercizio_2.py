"""Mostra la somma dei pari e il prodotto dei dispari in una sequenza di esempio."""

# =============================================================================
# ANALISI DEL PROBLEMA
# =============================================================================
# 1. Quali sono gli input del problema?
#    Un numero arbitrario di valori numerici passati come argomenti alla funzione.
# 2. Quali sono gli output?
#    La somma dei soli numeri pari e il prodotto dei soli numeri dispari.
# 3. Suddivisione in problemi semplici:
#    - Definire una funzione che accetti un numero variabile di argomenti (*args).
#    - Scorrere i valori ricevuti per distinguere tra pari e dispari.
#    - Accumulare la somma per i pari e il prodotto per i dispari.
#    - Gestire il caso in cui non vengano passati numeri dispari (evitando che il prodotto resti 1 di default).
#    - Restituire i risultati al programma principale.
# 4. Rappresentazione come funzione:
#    - Nome: elabora_numeri
#    - Restituisce: due valori interi (somma_pari, prodotto_dispari).
#    - Parametri: *args (arbitrari).
# =============================================================================

# =============================================================================
# DEFINIZIONE DELLE FUNZIONI
# =============================================================================

def elabora_numeri(*numeri):
    """
    Descrizione: Riceve un numero arbitrario di valori numerici, calcola la somma 
                 dei pari e il prodotto dei dispari.
    Parametri formali:
        - *numeri (int): sequenza variabile di numeri interi.
    Restituisce:
        - tuple: (somma_pari, prodotto_dispari) contenente i due risultati.
    """
    somma_pari = 0
    prodotto_dispari = 1
    ha_dispari = False
    
    for n in numeri:
        if n % 2 == 0:
            somma_pari += n
        else:
            prodotto_dispari *= n
            ha_dispari = True
            
    # Se la sequenza non conteneva numeri dispari, il prodotto viene impostato a 0
    if not ha_dispari:
        prodotto_dispari = 0
        
    return somma_pari, prodotto_dispari

# =============================================================================
# PROGRAMMA PRINCIPALE
# =============================================================================

def main():
    """
    Stampa somma dei pari e prodotto dei dispari per i numeri 2, 3, 4, 5, 6.

    Non riceve parametri e restituisce None.
    """
    # --- Sezione Inizializzazione Variabili ---
    # s_p: accumulatore per la somma dei numeri pari restituita dalla funzione
    # p_d: accumulatore per il prodotto dei numeri dispari restituito dalla funzione

    print("=== Elaborazione di un numero arbitrario di valori ===\n")

    # Chiamata alla funzione con una serie di valori numerici (Input di test)
    # In questo caso passiamo: 2, 3, 4, 5, 6
    # Somma pari attesa: 2 + 4 + 6 = 12
    # Prodotto dispari atteso: 3 * 5 = 15
    s_p, p_d = elabora_numeri(2, 3, 4, 5, 6)

    # Stampa in output dei risultati
    print(f"Valori analizzati: 2, 3, 4, 5, 6")
    print(f"Risultato - Somma dei pari: {s_p}")
    print(f"Risultato - Prodotto dei dispari: {p_d}")

if __name__ == "__main__":
    main()