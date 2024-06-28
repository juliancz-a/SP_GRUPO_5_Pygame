import pygame
from class_box import Box
from constantes import *

from data.config.config import *


class SetScore:
    def __init__(self, surface:pygame.Surface, match, score, lista_jugadores) -> None:
        self.surface = surface

        self.lista_jugadores = lista_jugadores
        
        self.match = match
        self.score = score

        self.title = Box((230, 20), (400,150))
        self.score_text = Box((230, 100), (400,150))
        self.input_box = Box((650, 500), (275,50))
        self.text =  Box((self.input_box.rectangulo.x + 5, self.input_box.rectangulo.y + 2), (200,20))
        self.submit_button = Box((self.input_box.rectangulo.centerx - 275 // 2, self.input_box.rectangulo.y + 75), (275,50))

        self.background = pygame.image.load(r"code\data\img\Runes 3.png")

    def render(self):
        text = ""
        activo = False
        submit = False

        pygame.transform.scale(self.background, self.surface.get_size())

        self.title.rectangulo.centerx = self.surface.get_width() // 2
        self.score_text.rectangulo.centerx = self.surface.get_width() // 2
        self.input_box.set_color("white", "red", "grey1")
        self.submit_button.set_color("mediumpurple4", "mediumpurple3", "mediumpurple3")

        while True:
            if submit:
                self.lista_jugadores.append({"nombre" : text , "puntos" : self.score, "partidas" : self.match})
                
                ordenar_elementos(self.lista_jugadores, "puntos", 2)

                update_score(r"code\data\config\scoreboard.csv", self.lista_jugadores)
                return "menu"
            
            event = self.write_name(text, activo)
            if event != False:
                text = event[0]
                activo = event[1]
                submit = event[2]
            else:
                return False
        
            self.blit_buttons(text)

            pygame.display.update()

    def write_name(self, text, activo) -> tuple|bool:
        max_chars = 10
        submit = False
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

        return (text, activo, submit)

    def blit_buttons(self, nickname):
        self.surface.fill("red")
        self.surface.blit(self.background, (0,0))

        self.score_text.draw_text(self.surface, f"Tu puntaje final es de {self.score} puntos",
                                "white", FUENTE_1, center=True, font_size=45,border=True, border_thickness=1)
        
        self.input_box.draw_box(self.surface, border_radius= 25)

        self.title.draw_text(self.surface, f"Registra tu nombre", "white", FUENTE_1, center=True,
                            font_size=60, border=True, border_thickness=1)
        
        if len(nickname) > 3:
            self.submit_button.draw_box(self.surface, border_radius= 25)
            self.submit_button.draw_text(self.surface, "Listo", "grey90", FUENTE_1, font_size=40, center=True)
        
        if len(nickname) == 0:
            self.text.draw_text(self.surface, " Nombre:", "gray59", FUENTE_1, font_size=60)
        else:
            self.text.draw_text(self.surface, nickname, "black", FUENTE_1, font_size=60)

    
def ordenar_elementos (list:list[dict], key: str, orden:int):

    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            match orden:
                case 1:
                    if list[i][key] >= list[j][key]:
                            swap(list, i, j)
                case 2:
                    if list[i][key] <= list[j][key]:
                        swap(list, i, j)

def swap(list:list[dict], a:int, b:int):
    aux = list[a]
    list[a] = list[b]
    list[b] = aux
