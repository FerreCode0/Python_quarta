lista = ["Luca", "Mario", "alice", "Giovanni"]

nomeMax = 0
lenMax = 0

for nome in lista:
    n = len(nome)
    if n > lenMax:
        lenMax = nomeMax
    print(nomeMax)