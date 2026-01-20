#Catalogo libri
#Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
#per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più
#recente.

def cerca_autore(libri, ricerca):
    for libro in libri:
        if 

def main():
    libri = [
        {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
        {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
        {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},   
        {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
        {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]
    ricerca = input("inserisci il libro: ")
    cerca_autore(libri, ricerca)
if __name__ == "__main__":
    main()
