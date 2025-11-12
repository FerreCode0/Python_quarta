#programma che somma i primi n numeri dispari

import math 

a = int(input("inserisci un numero ->"))
somma = 0

if a >= 0:
    for i in range(1, 2 * a + 1, 2):
        somma += i

radice_intera = math.isqrt(somma)
print(f"la somma è: {somma}, Quadrato perfetto: {radice_intera** 2 == somma}")
