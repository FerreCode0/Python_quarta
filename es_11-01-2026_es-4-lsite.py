# Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.

lista_a = [1, 5, 8, 12, 15, 20]
lista_b = [3, 5, 10, 12, 18, 20, 25]
lista_ab = []

for a in lista_a:
    for b in lista_b:
        if a == b:
            lista_ab.append(a)
print(lista_ab)