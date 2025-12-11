def main():
    file = open("./dati.csv","r",encoding= "utf8")
    righe = file.readlines() 
    file.close()
    lista_nomi = ["rob","frank","mg"]
    lista_voti =["8","7","9"]
    frase = input("insericsci una frase --> ")
    print("uso di input:")
    print(f"{frase}\n")
    print("ciclo for con uso di append enumerate")
    righe.append("192.168.1.150, server_laboratorio,3\n")
    for i,riga in enumerate(righe):
        print(f"{i+1}-{riga}")
    print("ciclo for con split e replace degli ip di dati.csv")
    for dati in righe[1:]:
        dati = dati[0:13]
        dati_s = dati.replace("-",".").split(",")
        print(dati_s)
    print("\nuso len per calcolare la lunghezza dell'ultima stringa di riga:")
    print(f"{len(riga)}\n")
    print("uso di replace() e uso anche si upper")
    frase_modificata = frase.replace("c","d")
    print(f"la frase modicicata: {frase_modificata.upper()}\n")
    print("uso del ciclo for con zip ")
    for nomi,voti in zip(lista_nomi,lista_voti):
        print(f"nomi: {nomi.split(",")} voti: {voti}")
    print("\n")

    

if __name__ == "__main__":
    main()