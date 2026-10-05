"""Confronta due durate inserite in ore, minuti e secondi convertendole in secondi."""

# =============================================================================
# DEFINIZIONE DELLE FUNZIONI
# =============================================================================

def calcola_secondi(ore=0, minuti=0, secondi=0):
    """
    Descrizione: Converte una quantità di tempo espressa in ore, minuti e secondi 
                 nel corrispondente valore totale in secondi.
    Parametri formali:
        - ore (int): numero di ore (default 0)
        - minuti (int): numero di minuti (default 0)
        - secondi (int): numero di secondi (default 0)
    Restituisce:
        - int: il totale dei secondi (tipo intero)
    """
    # Calcolo: 1 ora = 3600 secondi, 1 minuto = 60 secondi
    totale = (ore * 3600) + (minuti * 60) + secondi
    return totale

# =============================================================================
# PROGRAMMA PRINCIPALE
# =============================================================================

def main():
    """
    Legge due durate e stampa il confronto dei totali in secondi.

    Non riceve parametri e restituisce None.
    """
    # --- Sezione Inizializzazione Variabili ---
    # h, m, s: variabili per memorizzare ore, minuti e secondi inseriti
    # tempo1_sec: totale secondi della prima quantità
    # tempo2_sec: totale secondi della seconda quantità

    print("=== Confronto tra due quantità di tempo ===")

    # Input della prima quantità di tempo
    print("\nInserisci la prima quantità di tempo:")
    h1 = int(input("Ore: "))
    m1 = int(input("Minuti: "))
    s1 = int(input("Secondi: "))

    # Input della seconda quantità di tempo
    print("\nInserisci la seconda quantità di tempo:")
    h2 = int(input("Ore: "))
    m2 = int(input("Minuti: "))
    s2 = int(input("Secondi: "))

    # Esecuzione del calcolo tramite funzione
    tempo1_sec = calcola_secondi(h1, m1, s1)
    tempo2_sec = calcola_secondi(h2, m2, s2)

    # Confronto dei risultati e output
    print("\n--- Risultato ---")
    if tempo1_sec > tempo2_sec:
        print("La PRIMA quantità di tempo è maggiore.")
        print(f"Dettaglio: {tempo1_sec} secondi contro {tempo2_sec} secondi.")
    elif tempo2_sec > tempo1_sec:
        print("La SECONDA quantità di tempo è maggiore.")
        print(f"Dettaglio: {tempo2_sec} secondi contro {tempo1_sec} secondi.")
    else:
        print("Le due quantità di tempo sono UGUALI.")
        print(f"Dettaglio: entrambi equivalgono a {tempo1_sec} secondi.")

# Richiamo del programma principale
if __name__ == "__main__":
    main()
