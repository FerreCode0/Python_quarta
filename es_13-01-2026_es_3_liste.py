#Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati,
#mantenendo l’ordine di prima apparizione.
elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]

senza_duplicati = []
for elemento in elementi:
    if elemento not in senza_duplicati:
        senza_duplicati.append(elemento)
print(senza_duplicati)

