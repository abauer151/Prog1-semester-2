#Aidan Bauer 2/5/20
from turtle import *
def smiley_face():
    circle(100)
    penup()
    forward(50)
    left(90)
    forward(125)
    pendown()
    circle(25)
    penup()
    setposition(0,0)
    left(90)
    forward(25)
    right(90)
    forward(125)
    pendown()
    circle(25)
    penup()
    setposition(-50,75)
    right(115)
    pendown()
    circle(100,80) 
happy = input("How are you feeling?")
if happy == "happy":
    smiley_face()

    
        
