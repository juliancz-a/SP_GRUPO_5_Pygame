import pygame
from game_tools.class_image import *
from data.config.assets_cfg import *
from game_tools.draw_functions import *


mucho_texto = (
"Pop the Card es un juego de descubrir las palabras. Se te daran 6 letras, con"
"las cuales deberás\nformar la mayor cantidad de palabras posibles, sin repetirlas letras."
"\n\nLas palabras a encontrar estarán compuestas de 3, 4, 5 y 6 caracteres, y cada"
"partida durará 90\nsegundos, debiendo jugar por lo menos 3 partidas para poder guardar tu puntaje.\n"
"Además, contás con los botones SHUFFLE, que cambia el lugar de las letras, CLEAR, para deshacer\n"
"el orden de las cartas que elegiste, y el comodín, el cual elige una letra aleatoria, y muestra "
"donde\nse encuentra la misma en cada palabra."
)

# fuente = pygame.font.Font(r"code\data\fonts\vinque rg.otf", 28)
# comodin = pygame.image.load(r"code\data\img\spell_comodin_hover.png")
# clear = pygame.image.load(r"code\data\img\clear_button.png")
# shuffle = pygame.image.load(r"code\data\img\shuffle_button.png")
# background = pygame.image.load(r"code\data\img\Grimoire_blur.jpg")
# background_scale = pygame.transform.scale(background, (1280, 720))

# dict_images = {
#     "comodin": {"image": [comodin, (100, 480)],
#                 "text": "Comodin",
#                 "text_pos": (220, 510)},
#     "clear": {"image": [clear, (400, 460)],
#               "text": 'Botón "CLEAR"',
#               "text_pos": (500, 480)},
#     "shuffle": {"image": [shuffle, (400, 550)],
#                 "text": 'Botón "SHUFFLE"',
#                 "text_pos": (500, 570)},
# }

# def blit_instructions(screen, diccionario):
#     for key in diccionario.keys():
#         screen.blit(*diccionario[key]["image"])
#         screen.blit(fuente.render(diccionario[key]["text"], True, "white"), diccionario[key]["text_pos"])

def render_multi_line(surface, text, x, y, font_size):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        box_line = Box((x, y + font_size * i), (50,1200))
        box_line.draw_text(surface, line, "white", FUENTE_1, font_size, "shadow", 2, "black")

class Help:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.menu_button = HELP_ASSETS[0]["box"]

        self.background = Image(HELP_BACKGROUND, (0,0), (1280,720))
        self.comodin_button_img = Image (COMODIN, (100, 480), (100, 150))
        self.clear_button_img = Image (r"code\data\img\clear_button.png" (400, 460), (100, 150))
        self.shuffle_button_img = Image (r"code\data\img\shuffle_button.png", (400, 550), (100, 150))

        self.config_list = HELP_ASSETS
        self.box_list  = [self.menu_button]
        self.image_list = [self.background, self.comodin_button_img, self.clear_button_img, self.shuffle_button_img]

    def render(self):

        self.surface.fill("aquamarine4")
        
        draw_assets(self.surface, self.box_list, self.image_list, self.config_list)

        render_multi_line(self.surface, mucho_texto, 10, 10, 50)

        pygame.display.update()

    def handle_event (self):
        pass

    def update(self):
        pass
    def set_music(self):
        pass