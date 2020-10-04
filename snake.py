import random

import pygame

pygame.init()
resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
pygame.display.update()


class snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]


    def blit(self, screen):
        for posicao in self.corpo:
            screen.blit(self.textura, posicao)


class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)
    posicao = (200, 200)


    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        x = random.randint(0, 49) * 10
        y = random.randint(0, 49) * 10
        self.posicao = (x, y)


    def blit(self, screen):
        screen.blit(self.textura, self.posicao)


frutinha = Frutinha()
cobrinha = snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    frutinha.blit(screen)
    cobrinha.blit(screen)

    pygame.display.update()





