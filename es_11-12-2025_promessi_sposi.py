file = open("promessi_sposi.txt","r", encoding = 'utf-8')
testo = file.read()
file.close()

diz = {}
percentuale = {}
for lettera in testo:
    lettera = lettera.lower()
    if lettera in diz:
        diz[lettera] += 1
    else:
        diz[lettera] = 1
cerca = input("inserisci un carattere da ricercare: ")
if cerca in diz:
    print(diz[cerca])
else:
    print("il carattere non è nel testo")
for l in diz:
    perc = diz[l] / len(testo) * 100
    percentuale[l] = perc
p = input("inserisci un carattere da ricercare della percentuale: ")
if p in percentuale:
    print(f"{percentuale[p]:.2f}%")
else:
    print("il carattere non è nel testo")
somma = 0
for p in percentuale:
    somma += percentuale[p]
print(somma)

