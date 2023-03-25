import pygame
from py_class import *
from enum import Enum
from highscore import parse_score

pygame.init()
screen = pygame.display.set_mode((588, 883))
pygame.display.set_caption("SKIll")

class Scene(Enum):
    MAIN_MENU = 1
    GAME = 2
    HIGHSCORE = 3

def temp_play():
    print ("GAME")
    scores = parse_score()
    return Scene.GAME, scores

def temp_highscore():
    scores = parse_score()
    return Scene.HIGHSCORE, scores
    

def gen_button_rect(index: int, screen) -> Rectangle:
    button_length = 275
    button_height = 100
    button_spacing = 40
    y_pos = 425 + (index * (button_height + button_spacing))
    x_pos = 150
    return Rectangle(screen, x_pos, y_pos, button_length, button_height, Couleur(200, 200, 200))

def main_menu():
    scene = Scene.MAIN_MENU
    background_menu = pygame.image.load("assets/background_menu.png")
    buttons_menu = pygame.image.load("assets/buttons.png")
    logo = pygame.image.load("assets/logo.png")
    Boutons = []
    Boutons.append(Button("Jouer", temp_play, gen_button_rect(0, screen)))
    Boutons.append(Button("Highscore", temp_highscore, gen_button_rect(1, screen)))
    Boutons.append(Button("Exit", exit, gen_button_rect(2, screen)))
    while True:
        for event in pygame.event.get(): # Boucle des évènements
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and scene == Scene.MAIN_MENU:
                for i in range(len(Boutons)):
                    if Boutons[i].is_clicked(event) == True:
                        scene, score = Boutons[i].linked_function()
        screen.fill((0, 0, 0))
        if (scene == Scene.MAIN_MENU):
            screen.blit(background_menu, (0, 0))
            screen.blit(buttons_menu, (150, 400))
            screen.blit(logo, (50, 0))
        if (scene == Scene.HIGHSCORE):
            screen.blit(background_menu, (0, 0))
            Rectangle(screen, 50, 50, 470, 750, Couleur(200, 200, 200)).draw()
            for i in range(10):
                if (i >= len(score)):
                    break
                text = str(i + 1) + ". " + score[i][0] + " : " + str(score[i][1])
                textobj = pygame.font.Font(None, 36).render(text, 1, (0, 0, 0))
                textrect = textobj.get_rect()
                textrect.center = (294, 200 + (i * 50))
                screen.blit(textobj, textrect)
        if (scene == Scene.GAME):
            1
        pygame.display.update() # Mettre à jour l'écran

main_menu()
