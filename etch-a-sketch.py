import turtle
import tkinter as tk

def forward():
    t.forward(15)

def back():
    t.back(15)

def left():
    t.left(90)

def right():
    t.right(90)
root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()
t = turtle.RawTurtle(canvas)
t.pencolor("blue") 
t.penup()  
t.pendown() 

tk.Button(master = root, text = "Forward", command = forward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Back", command = back).pack(side = tk.LEFT)
tk.Button(master = root, text = "Left", command = left).pack(side = tk.LEFT)
tk.Button(master = root, text = "Right", command = right).pack(side = tk.LEFT)

root.mainloop()
