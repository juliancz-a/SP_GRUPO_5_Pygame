import pygame
from game_tools.class_image import *
from game_tools.draw_functions import *
from game_tools.event_handle import *
from game_tools.extra_functions import *

class Help:
    def __init__(self, surface: pygame.Surface, help_assets: list, volume: bool) -> None:
        """Escena How to Play (Help)

        Args:
            surface (pygame.Surface): Superficie sobre la cual se renderizarán los recursos de la escena.
            help_assets (list): Configuración de los assets utilizados por la escena
            volume (bool): Booleano que indica si se desea reproducir audio en la escena.
        """
        self.surface = surface
        self.volume = volume

        self.assets_config = help_assets
        self.assets = self.init_assets()
        
        self.option = None

    def init_assets(self):
        """Inicializar los recursos de la escena.
        Returns: 
            dict: Recursos con su correspondiente configuración"""
        assets = {  "menu_button" : self.assets_config[0]["box"],
                    "comodin_img" : self.assets_config[1]["image"],
                    "shuffle_img" : self.assets_config[2]["image"],
                    "clear_img" : self.assets_config[3]["image"],
                    "volume_button" : self.assets_config[4]["image"],
                    "help_background" : self.assets_config[5]["image"]
                  }

        return assets
    
    def render(self):
        """Renderizar los elementos de la escena Play. Botones, fondo, titulo, texto, imagenes"""
        images = [self.assets["help_background"], self.assets["comodin_img"], 
                self.assets["shuffle_img"], self.assets["clear_img"], 
                self.assets["volume_button"]]

        set_buttons_colors([self.assets["menu_button"]], self.assets_config)

        self.surface.fill("aquamarine4")
        
        draw_assets(self.surface, [self.assets["menu_button"]],
                    images, self.assets_config)

        render_multi_line(self.surface, HELP_TEXT, 620, 10, 140, center_text= True)

        pygame.display.update()

    def handle_event (self, event: pygame.event.Event):
        """Manejar eventos necesarios para la interacción con la interfaz
        Args:
            event (pygame.event.Event): Evento capturado"""
        if self.assets["volume_button"].image_box.interaction(event):
            self.volume = not self.volume

        self.option = get_option_selected(event, self.assets_config)

    def update(self):
        """Actualizar la escena en caso de haberse seleccionado una opción
        Returns:
            str: Nueva escena"""
        selection = None

        match self.option:
            case 0:
                selection = "menu"
        
        return selection

    def update_audio(self):
        """
        Actualizar el volumen de la música según el estado de la atributo 'volume'
        
        Returns:
            bool: Estado del volumen actual.
        """

        if self.volume:
            pygame.mixer.music.set_volume(0.1)
            self.assets["volume_button"] = Image(VOLUME_BUTTON, (10, 650), (60,60))
        else:
            pygame.mixer.music.set_volume(0)
            self.assets["volume_button"] = Image(VOLUME_MUTE_BUTTON, (10, 650), (60,60))

        return self.volume    

    
    