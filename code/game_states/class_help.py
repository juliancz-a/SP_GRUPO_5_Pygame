import pygame
from game_tools.class_image import *
# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Botones y Colisiones")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir botones como rectángulos
button1 = pygame.Rect(100, 500, 150, 50)
button2 = pygame.Rect(300, 300, 150, 50)
mucho_texto = (
"Pop the Card es un juego de descubrir las palabras. Se te daran 6 letras, con"
"las cuales deberás\nformar la mayor cantidad de palabras posibles, sin repetirlas letras."
"\n\nLas palabras a encontrar estarán compuestas de 3, 4, 5 y 6 caracteres, y cada"
"partida durará 90\nsegundos, debiendo jugar por lo menos 3 partidas para poder guardar tu puntaje.\n"
"Además, contás con los botones SHUFFLE, que cambia el lugar de las letras, CLEAR, para deshacer\n"
"el orden de las cartas que elegiste, y el comodín, el cual elige una letra aleatoria, y muestra "
"donde\nse encuentra la misma en cada palabra."
)

fuente = pygame.font.Font(r"code\data\fonts\vinque rg.otf", 28)
comodin = pygame.image.load(r"code\data\img\spell_comodin_hover.png")
clear = pygame.image.load(r"code\data\img\clear_button.png")
shuffle = pygame.image.load(r"code\data\img\shuffle_button.png")
background = pygame.image.load(r"code\data\img\Grimoire_blur.jpg")
background_scale = pygame.transform.scale(background, (1280, 720))

dict_images = {
    "comodin": {"image": [comodin, (100, 480)],
                "text": "Comodin",
                "text_pos": (220, 510)},
    "clear": {"image": [clear, (400, 460)],
              "text": 'Botón "CLEAR"',
              "text_pos": (500, 480)},
    "shuffle": {"image": [shuffle, (400, 550)],
                "text": 'Botón "SHUFFLE"',
                "text_pos": (500, 570)},
}

def blit_instructions(screen, diccionario):
    screen.blit(background_scale, (0, 0))
    for key in diccionario.keys():
        screen.blit(*diccionario[key]["image"])
        screen.blit(fuente.render(diccionario[key]["text"], True, "white"), diccionario[key]["text_pos"])

def render_multi_line(screen, text, x, y, font_size, color):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        screen.blit(fuente.render(line, 0, color), (x, (y + font_size * i)))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("aquamarine4")

    blit_instructions(screen, dict_images)

    render_multi_line(screen, mucho_texto, 10, 10, 50, "white")

    pygame.display.flip()


pygame.quit()


class Help:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.background = Image

    def render(self):
        pass

    def handle_event (self):
        pass

    def update(self):
        pass
    def set_music(self):
        pass