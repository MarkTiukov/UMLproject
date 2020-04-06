import pygame
import pygame_gui as gui
import sys

import Colors
import pygame_textinput as Textfield

from charts.ClassChart import ClassChart
from charts.InterfaceChart import InterfaceChart

FPS = 120
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
interfaceCreationButton = gui.elements.UIButton(pygame.Rect((0, 100), (windowWidth // 5, 100)), "add Interface",
                                                manager)

running = True

creationMode = "none"

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not creationMode == "none":
                if creationMode == "class":
                    charts.append(ClassChart(windowSurface, manager, x=event.pos[0], y=event.pos[1]))
                elif creationMode == "interface":
                    charts.append(InterfaceChart(windowSurface, manager, x=event.pos[0], y=event.pos[1]))
                creationMode = "none"
        elif event.type == pygame.USEREVENT:
            if event.user_type == gui.UI_BUTTON_PRESSED:
                if event.ui_element == classCreationButton:
                    creationMode = "class"
                elif event.ui_element == interfaceCreationButton:
                    creationMode = "interface"
                else:
                    try:
                        if event.ui_element.object_ids[0].split("|")[0] == "smallchartbutton":
                            #TODO
                            # add action on click
                            print(event.ui_element.object_ids[0].split("|")[1], "     ", event.ui_element.relative_rect)
                    except Exception as e:
                        print("EXCEPTION!!!!", e)


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
