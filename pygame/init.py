import pygame

pygame.init()
largura_tela, altura_tela = 800, 640
tela = pygame.display.set_mode((largura_tela, altura_tela))

branco = (255, 255, 255)
preto = (0, 0, 0)

terminou = False

tela.fill(preto)

pygame.display.update()
while not terminou:
    # Checar os eventos do mouse aqui
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
