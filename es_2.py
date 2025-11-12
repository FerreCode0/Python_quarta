# crea un programma in python che chiede all'utente il suo nome e lo stampa 
# sempre con l'iniziale miuscola

print("inserisci il tuo nome")

a = input("nome=")
a = a[0].upper()+ '*' *len(a).lower()

print(f"il tuo nome è:{a}")


