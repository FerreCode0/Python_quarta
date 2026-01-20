#Un dizionario associa nomi di playlist a liste di titoli di canzoni. Scrivere funzioni per:
#(a) contare le canzoni totali, (b) cercare in quale playlist si trova una canzone, (c) unire
#due playlist in una nuova.

def conta_canzoni(playlist):
    Ncanzoni = 0
    for genere in playlist:
        Ncanzoni += len(playlist[genere])
    print(f"in totale ci sono {Ncanzoni} canzoni")

def cerca_canzone(playlist, ricerca):
    for genere in playlist:
        for canzone in playlist[genere]:
            if ricerca == canzone.lower():
                print(f"la canzone che hai inserito e nella categoria {genere}")

def unione_playlist(playlist, can_1, can_2):
    playlist_2 = []
    for genere in playlist:
        if can_1 in genere:
            playlist_2.append(genere)
        if can_2 in playlist:
            playlist_2.append(genere)
    print(f"le canzini che hai unito sono: {playlist_2}")

def main():
    playlist = {
    "Rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "Pop": ["Thriller", "Like a Prayer", "Billie Jean"],
    "Relax": ["Hotel California", "Imagine", "Let It Be"]
    }
    #conta_canzoni(playlist)
    #ricerca = input("inserisci la canzone che vuoi cercare: ").lower()
    #cerca_canzone(playlist, ricerca)
    can_1 = input("quale playlist vuoi unire? = ")
    can_2 = input("quale playlist vuoi unire? = ")
    unione_playlist(playlist, can_1, can_2)


if __name__ == "__main__":
    main()