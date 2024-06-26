import pygame
from constantes import *

class Scoreboard_2:
    def __init__(self, font, surface, player_list:list[dict]) -> None:
        self.surface = surface
        self.player_list = player_list
        self.draw_pos = (800,40)

        self.font = pygame.font.Font(font, 20)
     
    def draw (self):
        y = self.draw_pos[1]
        
        header_pos = Scoreboard_2.draw_header(self.surface, ["nombre", "puntos", "partidas"], self.font,(800, 20))
        
        for player in self.player_list:
            y += 50
            for header in header_pos:

                for key,value in header.items():
                    header_data = self.font.render(str(player[key]), True, "black")
                    self.surface.blit(header_data, (value, y))

            # player_name = self.font.render(player["nombre"], True, "black")
            # player_points = self.font.render(str(player["puntos"]), True, "black")
            # player_matches = self.font.render(str(player["partidas"]), True, "black")
            # self.surface.blit(player_name, (x,y))
            # x += 100
            # self.surface.blit(player_points, (x,y))
            # x += 100
            # self.surface.blit(player_matches, (x,y))
            # x = 800
            # y += 10
    
    def draw_header (surface:pygame.Surface, header_elements:list[str], font, initial_pos:tuple) -> list:
        x = initial_pos[0]
        y = initial_pos[1]
        header_pos = []

        for header in header_elements:
            header_text = font.render(header, True, "black")
            surface.blit(header_text, (x,y))

            header_pos.append({header: x})

            x += len(header) + 110
       
        return header_pos