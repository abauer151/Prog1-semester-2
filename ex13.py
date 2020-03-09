#Aidan Bauer 2/5/20
from turtle import *
bottom = int(input("bottom snowball radius?"))
middle = int(input("middle snowball radius?"))
top = int(input("top snowball radius?"))
def snow_ball(radius):
    pendown()
    circle(radius)
    penup()
    left(90)
    forward(radius * 2)
    right(90)

snow_ball(bottom)
snow_ball(middle)
snow_ball(top)