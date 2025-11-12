# il carattere # serve pr i commenti
# in questo programma useremo l'assegnazione

# in python non ci sono le dichiarazioni, python fa
# dynamic type checking (controllo dinamico dei tipi)
# sulla base dei valori assegnati alle variabili

a = input("Scrivi qualcosa ->") # è simile a scanf
# input retituisce sempre stringhe!
# facciamo una print con una f-string
print(f"Hai inserito {a} che e' di tipo {type(a)}")