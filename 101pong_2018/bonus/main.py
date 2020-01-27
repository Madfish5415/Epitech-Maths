import pygame
from constants.display import *
from scenes.title import *


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    current_scene = TitleScene()

    while current_scene is not None:
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                return
        current_scene.events_manager(events, pressed_keys)
        current_scene.update()
        current_scene.render(window)
        current_scene = current_scene.scene
        pygame.display.flip()
        clock.tick(60 * display.SPEED)


if __name__ == '__main__':
    main()
