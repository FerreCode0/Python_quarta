# In python possiamo delimitare con "" oppure ''
stringa = "Ciao mondo!"
print (stringa)

#Esempio di indicizazione della stringa
print(f"l'ultimo carattere della stringa è {stringa[-1]}")

# Esempio di slicing delle stringhe
print(f"La sottstringa 2-5 è {stringa[2:5]}.")

# Assegnazione multipla (vale per ogni tipo di dato)
nome, cognome = "Mario", "Rossi"

# Concatenazione tra stringhe 
x = nome + " "+ cognome
print(x)

#???????
y = (nome+" ")*5
print(y)