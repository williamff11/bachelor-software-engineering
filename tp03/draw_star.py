import math
import pygame

# Game init
pygame.init()
pygame.font.init()

largura_tela, altura_tela = 800, 640
tela = pygame.display.set_mode((largura_tela, altura_tela))

preto = (0, 0, 0)
branco = (255, 255, 255)

pygame.display.set_caption('Estrelinha')


def draw_star(tela, color, sides, radius, posicao):
    points = []

    for n in range(sides * 2):
        rad = radius if n % 2 == 0 else radius // 2
        angle = (n * math.pi / sides) + (90 * math.pi / 60)

        point = (
            int(math.cos(angle) * rad + posicao[0]),
            int(math.sin(angle) * rad + posicao[1])
        )

        points.append(point)

    return pygame.draw.polygon(tela, color, points)


terminou = False
clock = pygame.time.Clock()

while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    tela.fill(preto)

    draw_star(tela, branco, 5, 100, [
              tela.get_width() // 2, tela.get_height() // 2])

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
