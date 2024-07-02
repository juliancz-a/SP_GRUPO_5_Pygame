import pygame
from game_tools.class_box import Box
from constantes import *
from game_tools.class_image import *
from data.config.assets_cfg import *

from game_tools.draw_functions import *
class FinishMatch:
    def __init__(self, surface:pygame.Surface, match, score, finish_match_assets) -> None:
        self.surface = surface
        self.match = match
        self.music = self.set_music()

        self.assets_config = finish_match_assets
        self.assets = self.init_assets()

        self.score = score
        self.option = None

    def init_assets(self):
        assets = {"continue_button" : self.assets_config[0]["box"],
                  "finish_button" : self.assets_config[1]["box"],
                  "score_text" : self.assets_config[2]["box"],
                  "background" : self.assets_config[3]["image"]}

        return assets
    
    def render(self):
        buttons = [self.assets["continue_button"], self.assets["finish_button"]]
        set_buttons_colors(buttons, self.assets_config)

        self.assets["score_text"].rectangulo.centerx = self.surface.get_width() // 2

        self.surface.fill("black")
            
        draw_assets(self.surface, buttons, [self.assets["background"]], self.assets_config)

        if self.match > 2:
            self.assets["finish_button"].draw_box(self.surface)
            self.assets["finish_button"].draw_text(self.surface, "Definir puntaje", "white", FUENTE_1, 30, "border", 2, "black", True)
            
        self.assets["score_text"].draw_text(self.surface, f"Tu puntaje total hasta el momento es: {self.score}", "white", FUENTE_1, 50, "border", 3, "black", True)

        pygame.display.update()

    def handle_event(self, event):
        if self.assets["continue_button"].interaction(event):
            self.option = 0
       
        if self.match > 2:
            if self.assets["finish_button"].interaction(event):
                self.option = 1
     
    def update(self):
        selection = None

        match self.option:
            case 0:
                selection = "play"
            case 1:
                selection = "setscore"

        return selection

    def set_music(self):

        pygame.mixer.music.load(FINISH_MATCH_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.01)