from random import randint
from sys import exit

import pygame
from pygame.locals import *

pygame.init()

largura = 640
altura = 480
x = largura / 2
y = altura / 2

x_azul = randint(40, 600)
y_azul = randint(50, 430)

colisoes = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

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
    rect_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    rect_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if rect_vermelho.colliderect(rect_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        colisoes += 1
        print(f'Pontos: {colisoes}')
    pygame.display.update()
