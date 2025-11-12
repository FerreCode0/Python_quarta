#in python abbiamo le condizioni. Tra le condizioni abbiamo:
#Liste, tuple, dizionari, Set.

#Vediamo le liste

#creare una lista

l = [3, 3.14 , 10, "ciao", True]

#Per accedere agli elementi valgono le stesse regole 
#di INDICAZIONE e SLICING  delle stringhe!

print(f"l'ultimo elemento della stringa è: {l[-1]}")
print(l)
print(f"Tutta la lista senza il primo e l'ultimo elemento è: {l[1:-1]}")

#Aggiunta di un elemento 

l.append("NUOVO") # NON RESTITUISCE NULLA, MA MODIFICA L!
print(l)
l.pop() # rimuove l'ultimo elemento
print(l)