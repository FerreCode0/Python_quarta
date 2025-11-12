def main():
    lista_nomi= ["gabriele", "giovanni", "rachele", "robert"]
    lista_voti = [[4, 6 , 7]]


    for nome, voti in zip(lista_nomi, lista_voti):
        somma = 0
        n_voti = len(voti)
        voto_max = 0
        voto_min = 0
        for voto in voti:
            somma += voto
            if voto > voto_max:
                voto_max = voto
            if voto < voto_min:
                voto_min = voto
        media = somma / n_voti

        print(f"i voti dell'alunno {nome}:\n{voti}")
        print(f"ecco la media dei voti di {nome}:\n{voti}") 
        print(f"{nome} ha {n_voti} voti")
        print(f"ecco il voto piu basso che ha preso: {nome}, {voto_min}, {voto_max}")

if __name__=="__main__":  #__ si chiama dunder (double underscore)
    main()
