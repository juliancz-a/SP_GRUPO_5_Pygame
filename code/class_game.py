import pygame
import sys
from constantes import * 
from class_box import Box
from class_menu import Menu
from class_play import Play

class Game:

    def __init__(self, size, title, icon:str) -> None:

        pygame.init()

        self.surface_size = size
        self.surface = pygame.display.set_mode((self.surface_size), pygame.RESIZABLE)

        self.window = Menu(size, self.surface, music_file = MENU_MUSIC)

        pygame.display.set_caption(title)

        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)

    def run(self):
        
        while True:
            game_state = self.window.render()
            if game_state[0] is False:
                break

            info = pygame.display.Info()
            self.surface_size = info.current_w, info.current_h
            print(self.surface_size)
            print(self.surface)
            Game.update_window(self, game_state[1], game_state[0])


    def update_window(self, wh, game_state):
        match game_state:

            case "menu":
                self.window = Menu(wh, self.surface, music_file= MENU_MUSIC)
            case "play":   
                self.window = Play(wh, self.surface, music_file= PLAY_MUSIC)
            # case "options":
            #     self.window = Options(self.surface)
            # case "scoreboard":
            #     self.window = Scoreboard(self.surface)



juego = Game((1280,720), "POP THE CARD", r"code\data\img\image.png")
juego.run()

