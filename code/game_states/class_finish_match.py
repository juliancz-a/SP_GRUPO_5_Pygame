import pygame
from game_tools.class_box import Box
from constantes import *
from game_tools.class_image import *
from data.config.assets_cfg import *

from game_tools.draw_functions import *
class FinishMatch:
    def __init__(self, surface:pygame.Surface, match, lista, score) -> None:
        self.surface = surface
        self.match = match
        self.lista = lista
        self.background = Image(r"code\data\img\play_bg(blur).png", (0,0), self.surface.get_size())
        self.music = self.set_music()

        self.score = score
        self.continue_button = FINISH_MATCH_ASSETS[0]["box"]
        self.finish_button = FINISH_MATCH_ASSETS[1]["box"]
        self.score_text = Box((230, 100), (400,150))

        self.box_list = [self.continue_button]
        self.image_list = [self.background]

        self.lista_cfg = FINISH_MATCH_ASSETS

        
        self.option = None

    def render(self):
        set_buttons_colors(self.box_list, self.lista_cfg)
        self.finish_button.set_color(*FINISH_MATCH_ASSETS[1]["colors"])

        self.score_text.rectangulo.centerx = self.surface.get_width() // 2

        self.surface.fill("black")
            
        draw_assets(self.surface, self.box_list, self.image_list, self.lista_cfg)

        if self.match > 1:
            self.finish_button.draw_box(self.surface)
            self.finish_button.draw_text(self.surface, "Definir puntaje", "white", FUENTE_1, 30, "border", 2, "black", True)
            
        self.score_text.draw_text(self.surface, f"Tu puntaje total hasta el momento es: {self.score}", "white", FUENTE_1, 50, "border", 3, "black", True)

        pygame.display.update()

    def handle_event(self, event):
        if self.continue_button.interaction(event):
            self.option = 0
       
        if self.match > 1:
            if self.finish_button.interaction(event):
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

        pygame.mixer.music.load(FINISH_MATCH_BACKGROUND)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.01)