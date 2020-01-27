import pygame


class Font:
    def __init__(self, text, font, color, size):
        self.text = text
        self.font = pygame.font.Font(font, int(size))
        self.color = color
        self.width = self.font.size(text)[0]
        self.height = self.font.size(text)[1]

    def get_font(self):
        return self.font

    def get_size(self):
        return self.width, self.height

    def render(self, window, pos):
        text = self.font.render(self.text, True, self.color)
        window.blit(text, pos)
