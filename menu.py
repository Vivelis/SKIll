import pygame
from py_class import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SKIll")

def temp_play():
    print("Jouer")

def temp_highscore():
    print("Highscore")

def main_menu():
    Boutons = []
    Boutons.append(Button("Jouer", temp_play, Rectangle(screen, 300, 150, 200, 50, Couleur(255, 255, 255))))
    Boutons.append(Button("Highscore", temp_highscore, Rectangle(screen, 300, 250, 200, 50, Couleur(255, 255, 255))))
    Boutons.append(Button("Exit", exit, Rectangle(screen, 300, 350, 200, 50, Couleur(255, 255, 255))))
    while True:
        for event in pygame.event.get(): # Boucle des évènements
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(Boutons)):
                    if Boutons[i].is_clicked(event) == True:
                        Boutons[i].linked_function()

        screen.fill((0, 205, 225)) # Remplir l'écran avec du bleu clair

        for i in range(len(Boutons)): # Afficher les boutons
            Boutons[i].draw()

        pygame.display.update() # Mettre à jour l'écran

main_menu()
