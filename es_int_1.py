#stampa un punto esclamativo se la parola inizia con c


l = ["ciao", "python", "casa"]

for parola in l:
    if parola[0] == "c":
        print(parola + "!") 
    else:
        print(parola)
    