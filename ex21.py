#Aidan Bauer 2/14/20
from tkinter import *
root = Tk()
screen = Canvas(root, width = 400, height = 300)
screen.pack()
bottom_diameter = 75
middle_diameter = 50
top_diameter = 25
canvas_height = 300
screen.create_oval(200,canvas_height/2,middle_diameter + 200,canvas_height/2 + middle_diameter)
screen.create_oval(200,canvas_height/2.5,top_diameter + 200,canvas_height/2.5 + top_diameter)
screen.create_oval(200,canvas_height/1.5,bottom_diameter + 200,canvas_height/1.5 + bottom_diameter)

mainloop()