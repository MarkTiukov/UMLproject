import tkinter as tk

import Colors


def func():
    print("test")


def func2():
    print("test2")


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
        self.smallButtons = [
            tk.Button(text="", width=1, height=1, bg=Colors.PINK, fg=Colors.BLACK, activebackground=Colors.YELLOW,
                      activeforeground=Colors.GREEN),
            tk.Button(text="", width=1, height=1, bg=Colors.PINK, fg=Colors.BLACK, activebackground=Colors.YELLOW,
                      activeforeground=Colors.GREEN),
            tk.Button(text="", width=1, height=1, bg=Colors.PINK, fg=Colors.BLACK, activebackground=Colors.YELLOW,
                      activeforeground=Colors.GREEN),
            tk.Button(text="", width=1, height=1, bg=Colors.PINK, fg=Colors.BLACK, activebackground=Colors.YELLOW,
                      activeforeground=Colors.GREEN)]
        self.buttonCoordinates = [(self.x + self.width // 2 - 5, self.y - 12),
                                  (self.x + self.width + 2, self.y + self.height // 2 - 5),
                                  (self.x + self.width // 2 - 5, self.y + self.height + 2),
                                  (self.x - 12, self.y + self.height // 2 - 5)]

    def draw(self):
        self.canvas.create_rectangle(self.x - 1, self.y - 1, self.x + self.width + 1, self.y + self.height + 1,
                                     width=self.thickness, outline=self.boundColor)
        self.smallButtons[0].place(x=self.buttonCoordinates[0][0], y=self.buttonCoordinates[0][1], height=10, width=10)
        self.smallButtons[1].place(x=self.buttonCoordinates[1][0], y=self.buttonCoordinates[1][1], width=10, height=10)
        self.smallButtons[2].place(x=self.buttonCoordinates[2][0], y=self.buttonCoordinates[2][1], height=10, width=10)
        self.smallButtons[3].place(x=self.buttonCoordinates[3][0], y=self.buttonCoordinates[3][1], width=10, height=10)
