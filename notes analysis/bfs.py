import pygame
pygame.font.init()
font = pygame.font.SysFont('Arial', 11)


def draw(lt, screen):
    for el in lt:
        pygame.draw.circle(screen, (200, 0, 0), el, 0)
        pygame.display.update()


def textwrite(pos, text, screen):
    pic = font.render(text, True, (0, 0, 0))
    screen.blit(pic, pos)
