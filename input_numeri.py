intero = int(input("inserici un numero intero ->"))
print(f"Hai inserito {intero} che e' di tipo {type(intero)}")

decimale = float(input("inserici un numero decimale ->"))
print(f"Hai inserito {decimale} che e' di tipo {type(decimale)}")

somma = intero + decimale
print(f"La somma tre i due numeri vale {somma} ed e di tipo {type(somma)}")