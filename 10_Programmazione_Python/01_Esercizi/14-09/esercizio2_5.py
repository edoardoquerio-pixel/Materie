# Chiediamo il numero di alunni (N)
num_alunni = int(input("Inserisci il numero di alunni nella classe: "))

# Verifica che il numero di studenti inserito sia valido
if num_alunni <= 0:
    print("Il numero di alunni deve essere maggiore di zero.")
else:
    # Ciclo esterno per gestire l'inserimento dei dati di ogni singolo studente
    for i in range(num_alunni):
        print(f"\n--- Alunno {i + 1} ---")
        # Chiediamo il numero di voti (M) per l'alunno corrente
        num_voti = int(input(f"Quanti voti vuoi inserire per l'alunno {i + 1}? "))

        # Controllo sulla validità del numero totale di voti per studente
        if num_voti > 0:
            somma_voti = 0    # Inizializza l'accumulatore dei voti dello studente
            # Ciclo interno per raccogliere tutti i voti dell'alunno corrente
            for j in range(num_voti):
                voto = float(input(f"Inserisci il voto {j + 1}: "))
                somma_voti += voto    # Aggiunge il voto alla somma complessiva del singolo alunno
            
            # Calcola la media aritmetica dei voti dello studente corrente
            media = somma_voti / num_voti
            # Mostra la media formattata con due cifre decimali (.2f)
            print(f"La media dei voti per l'alunno {i + 1} è: {media:.2f}")
        else:
            print("Il numero di voti deve essere maggiore di zero.")
