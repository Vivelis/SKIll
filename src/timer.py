import time
import pygame


def display():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    start = time.time()
    done = False
    white=(255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)

    bg = (0,0,0)
    while not done:
        for event in pygame.event.get():
            screen.fill(bg)
            if event.type == pygame.QUIT:
                done = True
            font = pygame.font.SysFont("Arial", 22)
        screen.fill(bg)
        txtsurf = font.render(timer(start, 120), True, white)
        screen.blit(txtsurf,(370 - txtsurf.get_width() // 2, 0 + txtsurf.get_height() // 2))
        pygame.display.update()

display()
