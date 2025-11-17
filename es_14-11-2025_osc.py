# Data una lista di parole creare la funzione che oscura con * tutte le lettere tranne la prima lettra

def password(parola):
    nCaratteri = len(parola)
    password_blanked = parola[0] + "*" * (int(nCaratteri - 1))
    return password_blanked

def main():

    lista = ["ciao", "calcio", "trapano"]
    for parola in lista:
        
        print(password(parola))

if __name__ == "__main__":
    main()


    