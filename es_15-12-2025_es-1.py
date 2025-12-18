# Legga un file chiamato numeri.csv contenente numeri interi separati da virgole su più righe.
# Calcoli e stampi:
# _La somma totale di tutti i numeri
# _Il numero massimo e minimo
# _La media (con 2 decimali)


file = open("numeri.csv", "r")
righe = file.readlines()
file.close()

somma = 0
contatore = 0
massimo = None
minimo = None

for riga in righe:
    valori = riga.strip().split(",")

    for v in valori:
        numero = int(v)

        somma += numero
        contatore += 1

        if massimo is None or numero > massimo:
            massimo = numero

        if minimo is None or numero < minimo:
            minimo = numero

media = somma / contatore

print("Somma:", somma)
print("Minimo:", minimo)
print("Massimo:", massimo)
print(f"Media: {media:.2f}")
