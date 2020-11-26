import pygame

pygame.init()
largura_tela = 800
altura_tela = 640
posicao_horizontal_circle = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
conta_clocks = 0

# cores
purple = (150, 70, 255)
azul = (18, 10, 143)
preto = (0, 0, 0)

pygame.display.set_caption('Circle')


def draw_circle(posy):
    tela.fill(preto)
    pygame.draw.circle(
        tela, azul, (posy, altura_tela/2), 50)
    pygame.display.update()


terminou = False
tela.fill(preto)
draw_circle(posicao_horizontal_circle)
while not terminou:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks += 1
    if conta_clocks == 10:
        conta_clocks = 0

        if posicao_horizontal_circle >= 750:
            posicao_horizontal_circle = 50
            draw_circle(posicao_horizontal_circle)
        else:
            posicao_horizontal_circle += 5
            draw_circle(posicao_horizontal_circle)


pygame.display.quit()

pygame.quit()
