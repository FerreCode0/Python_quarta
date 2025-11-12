print("Premi A per inserire. ")
print("Premi B per modificare. ")
print("primi C per cancellare. ")

tasto = input("-->")
tasto = tasto.upper() #questa riga serve per trasformare qualsiasi input inserito dall'utente in maiuscolo
#per mettere tutte le lettere minuscole si mette:
#.lower()

if tasto == "A":
    print("L'utente vuole inserire")
elif tasto == "B": 
    print("L'utente vuole modificare")
elif tasto == "C":
    print("L'utente vuole calcellare")
else:
    print("Tasto non valido")
    