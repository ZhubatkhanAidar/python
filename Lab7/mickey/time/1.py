import pygame
import datetime 

pygame.init()


width = 900
length = 800

screen = pygame.display.set_mode((width, length))

mainclock = pygame.image.load(r"C:\Users\Aidar\Desktop\pp2\Lab7\mickey\time\mainclock.png")
righthand = pygame.image.load(r"C:\Users\Aidar\Desktop\pp2\Lab7\mickey\time\rightarm.png")
lefthand = pygame.image.load(r"C:\Users\Aidar\Desktop\pp2\Lab7\mickey\time\leftarm.png")

clockCenter = screen.get_rect().center

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()

    secondAngle = (now.second / 60) * 360
    hourAngle = (now.hour / 60) * 360

    location = mainclock.get_rect(center = clockCenter)
    screen.blit(mainclock, location)

    newLeft = pygame.transform.rotate(lefthand, -secondAngle)
    leftLocation = newLeft.get_rect(center = clockCenter)
    screen.blit(newLeft, leftLocation)


    newRigth = pygame.transform.rotate(righthand, -hourAngle)
    rightLocation = newRigth.get_rect(center = clockCenter)
    screen.blit(newRigth, rightLocation)


    pygame.display.flip()