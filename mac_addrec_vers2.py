def main():
    with open("mac-vendors-export.csv", "r", encoding = 'utf-8') as file:
        righe = file.readlines()
    

    m = input("inserisci le prime 8 cifre del MAC address ->").upper()
    m = m.replace(m[2], ":")
    for riga in righe[1:]:
        lista = riga.split(",")
        if m[0:8] == lista[0]:
            print(lista[1])
            print(lista[-1])

if __name__ == "__main__":
    main()
        