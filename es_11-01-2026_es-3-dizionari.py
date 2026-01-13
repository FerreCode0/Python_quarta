# Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
# trovare quale voto compare più spesso.
studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
}

conteggio = {}

for studente in studenti_voti:
    voto = studenti_voti[studente]

    if voto in conteggio:
        conteggio[voto] += 1
    else:
        conteggio[voto] = 1
    
max_voto = 0
occorrenze = 0

for voto in conteggio:
    if conteggio[voto] > occorrenze:
        occorrenze = conteggio[voto]
        max_voto = voto

print("Voto più frequente:", max_voto)

