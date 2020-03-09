#Aidan BAuer 1/31/20
from turtle import *
def bracelet():
    for i in range (100):
        penup()
        forward(100)
        pendown()
        circle(10)
        penup()
        forward(-100)
        left(10)

bracelet()

turtle.getscreen()._root.mainloop()    
