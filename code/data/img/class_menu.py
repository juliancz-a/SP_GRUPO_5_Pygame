import pygame
from testeo import MENU_LISTA
from constantes import *
from class_box import Box
from draw_scoreboard import Scoreboard_2

class Menu:

    def __init__(self, wh, surface:pygame.Surface, lista, lista_jugadores, music_file = None) -> None:

        self.lista = lista
        self.lista_jugadores = lista_jugadores
        self.surface = surface
        self.original_wh = wh
        self.background = MENU_BACKGROUND

        self.config_list = MENU_LISTA

        self.exit_button = MENU_LISTA[1]["box"]
        self.play_button = MENU_LISTA[0]["box"]
        self.options_button = MENU_LISTA[2]["box"]

        self.buttons_list = [self.play_button, self.options_button, self.exit_button]
        self.buttons_colors = [COLOR_BOX, BORDE_BOX, HOVER_BOX]
        self.config = [self.surface, 15, True, 5]

        self.chains = Box(self.original_wh, (130, 320), (150, 270), press_sound=None, image=CHAINS)

        self.title = Box((self.original_wh), (200,100), (400,50))
        
        self.music = music_file

    def buttons_colors(self, button_list):
        for i in range(len(button_list)):
            for button in self.config_list:
                button_list[i].set_color(button["colors"][0], button["colors"][1], button["colors"][2])

    def draw_buttons(self, button_list):
        for i in range(len(button_list)):
            for button in self.config_list:
                button_list[i].draw_box(self.surface, *button["config"])

    def render(self):
        print(self.lista_jugadores)
        play = False
        option = False
        exit = False

        Menu.set_music(self)

        while True:
            background = pygame.image.load(self.background)
            background = pygame.transform.scale(background, (self.surface.get_width(), self.surface.get_height()))
            
            if play:
                return ("play", self.original_wh, 0, self.lista, 0)
            elif option:
                return "how to play"
            
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

            self.chains.draw_image(self.surface)

            Menu.draw_buttons(self, self.buttons_list)
            self.exit_button.draw_text(self.surface, "Salir", LETRAS_2, FUENTE_1, 60, "shadow", outline_thickness=1, outline_color=BORDE_2, center=True)

            self.options_button.draw_text(self.surface, "Opciones", LETRAS_2, FUENTE_1, 60, "shadow", outline_thickness=1, outline_color=BORDE_2, center=True)

            self.play_button.draw_text(self.surface, "Jugar", LETRAS_2, FUENTE_1, 60, "shadow", outline_thickness=1, outline_color=BORDE_2, center=True)

            self.title.draw_text(self.surface, "Pop The Card", COLOR_LETRAS, FUENTE_1, 80, "border", outline_thickness=2, outline_color=TITULO, center=True)


            scoreboard = Scoreboard_2(FUENTE_1, self.surface, self.lista_jugadores)
            scoreboard.draw()
            pygame.display.update()

    def set_bg():
        pass

    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)


