#Scrivi una funzione media(lista) che ritorna:
#la media dei valori
#il numero di elementi
#Usala su una lista di voti.

def main ():
    lista = [9, 7, 7, 5, 9, 4, 7]
    print(lista)
    media(lista)

def media(lista):
    nVoti = len(lista)
    somma = 0
    for numero in lista:
        somma += numero
    mediaTot = somma / nVoti
    print(f"la media dei voti dello stidente è: {mediaTot}")
    print(f"la media è basta su {nVoti} voti")

if __name__ == "__main__":
    main()