import pygame
from game_tools.class_image import *
from data.config.assets_cfg import *
from game_tools.draw_functions import *
from game_tools.event_handle import *

mucho_texto = (
"Pop the Card es un juego de descubrir las palabras. Se te daran 6 letras, con"
"las cuales deberás\nformar la mayor cantidad de palabras posibles, sin repetirlas letras."
"\nLas palabras a encontrar estarán compuestas de 3, 4, 5 y 6 caracteres, y cada"
"partida durará 90 segundos,\ndebiendo jugar por lo menos 3 partidas para poder guardar tu puntaje.\n"
"Además, contás con los siguientes botones durante una partida:\n"
" -> SHUFFLE, que cambia el lugar de las letras.\n -> CLEAR, para deshacer"
"el orden de las cartas que elegiste.\n -> Un comodín (libro mágico), el cual elige una letra aleatoria, y muestra "
"donde se encuentra la misma en cada palabra.")

def render_multi_line(surface, text, x, y, font_size):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        box_line = Box((x, y + font_size // 3 * i), (50,1200))
        box_line.draw_text(surface, line, "white", FUENTE_1, font_size, "shadow", 2, "black")

class Help:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.menu_button = HELP_ASSETS[0]["box"]

        self.background = Image(HELP_BACKGROUND, (0,0), (1280,720))

        self.comodin_button_img = Image (COMODIN, (100, 480), (100, 100))
        self.clear_button_img = Image (r"code\data\img\clear_button.png", (600, 450), (160, 100))
        self.shuffle_button_img = Image (r"code\data\img\shuffle_button.png", (400, 450), (160, 100))

        self.config_list = HELP_ASSETS
        self.box_list  = [self.menu_button]
        self.image_list = [self.background, self.comodin_button_img, self.clear_button_img, self.shuffle_button_img]

        self.option = None

    def render(self):

        set_buttons_colors(self.box_list, self.config_list)

        self.surface.fill("aquamarine4")
        
        draw_assets(self.surface, self.box_list, self.image_list, self.config_list)

        render_multi_line(self.surface, mucho_texto, 10, 10, 150)

        pygame.display.update()

    def handle_event (self, event):
        self.option = button_click_event(event, self.config_list)

    def update(self):
        selection = None

        match self.option:
            case 0:
                selection = "menu"
        
        return selection
    def set_music(self):
        pass