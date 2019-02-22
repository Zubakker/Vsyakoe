# -*- coding: utf-8 -*-

# from pynput import keyboard
from time import sleep

# keyboard2 = keyboard.Controller()


class Snake:
    def __init__(self):
        self.segs = [(1, 1), (1, 2)]
        self.direction = (1, 0)
        self.count = 0
        self.gameover = False

    def move(self, key):
        if key == 261 and self.direction != (-1, 0):
            self.direction = (1, 0)
        elif key == 260 and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == 259 and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == 258 and self.direction != (0, -1):
            self.direction = (0, 1)
        return False

    def nothing(self, key):
        return False

    def run(self, screen):
        self.count += 1
        if self.count == 8:
            self.count = 0

            a, b = self.segs[-1]
            j, i = self.direction
            a, b = a+i, b+j
            self.segs.append((a, b))

            if screen.map[a][b] != 0 and screen.map[a][b] != 9:
                self.gameover = True

            if (a, b) != screen.apple:
                del self.segs[0]
            else:
                screen.change(self)
                screen.gen_apple()
