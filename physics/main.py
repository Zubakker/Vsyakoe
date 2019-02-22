import pygame
import time
import sys

# from floor import Floor
from box import Box
from dialogwindow import dialog_window


pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.font.init()
font = pygame.font.SysFont('arial', 20)
pygame.key.get_pressed()


box = Box((400, 350), (1))
while True:
    now = time.clock()
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        dialog_window(screen, font)

    pygame.display.update()
    time.sleep(0.01)
