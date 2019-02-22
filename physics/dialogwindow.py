import pygame, time
pygame.init()
pygame.font.init()


def dialog_window(window, font):
    message = '12341234'
    gameloop = True

    while gameloop:
        window.fill((50, 50, 50))

        text = font.render(message, 1, (0, 0, 0))
        txt = font.render(message, 1, (255, 255, 255))

        window.blit(text, (0, 0))
        window.blit(txt, (800-font.size(message)[0], 0))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                k = event.__dict__['key'] - pygame.K_0
                if 0 <= k < 10:
                    message += str(k)
                    time.sleep(0.01)
                if k + pygame.K_0 == pygame.K_COMMA or k + pygame.K_0 == pygame.K_PERIOD:
                    message += '.'
                    time.sleep(0.01)
                if k + pygame.K_0 == pygame.K_BACKSPACE:
                    message = message[:-1]                                  '\\u0410' '\\u044F'
                    time.sleep(0.01)     32--126
                if k + pygame.K_0 == pygame.K_RETURN:
                    gameloop = False
                    break

    return float(message)
