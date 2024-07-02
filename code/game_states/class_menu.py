import pygame

from constantes import *
from game_tools.scoreboard import Scoreboard
from game_tools.draw_functions import *
from game_tools.event_handle import *
from game_tools.extra_functions import *

class Menu:

    def __init__(self, surface:pygame.Surface, lista_jugadores, menu_assets, volume) -> None:

        self.surface = surface

        self.assets_config = menu_assets
        self.assets = self.init_assets()
        
        self.lista_jugadores = lista_jugadores
        self.volume = volume

        self.option = None

        self.music = self.set_music()
    
    def init_assets (self):
        assets = { "play_button" : self.assets_config[0]["box"],
                "help_button" : self.assets_config[1]["box"],
                "exit_button" : self.assets_config[2]["box"],
                "title" : self.assets_config[3]["box"],
                "volume_button" : self.assets_config[4]["image"],
                "background" : self.assets_config[5]["image"],
                "chains" : self.assets_config[6]["image"]
                }
    
        return assets
    
    def render(self):
 

        images = [self.assets["background"], self.assets["chains"], self.assets["volume_button"]]
        box_list = [self.assets["play_button"], self.assets["help_button"], self.assets["exit_button"], self.assets["title"]]

        set_buttons_colors(box_list, self.assets_config)
            
        self.surface.fill("white")
        
        draw_assets(self.surface, box_list , images, self.assets_config)
        Scoreboard(FUENTE_1, self.surface, self.lista_jugadores, (850,200)).draw()

        pygame.display.update()
  
    def handle_event (self, event):
      
        
        if self.assets["volume_button"].image_box.interaction(event):
            self.volume = not self.volume
    
        self.option = button_click_event(event, self.assets_config)

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

    def update_audio(self):

        if self.volume:
            pygame.mixer.music.set_volume(0.1)
            self.assets["volume_button"] = Image(VOLUME_BUTTON, (10, 10), (60,60))       
        else:
            pygame.mixer.music.set_volume(0)
            self.assets["volume_button"] = Image(  VOLUME_MUTE_BUTTON, (10, 10), (60,60))     


        return self.volume    
    
    def set_music(self):
        
        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.play(-1)
        

