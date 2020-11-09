import pygame
import random

pygame.init()
largura_tela = 800
altura_tela = 600

lightBlue = (11, 158, 217)
blue = (3, 44, 166)
darkBlue = (2, 24, 89)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (242, 92, 162)

random_lightBlue = (110, 18, 214)
random_blue = (30, 4, 78)
random_darkBlue = (12, 42, 147)
random_white = (59, 55, 25)
random_black = (10, 100, 255)
random_pink = (22, 90, 212)
cores = [lightBlue, blue, darkBlue, white, black, pink, random_lightBlue,
         random_blue,
         random_darkBlue,
         random_white,
         random_black,
         random_pink,
         ]

clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura_tela, altura_tela))

conta_clocks = 0

pontos = 0

conta_segundos = 0


def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo " + str(tempo) +
                       "s | Pontuação: " + str(pontos), False, white)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)


terminou = False
while not terminou:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    conta_clocks += 1
    if conta_clocks == 50:
        conta_segundos += 1
        conta_clocks = 0
        tela.fill(cores[random.randint(0, 10)])

    mostra_tempo(conta_segundos, pontos)
    pygame.draw.rect(tela, black, (10, 10, 200, 100), 3)
    # Desenha um retângulo todo preenchido de vermelho
    pygame.draw.rect(tela, white, (400, 300, 50, 50))
    pygame.display.update()
    clock.tick(50)


pygame.display.quit()

pygame.quit()
