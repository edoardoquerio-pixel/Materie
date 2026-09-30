import math

raggio = float(input("inserisci il raggio del cerchio: "))
if raggio >0:
    area = math.pi*raggio**2
    circonferenza = 2*math.pi*raggio
    print ("l'area del cerchio è: ", area)
    print ("la circonferenza del cerchio è: ", circonferenza)
else:
        print("raggio non valido")