import tkinter as tk

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

xToCreate = 100
yToCreate = 100


def popup(event):
    global xToCreate, yToCreate
    xToCreate = event.x
    yToCreate = event.y
    menu.post(event.x_root, event.y_root)


def createClass():
    global charts
    charts.append(ClassChart(canvas, x=xToCreate, y=yToCreate))
    charts[len(charts) - 1].draw()


def createInterface():
    global charts
    charts.append(InterfaceChart(canvas, x=xToCreate, y=yToCreate))
    charts[len(charts) - 1].draw()


menu = tk.Menu(tearoff=0)
menu.add_command(label="Class", command=createClass)
menu.add_command(label="Interface", command=createInterface)

canvas.bind("<Button-2>", popup)

createClass()

root.mainloop()
