import pygame
from class_box import Box
from constantes import *

from data.config.config import *


class Scoreboard:
    def __init__(self, wh, surface:pygame.Surface, match, lista, score, lista_jugadores) -> None:
        self.lista_jugadores = lista_jugadores
        self.surface = surface
        self.original_wh = wh
        self.match = match
        self.lista = lista

        self.score = score

        self.score_text = Box(wh, (230, 410), (400,150))
        self.input_box = Box(wh, (500, 100), (275,50))
        self.text =  Box(wh, (self.input_box.rectangulo.x + 5, self.input_box.rectangulo.y + 5), (200,20))
        self.submit_button = Box(wh, (self.input_box.rectangulo.centerx, 150), (275,50))

    def render(self):
        text = ""
        activo = False
        submit = False
        max_chars = 10
        self.input_box.set_color("white", "red", "grey1")
        self.submit_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")

        while True:
            if submit:
                self.lista_jugadores.append({"nombre" : text , "puntos" : self.score, "partidas" : self.match})
                update_score(r"code\data\config\scoreboard.csv", self.lista_jugadores)
                return "menu", self.original_wh

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.rectangulo.collidepoint(event.pos):
                        activo = not activo


                elif event.type == pygame.KEYDOWN:
                    if activo:
                        if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif event.key == pygame.K_ESCAPE:
                            text = ""
                        elif max_chars > len(text):
                            text += event.unicode
                if len(text) > 3:
                    submit = self.submit_button.interaction(event)
                
            self.surface.fill("red")

            self.score_text.draw_text(self.surface, f"Tu puntaje final es: {self.score}", "white", FUENTE_1, center=True, font_size=20)
            self.input_box.draw_box(self.surface)
            if len(text) > 3:
                self.submit_button.draw_box(self.surface)
                self.submit_button.draw_text(self.surface, "Ok", "white", FUENTE_1, font_size=60)
            self.text.draw_text(self.surface, text, "black", FUENTE_1, font_size=60)

            pygame.display.update()
