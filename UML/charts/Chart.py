import tkinter as tk

import Colors


class Chart:
    def __init__(self,
                 canvas,
                 x=0, y=0,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 thickness=4,
                 backgroundColor=Colors.LIGHT_LIGHT_GREY):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.boundColor = boundColor
        self.x = x
        self.y = y
        self.thickness = thickness
        self.backgroundColor = backgroundColor
        self.frame = tk.Frame(width=self.width, height=self.height, bg=self.backgroundColor)

    def draw(self):
        self.canvas.create_rectangle(self.x - 1, self.y - 1, self.x + self.width + 1, self.y + self.height + 1,
                                     width=self.thickness, outline=self.boundColor)
