
#Aidan Bauer 2/5/20
from turtle import *
"""
This code will fill the canvas with light blue circles.

Now add a function that will draw a white highlight on each bubble.
"""
speed(0)
# This function will draw one row of 10 circles
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        penup()
        forward(40)

def highlight_row():
    for i in range(10):
        pendown()
        color("light blue","white")
        begin_fill()
        circle(10,90)
        end_fill()
        circle(10,270)
        penup()
        
        forward(40)



# This function will move Tracy from end of row up to beginning of the row on top        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
# Send Tracy to starting position in bottom left corner
penup()
setposition(-180,-200)

# Call circle drawing function 10 times to fill ten rows

for i in range(10):
    draw_circle_row()
    move_up_a_row()

penup()
setposition(-185,-200)

for i in range(10):
    highlight_row()
    move_up_a_row()
    