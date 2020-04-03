import pygame
import sys

from charts.Chart import Chart
from charts.ClassChart import ClassChart

FPS = 60
windowWidth = 900
windowHeight = 900
clock = pygame.time.Clock()

pygame.init()

canvas = pygame.display.set_mode((windowWidth, windowHeight))

chart = ClassChart(canvas, x=100, y=100, name="TEst")

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    canvas.fill((255, 255, 255))

    chart.draw()

    pygame.display.update()
    clock.tick(FPS)
