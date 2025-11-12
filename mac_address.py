def main():
    file = open("mac-vendors-export.csv", "r", encoding = "utf-8")
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    for riga in righe [1: 10]:
        campi = riga.split(",") #per ogni riga ho una lista di campi
        mac_address.append(campi[0])
        vendor.append(campi[1])

    print(mac_address)

    # exit() serve per compilare un programma fino a exit()
    mac = input("inserisci il MAC address per intero ->").upper()
    for m, v in zip(mac_address, vendor):
        if m [0:8] == mac [0:8]:
            print(f"il produttore è {v}")

if __name__=="__main__":  #__ si chiama dunder (double underscore)
    main()