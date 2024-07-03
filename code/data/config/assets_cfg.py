from constantes import *
from game_tools.class_box import Box
from game_tools.class_image import Image

# MENU SCENE ASSETS

quit_button = {
              "box": Box((100,540), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Salir", LETRAS_2, FUENTE_1, 60, "shadow", 2, BORDE_2, True],
              "interaction" : True
              }

play_button = {
              "box": Box((100,300), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Jugar", LETRAS_2, FUENTE_1, 60, "shadow", 2, BORDE_2, True],
              "interaction" : True
              }

help_button = {
              "box": Box((100,420), (210,95), press_sound=PRESS_SOUND),
              "colors": [COLOR_BOX, BORDE_BOX, HOVER_BOX],
              "config": [15, 5],
              "text": ["Cómo jugar", LETRAS_2, FUENTE_1, 50, "shadow", 2, BORDE_2, True],
              "interaction" : True
              }

menu_volume_button = {
                "image" : Image(VOLUME_BUTTON, (10, 10), (60,60)),
                "interaction" : False
}

menu_title = {
              "box": Box((200,100), (400,50)),
              "colors" : [],
              "config" : [],
              "text" :  ["Pop The Card", COLOR_LETRAS, FUENTE_1, 80, "border", 
                        2, TITULO, True],
              "interaction" : False
              }

menu_background = {
                "image" : Image(MENU_BACKGROUND, (0,0), (1280,720)),
                "interaction" : False
                }
menu_chains = {
                "image" : Image(CHAINS, (130, 320), (150, 270)),
                "interaction" : False}

MENU_ASSETS = [play_button, help_button, quit_button, menu_title, menu_volume_button, 
               menu_background, menu_chains]


# PLAY SCENE ASSETS
back_button = {"box": Box((1160,650), (100,50)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["Volver al menú", "white", FUENTE_1, 40, "shadow", 
                        1, "black", True]
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

join_button = {"box": Box((750,390), (160,70)),
               "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
               "config" : [],
               "text" : []
               }

timer = {"box": Box((640, 420), (50,50)),
        "colors": [],
        "config" : [],
        "text" : []
        }

score_text = {"box": Box((400, 420), (100,50)),
            "colors": [],
            "config" : [],
            "text" : []
            }

comodin_button = {"image" : Image(COMODIN, (1070, 220), (100,100), 
                                image_hover_path = COMODIN_HOVER, 
                                press_sound = PRESS_COMODIN_SOUND)
                }

volume_button = {"image" : Image(VOLUME_BUTTON, (10, 10), (60,60))}

play_background = {"image" : Image(PLAY_BACKGROUND_1, (0,0), (1280,720))}


PLAY_ASSETS = [back_button, clear_button, shuffle_buton, join_button, timer, 
               score_text, comodin_button, volume_button, play_background]



#FINISH MATCH SCENE ASSETS
continue_button = {
                  "box": Box((640, 360), (400,150)),
                  "colors": ["violetred3", "violetred4", "violetred4"],
                  "config": [1,1],
                  "text": ["Seguir jugando", "white", FUENTE_1, 30, "border", 
                           2, "black", True]
                  }

finish_button = {
                  "box": Box( (213, 360), (400,150)),
                  "colors": ["violetred3", "violetred4", "violetred4"],
                  "config": [],
                  "text": []
                  }

score_text = {"box" : Box((230, 100), (400,150)),
              "colors": [],
              "config" : [],
              "text" : []}

volume_button = {"image" : Image(VOLUME_BUTTON, (10, 10), (60,60))}

finish_match_bg = {"image" : Image(FINISH_MATCH_BACKGROUND, (0,0), (1280,720))}

FINISH_MATCH_ASSETS = [continue_button, finish_button, score_text, volume_button, 
                       finish_match_bg]


#SET SCORE SCENE ASSETS
input_box = {
            "box" : Box((500, 500), (275,50)),
            "colors" : ["white", "grey66", "grey1"],
            "config" : [5, 5],
            "text" : [],
            "interaction" : False
                }

submit_button = {"box" :  Box((500, 575), (275,50)),
                "colors" : ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
                "config" : [],
                "text" : [],
                "interaction" : False}

game_over_title = {
            "box" :  Box((0, 20), (400,150)),
            "colors" : [],
            "config" : [],
            "text" : ["Registra tu nombre", "white", FUENTE_1, 60, "border", 2, 
                      "grey55", True],
            "interaction" : False
}

nickname  = {
            "box" :  Box((505,502), (200,20)),
            "colors" : [],
            "config" : [],
            "text" : [],
            "interaction" : False}

volume_button = {"image" : Image(VOLUME_BUTTON, (10, 10), (60,60))}

set_score_bg = {"image" : Image(SET_SCORE_BACKGROUND, (0,0), (1280,720))}
REGISTER_SCORE_ASSETS = [input_box, submit_button, game_over_title, nickname, 
                         volume_button, set_score_bg]

#HELP SCENE ASSETS
back_button = {"box": Box((1110,600), (150,100)),
              "colors": ["mediumpurple4", "mediumpurple3", "mediumpurple3"],
              "config": [5, 5],
              "text": ["Volver al menú", "white", FUENTE_1, 40, "shadow", 1, "black", True],
              "interaction" : True
              }
comodin_img = {"image" : Image (COMODIN, (580, 505), (100, 100)),
               "interaction" : False
               }

shuffle_img = {"image" : Image (r"code\data\img\shuffle_button.png", (400, 500), (160, 100)),
                "interaction" : False
               }

clear_img = {"image" : Image (r"code\data\img\clear_button.png", (690, 500), (160, 100)),
              "interaction" : False}

volume_button = {"image" : Image(VOLUME_BUTTON, (10, 650), (60,60)),
                 "interaction" : False}

help_background = {"image" : Image(HELP_BACKGROUND, (0,0), (1280,720)),
               "interaction" : False}

HELP_ASSETS = [back_button, comodin_img, shuffle_img, clear_img, 
               volume_button, help_background]


#ALL GAME ASSETS
game_assets = {
    "menu" : MENU_ASSETS,
    "play" : PLAY_ASSETS,
    "finish_match" : FINISH_MATCH_ASSETS,
    "set_score" : REGISTER_SCORE_ASSETS,
    "help" : HELP_ASSETS
}