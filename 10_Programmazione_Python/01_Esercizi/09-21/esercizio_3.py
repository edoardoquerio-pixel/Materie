"""Legge una temperatura Fahrenheit e stampa la conversione in Celsius."""

# =============================================================================
# DEFINIZIONE DELLE FUNZIONI
# =============================================================================

def convertiCF(fahrenheit):
    """
    Descrizione: Converte una temperatura da gradi Fahrenheit a gradi Celsius.
    Parametri formali:
        - fahrenheit (float): valore della temperatura da convertire.
    Restituisce:
        - float: il valore convertito in gradi Celsius.
    """
    # Formula: C = (F - 32) * 5 / 9
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# =============================================================================
# PROGRAMMA PRINCIPALE
# =============================================================================

def main():
    """
    Legge una temperatura e stampa i gradi Celsius, segnalando input non numerici.

    Non riceve parametri e restituisce None.
    """
    # --- Sezione Inizializzazione Variabili ---
    # gradi_f: variabile per memorizzare l'input dell'utente (float)
    # gradi_c: variabile per memorizzare il valore restituito dalla funzione (float)

    print("=== Convertitore Temperatura Fahrenheit -> Celsius ===\n")
    
    # Acquisizione dell'input
    try:
        gradi_f = float(input("Inserisci la temperatura in Fahrenheit: "))
        
        # Richiamo della funzione di conversione
        gradi_c = convertiCF(gradi_f)
        
        # Stampa del risultato con formattazione a 3 cifre decimali
        print(f"\nRisultato: {gradi_c:.3f} °C")
        
    except ValueError:
        print("Errore: Inserire un valore numerico valido.")

if __name__ == "__main__":
    main()
