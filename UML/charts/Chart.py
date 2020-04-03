import pygame
import Colors


class Chart:
    value = 0

    def __init__(self, canvas, sizeX=160, sizeY=200, color=Colors.BLACK, x=0, y=0, thickness=2):
        self.canvas = canvas
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.color = color
        self.x = x
        self.y = y
        self.thickness = thickness

    def draw(self):
        print("drawing:", self.sizeX)
        pygame.draw.rect(self.canvas, self.color,
                         (self.x, self.y, self.sizeX, self.sizeY), self.thickness)
