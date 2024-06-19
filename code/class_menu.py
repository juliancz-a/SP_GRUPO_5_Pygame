import pygame
from constantes import *
from class_box import Box

class Menu:

    def __init__(self, surface:pygame.Surface) -> None:
        self.surface = surface
        self.background = r"code\data\img\Menu_background.png"
        self.music = MUSICA_MENÚ


    def render(self):
        background = pygame.image.load(self.background)
        background = pygame.transform.scale(background, (1280,720))

        play_button = Box((300,200), (200,100))
        play_button.set_color("darkslategray4", "darkslategrey", "grey")
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
            self.surface.blit(background, (0,0))

            play_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            play_button.draw_text(self.surface, "Jugar", "dodgerblue4", FUENTE, 50, True, 1, BORDE_1)

            title.draw_text(self.surface, "POP THE CARD", "dodgerblue4", FUENTE, 50, True, 5, BORDE_1)
            pygame.display.update()

    def set_bg():
        pass

    def set_music(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.1)


