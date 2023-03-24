import pygame

class obstacle :
    def __init__(self, x, y, color) :
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen) :
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

class pomeranian(obstacle) :
    def __init__(self, x, y, color) :
        super().__init__(x, y, color)
        self.img = pygame.image.load("assets/pomeranian.png")

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.img, (self.x, self.y))

class obstacleSpawner :
    def __init__(self, screen) :
        self.screen = screen
        self.obstacles = []
        self.clock = pygame.time.Clock()
        self.spawn_rate = 1

    def spawn(self) :
        self.obstacles.append(pomeranian(0, 0, (255, 0, 0)))

    def draw(self) :
        for obstacle in self.obstacles :
            obstacle.draw(self.screen)

    def update(self) :
        self.draw()
        if self.clock.get_time() > self.spawn_rate :
            self.spawn()
            self.clock.tick()
            print(self.clock.get_time())