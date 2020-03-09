#Aidan Bauer 2/14/20
from tkinter import *
root = Tk()
screen = Canvas(root, width = 400, height = 300)
screen.pack()
screen.create_rectangle(0,0,400,100,fill = "black")
screen.create_rectangle(0,100,400,200,fill = "red")
screen.create_rectangle(0,200,400,300,fill = "yellow")

mainloop()