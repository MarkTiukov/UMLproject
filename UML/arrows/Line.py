import tkinter as tk

import Colors


class Line:
    def __init__(self, canvas: tk.Canvas,
                 start: (int, int),
                 end: (int, int),
                 name: str,
                 color=Colors.BLACK,
                 thickness=2):
        self.canvas = canvas
        self.start = start
        self.end = end
        self.name = name
        self.color = color
        self.thickness = thickness
        self.points = [start, end]
        self.canvasObject = 0

    def setStart(self, coordinates):
        if len(self.points) == 0:
            self.points.append(coordinates)
        else:
            self.points[0] = coordinates

    def setEnd(self, coordinates):
        if len(self.points) == 1:
            self.points.append(coordinates)
        else:
            self.points[len(self.points - 1)] = coordinates

    def draw(self):
        if len(self.points) == 2:
            self.canvasObject = self.canvas.create_line(*self.start, *self.end,
                                                        fill=self.color,
                                                        width=self.thickness,
                                                        arrow=tk.LAST,
                                                        arrowshape="10 20 10")

    def getName(self):
        return self.name

    def getObject(self):
        return self.canvasObject
