"""Trova il minimo tra N numeri inseriti, richiedendo N maggiore di zero."""

# Chiediamo all'utente quanti numeri vuole inserire
N = int(input("Inserisci il numero di elementi (N): "))

# Verifichiamo che N sia un numero valido
if N <= 0:
    print("Il numero di elementi deve essere maggiore di zero.")
else:
    # Inizializziamo il minimo con il primo numero inserito
    minimo = float(input("Inserisci il numero 1: "))

    # Confronta i restanti numeri inseriti dall'utente con il minimo attuale
    # Ciclo per leggere i restanti N-1 numeri
    for i in range(1, N):
        numero = float(input(f"Inserisci il numero {i+1}: "))
        
        # Se il numero appena inserito è minore del minimo attuale, aggiorniamo il minimo
        if numero < minimo:
            minimo = numero
            
    # Stampiamo il risultato finale
    print("Il numero minimo inserito è:", minimo)
