import pygame
import sys
from constantes import * 

from class_menu import Menu
from class_play import Play
from class_finish_match import FinishMatch
from class_scoreboard import Scoreboard

import random 
from data.config.config import *

lista_jugadores = []
lista_palabras = read_data(r"code\data\config\palabras.json")
lista_jugadores = read_score(r"code\data\config\scoreboard.csv", lista_jugadores)

class Game:

    def __init__(self, size, title, icon:str, lista_palabras:list, lista_jugadores:list) -> None:

        pygame.init()

        self.surface = pygame.display.set_mode((size), pygame.RESIZABLE)

        self.lista_jugadores = lista_jugadores
        self.lista_palabras = lista_palabras
        self.window = Menu(self.surface, self.lista_palabras, self.lista_jugadores, music_file = MENU_MUSIC)

        self.match = 0
        self.score = 0

        pygame.display.set_caption(title)

        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)

    def run(self):
        
        while True:
            game_state = self.window.render()
            if game_state is False:
                break
            Game.update_window(self, game_state)
            
    def update_window(self, game_state):
        match game_state:

            case "menu":
                self.window = Menu( self.surface, self.lista_palabras, self.lista_jugadores, music_file= MENU_MUSIC)
            case "play":   
                self.window = Play( self.surface, self.match,  self.lista_palabras, self.score, music_file= PLAY_MUSIC)
            case "finish_match":
                data_updated = self.window.update(self.match, self.score, self.lista_jugadores)
                self.match = data_updated[0] 
                self.score = data_updated[1] 
                self.lista_jugadores = data_updated[2]
                self.window = FinishMatch(self.surface, self.match,  self.lista_palabras, self.score)
            case "scoreboard":
                self.window = Scoreboard(self.surface, self.match , self.score, self.lista_jugadores)
            # case "options":
            #     self.window = Options(self.surface)



juego = Game((1280,720), "POP THE CARD", ICON, lista_palabras, lista_jugadores)
juego.run()


