import pygame

from class_box import Box

class Menu:

    def __init__(self, surface) -> None:
        self.surface = surface
        self.background = None
        self.music = None


    def render(self):

        play_button = Box((150,150), (300,300))
        play_button.set_color("red", "yellow", "grey")
        play = False
        title = Box((200,50), (400,50))

        while True:
            if play:
                return "play"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                play = play_button.interaction(event)

            self.surface.fill("black")

            play_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            title.draw_text(self.surface, "Juego", "red", "Arial", 50)
            pygame.display.update()
   
    def set_bg():
        pass

    def set_music():
        pass


