from turtle import *
penup()
forward(-200)
left(90)
forward(300)
right(90)
for i in range(5):
    forward(100)
    pendown()
    right(90)
    forward(400)
    penup()
    left(180)
    forward(400)
    right(90)
turtle.getscreen()._root.mainloop()   


