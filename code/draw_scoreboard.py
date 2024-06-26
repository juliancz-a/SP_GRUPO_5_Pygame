import pygame
from constantes import *

class Scoreboard_2:
    def __init__(self, font, surface, player_list:list[dict]) -> None:
        self.surface = surface
        self.player_list = player_list
        self.draw_pos = (800,40)

        self.font = pygame.font.Font(font)
    def draw (self):
        x = self.draw_pos[0]
        y = self.draw_pos[1]
        
        Scoreboard_2.draw_header(self.surface, ["NOMBRE", "PUNTAJE", "PARTIDAS"], self.font, (800, 20))
        
        for player in self.player_list:
            player_name = self.font.render(player["nombre"], True, "black")
            player_points = self.font.render(str(player["puntos"]), True, "black")
            player_matches = self.font.render(str(player["partidas"]), True, "black")
            self.surface.blit(player_name, (x,y))
            x += 100
            self.surface.blit(player_points, (x,y))
            x += 100
            self.surface.blit(player_matches, (x,y))
            x = 800
            y += 10
    
    def draw_header (surface:pygame.Surface, headers:list[str], font, initial_pos:tuple):
        x = initial_pos[0]
        y = initial_pos[1]

        for header in headers:
            header_text = font.render(header, True, "black")
            surface.blit(header_text, (x,y))

            x += len(header) + 100