from turtle import *
penup()
forward(-400)
pendown()
color('green','green')
begin_fill()
while True:
    circle(20)
    penup()
    forward(40)
    pendown()
    if abs(pos()) < 1:
        break
end_fill()
done()