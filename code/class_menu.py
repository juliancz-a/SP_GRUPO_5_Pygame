import pygame
from constantes import *

from class_box import Box
from scoreboard import Scoreboard

from class_image import Image
from assets_cfg import *

class Menu:

    def __init__(self, surface:pygame.Surface, lista_jugadores, music_file = None) -> None:

        self.lista_jugadores = lista_jugadores
        self.surface = surface
        
        self.background = Image(MENU_BACKGROUND, (0,0), (1280,720))
        self.chains = Image(CHAINS, (130, 320), (150, 270))

        self.lista_cfg = MENU_LISTA
      
        self.play_button = MENU_LISTA[0]["box"]
        self.exit_button = MENU_LISTA[1]["box"]
        self.options_button = MENU_LISTA[2]["box"]

        self.buttons_list = [self.play_button, self.options_button, self.exit_button]


        self.images = [self.background, self.chains]

        self.title = Box((200,100), (400,50))
        
        self.music = music_file


    def set_buttons_colors(self, button_list, list_cfg):
        for i in range(len(button_list)):
            button_list[i].set_color(*list_cfg[i]["colors"])

    def draw_buttons(self, button_list, lista_cfg):
        for i in range(len(button_list)):
            button_list[i].draw_box(self.surface, *lista_cfg[i]["config"])

    def draw_buttons_text(self, button_list, lista_cfg):
        for i in range(len(button_list)):
            button_list[i].draw_text(self.surface, *lista_cfg[i]["text"])

    def render(self):
        
        play = False
        option = False
        exit = False

        Menu.set_buttons_colors(self, self.buttons_list, self.lista_cfg)
        Menu.set_music(self)

        while True:
            if play:
                return "play"
            elif option:
                return "how to play"
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT or exit:
                    return False
                
                play = self.play_button.interaction(event)
                option = self.options_button.interaction(event)
                exit = self.exit_button.interaction(event)

            self.surface.fill("white")
            
            self.background.draw_image(self.surface)

            self.chains.draw_image(self.surface)

            Menu.draw_buttons(self, self.buttons_list, self.lista_cfg)
            Menu.draw_buttons_text(self, self.buttons_list, self.lista_cfg)
           
            self.title.draw_text(self.surface, "Pop The Card", COLOR_LETRAS, FUENTE_1, 80, "border", 2, TITULO, True)


            Scoreboard(FUENTE_1, self.surface, self.lista_jugadores).draw()


    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)





    # def draw_menu_assets (self):
    #     #image
            
    #     #buttons
    #     for button,properties in self.buttons:
    #         button.draw_box(self.surface, properties["border_radius"], properties["border"], properties["border_width"])
    #         button.draw_text(self.surface, properties["text"], properties["text_color"], properties["text_font"], properties["font_size"], outline = properties["text_outline"], outline_color= properties["text_outline_color"], center =properties["text_pos"])

    #     self.title.draw_text(self.surface, "Pop The Card", COLOR_LETRAS, FUENTE_1, 80, outline="shadow", outline_color=TITULO, center=True)
