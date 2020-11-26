"""
Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um
círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)
"""
import pygame

pygame.init()
largura_tela = 800
altura_tela = 640
tela = pygame.display.set_mode((largura_tela, altura_tela))

# cores
purple = (150, 70, 255)
azul = (18, 10, 143)
preto = (0, 0, 0)

pygame.display.set_caption('Circle')


def draw_circle():
    pygame.draw.circle(tela, azul, (largura_tela/2, altura_tela/2), 50)
    pygame.display.update()


terminou = False
tela.fill(purple)
draw_circle()
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True


pygame.display.quit()

pygame.quit()
