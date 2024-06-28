import pygame
from constantes import *

from class_box import Box
from scoreboard import Scoreboard

from class_image import Image
from assets_cfg import *

from draw_functions import *
class Menu:

    def __init__(self, surface:pygame.Surface, lista_jugadores, music_file = None) -> None:

        self.lista_jugadores = lista_jugadores
        self.surface = surface
        
        self.background = Image(MENU_BACKGROUND, (0,0), (1280,720))
        self.chains = Image(CHAINS, (130, 320), (150, 270))

        self.lista_cfg = MENU_LISTA
      
        self.play_button = MENU_LISTA[0]["box"]
        self.options_button = MENU_LISTA[1]["box"]
        self.exit_button = MENU_LISTA[2]["box"]

        self.buttons_list = [self.play_button, self.options_button, self.exit_button]

        self.images = [self.background, self.chains]

        self.title = Box((200,100), (400,50))
        
        self.music = music_file

    def render(self):
        
        play = False
        option = False
        exit = False

        set_buttons_colors(self.buttons_list, self.lista_cfg)
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
                help = self.options_button.interaction(event)
                exit = self.exit_button.interaction(event)
            
            self.surface.fill("white")
            
            draw_assets(self.surface, self.buttons_list, self.images, self.lista_cfg)

            self.title.draw_text(self.surface, "Pop The Card", COLOR_LETRAS, FUENTE_1, 80, "border", 2, TITULO, True)

            pygame.display.update()

            Scoreboard(FUENTE_1, self.surface, self.lista_jugadores).draw()


    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)

def handle_mouse_events (button_list, event):
    action_set = set()
    for button in button_list:
        action = button.interaction(event)
        action_set.add(action)
  
