import pygame
import random

pygame.init()
largura_tela, altura_tela = 800, 640
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()

branco = (255, 255, 255)
preto = (0, 0, 0)


def generate_random():
    return [random.randint(0, 750), random.randint(0, 590)]


def draw_quadrado(x, y):
    tela.fill(preto)
    area = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(tela, branco, area)
    pygame.display.update()


terminou = False
posicao_atual = [largura_tela/2 - 50, altura_tela/2 - 50]
draw_quadrado(*posicao_atual)

while not terminou:
    # Checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                larg, altu = generate_random()
                draw_quadrado(larg, altu)


# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
