# Scrivi una funzione prima_lettera_maiuscola(stringa) che restituisce la stringa con la prima lettera maiuscola e le altre minuscole.

def prima_lettera_maiuscola(stringa):
    print(f"la tua strinfaga è {stringa[0].upper}")

def main():
    stringa = ["gabriele"]
    lettera = stringa[0].upper()

if __name__ == "__main__":
    main()