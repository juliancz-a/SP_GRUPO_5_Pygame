import pygame

from constantes import *
from game_tools.scoreboard import Scoreboard
from game_tools.draw_functions import *
from game_tools.event_handle import *
from game_tools.extra_functions import *

class Menu:

    def __init__(self, surface: pygame.Surface, lista_jugadores: list, 
                menu_assets: list[dict], volume: bool) -> None:
        """Escena menú.

        Args:
            surface (pygame.Surface): Superficie sobre la cual se renderizarán los 
            recursos de la escena.
            lista_jugadores (list): Lista de jugadores con sus datos, para la 
            renderización del Scoreboard
            menu_assets (list): Configuración de los assets utilizados por la escena
            volume (bool): Booleano que indica si se desea reproducir audio en la escena.
        """

        self.surface = surface

        self.assets_config = menu_assets
        self.assets = self.init_assets()
        
        self.lista_jugadores = lista_jugadores
        self.volume = volume

        self.option = None

        self.music = self.set_music()
    
    def init_assets (self) -> dict:
        """Inicializar los recursos de la escena.
        Returns: 
            dict: Recursos con su correspondiente configuración"""
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
        """Renderizar los elementos de la escena menú. Botones, fondo y titulo """

        images = [self.assets["background"], self.assets["chains"], 
                    self.assets["volume_button"]]
        box_list = [self.assets["play_button"], self.assets["help_button"], 
                    self.assets["exit_button"], self.assets["title"]]

        set_buttons_colors(box_list, self.assets_config)
            
        self.surface.fill("white")
        
        draw_assets(self.surface, box_list , images, self.assets_config)
        Scoreboard(FUENTE_1, self.surface, self.lista_jugadores, (850,200)).draw_scoreboard(7)

        pygame.display.update()
  
    def handle_event (self, event: pygame.event.Event):
        """Manejar eventos necesarios para la interacción con la interfaz
        Args:
            event (pygame.event.Event): Evento capturado"""
        
        if self.assets["volume_button"].image_box.interaction(event):
            self.volume = not self.volume
    
        self.option = get_option_selected(event, self.assets_config)

    def update (self) -> str:
        """Actualizar la escena en caso de haberse seleccionado una opción
        Returns:
            str: Nueva escena"""
            
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
        """
        Actualizar el volumen de la música según el estado de la atributo 'volume'
        
         Returns:
            bool: Estado del volumen actual."""

        if self.volume:
            pygame.mixer.music.set_volume(0.1)
            self.assets["volume_button"] = Image(VOLUME_BUTTON, (10, 10), (60,60))       
        else:
            pygame.mixer.music.set_volume(0)
            self.assets["volume_button"] = Image(VOLUME_MUTE_BUTTON, (10, 10), (60,60))     


        return self.volume    
    
    def set_music(self):
        """Carga la música, y la reproduce en un loop infinito."""
        
        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.play(-1)
        

