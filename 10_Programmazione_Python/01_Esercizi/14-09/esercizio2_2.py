# Chiede il numero totale dei conti correnti da elaborare
N = int(input("Inserisci il numero di conti correnti (N): "))
# Inizializza la variabile per accumulare la somma dei saldi negativi
somma_negativi = 0
# Inizializza il contatore per contare quanti conti sono in rosso
contatore_negativi = 0

# Esegue un ciclo iterativo per ciascuno degli N conti correnti
for i in range(N):
    saldo = float(input(f"Inserisci il saldo del conto {i+1}: "))
    # Verifica se il conto ha un saldo negativo
    if saldo < 0:
        somma_negativi += saldo       # Accumula il saldo negativo
        contatore_negativi += 1       # Incrementa il totale dei conti negativi

# Calcola la media se è stato registrato almeno un saldo in rosso
if contatore_negativi > 0:
    print("La media dei saldi negativi è:", somma_negativi / contatore_negativi)
else:
    print("Non sono stati inseriti saldi negativi.")