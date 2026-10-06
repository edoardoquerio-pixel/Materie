"""Calcola la spesa con sconto del 5% da 100 a meno di 300 e del 10% da 300."""

# Riceve in input l'importo totale della spesa sostenuta dall'utente
spesa = int(input())

if spesa >= 100 and spesa < 300:
# Controlla se la spesa è tra 100 e 299 per applicare lo sconto del 5%
    print ("importo effettivo da pagare: ", spesa - (spesa*0.05))
# Controlla se la spesa è pari o superiore a 300 per applicare lo sconto del 10%
elif spesa >= 300:
    print("importo effettivo da pagare: ", spesa - (spesa*0.1))
# Se la spesa è minore di 100, non applica alcuno sconto
else :
    print("importo effettivo da pagare: ", spesa)


 