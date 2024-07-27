from Static.static import TitleFont, Font, screen, Cols


class Text:
    def __init__(self, name, x, y, font):
        self.name = name
        self.x = x
        self.y = y
        self.font = font

    def write(self, screenType, col):
        text = self.font.render(self.name, True, col)
        screenType.blit(text, (self.x, self.y))


def InfoText(planet):
    title = Text(f"{planet.name} info", 50, 30, TitleFont)
    menu = Text("Back", 50, 200, Font)
    mass_info = Text(f"Mass: {planet.mass}", 500, 30, Font)
    sa_info = Text(f"Surface Area: {planet.radius**2 * 3.14159 * 4 / 1e6} km^2", 500, 180, Font)  # Corrected surface area
    rad_info = Text(f"Radius: {planet.radius} km", 500, 330, Font)  # Corrected units
    age_info = Text(f"Age: Unknown", 500, 480, Font)  # Placeholder
    grav_info = Text(f"Gravitational Pull: Unknown", 500, 630, Font)  # Placeholder
    vel_info = Text(f"Velocity: {planet.velocity}", 500, 780, Font)
    return Sentence(title, menu, mass_info, sa_info, rad_info, age_info, grav_info, vel_info)


def playText():
    SolarSystemText = Text("The Solar System", 50, 30, TitleFont)
    menu_text = Text("Menu", 50, 200, Font)
    SpeedUpText = Text("Speed +", 50, 300, Font)
    SpeedDownText = Text("Speed -", 50, 400, Font)
    StopText = Text("Stop", 50, 500, Font)
    return Sentence(SolarSystemText, menu_text, SpeedUpText, SpeedDownText, StopText)


class Sentence:
    def __init__(self, *text):
        self.all = text

    def writeAll(self):
        for item in self.all:
            item.write(screen, Cols.white)
