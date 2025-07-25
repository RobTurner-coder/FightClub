import pygame
from circleshape import *
from constants import *
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, display):
        pygame.draw.circle(display, "White", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_angle = pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.draw(new_radius)
        