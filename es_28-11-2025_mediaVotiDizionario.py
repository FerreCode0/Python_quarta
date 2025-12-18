def leggi_registro(file):
    diz = {}
    lines = file.readlines()
    for line in lines:
        dati = lines.split(';')
        voti = []
        for voto_stringa in dati[1:]:
            voti.append(int(voto_stringa))
        diz[dati[0]] = voti
    return diz

def classifica(registro):
    lista_voti = []
    for nome in registro():
        lista_voti.append((nome, calcola_media(registro[nome])))
    lista_ordinata = sorted(lista_voti, reverse=True)
    return lista_voti

def calcola_media(voti):
    return sum(voti)/len(voti)

def main():
    file = open("registro.txt", "r")
    diz = leggi_registro(file)



