import pygame
from time import sleep
import sys
from PIL import Image
import tkinter
from tkinter import filedialog


from choose import choose_staff

root = tkinter.Tk()
root.withdraw()

saves = open('information.txt', 'r')
last_path = '/'.join(saves.read().split('/')[:-1])+'/'
saves.close()


# master = tkinter.Tk()
# canvas = tkinter.Canvas(master, bg='blue', height=600, widthscreen.blit(pic, (0, 0))=600)saves.read().split('/')[:-1]
# oval = canvas.create_oval((300, 300), (310, 310), fill='green')saves.read().split('/')[:-1]
# ova = canvas.create_oval((400, 400), (450, 450), fill='yellow')
# label = tkinter.Label(master, text="press Up/Down/Left/Right to move, space to restart, other to freeze enemies")
# label.pack()
# canvas.pack()
# master.bind("<KeyPress>", key_pressed)
# master.mainloop()

file_path = filedialog.askopenfilename(initialdir=last_path)
saves = open('information.txt', 'w')
saves.write(file_path)
saves.close()

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1120, 630))
pic = pygame.image.load(file_path)
screen.blit(pic, (0, 0))
font = pygame.font.SysFont('Arial', 20)
        
pygame.display.update()
while True:
    keys = pygame.key.get_pressed()
    print(keys)
    if keys[pygame.K_SPACE]:
        print('hello')
    pygame.display.update()

choose_staff(screen, pic, font)