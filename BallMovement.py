import pygame
SnekBall = pygame.image.load('SnekBall.png')
BlackBox = pygame.image.load('black.png')
screen.blit(BlackBox, (XPosBall, YPosBall))

XPosBall = XPosBall + XDirectionBall
YPosBall = YPosBall + YDirectionBall

if XPosBall == 1230:
    XDirectionBall = -10
if YPosBall == 670:
    YDirectionBall = -10
#if XPosBall == 0:
#    XDirectionBall = 1
if YPosBall == 0:
    YDirectionBall = 10
screen.blit(SnekBall, (XPosBall, YPosBall))
pygame.display.update()
pygame.display.flip()

execfile("Collision.py")



## if 'Ball Collides with player'
##     DirectionModifier = random.randrange(1)
##if   DirectionModifier == 0
##     XDirection = -2
##     YDirection = 2
##elif DirectionModifier == 1
##     XDirection = -2
##     YDirection = -2