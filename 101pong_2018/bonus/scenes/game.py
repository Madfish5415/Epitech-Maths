import pygame
from pygame.locals import *
from classes import *
from constants import *
import scenes.title


class GameScene(scene.Scene):
    def __init__(self):
        super().__init__()
        self.player_one = bat.Bat(elements.BAT_SIZE, elements.BAT_VELOCITY, 20)
        self.player_two = bat.Bat(elements.BAT_SIZE, elements.BAT_VELOCITY,
                                  display.WIDTH - elements.BAT_SIZE[0] - 20)
        self.score_one = 0
        self.score_two = 0
        self.text_one = font.Font(str(self.score_one), display.FONT, colors.WHITE, 80)
        self.text_two = font.Font(str(self.score_two), display.FONT, colors.WHITE, 80)
        self.ball = ball.Ball(elements.BALL_RADIUS, elements.BALL_VELOCITY)

    def render(self, window):
        window.fill(colors.BLACK)
        pygame.draw.rect(window, colors.WHITE, self.player_one.get_rect())
        pygame.draw.rect(window, colors.WHITE, self.player_two.get_rect())
        pygame.draw.circle(window, colors.WHITE, self.ball.pos, self.ball.radius)
        self.text_one.render(window, [200, display.HEIGHT - 200])
        self.text_two.render(window, [display.WIDTH - 200, display.HEIGHT - 200])

    def events_manager(self, events, pressed_keys):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.switch_to(scenes.title.TitleScene())
        if pressed_keys[K_z]:
            self.player_one.move("UP")
        if pressed_keys[K_s]:
            self.player_one.move("DOWN")
        if pressed_keys[K_UP]:
            self.player_two.move("UP")
        if pressed_keys[K_DOWN]:
            self.player_two.move("DOWN")

    def update(self):
        if self.ball.pos[0] < 0:
            self.score_one += 1
            self.text_one.text = str(self.score_one)
            self.ball.reset()
        if self.ball.pos[0] > display.WIDTH:
            self.score_two += 1
            self.text_two.text = str(self.score_two)
            self.ball.reset()
        self.ball.move(self.player_one.get_rect(), self.player_two.get_rect())
