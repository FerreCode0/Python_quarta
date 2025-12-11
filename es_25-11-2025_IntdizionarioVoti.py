nomi = ['luca', 'Mario', 'alice']
voti = [7, 8, 10]

diz = {}
for n, v in zip(nomi, voti):
    diz[n] = v
print(f'il voto di alice è : {diz["alice"]}')