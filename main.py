import pygame
from pygame import mouse, display, MOUSEBUTTONUP as MBU, MOUSEBUTTONDOWN as MBD, K_ESCAPE as ESC, K_SPACE as SPACE
from text_class import playText, InfoText
from planetClass import Planets, Planet
from button_class import SpeedUpButton, StopButton, SpeedDownButton, Button, button_press
from Static.static import Font, Background, Cols, click, screen


class Scale:
    scale = 100000
    center = (screen.get_width() / 2, screen.get_height() / 2)


class Screen:
    def __init__(self, display, buttons, primary):
        self.screen = display
        self.buttons = buttons
        self.primary = primary

    def draw(self):
        self.screen.blit(Background, [0, 0])
        self.buttons.writeAll() if self.buttons else None

    def isPrimary(self):
        return True if self.primary else False


def quit_game():
    pygame.quit()
    exit()


class Run:
    def __init__(self, screens):
        self.screens = screens
        self.current_screen = None
        self.done = False
        self.buttonDown = False
        self.zoom_in = False
        self.zoom_out = False
        self.speedUp = False
        self.slowDown = False
        self.mouse_pos = [0, 0]
        self.run()

    def check_keys(self, event, state):
        self.zoom_in = state if event.key == pygame.K_DOWN else self.zoom_in
        self.zoom_out = state if event.key == pygame.K_UP else self.zoom_out
        self.speedUp = state if event.key == pygame.K_EQUALS else self.speedUp
        self.slowDown = state if event.key == pygame.K_MINUS else self.slowDown

    def event(self, event):
        self.done = True if event.type == pygame.QUIT else None
        self.buttonDown = True if event.type == MBD else False if event.type == MBU else self.buttonDown
        if event.type == pygame.KEYDOWN:
            quit_game() if event.key == ESC else None
            self.check_keys(event, True)
            Planet.move() if event.key == SPACE and not Planet.moving() else Planet.stop() if event.key == SPACE and Planet.moving() else None
        elif event.type == pygame.KEYUP:
            self.check_keys(event, False)

    def events(self):
        for event in pygame.event.get():
            self.event(event)

    def renderPlanet(self, planet):
        planet.render(screen, Scale.scale, Scale.center)
        xa = planet.centre_xa()
        ya = planet.centre_ya()
        planetText = Font.render(planet.getname(), True, Cols.white)
        screen.blit(planetText, (xa, ya))
        mx, my = self.mouse_pos[0], self.mouse_pos[1]
        if mx < xa - 30 or mx > xa + 30 or my < ya - 30 or my > ya + 30:
            return
        if self.buttonDown:
            click.play()
            # self.current_screen = FactsPage(planet)

    def speedChange(self):
        Planet.speedUp() if self.speedUp else Planet.slowDown() if self.slowDown else None

    def scale(self):
        old_scale = Scale.scale
        Scale.scale *= 1.01 if self.zoom_in else (1 / 1.01 if self.zoom_out else 1)
        scale_change = Scale.scale / old_scale
        Scale.center = (
            Scale.center[0] + (self.mouse_pos[0] - Scale.center[0]) * (1 - 1 / scale_change),
            Scale.center[1] + (self.mouse_pos[1] - Scale.center[1]) * (1 - 1 / scale_change)
        )

    def run(self):
        self.current_screen = play
        clock = pygame.time.Clock()
        while not self.done:
            self.mouse_pos[0], self.mouse_pos[1] = mouse.get_pos()
            self.current_screen.draw()
            self.events()
            self.scale() if self.zoom_in or self.zoom_out else None
            self.speedChange() if self.speedUp or self.slowDown else None
            [self.renderPlanet(planet) for planet in Planets] if self.current_screen.isPrimary() else None
            display.flip()
            clock.tick(60)


# button_press((mx, my), ButtonDown, SpeedUpButton, SpeedDownButton, StopButton)


def FactsPage(planet):
    done = False
    text = InfoText(planet)
    while not done:
        screen.blit(Background, [0, 0])
        screen.blit(planet.image, [-750, -100])
        mx, my = pygame.mouse.get_pos()
        text.writeAll()

        # done, ButtonDown, _, _ = eventLoop()

        # button_class.button_press(button_class.Buttons.MenuButton, (mx, my), ButtonDown)


play = Screen(screen, [], True)

if __name__ == "__main__":
    Run(play)