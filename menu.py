import pygame
from py_class import *
from enum import Enum
from highscore import parse_score
import time

pygame.init()
screen = pygame.display.set_mode((588, 883))
pygame.display.set_caption("SKIll")

class Scene(Enum):
    MAIN_MENU = 1
    GAME = 2
    HIGHSCORE = 3
    GAMEOVER = 4

def temp_play():
    print ("GAME")
    scores = parse_score()
    return Scene.GAME, scores

def temp_test():
    scores = parse_score()
    return Scene.GAMEOVER, scores

def temp_highscore():
    scores = parse_score()
    return Scene.HIGHSCORE, scores
    
def temp_gameover():
    return Scene.GAMEOVER, []

def temp_menu():
    return Scene.MAIN_MENU, []

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
    buttons_menu2 = pygame.image.load("assets/buttons2.png")
    logo = pygame.image.load("assets/logo.png")
    Boutons = []
    Boutons.append(Button("Jouer", temp_test, gen_button_rect(0, screen)))
    Boutons.append(Button("Highscore", temp_highscore, gen_button_rect(1, screen)))
    Boutons.append(Button("Exit", exit, gen_button_rect(2, screen)))
    Boutons2 = []
    Boutons2.append(Button("RePlay", temp_play, gen_button_rect(0, screen)))
    Boutons2.append(Button("Menu", temp_menu, gen_button_rect(1, screen)))
    Boutons2.append(Button("Exit", exit, gen_button_rect(2, screen)))
    while True:
        for event in pygame.event.get(): # Boucle des évènements
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if scene == Scene.MAIN_MENU :
                if event.type == pygame.MOUSEBUTTONDOWN and scene == Scene.GAMEOVER:
                    for i in range(len(Boutons2)):
                        if Boutons2[i].is_clicked(event) == True:
                            scene, score = Boutons2[i].linked_function()
                if event.type == pygame.MOUSEBUTTONDOWN and scene == Scene.MAIN_MENU:
                    for i in range(len(Boutons)):
                        if Boutons[i].is_clicked(event) == True:
                            scene, score = Boutons[i].linked_function()
            else :
                if event.type == pygame.MOUSEBUTTONDOWN and scene == Scene.MAIN_MENU:
                    for i in range(len(Boutons)):
                        if Boutons[i].is_clicked(event) == True:
                            scene, score = Boutons[i].linked_function()
                if event.type == pygame.MOUSEBUTTONDOWN and scene == Scene.GAMEOVER:
                    for i in range(len(Boutons2)):
                        if Boutons2[i].is_clicked(event) == True:
                            scene, score = Boutons2[i].linked_function()
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
        if (scene == Scene.GAMEOVER):
            screen.blit(background_menu, (0, 0))
            background_menu = pygame.image.load("assets/background_menu.png")
            panneau = pygame.image.load("assets/panneau.png")
            panneau = pygame.transform.scale(panneau, (500, 400))
            screen.blit(panneau, (40, 0))
            text = "Distance parcourue :"
            textobj = pygame.font.Font(None, 50).render(text, 1, (0, 0, 0))
            textrect = textobj.get_rect()
            textrect.center = (294, 130)
            screen.blit(textobj, textrect)
            text = "485 480" + " m"
            textobj = pygame.font.Font(None, 60).render(text, 1, (0, 0, 0))
            textrect = textobj.get_rect()
            textrect.center = (294, 180)
            screen.blit(textobj, textrect)
            screen.blit(buttons_menu2, (150, 400))
            text = "RePlay"
            textobj = pygame.font.Font(None, 70).render(text, 1, (0, 0, 0))
            textrect = textobj.get_rect()
            textrect.center = (294, 480)
            screen.blit(textobj, textrect)
            text = "Menu"
            textobj = pygame.font.Font(None, 70).render(text, 1, (0, 0, 0))
            textrect = textobj.get_rect()
            textrect.center = (294, 610)
            screen.blit(textobj, textrect)
            text = "Leave"
            textobj = pygame.font.Font(None, 70).render(text, 1, (0, 0, 0))
            textrect = textobj.get_rect()
            textrect.center = (294, 750)
            screen.blit(textobj, textrect)

        pygame.display.update() # Mettre à jour l'écran

main_menu()
