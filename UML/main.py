import pygame
import pygame_gui as gui
import sys

import Colors
import pygame_textinput as Textfield

from charts.ClassChart import ClassChart

FPS = 60
windowWidth = 900
windowHeight = 900
clock = pygame.time.Clock()

pygame.init()

windowSurface = pygame.display.set_mode((windowWidth, windowHeight))
manager = gui.UIManager((windowWidth, windowHeight))
background = pygame.Surface((windowWidth, windowHeight))
background.fill(Colors.WHITE)

chart = ClassChart(windowSurface, manager, x=100, y=100, name="TEst")

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    manager.process_events(event)

    windowSurface.blit(background, (0, 0))
    chart.draw()

    manager.update(FPS)
    manager.draw_ui(windowSurface)
    pygame.display.update()
    clock.tick(FPS)
