import pygame


class Enemy:
    def __init__(self, display, coords):
        self.display = display
        self.y, self.x = coords
        self.hp = 100
        self.renderable = True

    def hurt(self):
        self.hp -= 30
        if self.hp <= 0:
            self.renderable = False
            self.x, self.y = 0, 0

    def render(self):
        if self.renderable:
            pygame.draw.rect(self.display, (30, 30, 100), (self.x*50+10, self.y*50+10, 30, 30))
            if self.hp < 100:
                pygame.draw.rect(self.display, (100, 0, 0), (self.x*50, self.y*50 + 45, 50, 10))
                pygame.draw.rect(self.display, (0, 200, 0), (self.x*50, self.y*50 + 45, self.hp // 2, 10))
