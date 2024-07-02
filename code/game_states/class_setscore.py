import pygame
from game_tools.class_box import Box
from constantes import *

from data.config.config import *
from game_tools.draw_functions import *
from game_tools.event_handle import *
from game_tools.extra_functions import *

class SetScore:
    def __init__(self, surface:pygame.Surface, match, score, lista_jugadores, setscore_assets) -> None:
        self.surface = surface
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
        assets = {
            "input_box" : self.assets_config[0]["box"],
            "submit_button" : self.assets_config[1]["box"],
            "game_over_title" : self.assets_config[2]["box"],
            "nickname" : self.assets_config[3]["box"],
            "background" : self.assets_config[4]["image"]
        }

        return assets
    
    def render(self):

        box_list = [self.assets["input_box"], self.assets["submit_button"], self.assets["game_over_title"]]
        self.assets["game_over_title"].rectangulo.centerx = self.surface.get_width() // 2

        set_buttons_colors(box_list, self.assets_config)
        

        self.surface.fill("black")

        draw_assets(self.surface, box_list, [self.assets["background"]], self.assets_config)

        if len(self.nickname_text) > 3:
            self.assets["submit_button"].draw_box(self.surface, 5, 5)
            self.assets["submit_button"].draw_text(self.surface, "Listo", "grey90", FUENTE_1, 40, center=True)
        
        if len(self.nickname_text) == 0:
            self.assets["nickname"].draw_text(self.surface, " Nombre:", "gray59", FUENTE_1, 60)
        else:
            self.assets["nickname"].draw_text(self.surface, self.nickname_text, "black", FUENTE_1, 60)

        render_multi_line(self.surface, self.score_text, 610, 250, 200, center_text= True)

        pygame.display.update()
    
    def handle_event (self, event):
        submit = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.assets["input_box"].rectangulo.collidepoint(event.pos):
                self.activo = not self.activo

        self.nickname_text = handle_input_event(self.activo, event, self.nickname_text, 10)

        if len(self.nickname_text) > 3:
            submit = self.assets["submit_button"].interaction(event)
        
        if submit:
            self.option = 0

    def update (self):
        selection = None

        match self.option:
            case 0:
                self.lista_jugadores.append({"nombre" : self.nickname_text , "puntos" : self.score_promedio, "partidas" : self.match})
                
                ordenar_elementos(self.lista_jugadores, 2, "puntos")

                update_score(r"code\data\config\scoreboard.csv", self.lista_jugadores)
                selection = "menu"

        return selection

    def set_music(self):
    
        pygame.mixer.music.load(r"code\data\sound\566579__bainmack__chime_song_mellow_chill_short2.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
