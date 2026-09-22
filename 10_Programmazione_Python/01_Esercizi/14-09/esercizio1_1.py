# Richiede all'utente di inserire il primo numero (coefficiente a)
print("insercisi primo numero")
a = float(input())

# Richiede all'utente di inserire il secondo numero (termine noto b)
print("inserisci secondo numero")
b = float(input())

# Controlla che il divisore 'a' sia diverso da zero per evitare errori matematici
if a != 0:
    # Calcola il risultato della divisione x = b / a
    x = b / a
    print("la soluzione è: ",x)
else:
    print("i numeri inseriti non sono corretti")