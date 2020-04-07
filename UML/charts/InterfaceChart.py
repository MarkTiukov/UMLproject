import pygame
import pygame_gui as gui

import Colors
from charts.Chart import Chart


class InterfaceChart(Chart):
    def __init__(self,
                 parentSurface,
                 manager,
                 width=160,
                 height=200,
                 boundColor=Colors.BLACK,
                 x=0, y=0, thickness=2,
                 name="Interface",
                 backgroundColor=Colors.LIGHT_LIGHT_GREY, ):
        super().__init__(parentSurface, manager, width, height, boundColor, x, y, thickness)
        # self.manager = gui.UIManager((self.width, self.height))
        # self.name = gui.elements.UITextEntryLine(pygame.Rect((0, 0), (self.width, self.height)), self.manager)
        self.name = gui.elements.UITextEntryLine(pygame.Rect((self.x, self.y), (self.width, self.height)), manager)
        self.nameSize = self.height // 10
        self.name.set_text(name)

    def draw(self):
        super(InterfaceChart, self).draw()
        pygame.draw.line(self.surface, self.boundColor, (0, self.nameSize),
                         (self.width, self.nameSize), self.thickness)
        # self.manager.update(60)
        # self.manager.draw_ui(self.surface)
        self.blit()