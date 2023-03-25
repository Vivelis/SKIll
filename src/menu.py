import pygame
from enum import Enum

from src.py_class import *
from src.highscore import parse_score
from src.skis import Skis


class Scene():
    MAIN_MENU = 1
    GAME = 2
    EXIT = 3

    def __init__(self, screen) -> None:
        self.scene = Scene.MAIN_MENU
        self.screen = screen
        self.clock = pygame.time.Clock()

def temp_play(scn: Scene):
    scn.scene = Scene.GAME

def temp_highscore(scn: Scene):
    scn.scene = Scene.HIGHSCORE
    scn.scores = parse_score()

def gen_button_rect(index: int, screen) -> Rectangle:
    button_length = 275
    button_height = 100
    button_spacing = 40
    y_pos = 425 + (index * (button_height + button_spacing))
    x_pos = 150
    return Rectangle(screen, x_pos, y_pos, button_length, button_height, Couleur(200, 200, 200))

def main_menu(scn: Scene):
    highscore = False
    background_menu = pygame.image.load("assets/background_menu.png")
    buttons_menu = pygame.image.load("assets/buttons.png")
    back_button = pygame.image.load("assets/back_button.png")
    logo = pygame.image.load("assets/logo.png")
    Boutons = []
    Boutons.append(Button("Jouer", temp_play, gen_button_rect(0, scn.screen)))
    Boutons.append(Button("Highscore", temp_highscore, gen_button_rect(1, scn.screen)))
    Boutons.append(Button("Exit", exit, gen_button_rect(2, scn.screen)))

    while scn.scene == Scene.MAIN_MENU:
        dt = scn.clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(Boutons)):
                    if Boutons[i].is_clicked(event) == True:
                        if (Boutons[i].text == "Highscore"):
                            score = parse_score()
                            highscore = True
                        else:
                            score = Boutons[i].linked_function(scn)
                    if highscore == True and 450 <= event.pos[0] <= 490 and 730 <= event.pos[1] <= 770:
                        print("back")
                        highscore = False
        if (not highscore):
            scn.screen.fill((0, 0, 0))
            scn.screen.blit(background_menu, (0, 0))
            scn.screen.blit(buttons_menu, (150, 400))
            scn.screen.blit(logo, (50, 0))
        else:
            scn.screen.blit(background_menu, (0, 0))
            Rectangle(scn.screen, 50, 50, 470, 750, Couleur(200, 200, 200)).draw()
            for i in range(10):
                if (i >= len(score)):
                    break
                text = str(i + 1) + ". " + score[i][0] + " : " + str(score[i][1])
                textobj = pygame.font.Font(None, 36).render(text, 1, (0, 0, 0))
                textrect = textobj.get_rect()
                textrect.center = (294, 200 + (i * 50))
                scn.screen.blit(back_button, (450, 730))
                scn.screen.blit(textobj, textrect)
        pygame.display.update() # Mettre à jour l'écran
