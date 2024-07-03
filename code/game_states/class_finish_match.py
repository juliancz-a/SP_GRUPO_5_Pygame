import pygame
from game_tools.class_box import Box
from constantes import *
from game_tools.class_image import *
from data.config.assets_cfg import *

from game_tools.draw_functions import *
class FinishMatch:
    def __init__(self, surface: pygame.Surface, match: int, score: int, 
                finish_match_assets: list, volume: bool) -> None:
        """Escena FinishMatch (Escena ejecutada entre partidas)

        Args:
            surface (pygame.Surface): Superficie sobre la cual se renderizarán los 
            recursos de la escena.
            match (int): Numero de partidas jugadas en una misma instancia de juego.
            score (int): Puntaje acumulado hasta el momento.
            finish_match_assets (list): Configuración de los assets utilizados por la escena
            volume (bool): Booleano que indica si se desea reproducir audio en la escena.
        """
        self.surface = surface
        self.match = match
        self.music = self.set_music()
        self.volume = volume

        self.assets_config = finish_match_assets
        self.assets = self.init_assets()

        self.score = score
        self.option = None

    def init_assets(self):
        """Inicializar los recursos de la escena.
        Returns: 
            dict: Recursos con su correspondiente configuración"""
        assets = {"continue_button" : self.assets_config[0]["box"],
                  "finish_button" : self.assets_config[1]["box"],
                  "score_text" : self.assets_config[2]["box"],
                  "volume_button" : self.assets_config[3]["image"],
                  "background" : self.assets_config[4]["image"]}

        return assets
    
    def render(self):
        """Renderizar los elementos de la escena FinishMatch. Botones, fondo y titulo.
        """
        buttons = [self.assets["continue_button"], self.assets["finish_button"]]
        images = [self.assets["background"], self.assets["volume_button"]]
        set_buttons_colors(buttons, self.assets_config)

        self.assets["score_text"].rectangulo.centerx = self.surface.get_width() // 2

        self.surface.fill("black")
            
        draw_assets(self.surface, buttons, images, self.assets_config)

        if self.match > 2:
            self.assets["finish_button"].draw_box(self.surface)
            self.assets["finish_button"].draw_text(self.surface, "Definir puntaje", 
                                                "white", FUENTE_1, 30, "border", 
                                                2, "black", True)
            
        self.assets["score_text"].draw_text(self.surface, 
                                            f"Tu puntaje total hasta el momento es: {self.score}", 
                                            "white", FUENTE_1, 50, "border", 3, "black", True)

        pygame.display.update()

    def handle_event(self, event:pygame.event.Event):
        """Manejar eventos necesarios para la interacción con la interfaz
        Args:
            event (pygame.event.Event): Evento capturado"""
        if self.assets["continue_button"].interaction(event):
            self.option = 0
        
        elif self.assets["volume_button"].image_box.interaction(event):
            self.volume = not self.volume
       
        if self.match > 2:
            if self.assets["finish_button"].interaction(event):
                self.option = 1
     
    def update(self):
        """Actualizar la escena en caso de haberse seleccionado una opción
        Returns:
            str: Nueva escena"""
        selection = None

        match self.option:
            case 0:
                selection = "play"
            case 1:
                selection = "setscore"

        return selection

    def update_audio(self):
        """Actualizar el volumen de la música según el estado de la atributo 'volume'
        
        Returns:
            bool: Estado del volumen actual."""
        if self.volume:
            pygame.mixer.music.set_volume(0.1)
            self.assets["volume_button"] = Image(VOLUME_BUTTON, (10, 10), (60,60)) 
        else:
            pygame.mixer.music.set_volume(0)
            self.assets["volume_button"] = Image(  VOLUME_MUTE_BUTTON, 
                                                (10, 10), (60,60))  

        return self.volume    
    

    def set_music(self):
        """Carga la música, y la reproduce en un loop infinito."""
        pygame.mixer.music.load(FINISH_MATCH_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.01)