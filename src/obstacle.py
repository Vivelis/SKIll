import pygame

class obstacle :
    def __init__(self, x, y, color) :
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen) :
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
