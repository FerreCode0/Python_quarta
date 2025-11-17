# Chiedi all’utente una parola e stampa la versione oscurata:
# visibile solo la prima e l’ultima lettera
# tutte le altre sostituite con *

parola = input("inserisci una parola ->")

nCaratteri = len(parola) - 2
print(parola[0] + "*" * nCaratteri + parola[-1])