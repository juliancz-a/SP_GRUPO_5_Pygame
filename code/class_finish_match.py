import pygame
from class_box import Box
from constantes import *
from class_image import *
from assets_cfg import *

from draw_functions import *
class FinishMatch:
    def __init__(self, surface:pygame.Surface, match, lista, score) -> None:
        self.surface = surface
        self.match = match
        self.lista = lista
        self.background = Image(r"code\data\img\play_bg(blur).png", (0,0), self.surface.get_size())
        self.music = FINISH_MATCH_BACKGROUND

        self.score = score
        self.continue_button = FINISH_MATCH_LISTA[0]["box"]
        self.finish_button = FINISH_MATCH_LISTA[1]["box"]
        self.score_text = Box((230, 100), (400,150))

        self.box_list = [self.continue_button, self.finish_button]
        self.lista_cfg = FINISH_MATCH_LISTA

        self.option = None

    def render(self):
        set_buttons_colors(self.box_list, self.lista_cfg)
        self.score_text.rectangulo.centerx = self.surface.get_width() // 2

        continuar = False
        finalizar = False

        if continuar:
            return "play"
        elif finalizar:
            return "scoreboard"
    
               
        self.surface.fill("black")
            
        self.background.draw_image(self.surface)
        self.score_text.draw_text(self.surface, f"Tu puntaje total es: {self.score}", "white", FUENTE_1, 50, "border", 3, "black", True)
        draw_boxes(self.surface, self.box_list, self.lista_cfg)
        draw_boxes_text(self.surface, self.box_list, self.lista_cfg)
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

        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)