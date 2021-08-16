# https://www.youtube.com/watch?v=k7PLSocEREs&list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ

from sys import exit

import pygame
from pygame.locals import *

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        pygame.display.update()
