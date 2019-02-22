# -*- coding: utf-8 -*-

import time
import sys
from curses import *


from screen import Screen
from nake import Snake


def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    stdscr.refresh()
    L, C = stdscr.getmaxyx()
    curs_set(0)
    wind = newwin(L, C, 0, 0)
    # wind.border()

    display = Screen(wind)
    snake = Snake()

    display.change(snake)
    display.gen_apple()

    while not snake.gameover:
        stdscr.clear()
        # wind.addch(0, n, 'a')
        k = stdscr.getch()
        snake.move(k)

        display.change(snake)
        display.update()
        snake.run(display)

        stdscr.refresh()
        wind.refresh()
        time.sleep(0.05)


wrapper(main)
