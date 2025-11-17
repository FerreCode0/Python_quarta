def main():
    file = open("./mac-vendors-export.csv", "r", encoding = 'utf-8')
    righe = file.readlines()
    file.close()

    mac_address = []
    vendor = []
    date = []
    for riga in righe[1:]:
        campi = riga.split(",")
        mac_address.append(campi[0])
        vendor.append(campi[1])
        date.append(campi[-1])

    mac = input("Inserisci le prime otto cifre del MAC address -> ").upper()
    # gestire anche il carattere - come separatore dei byte del MAC
    # usare il metodo replace delle stringhe
    # usando l' IA: scrivere una funzione python che restituisca il MAC address
    # della scheda di rete wi-fi del mio pc
    for m, v, d in zip(mac_address, vendor, date):
        if m == mac[0:8]:
            print(f"Il produttore è {v}")
            print(f"La data è {d}")



if __name__=="__main__":
    main()
