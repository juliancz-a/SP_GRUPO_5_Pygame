import pygame
from game_tools.class_box import Box
from constantes import *

from data.config.config import *
from game_tools.draw_functions import *
from game_tools.event_handle import *
from game_tools.extra_functions import *

class SetScore:
    def __init__(self, surface:pygame.Surface, match:int, score:int, lista_jugadores:list, setscore_assets:list, volume:bool) -> None:
        """Escena SetScore

        Args:
            surface (pygame.Surface): Superficie sobre la cual se renderizarán los recursos de la escena.
            match (int): Numero de partidas jugadas totales.
            score (int):  Puntaje de todas las partidas jugadas.
            lista_jugadores (list): Lista de jugadores con sus datos, para agregar un nuevo jugador.
            setscore_assets (list): Configuración de los assets utilizados por la escena
            volume (bool):  Booleano que indica si se desea reproducir audio en la escena.
        """
        self.surface = surface
        self.volume = volume
        self.assets_config = setscore_assets
        self.assets = self.init_assets()

        self.lista_jugadores = lista_jugadores
        self.match = match

        self.score = score
        self.score_promedio = operacion(score, match, lambda x, y: x // y)
        self.score_text = (f"Tu puntaje total es: {score}\nLa cantidad de partidas jugadas es: {match}\nTu puntaje final es de: {self.score_promedio}")

        self.nickname_text = ""

        self.music = self.set_music()

        self.option = None
        self.activo = False

    def init_assets(self):
        """Inicializar los recursos de la escena
        Returns: 
            dict: Recursos con su correspondiente configuración"""
        assets = {
            "input_box" : self.assets_config[0]["box"],
            "submit_button" : self.assets_config[1]["box"],
            "game_over_title" : self.assets_config[2]["box"],
            "nickname" : self.assets_config[3]["box"],
            "volume_button" : self.assets_config[4]["image"],
            "background" : self.assets_config[5]["image"]
        }

        return assets
    
    def render(self):
        """Renderizar los elementos de la escena SetScore. Botones, fondo y titulo """

        box_list = [self.assets["input_box"], self.assets["submit_button"], self.assets["game_over_title"]]
        images = [self.assets["background"], self.assets["volume_button"]]
        self.assets["game_over_title"].rectangulo.centerx = self.surface.get_width() // 2

        set_buttons_colors(box_list, self.assets_config)
        
        self.surface.fill("black")

        draw_assets(self.surface, box_list, images, self.assets_config)

        if len(self.nickname_text) > 3:
            self.assets["submit_button"].draw_box(self.surface, 5, 5)
            self.assets["submit_button"].draw_text(self.surface, "Listo", "grey90", FUENTE_1, 40, center=True)
        
        if len(self.nickname_text) == 0:
            self.assets["nickname"].draw_text(self.surface, " Nombre:", "gray59", FUENTE_1, 60)
        else:
            self.assets["nickname"].draw_text(self.surface, self.nickname_text, "black", FUENTE_1, 60)

        render_multi_line(self.surface, self.score_text, 610, 250, 200, center_text= True)

        pygame.display.update()
    
    def handle_event (self, event: pygame.event.Event):
        """Manejar eventos necesarios para la interacción con la interfaz
        Args:
            event (pygame.event.Event): Evento capturado"""

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.assets["input_box"].rectangulo.collidepoint(event.pos):
                self.activo = not self.activo
        
        elif self.assets["volume_button"].image_box.interaction(event):
            self.volume = not self.volume

        self.nickname_text = handle_input_event(self.activo, event, self.nickname_text, 10)

        if len(self.nickname_text) > 3:
            if self.assets["submit_button"].interaction(event):
                self.option = 0

    def update (self):
        """Actualizar la escena en caso de haberse seleccionado una opción
        Returns:
            str: Nueva escena"""
        selection = None

        match self.option:
            case 0:
                self.lista_jugadores.append({"nombre" : self.nickname_text , "puntos" : self.score_promedio, "partidas" : self.match})
                
                ordenar_elementos(self.lista_jugadores, 2, "puntos")

                update_score(SCOREBOARD_PATH, self.lista_jugadores)
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
            self.assets["volume_button"] = Image(VOLUME_BUTTON, (10, 10), (60,60))       
        else:
            pygame.mixer.music.set_volume(0)
            self.assets["volume_button"] = Image(VOLUME_MUTE_BUTTON, (10, 10), (60,60))       

        return self.volume    

    def set_music(self):
        """Carga la música, y la reproduce en un loop infinito."""
    
        pygame.mixer.music.load(r"code\data\sound\566579__bainmack__chime_song_mellow_chill_short2.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
    