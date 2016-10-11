import pygame
from pygame.locals import *

XPos = 640
YPos = 360
XDirection = 1
YDirection = 1
screen = pygame.display.set_mode((1280, 720))

running = True
while running:


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    execfile("SNEKKK.py")