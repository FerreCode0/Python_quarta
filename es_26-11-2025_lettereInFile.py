file = open("promessi_sposi.txt","r")
testo = file.read()
file.close()

lettere_diz = {}
conteggio = 0

for carattere in testo:
    if carattere.isalpha():
        lettera = carattere.lower()
        tot_lettere += 1
        if lettera in lettere_diz:
            lettere_diz[lettera] += 1
        else:
            lettere_diz[lettera] = 1

percentuali = {}
for lettura in lettere_diz:
    perc = (lettere_diz[lettera] * 100)/tot_lettere
    percentuali[lettera] = perc
    print


    