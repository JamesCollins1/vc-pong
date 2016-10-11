import pygame, sys
from pygame.locals import *
Paddle = pygame.image.load("Paddle.png")
BlackPaddle = pygame.image.load("BlackPaddle.png")

screen.blit(BlackPaddle, (10, 0))


WindowWidth = 400
WindowHeight = 300
LineThickness = 10
PaddleSize = 50
PaddleOffset = 20
(x, YPosPaddle) = pygame.mouse.get_pos()
Black = (0, 0 , 0)
White = (255, 255, 255)
screen.blit(Paddle,(10,YPosPaddle))
def drawpaddle(paddle):
    if paddle.bottom > WindowHeight - LineThickness:
        paddle.bottom = WindowHeight - LineThickness
    elif paddle.top < LineThickness:
        paddle.top = LineThickness

    pygame.draw.rect(DISPLAYSURF, White, paddle)

pygame.display.update()
pygame.display.flip()

