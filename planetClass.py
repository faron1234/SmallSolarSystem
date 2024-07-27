import math
from random import uniform
from Static.static import screen_size, Cols
from pygame import image, transform, draw


class Planet:
    def __init__(self, name, rad, col, vel, dist, mass, scale_size=None, orbiting_planet=None):
        self.name = name
        self.radius = rad
        self.colour = col
        self.velocity = vel
        self.distance = dist
        self.mass = mass
        self.scale_size = [1200, 1200] if scale_size is not None else scale_size
        self.orbiting_planet = orbiting_planet
        self.y = None
        self.x = None
        self.angle = uniform(0, 6.2832)
        self.image = transform.scale(image.load(f"Static/images/{self.name}.png"), self.scale_size)
        self.centre_of_screen = (screen_size[0] / 2, screen_size[1] / 2)

    def render(self, screen, scale, center):
        scaled_distance = self.distance / scale
        scaled_radius = self.radius / scale
        self.updatePos(scale, center)
        draw.circle(screen, Cols.mercury, [int(self.centre_x(center)), int(self.centre_y(center))], int(scaled_distance), 1)
        draw.circle(screen, self.colour, [int(self.x), int(self.y)], int(scaled_radius))

    def updatePos(self, scale, center):
        self.angle += self.velocity
        scaled_distance = self.distance / scale
        xChange = math.sin(self.angle) * scaled_distance
        yChange = math.cos(self.angle) * scaled_distance
        self.x = xChange + self.centre_x(center)
        self.y = yChange + self.centre_y(center)

    def centre_x(self, center):
        if self.orbiting_planet is not None:
            return self.orbiting_planet.x
        else:
            return center[0]

    def centre_y(self, center):
        if self.orbiting_planet is not None:
            return self.orbiting_planet.y
        else:
            return center[1]

    def centre_xa(self):
        return self.x

    def centre_ya(self):
        return self.y

    def getname(self):
        return self.name

    @classmethod
    def speedUp(cls):
        for planet in Planets:
            planet.velocity += 0.2 * planet.velocity

    @classmethod
    def slowDown(cls):
        for planet in Planets:
            planet.velocity -= 0.2 * planet.velocity

    @classmethod
    def stop(cls):
        for planet in Planets:
            planet.velocity = 0


Sun = Planet("Sun", 696340, Cols.sun, 0, 0, "1.989 × 10^30 kg", [1400, 1400])
Mercury = Planet("Mercury", 2439.7, Cols.mercury, 0.00477, 57900000, "3.285 × 10^23 kg", Sun)
Venus = Planet("Venus", 6051.8, Cols.venus, 0.00354, 108200000, "4.867 × 10^24 kg", Sun)
Earth = Planet("Earth", 6371, Cols.earth, 0.003, 149600000, "5.9722 × 10^24 kg", Sun)
Moon = Planet("Moon", 1737.4, Cols.venus, 0.015, 384400, "7.3477 × 10^22 kg", Earth)
Mars = Planet("Mars", 3389.5, Cols.mars, 0.002424, 227900000, "6.39 × 10^23 kg", Sun)
Jupiter = Planet("Jupiter", 69911, Cols.jupiter, 0.001317, 778600000, "1.898 × 10^27 kg", Sun)
Saturn = Planet("Saturn", 58232, Cols.saturn, 0.000975, 1433500000, "5.683 × 10^26 kg", [2500, 1400], Sun)
Uranus = Planet("Uranus", 25362, Cols.uranus, 0.000684, 2872500000, "8.681 × 10^25 kg", Sun)
Neptune = Planet("Neptune", 24622, Cols.neptune, 0.000546, 4495100000, "1.024 × 10^26 kg", Sun)
Pluto = Planet("Pluto", 1188.3, Cols.pluto, 0.000471, 5906376272, "1.30900 × 10^22 kg", Sun)
Planets = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon]
