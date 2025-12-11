# Leggi un file di testo e stampa solo le righe che iniziano con #.

def main():
    file = open("frasi.txt","r")
    frasi = file.readlines()
    file.close()

    for frase in frasi:
        if frase[0] == "#":
            print(f"{frase}, inizia con # ")
        
if __name__ == "__main__":
    main()
