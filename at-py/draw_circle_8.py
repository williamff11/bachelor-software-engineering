import pygame
import sys
import random
from collections import namedtuple


class Collision:
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    running = True
    background = (150, 70, 255)
    cinza = (232, 232, 232)
    azul = (18, 10, 143)

    quadradinhos = []

    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font(None, 20)
        self.screenSize = self.Coordinate(x=800, y=600)
        self.screen = pygame.display.set_mode(self.screenSize)

        self.button = pygame.Rect(
            self.screen.get_width() // 2 - 50, 50, 100, 100)

        self.loop()

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse(event)

            self.screen.fill(self.background)

            self.draw_circle('Clique')

            for quadrado in self.quadradinhos:
                pygame.draw.rect(self.screen, self.cinza, quadrado)

            pygame.display.update()

        pygame.display.quit()

    def handle_mouse(self, event):
        if event.button == 1:
            position = pygame.mouse.get_pos()

            if self.button.collidepoint(position):
                rect = self.draw_square()
                self.quadradinhos.append(rect)
                self.verifica_colisao(rect)

    def draw_circle(self, text):
        pygame.draw.ellipse(self.screen, self.azul, self.button)
        button_text = self.font.render(text, False, self.background)
        button_text_rect = button_text.get_rect(center=self.button.center)

        self.screen.blit(button_text, button_text_rect)

    def draw_square(self):
        x = random.randint(25, self.screen.get_width() - 25)
        y = random.randint(25, self.screen.get_height() - 25)

        return pygame.Rect(x, y, 50, 50)

    def verifica_colisao(self, rect):
        for quadrado in self.quadradinhos:
            if quadrado is not rect and quadrado.colliderect(rect):
                self.quadradinhos.remove(quadrado)
                if rect in self.quadradinhos:
                    self.quadradinhos.remove(rect)


colision_game = Collision()
