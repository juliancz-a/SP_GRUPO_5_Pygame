import pygame
from constantes import *
from class_box import Box

class Menu:

    def __init__(self, surface:pygame.Surface) -> None:
        self.surface = surface
        self.resize_surface = None
        self.background = r"code\data\img\Menu_background.png"
        self.play_button = Box(surface.get_size(), (300,200), (200,100))
        self.title = Box((surface.get_size()), (200,50), (400,50))
        self.music = None


    def render(self):

        play = False

        self.play_button.set_color("darkslategray4", "darkslategrey", "grey")

        while True:
            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            
            if play:
                return "play"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.VIDEORESIZE:
                    print(event.size)
                    print(self.surface.get_size())
                    self.resize_surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.play_button.resize(event.size)
                    self.surface = self.resize_surface
                play = self.play_button.interaction(event)
            
            self.surface.fill("black")
            self.surface.blit(background, (0,0))
            
            self.play_button.draw_box(self.surface, border_radius=5, border=True, border_width=5)
            self.play_button.draw_text(self.surface, "Jugar", "dodgerblue4", r"code\data\vinque rg.otf", 50)

            self.title.draw_text(self.surface, "POP THE CARD", "dodgerblue4", r"code\data\vinque rg.otf", 50)
            pygame.display.update()

    def set_bg():
        pass

    def set_music(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(0)
        pygame.mixer.music.set_volume(0.1)


