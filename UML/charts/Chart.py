import tkinter as tk
import Colors


class Chart:
    def __init__(self,
                 canvas,
                 x=0, y=0,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 thickness=2,
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


