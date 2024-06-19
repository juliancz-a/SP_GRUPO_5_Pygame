import pygame
from constantes import *
from class_box import Box

class Menu:

    def __init__(self, surface:pygame.Surface) -> None:
        self.surface = surface
        self.background = r"code\data\img\Menu_background.png"

        self.play_button = Box(surface.get_size(), (300,200), (200,75))
        self.options_button = Box(surface.get_size(), (300,300), (200,75))
        self.exit_button = Box(surface.get_size(), (300,400), (200,75))

        self.title = Box((surface.get_size()), (200,50), (400,50))
        self.music = None


    def render(self):

        play = False
        option = False
        exit = False

        self.play_button.set_color("darkslategray4", "darkslategrey", "grey")
        self.options_button.set_color("darkslategray4", "darkslategrey", "grey")
        self.exit_button.set_color("darkslategray4", "darkslategrey", "grey")


        while True:
            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            
            if play:
                return "play"
            elif option:
                return "option"
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT or exit:
                    return False
                
                elif event.type == pygame.VIDEORESIZE:
                    self.resize_surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.play_button.resize(event.size)
                    self.title.resize(event.size)
                    self.options_button.resize(event.size)

                play = self.play_button.interaction(event)
                option = self.options_button.interaction(event)
                exit = self.exit_button.interaction(event)

            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            self.exit_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.exit_button.draw_text(self.surface, "Salir", "dodgerblue4", r"code\data\vinque rg.otf", 50, border=True, border_thickness=1, border_color="red")

            self.options_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.options_button.draw_text(self.surface, "Opciones", "dodgerblue4", r"code\data\vinque rg.otf", 50, border=True, border_thickness=1, border_color="red")

            self.play_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.play_button.draw_text(self.surface, "Jugar", "dodgerblue4", r"code\data\vinque rg.otf", 50, border=True, border_thickness=1, border_color="red")

            self.title.draw_text(self.surface, "POP THE CARD", "dodgerblue4", r"code\data\vinque rg.otf", 50, border=True)

            pygame.display.update()

    def set_bg():
        pass

    def set_music(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.1)


