import pygame
import pygame_gui as gui
import sys

import Colors
import pygame_textinput as Textfield

from charts.ClassChart import ClassChart

FPS = 60
windowWidth = 1500
windowHeight = 1000
clock = pygame.time.Clock()

pygame.init()

windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
manager = gui.UIManager((windowWidth, windowHeight))
background = pygame.Surface((windowWidth, windowHeight))
background.fill(Colors.WHITE)

charts = list()

menu = gui.elements.UIPanel(pygame.Rect((0, 0), (windowWidth // 5, windowHeight)), 0, manager)
classCreationButton = gui.elements.UIButton(pygame.Rect((0, 0), (windowWidth // 5, 100)), "add Class", manager)
enteringCoordinates = gui.elements.UITextEntryLine(
    pygame.Rect((0, windowHeight - 100), (windowWidth // 5, windowHeight)), manager)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == classCreationButton:
                    charts.append(ClassChart(windowSurface, manager, x=200 + windowWidth // 5, y=100))

    manager.process_events(event)

    windowSurface.blit(background, (windowWidth // 5, 0))
    for chart in charts:
        # TODO
        # add try catch here
        chart.draw()

    manager.update(FPS)
    manager.draw_ui(windowSurface)
    pygame.display.update()
    clock.tick(FPS)
