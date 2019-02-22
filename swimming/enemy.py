import pygame
import math
from draw_obj import draw_obj


class Enemy:
    def __init__(self, coords, display):
        self.x, self.y = coords
        self.display = display
        self.alpha = math.atan2(self.y, self.x)
        self.dist = math.sqrt(self.x**2 + self.y**2)

    def move(self, angle, deltas):
        dx, dy = deltas
        self.alpha += angle
        self.x, self.y = math.cos(self.alpha)*self.dist, math.sin(self.alpha)*self.dist
        self.y -= dy
        self.x -= dx
        self.dist = math.sqrt(self.x**2 + self.y**2)
        self.alpha = math.atan2(self.y, self.x)

    def render(self):
        a, b, c = draw_obj(self.x, self.y, self.display)
        pygame.draw.circle(self.display, (200, 100, 0), (a, b), 5)#c)
