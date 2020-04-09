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
        self.frame.bind("<Button-2>", func)
        self.smallButtons = [
            tk.Button(text="", width=1, height=1, bg=Colors.YELLOW, fg=Colors.BLACK, activebackground=Colors.PINK,
                      activeforeground=Colors.GREEN, command=func2),
            tk.Button(text="", width=1, height=1, command=func),
            tk.Button(text="", width=1, height=1, command=func),
            tk.Button(text="", width=1, height=1, command=func)]
        self.smallButtons[0].config(bg=Colors.PINK)

    def draw(self):
        self.canvas.create_rectangle(self.x - 1, self.y - 1, self.x + self.width + 1, self.y + self.height + 1,
                                     width=self.thickness, outline=self.boundColor)
        self.smallButtons[0].place(x=self.x + self.width // 2 - 5, y=self.y - 12, height=10, width=10)
        # self.smallButtons[1].place(x=self.x - 10, y=self.y - )
