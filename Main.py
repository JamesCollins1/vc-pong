import pygame
from pygame.locals import *

YPosPaddle = 10
XPosBall = 640
YPosBall = 360
XDirectionBall = 10
YDirectionBall = 10
Score = 0
screen = pygame.display.set_mode((1280, 720))

running = True
while running:


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    execfile("BallMovement.py")
    execfile("SNEKKK.py")

