import pygame
class Window:

    def __init__(self, size, title, icon_path) -> None:
        self.size = size
        self.title = title
        self.icon = icon_path


    def render_window (self):

        surface = pygame.display.set_mode(self.size)

        pygame.display.set_caption(self.title)

        icon = pygame.image.load(self.icon)

        pygame.display.set_icon(icon)

        return surface