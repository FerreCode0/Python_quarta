ip = input("inserisci l'indirizzo IP -->")
# .split(SEP) è un metodo delle stringhe che suddivide una 
# stringa cercando il carattere separatore (SEP)
ottetti_str = ip.split(".")
print(ottetti_str)

ottetti = [] # lista vuota
for s in ottetti_str:
    ottetti.append(int(s))

print(bin(ottetti[0]))