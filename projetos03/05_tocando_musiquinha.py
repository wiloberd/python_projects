import pygame 
from pygame import mixer


caminho_musica = '001.mp3'

print('Vamos ouvir uma musiquina boa!')
pygame.init()
mixer.init()
mixer.music.load(caminho_musica)
pygame.mixer.music.play()
input()
pygame.event.wait()
print('finalizando...')


# SOBRE O EXERCICIO PROPOSTO
"""
Exercício Python 21: Faça um programa em Python que 
abra e reproduza o áudio de um arquivo MP3.
"""