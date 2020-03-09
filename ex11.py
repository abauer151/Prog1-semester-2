#Aidan Bauer 2/5/20
from turtle import *
def Circle(radius):
    penup()
    left(90)
    forward(radius * -1)
    right(90)
    pendown()
    circle(radius)
    penup()
    setposition(0,0)
Circle(25)
Circle(50)
Circle(75)
Circle(100)

