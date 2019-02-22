import pygame
import math


from draw_obj import draw_obj


class Wall:
    def __init__(self, left_corn, right_corn, height, display):
        self.display = display
        self.d_one = left_corn
        self.d_two = right_corn
        self.height = height
        x, y = self.d_one
        x2, y2 = self.d_two
        self.alpha = math.atan2(y, x)
        self.alpha2 = math.atan2(y2, x2)
        self.dist = math.sqrt(x**2 + y**2)
        self.dist2 = math.sqrt(x2**2 + y2**2)

    def move(self, angle, deltas):
        dx, dy = deltas
        self.alpha += angle
        self.alpha2 += angle
        x, y = math.cos(self.alpha) * self.dist, math.sin(self.alpha) * self.dist
        x2, y2 = math.cos(self.alpha2) * self.dist2, math.sin(self.alpha2) * self.dist2
        y -= dy
        x -= dx
        x2 -= dx
        y2 -= dy
        self.dist = math.sqrt(x ** 2 + y ** 2)
        self.dist2 = math.sqrt(x2 ** 2 + y2 ** 2)
        self.alpha = math.atan2(y, x)
        self.alpha2 = math.atan2(y2, x2)
        self.d_one, self.d_two = (x, y), (x2, y2)

    def render(self):
        x, y = self.d_one
        x2, y2 = self.d_two
        a, b, c = draw_obj(x, y, self.display)
        d, e, f = draw_obj(x2, y2, self.display)
        c, f = c*self.height, f*self.height
        # pygame.draw.circle(self.display, (50, 50, 50), (a, b), 5)
        # pygame.draw.circle(self.display, (50, 50, 50), (d, e), 5)
        # pygame.draw.circle(self.display, (50, 50, 50), (d, e-f), 5)
        # pygame.draw.circle(self.display, (50, 50, 50), (a, b-c), 5)
        pygame.draw.polygon(self.display, (50, 50, 50), [(a, b), (d, e), (d, e-f), (a, b-c)])
        pygame.draw.line(self.display, (0, 0, 0), (a, b), (a, b-c))
        pygame.draw.line(self.display, (0, 0, 0), (d, e), (d, e-f))