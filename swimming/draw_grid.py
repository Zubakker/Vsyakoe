import pygame


def draw_grid(square_width, screen):
    sw = square_width

    for i in range(-1000, 1010, 1):
        pygame.draw.line(screen, (0, 0, 0), (i * sw * 10, 675), (1200 - i * sw * 10, 0))

    k = 400  # (338 * 1200)/(1200 - 338)

    for j in range(1, 3000//sw):
        d = (j * sw) / (j * sw + k)
        pygame.draw.line(screen, (0, 0, 0), (0, int(d * k)), (1200, int(d * k)))
        pygame.draw.line(screen, (0, 0, 0), (0, int(675 - d * k)), (1200, int(675 - d * k)))