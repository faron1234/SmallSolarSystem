import math
from random import uniform
from Static.static import screen_size, Cols, PhysicsConstant as PC, velocity_scale
from pygame import image, transform, draw


class Planet:
    def __init__(self, name, rad, col, dist, mass, orbiting_planet=None, scale_size=None):
        self.name = name
        self.radius = rad
        self.colour = col
        self.distance = dist
        self.mass = mass
        self.orbiting_planet = orbiting_planet
        self.scale_size = scale_size if scale_size is not None else [1200, 1200]
        self.moving = True
        self.y = None
        self.x = None
        self.velocity = self.calculate_velocity() * velocity_scale if orbiting_planet else 0
        self.angle = uniform(0, 6.2832)
        self.image = transform.scale(image.load(f"Static/images/{self.name}.png"), self.scale_size)
        self.centre_of_screen = (screen_size[0] / 2, screen_size[1] / 2)

    def calculate_velocity(self):
        # Calculate orbital velocity based on distance from Sun (or orbiting planet)
        r = self.distance * 1000  # convert distance from km to meters
        return math.sqrt(PC.G * Sun.mass / r) / 1000  # convert velocity from m/s to km/s

    def render(self, screen, scale, center):
        scaled_distance = self.distance / scale
        scaled_radius = self.radius / scale
        self.updatePos(scale, center)
        draw.circle(screen, Cols.mercury, [int(self.centre_x(center)), int(self.centre_y(center))], int(scaled_distance), 1)
        draw.circle(screen, self.colour, [int(self.x), int(self.y)], int(scaled_radius))

    def updatePos(self, scale, center):
        self.angle += self.velocity if self.moving else +0
        scaled_distance = self.distance / scale
        xChange = math.sin(self.angle) * scaled_distance
        yChange = math.cos(self.angle) * scaled_distance
        self.x = xChange + self.centre_x(center)
        self.y = yChange + self.centre_y(center)

    def centre_x(self, center):
        return self.orbiting_planet.x if self.orbiting_planet else center[0]

    def centre_y(self, center):
        return self.orbiting_planet.y if self.orbiting_planet else center[1]

    def centre_xa(self):
        return self.x

    def centre_ya(self):
        return self.y

    def getname(self):
        return self.name

    @classmethod
    def speedUp(cls):
        for planet in Planets:
            planet.velocity += 0.02 * planet.velocity

    @classmethod
    def slowDown(cls):
        for planet in Planets:
            planet.velocity -= 0.02 * planet.velocity

    @classmethod
    def stop(cls):
        for planet in Planets:
            planet.moving = False

    @classmethod
    def move(cls):
        for planet in Planets:
            planet.moving = True

    @classmethod
    def moving(cls):
        return any(planet.moving for planet in Planets)


# Initialize the planets with adjusted velocities
Sun = Planet("Sun", 696340, Cols.sun, 0, 1.989e30, scale_size=[1400, 1400])
Mercury = Planet("Mercury", 2439.7, Cols.mercury, 57900000, "3.285 × 10^23 kg", Sun)
Venus = Planet("Venus", 6051.8, Cols.venus, 108200000, "4.867 × 10^24 kg", Sun)
Earth = Planet("Earth", 6371, Cols.earth, 149600000, "5.9722 × 10^24 kg", Sun)
Moon = Planet("Moon", 1737.4, Cols.venus, 384400, "7.3477 × 10^22 kg", Earth)  # Correct orbiting planet
Mars = Planet("Mars", 3389.5, Cols.mars, 227900000, "6.39 × 10^23 kg", Sun)
Jupiter = Planet("Jupiter", 69911, Cols.jupiter, 778600000, "1.898 × 10^27 kg", Sun)
Saturn = Planet("Saturn", 58232, Cols.saturn, 1433500000, "5.683 × 10^26 kg", Sun, [2500, 1400])
Uranus = Planet("Uranus", 25362, Cols.uranus, 2872500000, "8.681 × 10^25 kg", Sun)
Neptune = Planet("Neptune", 24622, Cols.neptune, 4495100000, "1.024 × 10^26 kg", Sun)
Pluto = Planet("Pluto", 1188.3, Cols.pluto, 5906376272, "1.30900 × 10^22 kg", Sun)

# Collect all planets into a list
Planets = [Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
