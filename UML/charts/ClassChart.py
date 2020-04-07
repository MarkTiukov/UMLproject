import tkinter as tk

import Colors
from charts.Chart import Chart


class ClassChart(Chart):
    def __init__(self,
                 canvas,
                 x=0, y=0,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 thickness=2,
                 backgroundColor=Colors.LIGHT_LIGHT_GREY,
                 name="Class"):
        super().__init__(canvas, x, y, width, height, boundColor, thickness, backgroundColor)
        self.name = tk.Text(self.frame, width=self.width, height=self.height, bg=backgroundColor)
        self.fields = tk.Text(self.frame, width=self.width, height=self.height)


    def draw(self):
        super(ClassChart, self).draw()
        pygame.draw.line(self.surface, self.boundColor, (0, self.nameSize),
                         (self.width, self.nameSize), self.thickness)
        pygame.draw.line(self.surface, self.boundColor, (0, self.nameSize + self.fieldSize),
                         (self.width, self.nameSize + self.fieldSize), self.thickness)
        # self.manager.update(60)
        # self.manager.draw_ui(self.surface)
        self.blit()
