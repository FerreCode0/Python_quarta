import uuid

def getMyMac():
    mac = uuid.getnode()
    mac_str = ":".join(f"{(mac>>i)&0xff:02x}" for i in range (40, -1, -8))
    return mac_str

def preparaMac(mac_str):
    mac_str = mac_str.replace("-", ":")
    return mac_str.upper()


def main():
    file = open("MAC.csv", "r", encoding = "utf-8")
    righe = file.readlines()[1:]        #righe è una lista di stringhe
    file.close()
    elencoMacVendor = {}
    elencoMacData = {}
    for riga in righe:      #riga è una stringa
        elem = riga.split(",")      #elem è una lista di stringhe
        elencoMacVendor[elem[0]] = elem[1]      #metto come chiave il mac address e come valore il vendor
        elencoMacData[elem[0]] = elem[-1]
    print(elencoMacVendor["20:2B:DA:1"])        #mi chiedo il vendor del seguente mac address
    print(elencoMacData["20:2B:DA:1"])
    myMac = getMyMac()
    myMacPreparato = preparaMac(myMac)
    primiTreByte = myMacPreparato[:8]
    if (primiTreByte in elencoMacVendor):
        print(f"il produttore del dispositivo con mac address {myMacPreparato} è {elencoMacVendor[primiTreByte]} e la sua data di inizio produzione è {elencoMacData[primiTreByte]}")       #quando ci mette un keyError ci mostra quello che abbiamo inserito
    else:
        print(f"il produttore del dispositivo con mac address {myMacPreparato} è ignoto")       #quando ci mette un keyError ci mostra quello che abbiamo inserito





if __name__ == "__main__":
    main()