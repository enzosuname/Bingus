import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants


# Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60

# def for similar attributes


#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()
# game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    # screen.fill()

    g.display.flip()
    clock.tick(FPS)