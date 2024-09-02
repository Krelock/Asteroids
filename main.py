import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    pygame.time.Clock().tick(60)
    pygame.font.init()
    
    pygame.display.set_caption("Asteroids")
    
    score = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Shot.containers = (shots,updatable, drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if player.collision(obj):
                return
        for obj in asteroids:
            for shot in shots:
                if shot.collision(obj):
                    Asteroid.split(obj)
                    Asteroid.split(shot)
                    score += 1
                    pygame.display.set_caption(f"Asteroids - {score}")
                
        
        screen.fill("black")
        

        for obj in drawable:
            obj.draw(screen)
        
        
            
        
        
        
        pygame.display.flip()
        
        
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
