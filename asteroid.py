import pygame
import random
from logger import *
from constants import  LINE_WIDTH, ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_asteroid_one_direction = self.velocity.rotate(random.uniform(20, 50))
        new_asteroid_two_direction = self.velocity.rotate(random.uniform(20, 50))

        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_one = Asteroid(self.position.x,self.position.y, new_asteroids_radius)
        new_asteroid_two = Asteroid(self.position.x,self.position.y, new_asteroids_radius)

        new_asteroid_one.velocity = new_asteroid_one_direction * 1.2
        new_asteroid_two.velocity = new_asteroid_two_direction * 1.2
