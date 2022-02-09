from turtle import back
import pygame
import sys
from pygame.locals import *

from Necromancer import Necromancer

pygame.init()

# Cursor
pygame.mouse.set_visible(False)

# Teclas
pygame.key.set_repeat(1, 25)

# Music
pygame.mixer.music.load("Music/8_Bit_Adventure.mp3")
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.10)

# Clock
fps = 60
clock = pygame.time.Clock()

# Window
window = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Machine Chronicles")
green = (0, 255, 0)

# Force (v) up and mass m.
v = 5
m = 1
isjump = False

# Methods

player = Necromancer("Images/Necromancer/Necromancer.png", "Necromancer")



while True:

    if isjump :
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F =(1 / 2)*m*(v**2)
        # change in the y co-ordinate
        player.get_rect().bottom-= F
        # decreasing velocity while going up and become negative while coming down
        v = v-1
        # object reached its maximum height
        if v<0:
            # negative sign is added to counter negative velocity
            m =-1
        # objected reaches its original state
        if v ==-6:
            # making isjump equal to false 
            isjump = False
            # setting original values to v and m
            v = 5
            m = 1

    window.fill(green)

    #player.applyGravity()

    player.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == KEYDOWN:
            player.handle_events(event.key)

            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_SPACE:
                isjump = True
                #player.jump()

        elif event.type == KEYDOWN:
            player.handle_events(event.key)

            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_SPACE:
                player.jump()

    pygame.display.update()
    clock.tick(fps)
