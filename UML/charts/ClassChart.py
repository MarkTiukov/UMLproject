import tkinter as tk

import Colors
from charts.Chart import Chart


class ClassChart(Chart):
    def __init__(self,
                 canvas: tk.Canvas,
                 charts: list,
                 arrows: list,
                 x=0, y=0,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 thickness=4,
                 backgroundColor=Colors.LIGHT_LIGHT_GREY,
                 name="Class"):
        super().__init__(canvas, charts, arrows, x, y, width, height,
                         boundColor,
                         thickness, backgroundColor)
        self.name = tk.Text(self.frame, width=self.width, height=1,
                            bg=self.backgroundColor, wrap=tk.WORD)
        self.name.insert(1.0, name)
        self.name.tag_configure("center", justify='center')
        self.name.tag_add("center", "1.0", "end")
        self.fields = tk.Text(self.frame, width=self.width, height=5,
                              bg=self.backgroundColor)
        self.methods = tk.Text(self.frame, width=self.width,
                               bg=self.backgroundColor)

    def draw(self):
        self.name.pack()
        self.fields.pack()
        self.methods.pack()
        self.frame.place(x=self.x, y=self.y, width=self.width,
                         height=self.height)
        super().draw()
