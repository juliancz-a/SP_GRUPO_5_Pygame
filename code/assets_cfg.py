from constantes import *
from class_box import Box

# MENU WINDOW ASSETS


quit_button = {
              "box": Box((100,540), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Salir", LETRAS_2, FUENTE_1, 60, True, 1, BORDE_2, True]
              }

play_button = {
              "box": Box((100,300), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Jugar", LETRAS_2, FUENTE_1, 60, True, 1, BORDE_2, True]
              }

help_button = {
              "box": Box((100,420), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Cómo jugar", LETRAS_2, FUENTE_1, 50, True, 1, BORDE_2, True]
              }

MENU_LISTA = [play_button, help_button, quit_button]


# PLAY WINDOW ASSETS

back_button = {"box": Box((1160,650), (100,50)),
                     "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
                     "config": [5, 5],
                     "text": ["Volver al menú", "white", FUENTE_1, 40, True]}

clear_button = {
              "box": Box((200, 200), (80, 50)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["CLEAR", "white", FUENTE_1, 40, True]
            }

shuffle_buton = {
              "box": Box((200, 200), (80, 50)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["CLEAR", "white", FUENTE_1, 40, True]
            }

PLAY_LISTA = [back_button, clear_button, shuffle_buton]

finish_continue = {"box": Box( (213, 360), (400,150)),
                   "colors": ["violetred3", BORDE_BOX, "violetred4"],
                   "config": [],
                   "text": ["Continuar", "white", FUENTE_1, True, 60, True, 2]}


FINISH_MATCH_LISTA = []
