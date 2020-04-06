import pygame
import pygame_gui as gui
import Colors


class Chart:
    def __init__(self,
                 parentSurface,
                 manager,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 x=0, y=0,
                 thickness=2,
                 backgroundColor=Colors.LIGHT_LIGHT_GREY):
        self.parentSurface = parentSurface
        self.manager = manager
        self.width = width
        self.height = height
        self.boundColor = boundColor
        self.x = x
        self.y = y
        self.thickness = thickness
        self.backgroundColor = backgroundColor
        self.surface = pygame.Surface((self.width, self.height))
        self.circles = list()
        self.createDefaultCircles()

    def createDefaultCircles(self):
        self.circles.append(
            gui.elements.UIButton(pygame.Rect((self.x + self.width // 2 - 5, self.y - 10), (10, 10)), "", self.manager))
        self.circles.append(
            gui.elements.UIButton(pygame.Rect((self.x + self.width, self.y + self.height // 2 - 5), (10, 10)), "", self.manager))
        self.circles.append(
            gui.elements.UIButton(pygame.Rect((self.x + self.width // 2 - 5, self.y + self.height), (10, 10)), "",
                                  self.manager))
        self.circles.append(
            gui.elements.UIButton(pygame.Rect((self.x - 10, self.y + self.height // 2 - 5), (10, 10)), "", self.manager))

    def draw(self):
        # print("drawing:", self.width)
        self.surface.fill(self.backgroundColor)
        pygame.draw.rect(self.surface, self.boundColor,
                         (0, 0, self.width, self.height), self.thickness * 2)

    def blit(self):
        self.parentSurface.blit(self.surface, (self.x, self.y))
