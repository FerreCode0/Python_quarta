# Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
# per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più
# recente.

def stampaLibriAutore(lista, nome):
    trovati = []
    for libro in lista:
        if libro["autore"].lower() == nome.lower():
            trovati.append(libro)
    return trovati

def calcolaPrezzoMedio(lista):
    somma_prezzi = 0
    for libro in lista:
        somma_prezzi += libro["prezzo"]
    numero_libri = len(lista)
    return somma_prezzi / numero_libri

def libroRecente(lista):
    libro_max = lista[0]
    anno_max = libro_max["anno"]
    for libro in lista:
        if libro["anno"] > anno_max:
            anno_max = libro["anno"]
            libro_max = libro
    return libro_max

def main():
    libri = [
        {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
        {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
        {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
        {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
        {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]
    libro = stampaLibriAutore(libri, "umberto eco")
    print(libro)
    media = calcolaPrezzoMedio(libro)
    print(f"Media Prezzi: {media}€")
    recente = libroRecente(libro)
    print(f"il libro piu recente è: {recente}")

if __name__ == "__main__":
    main()