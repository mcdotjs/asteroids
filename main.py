import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    pygame.display.set_caption("Mirkova prva hra")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            item.update(dt)
        for item in asteroids:
            if item.is_colliding(player):
                print("Game over!")
                sys.exit()
                # pygame.quit()
        for item in asteroids:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
