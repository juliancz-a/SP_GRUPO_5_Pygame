import pygame
from class_box import Box

class Play:
    def __init__(self, surface  ) -> None:
        self.surface = surface


    def render(self):
        
        title = Box((200,50), (400,50))

        menu_button = Box((400,300), (200,100))
        menu_button.set_color("red", "yellow", "grey")
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
                
                menu = menu_button.interaction(event)

            self.surface.fill("black")
            
            menu_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            menu_button.draw_text(self.surface, "Menú", "white", r"code\data\vinque rg.otf", 30)

            title.draw_text(self.surface, "A jugar!", "red", r"code\data\vinque rg.otf", 50)
            pygame.display.update()