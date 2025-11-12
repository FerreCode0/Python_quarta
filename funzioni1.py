# MODULARITA: suddividere il codice in funzioni.

# COSTANTE è una variabile globale
#ATTENZIONE: COSTANTE è accessibile da tutte le funzioni soltanto in lettra!
COSTANTE = 3.14

def prima_lettera_maiuscola(stringa):
    '''
    il nome di questa cosa nella riga 6 si chiama DOCSTRING
    la funzione restituisce la stringa con la lettera iniziale minuscola
    '''
    # stringa è una variabile locale alla funzione
    s = stringa[0].upper() + stringa[1:].lower()
    return s

def media(lista):
    '''
    la funzione restituisce la media dei valori presenti in lista
    e il numero di elementi di lista
    '''
    somma = 0.
    n_lista = len(lista)
    for val in lista:
        somma = somma + val

    return somma/n_lista, n_lista

def main():
    #print(help(prima_lettera_maiuscola))
    #nome = input("inserisci una parola ->")
    #print(prima_lettera_maiuscola(nome))
    voti = [4.5, 10, 8.25, 7, 6]
    m, n = media(voti)
    print(f"La media è {m}, il numero di voti è {n}.")

if __name__=="__main__": 
    main()