import pygame
from constantes import *
from class_box import Box

class Menu:

    def __init__(self, wh, surface:pygame.Surface, music_file = None) -> None:
        self.surface = surface
        self.original_wh = wh
        self.background = MENU_BACKGROUND

        self.play_button = Box(self.original_wh, (300,300), (200,75), press_sound=PRESS_SOUND)
        self.options_button = Box(self.original_wh, (300,400), (200,75), press_sound=PRESS_SOUND)
        self.exit_button = Box(self.original_wh, (300,500), (200,75), press_sound=PRESS_SOUND)


        self.title = Box((self.original_wh), (200,100), (400,50))
        
        self.music = music_file


    def render(self):

        play = False
        option = False
        exit = False

        self.play_button.set_color(COLOR_BOX, BORDE_BOX, "grey")
        self.options_button.set_color(COLOR_BOX, BORDE_BOX, "grey")
        self.exit_button.set_color(COLOR_BOX, BORDE_BOX, "grey")

        self.play_button.resize(self.surface.get_size())
    
        self.title.resize(self.surface.get_size())
        self.exit_button.resize(self.surface.get_size())
        self.options_button.resize(self.surface.get_size())

        Menu.set_music(self)

        while True:
            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            
            if play:
                return "play", self.original_wh
            elif option:
                return "option"
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT or exit:
                    return False
                
                elif event.type == pygame.VIDEORESIZE:

                    self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.play_button.resize(event.size)
                    self.title.resize(event.size)
                    self.exit_button.resize(event.size)
                    self.options_button.resize(event.size)

                play = self.play_button.interaction(event)
                option = self.options_button.interaction(event)
                exit = self.exit_button.interaction(event)

            self.surface.fill("black")
            self.surface.blit(background, (0,0))

            self.exit_button.draw_box(self.surface, border_radius=15, border=True, border_width=5)
            self.exit_button.draw_text(self.surface, "Salir", COLOR_LETRAS, FUENTE_1, 50, shadow=True, border_thickness=2, border_color=BORDE_LETRAS)

            self.options_button.draw_box(self.surface, border_radius=15, border=True, border_width=5)
            self.options_button.draw_text(self.surface, "Opciones", COLOR_LETRAS, FUENTE_1, 50, shadow=True, border_thickness=2, border_color=BORDE_LETRAS)

            self.play_button.draw_box(self.surface, border_radius=15, border=True, border_width=5)
            self.play_button.draw_text(self.surface, "Jugar", COLOR_LETRAS, FUENTE_1, 50, shadow=True, border_thickness=2, border_color=BORDE_LETRAS)

            self.title.draw_text(self.surface, "Pop The Card", COLOR_LETRAS, FUENTE_1, 72, border=True, border_thickness=2, border_color=BORDE_LETRAS)

            pygame.display.update()

    def set_bg():
        pass

    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)


