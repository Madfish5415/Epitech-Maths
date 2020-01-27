import pygame
from classes.font import *
from constants import display


class Button:
    def __init__(self, text, size, style):
        self.font = Font(text, display.FONT, style.color, size[1] * 0.6)
        self.style = style
        self.width = size[0]
        self.height = size[1]

    def render(self, window, pos):
        rectangle = pos[0], pos[1], self.width, self.height

        pygame.draw.rect(window, self.style.bg_color, rectangle)
        self.font.render(window, (pos[0] + ((self.width - self.font.width) / 2),
                                  pos[1] + ((self.height - self.font.height) / 2)))
