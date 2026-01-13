#Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con
#i numeri pari e una con i dispari.
#numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]

def separa_pari_dispari(numeri):
    pari = []
    dispari = []

    for n in numeri:
        if n % 2 == 0:
            pari.append(n)
        else:
            dispari.append(n)

    return pari, dispari


def main():
    numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]

    pari, dispari = separa_pari_dispari(numeri)

    print("Lista originale:", numeri)
    print("Numeri pari:", pari)
    print("Numeri dispari:", dispari)


if __name__ == "__main__":
    main()
