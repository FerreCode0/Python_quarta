# Chiedi all’utente il suo nome e stampalo con l’iniziale maiuscola, indipendentemente da come lo inserisce.

nome = input("inserisci il tuo nome ->")

maiscolo = nome[0].upper()
print(maiscolo + nome[1::])