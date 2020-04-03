import pygame

import Colors
from charts.Chart import Chart


class ClassChart(Chart):
    def __init__(self, canvas, sizeX=160, sizeY=200, color=Colors.BLACK, x=0, y=0, thickness=2, name="Class"):
        super().__init__(canvas, sizeX, sizeY, color, x, y, thickness)
        self.name = name
        self.nameSize = self.sizeY // 10
        self.fieldSize = (self.sizeY - self.nameSize) // 2

    def draw(self):
        super(ClassChart, self).draw()
        print("X == {}".format(self.sizeX))
        pygame.draw.line(self.canvas, self.color, (self.x, self.y + self.nameSize),
                         (self.x + self.sizeX, self.y + self.nameSize), self.thickness)
        pygame.draw.line(self.canvas, self.color, (self.x, self.y + self.nameSize + self.fieldSize),
                         (self.x + self.sizeX, self.y + self.nameSize + self.fieldSize), self.thickness)
