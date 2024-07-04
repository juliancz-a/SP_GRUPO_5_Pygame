from class_game import *
from data.config.assets_cfg import game_assets
from game_tools.extra_functions import *

lista_jugadores = []
lista_palabras = read_data(r"code\data\config\palabras")
lista_jugadores = read_score(r"code\data\config\scoreboard", lista_jugadores)
if len(lista_jugadores) > 0:
    ordenar_elementos(lista_jugadores, 2, "puntos")

juego = Game((1280,720), "POP THE CARD", ICON, lista_palabras, lista_jugadores,
            game_assets)

juego.run()