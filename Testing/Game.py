import pygame
import time
import sys

from player import Player
from draw_floor import draw_floor
from gen_level import gen_level
from enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((700, 550))
player = Player((50, 50), screen)
start = 0
nif = 1, 1
level, fin, enemies = gen_level((1, 1), screen)

while True:
    now = time.clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or player.hp <= 0:
            pygame.quit()
            sys.exit()
    heal = False
    ly, lx = player.y, player.x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and now - start > 0.15 and level[player.y//50][player.x//50+1] != -1:
        start = now
        heal = True
        player.move((50, 0))
    if keys[pygame.K_LEFT] and now - start > 0.15 and level[player.y//50][player.x//50-1] != -1:
        start = now
        heal = True
        player.move((-50, 0))
    if keys[pygame.K_UP] and now - start > 0.15 and level[player.y//50-1][player.x//50] != -1:
        start = now
        heal = True
        player.move((0, -50))
    if keys[pygame.K_DOWN] and now - start > 0.15 and level[player.y//50+1][player.x//50] != -1:
        start = now
        heal = True
        player.move((0, 50))
    if keys[pygame.K_u] and now - start > 0.15:
        start = now
        heal = True

    screen.fill((0, 0, 0))
    draw_floor(screen, level, nif, fin)
    for enemy in enemies:
        if enemy.x*50 == player.x and enemy.y*50 == player.y:
            enemy.hurt()
            player.hurt()
            player.move((lx-player.x, ly-player.y))
        enemy.render()
    if heal:
        player.heal()
    if (player.y//50, player.x//50) == fin and keys[pygame.K_SPACE]:
        nif = fin
        level, fin, enemies = gen_level(nif, screen)
    player.render()
    pygame.display.update()
    time.sleep(0.016)
