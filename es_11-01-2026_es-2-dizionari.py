# Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. Se
# una parola non è nel dizionario, lasciarla invariata.
dizionario = {
"ciao": "hello",
"mondo": "world",
"casa": "house",
"gatto": "cat",
"cane": "dog",
"libro": "book",
"albero": "tree",
"è": "is"
}
frase = "ciao mondo il gatto è in casa"

p = frase.split()
tradotta = ""
for parola in p:
    if parola in dizionario:
        tradotta = dizionario[parola]
    else:
        tradotta = parola
    print(tradotta, end=" ")