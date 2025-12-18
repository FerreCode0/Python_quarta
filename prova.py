import turtle

file = open("disegno.txt", "r", encoding="utf-8")
righe = file.readlines()
file.close()

turtle.width(50)

tutorial = []
for riga, n in zip(righe, range(len(righe))):
    if n == len(righe) - 1:
        riga = riga.split(" ")
    else:
        riga = riga[0:-1].split(" ")
    tutorial.append(riga)

colori = {"rosso": "red", "blu": "blue", "verde": "green"}

for riga in tutorial:
    comando = riga[0]
    resto = riga[1:]
    if comando == "avanti":
        turtle.forward(int(resto[0]))
    elif comando == "destra":
        turtle.right(int(resto[0]))
    elif comando == "dietro":
        turtle.backward(int(resto[0]))
    elif comando == "sinistra":
        turtle.left(int(resto[0]))
    elif comando == "salta":
        turtle.up()
        turtle.setx(int(resto[0]))
        turtle.sety(int(resto[1]))
        turtle.down()
    elif comando == "cerchio":
        turtle.circle(int(resto[0]))
    elif comando == "colore":
        turtle.color(colori[resto[0]])
    elif comando == "sfondo":
        screen = turtle.Screen()
        screen.bgcolor(colori[resto[0]])
    elif comando == "cerchioPieno":
        t = turtle.Turtle()
        r = 200  # raggio
        t.penup()
        t.goto(0, -r)  # punto in basso del cerchio
        t.pendown()
        t.color("white", "white")
        t.begin_fill()
        t.circle(r)
        t.end_fill()


turtle.mainloop()