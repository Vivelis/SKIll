import pygame

# Classe Couleur
# @param r: Rouge
# @param g: Vert
# @param b: Bleu
# @description: Classe permettant de créer une couleur RGB et de la récupérer
class Couleur:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_couleur(self):
        return (self.r, self.g, self.b)
    
# Classe Rectangle
# @param screen: Surface de pygame
# @param x: Position x du rectangle
# @param y: Position y du rectangle
# @param width: Largeur du rectangle
# @param height: Hauteur du rectangle
# @param couleur: Classe Couleur
# @description: Classe permettant de créer un rectangle et de l'afficher
class Rectangle:
    def __init__(self, screen, x, y, width, height, couleur):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.couleur = couleur

    def draw(self):
        pygame.draw.rect(self.screen, self.couleur.get_couleur(), (self.x, self.y, self.width, self.height))


# Classe Bouton
# @param text: Texte du bouton
# @param linked_function: Fonction liée au bouton éxécutée quand le bouton est cliqué
# @param rectangle: Classe Rectangle
# @description: Classe permettant de créer, cliquer et afficher un bouton
class Button:
    def __init__(self, text, linked_function, rectangle:Rectangle):
        self.text = text
        self.linked_function = linked_function
        self.rectangle = rectangle
        
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangle.x <= event.pos[0] <= self.rectangle.x + self.rectangle.width and self.rectangle.y <= event.pos[1] <= self.rectangle.y + self.rectangle.height:
                return True
        return False
    
    def linked_function(self):
        self.linked_function()

    def draw(self):
        self.rectangle.draw()
        textobj = pygame.font.Font(None, 36).render(self.text, 1, (0, 0, 0))
        textrect = textobj.get_rect()
        textrect.center = (self.rectangle.x + self.rectangle.width / 2, self.rectangle.y + self.rectangle.height / 2)
        self.rectangle.screen.blit(textobj, textrect)
