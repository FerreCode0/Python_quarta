file= open("mac-vendors-export.csv", "r") ##oggetto file
righe = file.readlines()##lista di stringhe che contiene le righe
##   print(file) ##stampa nn il contenuto del file ma delle info sul file
print(righe)
file.close()

##   print(righe[0]) ## stampa la prima riga
prima_riga = righe[0]

# unpaching -->spacchettamento
titolo1, titolo2, titolo3= prima_riga[0] [0:-1].split(",")
print(titolo1)


##leggere tutte le altre rghe del file e stamparle, usare un ciclo for paytonico (NO RANGE)