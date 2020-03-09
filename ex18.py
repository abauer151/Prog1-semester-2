#Aidan Bauer 2/10/20
from turtle import *
length = 50
d = 2
while length < 400:
    pendown()
    forward(length)
    right(90)
    forward(length)    
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    penup()
    forward(-length/d)
    left(90)
    forward(length/d)
    right(90)
    length = length + 50
    d = d + 2