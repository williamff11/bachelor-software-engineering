import pygame

pygame.init()
largura_tela, altura_tela = 800, 640
tela = pygame.display.set_mode((largura_tela, altura_tela))

branco = (255, 255, 255)
preto = (0, 0, 0)


def draw_quadrado(x, y):
    tela.fill(preto)
    area = pygame.Rect(x, y, 100, 100)
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
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                posicao_atual[0] -= 5
                print('move para a esquerda')
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                posicao_atual[0] += 5
                print('move para a direita')
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                posicao_atual[1] += 5
                print('move para a baixo')
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                posicao_atual[1] -= 5
                print('move para a cima')
            draw_quadrado(*posicao_atual)

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
