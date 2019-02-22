import pygame
import math


def draw_obj(distance_x, distance_y, screen):
    alpha = math.atan2(distance_x * 10, 338)
    k = 400
    t = (k*distance_y)/(distance_y+k)
    if t > 338:
        t = 338
    ans = math.tan(alpha)*t - 600

    dist = math.sqrt(distance_x**2 + distance_y**2)
    b = (k*dist)/(dist+k)
    beta = math.atan2(800, 338)
    ans2 = math.tan(beta) * (338 - b)

    return int(distance_x * 10 - ans), int(675 - t), int(ans2)
