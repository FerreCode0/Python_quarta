import turtle

file = open("disegno.txt", "r")
lines = file.readlines()
file.close()

lista = []
colori = {"rosso": "red", "blu": "blue", "verde": "green"}

for line, num in zip(lines, range(len(lines))):
    if num == len(lines) - 1:
        line = line.split(" ")
    else:
        line = line[0: -1].split(" ")
    lista.append(line)

for line in lista:
    numero = line[1:]
    comando = line[0]
    if comando == "avanti":
        turtle.forward(int(numero[0]))
    elif comando == "destra":
        turtle.right(int(numero[0]))
    elif comando == "cerchio":
        turtle.circle(int(numero[0]))
    elif comando == "colore":
        turtle.color(colori[numero[0]])
    elif comando == "salta":
        turtle.up()
        turtle.goto(int(numero[0]), int(numero[1]))
        turtle.down()

turtle.mainloop()