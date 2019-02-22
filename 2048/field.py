import pygame
import random
import time
import sys


class Field:
    def __init__(self, screen, font):
        self.pol = [[-1, -1,  -1,  -1,  -1,  -1],
                    [-1,  0,   0,   0,   0,  -1],
                    [-1,  0,   0,   0,   0,  -1],
                    [-1,  0,   0,   0,   0,  -1],
                    [-1,  0,   0,   0,   0,  -1],
                    [-1, -1,  -1,  -1,  -1,  -1]]
        self.screen = screen
        self.font = font
        self.score = 0

    def gen(self):
        pos = []
        job = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        for i in range(1, 5):
            for j in range(1, 5):
                if self.pol[i][j] == 0:
                    pos.append([i, j])
        if pos:
            a, b = random.choice(pos)
            t = random.choice(job)
            self.pol[a][b] = t
        else:
            self.screen.fill((0, 200, 0))
            txt = self.font.render("GAME OVER", True, (0, 0, 0))
            self.screen.blit(txt, (200 - txt.get_width() // 2, 200 - txt.get_height() // 2))
            pygame.display.update()
            time.sleep(1)
            pygame.font.quit()
            pygame.quit()
            sys.exit()

    def __abs__(self):
        for i in range(1, 5):
            for j in range(1, 5):
                self.pol[i][j] = abs(self.pol[i][j])

    def mover(self, i, j):
        for b in range(1, 6-j):
            if self.pol[i][j+b] != 0:
                t = self.pol[i][j]
                if self.pol[i][j+b] == self.pol[i][j]:
                    self.pol[i][j] = 0
                    self.pol[i][j+b] += 1
                    self.score += 2**self.pol[i][j+b]
                    self.pol[i][j+b] *= -1
                else:
                    self.pol[i][j] = 0
                    self.pol[i][j+b-1] = t
                break

    def movel(self, i, j):
        for b in range(1, j+1):
            if self.pol[i][j-b] != 0:
                t = self.pol[i][j]
                if self.pol[i][j-b] == self.pol[i][j]:
                    self.pol[i][j] = 0
                    self.pol[i][j-b] += 1
                    self.score += 2 ** self.pol[i][j-b]
                    self.pol[i][j-b] *= -1
                else:
                    self.pol[i][j] = 0
                    self.pol[i][j-b+1] = t
                break

    def moved(self, i, j):
        for b in range(1, 6-i):
            if self.pol[i+b][j] != 0:
                t = self.pol[i][j]
                if self.pol[i+b][j] == self.pol[i][j]:
                    self.pol[i][j] = 0
                    self.pol[i+b][j] += 1
                    self.score += 2 ** self.pol[i+b][j]
                    self.pol[i+b][j] *= -1
                else:
                    self.pol[i][j] = 0
                    self.pol[i+b-1][j] = t
                break

    def moveu(self, i, j):
        for b in range(1, i+1):
            if self.pol[i-b][j] != 0:
                t = self.pol[i][j]
                if self.pol[i-b][j] == self.pol[i][j]:
                    self.pol[i][j] = 0
                    self.pol[i-b][j] += 1
                    self.score += 2 ** self.pol[i-b][j]
                    self.pol[i-b][j] *= -1
                else:
                    self.pol[i][j] = 0
                    self.pol[i-b+1][j] = t
                break

    def render(self):
        for i in range(4):
            for j in range(4):
                t = self.pol[i+1][j+1]
                pygame.draw.rect(self.screen, ((t*64)%256, (t*48)%256, (t*32)%256), [j*100, i*100, 100, 100])
                text = self.font.render(str(2**t), True, (0, 0, 0))
                self.screen.blit(text, (j*100 + 50 - text.get_width() // 2, i*100 + 50 - text.get_height() // 2))
        tst = self.font.render(str(self.score), True, (200, 200, 200))
        self.screen.blit(tst, (200 - tst.get_width() // 2, 410 - tst.get_height() // 2))
