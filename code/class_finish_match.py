import pygame
from class_box import Box
from constantes import *

class FinishMatch:
    def __init__(self, surface:pygame.Surface, match, lista, score) -> None:
        self.surface = surface
        self.match = match
        self.lista = lista
        self.background = pygame.image.load(r"code\data\img\play_bg(blur).png")
        self.music = FINISH_MATCH_BACKGROUND

        self.score = score
        self.score_text = Box( (230, 100), (400,150))
        self.finish_button = Box( (self.surface.get_width() // 6, self.surface.get_height() // 2), (400,150))
        self.continue_button = Box( (self.surface.get_width() // 2, self.surface.get_height() // 2), (400,150))

    def render(self):
        self.continue_button.set_color("violetred3", BORDE_BOX, "violetred4")
        self.finish_button.set_color("violetred3", BORDE_BOX, "violetred4")
        pygame.transform.scale(self.background, (self.surface.get_size()))

        self.score_text.rectangulo.centerx = self.surface.get_width() // 2

        continuar = False
        finalizar = False

        FinishMatch.set_music(self)

        while True:
            if continuar:
                return "play"
            elif finalizar:
                return "scoreboard"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                continuar = self.continue_button.interaction(event)
                if self.match > 1:
                    finalizar = self.finish_button.interaction(event)
                
            self.surface.fill("black")
            self.surface.blit(self.background, (0,0))
            self.score_text.draw_text(self.surface, f"Tu puntaje total es: {self.score}", "white", FUENTE_1, center=True, font_size=50, border=True, border_thickness=3)
            self.continue_button.draw_box(self.surface)
            self.continue_button.draw_text(self.surface, "Continuar", "white", FUENTE_1, center=True, font_size=60, border=True, border_thickness=2)
            if self.match > 1:
                self.finish_button.draw_box(self.surface)
                self.finish_button.draw_text(self.surface, "Definir puntaje", "white", FUENTE_1, center=True, font_size=40, border=True, border_thickness=2)

            pygame.display.update()

    def set_music(self):
        if self.music != None:
            pygame.mixer.music.load(self.music)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)