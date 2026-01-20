# in python tuto è un oggetto! anche int o float sonon oggetti!!
# Anche le funzioni sono oggetti

#Creare classi ci permette di creare nuovo oggetti
import math
import turtle
class Punto():
    # costruttori
    def __init__(self, x, y):# self e come this in java
        # Attributi (in python tutto e publico)
        self.x = x
        self.y = y
    def __str__(self):
        # Questo metodo deve ritornare una stringa 
        return f"{self.x}, {self.y}"
    def distanza_origine(self):
        # ritorno la distanza del punto dall'origine 0, 0
        return math.sqrt(self.x**2 + self.y**2)
    def scambia_coordinate(self):
        # questo metodo ritorna un nuovo punto con x e y scambiati
        return Punto(self.y, self.x)
    def disegna(self):
        # questo metodo usa Turtle per disegnare il punto
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y)
        t.dot(5) 
        turtle.pendown()
    def distanza(self, altro):
        # questo metodo restituisce la distanza tra il punto e altro
        # altro è una istanza di un altro punto
        return math.sqrt((self.x - altro.x)**2 + (self.y - altro.y)**2)

def main():
    a = Punto(1, 2) #Istanza di punto
    print(a)
    print(f"Il punto dista {a.distanza_origine()} dall'origine")
    print(f"la distanza tra i 2 punti e di {a.distanza(altro)}")

if __name__ == "__main__":
    main()