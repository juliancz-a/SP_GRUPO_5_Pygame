import pygame

from constantes import *
from scoreboard import Scoreboard

from class_image import Image
from assets_cfg import *

from draw_functions import *

from class_states import *
class Menu:

    def __init__(self, surface:pygame.Surface, lista_jugadores) -> None:

        self.surface = surface
        self.lista_jugadores = lista_jugadores
        self.background = Image(MENU_BACKGROUND, (0,0), (1280,720))
        self.chains = Image(CHAINS, (130, 320), (150, 270))

        self.play_button = MENU_LISTA[0]["box"]
        self.options_button = MENU_LISTA[1]["box"]
        self.exit_button = MENU_LISTA[2]["box"]
        self.title = MENU_LISTA[3]["box"]

        self.box_list = [self.play_button, self.options_button, self.exit_button, self.title]

        self.images = [self.background, self.chains]

        self.lista_cfg = MENU_LISTA

        self.option = None

        self.music = MENU_MUSIC
    
    def render(self):

        set_buttons_colors(self.box_list, self.lista_cfg)
            
        self.surface.fill("white")
        
        draw_assets(self.surface, self.box_list, self.images, self.lista_cfg)
        Scoreboard(FUENTE_1, self.surface, self.lista_jugadores).draw()

        pygame.display.update()


  
    def handle_event (self, event):
        
        self.option = self.button_click_event(event)

    def update (self):

        selection = None

        match self.option:
            case 0:
                selection = "play"
            case 1:
                selection = "help"
            case 2:
                selection = "quit"
            
        return selection
    
    def set_music(self):
    
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    
    def button_click_event (self, event):
        lista = [ self.play_button,
        self.options_button,
        self.exit_button]
        
        button_selected = 0
        for boton in lista:
            retorno = boton.interaction(event)

            if retorno:
                return button_selected

            button_selected += 1
        
        return None