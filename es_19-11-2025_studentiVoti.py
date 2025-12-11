# Dato un elenco di nomi e una lista di liste con i voti,
# stampa per ogni studente:
# - i voti
# - la media
# - il voto massimo
# - il voto minimo
# - il numero di voti

nomi = ["Marco", "Luca", "Anna", "Sara"]
voti = [
    [7, 8, 6, 9],
    [5, 6, 7],
    [9, 10, 8, 9, 10],
    [6, 6, 5, 7]
]

for i in range(len(nomi)):
    nome = nomi[i]
    lista_voti = voti[i]

    media = sum(lista_voti) / len(lista_voti)
    voto_max = max(lista_voti)
    voto_min = min(lista_voti)
    numero_voti = len(lista_voti)

    print(f"Studente: {nome}")
    print(f"  Voti: {lista_voti}")
    print(f"  Media: {media:.2f}")
    print(f"  Voto massimo: {voto_max}")
    print(f"  Voto minimo: {voto_min}")
    print(f"  Numero di voti: {numero_voti}")
    print("-" * 30)
