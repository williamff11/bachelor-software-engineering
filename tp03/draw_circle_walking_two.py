import pygame

pygame.init()
largura_tela = 800
altura_tela = 640
posicao_horizontal_circle = 400
posicao_vertical_circle = 320
horizontal = 1
vertical = 1
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
conta_clocks = 0

# cores
purple = (150, 70, 255)
amarelo = (255, 255, 0)
preto = (0, 0, 0)

pygame.display.set_caption('Circle')


def draw_circle(posy_horizontal, posy_vertical):
    tela.fill(preto)
    pygame.draw.circle(
        tela, amarelo, (posy_horizontal, posy_vertical), 50)
    pygame.display.update()


terminou = False
tela.fill(preto)
draw_circle(posicao_horizontal_circle, posicao_vertical_circle)
while not terminou:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                horizontal = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                horizontal = 1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                vertical = -1
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                vertical = 1
        draw_circle(posicao_horizontal_circle, posicao_vertical_circle)
        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks += 1
    if conta_clocks == 100:

        # horizontal
        if posicao_horizontal_circle == 750 and horizontal == 1:
            horizontal = 1
            posicao_horizontal_circle = 50
            draw_circle(posicao_horizontal_circle, posicao_vertical_circle)
        elif posicao_horizontal_circle == 50 and horizontal == -1:
            horizontal = -1
            posicao_horizontal_circle = 750
            draw_circle(posicao_horizontal_circle, posicao_vertical_circle)
        else:
            if horizontal == 1:
                posicao_horizontal_circle += 5
            else:
                posicao_horizontal_circle -= 5
            draw_circle(posicao_horizontal_circle, posicao_vertical_circle)

        # verify_vertical(posicao_vertical_circle)
        if posicao_vertical_circle == 50 and vertical == 1:
            posicao_vertical = 1
            posicao_vertical_circle = 590
            draw_circle(posicao_horizontal_circle, posicao_vertical_circle)
        elif posicao_vertical_circle == 590 and vertical == -1:
            posicao_vertical = -1
            posicao_vertical_circle = 50
            draw_circle(posicao_horizontal_circle, posicao_vertical_circle)
        else:
            if vertical == -1:
                posicao_vertical_circle += 5
            else:
                posicao_vertical_circle -= 5
            draw_circle(posicao_horizontal_circle, posicao_vertical_circle)

        conta_clocks = 0

pygame.display.quit()

pygame.quit()
