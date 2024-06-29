import pygame
import sys
from constantes import * 

from class_menu import Menu
from class_play import Play
from class_finish_match import FinishMatch
from class_setscore import SetScore

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
        self.window = Menu(self.surface, self.lista_jugadores)

        self.match = 0
        self.score = 0
        self.comodin = 1

        self.quit = False

        pygame.display.set_caption(title)
        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)
    
    def get_events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            self.window.handle_event(event)
        
    def run(self):

        self.window.set_music()
        
        while self.quit is False:
            self.get_events()
            self.window.render()

            game_state = self.window.update()
            if game_state == "quit":
                self.quit = True

            Game.update_window(self, game_state)
            
    def update_window(self, game_state):
        match game_state:

            case "menu":
                self.match = 0
                self.score = 0

                self.window = Menu(self.surface, self.lista_jugadores)

            case "play":   
                self.window = Play(self.surface, self.match,  self.lista_palabras, self.score, self.comodin, music_file= PLAY_MUSIC)

            case "finish_match":
                
                data_updated = self.window.update_play_instance()
                self.match = data_updated[0] 
                self.score = data_updated[1]
                
                self.window = FinishMatch(self.surface, self.match,  self.lista_palabras, self.score)

            case "setscore":
                self.window = SetScore(self.surface, self.match , self.score, self.lista_jugadores)



juego = Game((1280,720), "POP THE CARD", ICON, lista_palabras, lista_jugadores)
juego.run()

