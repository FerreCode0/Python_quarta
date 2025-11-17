# Si vuole gestiremun magazino, nel magazzi possono entrare dei prodotti
# in una certa quantità, stampare dopo ingresso la situazione dopo lo scarico

def main():
    print("inizia lo scaricamento: ")
    nomeProdotti = []
    quantitaProdotti = []
    nome = input("inserisci il nome del prodotto ->").lower()
    while nome != "fine":
        quantita = int(input("inserisci la quantità del prodotto ->"))
        quantitaProdotti.append(quantita)
        nomeProdotti.append(nome)
        nome = input("inserisci il nome del prodotto ->").lower()
    
    for n, q in zip(nomeProdotti, quantitaProdotti):
        print(f"{n} - {q}")
if __name__ == "__main__":
    main()