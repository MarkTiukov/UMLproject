import tkinter as tk
import sys


import Colors

from charts.ClassChart import ClassChart
from charts.InterfaceChart import InterfaceChart

windowWidth = 1500
windowHeight = 1000

root = tk.Tk()
root.geometry("{}x{}".format(windowWidth, windowHeight))
root.title("UML")

canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, bg='white')
canvas.place(x=0, y=0)



charts = list()
arrows = list()

menu = tk.Menu(tearoff=0)
#TODO
# createClass()
# createInterface()

root.mainloop()

