import pygame
import const
import sprite


class Game:
    def __init__(self):
        #  Criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((const.LARGURA, const.ALTURA))
        pygame.display.set_caption(const.TITULO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True

    def novo_jogo(self):
        #  Instancia as classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        # loop do jogo
        self.jogando = True

        while self.jogando:
            self.relogio.tick(const.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #  Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(const.PRETO)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def tela_start(self):
        pass

    def game_over(self):
        pass

g = Game()

g.tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.game_over()
