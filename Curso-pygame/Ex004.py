from sys import exit

import pygame
from pygame.locals import *

pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        """ if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            if event.key == K_s:
                y += 20 """
    if pygame.key.get_pressed()[K_a]:
        x -= 5
    if pygame.key.get_pressed()[K_d]:
        x += 5
    if pygame.key.get_pressed()[K_w]:
        y -= 5
    if pygame.key.get_pressed()[K_s]:
        y += 5
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    pygame.display.update()
