# Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati,
# mantenendo l’ordine di prima apparizione.

elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]

s_duplicato = []
for parola in elementi:
    if parola not in s_duplicato:
        s_duplicato.append(parola)
print(s_duplicato)