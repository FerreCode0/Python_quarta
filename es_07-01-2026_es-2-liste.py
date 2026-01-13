#Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza
#usare sort o sorted).
valori = [45, 12, 78, 34, 67, 23, 89, 56]

def secondoMassimo(valori):

    massimo = valori[0]
    min = valori[0]
    for v in valori:
        if v < min:
             min = v
        if v > massimo:
            massimo = v
    secondoMassimo = min
    for v in valori:
        if (v > secondoMassimo) and (v != massimo):
                secondoMassimo = v
    return secondoMassimo

def main():
    n = secondoMassimo(valori)
    
    print(n)
if __name__ == "__main__":
    main()