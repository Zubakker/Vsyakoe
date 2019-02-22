import pygame
import random
from enemy import Enemy


def gen_level(start_pos, screen):
    start_pos = start_pos[0], start_pos[1]
    wall_count = 0
    level = [[-1]*14]
    for i in range(9):
        level.append([-1]+[0]*12+[-1])
    level.append([-1]*14)

    while wall_count < 20:
        x, y = random.randrange(12), random.randrange(9)
        if not level[y][x] and level[y][x] != start_pos:
            level[y][x] = -1
            wall_count += 1

    stack = [start_pos]
    start = 0
    while start != len(stack):
        ky, kx = stack[start]
        start += 1
        level[ky][kx] = 1
        if kx > 1 and not level[ky][kx - 1] and (ky, kx - 1) not in stack:
            stack.append((ky, kx - 1))
        if kx < 12 and not level[ky][kx + 1] and (ky, kx + 1) not in stack:
            stack.append((ky, kx + 1))
        if ky > 1 and not level[ky - 1][kx] and (ky - 1, kx) not in stack:
            stack.append((ky - 1, kx))
        if ky < 9 and not level[ky+1][kx] and (ky + 1, kx) not in stack:
            stack.append((ky + 1, kx))

    if len(stack) > 1:
        fin = random.choice(stack[1:])
    else:
        if start_pos[0] < 12:
            fin = start_pos[0]+1, start_pos[1]
        else:
            fin = start_pos[0]-1, start_pos[1]
    level[fin[0]][fin[1]] = 1
    level[start_pos[0]][start_pos[1]] = 1

    coors = []
    enemies = []
    num_enemies = 0
    while num_enemies < 2:
        x, y = random.choice(stack)
        if fin != (x, y) != start_pos and (x, y) not in coors:
            coors.append((x, y))
            enemies.append(Enemy(screen, (x, y)))
            num_enemies += 1
    print(stack)
    return level, fin, enemies
