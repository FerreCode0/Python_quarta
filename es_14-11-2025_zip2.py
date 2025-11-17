# Si vuole gestiremun magazino, nel magazzi possono entrare dei prodotti
# in una certa quantità, stampare dopo ingresso la situazione dopo lo scarico

def main():
    file = open("magazzino.txt", "r")
    titolo = file.readline()
    righe = file.readlines()  # righe = righe[1:], sono la stessa cosa
    file.close()

    nomi = []
    quantita = []
    tot = 0
    
    for riga in righe:
        lista = riga.split(",")
        nomi.append(lista[0])
        qt = lista[1]
        quantita.append(int(qt[:-1]))

    print(f"{titolo}")
    for n, q in zip(nomi, quantita):
        print(f"{n} - {q}")
        tot += q
    print(f"la quatità totale è di: {tot}")
if __name__ == "__main__":
    main()