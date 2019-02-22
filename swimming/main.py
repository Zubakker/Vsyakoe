import pygame
import time
import sys
import math


from draw_grid import draw_grid
from draw_obj import draw_obj
from enemy import Enemy
from wall import Wall

screen = pygame.display.set_mode((1200, 675))
enemys = [Enemy((10000, 100000), screen)]
start = 0
walls = [Wall((-100/2, 300/2), (-100/2, 400/2), 1, screen),
         Wall((-100/2, 400/2), (0, 400/2), 1, screen),
         Wall((0, 400/2), (0, 300/2), 1, screen),
         Wall((0, 300/2), (-100/2, 300/2), 1, screen)]

while True:
    now = time.clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    floor = pygame.draw.rect(screen, (30, 30, 80), (0, 338, 1200, 338))
    ceiling = pygame.draw.rect(screen, (60, 60, 100), (0, 0, 1200, 338))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        for wall in walls:
            wall.move(math.pi/(90/1), (0, 0))
        for enemy in enemys:
            enemy.move(math.pi/(90/1), (0, 0))
    if keys[pygame.K_LEFT]:
        for wall in walls:
            wall.move(-math.pi/(90/1), (0, 0))
        for enemy in enemys:
            enemy.move(-math.pi/(90/1), (0, 0))
    if keys[pygame.K_UP]:
        for wall in walls:
            wall.move(0, (0, 20))
        for enemy in enemys:
            enemy.move(0, (0, 20))
    if keys[pygame.K_DOWN]:
        for wall in walls:
            wall.move(0, (0, -20))
        for enemy in enemys:
            enemy.move(0, (0, -20))

    # draw_grid(100, screen)
    for enemy in enemys:
        enemy.render()
    for wall in walls:
        wall.render()

    pygame.display.update()
    time.sleep(0.1)
