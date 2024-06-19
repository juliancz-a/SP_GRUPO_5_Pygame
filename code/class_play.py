import pygame
from class_box import Box

class Play:
    def __init__(self, surface  ) -> None:
        self.surface = surface
        self.menu_button = Box(surface.get_size(),(400,300), (200,100))
        self.play_title = Box(surface.get_size(),(200,50), (400,50))


    def render(self):
        

        self.menu_button.set_color("red", "yellow", "grey")
        menu = False

        options = False
        while True:
            if options:
                return "options"
            if menu:
                return "menu"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                menu = self.menu_button.interaction(event)

            self.surface.fill("black")
            
            self.menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.menu_button.draw_text(self.surface, "Volver al menú", "white", r"code\data\vinque rg.otf", 30)

            self.play_title.draw_text(self.surface, "A jugar!", "red", r"code\data\vinque rg.otf", 50)
            pygame.display.update()