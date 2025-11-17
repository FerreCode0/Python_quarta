# calcolare la somma di tutti i numeri nel file

def main():
    
    file = open("numeri.csv", "r")
    righe = file.readlines()
    file.close()
    
    somma = 0
    for riga in righe:
        n = riga[0:-1]
        numeri = n.split(",")
        for numero in numeri:
            somma += int(numero)
    print(f"la somma di tutti i numeri dentro il file è: {somma}")

if __name__ == "__main__":
    main()