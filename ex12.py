#Aidan Bauer 2/5/20
from turtle import *
outside_circle = input("Outside circle color?")
second_circle = input("Second circle color?")
third_circle = input("Third circle color")
center_circle = input("Center circle color?")
def Circle(radius,Color):
    penup()
    left(90)
    forward(radius * -1)
    right(90)
    pendown()
    color(Color)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    setposition(0,0)

Circle(100,outside_circle)
Circle(75,third_circle)
Circle(50,second_circle)
Circle(25,center_circle)


