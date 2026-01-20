def temp_media(dati):
    somma = 0
    Ndati = len(dati)
    for luogo in dati:
        somma += luogo["temp"]
    media = somma / Ndati
    print(f"la media delle temperature è pari a {media:.2f}°")

def filtra_citta(dati, citta):
    temperatura = []
    for luogo in dati:
        if citta in luogo["citta"]:
            temperatura.append(luogo["temp"])
    return temperatura

def temp_per_citta(dati):
    lista_citta = {}
    for luogo in dati:
        if luogo["citta"] not in lista_citta:
            lista_citta[luogo["citta"]] = [luogo["temp"]]
        else:
            lista_citta[luogo["citta"]].append(luogo["temp"])
    return lista_citta

def carica_regioni(nome_file):
    file = open(nome_file, "r")
    righe = file.readlines()
    file.close()

    diz = {}
    for riga in righe:
        campi = riga.split(';')
        diz[campi[0]] = campi[1][:-1]
    return diz

def main():
    dati = [
        {"citta": "Milano", "temp": 12},
        {"citta": "Roma", "temp": 18},
        {"citta": "Milano", "temp": 14},
        {"citta": "Napoli", "temp": 20},
        {"citta": "Roma", "temp": 17},
        {"citta": "Napoli", "temp": 22},
        {"citta": "Milano", "temp": 10}
    ]
    temp_media(dati)
    print("----------------------------------------------------------------------")
    ricerca = "Milano"
    print(filtra_citta(dati, ricerca))
    print("----------------------------------------------------------------------")
    print(temp_per_citta(dati))
    print("----------------------------------------------------------------------")
    print(carica_regioni('regioni.txt'))

if __name__ == "__main__":
    main()