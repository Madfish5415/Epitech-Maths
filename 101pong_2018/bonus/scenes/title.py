from pygame.locals import *
from classes import *
from constants import *
import scenes.game


class TitleScene(scene.Scene):
    def render(self, window):
        title_font = font.Font("101pong", display.FONT, colors.WHITE, 100)
        caption_font = font.Font("Press 'Enter' to confirm your choice", display.FONT, colors.WHITE, 20)
        play_button = button.Button("PLAY", (250, 80), style.Style(colors.WHITE, colors.BLACK))

        window.fill(colors.BLACK)
        title_font.render(window, ((display.WIDTH - title_font.width) / 2,
                                   display.HEIGHT * 0.1))
        play_button.render(window, ((display.WIDTH - play_button.width) / 2,
                                    (display.HEIGHT - play_button.height) / 2))
        caption_font.render(window, ((display.WIDTH - caption_font.width) / 2,
                                     display.HEIGHT * 0.9))

    def events_manager(self, events, pressed_keys):
        for event in events:
            if event.type == KEYDOWN:

                if event.key == K_RETURN:
                    self.switch_to(scenes.game.GameScene())
                if event.key == K_ESCAPE:
                    self.switch_to(None)

    def update(self):
        pass
