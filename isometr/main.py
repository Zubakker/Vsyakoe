import pygame
import sys
import math

# Типы платформ: плоская, 1/2 наклонная, 1/4 вверх и 1/4 вниз

pygame.init()
screen = pygame.display.set_mode((1036, 711))
jm = pygame.image.load('romb.png')
forms = [pygame.image.load('flat.png'), pygame.image.load('half_up_l'), pygame.image.load('half_up_r')]
while True:
    screen.fill((255, 255, 255))

    h = 0
    g = [[16, -8], [16, 9], [-16, 8], [-16, -9]]
    a, b = -13, 325

    for c in [32]+[d for d in range(31, 0, -1) for e in range(2)]:
        for f in range(c):
            i, j = g[h]
            a += i
            b += j
            screen.blit(jm, (a, b-9))
        h += 1
        h %= 4

    pygame.display.update()
    pygame.time.wait(50)