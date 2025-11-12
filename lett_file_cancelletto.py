file = open("nome file.txt", "r")
contenuto = file.readlines(file)

for righe in contenuto:
    if(righe[0] == '#'):
        print(righe)
close(file)