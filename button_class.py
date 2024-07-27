from Static.static import click, Cols, screen, Font
from text_class import Text
from pygame import Rect
from planetClass import Planet


def button_press(mouse_pos, mouse_status, *buttons):
    for button in buttons:
        if not button.rect.collidepoint(mouse_pos):
            continue
        button.write(screen, Cols.mercury)
        if mouse_status:
            click.play()
            button.func()


class Button(Text):
    def __init__(self, name, x, y, font, func, rect):
        super().__init__(name, x, y, font)
        self.func = func
        self.rect = rect


SpeedUpButton = Button("Speed +", 30, 300, Font, Planet.speedUp, Rect(30, 300, 165, 50))
SpeedDownButton = Button("Speed -", 30, 400, Font, Planet.slowDown, Rect(30, 400, 165, 50))
StopButton = Button("Stop", 30, 500, Font, Planet.stop, Rect(30, 500, 110, 50))
