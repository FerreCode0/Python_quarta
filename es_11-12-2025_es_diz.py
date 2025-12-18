#data una rubrica telefoni e preso un numero di telefono in input o un nome di una persona
#bisogna vedere la corrispondenza numero persona

diz = {
    "3451237890": "Marco Rossi",
    "3479876543": "Giulia Bianchi",
    "3205567890": "Marco Rossi",
    "3391122334": "Luca Verdi",
    "3487788990": "Anna Russo"
}

cerca = input("inserisci il numero di telefono o il nome della perosona che vuoi cercare: ")
if cerca[0] in "1234567890":
    if cerca in diz:   #controlla solo le chiavi
        nome = diz[cerca]
        print(nome + " = " + cerca)
    else:
        print("il numero non è presente nella rubrica")
else:
    trovato = False
    for numero, nome in diz.items():
        if(cerca == nome):
            print(numero + " = " + nome)
            trovato = True
    if(trovato == False):
        print("valori non trovati!!!")
