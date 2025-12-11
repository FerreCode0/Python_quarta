def main():
    #un dizionario è una freguenza di coppie chiavi: valore
    elenco = {"A3-32-B4-FF-F4-32": "Luca",
              "65-A0-AA-11-F4-19":"Mario"}
    mac = "A3-32-B4-FF-F4-32"
    
    if mac in elenco :
        print(elenco[mac])
    else: 
        print("MAC non trovato !")
    #aggiungiamo nuovo elemento al dizionario
    elenco ["FF-FF-FF-FF-FF-FF"] = "broadcast"
    print(elenco)
 
if __name__ == "__main__":
    main()

# quando aggiungi