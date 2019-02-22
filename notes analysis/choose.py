import pygame
from time import sleep
pygame.init()


def choose_staff(screen, pic, font):
    tik = font.render('Выберите линию, на которой нет нот, только нотный стан', True, (0, 0, 0))
    pressed = False
    keys = pygame.key.get_pressed()
    while True:
        if keys[pygame.K_LEFT]:
            pressed = True
            print('hello')
        # else:
            # pressed = False
        screen.blit(pic, (0, 0))
        if pressed:
            x, y = pygame.mouse.get_pos()
            pygame.draw.line(screen, (15, 172, 224), (x, 0), (x, 630), 2)
        else:
            pygame.draw.rect(screen, (255, 140, 0), (0, 0, 1120, 30))
            pygame.draw.rect(screen, (255, 140, 0), (0, 0, 5, 630))
            pygame.draw.rect(screen, (255, 140, 0), (0, 625, 1120, 5))
            pygame.draw.rect(screen, (255, 140, 0), (1115, 0, 5, 630))
        screen.blit(tik, (5, 5))
        pygame.display.update()
        sleep(0.01)
