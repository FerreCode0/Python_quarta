# Crea un menu interattivo:
#A → inserisci
#B → modifica
#C → cancella
#Ogni scelta deve stampare un messaggio.
#Input valido anche se l’utente scrive in minuscolo.

print("fai la tua scelta!!!")
print("A → inserisci")
print("B → modifica")
print("C → cancella")
scelta = input("inserisci la lettera analoga all'azione che vuoi compiere ->").upper()

if scelta == "A":
    print(f"hai scelto la lettera {scelta}.\nvuoi inserire!")
if scelta == "B":    
    print(f"hai scelto la lettera {scelta}.\nvuoi modificare!")
if scelta == "C":
    print(f"hai scelto la lettera {scelta}.\nvuoi cancellare!")
