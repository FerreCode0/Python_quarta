# Dato un'indirizzo ip in input riscriverlo in binario

ip = input("inserisci un indirizzo ip ->")

numeri = ip.split(".")

binario = ""
for numero in numeri:
    nBinario = bin(int(numero))
    nBinario = nBinario[2:]
    lunghezza = len(nBinario)
    if lunghezza != 8:
        nBinario = "0" * (8 - lunghezza) + nBinario

    binario = binario + nBinario + "."

print(binario[:-1])