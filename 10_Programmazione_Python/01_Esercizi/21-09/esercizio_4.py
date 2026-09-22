# =============================================================================
# DEFINIZIONE DELLE FUNZIONI
# =============================================================================

def fattoriale(n):
    """
    Descrizione: Calcola il fattoriale di un numero intero non negativo.
    Parametri formali:
        - n (int): il numero di cui calcolare il fattoriale.
    Restituisce:
        - int: il valore del fattoriale.
    """
    risultato_f = 1
    for i in range(1, n + 1):
        risultato_f *= i
    return risultato_f

def calcola_e(N):
    """
    Descrizione: Calcola un'approssimazione del numero di Nepero 'e' sommando N termini.
                 Richiama la funzione fattoriale().
    Parametri formali:
        - N (int): il numero di termini della serie da sommare.
    Restituisce:
        - float: l'approssimazione di e ottenuta.
    """
    valore_e = 0.0
    # La serie parte da 0!: 1/0! + 1/1! + ... + 1/(N-1)!
    for i in range(N):
        valore_e += 1 / fattoriale(i)
        
    return valore_e

# =============================================================================
# PROGRAMMA PRINCIPALE
# =============================================================================

def main():
    # --- Sezione Inizializzazione Variabili ---
    # n_termini: numero di elementi della serie da calcolare (input utente)
    # e_stimato: variabile che conterrà il risultato dell'approssimazione restituito dalla funzione

    print("=== Calcolo approssimato del numero di Nepero 'e' ===\n")
    
    # Richiesta input all'utente
    input_utente = input("Inserisci il numero di termini (N) per l'approssimazione: ")
    
    # Validazione base dell'input
    if input_utente.isdigit():
        n_termini = int(input_utente)
        
        if n_termini > 0:
            # Chiamata alla funzione di calcolo
            e_stimato = calcola_e(n_termini)
            
            # Stampa del risultato
            print(f"\nRisultato con N={n_termini}:")
            print(f"e ≈ {e_stimato}")
            
            # Verifica del caso di test N=3
            if n_termini == 3:
                print("(Verifica esempio: 1/0! + 1/1! + 1/2! = 1 + 1 + 0.5 = 2.5)")
        else:
            print("Errore: Inserire un numero intero maggiore di zero.")
    else:
        print("Errore: Input non valido. Inserire un numero intero positivo.")

# Esecuzione del programma principale
if __name__ == "__main__":
    main()
