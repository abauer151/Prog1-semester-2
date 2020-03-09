#Aidan Bauer 2/10/20
from turtle import *
from tkinter import *

root = Tk()
screen = Canvas(root, width=200, height=200, background="red")
screen.pack()
screen.create_line(125,25,125,325)
screen.create_line(75,25,75,325)
screen.create_line(25,125,325,125)
screen.create_line(25,75,325,75)




mainloop()

