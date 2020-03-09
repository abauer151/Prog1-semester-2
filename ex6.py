# Aidan Bauer 1/31/20
from turtle import *
speed(0)
for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()
penup()
setposition(50,85)
pendown()
for i in range(2):
    circle(50)
    penup()
    forward(100)
    pendown()
penup()
setposition(100,170)
pendown()
circle(50)

turtle.getscreen()._root.mainloop()
