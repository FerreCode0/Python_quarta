def main():
    file = open("mac-vendors-export.csv","r", encoding = 'utf-8')
    righe = file.readlines()
    file.close()

    nome = input("inserisci il MAC addres del tuo pc: ")
    for riga in righe:
        campi = riga.split(",")
        if nome[0:8] == campi[0]:
            print(campi[1])
            print(campi[-1])
if __name__ == "__main__":
    main()