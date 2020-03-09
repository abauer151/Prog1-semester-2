#Aidan Bauer 2/5/20
from turtle import *
for i in range(5):
    penup()
    left(90)
    forward(i * -25)
    right(90)
    pendown()
    circle(i * 25)
    penup()
    setposition(0,0)

