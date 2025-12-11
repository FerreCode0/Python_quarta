# Leggi un file CSV contenente numeri separati da virgole e stampa la SOMMA totale di tutti i numeri

def main():
    file = open("somma.csv", "r")
    numeri = file.readlines()
    file.close()

    somma = 0
    for n in numeri:
        valori = n.split(",")        # lista di numeri come stringhe
        for v in valori:             # ciclo sui singoli valori
            somma += float(v)  # converto e sommo

    print(f"La somma dei numeri è {somma}")

if __name__ == "__main__":
    main()
