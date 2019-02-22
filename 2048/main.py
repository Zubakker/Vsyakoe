import pygame
import time
import sys

from field import Field


pygame.init()
screen = pygame.display.set_mode((400, 420))
pygame.font.init()
font = pygame.font.SysFont("arial", 16)
field = Field(screen, font)
start = 0
field.gen()
while True:
    screen.fill((0, 0, 0))
    act = False
    now = time.clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    reserv = []
    for el in field.pol:
        reserv.append(el.copy())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and now - start >= 0.005:
        start = now
        for i in range(1, 5):
            for j in range(4, 0, -1):
                field.mover(i, j)
        abs(field)
        if field.pol != reserv:
            field.gen()
    if keys[pygame.K_LEFT] and now - start >= 0.005:
        start = now
        for i in range(1, 5):
            for j in range(1, 5):
                field.movel(i, j)
        abs(field)
        if field.pol != reserv:
            field.gen()
    if keys[pygame.K_DOWN] and now - start >= 0.005:
        start = now
        for j in range(1, 5):
            for i in range(4, 0, -1):
                field.moved(i, j)
        abs(field)
        if field.pol != reserv:
            field.gen()
    if keys[pygame.K_UP] and now - start >= 0.005:
        start = now
        for i in range(1, 5):
            for j in range(1, 5):
                field.moveu(i, j)
        abs(field)
        if field.pol != reserv:
            field.gen()
    field.render()

    pygame.display.update()
    time.sleep(0.1)