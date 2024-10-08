import pygame
import random
from constants import *
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    
    def split(self):
        pygame.sprite.Sprite.kill(self)
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random1 = random.uniform(20, 550)
            random2 = random.uniform(20, 550)
            
            asteroid_velocity1 = pygame.Vector2(self.velocity).rotate(random1)
            asteroid_velocity2 = pygame.Vector2(self.velocity).rotate(random2)

            new_radius = self.radius - ASTEROID_MIN_RADIUS          
            
            
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid_velocity1 * 1.2
            
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = asteroid_velocity2 * 1.2
            
           
    