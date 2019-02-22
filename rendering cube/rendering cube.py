import pygame
import time
import sys
from math import atan2, sin, cos, pi


def project(t, o, s):  # t -- искомая точка o наблюдатель s экран, на который проекцируем
    a = (abs(t['x'] - s['x'])/abs(t['x'] - o['x']))
    b = (abs(s['x'] - o['x'])/abs(t['x'] - o['x']))
    x = 400 + abs(t['y'] - o['y'])*b*(t['y']/abs(t['y']))
    y = 350 - abs(t['z'] - o['z'])*b*(t['z']/abs(t['z']))
    return int(x), int(y)


def rotate(x, y, z):  # x, y, z -- это углы в **радианах** на которые будет поворачиваться куб по соответсв осям
    global dots, twod
    newdots = []
    twod = []
    for dot in dots:
        for a, b, c, e in [['x', 'y', 'z', z], ['y', 'z', 'x', x], ['z', 'x', 'y', y]]:
            d = (dot[a]**2 + dot[b]**2)**0.5
            alpha = atan2(dot[b], dot[a]) + e
            y1, x1 = sin(alpha)*d, cos(alpha)*d
            dot = {a: x1, b: y1, c: dot[c]}
        newdots.append(dot)

        twod.append(project(dot, {'x': 800, 'y': 0, 'z': 00}, {'x': 400}))
    dots = newdots


pygame.init()
# Расстояние наблюдателя от центра куба (точки 0, 0, 0): (0, 4, 4) с 1 == сторона куба, а экран находится посередине (0, 2, 0-4)
screen = pygame.display.set_mode((800, 700))
dots = [{'x':  200, 'y': -200, 'z':  200}, {'x': -200, 'y': -200, 'z':  200},
        {'x': -200, 'y':  200, 'z':  200}, {'x':  200, 'y':  200, 'z':  200},
        {'x':  200, 'y':  200, 'z': -200}, {'x': -200, 'y':  200, 'z': -200},
        {'x': -200, 'y': -200, 'z': -200}, {'x':  200, 'y': -200, 'z': -200},]
twod = [project(dot, {'x': 800, 'y': 0, 'z': 00}, {'x': 400})for dot in dots]

screen.fill((255, 255, 255))
while True:
    screen.fill((255, 255, 255))
    # rotate(pi/180/2, 0, 0)

    for i in range(7):
        pygame.draw.circle(screen, (0, 0, 0), twod[i], 3)
        pygame.draw.line(screen, (0, 0, 0), twod[i], twod[i+1])
    pygame.draw.circle(screen, (0, 0, 0), twod[7], 3)
    pygame.draw.line(screen, (0, 0, 0), twod[1], twod[6])
    pygame.draw.line(screen, (0, 0, 0), twod[2], twod[5])
    pygame.draw.line(screen, (0, 0, 0), twod[0], twod[3])
    pygame.draw.line(screen, (0, 0, 0), twod[4], twod[7])

    keys = pygame.key.get_pressed()
    if any(keys):
        print('hello')
    if keys[pygame.K_w]:
        print('hello')
        rotate(0, -pi/90, 0)
    if keys[pygame.K_s]:
        rotate(0, pi/90, 0)
    if keys[pygame.K_a]:
        rotate(0, 0, pi/90)
    pygame.display.update()
    time.sleep(0.01)