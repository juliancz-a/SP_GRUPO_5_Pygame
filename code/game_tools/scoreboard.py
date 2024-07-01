import pygame
from constantes import *

class Scoreboard:
    def __init__(self, font:pygame.font, surface:pygame.Surface, player_list:list[dict]) -> None:
        self.surface = surface
        self.player_list = player_list
        self.draw_pos = (850,200)

        self.header = ["nombre", "puntos", "partidas"]

        self.font = pygame.font.Font(font, 18)
     
    def draw (self):
        y = self.draw_pos[1]
        if len(self.player_list) == 0:
            self.header = ["No se han registrado jugadores aún"]
        header_data = Scoreboard.draw_header(self.surface, self.header, self.font,(850, 220))
        
        for i in range(len(self.player_list)):
            y += 50
            if i < 7:
                
                for header in header_data:

                    for key,value in header.items():
                        player_data = self.font.render(str(self.player_list[i][key]), True, "white")
                        self.surface.blit(player_data, (value, y))
    
    def draw_header (surface:pygame.Surface, header_elements:list[str], font, initial_pos:tuple) -> list:
        x = initial_pos[0]
        y = initial_pos[1]
        header_data = []

        for header in header_elements:
            header_text = font.render(header.upper(), True, "yellow")
            surface.blit(header_text, (x,y))

            header_data.append({header: x})

            x += len(header) + 110
       
        return header_data