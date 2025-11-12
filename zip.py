def main():
    lista_nomi = ["Alice", "Luca", "Giovanni", "Mario"]
    lista_voti = [[6, 7, 8, 5],
                  [6, 7],
                  [4, 7, 7, 4], 
                  [2, 6, 7, 4]]


    # Voglio stampare il voto a fianco di ogni nome
    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")

    for nome, voto in zip(lista_nomi, lista_voti):
        pass
    # zip() mi permette di ciclare in parallelo su
    # due o più liste

if __name__=="__main__":  #__ si chiama dunder (double underscore)
    main()


    #modificare il codice sotto per:
    #-stampare la media
    #-stampoare il numero di voti per ognuno
    #-stamopare il voto massimo e il voto minimo