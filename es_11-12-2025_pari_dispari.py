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
    
def main():
    n = int(input("quante partite vuoi giocare? = "))
    gio1 = input("inserisci il nome del primo giocatore = ")
    gio2 = input("inserisci il nome del secondo giocatore =")
    diz = {gio1 : [], gio2: []}
    vincitori = []
    for num in range(n):
        lancio1 = random.randint(0, 5)
        lancio2 = random.randint(0, 5)
        diz[gio1].append(lancio1)
        diz[gio2].append(lancio2)
        somma = lancio1 + lancio2
        resto = somma % 2
        if(resto == 0):
            vincitori.append(gio1)
        else:
            vincitori.append(gio2)
    print(vincitori)
if __name__ == "__main__":
    main()