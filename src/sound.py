import pygame
from pygame import mixer

pygame.init()

#importer le song dans notre jeu
def play_sound():
    mixer.init()
    mixer.music.load("assets/ski-sounds.mp3")
    mixer.music.set_volume(0.25)
    mixer.music.play()
    print("music stopped")

#generer la fentre de notre jeu
pygame.display.set_caption("Skill")
pygame.display.set_mode((1080,720))

runing = True

play_sound()
while runing:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                mixer.music.stop()
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()
            print("fermeture du jeu")