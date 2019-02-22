import sys
from curses import *
import time


def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    stdscr.refresh()
    n = 0
    r = newwin(60, 60, 0, 0)
    while True:
        n += 1
        n %= 10**3
        sys.stdout.flush()
        stdscr.refresh()
        r.refresh()
        r.addch(0, n, 'a')
        stdscr.getch()
        stdscr.clear()
        time.sleep(0.2)


wrapper(main)
