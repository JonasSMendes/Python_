import pygame
pygame.init()
pygame.mixer.music.load('021.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
