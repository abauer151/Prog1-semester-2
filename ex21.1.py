#Aidan Bauer 2/17/20
from tkinter import *
root = Tk()
screen = Canvas(root, width = 400, height = 300)
screen.pack()
radius = 50
dist_between_lights = 20
def circle(x,y,color):#Creates circle with parameters
    screen.create_oval(x,y,x+radius,y+radius,fill=color)
screen.create_rectangle(200-dist_between_lights,50-dist_between_lights,250+dist_between_lights,240+dist_between_lights,fill="gray")
circle(200,50,"red")
circle(200,120,"yellow")
circle(200,190,"green")
mainloop()