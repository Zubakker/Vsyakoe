# -*- coding: utf-8 -*-

import sys
import random
from curses import *
import time

# ◯ ⃝

class Screen:
    def __init__(self, wind):
        self.map = [[0]*40 for i in range(24)]
        self.apple = (-1, -1)
        self.window = wind

    def update(self):
        for i in range(24):
            for j in range(40):
                # if self.map[i][j] == 0:
                #     self.window.addch(i, j*2, ' ')
                if self.map[i][j] == 1:
                    self.window.addch(i, j*2, 'o')
                elif self.map[i][j] == 2:
                    self.window.addch(i, j*2, 'H')
                    self.window.addch(self.apple[0], self.apple[1]*2, 'G')

    def change(self, snake):
        self.map = [[0] * 40 for i in range(24)]
        points = snake.segs
        for i in range(len(points)-1):
            y, x = points[i]
            self.map[y][x] = 1
        y, x = points[-1]
        self.map[y][x] = 2

    def gen_apple(self):
        gens = []
        for i in range(24):
            for j in range(40):
                if self.map[i][j] == 0:
                    gens.append((i, j))

        self.apple = random.choice(gens)
        self.map[self.apple[0]][self.apple[1]] = 3
