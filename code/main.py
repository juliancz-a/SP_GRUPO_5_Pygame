from class_game import *
from data.config.assets_cfg import game_assets

lista_jugadores = []
lista_palabras = read_data(r"code\data\config\palabras.json")
lista_jugadores = read_score(r"code\data\config\scoreboard.csv", lista_jugadores)

juego = Game((1280,720), "POP THE CARD", ICON, lista_palabras, lista_jugadores, game_assets)
juego.run()