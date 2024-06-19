import pygame
from class_box import Box

class Play:
    def __init__(self, surface  ) -> None:
        self.surface = surface


    def render(self):

        title = Box((200,50), (400,50))

        options = False
        while True:
            if options:
                return "options"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                

            self.surface.fill("black")

            title.draw_text(self.surface, "A jugar!", "red", "Arial", 50)
            pygame.display.update()