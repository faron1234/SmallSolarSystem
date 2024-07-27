import os

import pygame
from pygame import mixer, display

pygame.init()

screen_size = (display.Info().current_w, display.Info().current_h)
click = mixer.Sound(os.path.join("static", "buttonclick.wav"))
Font = pygame.font.Font(os.path.join("static", "Dosis-ExtraLight.ttf"), 45)
TitleFont = pygame.font.Font(os.path.join("static", "Dosis-ExtraLight.ttf"), 80)
screen = display.set_mode(screen_size)


class Cols:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    sun = (230, 230, 0)
    mercury = (131, 134, 139)
    venus = (231, 227, 224)
    earth = (0, 0, 255)
    mars = (253, 133, 96)
    jupiter = (217, 199, 176)
    saturn = (178, 167, 122)
    uranus = (143, 161, 171)
    neptune = (108, 139, 183)
    pluto = (235, 193, 153)


Background = pygame.image.load(os.path.join("static", "images/Stars.jpg"))
Background = pygame.transform.scale(Background, screen_size)

