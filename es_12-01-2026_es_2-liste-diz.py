# Una lista contiene dizionari con chiavi nome, punteggio. Scrivere una funzione che
# stampi la classifica ordinata per punteggio decrescente, numerando le posizioni.

def stampa_classifica(giocatori):
    classifica = sorted(giocatori, key=lambda punteggio: punteggio["punteggio"], reverse=True) #il primo elemto (giocatore) dice dove in quele lista bisogna fare ciclo, 
                                                                               #secondo bisogna lasciare key=lambda con la variabile che deve essere associata alla chiave dell'elemtento nella lista,
                                                                               #terzo è l'ordine in qui deve essere ordinata la nuova lista in questo caso con il True crea un'ordine decrescente
    count = 1

    for giocatore in giocatori:
        print(f"{count}. {giocatore['nome']} - {giocatore['punteggio']}")
        count += 1

def main():
    giocatori = [
        {"nome": "Player1", "punteggio": 4500},
        {"nome": "Player2", "punteggio": 7200},
        {"nome": "Player3", "punteggio": 3100},
        {"nome": "Player4", "punteggio": 8900},
        {"nome": "Player5", "punteggio": 5600}
    ]
    stampa_classifica(giocatori)
           

if __name__ == "__main__":
    main()