import sys
import tkinter as tk
from tkinter import messagebox as mb

from arrows.Line import Line
from charts.ClassChart import ClassChart
from charts.InterfaceChart import InterfaceChart

mouseRightButton = {"linux": "<Button-3>", "win32": "<Button-3>", "cygwin": "<Button-3>", "darwin": "<Button-2>"}[
    sys.platform]

windowWidth = 1500
windowHeight = 1000

root = tk.Tk()
root.geometry("{}x{}".format(windowWidth, windowHeight))
root.title("UML")

canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, bg='white')
canvas.place(x=0, y=0)

charts = list()
arrows = list()

arrowStart = None
arrowEnd = None

xToCreate = 100
yToCreate = 100

mb.showinfo("Небольшой туториал", "Нажми правой кнопкой там, где хочешь создать класс или интерфейс")


def drawArrow():
    arrows.append(Line(canvas, arrowStart, arrowEnd))
    arrows[-1:][0].draw()


def createArrow(coordinates):
    global arrowStart, arrowEnd
    global arrows
    if arrowStart is None:
        arrowStart = coordinates
    elif arrowEnd is None:
        arrowEnd = coordinates
        drawArrow()
        arrowStart = None
        arrowEnd = None


def popup(event):
    global xToCreate, yToCreate
    xToCreate = event.x
    yToCreate = event.y
    menu.post(event.x_root, event.y_root)


def createChart():
    charts[-1:][0].smallButtons[0]['command'] = lambda coor=charts[-1:][0].buttonCoordinates[0]: createArrow(coor)
    charts[-1:][0].smallButtons[1]['command'] = lambda coor=charts[-1:][0].buttonCoordinates[1]: createArrow(coor)
    charts[-1:][0].smallButtons[2]['command'] = lambda coor=charts[-1:][0].buttonCoordinates[2]: createArrow(coor)
    charts[-1:][0].smallButtons[3]['command'] = lambda coor=charts[-1:][0].buttonCoordinates[3]: createArrow(coor)
    charts[-1:][0].draw()


def createClass():
    global charts
    charts.append(ClassChart(canvas, x=xToCreate, y=yToCreate))
    createChart()


def createInterface():
    global charts
    charts.append(InterfaceChart(canvas, x=xToCreate, y=yToCreate))
    createChart()


menu = tk.Menu(tearoff=0)
menu.add_command(label="Class", command=createClass)
menu.add_command(label="Interface", command=createInterface)

canvas.bind(mouseRightButton, popup)

root.mainloop()
