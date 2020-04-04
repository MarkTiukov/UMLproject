import pygame
import Colors


class Chart:
    def __init__(self,
                 parentSurface,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 x=0, y=0,
                 thickness=2,
                 backgroundColor=Colors.LIGHT_LIGHT_GREY):
        self.parentSurface = parentSurface
        self.width = width
        self.height = height
        self.boundColor = boundColor
        self.x = x
        self.y = y
        self.thickness = thickness
        self.backgroundColor = backgroundColor
        self.surface = pygame.Surface((self.width, self.height))

    def draw(self):
        # print("drawing:", self.width)
        self.surface.fill(self.backgroundColor)
        pygame.draw.rect(self.surface, self.boundColor,
                         (0, 0, self.width, self.height), self.thickness * 2)

    def blit(self):
        self.parentSurface.blit(self.surface, (self.x, self.y))
