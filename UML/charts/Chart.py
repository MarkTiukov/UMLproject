import tkinter as tk

import Colors


def func():
    print("test")


def func2():
    print("test2")


class Chart:

    def __init__(self,
                 canvas: tk.Canvas,
                 arrows: list,
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
        self.frame = tk.Frame(width=self.width, height=self.height,
                              bg=self.backgroundColor)
        self.smallButtons = [
            tk.Button(text="", width=1, height=1, bg=Colors.PINK,
                      fg=Colors.BLACK, activebackground=Colors.YELLOW,
                      activeforeground=Colors.GREEN) for i in range(4)]
        self.buttonCoordinates = [(self.x + self.width // 2 - 5, self.y - 12),
                                  (self.x + self.width + 2,
                                   self.y + self.height // 2 - 5),
                                  (self.x + self.width // 2 - 5,
                                   self.y + self.height + 2),
                                  (self.x - 12, self.y + self.height // 2 - 5)]
        self.deleteButton = tk.Button(text="x", width=1, height=1,
                                      bg=Colors.RED, command=self.destroy)

    def draw(self):
        self.border = self.canvas.create_rectangle(self.x - 1, self.y - 1,
                                                   self.x + self.width + 1,
                                                   self.y + self.height + 1,
                                                   width=self.thickness,
                                                   outline=self.boundColor)
        for i in range(len(self.smallButtons)):
            self.smallButtons[i].place(x=self.buttonCoordinates[i][0],
                                       y=self.buttonCoordinates[i][1],
                                       height=10,
                                       width=10)
        self.deleteButton.place(x=self.x - 10, y=self.y)

    def destroy(self):
        for button in self.smallButtons:
            button.destroy()
        self.deleteButton.destroy()
        self.canvas.delete(self.border)
        self.frame.destroy()
