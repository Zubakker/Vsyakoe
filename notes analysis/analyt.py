import pygame
from PIL import Image
import sys
from time import sleep

from bfs import draw, textwrite


def bfs(y, x):
    global pix2
    que = [[y, x]]
    k = 0
    while k != len(que):
        y, x = que[k]
        pix2[y, x] = (255, 0, 0, 0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if pix2[y+i, x+j][0] != 255 and sum(pix2[y+i, x+j]) < 850 and [y+i, x+j] not in que:
                    que.append([y+i, x+j])
        k += 1
    return que


lines = []
lines2 = []

saves = open('notes.txt', 'a')
# PIL
pic = Image.open('notes2.png')
pixs = pic.load()
pix2 = pic.load()
x, y = pic.size
t = 0
h = 0
for b in range(y):
    if b+t < y and sum(pixs[50, b+t]) < 850 and len(lines) < 5:
        st = b+t
        while sum(pixs[50, b+t]) < 850:
            for a in range(x):
                pix2[a, b+t] = 255, 0, 0, 0
            t += 1
        if b+t-st <= 5:
            lines.append([st, b+t-st])
        if len(lines) == 5:
            break
    if b+h < y and sum(pixs[100, b+h]) < 850 and len(lines2) < 5:
        stp = b+h
        while sum(pixs[100, b+h]) < 850:
            for a in range(x):
                pix2[a, b+h] = 255, 0, 0, 0
            h += 1
        if b+h-stp <= 5:
            lines2.append([stp, b+h-stp])
        if len(lines2) == 5:
            break

# pygame
pygame.init()
screen = pygame.display.set_mode((1120, 630))
notes = pygame.image.load('/home/zubakker/Pictures/Screenshot from 2018-05-19 12-14-29.png')
screen.blit(notes, (0, 0))
if len(lines) < 5:
    lines = lines2
dist = lines[1][0] - lines[0][0] - lines[0][1]

for i in range(3):
    lines.insert(0, [lines[0][0] - dist - lines[0][1], lines[0][1]])

for i in range(2):
    lines.append([lines[-1][0] + lines[-1][1] + dist, lines[-1][1]])
for i, j in lines:
    for k in range(j):
        pygame.draw.line(screen, (200, 0, 0), (0, i+k), (x, i+k))

for a in range(x):
    for i in range(10):
        c, v = lines[i]
        v = c+v
        if sum(pixs[a, c - 2]) < 850 and pix2[a, c-1][0] != 255 and \
                sum(pixs[a, v+2]) < 850 and pix2[a, v+1][0] != 255:
            k = bfs(a, v + 2)
            if len(k) <= 2*dist:
                print(len(k))
                # draw(g, screen)
                break
            g = bfs(a, c - 1)
            if len(g) <= 2*dist:
                # draw(k, screen)
                break
            else:
                draw(k, screen)
                draw(g, screen)
                saves.write(str(i) + 'D|')
                textwrite((a, lines[-1][0] + 10), "на " + str(i), screen)
                break
        if sum(pixs[a, c - 2]) < 850 and pix2[a, c-2][0] != 255:
            k = bfs(a, c - 2)
            if len(k) < 30:
                break
            else:
                saves.write(str(i) + 'O|')
                textwrite((a, lines[0][0] - 20), "над " + str(i), screen)
                draw(k, screen)
                break

# pygame again

pygame.display.update()
sleep(5)