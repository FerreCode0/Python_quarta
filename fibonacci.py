#fibonacci

n = int(input("inserisci quanti numeri di fobonacci vuoi: "))

a = 1
b = 1

if n > 2:

    for i in range(n-4):

        print(a, end=" - ")

        a,b = b, a+b

elif n == 0:

    print("nessun numero stampato...")

elif n == 2:

    print(a, end=" - ")
    print(b)

elif n == 1:

    print(b)
