# Un dizionario associa nomi di materie a liste di voti.
# (a) calcolare la media di una materia
# (b) trovare la materia con media più alta
# (c) aggiungere un voto a una materia

def calcola_media(voti_materie, materia):
    SommaVoti = 0
    nVoti = len(voti_materie[materia])

    for voto in voti_materie[materia]:
        SommaVoti += voto

    media = SommaVoti / nVoti
    return media


def materia_media_piu_alta(voti_materie):
    max_media = 0
    materia_max = None

    for materia in voti_materie:
        media = calcola_media(voti_materie, materia)
        if media > max_media:
            max_media = media
            materia_max = materia

    return materia_max, max_media


def aggiungi_voto(voti_materie, materia, voto):
    voti_materie[materia].append(voto)


def main():
    voti_materie = {
        "Matematica": [6, 7, 5, 8, 7],
        "Italiano": [7, 8, 7, 6],
        "Inglese": [8, 8, 9, 7, 8],
        "Informatica": [9, 8, 9, 10, 8]
    }

    # (a) media di una materia
    materia = "Matematica"
    media = calcola_media(voti_materie, materia)
    print(f"La media di {materia} è: {media}")

    # (b) materia con media più alta
    materia_max, media_max = materia_media_piu_alta(voti_materie)
    print(f"La materia con la media più alta è {materia_max}: {media_max}")

    # (c) aggiungere un voto
    aggiungi_voto(voti_materie, "Italiano", 9)
    print("Voti aggiornati di Italiano:", voti_materie["Italiano"])


if __name__ == "__main__":
    main()
