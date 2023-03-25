import pygame
import random
from timeit import default_timer

class obstacle :
    def __init__(self, x, y, w, h, color) :
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, screen) :
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

class pomeranian(obstacle) :
    def __init__(self, x, y, w, h, color) :
        super().__init__(x, y, w, h, color)
        self.img = pygame.image.load("assets/pomeranian.png")
        self.img = pygame.transform.scale(self.img, (w, h))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

class obstacleSpawner :
    def __init__(self, screen) :
        self.screen = screen
        self.obstacles = []
        self.last_spawn = default_timer()
        self.spawn_time = 1
        random.seed(10)

    def spawn(self) :
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.obstacles.append(pomeranian(x, y, 100, 100, (255, 0, 0)))

    def draw(self) :
        for obstacle in self.obstacles :
            obstacle.draw(self.screen)

    def update(self) :
        self.draw()
        if default_timer() - self.last_spawn > self.spawn_time :
            self.spawn()
            self.last_spawn = default_timer()
