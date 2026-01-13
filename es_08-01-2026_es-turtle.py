import turtle
def sposta(x, y):
    turtle.penup()
    turtle.color("white")
    turtle.goto(x, y)
    turtle.pendown()

def poligoni(n, lung):
    angolo = 360 / n
    for _ in range(n):
        turtle.forward(lung)
        turtle.left(angolo)

def main():
    nPoligoni = 4
    lato = 90
    shift = 180
    x_0, y_0 = -300, -lato/2
    for i in range(nPoligoni):
        y = y_0
        x = x_0 + shift * i
        sposta(x, y)
        poligoni(i + 3, lato)

    turtle.mainloop()

if __name__ == "__main__":
    main()