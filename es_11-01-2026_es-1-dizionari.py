# Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte
# che compare.
testo = "abracadabra"

conteggio = {}

for c in testo:
    if c in conteggio:
        conteggio[c] += 1
    else:
        conteggio[c] = 1

print(conteggio)