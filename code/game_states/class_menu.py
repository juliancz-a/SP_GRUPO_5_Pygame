import pygame

from constantes import *
from game_tools.scoreboard import Scoreboard
from game_tools.draw_functions import *
from game_tools.event_handle import *

class Menu:

    def __init__(self, surface:pygame.Surface, lista_jugadores, menu_assets) -> None:

        self.surface = surface
        self.menu_assets = menu_assets
        self.lista_jugadores = lista_jugadores
        self.volume = True

        self.background = Image(MENU_BACKGROUND, (0,0), (1280,720))
        self.chains = Image(CHAINS, (130, 320), (150, 270))
        self.volume_button = Image(r"code\data\img\volume_button.png", (10, 10), (100,100))

        self.play_button = self.menu_assets[0]["box"]
        self.options_button = self.menu_assets[1]["box"]
        self.exit_button = self.menu_assets[2]["box"]
        self.title = self.menu_assets[3]["box"]

        self.box_list = [self.play_button, self.options_button, self.exit_button, self.title]


        self.option = None

        self.music = self.set_music()
    
    def render(self):
        images = [self.background, self.chains, self.volume_button]
        set_buttons_colors(self.box_list, self.menu_assets)
            
        self.surface.fill("white")
        
        draw_assets(self.surface, self.box_list, images, self.menu_assets)
        Scoreboard(FUENTE_1, self.surface, self.lista_jugadores).draw()

        pygame.display.update()
  
    def handle_event (self, event):
        volume_img = [{"img" : VOLUME_BUTTON}, {"img" : VOLUME_MUTE_BUTTON}]
        
        if self.volume_button.image_box.interaction(event):
            self.volume = not self.volume
            self.volume_button = Image(change_volume(self.volume, self.volume_button, volume_img), (10,10), (100,100))
       
        self.option = button_click_event(event, self.menu_assets)

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

        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.set_volume(0.1) 
        pygame.mixer.music.play(-1)
        
        

