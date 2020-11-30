import pygame

pygame.init()
largura_tela, altura_tela = 800, 640
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()

branco = (255, 255, 255)
preto = (0, 0, 0)


def draw_quadrado(posicioes):
    tela.fill(preto)
    area = pygame.Rect(posicioes[0], posicioes[1], 100, 100)
    pygame.draw.rect(tela, branco, area)
    pygame.display.update()


terminou = False
posicao_atual = [largura_tela/2 - 50, altura_tela/2 - 50]
draw_quadrado(posicao_atual)

while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.MOUSEBUTTONUP:
            # getposicaodoclick
            pos = pygame.mouse.get_pos()
            draw_quadrado(pos)


pygame.display.quit()
pygame.quit()
