# Dato un elenco di nomi, stampa solo quelli che iniziano con la lettera “c”.
# Poi stampa tutti gli altri senza modifiche.

lista = ["ciao", "gabri", "asia", "cristian", "caste", "dido"]

for paroleC in lista:
    if paroleC[0] == "c":
        print(paroleC)
for parole in lista:
    if parole[0] != "c":
        print(parole)