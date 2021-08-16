# https://www.youtube.com/watch?v=FbgiJnqyF_I&list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ&index=2

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

        pygame.draw.rect(tela, (190, 0, 190), (200, 300, 40, 50))
        pygame.draw.circle(tela, (90, 90, 200), (300, 260), 40)
        pygame.draw.line(tela, (200, 200, 0), (390, 0), (390, 600), 5)
        pygame.display.update()
