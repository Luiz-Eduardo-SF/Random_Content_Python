import pygame

pygame.init()
pygame.mixer.music.load('exercicios_python/exe021-music.mp3')
pygame.mixer.music.play()
pygame.event.wait()