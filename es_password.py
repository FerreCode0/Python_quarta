#l'utente inserisce in input una password
#il programma stampa la password oscurata da *

password = input("inserisci una password --> ")
password_blenked = "*" * len(password)
print(f"hai inserito la passowrd: {password_blenked}")