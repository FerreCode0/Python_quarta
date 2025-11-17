# dato n numero intero stampare i primi n. dispari

n = int(input("inserisci in numero intero -> "))

for numeri in range(0, n * 2 + 1):
    if numeri % 2 != 0:
        print(numeri)