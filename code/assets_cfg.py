from constantes import *
from class_box import Box

menu_salir = {
              "box": Box((1280, 720), (100,540), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, True, 5],
              "text": ["Salir", LETRAS_2, FUENTE_1, 60, True, 1, BORDE_2, True]
              }

menu_jugar = {
              "box": Box((1280, 720), (100,300), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, True, 5],
              "text": ["Jugar", LETRAS_2, FUENTE_1, 60, True, 1, BORDE_2, True]
              }

menu_options = {
              "box": Box((1280, 720), (100,420), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, True, 5],
              "text": ["Opciones", LETRAS_2, FUENTE_1, 60, True, 1, BORDE_2, True]
              }


MENU_LISTA = [menu_jugar, menu_salir, menu_options]

print(menu_jugar["colors"][0], menu_jugar["colors"][1], menu_jugar["colors"][2])