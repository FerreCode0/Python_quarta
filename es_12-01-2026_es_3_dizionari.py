# Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
# trovare quale voto compare più spesso.
def main():
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

    diz_contatori = {} #la chiave è il voto, il valore è il numero di occorrenze

    for studente in studenti_voti:
        voto = studenti_voti[studente]
        if voto in diz_contatori:
            diz_contatori[voto] += 1
        else:
            diz_contatori[voto] = 1
    
    voto_piu_frequente = 6
    frequenza_max = diz_contatori[6]

    for voto in diz_contatori:
        if diz_contatori[voto] > frequenza_max:
            frequenza_max = diz_contatori[voto]
            voto_piu_frequente = voto
    print(f"Il voto più frequente è {voto_piu_frequente}, ed è capitato {frequenza_max} volte.")

if __name__ == "__main__":
    main()