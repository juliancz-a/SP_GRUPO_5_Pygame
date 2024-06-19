import pygame
import sys
from class_box import Box
from class_menu import Menu
from class_play import Play

boxes_menu = [{"colors": ["gray77", "gray85", "gray85"], "coords": (150,150), "size" : (300,300), "border_width" : 0, "text" : None},
            {"colors": ["gray77", "gray85", "gray85"], "coords": (500,300), "size" : (200,100), "border_width" : 0, "text" : None},
            {"colors": ["gray77", "gray85", "gray85"], "coords": (100,300), "size" : (200,100), "border_width" : 0, "text" : None}]


class Game:

    def __init__(self, size, title, icon:str) -> None:

        pygame.init()

        self.surface = pygame.display.set_mode((size))
        self.window = Menu(self.surface)

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
                self.window = Menu(self.surface)
            case "play":   
                self.window = Play(self.surface)
            # case "options":
            #     self.window = Options(self.surface)
            # case "scoreboard":
            #     self.window = Scoreboard(self.surface)



juego = Game((800,600), "a jugar ", r"code\data\img\image.png")
juego.run()

