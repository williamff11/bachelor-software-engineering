import pygame
import math
import random

pygame.init()
font = pygame.font.Font(None, 32)
largura_tela = 800
altura_tela = 640
tela = pygame.display.set_mode((largura_tela, altura_tela))

# cores
purple = (150, 70, 255)
azul = (18, 10, 143)
preto = (0, 0, 0)
branco = (255, 255, 255)

pygame.display.set_caption('Circle')


def draw_circle():
    pygame.draw.circle(tela, azul, (largura_tela/2, 60), 50)
    pygame.display.update()


def generate_random():
    return [random.randint(0, 750), random.randint(0, 590)]


def draw_quadrado(x, y):
    # tela.fill(preto)
    area = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(tela, branco, area)


def escreva():
    # definindo o texto
    text = font.render('Clique', True, branco)
    # copiando o texto para a superfície
    tela.blit(text, [largura_tela/2 - 35, 60])
    # atualizando a tela
    pygame.display.flip()


terminou = False
tela.fill(preto)
while not terminou:
    draw_circle()
    escreva()
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    sqx = (x - largura_tela/2)**2
    sqy = (y - 60)**2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if math.sqrt(sqx + sqy) < 100 and event.type == pygame.MOUSEBUTTONDOWN:
            larg, altu = generate_random()
            print([larg, altu])
            draw_quadrado(larg, altu)
    pygame.display.update()


pygame.display.quit()

pygame.quit()
