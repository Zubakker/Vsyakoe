import pygame
import sys
import random


class Snake:
    def __init__(self, screen, font):
        self.segs = [(2, 2), (3, 2)]
        self.napr = (+1, 0)
        self.tim = 0
        self.screen = screen
        self.rendered = True
        self.apple = (-1, -1)
        self.font = font
        self.gameover = False
        self.field = [[3]*17]
        for i in range(15):
            self.field.append([3]+[0]*15+[3])
        self.field.append([3]*17)
        for el in self.segs:
            a, b = el
            self.field[a][b] = 1

    def move(self, dir):
        self.napr = dir
        self.rendered = False

    def render(self):
        self.tim += 1
        if self.tim == 4:
            self.rendered = True
            self.tim = 0
            a, b = self.segs[-1]
            i, j = self.napr
            a, b = a + i, b + j
            if self.field[a][b] != 0:
                self.gameover = True

            self.segs.append((a, b))
            if self.apple != (a, b):
                del self.segs[0]
            else:
                self.apple = (-1, -1)

            self.field = [[3] * 17]
            for i in range(15):
                self.field.append([3] + [0] * 15 + [3])
            self.field.append([3] * 17)
            for el in self.segs:
                a, b = el
                self.field[a][b] = 1

        pygame.draw.rect(self.screen, (0, 150, 0), (self.apple[0]*20-20, self.apple[1]*20-20, 20, 20))
        for el in self.segs:
            a, b = el
            pygame.draw.rect(self.screen, (150, 0, 0), (a * 20 - 20, b * 20 - 20, 20, 20))

    def gen(self):
        k = []
        for i in range(1, 16):
            for j in range(1, 16):
                if self.field[i][j] == 0:
                    k.append((i, j))
        self.apple = random.choice(k)