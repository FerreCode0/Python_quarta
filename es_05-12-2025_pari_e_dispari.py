# fare un programma che simuli n partite n. partite, 
# - in input n: n. di partite
# - nome primo giocatore
# - nome secondo giocatore

# 1)per simulare le partite usiamo un dizionario
# esempio nel caso n = 3
# d = {"Nome giocatore 1": [3, 2, 5], "nome giocatore 2": [1,4,4]}
# le singole giocate sono generate con random.randit()

# 2) creare una lista che contiene i nomi dei vincitori per ogni partita e stamparla,
# ipotesi: il primo giocatore vince se esce pari.
import random
MIN = 0
MAX = 5
partite = int (input("Inserire il numero di partite che si vuole fare: "))
giocatore1 = input("Inserire il nome del primo giocatore: ")
giocatore2 = input("Inserire il nome del secondo giocatore: ")
vincitore_round = []
vincitore_finale = []
nomi = [giocatore1, giocatore2]

lancio_g1 = []
lancio_g2 = []
d = {giocatore1: [], giocatore2: []}

for i in range(0,partite):
    lancio_g1 = random.randint(MIN, MAX)
    lancio_g2 = random.randint(MIN, MAX)
    ris = lancio_g1 + lancio_g2
    d[giocatore1].append(lancio_g1)
    d[giocatore2].append(lancio_g2)
    
    if ris % 2 == 0:
        vincitore_round.append(giocatore1)
    else:
        vincitore_round.append(giocatore2)


print(f"Numeri lanciati dai giocatori {d}")
print(f"Vincitore di ciascun round {vincitore_round}")
