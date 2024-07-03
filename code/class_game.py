import pygame
import sys
from constantes import * 

from game_states.class_menu import Menu
from game_states.class_play import Play
from game_states.class_finish_match import FinishMatch
from game_states.class_setscore import SetScore
from game_states.class_help import Help
from game_tools.words import *

import random 
from data.config.config import *

class Game:

    def __init__(self, size, title, icon:str, lista_palabras:list, lista_jugadores:list, game_assets:dict) -> None:

        pygame.init()

        self.match = 0
        self.score = 0
        self.volume = True
        self.comodin = 1

        self.surface = pygame.display.set_mode((size))
        self.game_assets = game_assets
        self.lista_jugadores = lista_jugadores
        self.lista_palabras = lista_palabras
        
        self.window = Menu(self.surface, self.lista_jugadores, self.game_assets["menu"], self.volume)

        self.quit = False

        pygame.display.set_caption(title)
        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)
    
    def get_events (self):
        """Obtención de eventos y manejo de los mismos según la escena actual del videojuego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            self.window.handle_event(event)
        
    def run(self):
        """Ciclo de ejecución del juego. Se obtienen eventos, se renderizan elementos, se actualizan datos."""
        while self.quit is False:

            self.get_events()
            self.window.render()
            self.volume = self.window.update_audio()

            game_state = self.window.update()
            if game_state == "quit":
                self.quit = True

            Game.update_window(self, game_state)
            
    def update_window(self, game_state:str):
        """Actualización de la escena del juego.
        Args:
            game_state (str): Estado nuevo del juego. Será la nueva escena del juego.
        """
        match game_state:

            case "menu":
                self.lista_palabras = read_data(r"code\data\config\palabras.json")
                self.match = 0
                self.score = 0

                self.window = Menu(self.surface, self.lista_jugadores, self.game_assets["menu"], self.volume)

            case "help":
                self.window = Help(self.surface, self.game_assets["help"], self.volume)

            case "play":
                datos_palabras = set_combination(self.lista_palabras)
                self.window = Play(self.surface, self.match, datos_palabras , self.score, self.comodin,  self.game_assets["play"], self.volume)

            case "finish_match":
                
                data_updated = self.window.update_play_instance()
                self.match = data_updated[0] 
                self.score = data_updated[1]
                
                self.window = FinishMatch(self.surface, self.match, self.score, self.game_assets["finish_match"], self.volume)

            case "setscore":
                self.window = SetScore(self.surface, self.match , self.score, self.lista_jugadores, self.game_assets["set_score"], self.volume)