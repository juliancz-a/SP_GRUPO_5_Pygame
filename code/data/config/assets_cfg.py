from constantes import *
from game_tools.class_box import Box

# MENU WINDOW ASSETS


quit_button = {
              "box": Box((100,540), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Salir", LETRAS_2, FUENTE_1, 60, "shadow", 1, BORDE_2, True],
              "interaction" : True
              }

play_button = {
              "box": Box((100,300), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Jugar", LETRAS_2, FUENTE_1, 60, "shadow", 1, BORDE_2, True],
              "interaction" : True
              }

help_button = {
              "box": Box((100,420), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Cómo jugar", LETRAS_2, FUENTE_1, 50, "shadow", 1, BORDE_2, True],
              "interaction" : True
              }

menu_title = {
              "box": Box((200,100), (400,50)),
              "colors" : [],
              "config" : [],
              "text" :  ["Pop The Card", COLOR_LETRAS, FUENTE_1, 80, "border", 2, TITULO, True],
              "interaction" : False
              }

MENU_ASSETS = [play_button, help_button, quit_button, menu_title]


# PLAY WINDOW ASSETS
join_button = {"box": Box((750,390), (160,70)),
               "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
               "config" : [5, 5],
               "text" : ["¡Unir!", "white", FUENTE_1, 40, True]
               }

back_button = {"box": Box((1160,650), (100,50)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["Volver al menú", "white", FUENTE_1, 40, "shadow", 1, "black", True]
              }

clear_button = {
              "box": Box((160, 110), (120, 70)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["CLEAR", "white", FUENTE_1, 50, "shadow", 1, "black", True]
              }

shuffle_buton = {
              "box": Box((160, 210), (120, 70)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["SHUFFLE", "white", FUENTE_1, 50, "shadow", 1, "black", True],
              }



PLAY_ASSETS = [back_button, clear_button, shuffle_buton]

continue_button = {
                  "box": Box((640, 360), (400,150)),
                  "colors": ["violetred3", "violetred4", "violetred4"],
                  "config": [],
                  "text": ["Seguir jugando", "white", FUENTE_1, 30, "border", 2, "black", True]
                  }

finish_button = {
                  "box": Box( (213, 360), (400,150)),
                  "colors": ["violetred3", "violetred4", "violetred4"],
                  "config": [],
                  "text": ["Definir puntaje", "white", FUENTE_1, 40, "border", 2, "black", True]
                  }

FINISH_MATCH_ASSETS = [continue_button, finish_button]

input_box = {
            "box" : Box((650, 500), (275,50)),
            "colors" : ["white", "red", "grey1"],
            "config" : [5, 5],
            "text" : [],
            "interaction" : True
                }

game_over_title = {
            "box" :  Box((230, 20), (400,150)),
            "colors" : [],
            "config" : [],
            "text" : ["Registra tu nombre", "white", FUENTE_1, 60, "border", 2, "grey55", True],
            "interaction" : False
    
}
REGISTER_SCORE_ASSETS = [input_box, game_over_title]


back_button = {"box": Box((1110,600), (150,100)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["Volver al menú", "white", FUENTE_1, 40, "shadow", 1, "black", True],
              "interaction" : True
              }

HELP_ASSETS = [back_button]