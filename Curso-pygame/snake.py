import pygame
from pygame.locals import *

from sys import exit

from random import randint

pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.3)
musica = pygame.mixer.music.load('Curso-pygame/music.wav')
pygame.mixer.music.play(-1, 0, 200)

som_colisao = pygame.mixer.Sound('Curso-pygame/coin.wav')

largura = 640
altura = 480
x_cobra = int(largura/2 )
y_cobra = int(altura/2)

velocidade = 5

comprimento_inicial = 100

morreu = False

x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

fonte = pygame.font.SysFont('cascadia code', 20, True, True)
pontos = 0
recorde = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

relogio = pygame.time.Clock()

lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, y_maca, x_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

while True:
    relogio.tick(60)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    recorde_msg = f'Recorde de pontos: {recorde}'
    texto_formatado_recorde = fonte.render(recorde_msg, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    x_cobra += x_controle
    y_cobra += y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        som_colisao.play()
        comprimento_inicial += 1

    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = 480
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = 640

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over!  Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        rect_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        if recorde < pontos:
                            recorde = pontos
                        reiniciar_jogo()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                        
            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, rect_texto)
            pygame.display.update()

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (450, 40))
    tela.blit(texto_formatado_recorde, (320, 60))
    pygame.display.update()
