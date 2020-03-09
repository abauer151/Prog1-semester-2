#Aidan Bauer 2/17/20
from tkinter import *
root = Tk()
screen = Canvas(root, width = 400, height = 400)
screen.pack()
diameter = 40
canvas_height = 400
while diameter <= canvas_height:
    screen.create_oval(0,0,diameter,diameter)
    diameter = diameter + 20
mainloop()