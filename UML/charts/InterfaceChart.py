import tkinter as tk

import Colors
from charts.Chart import Chart


class InterfaceChart(Chart):
    def __init__(self,
                 canvas: tk.Canvas,
                 arrows: list,
                 x=0, y=0,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 thickness=2,
                 backgroundColor=Colors.LIGHT_LIGHT_GREY,
                 name="Interface"):
        super().__init__(canvas, arrows, x, y, width, height, boundColor,
                         thickness,
                         backgroundColor)
        self.name = tk.Text(self.frame, width=self.width, height=2,
                            bg=self.backgroundColor, wrap=tk.WORD)
        self.name.insert(1.0, "<<Interface>>\n", "center")
        self.name.insert(tk.END, name, "center")
        self.name.tag_configure("center", justify='center')
        self.name.tag_add("center", "1.0", "end")
        self.methods = tk.Text(self.frame, width=self.width,
                               bg=self.backgroundColor)

    def draw(self):
        super().draw()
        self.name.pack()
        self.methods.pack()
        self.frame.place(x=self.x, y=self.y, width=self.width,
                         height=self.height)
