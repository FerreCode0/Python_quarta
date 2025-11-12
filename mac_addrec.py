def main():
    file = open("mac-vendors-export.csv", "r")
    #risolve i problemi dell'apertura file in windows
    righe = file.readlines()
    file.close()

    mac = input("inserisci il mac addres= ")
    for riga in righe:
        if riga[0:9] == mac:
            print(riga)

if __name__=="__main__":  #__ si chiama dunder (double underscore)
    main()